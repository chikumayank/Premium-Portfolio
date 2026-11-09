#!/usr/bin/env python3
"""Recipe roll: pick a fresh, non-repeating creative recipe for the next video.

Reads the creative libraries (references/libraries.md, effects-library.md, creator-edit-styles.md)
and the creator's content log (markdown table, newest row first), removes recently used choices
according to the freshness rules, and prints one or more recipe cards.

Usage:
  python3 recipe_roll.py --log ../../../creator/content-log.md
  python3 recipe_roll.py --log LOG --count 3 --seed 7
  python3 recipe_roll.py --log LOG --series "NRI Desk"      # keep the series look, rotate the rest
  python3 recipe_roll.py --formats F06,F22,F29              # restrict the pool
"""
import argparse
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REFS = HERE.parent / "references"

# dimension -> (library prefix, log column names, exclusion rule)
#   rule ("last", n)  : exclude anything used in the last n posts
#   rule ("max", n, k): exclude anything used >= k times in the last n posts, plus the immediately previous one
#   rule ("streak", n): exclude a value only if it was used in each of the last n posts
DIMENSIONS = {
    "Format": ("F", ["format"], ("max", 7, 2)),
    "Creator edit style": ("ES", ["notes", "edit style", "creator edit style"], ("last", 1)),
    "Hook archetype": ("H", ["hook archetype", "hook"], ("last", 5)),
    "Story structure": ("S", ["story structure", "structure"], ("last", 3)),
    "Edit pace": ("P", ["edit pace", "pace"], ("streak", 2)),
    "Transition style": ("T", ["transition style", "transition"], ("last", 3)),
    "Effect families": ("E", ["effects", "effect families"], ("last", 1)),
    "Font style (Edits)": ("EF", ["font pairing", "font", "font style"], ("last", 4)),
    "Font pairing (covers)": ("FP", ["font pairing", "font", "cover font"], ("last", 4)),
    "Caption style": ("C", ["caption style", "caption", "captions"], ("last", 3)),
    "Grade": ("G", ["grade"], ("last", 4)),
    "Music mood": ("M", ["music mood", "music"], ("last", 3)),
    "Camera style": ("CS", ["camera style", "camera"], ("last", 3)),
}
SERIES_LOCKED = ["Creator edit style", "Font style (Edits)", "Font pairing (covers)", "Caption style", "Grade", "Camera style"]
EFFECT_FAMILIES = {
    "ZOOM": "Zoom & camera motion", "TIME": "Speed & time", "TRANS": "Transitions",
    "TEXT": "Text animation", "VFX": "VFX & cutouts", "STYLE": "Film & texture",
    "INFO": "Information graphics", "NEWS": "News effects", "BEAT": "Beat & rhythm",
}
EDITS_FONTS = {
    "EF1": "Bold condensed", "EF2": "Elegant serif", "EF3": "Clean modern sans",
    "EF4": "Typewriter / mono", "EF5": "Handwritten / marker",
}


def id_regex(prefix):
    # CS must not be confused with C, ES with E, FP with F, EF with E/F.
    return re.compile(r"(?<![A-Z-])" + prefix + r"(\d{1,2})(?![\d])")


def parse_library_sections(text):
    """Return {prefix: {id: name}} from '## N. Title (PREFIX)' sections."""
    out = {}
    for m in re.finditer(r"^## \d+\.\s+(.+?)\(([A-Z]+)\)\s*$", text, re.M):
        prefix = m.group(2)
        start = m.end()
        nxt = re.search(r"^## ", text[start:], re.M)
        body = text[start: start + nxt.start()] if nxt else text[start:]
        items = {}
        for row in re.finditer(r"^\|\s*(" + prefix + r"\d+)\s*\|\s*([^|]+)\|", body, re.M):
            items[row.group(1)] = row.group(2).strip()
        if not items:  # inline "M01 lo-fi chill · M02 ..."
            for chunk in re.split(r"·|\n", body):
                im = re.match(r"\s*(" + prefix + r"\d+)\s+(.+)", chunk)
                if im:
                    items[im.group(1)] = im.group(2).strip()
        out[prefix] = items
    return out


def parse_edit_styles(text):
    return {m.group(1): m.group(2).strip().strip("*")
            for m in re.finditer(r"^\|\s*(ES\d+)\s*\|\s*([^|]+)\|", text, re.M)}


def parse_log(path):
    """Return a list of row dicts (lowercased headers), newest first, skipping empty rows."""
    if not path or not Path(path).exists():
        return []
    lines = [l for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip().startswith("|")]
    if len(lines) < 2:
        return []
    header = [h.strip().lower() for h in lines[0].strip().strip("|").split("|")]
    rows = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not any(cells):
            continue
        rows.append(dict(zip(header, cells + [""] * (len(header) - len(cells)))))
    return rows


def values_in(row, columns, prefix):
    found = []
    for col in columns:
        cell = row.get(col, "")
        if not cell:
            continue
        if prefix == "E":
            found += re.findall(r"E-([A-Z]+)-\d+", cell)
            found += [f for f in EFFECT_FAMILIES if re.search(r"\b" + f + r"\b", cell)]
        else:
            found += [prefix + n.zfill(2 if prefix not in ("EF",) else 1) for n in id_regex(prefix).findall(cell)]
    return sorted(set(found))


def excluded(rows, prefix, columns, rule):
    history = [values_in(r, columns, prefix) for r in rows]
    kind = rule[0]
    if kind == "last":
        return {v for h in history[: rule[1]] for v in h}
    if kind == "max":
        window, limit = rule[1], rule[2]
        counts = {}
        for h in history[:window]:
            for v in h:
                counts[v] = counts.get(v, 0) + 1
        ex = {v for v, c in counts.items() if c >= limit}
        if history:
            ex |= set(history[0])
        return ex
    if kind == "streak":
        n = rule[1]
        if len(history) < n:
            return set()
        common = set(history[0])
        for h in history[1:n]:
            common &= set(h)
        return common
    return set()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--log", help="path to content-log.md")
    ap.add_argument("--count", type=int, default=1, help="number of alternative recipes")
    ap.add_argument("--seed", type=int, help="random seed for reproducible rolls")
    ap.add_argument("--series", help="series name: keep that series' look (from SERIES:<name> rows)")
    ap.add_argument("--formats", help="comma-separated allowed format IDs (e.g. from the brand profile)")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    lib = parse_library_sections((REFS / "libraries.md").read_text(encoding="utf-8"))
    lib["ES"] = parse_edit_styles((REFS / "creator-edit-styles.md").read_text(encoding="utf-8"))
    lib["E"] = dict(EFFECT_FAMILIES)
    lib["EF"] = dict(EDITS_FONTS)
    if args.formats:
        allowed = {f.strip().upper() for f in args.formats.split(",")}
        lib["F"] = {k: v for k, v in lib["F"].items() if k in allowed} or lib["F"]

    rows = parse_log(args.log)
    series_row = None
    if args.series:
        tag = "series:" + args.series.lower()
        series_row = next((r for r in rows if tag in r.get("notes", "").lower()), None)
        if series_row is None:
            print(f"(No previous post tagged SERIES:{args.series}; rolling a fresh look that will define the series.)\n")

    print(f"Posts in log considered: {len(rows)}\n")
    for i in range(args.count):
        print(f"### Recipe {i + 1}" if args.count > 1 else "### Recipe")
        print("| Dimension | Pick | Excluded (recently used) |")
        print("|---|---|---|")
        for dim, (prefix, cols, rule) in DIMENSIONS.items():
            pool = lib.get(prefix, {})
            if not pool:
                continue
            if series_row is not None and dim in SERIES_LOCKED:
                locked = values_in(series_row, cols, prefix)
                if locked:
                    names = ", ".join(f"{v} {pool.get(v, '')}".strip() for v in locked)
                    print(f"| {dim} | {names} (series lock) | n/a |")
                    continue
            ex = excluded(rows, prefix, cols, rule)
            choices = [k for k in pool if k not in ex] or list(pool)
            k = 2 if prefix == "E" else 1
            picks = rng.sample(choices, min(k, len(choices)))
            pick_txt = " + ".join(f"{p} {pool[p]}" for p in picks)
            print(f"| {dim} | {pick_txt} | {', '.join(sorted(ex)) or 'none'} |")
        print()
    print("Next: sanity-check the roll against the topic's mood. Swap any pick that fights the message, but keep it outside the excluded list.")


if __name__ == "__main__":
    sys.exit(main())

# Freshness Engine (AUDIT)

## Repeat rules (the defaults; the creator's log can override them)
| Dimension | Rule |
|---|---|
| Format (F) | Not twice in a row; at most 2 in any 7 posts |
| Hook archetype (H) | Not repeated within 5 posts |
| Story structure (S) | Not repeated within 3 posts |
| Edit pace (P) | Not the same 3 times in a row |
| Transition style (T) | Not repeated within 3 posts |
| Primary effect families | Not the same main family twice in a row |
| Font style or pairing (EF/FP) | Not repeated within 4 posts (anchor excluded) |
| Caption style (C) | Not repeated within 3 posts |
| Grade (G) | Not repeated within 4 posts |
| Music mood (M) | Not repeated within 3 posts |
| Camera style (CS) | Not repeated within 3 posts |
| Creator edit style (ES) | Not the same primary style twice in a row |
| Language | Across 10 posts: at least 2 English-only and 2 Hindi-only |
| Opening line / CTA wording | No identical opening words within 10 posts; vary CTA verbs |
**Series exception:** posts marked `SERIES:<name>` may keep their look consistent (that's the point of a series). Rotate everything else.

## Mode A: Log a post
Add a row at the top of `creator/content-log.md` with IDs for every column; ask only for what's missing; leave metrics blank.

## Mode B: Audit
1. Read the last N rows (default 10) plus any planned posts. If there's no log, ask for descriptions, captions or screenshots.
2. **Sameness heatmap:**
   | Dimension | Distinct / posts | Most repeated | Status |
   🟢 ≥ 60% distinct · 🟡 30–59% · 🔴 < 30%.
3. List rule violations.
4. **Verbal tics:** repeated phrases across captions or scripts (e.g. "guys", "literally", the same CTA).
5. **Prescription:** for each 🔴/🟡, give concrete swaps for the next 3 posts ("Next formats: F16, F22, F12").
6. **Keep list:** what's working and should stay (the signature, the anchor, a performing series). Only unplanned repetition is the problem.

## Recipe roll (automated)
`scripts/recipe_roll.py` reads `references/libraries.md` and the content log, removes recently used IDs per the rules above and picks a
fresh combination. Options: `--seed N` for reproducibility, `--count 3` for 3 alternatives, `--series NAME` to lock the look for a series.
If code can't run, do the same selection by hand and show which IDs were excluded and why.

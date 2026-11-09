---
name: freshness-audit
description: Audits planned or recent content for sameness (repeated formats, hooks, structures, fonts, grades, transitions, music, camera styles, topics, and phrases) and prescribes specific swaps. Also logs new posts into creator/content-log.md. Use when the user asks "am I getting repetitive", "why does my content feel boring", "check my plan", "review my last 10 reels", or "log this post".
---

# Freshness Audit

## Mode A: Log a post
When the user describes a published post, add a row at the top of `creator/content-log.md`, filling every
column it can (IDs from `creator/libraries.md`) and asking only for what's missing. Leave metrics blank
for `performance-review` to fill later.

## Mode B: Audit
1. Read the last 10 (or user-specified N) rows of `creator/content-log.md`, plus any planned posts.
   If the log is empty, ask the user to describe their last 6–10 posts or paste captions, links or screenshots.
2. **Sameness heatmap:** for each dimension (pillar, format, hook, structure, pace, transition, font pairing,
   caption style, grade, music, camera, length, opening line, CTA), count how many distinct values were used
   and identify the most repeated one.

   | Dimension | Distinct used / posts | Most repeated | Status |
   |---|---|---|---|
   | Format | 2/10 | F01 talking head ×8 | 🔴 stale |

   Status: 🟢 ≥ 60% distinct · 🟡 30–59% · 🔴 < 30%. Series marked `SERIES:` are excluded.
3. **Check repeat-rule violations** from the content log rules.
4. **Verbal tics:** find repeated phrases across captions or scripts ("guys", "literally", the same CTA).
5. **Prescription:** for each 🔴 and 🟡, give a concrete swap for the next 3 posts, e.g.
   "Next 3 formats: F16 mini-doc, F22 split-screen, F12 process-ASMR".
6. **Keep list:** what's working and should stay consistent (the signature element, the anchor font, a
   series that's performing). Not all consistency is bad. Only unplanned repetition is.

## Output
The heatmap, the violations, the prescriptions, the keep list, and a one-line verdict.

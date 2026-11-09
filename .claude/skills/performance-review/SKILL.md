---
name: performance-review
description: Reviews Instagram and YouTube analytics (views, reach, average watch %, retention graph drop-offs, skip rate, saves, shares, comments, follows, CTR, AVD) against the creative choices logged in creator/content-log.md, finds what actually drives results, and designs the next experiments. Use when the user shares analytics, screenshots or numbers, asks "why did this flop/go viral", "what's working", or wants a weekly or monthly review.
---

# Performance Review

## Inputs
Numbers or screenshots from Instagram Insights / Professional Dashboard and YouTube Studio, and
`creator/content-log.md`. Update the log's metric columns with whatever the user provides.

## Process
1. **Normalise:** compare posts by ratios, not raw views:
   - Hold: % still watching at 3s (short-form) or 30s (long-form)
   - Avg % watched / average view duration
   - Shares per 1k views (reach signal) and saves per 1k views (value signal)
   - Follows per 1k views (conversion)
   - Long-form: impressions CTR, and retention dips at the timestamps where viewers leave
2. **Diagnose each post** in one line:
   - Low 3s hold → hook problem (re-run `hook-lab`)
   - Good hold but low avg % → middle sags (tighten pacing, add re-hooks)
   - High watch, low shares → useful but not relatable or surprising
   - High shares, low follows → unclear who you are (check the `creator-dna` positioning)
3. **Pattern-find across the log:** group by format, hook archetype, structure, pace, grade and length. Point out
   which choices are correlated with better ratios. Be honest about small samples (fewer than 3 posts per group means it's a hint, not proof).
4. **Experiments for next week:** 2–3 tests, each changing **one** variable, with a hypothesis and a success metric
   ("Test H03 result-first vs H01 contrarian on the same topic; success = 3s hold > 70%").
5. **Keep / Kill / Try** summary.

## Rules
- Never tell the user to chase a trend that conflicts with their never-us list.
- Credit the creative choices, not luck, only when the data supports it.
- Remind the user that posting time matters less than hook and retention, and suggest testing rather than guessing.

# Creator Studio: Claude Skills for Reels, Shorts & Vlogs

A one-stop skill system for Instagram Reels, YouTube Shorts, YouTube vlogs and long-form video.
It is built around one rule: **no two posts in a row should look, sound or open the same way.**

## How it fights monotony

Most creators get repetitive because they decide everything from memory. Here, every
decision (hook type, format, font, colour, transition, music mood, camera angle,
pacing) is picked from a **library** and checked against the **content log**
(`creator/content-log.md`). Skills refuse to repeat a choice that was used in the
last few posts unless you ask for it.

```
creator-dna  ->  idea-engine  ->  hook-lab  ->  script-writer  ->  shot-planner
                                                                       |
performance-review  <-  freshness-audit  <-  repurpose  <-  type-and-color  <-  edit-recipe
        |                                                                ^
        +-------------------- creator/content-log.md --------------------+
```

## The skills (`.claude/skills/`)

| Skill | What it does | Say something like |
|---|---|---|
| `creator-dna` | Builds your brand profile: niche, pillars, voice, audience, visual identity, signature elements, and what's "never us" | "set up my creator profile" |
| `idea-engine` | Generates ideas across 25+ formats, scores them, rotates pillars and formats | "give me 10 reel ideas for this week" |
| `hook-lab` | Writes 3-second openers across 20 hook archetypes (verbal, visual, text, audio) | "hooks for my Goa vlog" |
| `script-writer` | Scripts for 15s/30s/60s/90s reels, shorts and 8–15 min vlogs, using varied story structures | "script this idea as a 45s reel" |
| `shot-planner` | Shot list, angles, b-roll, transitions-in-camera, location and light plan | "shot list for tomorrow's shoot" |
| `edit-recipe` | A unique edit plan for each video: pacing map, cuts, transitions, sound design, music mood, captions, effects | "edit recipe for this script" |
| `type-and-color` | Font pairings, caption styles, colour grades and text animation, rotated each post within your brand | "fonts and colours for this reel" |
| `repurpose` | Turns one vlog into shorts, reels, carousels, a community post and captions for each platform | "repurpose my vlog" |
| `freshness-audit` | Checks a plan or your last N posts for sameness and prescribes changes | "am I getting repetitive?" |
| `performance-review` | Reads your numbers (retention, saves, shares, CTR) and turns them into next experiments | "review last week's analytics" |

## Where to start (week 1)

1. **Day 1:** run `creator-dna`. Answer its questions honestly. This is the base everything else uses.
2. **Day 2:** run `idea-engine` and choose 5 ideas, each in a **different format**.
3. **Day 3:** run `hook-lab` → `script-writer` for the first 2 ideas.
4. **Day 4:** run `shot-planner`, then shoot both in one session.
5. **Day 5:** run `edit-recipe` + `type-and-color`, then edit.
6. **Day 6:** post, then log each post in `creator/content-log.md` (the skills can do this for you).
7. **Day 7:** run `freshness-audit` + `performance-review`.

Repeat each week. After 4 weeks, `performance-review` will have enough data to tell
you which experiments to keep.

## Files

- `creator/brand-profile.md`: your creator DNA (filled in by `creator-dna`)
- `creator/content-log.md`: every post and the choices behind it (the system's memory)
- `creator/libraries.md`: the shared libraries of formats, hooks, structures, transitions, fonts and grades

## Using these skills

Open this repo in Claude Code (CLI, desktop or claude.ai/code) and the skills in
`.claude/skills/` load automatically. To use them in the Claude app instead, zip a skill
folder and upload it under Settings → Capabilities → Skills.

---
name: creator-studio
description: A complete content-creation studio for Instagram Reels, YouTube Shorts, YouTube vlogs and long-form video, covering creator strategy and niche, idea generation, trend-jacking, hooks, scripting (Hindi/English/Hinglish), phone filming, editing, a 90+ effects library (transitions, text animations, VFX, green screen, cutouts, speed ramps, glitches, map and document effects), sound design, fonts and colour grading, current creator edit styles, news and finance explainers with compliance, captions, hashtags, SEO, posting, repurposing, freshness audits against repetitive content, analytics reviews and growth. Use it for anything about making social video content, e.g. "reel idea", "script this", "how do I edit this", "what effect should I use", "transition ideas", "my reels look the same", "fonts for reels", "what's trending", "news reel", "review my analytics", "content plan", "how do creators do X", or when the user shares a topic and wants a reel made.
---

# Creator Studio

A complete production studio in one skill. It takes the creator from an idea to a published, logged and reviewed video,
and it **makes sure no two videos look, sound or open the same way.**

## Core principles (apply to every answer)
1. **Viewer first:** every choice must serve one of these: *stop the scroll, keep watching, feel something, save, share, follow.*
2. **Have a system for variety:** pick every creative choice (format, hook, structure, pace, transitions, effects, font,
   caption style, grade, music, camera) from the libraries, check it against recent posts, and rotate it. Keep the brand
   anchors fixed (about 70% fixed, 30% fresh).
3. **Be specific:** give exact words, seconds, settings and steps. Never give generic advice like "be authentic" or "use trending audio".
4. **Work on a phone:** assume an Android phone and the Instagram Edits app unless the profile says otherwise. Give CapCut or other
   app steps as an alternative only when Edits can't do something.
5. **Be accurate and safe:** no invented facts or figures. Finance and news content follows `references/news-finance-compliance.md`.
6. **Match the creator's voice and language mix:** write Hinglish as people actually speak it (Roman script by default, Devanagari if asked).

## Memory: read these files first, if they exist
| File | What it is | If missing |
|---|---|---|
| `creator/brand-profile.md` | Niche, pillars, audience, voice, fixed identity, variable zone, never-us, gear, guardrails | Run **ONBOARD** (short version), keep the answers in the conversation and offer to save the file |
| `creator/content-log.md` | Every post and the choices behind it, plus repeat rules | Ask the user to describe their last 5 posts, or start fresh |
| `creator/weekly-system.md` | The creator's weekly workflow and current plan | Use the default in `references/workflow-and-growth.md` |

When working outside a repo (e.g. in the Claude app), keep the profile and log as markdown in the chat and
give the user a **log row to copy** at the end of every production.

## Modes: pick from the request, or run several in sequence
| Mode | Trigger examples | Read |
|---|---|---|
| **ONBOARD** | "set up my profile", "what niche", "relaunch my account" | `references/strategy-and-niche.md` |
| **IDEATE** | "ideas", "what should I post", "content calendar", "series" | `references/ideas-and-trends.md`, `references/libraries.md` §1 |
| **TRENDS** | "what are creators doing", "what's trending", "how does X creator edit" | `references/ideas-and-trends.md`, `references/creator-edit-styles.md` |
| **NEWS** | "news reel", "explain this headline", "budget/RBI/geopolitics" | `references/news-finance-compliance.md` |
| **HOOK** | "hooks", "opening", "first 3 seconds" | `references/hooks.md` |
| **SCRIPT** | "script", "voiceover", "vlog outline" | `references/scripting.md` |
| **SHOOT** | "shot list", "how to film", "b-roll", "lighting", "audio" | `references/filming-on-phone.md` |
| **EDIT** | "how do I edit", "pacing", "cut list", "edit recipe" | `references/editing-playbook.md` |
| **EFFECTS** | "effects", "transitions", "VFX", "text animation", "make it look premium" | `references/effects-library.md` |
| **SOUND** | "music", "sound effects", "audio", "voice" | `references/sound-design.md` |
| **LOOK** | "fonts", "captions", "colours", "grade", "cover", "thumbnail" | `references/typography-and-color.md` |
| **PUBLISH** | "caption", "hashtags", "title", "when to post", "Shorts vs Reels" | `references/platforms-and-publishing.md` |
| **REPURPOSE** | "repurpose", "clips from my vlog", "cross-post" | `references/workflow-and-growth.md` §Repurpose |
| **AUDIT** | "am I repetitive", "log this post", "check my plan" | `references/freshness-engine.md` |
| **REVIEW** | analytics screenshots, "why did this flop", "what's working" | `references/workflow-and-growth.md` §Analytics |
| **PRODUCE** (default) | the user gives a topic or idea and wants a reel | Run the full pipeline below |

## PRODUCE: the full pipeline (default when given a topic)
Run these steps in order and output a single **Production Pack** using `templates/production-pack.md`:

1. **Brief:** the topic, which pillar it belongs to, the target viewer, the single takeaway (one sentence), platform, length and language.
   For news, finance or tax topics, build the **fact pack** first (`references/news-finance-compliance.md`).
2. **Recipe roll:** choose a non-repeating creative recipe. If you can run code, use:
   `python3 scripts/recipe_roll.py --log creator/content-log.md` (relative to this skill folder, or pass full paths).
   Otherwise pick by hand from `references/libraries.md` using the repeat rules in `references/freshness-engine.md`.
   Show the recipe card and give it a memorable name.
3. **Hooks:** 3 options from different archetypes, each with all 4 layers (visual, text, spoken, sound). Recommend one and name a backup to A/B test.
4. **Script:** a timed beat table (time · spoken · on-screen text · visual/b-roll · sound · effect ID). Check the word count against the length.
5. **Shot list:** primary and secondary camera styles, numbered shots, a b-roll bank, transitions to film in camera, light and audio.
6. **Edit plan:** a pacing map, a cut list with effect IDs at exact timestamps, a sound design pass, step-by-step app instructions
   for the 3 hardest moves, and export settings.
7. **Look:** font style or pairing, caption style, text animation, grade settings, accent colour, a cover/thumbnail brief.
8. **Publish kit:** IG caption, YouTube Shorts title and description, hashtags (≤ 5), a pinned comment, a CTA and a story or trial-reel plan.
9. **Compliance check:** run it if the topic is finance, tax, news or politics, or the creator is a regulated professional.
10. **Log row:** a completed content-log row (leave the metrics blank). Save it if the file exists.

Keep the pack scannable, with tables and short lines. Where a step is too long, give the essentials and offer more detail.

## Quality bar (check before answering)
- [ ] Hook works with the sound **off** (text plus visual) and with it **on**
- [ ] Something changes every 2–4 seconds (angle, text, b-roll, effect, sound)
- [ ] At most 2–3 effect *families* per video, each with a clear reason
- [ ] No repeated hook, format, font or grade from the recent log (unless it's a marked series)
- [ ] Text sits inside the safe zone and stays on screen long enough to read
- [ ] Facts have sources, finance content has disclaimers, and there are no buy/sell calls
- [ ] It sounds like the creator, not like an AI

# Creator Studio: One Claude Skill for Reels, Shorts & Vlogs

**`creator-studio`** is one complete skill covering the whole creator workflow: strategy → ideas → trends → hooks → scripts →
filming → editing → **100+ effects** → sound → fonts and colour → publishing → repurposing → analytics → growth,
plus news and finance compliance for a CA creator. Its core job is to make sure **no two videos look, sound or open the same way.**

## What's inside
```
.claude/skills/creator-studio/
├── SKILL.md                         ← main file: 15 modes + the full PRODUCE pipeline + quality bar
├── references/
│   ├── strategy-and-niche.md        ← positioning ("lens" method), pillars, identity, bio, relaunch
│   ├── ideas-and-trends.md          ← 10 idea sources, scoring, what creators are doing now, series formats
│   ├── creator-edit-styles.md       ← 18 creator edit-style archetypes + beginner progression
│   ├── hooks.md                     ← 4-layer hook anatomy + Hinglish hook bank + visual hook moves
│   ├── scripting.md                 ← word budgets, beat tables, structures, explainer formula, long-form
│   ├── filming-on-phone.md          ← Android settings, light, audio, framing, shot lists, batching
│   ├── editing-playbook.md          ← 7-pass edit, pacing maps, cut lists, Instagram Edits + CapCut how-to, export
│   ├── effects-library.md           ← 100+ effects in 9 families with IDs, how-to, difficulty, mood recipes
│   ├── sound-design.md              ← voice chain, music ducking, SFX library, sound-led formats
│   ├── typography-and-color.md      ← font styles, Devanagari fonts, caption specs, 10 grades with settings, covers
│   ├── platforms-and-publishing.md  ← Reels vs Shorts vs long-form, captions, hashtags, timing, publish kit
│   ├── news-finance-compliance.md   ← news radar, fact packs, SEBI/ICAI/Big Four guardrails
│   ├── freshness-engine.md          ← repeat rules, sameness heatmap audit
│   ├── workflow-and-growth.md       ← weekly system, repurposing, analytics benchmarks, growth, monetisation
│   └── libraries.md                 ← 34 formats, 24 hooks, 14 structures, pacing, transitions, fonts, captions, grades, music, camera
├── scripts/recipe_roll.py           ← picks a fresh, non-repeating creative recipe from your content log
└── templates/production-pack.md     ← the output template for a full reel production
```

## How to use it
Open this repo in Claude Code and just ask. The skill loads automatically:
- "Make a reel on the rupee hitting a 6-month high" → full **Production Pack** (brief, recipe, hooks, script, shots, edit plan with effect IDs, look, captions, compliance, log row)
- "What effects should I use for a serious geopolitics reel?" → EFFECTS mode
- "How do creators do the text-behind-person effect in Edits?" → TRENDS + EFFECTS
- "Am I getting repetitive?" → AUDIT · "Here are my insights screenshots" → REVIEW

Roll a fresh recipe yourself:
```
python3 .claude/skills/creator-studio/scripts/recipe_roll.py --log creator/content-log.md --count 3
```

To use it in the Claude app: upload `dist/creator-studio.zip` under Settings → Capabilities → Skills.

## Your files (the skill's memory)
- `creator/brand-profile.md`: your positioning, pillars, voice, identity and CA/Big Four guardrails
- `creator/content-log.md`: every post and its creative IDs (fill it in after each post)
- `creator/weekly-system.md`: your 5–7 hour weekly plan and Week 1 scripts
- `creator/edits-app-playbook.md`: quick Instagram Edits guide

---
name: style-skill-builder
description: Create or update reusable writing style skills from source material. Use when Codex needs to analyze writing samples, extract style from samples, brand or editorial guides, comments, interviews, public articles, Notion or Google Docs, then turn the findings into a neutral style guide and package that guide as a Codex or Claude skill. Also use to audit style-guide prompts or writing skills for bias, missing examples, vague guidance, weak anti-patterns, channel rules, accessibility, translation, legal constraints, operational content modules, evals, memory, or validation coverage.
---

# Style Skill Builder

## Purpose

Build one pipeline: extract a writing style from evidence, author a neutral style guide, then codify that guide into a reusable skill. Keep the scaffolding style-free. Concrete voice, tone, rules, examples, and anti-patterns must come from the user's sources or explicit answers, not from this skill's templates.

## Core Rule

Use source guides like Mailchimp as architecture inspiration only. Do not copy their house style, examples, word preferences, tone, or brand rules into a new style unless the user explicitly asks to build a skill for that exact source and has provided permission or an appropriate source basis.

## Workflow

1. Classify the job.
   - **Extract**: infer style from supplied writing or guides.
   - **Author**: produce a finished style guide from evidence or interview answers.
   - **Package**: create a reusable skill from a style guide.
   - **Audit**: find gaps in an existing style guide, prompt, or skill.

2. Gather and label sources.
   - Separate direct evidence from inference.
   - Preserve hard constraints such as legal, brand, accessibility, inclusive language, spelling, product naming, and channel-specific rules.
   - If samples are thin or inconsistent, ask targeted interview questions instead of inventing confidence.

3. Read only the needed references.
   - `references/analysis-framework.md` when the user asks for analysis, diagnosis, explanation, or multiple-sample comparison before guide generation.
   - `references/source-routing.md` for evidence handling, source weighting, and copyright-safe extraction.
   - `references/extraction-interview.md` when samples are missing, noisy, or need human taste calibration.
   - `references/neutral-style-guide-template.md` when writing the guide.
   - `references/style-skill-template.md` when packaging a guide as a skill.
   - `references/operational-modules.md` when building a Mailchimp-like content system with channel rules, web/UI microcopy, accessibility, translation, legal, or word-list modules.
   - `references/guide-validation.md` before packaging a production-ready style guide or when the user asks to test whether a guide works.
   - `references/self-improvement.md` when the user asks for evals, memory, self-learning, iteration, or making the generated skill improve over time.
   - `references/quality-rubric.md` before delivering or committing a guide or skill.

4. Produce the neutral guide.
   - Purpose and principles
   - Voice and tone
   - Structure
   - Sentence-level preferences
   - Signature moves
   - Anti-patterns and blacklist
   - Positive examples
   - Negative examples
   - Revision checklist

5. Package the guide as a skill when requested.
   - Name the skill in lowercase kebab-case.
   - Keep `SKILL.md` short and procedural.
   - Put the full style guide and review checklists in `references/`.
   - Add `agents/openai.yaml`.
   - Add `references/evals.md` and `references/memory.md` when the skill is meant to improve over repeated use.
   - Add optional operational modules only when supported by the sources or requested by the user.
   - Install in `/Users/Work/.agents/skills` unless the user specifies another location.
   - If the user wants Claude compatibility, symlink `/Users/Work/.claude/skills/<skill-name>` to the canonical folder.
   - Validate with the skill-creator validator when available.

## Extraction Standards

Use a two-column mental model:

- **Observed**: patterns visible in the source, with a short citation, filename, document title, or quoted fragment when allowed.
- **Inferred**: likely rules derived from repeated patterns, labeled with confidence.

Prefer operational guidance over adjectives. "Warm but concise" is too vague unless it becomes specific behaviors: how openings work, how much context to include, what kind of jokes are allowed, what words get cut, what endings should do.

## Packaging Standards

When generating a style skill, make it usable for drafting, revising, reviewing, and adapting. Include:

- Trigger-rich frontmatter description.
- A short workflow for applying the style.
- A reference to the full guide, not the full guide inline.
- A revision checklist.
- Pass/fail evals when output quality can be checked.
- A concise memory file when feedback should improve the skill over time.
- A refusal or escalation rule for missing source authority, legal claims, medical or financial claims, or external publishing.
- Channel rules only when the sources support them.
- Operational modules for accessibility, translation, legal, web/UI microcopy, word lists, or channel guidance only when the use case needs a full content system.

Run `scripts/scaffold_style_skill.py` when a deterministic starter folder would save time. Read or patch the generated files before considering the skill finished.

## Output Shapes

For guide-only work, return the neutral guide plus a short source confidence note.

For skill-building work, create or update files, validate them, then report:

- Skill path
- Key files created or changed
- Validation result
- Any source limits or assumptions

For audits, lead with missing capabilities and risk, then give concrete edits.

## Self-Improvement Loop

For mature generated style skills, include a lightweight learning loop:

1. Run the style task.
2. Evaluate the output against `references/evals.md` using pass/fail checks.
3. If a check fails, revise and rerun the checks until all pass or the eval is found to be faulty.
4. When the user gives durable feedback that does not fit a pass/fail eval, add a short dated note to `references/memory.md`.
5. Periodically audit the skill itself for bloat, vague triggers, stale memory, and rules that belong in evals instead.

Use a separate clean-context agent for evals when the runtime supports it. If not, perform the eval as a clearly separated second pass and label any residual uncertainty.

# Style Skill Template

Use this when turning a completed style guide into a reusable skill.

## Folder Shape

```text
<skill-name>/
+-- SKILL.md
+-- agents/
|   +-- openai.yaml
+-- references/
    +-- style-guide.md
    +-- revision-checklist.md
    +-- evals.md
    +-- memory.md
    +-- channel-rules.md
    +-- word-list.md
    +-- legal-and-accessibility.md
```

Add `references/evals.md` and `references/memory.md` when the skill should improve over repeated use. Add operational modules such as `references/channel-rules.md`, `references/word-list.md`, `references/legal-and-accessibility.md`, `references/translation.md`, or `references/web-elements.md` only when the source material supports them or the user asks for a full content system.

## SKILL.md Skeleton

```markdown
---
name: <skill-name>
description: Draft, revise, review, and adapt writing in <style-name>. Use when the user asks for <brand/person/team/publication> voice, <style-name> writing, style-consistent edits, draft review, line editing, channel adaptation, or applying the attached style guide to articles, posts, emails, docs, scripts, or other prose.
---

# <Style Name> Writing

## Purpose

Apply the style guide without flattening the user's intent. Preserve meaning, factual claims, and source constraints.

## Workflow

1. Identify the user's task: draft, revise, review, adapt, or diagnose.
2. Read `references/style-guide.md` before substantial writing or review.
3. Read `references/revision-checklist.md` before finalizing.
4. If this is recurring work or the user asks for extra rigor, read `references/evals.md` and run the pass/fail checks.
5. If the user gives durable feedback that should change future behavior, add a concise dated note to `references/memory.md`.
6. If optional operational modules exist, read only the module relevant to the task.
7. Ask for missing audience, channel, or source constraints only when they materially change the output.
8. Produce the requested draft or critique with brief notes on the most important style choices.

## Guardrails

- Do not invent facts, quotes, studies, legal claims, or product capabilities.
- Do not publish, send, or externally share without explicit user approval.
- If style rules conflict with accuracy, accessibility, legal constraints, or user instructions, surface the conflict and prioritize the higher-order constraint.
- If the source guide is thin, label uncertain choices instead of overfitting.

## Output

For drafts, provide the writing first, then a short style note if useful.

For reviews, lead with the highest-impact issues and concrete fixes.
```

## Reference Files

`references/style-guide.md` should hold the 8-section guide:

1. Voice and tone
2. Structure
3. Sentence-level preferences
4. Signature moves
5. Anti-patterns and blacklist
6. Positive examples
7. Negative examples
8. Revision checklist

`references/revision-checklist.md` should be short enough to use every time. It should include only the questions that change decisions.

`references/evals.md` should hold pass/fail checks, not numeric scores.

`references/memory.md` should hold short dated lessons from user feedback. Do not duplicate evals.

Operational modules should hold concrete rules for specific surfaces or constraints. Do not create them as generic best-practice dumps.

## openai.yaml

Use:

```yaml
interface:
  display_name: "<Human Name>"
  short_description: "<25 to 64 character skill description>"
  default_prompt: "Use $<skill-name> to revise this draft in the <style-name> style."
```

Quote string values. The default prompt must mention the skill with `$<skill-name>`.

## Installation

Prefer `/Users/Work/.agents/skills/<skill-name>` as the canonical location. For Claude compatibility, create a symlink:

```bash
ln -s /Users/Work/.agents/skills/<skill-name> /Users/Work/.claude/skills/<skill-name>
```

Validate after creation or update.

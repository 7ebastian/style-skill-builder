# Self-Improvement Pattern

Use this when a generated style skill should improve over repeated use.

## What To Add

A mature style skill can have four layers:

| File | Purpose | Loading rule |
| --- | --- | --- |
| `SKILL.md` | Trigger, workflow, guardrails, and routing | Always loaded when the skill triggers |
| `references/style-guide.md` | Full style rules and examples | Load for substantial drafting, revision, or review |
| `references/evals.md` | Pass/fail checks for output quality | Load before finalizing or when asked to run evals |
| `references/memory.md` | Short dated lessons from user feedback | Load when revising recurring work or improving the skill |

Keep `SKILL.md` short. Move bulky examples, evals, and memory out of it.

## Evals

Use pass/fail checks, not numeric scoring. Keep the set to roughly 6 to 10 checks. Good evals are objective enough that another agent can apply them.

Categories that often matter for writing skills:

- Opening: Does the first paragraph perform the style guide's opening job?
- Voice: Does the draft avoid banned patterns and preserve the target emotional temperature?
- Structure: Does the piece move in the expected order?
- Sentence level: Are rhythm, abstraction, jargon, and diction aligned?
- Substance: Are claims specific, useful, and source-backed?
- Channel: Does the output fit the intended format or platform?
- Constraints: Are legal, accessibility, localization, product naming, and external publishing rules respected?

Bad evals:

- "Is this a 4 out of 5?"
- "Does this sound good?"
- "Is it authentic?" without observable criteria.

Better eval:

- "Pass if the opening names a concrete problem or situation before the broader claim. Fail if it begins with generic context, a slogan, or summary."

## Clean-Context Evaluation

When the runtime supports subagents or separate agent threads, run evals in a clean context:

1. Give the evaluator the output, `references/evals.md`, and any required source excerpts.
2. Do not give it the author's reasoning or expected result.
3. Ask for pass/fail results with short evidence.
4. If any check fails, revise the original output and rerun.
5. Stop when all checks pass, the user accepts the output, or a check is identified as faulty.

When clean-context evaluation is unavailable, run a separated self-check and say that it was not independent.

## Memory

Use `references/memory.md` for durable lessons that should change future behavior but are too fuzzy or situational for evals.

Rules:

- Reverse chronological order.
- Each entry should be two or three sentences.
- Record only lessons that improve the skill itself.
- Do not duplicate evals.
- Prefer examples of user feedback over abstract rules.
- Prune stale or contradictory entries during audits.

Good memory entry:

```markdown
## 2026-06-17

User feedback: intros were technically accurate but felt too polished and low-friction. For this style, preserve a little unresolved tension in the opening instead of smoothing the premise into a clean summary.
```

## Skill-Editor Pass

Periodically audit the skill itself:

- Tighten the frontmatter description so the skill triggers correctly.
- Remove bloated instructions and move details to references.
- Convert repeated memory into evals when it becomes checkable.
- Remove stale memory.
- Cut generic AI writing advice not supported by the style guide.
- Validate the skill after edits.

## Human Final Pass

The loop can improve consistency, but the final 10 to 20 percent still belongs to human taste. For important public writing, leave a final human-review note rather than claiming the skill has fully solved taste.

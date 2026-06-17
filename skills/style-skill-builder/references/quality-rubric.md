# Quality Rubric

Run this before delivering a style guide or style skill.

## Style Guide

Score each item pass, partial, or fail.

| Check | Standard |
| --- | --- |
| Source traceability | Important rules are observed, inferred, user-stated, or marked as open |
| Neutrality | No template voice leaked into the guide |
| Specificity | Rules describe behaviors, not only adjectives |
| Tensions | Voice rules include boundaries, not only praise |
| Structure | Openings, movement, and endings are operational |
| Principles | Purpose and durable writing goals are explicit without adding template voice |
| Sentence level | Rhythm, syntax, diction, abstraction, and jargon are covered |
| Signature moves | The guide names repeatable moves with examples |
| Anti-patterns | Blacklist entries explain the fix, not just the error |
| Positive examples | Examples teach transferable lessons |
| Negative examples | Failure examples are realistic enough to catch drift |
| Checklist | The checklist can be used directly on a draft |
| Constraints | Legal, accessibility, translation, product naming, and channel rules are included when relevant |
| Sample conflicts | Conflicting patterns are explained rather than averaged away |

## Skill

| Check | Standard |
| --- | --- |
| Triggering | Frontmatter says when to use the skill in concrete terms |
| Progressive disclosure | Full guide lives in references, not bloated SKILL.md |
| Workflow | Skill supports drafting, revising, reviewing, and adapting |
| Evals | Recurring output quality has pass/fail checks when useful |
| Memory | Durable user feedback has a concise memory path when useful |
| Guardrails | Accuracy, external publishing, legal claims, and missing source limits are handled |
| Reference routing | The skill tells Codex when to read each reference |
| Operational modules | Optional modules exist only when source-backed or requested |
| UI metadata | `agents/openai.yaml` has display name, short description, and `$skill-name` default prompt |
| Validation | Skill passes available validator |
| Compatibility | Claude symlink exists when requested or locally expected |

## Red Flags

- A rule sounds true of "good writing" but is not source-backed.
- The guide uses examples from another brand as if they are target examples.
- The skill tells Codex to imitate a living writer without user-provided source material and clear constraints.
- The revision checklist is so long it will not be used.
- Memory repeats eval checks instead of capturing durable taste feedback.
- Evals use vague scores instead of pass/fail checks.
- The anti-pattern list bans common words without explaining when they are actually wrong.
- Channel advice is generic platform lore rather than source-specific style.
- Conflicting source patterns are silently blended into a bland average.
- A generated content-system skill lacks the operational modules needed for its actual writing surfaces.
- The skill encourages publishing or posting without explicit approval.

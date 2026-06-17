# Guide Validation

Use this before packaging a production-ready style guide as a skill, or when the user asks whether a guide actually works.

## Loop

1. Generate or revise a short test paragraph using the guide.
2. Diagnose the result against the guide.
3. Identify vague, missing, or contradictory rules.
4. Tighten the guide.
5. Repeat once if the first revision changed important rules.

## Diagnostic Questions

- Which rules changed the output in visible ways?
- Which rules were too vague to apply?
- Which anti-patterns still appeared?
- Which examples taught the wrong rhythm or level of polish?
- Did the output overfit a single sample?
- Did the output preserve productive friction, or flatten it into generic good writing?
- Are channel, legal, accessibility, translation, and product constraints present when needed?

## When To Stop

Stop when:

- The test paragraph follows the most important guide rules.
- Remaining issues require user taste, not clearer instructions.
- The source material is too thin and the uncertainty is labeled.

## Output

```markdown
## Validation Result

Pass/Partial/Fail

## What Worked

- ...

## Rules To Tighten

- ...

## Revised Guide Changes

- ...
```

# Style Skill Builder

Style Skill Builder is a single agent skill for turning writing samples, editorial guides, comments, interviews, and public references into reusable writing style skills.

It helps an agent:

- analyze writing samples with a richer craft framework
- extract a neutral style guide without importing another brand's voice
- package that guide as a Codex or Claude skill
- add pass/fail evals and memory so generated skills can improve over time
- scaffold content-system modules for channels, web/UI copy, accessibility, translation, legal constraints, and word lists

This is a skill repository, not a plugin. The skill lives at `skills/style-skill-builder/`.

## Repository Structure

```text
.
+-- skills/
|   +-- style-skill-builder/
|       +-- SKILL.md
|       +-- agents/openai.yaml
|       +-- references/
|       +-- scripts/scaffold_style_skill.py
+-- README.md
+-- LICENSE
```

## Install

Give your agent this one-liner:

```bash
npx skills add 7ebastian/style-skill-builder -g
```

That installs the skill globally for the current agent runtime.

To install explicitly for both Codex and Claude Code:

```bash
npx skills add 7ebastian/style-skill-builder -g -a codex -a claude-code -y
```

Restart Codex or Claude Code, or open a new thread, so the skill list refreshes.

To update later:

```bash
npx skills update style-skill-builder -g
```

### Claude.ai Or Other Skill Uploaders

For upload-only products, zip the skill folder:

```bash
git clone --depth 1 https://github.com/7ebastian/style-skill-builder.git && cd style-skill-builder/skills && zip -r style-skill-builder.zip style-skill-builder
```

## Use

Examples:

```text
Use $style-skill-builder to analyze these three essays and extract a reusable style guide.
```

```text
Use $style-skill-builder to turn this brand guide into a reusable writing skill with evals and memory.
```

```text
Use $style-skill-builder to create a full content-system skill with channel rules, accessibility, translation, legal constraints, and a word list.
```

The generated style skill can be minimal or operationally complete. Generated style skills use the short `sg-` prefix so multiple guides group together in autocomplete:

- `sg-noah`
- `sg-mailchimp`
- `sg-haavn`

For full content-system scaffolding, use the included script:

```bash
skills/style-skill-builder/scripts/scaffold_style_skill.py noah --modules all
```

That creates `sg-noah` by default.

Supported optional modules:

- `channel-rules`
- `web-elements`
- `legal-and-accessibility`
- `translation`
- `word-list`

## Design Notes

The skill is intentionally neutral. It can use public guides such as Mailchimp's style guide as architecture inspiration, but it does not copy another brand's voice, examples, terms, or house rules into generated skills unless the user explicitly asks for that exact style and provides an appropriate source basis.

The core guide shape includes:

1. Purpose and principles
2. Voice and tone
3. Structure
4. Sentence-level preferences
5. Signature moves
6. Anti-patterns and blacklist
7. Positive examples
8. Negative examples
9. Revision checklist

Generated style skills can also include:

- `references/evals.md` for pass/fail output checks
- `references/memory.md` for short dated lessons from user feedback
- optional operational modules for full content systems

## License

MIT

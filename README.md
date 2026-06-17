# Style Skill Builder

Style Skill Builder is an agent skill for turning writing samples, editorial guides, comments, interviews, and public references into reusable writing style skills.

It helps an agent:

- analyze writing samples with a richer craft framework
- extract a neutral style guide without importing another brand's voice
- package that guide as a Codex or Claude skill
- add pass/fail evals and memory so the generated skill can improve over time
- optionally scaffold Mailchimp-style content-system modules for channels, web/UI copy, accessibility, translation, legal constraints, and word lists

This repository is packaged in the same broad shape as public Agent Skills repositories: each skill is self-contained under `skills/<skill-name>/` with a `SKILL.md` file and optional references, scripts, and agent metadata.

## Included Skill

- `style-skill-builder`: Extract a writing style from source material, author a neutral style guide, and codify it into a reusable skill.

## Repository Structure

```text
.
+-- .claude-plugin/
|   +-- marketplace.json
|   +-- plugin.json
+-- .codex-plugin/
|   +-- plugin.json
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

### Claude Code

Run these commands inside Claude Code:

```text
/plugin marketplace add 7ebastian/style-skill-builder
/plugin install style-skill-builder@style-skill-builder-local
```

Restart Claude Code after installation.

You can then invoke the skill directly:

```text
/style-skill-builder
```

Or ask for it naturally:

```text
Use the style skill builder to extract a writing style from these samples and package it as a reusable skill.
```

### Codex

Register the marketplace:

```bash
codex plugin marketplace add 7ebastian/style-skill-builder
```

Then launch Codex, run `/plugins`, open the Style Skill Builder marketplace, and install `style-skill-builder`. Restart Codex after installation.

If your Codex setup uses skills directly instead of plugin marketplaces, install the skill folder into your Codex skills directory:

```bash
git clone https://github.com/7ebastian/style-skill-builder.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R style-skill-builder/skills/style-skill-builder "${CODEX_HOME:-$HOME/.codex}/skills/style-skill-builder"
```

In shared multi-agent setups, you can also place the skill in `~/.agents/skills/style-skill-builder` and symlink it into other runtimes.

### Claude.ai Or Other Skill Uploaders

Zip the skill folder and upload it as a custom skill:

```bash
cd style-skill-builder/skills
zip -r style-skill-builder.zip style-skill-builder
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

The generated style skill can be minimal or operationally complete. For full content-system scaffolding, use the included script:

```bash
skills/style-skill-builder/scripts/scaffold_style_skill.py my-writing-style --modules all
```

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

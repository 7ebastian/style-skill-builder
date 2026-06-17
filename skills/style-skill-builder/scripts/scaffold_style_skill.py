#!/usr/bin/env python3
"""Create a starter folder for a writing style skill."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


VALID_MODULES = {
    "channel-rules",
    "web-elements",
    "legal-and-accessibility",
    "translation",
    "word-list",
}


def normalize_skill_name(value: str) -> str:
    name = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    name = re.sub(r"-{2,}", "-", name)
    if not name:
        raise ValueError("skill name must contain at least one letter or digit")
    if len(name) > 64:
        raise ValueError("skill name must be 64 characters or fewer")
    return name


def title_from_name(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("-"))


def read_optional(path: str | None) -> str:
    if not path:
        return ""
    return Path(path).read_text(encoding="utf-8").strip()


def write_file(path: Path, text: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists. Pass --force to overwrite.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def build_skill_md(skill_name: str, style_name: str, modules: list[str]) -> str:
    if modules:
        final_steps = """6. If optional operational modules exist, read only the module relevant to the task.
7. Ask for missing audience, channel, or source constraints only when they materially change the output.
8. Produce the requested draft or critique with brief notes on the most important style choices."""
    else:
        final_steps = """6. Ask for missing audience, channel, or source constraints only when they materially change the output.
7. Produce the requested draft or critique with brief notes on the most important style choices."""
    return f"""---
name: {skill_name}
description: Draft, revise, review, and adapt writing in {style_name}. Use when the user asks for {style_name} voice, style-consistent edits, draft review, line editing, channel adaptation, or applying the attached style guide to articles, posts, emails, docs, scripts, or other prose.
---

# {style_name} Writing

## Purpose

Apply the style guide without flattening the user's intent. Preserve meaning, factual claims, and source constraints.

## Workflow

1. Identify the user's task: draft, revise, review, adapt, or diagnose.
2. Read `references/style-guide.md` before substantial writing or review.
3. Read `references/revision-checklist.md` before finalizing.
4. For recurring work or high-stakes drafts, read `references/evals.md` and run pass/fail checks.
5. If the user gives durable feedback that should change future behavior, add a short dated note to `references/memory.md`.
{final_steps}

## Guardrails

- Do not invent facts, quotes, studies, legal claims, or product capabilities.
- Do not publish, send, or externally share without explicit user approval.
- If style rules conflict with accuracy, accessibility, legal constraints, or user instructions, surface the conflict and prioritize the higher-order constraint.
- If the source guide is thin, label uncertain choices instead of overfitting.

## Output

For drafts, provide the writing first, then a short style note if useful.

For reviews, lead with the highest-impact issues and concrete fixes.
"""


def build_revision_checklist(style_guide: str) -> str:
    if "## 8. Revision Checklist" in style_guide:
        checklist = style_guide.split("## 8. Revision Checklist", 1)[1].strip()
        next_section = re.search(r"\n##\s+", checklist)
        if next_section:
            checklist = checklist[: next_section.start()].strip()
        if checklist:
            return "# Revision Checklist\n\n" + checklist
    return """# Revision Checklist

- Does the draft follow the voice and tone rules?
- Does the structure match the guide's opening, movement, and ending patterns?
- Are sentence-level choices consistent with the guide?
- Are signature moves present where useful?
- Are blacklist patterns removed or intentionally retained?
- Are legal, accessibility, localization, channel, or product constraints satisfied?
"""


def build_evals(style_name: str) -> str:
    return f"""# Evals

Use pass/fail checks for {style_name}. Do not use numeric scores.

## Opening

- [ ] Pass if the opening follows the style guide's required opening pattern. Fail if it begins with generic context, a slogan, or summary.

## Voice

- [ ] Pass if the draft follows the voice and tone rules in `style-guide.md`. Fail if it uses a banned voice pattern or unsupported register.

## Structure

- [ ] Pass if the piece moves in the structure described by the guide. Fail if it meanders, buries the point, or ends by collapsing into summary.

## Sentence Level

- [ ] Pass if sentence rhythm, diction, abstraction, and jargon match the guide. Fail if the draft sounds generic, over-polished, or inconsistent with the guide.

## Substance

- [ ] Pass if claims are specific and source-backed. Fail if the draft invents facts, vague authority, or unsupported certainty.

## Constraints

- [ ] Pass if legal, accessibility, localization, product naming, and external publishing constraints are respected. Fail if any constraint is violated or uncertain without being surfaced.

## Result Format

| Check | Result | Evidence | Fix |
| --- | --- | --- | --- |
"""


def build_memory() -> str:
    return """# Memory

Reverse chronological notes that improve this style skill over time.

Only add durable lessons from user feedback or repeated failures. Do not duplicate `references/evals.md`.

## YYYY-MM-DD

[Two or three sentences. Describe the feedback, what it changes, and when to apply it.]
"""


def parse_modules(raw: str | None) -> list[str]:
    if not raw:
        return []
    requested = [item.strip() for item in raw.split(",") if item.strip()]
    if "all" in requested:
        return sorted(VALID_MODULES)
    invalid = sorted(set(requested) - VALID_MODULES)
    if invalid:
        valid = ", ".join(sorted(VALID_MODULES | {"all"}))
        raise ValueError(f"unknown module(s): {', '.join(invalid)}. Valid: {valid}")
    return sorted(set(requested))


def build_module(module: str) -> str:
    if module == "channel-rules":
        return """# Channel Rules

Add only source-backed rules.

## [Channel]

- Purpose: [what this channel is for]
- Audience state: [what the reader needs or feels]
- Structure: [how this format should move]
- Voice adjustment: [how tone changes]
- Required elements: [CTA, links, proof, caveats]
- Avoid: [channel-specific failures]
"""
    if module == "web-elements":
        return """# Web Elements

Add rules only for surfaces this skill will actually write.

## Buttons

- [Verb/action rule]
- [Capitalization rule]
- [Length rule]

## Links

- [Descriptive link text rule]
- [Accessibility rule]

## Forms

- [Labeling rule]
- [Required field rule]
"""
    if module == "legal-and-accessibility":
        return """# Legal and Accessibility

## Claims

- [Evidence requirement]
- [Approval or escalation rule]

## Accessibility

- [Plain-language rule]
- [Heading/link/list/alt-text rule]

## Inclusive Language

- [People-first or identity-language rule]
- [Terms to avoid]
"""
    if module == "translation":
        return """# Translation

- [Sentence structure rule]
- [Ambiguity rule]
- [Term consistency rule]
- [Idioms/slang rule]
- [Units/currency/date rule]
"""
    if module == "word-list":
        return """# Word List

## Use

- [Term]: [usage rule]

## Use Carefully

- [Term]: [when allowed and how to define]

## Avoid

- [Term]: [replacement or reason]
"""
    raise ValueError(f"unsupported module: {module}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_name", help="Skill name or title. Normalized to kebab-case.")
    parser.add_argument("--output-dir", default="/Users/Work/.agents/skills", help="Directory that will contain the skill folder.")
    parser.add_argument("--style-name", help="Human-facing style name. Defaults to title-cased skill name.")
    parser.add_argument("--style-guide", help="Path to a completed style guide markdown file.")
    parser.add_argument(
        "--modules",
        help="Comma-separated optional modules: channel-rules, web-elements, legal-and-accessibility, translation, word-list, or all.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing files in the target skill folder.")
    args = parser.parse_args()

    skill_name = normalize_skill_name(args.skill_name)
    style_name = args.style_name or title_from_name(skill_name)
    modules = parse_modules(args.modules)
    target = Path(args.output_dir).expanduser() / skill_name
    style_guide = read_optional(args.style_guide) or "# Style Guide\n\n## 0. Purpose and Principles\n\n[Add the purpose and source-backed principles here.]\n\n## 1. Voice and Tone\n\n[Add the completed guide here.]"

    if target.exists() and not args.force:
        raise FileExistsError(f"{target} already exists. Pass --force to overwrite.")
    if target.exists() and args.force:
        shutil.rmtree(target)

    write_file(target / "SKILL.md", build_skill_md(skill_name, style_name, modules), True)
    write_file(target / "references" / "style-guide.md", style_guide, True)
    write_file(target / "references" / "revision-checklist.md", build_revision_checklist(style_guide), True)
    write_file(target / "references" / "evals.md", build_evals(style_name), True)
    write_file(target / "references" / "memory.md", build_memory(), True)
    for module in modules:
        write_file(target / "references" / f"{module}.md", build_module(module), True)
    write_file(
        target / "agents" / "openai.yaml",
        f"""interface:
  display_name: "{style_name}"
  short_description: "Write and edit in {style_name}"
  default_prompt: "Use ${skill_name} to revise this draft in the {style_name} style."
""",
        True,
    )
    print(target)


if __name__ == "__main__":
    main()

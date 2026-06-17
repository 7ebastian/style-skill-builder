# Operational Modules

Use this when the target is a full content system rather than a simple voice guide. Add modules only when source material supports them or the user asks for them.

## Module Decision Table

| Module | Create when | Should contain |
| --- | --- | --- |
| `channel-rules.md` | Writing differs by format, audience, or platform | Rules for articles, newsletters, social, email, support, educational, sales, or internal docs |
| `web-elements.md` | The style applies to product, website, or app UI | Buttons, links, forms, headings, alt text, navigation, empty states, errors |
| `legal-and-accessibility.md` | Claims, compliance, inclusion, accessibility, or approvals matter | Required disclaimers, claim handling, inclusive language, accessible structure |
| `translation.md` | Content is localized or read by international audiences | Plain-language rules, ambiguity avoidance, term consistency, units, currency |
| `word-list.md` | The source has preferred spellings or banned terms | Use, avoid, use carefully, capitalization, product names |

## Rules

- Keep operational modules separate from the main style guide.
- Do not create generic best-practice modules just because a mature guide usually has them.
- If the module is source-light, label it as a starter checklist rather than a rule set.
- Make each module operational: what to do, what to avoid, and what to check.
- Respect higher-order constraints over voice. Accuracy, accessibility, legal, and user instructions win.

## Starter Content

### channel-rules.md

```markdown
# Channel Rules

## [Channel]

- Purpose: [what this channel is for]
- Audience state: [what the reader needs or feels]
- Structure: [how this format should move]
- Voice adjustment: [how tone changes]
- Required elements: [CTA, links, proof, caveats]
- Avoid: [channel-specific failures]
```

### web-elements.md

```markdown
# Web Elements

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
```

### legal-and-accessibility.md

```markdown
# Legal and Accessibility

## Claims

- [Evidence requirement]
- [Approval or escalation rule]

## Accessibility

- [Plain-language rule]
- [Heading/link/list/alt-text rule]

## Inclusive Language

- [People-first or identity-language rule]
- [Terms to avoid]
```

### translation.md

```markdown
# Translation

- [Sentence structure rule]
- [Ambiguity rule]
- [Term consistency rule]
- [Idioms/slang rule]
- [Units/currency/date rule]
```

### word-list.md

```markdown
# Word List

## Use

- [Term]: [usage rule]

## Use Carefully

- [Term]: [when allowed and how to define]

## Avoid

- [Term]: [replacement or reason]
```

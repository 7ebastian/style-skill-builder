# Source Routing

Use this file to decide how to treat inputs before extracting style.

## Source Types

| Source type | Use it for | Guardrail |
| --- | --- | --- |
| Writing samples | Voice, structure, rhythm, signature moves, negative space | Label confidence by sample size and consistency |
| Existing brand or editorial guide | Explicit rules, terminology, channel guidance, legal constraints | Do not assume unstated voice rules |
| Public style guide or article | Scaffolding ideas and quoted rules when legally appropriate | Do not transfer another brand's house style into a new guide |
| Comments and edits | Reviewer taste, friction points, recurring objections | Distinguish one-off preference from stable rule |
| Interview answers | Intent, boundaries, taste, desired emotional temperature | Ask for examples when answers are abstract |
| Drafts plus revisions | What changes during editing and why | Prefer before/after deltas over final-only praise |

## Source Weighting

1. Explicit user instructions outrank all other sources.
2. Current organization style guides outrank old samples.
3. Repeated edited deltas outrank isolated polished examples.
4. Published samples outrank rough drafts for final voice, unless the task is to capture drafting voice.
5. Public third-party guides may inspire structure, not style, unless the target is that third-party style.

## Multiple-Sample Handling

When sources include more than one sample, do not smooth everything into one average voice.

- Identify patterns that repeat across samples.
- Separate durable voice rules from topic-specific choices.
- Note intentional variation by channel, audience, genre, funnel stage, or emotional context.
- Label each rule as strong, provisional, context-dependent, or conflicting.
- If samples conflict, explain the likely reason rather than hiding the conflict.
- Prefer before/after revisions, comments, and repeated edits when deciding which pattern is intentional.

Use a compact conflict table when useful:

| Pattern | Source A | Source B | Decision |
| --- | --- | --- | --- |
| [Observed difference] | [Evidence] | [Evidence] | [Rule, context split, or open question] |

## Copyright-Safe Extraction

Extract patterns, not large passages. Use short excerpts only when needed as evidence and stay within applicable quotation limits. Prefer paraphrased observations:

- "Openings tend to begin with a concrete user problem before naming the broader idea."
- "The guide bans empty intensifiers unless the claim is measurable."

Do not paste a full article, guide, chapter, or style section into the generated output.

## Web Source Extraction

When extracting from websites, especially blogs, newsletters, and Substack pages, avoid broad body dumps. Pages often include subscription boxes, paywall prompts, recommendations, comments, and footer text that can overwhelm the actual article.

Prefer bounded fields:

- page URL
- title and subtitle or meta description
- author and date when available
- headings
- short paragraph openings
- external source links and their anchor text
- visible paywall or access limits

Filter out subscription prompts, sign-in prompts, privacy or terms footers, comments, and repeated navigation unless the user's task specifically concerns those elements.

## Evidence Labels

Use these labels in notes or guide drafts when helpful:

- **Observed**: visible in named source material.
- **Inferred**: likely rule based on repeated patterns.
- **User-stated**: supplied directly by the user.
- **Constraint**: legal, compliance, accessibility, localization, brand, product, or channel requirement.
- **Open question**: needs user judgment before becoming a rule.

## Bias Check

Before finalizing, scan for style values that came from the template rather than sources. Remove or bracket them. Common leak points:

- Placeholder adjectives that survived as rules.
- Generic "plainspoken, warm, smart" language with no source basis.
- A borrowed blacklist from another guide.
- Examples that teach the wrong rhythm.
- Channel rules invented because similar guides usually include them.

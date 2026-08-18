# Sample Intake

Use this process when the user provides attractive whiteboard examples.

## Inputs

Accept:

- Feishu document links containing whiteboards.
- Whiteboard tokens.
- Screenshots or exported images.
- Raw OpenAPI JSON.
- Short notes such as "I like this style because it feels clean".

## Sensitive Input Boundary

Treat links, tokens, resource identifiers, raw JSON, screenshots, thumbnails, exact text, names, metrics, and dates as sensitive source material.

- Query and inspect source material only in an operating-system temporary directory or an ignored `work/` / `tmp/` directory.
- Do not copy source material into tracked files.
- Do not retain source provenance or details that could identify the original board, person, company, product, or project.
- If a reusable rule cannot be written without source-specific detail, do not store it.

## Extraction

For links or tokens:

1. Fetch the document or query the board with `lark-whiteboard`.
2. Export an image preview when possible.
3. Export raw/code when possible.
4. Note the traits listed in the main SKILL.md Learning Workflow.

For screenshots:

1. Inspect composition visually.
2. Estimate layout grid, palette, shapes, and typography.
3. Ask for the live board only if raw structure is needed.

## Style Memory Update

Only update `style-library.md` when a style is likely reusable. Store principles, not copied content.

Good memory:

- "Use a 4-column staged flow with thin gray lanes and blue hero cards for product workflows."
- "For leadership strategy maps, place north-star objective at top and use three pillar cards below."

Bad memory:

- Exact confidential text from an example.
- Source links, tokens, resource IDs, screenshots, thumbnails, or raw exports.
- People or company names, internal product/project names, unique copy, business metrics, dates, or endpoint errors.
- A one-off arrangement tied to one document only.
- Raw node JSON or exact node content, even when it appears reusable.

## Reporting Back

After learning from examples, summarize:

- What style family was learned.
- Which concrete rules were added.
- What kinds of future boards should use it.

Do not repeat source identifiers or sensitive source details in the report.

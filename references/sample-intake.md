# Sample Intake

Use this process when the user provides attractive whiteboard examples.

## Inputs

Accept:

- Feishu document links containing whiteboards.
- Whiteboard tokens.
- Screenshots or exported images.
- Raw OpenAPI JSON.
- Short notes such as "I like this style because it feels clean".

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
- A one-off arrangement tied to one document only.
- Raw node JSON copied without a reusable design reason.

## Reporting Back

After learning from examples, summarize:

- What style family was learned.
- Which concrete rules were added.
- What kinds of future boards should use it.

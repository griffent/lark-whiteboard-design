---
name: lark-whiteboard-design
description: Design polished Feishu/Lark whiteboards with stronger visual hierarchy, layout, color, spacing, and reusable diagram patterns. Use when the user asks to create, beautify, redesign, audit, learn from, or standardize Feishu/Lark whiteboards; when the user provides attractive board links, tokens, screenshots, thumbnails, or raw board data to learn from; or when a document, workflow, architecture, comparison, timeline, funnel, or strategy needs to become a high-quality whiteboard instead of a plain diagram. Coordinate with the lark-whiteboard skill for actual Feishu whiteboard querying, rendering, dry-run, and writing.
---

# Lark Whiteboard Design

Use this skill to make Feishu/Lark whiteboards look intentionally designed, not merely API-generated. It adds a design layer on top of the existing `lark-whiteboard` execution skill.

## Core Rule

Always separate four jobs:

1. Learn style from references.
2. Plan the information architecture.
3. Render the board with a chosen visual pattern.
4. Verify and write through `lark-whiteboard`.

When the task will touch a real Feishu whiteboard, read and follow the installed `lark-whiteboard` skill before querying, dry-running, or writing.

## Intake

Ask for or use any of these reference inputs:

- Feishu document URL containing one or more whiteboards.
- Whiteboard token.
- Screenshot or exported thumbnail.
- Existing raw board JSON.
- User description such as "make it like these examples".

If no references are provided, use the house style in `references/style-library.md`.

For reference links/tokens, use `lark-whiteboard +query` to capture both image and raw/code when possible. For screenshots, inspect the image directly and describe style traits.

## Learning Workflow

For each reference board, capture these traits in notes before drawing:

- Purpose: process, architecture, comparison, timeline, funnel, org chart, strategy map, etc.
- Layout: canvas orientation, sectioning, alignment grid, reading order, grouping.
- Visual hierarchy: title treatment, section headers, emphasis nodes, secondary nodes.
- Color system: background, primary color, accents, warning/success colors, neutral strokes.
- Shape language: cards, pills, frames, swimlanes, connectors, icons, badges.
- Density: node count, whitespace ratio, average text length, annotation style.
- Interaction affordance: where a reader's eye starts and where it ends.

Update `references/style-library.md` after the user approves a recurring style pattern.

## Design Workflow

1. State the board's single takeaway in one sentence.
2. Choose a pattern from `references/patterns.md`.
3. Sketch the layout in text: major regions, reading direction, node groups, and emphasis points.
4. Generate source using the route required by `lark-whiteboard`.
5. Convert to OpenAPI JSON with `whiteboard-cli`.
6. Run `scripts/whiteboard_quality_check.py` on the JSON when available.
7. Render/export a preview image through `lark-whiteboard +query --output_as image` when possible.
8. Fix layout issues before writing the final board.
9. Dry-run before overwriting an existing whiteboard; ask the user before deleting existing nodes.

## Visual Standards

Prefer:

- One clear canvas-level title and 2-5 well-labeled regions.
- A restrained palette with one primary, one accent, and neutrals.
- Consistent card sizes within the same semantic group.
- A visible grid: equal gutters, aligned edges, consistent connector anchors.
- Short node labels, with details in side notes or secondary text.
- Intentional contrast between hero nodes, normal nodes, and annotations.
- Connectors that express direction without crossing unnecessarily.
- Enough whitespace that the board can be read at 80-100 percent zoom.

Avoid:

- Default Mermaid-looking output unless the user explicitly wants that style.
- Random pastel boxes with no hierarchy.
- One-note palettes where everything is the same hue.
- Long paragraphs inside nodes.
- Unaligned boxes, diagonal connector clutter, or dense crossing lines.
- Decorative gradients, blobs, or icons that do not clarify meaning.
- Tiny text or huge empty boxes.

## Pattern Selection

Read `references/patterns.md` when choosing the visual structure. Default choices:

- Process or decision path: staged flow with lanes.
- System architecture: layered map with data/request arrows.
- Comparison: side-by-side matrix with shared criteria.
- Roadmap: horizontal timeline with milestones and risks.
- Funnel: vertical conversion shape with metrics and leakage notes.
- Cause analysis: fishbone or driver tree.
- Strategy: north-star goal with pillars, bets, and proof points.

## Example Learning Loop

When the user sends good boards:

1. Extract visual traits from 3-8 examples.
2. Cluster them into style families such as "executive strategy map", "product architecture", or "launch timeline".
3. Save durable rules in `references/style-library.md`.
4. Use those rules on the next live board.
5. Compare the result against the examples and revise.

## Validation

Before delivery, check:

- Does the board communicate the single takeaway in 5 seconds?
- Are major groups visually separated without relying only on text?
- Is every connector needed?
- Are text labels short enough to fit?
- Is there a clear start and end point?
- Does the palette match the intended tone?
- Did the live Feishu write return success?

If validation fails visually, revise the source and regenerate instead of manually patching many raw node coordinates.

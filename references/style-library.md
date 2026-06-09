# Style Library

This file stores durable style rules learned from user-approved Feishu/Lark whiteboard examples.

## House Style v0

Use this when no references are provided.

### Canvas

- Prefer a light neutral canvas with no decorative background blobs.
- Keep a clear title zone at the top-left or top-center.
- Use 24-40 px outer margins and consistent internal gutters.
- Use horizontal reading order for processes and timelines; use vertical hierarchy for strategy maps and funnels.

### Palette

- Primary: Feishu-like blue for active/system elements.
- Accent: green for success/recommendation, orange for risk/attention.
- Neutral: near-black text, soft gray strokes, pale neutral fills.
- Limit each board to 3-5 functional colors.
- Do not make the entire board purple, beige, slate, or one hue family.

### Type

- Title: concise, high contrast, no long subtitle inside the title.
- Section labels: short noun phrases.
- Node labels: 1-2 lines whenever possible.
- Details: move to small notes or side annotations instead of cramming paragraphs into nodes.

### Shapes

- Use rounded rectangles only when they behave like cards or states; keep radius modest.
- Use frames or swimlanes for groups.
- Use badges for status, owner, priority, or phase.
- Use connectors with consistent direction and anchor points.

### Hierarchy

- Make the most important path visually obvious through size, weight, or accent color.
- Use secondary color and thinner strokes for context nodes.
- Keep warnings visible but not louder than the main story unless the board is risk-focused.

## Learned Styles

Append user-approved style families here.

### Layered Capability Map With Scenario Rail

Name: Layered Capability Map With Scenario Rail
Reference source: User-provided Feishu whiteboard example, learned from raw nodes on 2026-06-02. Image export was unavailable because the Feishu thumbnail endpoint returned 403, so this style is inferred from node geometry and styles.
Best for: Business architecture maps, AI/product capability maps, platform strategy, operating model decomposition, and leadership explanations where readers need to see layers, capability groups, and business touchpoints together.
Layout:
- Use a wide-but-balanced canvas around 1100 x 900.
- Put the main architecture map on the left 75-80 percent of the canvas.
- Reserve a narrow right-side rail for scenarios, touchpoints, or business channels.
- Stack 3 major horizontal layers in the main area: top context/strategy, large middle capability layer, bottom foundation/infrastructure layer.
- In the large middle layer, use 3 aligned vertical cards of equal size for core capability groups.
- Use large pale section containers before placing small cards; do not rely on arrows to create structure.
Palette:
- Base fills: white and very light gray.
- Major section fill: pale blue similar to `#f0f4fc`.
- Secondary neutral fill: light gray similar to `#f5f5f5`.
- Functional accents: green, blue, and purple for sibling capability groups.
- Use lavender or light green only as soft emphasis, not full-canvas decoration.
Shapes:
- Rounded rectangles dominate; keep the same card size within each semantic group.
- Use large background containers, medium module cards, and small pill-like labels.
- Use tiny numbered markers for sequence or layer labels.
- Use very few connectors; hierarchy should come from placement, grouping, labels, and color.
Typography:
- Keep most labels at 12-14 px equivalent.
- Use 16-24 px only for canvas or major section titles.
- Keep labels short; target 4-12 Chinese characters for most nodes.
- Avoid paragraphs inside nodes; split detail into small adjacent labels.
Do:
- Create an obvious left-to-right split between "main system/capabilities" and "business touchpoints".
- Use consistent x/y alignment and repeated card dimensions.
- Put dense content inside framed groups so high node count still feels ordered.
- Use color to encode category, not decoration.
Avoid:
- Default flowchart output.
- Many crossing arrows.
- Random card widths in the same row.
- Overusing accent colors across unrelated groups.

### Product Evolution Storyboard

Name: Product Evolution Storyboard
Reference source: User-provided Feishu whiteboard example 2, learned from raw nodes on 2026-06-02.
Best for: Product vision evolution, current-state to ideal-state narratives, phased product roadmaps, and "from pain point to future capability" explanations.
Layout:
- Use a very wide panoramic canvas when comparing many stages.
- Organize by phases with each phase as a tall column or large vertical panel.
- Put problem/user pain, product stage, and ideal state in separate visual zones.
- Use large image/mockup blocks as anchors, then pair them with short text interpretation.
- Keep phase labels visible and repeated at the same y-position.
Palette:
- Use bright accent cards for stage headers or product capability labels.
- Combine blue/cyan for product capability, purple for future/AI capability, and gray for current-state notes.
- Let screenshots or mockups carry detail; keep surrounding cards simpler.
Shapes:
- Large rounded phase containers.
- Screenshot/image blocks aligned to the same baseline.
- Small status chips such as "ing", "to build", or stage numbers.
Typography:
- Use very large labels only for canvas-level stage titles.
- Keep explanatory text short and concrete; split dense reasoning into separate cards.
Do:
- Tell a before-to-after story visually.
- Pair each stage with both business/user problem and product expression.
- Use images as evidence, not decoration.
Avoid:
- Making all phases equal if the story has a clear current/future emphasis.
- Using long paragraphs where a screenshot plus one sentence would work.
- Letting the wide canvas lose orientation; repeat stage markers.

### Minimal Three-Step Asset Pipeline

Name: Minimal Three-Step Asset Pipeline
Reference source: User-provided Feishu whiteboard example 3, learned from raw nodes on 2026-06-02.
Best for: Simple methodology, enablement process, asset production loop, "three prerequisites" explanation, and onboarding flows.
Layout:
- Use three equal-width cards in a single row.
- Put concise text cards on top and matching visual/example blocks below.
- Keep the canvas short and calm; do not add connectors unless sequence ambiguity exists.
- Align all cards to identical x/y positions and dimensions.
Palette:
- Use pale blue card fills with blue borders for a clean instructional tone.
- Let embedded images carry visual variety.
Shapes:
- Three large rounded cards, same width and height.
- Image blocks directly below each card with the same width.
Typography:
- Each card can contain a short title, one blank-line break, and 2-3 support lines.
- Avoid more than 70 characters per card unless the board is meant to be read closely.
Do:
- Use for "Step 1 / Step 2 / Step 3" when the logic is already linear.
- Maintain symmetry and whitespace.
Avoid:
- Over-designing with icons, arrows, or many colors.
- Mixing card sizes.

### Clear Bridge Decision Map

Name: Clear Bridge Decision Map
Reference source: User-provided Feishu whiteboard example 4, explicitly noted by the user as clear-thinking.
Best for: Explaining how multiple inputs, constraints, skills, and scenarios route into a final output; design automation flows; agent orchestration; decision maps.
Layout:
- Use a near-square canvas, not an ultra-wide one.
- Put input artifacts at the top as a horizontal row.
- Put constraints and reusable assets near the upper/middle area.
- Put three scenario/demand cards in the center as the main decision split.
- Use a bottom output band spanning the canvas width.
- Connect only the key routing paths; keep connectors sparse and directional.
Palette:
- Use pale blue for neutral inputs/process.
- Use green for success/directly achieved.
- Use yellow/orange for constraints or caveats.
- Use red only for warnings or blocking checks.
- Use black sparingly for strong separators or critical emphasis.
Shapes:
- Rounded rectangles for artifacts and demand scenarios.
- Arrow-shaped blocks may be used as clear movement indicators, but keep them aligned.
- Use small "NEW" chips for newly introduced modules.
Typography:
- Scenario titles should include a category letter or short prefix, such as "A.", "B.", "C.".
- Use 18 px equivalent for primary scenario labels and 14 px equivalent for supporting nodes.
Do:
- Make the routing logic readable even if someone ignores every minor node.
- Use one central question/split and one final output band.
- Keep the number of connectors low enough to trace by eye.
Avoid:
- Drawing a spiderweb of every dependency.
- Placing scenarios in different sizes unless priority is different.
- Hiding the final output.

### Workflow Roadmap With Capability Chips

Name: Workflow Roadmap With Capability Chips
Reference source: User-provided Feishu whiteboard example 5, learned from raw nodes on 2026-06-02.
Best for: Design workflow maps, AI capability planning, multi-stage operating workflows, and capability coverage across phases.
Layout:
- Use a wide canvas around 1600 x 800.
- Start with a clear title/legend zone.
- Lay out 5-6 workflow stages horizontally.
- Add capability chips or cards under the stages they support.
- Add a foundation band across the bottom to show cross-cutting capabilities.
- Use a short explanatory note to decode chip colors.
Palette:
- Use soft warm orange, sky blue, and lavender as category fills.
- Use matching low-saturation borders for each category.
- Keep the canvas background almost white.
Shapes:
- Stage numbers are small, consistent markers.
- Capability chips can use rounded rectangles with category color.
- Foundation band should span most of the width and feel separate from stage cards.
Typography:
- Stage titles should be short verb/noun phrases.
- Long explanatory notes belong in a single low-emphasis note block.
Do:
- Encode category by color consistently across the whole board.
- Make coverage across stages visually scannable.
- Use a legend when colors carry meaning.
Avoid:
- Creating separate disconnected mini-diagrams for each stage.
- Using more than three chip colors.
- Letting the foundation band compete with the main stages.

### Template

Name:
Reference source:
Best for:
Layout:
Palette:
Shapes:
Typography:
Do:
Avoid:

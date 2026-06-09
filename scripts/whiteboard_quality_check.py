#!/usr/bin/env python3
import json
import math
import sys
from collections import Counter


def find_nodes(value):
    if isinstance(value, dict):
        nodes = value.get("nodes")
        if isinstance(nodes, list):
            return nodes
        for child in value.values():
            found = find_nodes(child)
            if found is not None:
                return found
    elif isinstance(value, list):
        for child in value:
            found = find_nodes(child)
            if found is not None:
                return found
    return None


def node_text(node):
    text = node.get("text")
    if isinstance(text, dict):
        raw = text.get("text")
        if isinstance(raw, str):
            return raw
    if isinstance(text, str):
        return text
    return ""


def style_colors(node):
    style = node.get("style")
    if not isinstance(style, dict):
        return []
    keys = ("fill_color", "border_color", "text_color")
    return [style[k] for k in keys if isinstance(style.get(k), str) and style[k]]


def finite_number(value):
    return isinstance(value, (int, float)) and math.isfinite(value)


def main():
    if len(sys.argv) != 2:
        print("usage: whiteboard_quality_check.py <openapi-json>", file=sys.stderr)
        return 2

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        payload = json.load(f)

    nodes = find_nodes(payload) or []
    shapes = [n for n in nodes if n.get("type") != "connector"]
    connectors = [n for n in nodes if n.get("type") == "connector"]
    texts = [node_text(n) for n in shapes if node_text(n)]
    colors = [c for n in shapes for c in style_colors(n)]
    type_counts = Counter(str(n.get("type", "unknown")) for n in nodes)

    xs = []
    ys = []
    for n in shapes:
        x, y = n.get("x"), n.get("y")
        w, h = n.get("width"), n.get("height")
        if all(finite_number(v) for v in (x, y, w, h)):
            xs.extend([x, x + w])
            ys.extend([y, y + h])

    warnings = []
    suggestions = []

    if not nodes:
        warnings.append("No whiteboard nodes found.")
    if len(shapes) < 3:
        warnings.append("Very few visual nodes; the board may not communicate enough structure.")
    if connectors and len(connectors) > max(1, len(shapes) * 1.5):
        warnings.append("Connector count is high relative to nodes; check for visual clutter.")
    if colors and len(set(colors)) <= 2 and len(shapes) >= 5:
        warnings.append("Only one or two colors detected; add hierarchy with neutrals and one accent.")

    long_texts = [t for t in texts if len(t) > 36]
    if long_texts:
        warnings.append(f"{len(long_texts)} node label(s) exceed 36 characters.")
        suggestions.append("Shorten labels or move detail into side notes.")

    if xs and ys:
        width = max(xs) - min(xs)
        height = max(ys) - min(ys)
        if width <= 0 or height <= 0:
            warnings.append("Bounding box is empty.")
        elif width / max(height, 1) > 8:
            warnings.append("Canvas is extremely wide; check readability in Feishu.")
        elif height / max(width, 1) > 5:
            warnings.append("Canvas is extremely tall; check scanability.")
    else:
        width = height = 0

    result = {
        "ok": not warnings,
        "summary": {
            "node_count": len(nodes),
            "shape_count": len(shapes),
            "connector_count": len(connectors),
            "type_counts": dict(type_counts),
            "unique_color_count": len(set(colors)),
            "text_label_count": len(texts),
            "bounds": {"width": round(width, 2), "height": round(height, 2)},
        },
        "warnings": warnings,
        "suggestions": suggestions,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not warnings else 1


if __name__ == "__main__":
    raise SystemExit(main())

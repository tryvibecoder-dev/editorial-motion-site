#!/usr/bin/env python3
"""Convert a PNG (or any Pillow-readable image) into colored ASCII art.

Terminal output uses 24-bit ANSI colors. HTML output uses <span> tags,
so the result can be pasted into a web page.

Examples:
    python3 png2ascii.py photo.png
    python3 png2ascii.py photo.png --width 120 --charset dense
    python3 png2ascii.py photo.png --html art.html
    python3 png2ascii.py photo.png --mono
"""

import argparse
import html
import sys

from PIL import Image

CHARSETS = {
    # from darkest to lightest; characters are chosen by brightness
    "dense": "@%#*+=-:. ",
    "blocks": "█▓▒░ ",
    "simple": "#@%&8WM*oc;:,. ",
    "thin": "@$B8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
}


def load_image(path, width, aspect):
    img = Image.open(path).convert("RGBA")
    # Terminal characters are roughly twice as tall as they are wide,
    # so the image height is scaled down to keep proportions.
    cols = width
    rows = max(1, int(img.height / img.width * cols * aspect))
    img = img.resize((cols, rows), Image.LANCZOS)

    # Flatten transparency onto a black background.
    bg = Image.new("RGBA", img.size, (0, 0, 0, 255))
    bg.alpha_composite(img)
    return bg.convert("RGB")


def brightness(rgb):
    r, g, b = rgb
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255.0


def pick_char(charset, value):
    # value: 0.0 = black (darkest) .. 1.0 = white (brightest).
    # The charsets are ordered dark to light, so index by brightness.
    index = int(value * (len(charset) - 1) + 0.5)
    return charset[index]


def render_ansi(img, charset, mono, invert):
    lines = []
    w, h = img.size
    px = img.load()
    for y in range(h):
        parts = []
        for x in range(w):
            rgb = px[x, y]
            v = brightness(rgb)
            if invert:
                v = 1.0 - v
            ch = pick_char(charset, v)
            if mono or ch == " ":
                parts.append(ch)
            else:
                r, g, b = rgb
                parts.append(f"\x1b[38;2;{r};{g};{b}m{ch}")
        if not mono:
            parts.append("\x1b[0m")
        lines.append("".join(parts))
    return "\n".join(lines)


def render_html(img, charset, invert, bg_color):
    w, h = img.size
    px = img.load()
    out = [
        "<!DOCTYPE html>",
        '<html lang="en"><head><meta charset="UTF-8"><title>ASCII art</title>',
        "<style>",
        f"body{{background:{bg_color};margin:0;padding:24px;}}",
        "pre{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:10px;"
        "line-height:1.0;letter-spacing:0;margin:0;}",
        "</style></head><body><pre>",
    ]
    for y in range(h):
        for x in range(w):
            rgb = px[x, y]
            v = brightness(rgb)
            if invert:
                v = 1.0 - v
            ch = pick_char(charset, v)
            if ch == " ":
                out.append(" ")
            else:
                r, g, b = rgb
                out.append(f'<span style="color:rgb({r},{g},{b})">{html.escape(ch)}</span>')
        out.append("\n")
    out.append("</pre></body></html>")
    return "".join(out)


def main():
    p = argparse.ArgumentParser(description="PNG to colored ASCII art")
    p.add_argument("image", help="input image path (PNG, JPG, WEBP, ...)")
    p.add_argument("--width", type=int, default=100, help="output width in characters (default 100)")
    p.add_argument("--charset", choices=sorted(CHARSETS), default="dense", help="character set")
    p.add_argument("--aspect", type=float, default=0.5,
                   help="character height/width ratio used for row count (default 0.5)")
    p.add_argument("--invert", action="store_true", help="swap light and dark (for light terminals)")
    p.add_argument("--mono", action="store_true", help="plain text, no colors")
    p.add_argument("--html", metavar="FILE", help="write colored HTML to FILE instead of printing")
    p.add_argument("--bg", default="#000000", help="background color for HTML output (default #000000)")
    args = p.parse_args()

    if args.width < 1:
        p.error("--width must be at least 1")

    charset = CHARSETS[args.charset]
    img = load_image(args.image, args.width, args.aspect)

    if args.html:
        with open(args.html, "w", encoding="utf-8") as f:
            f.write(render_html(img, charset, args.invert, args.bg))
        print(f"Saved {args.html} ({img.width}x{img.height} characters)", file=sys.stderr)
    else:
        print(render_ansi(img, charset, args.mono, args.invert))


if __name__ == "__main__":
    main()

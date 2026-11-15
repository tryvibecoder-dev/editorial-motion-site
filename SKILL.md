---
name: editorial-motion-site
description: Build a single-page site in a bold editorial-minimalism motion-design style, with a giant grotesque wordmark cropped at the edge, italic serif subtitles, monospace labels, flat colors, and GSAP ScrollTrigger animations. Use this whenever the user asks for a one-page site, landing page, studio or portfolio page, personal brand page, or anything described as "editorial", "motion-design studio style", "big typography", "contrast between heavy grotesk and italic serif", or "flat colors without gradients". Also use it when the user wants a bold typographic hero with scroll reveals, parallax, a magnetic or wipe-fill button, or a custom cursor, even if they never name the style.
---

# Editorial motion site

This skill produces one self-contained HTML file (inline CSS and JS) in the style of a modern motion-design studio: confident, graphic, typography-first, with very few decorative elements. The page is built from large type and thin rules, and the motion does the job that ornament would otherwise do.

The style is defined by its typography, its flat color, and its restraint. The specific palette is not part of the style. Pick colors per project (see below).

## Typography: three voices

Use exactly three typefaces from Google Fonts, each with a distinct role. Keep the contrast between them; that contrast is the look.

- **Heavy wide grotesque** (Archivo Black, Anton, or Unbounded) for the giant brand word and for section headings and list titles. Set it very large, with tight tracking (around -0.03em) and line-height near 0.9.
- **High-contrast italic serif** (Instrument Serif Italic, Playfair Display Italic, or DM Serif Display Italic) for subtitles, emphasized keywords inside heavy body text, and alternate words that appear on hover. Italic keywords are the main way the page adds elegance to heavy type.
- **Monospace** (JetBrains Mono or IBM Plex Mono) at small size, uppercase, with wide letter-spacing (around 0.1em), for navigation, numbered section labels like "(01) About", captions, footers, and metadata lines such as "studio · est. 2026".

Check that the chosen typeface supports the page's language. Many italic serifs are Latin-only. If the copy is not in a Latin-script language, choose a serif italic that covers it.

## Color: flat, two-tone, chosen per project

- Use two flat colors: a saturated background and a near-black or near-white ink. A third accent is allowed only if the brief asks for it.
- Choose the pair from the brief's mood or from the content, and make sure body text reads clearly on the background.
- No gradients, no drop shadows, no glows, no blurred backgrounds. Opacity is allowed for ghosted decorative type.
- Ink should be the only text color. Do not introduce grays for body text unless the brief asks for them.

## Layout

- **Hero:** full viewport height. The brand word is set at a size where it spans almost the full width and is cropped by the bottom edge, so part of the letters is cut off. A tagline in italic serif sits in the upper area, with a thin horizontal rule under it and a mono metadata line.
- **Sections:** start each with a mono label such as "(02) Services". Use generous vertical padding (around 14–20vh) and a grid of two or three columns for text.
- **Keywords:** inside heavy body text, set key words in the italic serif at a slightly larger size. Use only a few per paragraph.
- **Lists:** rows separated by 1px rules. Each row has a number in mono, a large title, a short mono description, and an arrow at the right. Do not use cards or boxes.
- **Button:** an outlined rectangle. On hover, fill it with the ink color from one side, invert the text, and turn the corners into a pill. Use CSS transitions for this.
- **Custom cursor (only on fine pointers):** a small dot that follows the pointer, and grows into an outlined ring over interactive elements. Hide the native cursor only when the custom one is active.
- **Footer:** an oversized italic serif call to action (for example "Let's talk"), followed by a single row of mono links with a rule above.

## Motion

Use GSAP with ScrollTrigger from a CDN. Animate only `transform` and `opacity`.

- **Intro:** the brand letters rise from inside a masked wrapper (`yPercent` from 110 to 0), staggered by about 0.08–0.09s, with `power4.out` and a duration of 0.8–1.2s. Each letter sits inside an `overflow: hidden` span so it appears to emerge from below.
- **Subtitle:** words fade up (opacity 0 to 1, y 24 to 0), staggered by about 0.06–0.07s.
- **Rules:** grow left to right with `scaleX` from 0, `transform-origin: left`.
- **Scroll reveals:** blocks rise (y 50 to 0, opacity 0 to 1) when they reach about 88% of the viewport. Italic keywords inside a paragraph fade in one after another.
- **Parallax:** use `scrub: true` with different `yPercent` values for layers. The giant brand word moves slower than the page; a ghosted background word moves in the opposite direction.
- **Hover:** list rows shift right (translateX around 3vw) and their title swaps to the italic alternate by fading opacity. The title and its alternate are stacked in one grid cell so the layout does not jump.

Always provide a `prefers-reduced-motion` path: skip the GSAP timelines and reveals, remove transitions, and hide the custom cursor.

## Responsive behavior

- On narrow screens the brand word keeps its crop and grows with viewport width (around 36vw for four letters).
- Two-column layouts collapse to one column. Hide long mono descriptions in list rows on small screens.
- Keep the page free of horizontal overflow, except in the intentional crop of the hero word.

## Copy

- Write real copy in the brief's language, never lorem ipsum. Use short declarative sentences for the heavy text and an informal, specific voice for the mono labels.
- Keep the copy short enough to read as design rather than as a document: one clear statement per section, plus a short list of services or offerings.

## Output

- One HTML file. Inline CSS and JS. Fonts and GSAP loaded from a CDN.
- Complete code with no placeholders or comments of the form "add the rest here".
- Before delivering, check: the brand word is cropped by the bottom edge, every italic keyword is set in the serif, the palette is flat, the animations use only transform and opacity, and the reduced-motion branch exists.

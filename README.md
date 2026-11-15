# editorial-motion-site

A Claude skill for building one-page sites in a bold editorial-minimalism motion-design style: a giant grotesque wordmark cropped at the edge, italic serif subtitles, monospace labels, flat colors, and GSAP ScrollTrigger animations.

**Live page:** https://tryvibecoder-dev.github.io/editorial-motion-site/

## Install

```bash
git clone https://github.com/tryvibecoder-dev/editorial-motion-site ~/.claude/skills/editorial-motion-site
```

Then ask Claude for a one-page site, a landing page, a studio or portfolio page, or anything described as "editorial" or "big typography". The skill triggers on those requests.

## What the skill specifies

- **Typography:** three Google Fonts with distinct roles. A heavy wide grotesque for the wordmark and headings, a high-contrast italic serif for subtitles and keywords, and a monospace face for labels and navigation.
- **Color:** two flat colors chosen per project, with no gradients, shadows, or glows.
- **Layout:** a full-height hero with the wordmark cropped by the bottom edge, numbered sections with mono labels, and list rows divided by thin rules.
- **Motion:** masked letter rise on load, word fades, rules that grow with `scaleX`, scroll reveals, and parallax. Only `transform` and `opacity` are animated.
- **Interaction:** a wipe-fill button that turns into a pill on hover, a custom cursor on fine pointers, and list rows whose titles swap to an italic alternate.
- **Accessibility:** a `prefers-reduced-motion` path that disables animation and the custom cursor.

## Repository layout

```
SKILL.md          the skill itself
docs/             the demo page published with GitHub Pages
docs/images/      screenshots of sites built with the skill
docs/demos/       demo sites built from the design-styles catalogue
docs/design-styles/ the design-styles section of the live page
skills/design-styles/ 200 visual directions, animations and 3D notes
```

## Demos

Six sites, all built as single HTML files with GSAP and ScrollTrigger, some with Three.js. Each one follows the tutorials in `skills/design-styles/references/animations.md` and `3d.md`.

| Demo | Idea | Motion used |
| --- | --- | --- |
| [Bauhaus](https://tryvibecoder-dev.github.io/editorial-motion-site/demos/bauhaus/) | geometry as language | shapes rotate and parallax on scroll |
| [Ma](https://tryvibecoder-dev.github.io/editorial-motion-site/demos/ma/) | Japanese emptiness | slow fades, large gaps |
| [Kinetic type](https://tryvibecoder-dev.github.io/editorial-motion-site/demos/kinetic/) | type as the object | variable font scrubbed by scroll |
| [Brutal](https://tryvibecoder-dev.github.io/editorial-motion-site/demos/brutal/) | raw grid, black marquee | marquee, word swap, magnetic button, counters |
| [Signal](https://tryvibecoder-dev.github.io/editorial-motion-site/demos/signal/) | terminal mood | typed command, flicker, grain, scrubbed text |
| [Orbit](https://tryvibecoder-dev.github.io/editorial-motion-site/demos/orbit/) | 3D object | Three.js, pinned morph, parallax, tilting cards |

The full catalogue and the list of files is on the [design-styles page](https://tryvibecoder-dev.github.io/editorial-motion-site/design-styles/).

## License

MIT

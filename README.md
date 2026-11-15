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
```

## License

MIT

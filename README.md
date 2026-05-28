# NaCTeM redesign

Work-in-progress redesign of [nactem.ac.uk](https://www.nactem.ac.uk/), the
National Centre for Text Mining at the University of Manchester.

This is an unaffiliated design exploration — not an official NaCTeM property.

## Stack

- [Astro](https://astro.build) (static, TypeScript strict)
- Tailwind CSS v4
- Deployed to GitHub Pages via Actions

## Layout

```
.
├── site/                  # Astro project (source of the redesigned site)
│   ├── src/
│   │   ├── pages/
│   │   ├── layouts/
│   │   ├── components/
│   │   └── styles/
│   └── package.json
├── original-mirror/       # wget mirror of the legacy site (gitignored, reference only)
└── .github/workflows/     # GH Pages deploy
```

## Local dev

```bash
cd site
npm install
npm run dev
# → http://localhost:4321
```

## Build

```bash
cd site && npm run build
```

Output lands in `site/dist/`, which the workflow uploads to GitHub Pages.

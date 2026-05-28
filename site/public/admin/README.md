# NaCTeM CMS — quick start

This site uses [Sveltia CMS](https://github.com/sveltia/sveltia-cms) as a
no-backend, git-based admin layer over the Astro content collections.

Visit https://jiminhuang.github.io/admin/ once the site is deployed.

## What it edits

| Collection | Folder | Editable? |
|---|---|---|
| News | `site/src/content/news/` | Create / edit / delete |
| People | `site/src/content/people/` | Create / edit / delete |
| Projects | `site/src/content/projects/` | Create / edit / delete |
| Tools | `site/src/content/tools/` | Create / edit / delete |
| Resources & Corpora | `site/src/content/corpora/` | Create / edit / delete |
| Press mentions | `site/src/content/press/` | Create / edit / delete |
| Seminars | `site/src/content/seminars/` | Create / edit / delete |
| Publications | `site/src/content/publications/` | **Read-only / edit existing** — the 576 entries are synced from Aigaion, do not add new ones here |

Each save becomes a `cms: <action> <collection> "<slug>"` commit on `main`.
GitHub Actions rebuilds the site and redeploys to GitHub Pages within a
couple of minutes.

## Authenticating

Sveltia uses GitHub for auth. Two options:

### Option A — built-in PKCE flow (recommended)

1. The site owner registers a GitHub OAuth App once:
   - https://github.com/settings/applications/new
   - **Application name**: `NaCTeM CMS`
   - **Homepage URL**: `https://jiminhuang.github.io`
   - **Authorization callback URL**: `https://jiminhuang.github.io/admin/`
2. Copy the issued Client ID into `public/admin/config.yml` under
   `backend.auth_endpoint` (replace the default). No client secret is
   needed.
3. From then on, anyone with **write access to this repo** can open
   `/admin/` and click "Sign in with GitHub" — they're redirected to
   GitHub, authorise, and land back in the CMS.

### Option B — personal access token

If you don't want to register an OAuth app, every editor can paste their
own [fine-grained GitHub PAT](https://github.com/settings/tokens?type=beta)
into the CMS sign-in screen. The PAT needs `Contents: read & write` for
this repo. The token is stored only in the editor's browser localStorage.

## What lives where

```
public/admin/
├── index.html       # Sveltia CMS entry point
├── config.yml       # Schema for all collections
└── README.md        # This file
```

Schema in `config.yml` mirrors the Zod schemas defined in
`site/src/content.config.ts`. **When you add a new field there, also
add it here.**

## Local dev

Sveltia can also run locally against a local backend. For now we don't
ship that — `npm run dev` plus a markdown editor (or `github.dev`,
press `.` on the repo) is usually faster than spinning up the CMS just
to fix a typo.

## Common tasks

| Task | Where |
|---|---|
| Add a "What's new" announcement | News → New News |
| Add a new PhD student | People → New People (set group to `PhD`) |
| Mark a PhD as graduated → Alumni | Edit the person, change `group` to `Alumni` and fill `yearGraduated` / `degree` / `currentPosition` |
| Add a new tool / corpus | Tools → New Tools, or Resources → New Resources |
| Log a press mention | Press → New Press mentions |
| Schedule a seminar | Seminars → New Seminars |
| Add or edit a project | Projects → New Projects |

## What's not in the CMS

- **Layout and visual changes** — these are in `.astro` files; edit
  via git.
- **The 576 publications from Aigaion** — sync, not authoring. To
  pull new publications, re-run the Aigaion scraper.
- **Funder logos / favicons** — sit in `public/funders` and
  `public/`; replace via git.

# cewlab.org

Website of the **Clean Energy and Water (CEW) Laboratory**, Department of Mechanical Engineering,
Kate Gleason College of Engineering, Rochester Institute of Technology.

Built with [Jekyll](https://jekyllrb.com/) and the
[al-folio](https://github.com/alshedivat/al-folio) theme; hosted free on GitHub Pages.
Replaces a Wix site retired in 2026.

## Editing the site

Everything is plain text. The common edits:

| To change | Edit |
|---|---|
| Publications | `_bibliography/papers.bib` — the page regenerates itself |
| Team roster | `_data/team.yml` |
| Home / Research / Teaching / Join Us / PI | the matching file in `_pages/` |
| News items | add a file to `_news/` |
| Colors, fonts, team-grid styling | `_sass/_brand.scss` |
| Site title, nav, contact, analytics | `_config.yml` |

Push to `main` and GitHub Actions rebuilds and redeploys automatically.

### Adding a publication

Append the BibTeX entry to `_bibliography/papers.bib`. Add `selected={true}` to feature it on the
home page. The master copy lives at `~/.claude/knowledge/publications.bib` — keep the two in sync.

### Adding a team member

Add a block under the right group in `_data/team.yml`:

```yaml
- name: Jane Doe
  role: PhD Student            # optional
  topic: Solid electrolytes    # optional, renders in italics
  photo: Jane_Doe.jpg          # optional; omit for the placeholder avatar
```

Put the headshot in `assets/img/team/`. Responsive WebP variants are generated at build time, so
drop in the full-resolution file — but downsize anything over ~1 MB first.

## Running locally

Requires Ruby 3.x+ (macOS system Ruby 2.6 is too old — `brew install ruby`).

```bash
bundle install
bundle exec jekyll serve
# http://127.0.0.1:4000
```

## Asset provenance

Source media (brand kit, headshots, figures, videos, paper PDFs) lives in
`gDrive/management/cewLab/advertisement/`. A complete archive of the retired Wix site — 22 PDFs,
9 videos, 71 images, and the page-data JSON — is at
`gDrive/management/cewLab/advertisement/website/wix-archive/`.

## Theme upgrades

The theme is the `al_folio_core` gem, so `bundle update al_folio_core` upgrades it. All custom
styling is confined to `_sass/_brand.scss` and `assets/css/main.scss`; no theme partial is forked.

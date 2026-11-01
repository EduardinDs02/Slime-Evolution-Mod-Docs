# Maintain the English Guide

The public site is written in English. Edit the Markdown guides, assets, and tools in this repository, then rebuild before publishing:

```sh
python -m pip install -r tools/docs/requirements.txt
python tools/docs/build-site.py --output .
node tools/docs/check-site-browser.mjs
```

Commit the Markdown, tools, and generated HTML, CSS, search index, sitemap, and assets together. GitHub Pages serves the root of the main branch, with `.nojekyll` disabling Jekyll processing. The mod source repository retains Portuguese documentation; this public guide uses English player-facing content.

Keep species IDs, recipe IDs, commands, numeric requirements, and existing page paths stable. Older Portuguese section fragments are retained as invisible aliases for existing links. Use real English gameplay captures for interface images.

The habitat table and the habitat fields in all 47 gallery cards are generated from the mod species JSON and recursively expanded block tags. With both repositories checked out, refresh them from the mod source repository:

```sh
python tools/docs/generate-habitats.py --english-docs /path/to/Slime-Evolution-Mod-Docs
python tools/docs/generate-habitats.py --english-docs /path/to/Slime-Evolution-Mod-Docs --check
```

Run these commands in the mod source checkout. Minecraft 1.21.1 block and biome labels are in its `tools/docs/habitat-labels.json`. Rebuild this English site afterward.

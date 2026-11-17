# santiago23florido.github.io

Personal research site — **https://santiago23florido.github.io**

Static page, no build step and no dependencies: `index.html` plus `style.css`.
GitHub Pages serves the `main` branch from the repository root, and `.nojekyll`
tells it not to run Jekyll over the files.

## Editing

| File | Holds |
|---|---|
| `index.html` | All the content: research, publications, projects, experience, skills, contact. |
| `style.css` | Design tokens at the top (`:root`), light and dark themes, layout. |

Colours are defined once as custom properties on `:root` and overridden for dark
mode, so changing the palette means editing those two blocks and nothing else.
The theme follows the operating system by default; the button in the navigation
bar overrides it and stores the choice in `localStorage`.

Every result quoted on the page is accompanied by the limits of the evidence
behind it — whether the work is in simulation, whether the data is synthetic,
and what has not been built yet. Keep it that way when updating.

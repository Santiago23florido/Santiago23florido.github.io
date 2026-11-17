# santiago23florido.github.io

Personal research site — **https://santiago23florido.github.io**

Static pages, no build step and no dependencies.

```
index.html              hero, about, the three section cards, contact
research/index.html     interests and publications
projects/index.html     the projects, their results and the limits of each
experience/index.html   positions, education, skills, languages
style.css               shared design tokens and layout
```

The navigation bar, the contact block and the footer are repeated verbatim in all four
pages. They are not edited by hand four times: `build.py` holds the shared head, navigation
and footer plus the body of each page, and writes the four files.

    python3 build.py

Colours are defined once as custom properties on `:root` in `style.css` and overridden for
dark mode, so changing the palette means editing those two blocks and nothing else. The
theme follows the operating system by default; the button in the navigation bar overrides
it and stores the choice in `localStorage`.

`.nojekyll` stops GitHub Pages from running Jekyll over the files. Pages serves `main`
from the repository root.

## One rule when updating

Every result quoted on the site is followed by the limits of the evidence behind it —
whether the work is in simulation, whether the data is synthetic, and what has not been
built yet. Keep it that way.

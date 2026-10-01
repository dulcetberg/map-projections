# Every Map Is Wrong

Twenty map projections, drawn and measured in Python, for the post at
https://bergstromgis.com/work/map-projections.html

Every flat map of the world distorts area, shape, distance or direction. This project draws the same
world in twenty projections, from the gnomonic star charts of ancient Greece to Equal Earth (2018),
puts Tissot's indicatrix on each one to show where the distortion goes, and measures it.

## What's here

- `notebooks/01-projection-maps.ipynb` draws all 20 maps, computes the distortion scorecard, counts
  the projections in PROJ and the EPSG registry, and exports the data for the page's interactive slider.
  Every judgement call is marked **Choice:** in the notebook.
- `figures/` holds the 20 maps and a contact sheet.
- `data/scorecard.csv` has three numbers per projection: area range, typical angle distortion, and how
  many times too big Greenland looks next to Africa.
- `data/interactive_world.json` holds the Greenland, Africa and rest-of-world outlines for the slider.
- `research/facts.md` is the fact sheet behind every date and attribution, with page-level citations,
  mostly to John Snyder's USGS manuals (Professional Papers 1395 and 1453).
- `site/` contains the scripts that build the page and add it to bergstromgis.com.

## Running it

Uses the `geo` conda environment: Python 3.12, cartopy 0.25, pyproj 3.7 (PROJ 9.5), geopandas,
matplotlib. Open the notebook from the repo root and use Run All. The first run downloads Natural Earth
data through cartopy.

## How the distortion is measured

PROJ reports, at any point, how a tiny circle on the globe comes out on the map: an ellipse with
longest radius a and shortest radius b. Area scale is a × b, and angle distortion is
2·arcsin((a − b)/(a + b)). These are measured at 100,000 evenly spread points, kept to land and to the
part of the world each map shows.

## Data and sources

Map data: Natural Earth (public domain). Projections: PROJ, via pyproj and cartopy. Full sources for the
histories are in `research/facts.md`.

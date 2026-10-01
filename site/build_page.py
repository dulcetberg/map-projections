"""Build the bergstromgis.com case-study page from draft/post.md.

Reuses the site's own nav, hero, sidebar and footer from an existing case-study
page so they stay identical, converts the draft's small Markdown subset to HTML,
drops each projection's map in after its heading, and fills every scorecard
from data/scorecard.csv so the page can't disagree with the notebook.

Writes into the gis-portfolio repo; commit and push are done separately.
"""
import csv
import html
import re
import shutil
import subprocess
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SITE = Path.home() / "gis-portfolio" / "docs"
TEMPLATE = SITE / "work" / "ghost-bus-index.html"
PAGE = SITE / "work" / "map-projections.html"
ASSETS = SITE / "map-projections"
URL = "https://bergstromgis.com/work/map-projections.html"
REPO = "https://github.com/dulcetberg/map-projections"

TITLE = "Every Map Is Wrong"
SUBTITLE = ("Twenty map projections, from ancient star charts to the map the UN just endorsed: "
            "what each one gets right, what it gives up, and why someone thought that trade was worth it.")
DESCRIPTION = ("Every flat map of the world distorts something. Twenty map projections, drawn and measured "
               "in Python, with the history of who made each one and why, from Mercator's navigation chart "
               "to the 2026 UN vote for equal-area maps.")
OG_ALT = ("Twenty small world maps in a grid on a near-black background, each drawn in a different map "
          "projection, from Gnomonic to Equal Earth.")

REGION = {
    "gnomonic": "the North Atlantic", "stereographic": "the Northern Hemisphere seen from above the North Pole",
    "orthographic": "a globe centered on Chicago", "azimuthal-equidistant": "the world centered on the North Pole",
    "lambert-conformal-conic": "the lower 48 US states", "albers": "the lower 48 US states",
    "lambert-azimuthal-equal-area": "Europe", "transverse-mercator": "the Americas",
    "polyconic": "North America",
}
SCOPE = {  # what the scorecard numbers were measured over, when it isn't the whole map
    "lambert-conformal-conic": "measured over the lower 48", "albers": "measured over the lower 48",
    "lambert-azimuthal-equal-area": "measured over Europe", "polyconic": "measured over North America",
    "transverse-mercator": "measured inside UTM zone 16",
}


# ---------- tiny Markdown subset ----------
def inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(https?://[^\s<)]+)", r'<a href="\1">\1</a>', t)
    return t


def table(lines):
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines if not re.match(r"^\|[-| ]+\|$", ln.strip())]
    head, body = rows[0], rows[1:]
    out = ['<figure class="wide"><div class="scroll"><table><thead><tr>']
    out += [f"<th>{inline(h)}</th>" for h in head]
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table></div></figure>")
    return "".join(out)


def blocks(md):
    """Split Markdown into (kind, payload) blocks."""
    lines, i, out = md.split("\n"), 0, []
    while i < len(lines):
        ln = lines[i]
        if not ln.strip() or ln.strip() == "---":
            i += 1
        elif ln.startswith("### "):
            out.append(("h3", ln[4:].strip())); i += 1
        elif ln.startswith("## "):
            out.append(("h2", ln[3:].strip())); i += 1
        elif ln.startswith("|"):
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            out.append(("table", lines[i:j])); i = j
        elif ln.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:]); i += 1
            out.append(("ul", items))
        else:
            j = i
            while j < len(lines) and lines[j].strip() and not lines[j].startswith(("#", "|", "- ")):
                j += 1
            out.append(("p", " ".join(x.strip() for x in lines[i:j]))); i = j
    return out


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


# ---------- assets ----------
def build_assets(score):
    ASSETS.mkdir(parents=True, exist_ok=True)
    sizes = {}
    for png in sorted((ROOT / "figures").glob("[0-9][0-9]-*.png")):
        webp = ASSETS / (png.stem + ".webp")
        subprocess.run(["cwebp", "-quiet", "-q", "86", "-alpha_q", "90", str(png), "-o", str(webp)], check=True)
        with Image.open(png) as im:
            sizes[png.stem] = im.size
    world = ROOT / "data" / "interactive_world.json"
    if world.exists():
        shutil.copy(world, ASSETS / "world.json")
    # Card / social image: the contact sheet cropped to 1200x630
    with Image.open(ROOT / "figures" / "00-contact-sheet.png") as im:
        # Letterbox the whole sheet onto the site background so all 20 maps show
        im = im.convert("RGB")
        h = 600
        w = round(im.width * h / im.height)
        card = Image.new("RGB", (1200, 630), (0x12, 0x0D, 0x0B))
        card.paste(im.resize((w, h), Image.LANCZOS), ((1200 - w) // 2, 15))
        card.save(SITE / "images" / "map-projections.jpg", quality=88)
    return sizes


def chips(row):
    g = row["greenland_exaggeration"]
    gtxt = "n/a" if not g else ("1.0× (honest)" if float(g) == 1.0 else f"{float(g):.1f}×")
    return (f'<div class="figures score"><div><b>{float(row["area_range"]):.1f}×</b><span>Area range</span></div>'
            f'<div><b>{float(row["median_angle_deg"]):.0f}°</b><span>Shape distortion</span></div>'
            f'<div><b>{gtxt}</b><span>Greenland check</span></div></div>')


# ---------- page ----------
def build():
    score = {r["slug"]: r for r in csv.DictReader(open(ROOT / "data" / "scorecard.csv"))}
    by_num = {int(r["n"]): r for r in score.values()}
    sizes = build_assets(score)

    md = (ROOT / "draft" / "post.md").read_text()
    md = md[md.index("## Every map is wrong"):]          # drop the review notes and draft title
    md = md.replace("## Every map is wrong\n", "", 1)    # the page header carries the title

    body, in_proj, toc, toc_after_next_p = [], False, [], False
    bl = blocks(md)
    k = 0
    while k < len(bl):
        kind, val = bl[k]
        if kind == "h3":
            num, name = val.split(". ", 1)
            row = by_num[int(num)]
            assert row["name"].split(" (")[0].replace("–", "-") in name, (name, row["name"])
            slug = row["slug"]
            stem = f"{int(num):02d}-{slug}"
            if in_proj:
                body.append("</section>")
            in_proj = True
            toc.append(f'<a href="#{slug}"><span>{num}</span>{html.escape(name)}</a>')
            meta = bl[k + 1][1].strip("*") if k + 1 < len(bl) and bl[k + 1][0] == "p" else ""
            w, h = sizes[stem]
            where = REGION.get(slug, "the world")
            body.append(f'<section class="proj" id="{slug}"><h3><span class="pn">{num}</span>{html.escape(name)}</h3>'
                        f'<p class="proj-meta">{inline(meta)}</p>'
                        f'<figure class="proj-fig"><img src="../map-projections/{stem}.webp" width="{w}" height="{h}" loading="lazy" '
                        f'alt="{html.escape(name)} projection of {where}, with coral circles that were all the same size on the globe, showing how the map distorts them."></figure>')
            k += 2
            continue
        if kind == "p" and val.startswith("*Scorecard"):
            body.append("@@SCORE@@")
            k += 1
            continue
        if kind == "h2":
            if in_proj:
                body.append("</section>"); in_proj = False
            body.append(f'<h2 id="{slugify(val)}">{inline(val)}</h2>')
            if val == "The twenty projections":
                toc_after_next_p = True
        elif kind == "p":
            if val == "`[INTERACTIVE]`":
                body.append(INTERACTIVE)
            else:
                body.append(f"<p>{inline(val)}</p>")
                if toc_after_next_p:
                    body.append("@@TOC@@"); toc_after_next_p = False
        elif kind == "ul":
            body.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in val) + "</ul>")
        elif kind == "table":
            body.append(table(val))
        k += 1
    if in_proj:
        body.append("</section>")

    # Fill scorecards in order of appearance from the CSV (never from the draft's text)
    order = [r for r in sorted(score.values(), key=lambda r: int(r["n"]))]
    it = iter(order)
    out = []
    for piece in body:
        if piece == "@@SCORE@@":
            r = next(it)
            note = f'<p class="score-note">{SCOPE[r["slug"]]}</p>' if r["slug"] in SCOPE else ""
            out.append(chips(r) + note)
        elif piece == "@@TOC@@":
            out.append('<nav class="proj-toc" aria-label="Jump to a projection">' + "".join(toc) + "</nav>")
        else:
            out.append(piece)
    content = "\n".join(out)
    content = content.replace("on GitHub <code>[LINK]</code>", f'on <a href="{REPO}">GitHub</a>')

    tpl = TEMPLATE.read_text()
    nav_hero = tpl[tpl.index("<body>"):tpl.index('<div class="blog-layout container">')]
    tail = tpl[tpl.index('    <aside class="blog-sidebar"'):]
    tail = tail.replace("</body>", SCRIPTS + "\n</body>")

    total = len(order)
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} &mdash; Brian Bergstrom</title>
<meta name="description" content="{html.escape(DESCRIPTION)}">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Brian Bergstrom">
<meta property="og:title" content="{TITLE} &mdash; Brian Bergstrom">
<meta property="og:description" content="{html.escape(DESCRIPTION)}">
<meta property="og:image" content="https://bergstromgis.com/images/map-projections.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{OG_ALT}">
<meta property="og:url" content="{URL}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE} &mdash; Brian Bergstrom">
<meta name="twitter:description" content="{html.escape(DESCRIPTION)}">
<meta name="twitter:image" content="https://bergstromgis.com/images/map-projections.jpg">
<link rel="icon" type="image/svg+xml" href="../favicon.svg">
<link rel="alternate icon" href="../favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="../favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="../favicon-16x16.png">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
<link rel="stylesheet" href="../css/brand.css">
<style>{STYLE}</style>
</head>
{nav_hero}<div class="blog-layout container">
  <div class="blog-main">
    <div class="container">
    <a class="breadcrumb" href="../work-personal.html">&larr; Back to personal work</a>

    <header class="project-header">
      <span class="tag tag-personal">Personal &mdash; Explainer</span>
      <h1>{TITLE}</h1>
      <p class="subtitle">{SUBTITLE}</p>
      <div class="meta-row">
        <span class="stat">{total} projections, about 2,500 years</span>
        <span class="stat">Drawn and measured in Python</span>
        <span class="stat">Sourced to USGS references</span>
      </div>
    </header>
  </div>

  <div class="project-hero-media">
    <div class="media-inner">
      <img src="../map-projections/00-contact-sheet.webp" alt="{OG_ALT}">
    </div>
  </div>

  <div class="project-body">
    <div class="figures">
      <div><b>{total}</b><span>Projections drawn</span></div>
      <div><b>155</b><span>Projection methods in PROJ</span></div>
      <div><b>5,291</b><span>Projected systems in EPSG</span></div>
      <div><b>{float(score['mercator']['greenland_exaggeration']):.1f}&times;</b><span>Greenland's inflation on Mercator</span></div>
    </div>

{content}

    <div class="evidence-panel">
      <p>The notebook that draws every map and computes every scorecard, the fact sheet with page-level
      citations for each history, and the data behind the slider are all in the repo.</p>
      <a class="btn btn-outline" href="{REPO}" target="_blank" rel="noopener">
        View the code <span class="visually-hidden">(opens in a new tab)</span>
      </a>
    </div>
  </div>
    </div>

{tail}"""
    PAGE.write_text(page)
    print(f"wrote {PAGE} ({PAGE.stat().st_size / 1024:.0f} KB), {len(sizes)} images into {ASSETS}")
    print("world.json present:", (ASSETS / "world.json").exists())


STYLE = """
  /* Page-local only. Every colour is a brand.css token. */
  .project-body figure { margin: 2rem 0 0.6rem; }
  .project-body .wide { max-width: none; width: min(100%, 1000px); }
  .project-body figcaption { font-size: 0.8rem; color: var(--text-muted); margin-top: 0.9rem; line-height: 1.55; max-width: 640px; }
  .scroll { overflow-x: auto; border: 1px solid var(--rule); background: var(--bg-raised); }
  .project-body table { border-collapse: collapse; width: 100%; font-size: 0.88rem; }
  .project-body th { font-size: 0.66rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--text-muted);
    text-align: left; padding: 0.8rem 0.85rem; border-bottom: 1px solid var(--rule); font-weight: 700; white-space: nowrap; }
  .project-body td { padding: 0.7rem 0.85rem; border-bottom: 1px solid var(--rule); vertical-align: top; }
  .project-body tbody tr:last-child td { border-bottom: none; }
  .project-body code { font-size: 0.85em; background: var(--bg-raised); padding: 0.05em 0.35em; border-radius: 3px; }

  .figures { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: var(--rule);
    border: 1px solid var(--rule); margin: 0 0 2rem; }
  .figures div { background: var(--bg-raised); padding: 1rem; }
  .figures b { display: block; font-family: var(--font-heading); font-size: 1.5rem; font-weight: 600;
    color: var(--text); font-variant-numeric: tabular-nums; }
  .figures span { display: block; font-size: 0.66rem; letter-spacing: 0.07em; text-transform: uppercase;
    color: var(--text-muted); margin-top: 0.35rem; line-height: 1.4; }
  .figures.score { grid-template-columns: repeat(3, 1fr); margin: 1.2rem 0 0.4rem; }
  .figures.score b { font-size: 1.2rem; }
  .score-note { font-size: 0.74rem; color: var(--text-muted); margin: 0 0 0.5rem; }
  @media (max-width: 720px) { .figures { grid-template-columns: repeat(2, 1fr); } .figures.score { grid-template-columns: repeat(3, 1fr); } }

  .proj { border-top: 1px solid var(--rule); padding-top: 2.2rem; margin-top: 2.6rem; scroll-margin-top: 1rem; }
  .proj h3 { display: flex; align-items: baseline; gap: 0.7rem; margin-bottom: 0.3rem; }
  .pn { font-family: var(--font-heading); color: var(--accent); font-variant-numeric: tabular-nums; }
  .proj-meta { font-size: 0.74rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 0; }
  .proj-fig img { display: block; width: 100%; height: auto; max-height: 560px; object-fit: contain; }

  .proj-toc { display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 1px;
    background: var(--rule); border: 1px solid var(--rule); margin: 1.4rem 0 1rem; }
  .proj-toc a { display: flex; gap: 0.6rem; align-items: baseline; background: var(--bg-raised); padding: 0.55rem 0.8rem;
    font-size: 0.84rem; color: var(--text); text-decoration: none; }
  .proj-toc a:hover, .proj-toc a:focus-visible { color: var(--accent); }
  .proj-toc span { font-family: var(--font-heading); color: var(--accent); min-width: 1.4em; font-variant-numeric: tabular-nums; }

  .morph .chart { background: var(--bg-raised); border: 1px solid var(--rule); padding: 1.1rem 1.1rem 0.9rem; }
  .morph-controls { display: grid; grid-template-columns: auto 1fr auto; gap: 0.9rem; align-items: center;
    font-size: 0.78rem; letter-spacing: 0.04em; color: var(--text-muted); }
  .morph-controls b { color: var(--text); font-weight: 600; }
  .morph-controls input[type=range] { width: 100%; accent-color: var(--accent); }
  #morphMap { display: block; width: 100%; height: auto; margin-top: 0.8rem; }
  #morphMap .ocean { fill: var(--bg); }
  #morphMap .grat { fill: none; stroke: var(--rule); stroke-width: 0.6; }
  #morphMap .land { fill: #4A3A30; }
  #morphMap .hi { fill: var(--accent); }
  #morphMap .edge { fill: none; stroke: var(--text-muted); stroke-width: 0.8; }
  .morph-readout { font-size: 0.95rem; margin: 0.8rem 0 0; min-height: 2.8em; }
  .morph-readout strong { color: var(--accent); font-variant-numeric: tabular-nums; }
"""

INTERACTIVE = """<figure class="wide morph">
  <div class="chart">
    <div class="morph-controls">
      <span><b>Mercator</b> 1569</span>
      <input type="range" id="morphT" min="0" max="1000" value="0" step="1" aria-label="Morph the map from Mercator to Equal Earth" aria-describedby="morphReadout">
      <span><b>Equal Earth</b> 2018</span>
    </div>
    <svg id="morphMap" viewBox="0 0 960 520" role="img" aria-label="World map that morphs from Mercator to Equal Earth, with Greenland and Africa highlighted"></svg>
    <p class="morph-readout" id="morphReadout" aria-live="polite">Loading the map&hellip;</p>
  </div>
  <figcaption>Drag the slider to morph the same world from Mercator into Equal Earth. Greenland and Africa
  are in coral. The land never changes, only the math that flattens it. Both maps are cut off at 60&deg;S and
  84&deg;N, because Mercator can't show the poles at all.</figcaption>
</figure>"""

SCRIPTS = """<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>
<script>
(function () {
  // Mercator to Equal Earth: blend the two projections' raw formulas by t, then refit.
  var W = 960, H = 520, LIM = 85 * Math.PI / 180;
  var svg = d3.select('#morphMap'), slider = document.getElementById('morphT'),
      readout = document.getElementById('morphReadout');
  if (!window.d3 || svg.empty()) return;
  var rawAt = function (t) {
    return function (x, y) {
      var c = Math.max(-LIM, Math.min(LIM, y));            // Mercator is infinite at the poles
      var a = d3.geoMercatorRaw(x, c), b = d3.geoEqualEarthRaw(x, y);
      return [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t];
    };
  };
  var mutate = d3.geoProjectionMutator(rawAt), proj = mutate(0), path = d3.geoPath(proj);
  var outline = d3.geoGraticule().extent([[-180, -60], [180, 84]]).outline();
  var grat = d3.geoGraticule().step([30, 30]).extent([[-180, -60], [180, 84]])();
  var ocean = svg.append('path').attr('class', 'ocean'),
      lines = svg.append('path').attr('class', 'grat'),
      layers = {}, edge;

  fetch('../map-projections/world.json').then(function (r) { return r.json(); }).then(function (world) {
    var f = {};
    world.features.forEach(function (d) { f[d.properties.name] = d; });
    layers.other = svg.append('path').attr('class', 'land').datum(f.other);
    layers.greenland = svg.append('path').attr('class', 'hi').datum(f.greenland);
    layers.africa = svg.append('path').attr('class', 'hi').datum(f.africa);
    edge = svg.append('path').attr('class', 'edge');
    var truth = f.greenland.properties.true_km2 / f.africa.properties.true_km2;

    function draw() {
      var t = +slider.value / 1000;
      mutate(t);
      proj.clipExtent(null).fitExtent([[6, 6], [W - 6, H - 6]], outline);
      var b = path.bounds(outline);
      proj.clipExtent(b);
      ocean.attr('d', path(outline));
      lines.attr('d', path(grat));
      Object.keys(layers).forEach(function (k) { layers[k].attr('d', path); });
      edge.attr('d', path(outline));
      var looks = path.area(f.greenland) / path.area(f.africa);
      var name = t === 0 ? 'Mercator' : t === 1 ? 'Equal Earth' : 'this in-between map';
      readout.innerHTML = 'On ' + name + ', Greenland looks <strong>' + Math.round(looks * 100) +
        '%</strong> the size of Africa. In reality it is <strong>' + Math.round(truth * 100) + '%</strong>.';
    }
    slider.addEventListener('input', draw);
    draw();
  }).catch(function () {
    readout.textContent = 'The interactive map could not load. The static maps below show the same comparison.';
  });
})();
</script>"""


if __name__ == "__main__":
    build()

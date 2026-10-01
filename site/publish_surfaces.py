"""Add the map-projections post to every bergstromgis.com surface that lists posts.

Safe to re-run: each step checks whether the post is already there. Following the
site's publish checklist, the homepage "Latest" grid and the calendar dates are
regenerated from blog.html rather than edited by hand, so they can't drift.
"""
import re
from pathlib import Path

DOCS = Path.home() / "gis-portfolio" / "docs"
HREF = "work/map-projections.html"
DATE, DATE_LONG = "2026-10-01", "October 1, 2026"
RFC822 = "Thu, 01 Oct 2026 14:00:00 GMT"
TITLE = "Every Map Is Wrong"
BLURB = ("Every flat map of the world distorts something. Twenty map projections, drawn and measured in "
         "Python, from ancient star charts to the equal-area map the UN voted for in September 2026, with "
         "the story of who made each one and what problem they were trying to solve.")
ALT = ("Twenty small world maps in a grid on a near-black background, each drawn in a different map "
       "projection, from Gnomonic to Equal Earth.")


def card(with_date):
    date_attr = f' data-date="{DATE}"' if with_date else ""
    return f"""      <article class="project-card"{date_attr}>
        <div class="card-media">
          <a href="{HREF}"><img src="images/map-projections.jpg" alt="{ALT}"></a>
        </div>
        <div class="card-body">
          <span class="post-date">{DATE_LONG}</span>
          <span class="tag tag-personal">Personal &mdash; Explainer</span>
          <h3>{TITLE}</h3>
          <p>{BLURB}</p>
          <a class="card-link" href="{HREF}">
            Read the story <span aria-hidden="true">&rarr;</span>
          </a>
        </div>
      </article>
"""


def blog():
    p = DOCS / "blog.html"; s = p.read_text()
    if HREF in s:
        return "blog.html: already listed"
    anchor = '<div class="project-grid" id="postGrid">\n\n'
    assert s.count(anchor) == 1
    p.write_text(s.replace(anchor, anchor + card(True)))
    return "blog.html: card added at the top"


def rss():
    p = DOCS / "rss.xml"; s = p.read_text()
    if HREF in s:
        return "rss.xml: already listed"
    item = f"""    <item>
      <title>{TITLE}</title>
      <link>https://bergstromgis.com/{HREF}</link>
      <guid isPermaLink="true">https://bergstromgis.com/{HREF}</guid>
      <pubDate>{RFC822}</pubDate>
      <description>{BLURB}</description>
    </item>
"""
    s = re.sub(r"<lastBuildDate>.*?</lastBuildDate>", f"<lastBuildDate>{RFC822}</lastBuildDate>", s, count=1)
    i = s.index("    <item>")
    p.write_text(s[:i] + item + s[i:])
    return "rss.xml: item added, lastBuildDate bumped"


def blog_cards():
    s = (DOCS / "blog.html").read_text()
    return re.findall(r"      <article class=\"project-card\" data-date=\"[^\"]+\">.*?</article>\n", s, re.S)


def homepage():
    p = DOCS / "index.html"; s = p.read_text()
    a = s.index('<div class="project-grid">', s.index('aria-label="Latest posts"')) + len('<div class="project-grid">')
    b = s.index("        </div>\n\n        <p class=\"see-all\">", a)
    latest = [re.sub(r' data-date="[^"]+"', "", c) for c in blog_cards()[:6]]
    p.write_text(s[:a] + "\n\n" + "".join(latest) + s[b:])
    titles = [re.search(r"<h3>(.*?)</h3>", c).group(1) for c in latest]
    return "index.html Latest regenerated from blog.html: " + " | ".join(titles)


def calendar():
    p = DOCS / "js" / "blog-post-data.js"; s = p.read_text()
    dates = re.findall(r'data-date="([^"]+)"', (DOCS / "blog.html").read_text())
    body = "window.BLOG_POST_DATES = [\n" + "".join(f'  "{d}",\n' for d in dates).rstrip(",\n") + "\n];"
    s = re.sub(r"window\.BLOG_POST_DATES = \[.*?\];", body, s, flags=re.S)
    p.write_text(s)
    return f"blog-post-data.js: {len(dates)} dates, newest {dates[0]}"


def personal():
    p = DOCS / "work-personal.html"; s = p.read_text()
    if HREF in s:
        return "work-personal.html: already listed"
    i = s.index('      <article class="project-card">')
    c = re.sub(r" *<span class=\"post-date\">.*?</span>\n", "", card(False))
    p.write_text(s[:i] + c + "\n" + s[i:])
    return "work-personal.html: card added at the top"


def sitemap():
    p = DOCS / "sitemap.xml"; s = p.read_text()
    if HREF in s:
        return "sitemap.xml: already listed"
    url = f"  <url>\n    <loc>https://bergstromgis.com/{HREF}</loc>\n    <lastmod>{DATE}</lastmod>\n  </url>\n"
    p.write_text(s.replace("</urlset>", url + "</urlset>"))
    return "sitemap.xml: page added"


if __name__ == "__main__":
    for step in (blog, rss, homepage, calendar, personal, sitemap):
        print(step())

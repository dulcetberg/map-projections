# Map projections: verified fact sheet

Research notes for a general-audience blog story (bergstromgis.com). Not prose. Compiled 2026-10-01.

Confidence labels used below:
- **Documented**: the creator's own publication, or a dated primary artifact, survives and is cited by the sources.
- **Traditionally attributed**: the standard references repeat the attribution, but no surviving text by that person proves it.
- **Disputed**: reputable sources disagree.

Citation shorthand: `S87 p.N` = Snyder 1987 printed page N (PDF page = N + 12). `S89 p.N` = Snyder 1989 printed page N (PDF page = N + 10). `HoC3 p.N` = Snyder 2007 chapter, printed page N. Everything else is a URL.

---

## Sources

**Primary references (read directly for this sheet)**
- **S87**: Snyder, John P. 1987. *Map Projections: A Working Manual*. USGS Professional Paper 1395. Public domain. https://pubs.usgs.gov/pp/1395/report.pdf
- **S89**: Snyder, John P., and Philip M. Voxland. 1989. *An Album of Map Projections*. USGS Professional Paper 1453. Public domain. Each projection has a one-page "Origin / Usage" entry. https://pubs.usgs.gov/pp/1453/report.pdf
- **HoC3**: Snyder, John P. 2007. "Map Projections in the Renaissance." In *The History of Cartography*, vol. 3, part 1, ed. David Woodward, ch. 10, pp. 365-381. University of Chicago Press (free PDF). https://press.uchicago.edu/books/hoc/HOC_V3_Pt1/HOC_VOLUME3_Part1_chapter10.pdf
- **PROJ**: PROJ documentation, projection pages. https://proj.org/en/stable/operations/projections/
- **EPSG**: EPSG registry data, read through mirrors: https://spatialreference.org/ref/epsg/3035/ , https://spatialreference.org/ref/epsg/3857/ , https://spatialreference.org/ref/epsg/5070/ , https://epsg.io/3857 (epsg.org itself returned 403 to the fetcher)
- **NGA 2015**: Rollins, C., and M. Paniccia. 2015. "NGA's Position on 'Web-Mercator'." NGA Office of Geomatics, Esri UC slides, approved for public release 15-519. https://www.sedris.org/wg8home/Documents/WG80605.pdf
- **NGEd**: National Geographic Education, "Selecting a Map Projection." https://education.nationalgeographic.org/resource/selecting-map-projection/
- **AP 1988**: AP wire story, "Geographic Society Unveils Map of World That's 'More Realistic'," *Deseret News*, 14 Oct 1988. https://www.deseret.com/1988/10/14/18781372/geographic-society-unveils-map-of-world-that-s-more-realistic/
- **UN emblem**: United Nations, "UN Emblem and Flag." https://www.un.org/en/about-us/un-emblem-and-flag
- **UN 2026**: UN News, "UN tells the world: Stop making Africa look small," 4 Sep 2026 (resolution A/80/L.104). https://news.un.org/en/story/2026/09/1168284
- **MODLAND**: NASA MODIS Land, "MODIS Sinusoidal grid." https://modis-land.gsfc.nasa.gov/MODLAND_grid.html
- **GISS**: NASA GISS, GISTEMP animations page. https://data.giss.nasa.gov/gistemp/animations/
- **LAMBDA**: NASA LAMBDA, WMAP first-year image page. https://lambda.gsfc.nasa.gov/product/wmap/pub_papers/firstyear/basic/wmap_cb1_images.html
- **Google**: Google Maps JavaScript API, "Map and Tile Coordinates." https://developers.google.com/maps/documentation/javascript/coordinates
- **Sidoli & Berggren 2007**: "The Arabic version of Ptolemy's Planisphere." *SCIAMVS* 8: 37-139. http://individual.utoronto.ca/acephalous/Sidoli_Berggren_2007.pdf
- **Papadopoulos 2016**: "Euler and Chebyshev: From the sphere to the plane and backwards." arXiv:1608.02724. https://arxiv.org/abs/1608.02724
- **Papadopoulos 2021**: "Mathematics and map drawing in the eighteenth century." arXiv:2111.11245. https://arxiv.org/abs/2111.11245
- **Favretto 2021**: "Arno Peters and 'his' equal area projection." *Abstracts of the ICA* 3: 75. https://doi.org/10.5194/ica-abs-3-75-2021
- **ICA 2019**: Šavrič, Patterson, Jenny, "The Equal Earth Projection: Distortion Characteristics, Adoption, and (Social) Media Impact." *Abstracts of the ICA* 1: 321. https://ica-abs.copernicus.org/articles/1/321/2019/

**Cited but not read directly** (bibliographic details confirmed; content known only through the sources above)
- Šavrič, B., T. Patterson, and B. Jenny. 2019. "The Equal Earth map projection." *IJGIS* 33(3): 454-465. https://doi.org/10.1080/13658816.2018.1504949 (publisher page returned 403; details confirmed via PROJ and ADS: https://ui.adsabs.harvard.edu/abs/2019IJGIS..33..454S/abstract)
- Snyder, John P. 1993. *Flattening the Earth: Two Thousand Years of Map Projections*. Univ. of Chicago Press. (Not online. Cited through HoC3 and Wikipedia footnotes only.)
- Crampton, Jeremy. 1994. "Cartography's Defining Moment: The Peters Projection Controversy, 1974-1990." *Cartographica* 31(4): 16-32.
- Robinson, Arthur H. 1974. "A New Map Projection: Its Development and Characteristics." *International Yearbook of Cartography* 14: 145-155 (cited in S89).
- Robinson, Arthur H. 1990. "Rectangular World Maps - No!" *Professional Geographer* 42(1): 101-104 (contains the 1989 resolution; not retrieved).
- Annoni, A., C. Luzet, E. Gubler, J. Ihde, eds. 2003. *Map Projections for Europe*. EUR 20120 EN, JRC. https://mapref.org/LinkedDocuments/MapProjectionsForEurope-EUR-20120.pdf (located, not read)
- Berggren, J. L. "Al-Bīrūnī on plane maps of the sphere." *Journal for the History of Arabic Science* (early 1980s; volume and pages vary between citations, so check before citing).

---

## General background (for the intro)

**No perfect flat map**
- Snyder states it flatly: "No map can be both equal-area and conformal." [S87 p.4]
- Gauss presented *Disquisitiones generales circa superficies curvas* to the Göttingen Royal Society on 8 Oct 1827; it was printed in 1828. It contains the *Theorema Egregium*: a surface's (Gaussian) curvature can be measured from distances within the surface alone. https://www.gutenberg.org/files/36856/36856-pdf.pdf ; https://proofwiki.org/wiki/Theorema_Egregium/Historical_Note
- **Precision note:** the theorem says no map from sphere to plane can preserve all distances, even up to a constant scale. The "can't keep both area and shape" result follows from it: a map that is both conformal and equal-area would preserve local distances everywhere, which the theorem rules out. Better wording: "Gauss's 1827 theorem proved that no flat map can keep every distance true. One consequence is that no map can preserve both areas and shapes." Avoid saying Gauss "proved maps must distort area or shape" as if that were the theorem's statement.
- **Euler came first:** in 1777 Euler published *De repraesentatione superficiei sphaericae super plano*. It starts from the fact that no "perfect" or "exact" map of the sphere onto a plane exists, so cartographers must seek best approximations. [Papadopoulos 2016]
- In §9 of that memoir Euler proves that no such "perfect" map exists. Here "perfect" means distances are preserved locally along meridians and parallels *and* the right angles between them are kept.
- Later authors misquoted this as "no map preserves distances up to scale." Papadopoulos notes that weaker fact "was well-known long before Euler." [Papadopoulos 2021, section on Euler's 1777 memoirs]
- Safe wording: "Euler proved in 1777 that a sphere can't be flattened onto a plane without distortion."

**Tissot's indicatrix**
- "In 1859 and 1881, Nicolas Auguste Tissot published a classic analysis of the distortion which occurs on a map projection." An infinitely small circle on the Earth projects as an infinitely small ellipse on the map. On a conformal map it stays a circle; on an equal-area map every ellipse has the same area. [S87 p.20]
- Tissot (1824-1897) was a French mathematician. His work is considered a precursor of 20th-century quasiconformal mapping theory. https://arxiv.org/abs/2001.03434
- S89 shows every projection with Tissot indicatrices, which makes it a good source for figures (public domain). [S89 throughout, e.g. p.10 fig. 1A]

**Web Mercator (EPSG:3857)**
- Google Maps launched on 8 Feb 2005 (widely reported; launch day itself not checked against a Google primary source). Google's API documentation confirms the Mercator projection, with imagery cut off at about ±85° "to make the resulting map shape square, which allows easier logic for tile selection." Zoom level 0 is a single 256×256 tile. [Google]
- What it is: ellipsoidal (WGS 84) latitude and longitude fed into the simpler *spherical* Mercator formula. [NGA 2015, slides 4, 7]
- **It is not conformal.** PROJ classifies it as "Cylindrical (non conformant if used with ellipsoid)." https://proj.org/en/stable/operations/projections/webmerc.html . The EPSG remark reads: "Not a recognised geodetic system. Uses spherical development of ellipsoidal coordinates. Relative to WGS 84 / World Mercator (CRS code 3395) gives errors of 0.7 percent in scale and differences in northing of up to 43km in the map (21km on the ground)." [https://epsg.io/3857]
- EPSG scope field: "Web mapping and visualisation." Area: between 85.06°S and 85.06°N. [EPSG via spatialreference.org/ref/epsg/3857]
- NGA (US National Geospatial-Intelligence Agency) issued a technical document (NGA.SIG.0011_1.0_WEBMERC, 18 Feb 2014) and an Advisory Notice on "Web Mercator" (22 May 2014). It calls Web Mercator non-conformal and says it conflicts with Mercator nautical charts. It shows northing differences of about 33 km at 50°N and 36.7 km at 59°N against true Mercator. [NGA 2015, slides 2, 15, 20]
- Why the web uses it: NGA summarizes the case as "Better than Plate Carrée; simpler than true (ellipsoidal) Mercator," "almost conformal," with a fast and exact inverse. [NGA 2015, slides 4, 10]. A Google Maps designer gave the reason that "north and south are straight up and down, and east and west are straight left and right" (Antin Harasymiv, Google Design, 27 Aug 2018, https://medium.com/google-design/google-maps-cb0326d165f5 ; read via a translation proxy).
- EPSG code history: the unofficial code "900913" (GOOGLE spelled in digits) came first; EPSG then issued 3785 (2008), then 3857. This comes from Wikipedia's Web Mercator article (https://en.wikipedia.org/wiki/Web_Mercator_projection), which cites EPSG documents I could not open. Treat the exact dates as secondary.
- Fun, checkable detail: in August 2018 Google Maps on desktop switched to a 3D globe when fully zoomed out. Google's tweet said Greenland "is no longer the size of Africa." https://techcrunch.com/2018/08/03/google-maps-is-no-longer-flatearth/ (secondary news report; the tweet itself was not checked)

**Big-picture context (useful hook, verified)**
- On 4 Sep 2026 the UN General Assembly adopted resolution A/80/L.104, "Correct the map," by 164 to 1 (United States against; Estonia, Georgia, Lithuania, Moldova, Serbia and Ukraine abstaining). It *encourages* governments, schools, international organizations and tech companies to use Equal Earth and other equal-area maps "when relative size matters." It "does not ban the Mercator projection or impose a replacement." [UN 2026]
- The resolution built on the #CorrectTheMap campaign by Africa No Filter and Speak Up Africa, which the African Union endorsed on 14 Aug 2025 (per Fortune). https://fortune.com/2025/08/23/africa-map-mercator-projection-greenland-projection/

---

## 1. Gnomonic

- **Creator/date:** **traditionally attributed** to Thales of Miletus (c. 6th c. BC), for star maps. S87 states it flatly ("It was used by Thales ... for star maps") [S87 p.164]. Snyder's own later Album hedges: "Possibly developed by Thales (c. 580 B.C.)" [S89 p.116]. No surviving text by Thales describes it.
- **Name:** called "horologium" (sundial) in early times. The name "gnomonic" was applied in the 19th century. The meridians fan out like the hour lines of a sundial for the same latitude, and the gnomon is the sundial's shadow-casting edge. [S87 p.164]
- **Why:** sundial design. In the Renaissance it "was used exclusively for sundials." The angles between hour marks on a sundial for a given latitude equal the angles between meridians on a gnomonic map centered at that latitude. [HoC3 p.366, pp.379-380]
- **Properties:** azimuthal; perspective (projected from the globe's center). Neither conformal nor equal-area. Its one special property: **every great circle (shortest route) is a straight line**. It cannot show even a full hemisphere. [S87 p.164; S89 p.116]
- **Uses:** plotting great-circle routes for navigators and aviators [S89 p.116]; star maps (Kepler used the equatorial aspect for a star map of 1606) [HoC3 p.379]; cube-faced globes and star maps of the late 18th to early 19th c. [S87 p.164-165]. The USGS has never used it for published maps. [S87 p.165]
- **Interesting:** the earliest known geographic (Earth) gnomonic map is an oblique gnomonic centered near Nuremberg, published by Franz Ritter in 1610 as a sundial design. [HoC3 pp.379-380, fig. 10.13]

## 2. Stereographic

- **Creator/date:** **traditionally attributed** to Hipparchus (2nd c. BC). S87: "Hipparchus was apparently the first Greek to use it. He is generally considered its inventor." [S87 p.154]. S89 hedges: "Apparently developed in polar aspect by Egyptians and Greeks by the 2d century B.C." [S89 p.120]. HoC3: "The principles of the stereographic were known to Hipparchus, and Ptolemy wrote a manual on its use, the *Planisphaerium*." [HoC3 p.378]
- **Earliest surviving text:** Ptolemy's *Planisphaerium* (2nd c. AD), "the first known treatise" on the method. Its methods "probably go back at least as far as Hipparchus" (citing Neugebauer 1975). [Sidoli & Berggren 2007, p.37-38]. The Hipparchus link rests on a later, ambiguous remark by Synesius (c. AD 400) (via Wikipedia's stereographic article; not checked against Synesius).
- **Name:** called *planisphaerium* into the 16th c. François d'Aiguillon named it "stereographic" in 1613. [S87 p.154; HoC3 p.376]
- **Why:** astronomy. It was the geometry behind the astrolabe's star map, because it is conformal and maps every circle on the sky to a circle. [HoC3 p.378]
- **Properties:** azimuthal; perspective (from the point opposite the center); **conformal**. "It is the only known true perspective projection of any kind that is also conformal." [S87 p.154]
- **Uses:**
  - Earliest known world map on the polar aspect: Walter (Gaultier) Lud of St-Dié, 1507. [S87 p.154; HoC3 p.367]
  - Equatorial aspect on an astrolabe by al-Zarqālī (Azarquiel) of Toledo, 11th c.; first world map Jean Rotz 1542; popularized by Rumold Mercator's two-hemisphere map (1587, in the 1595 atlas). [HoC3 pp.367, 378; S87 p.154]
  - Modern: polar aspect for Antarctica maps (USGS); the **Universal Polar Stereographic (UPS)** grid covers the poles beyond UTM (north of 84°N, south of 80°S); polar sheets of the International Map of the World since 1962; USGS planetary polar maps. [S87 pp.156-157]

## 3. Orthographic

- **Creator/date:** **traditionally attributed.** S87: "The Egyptians were probably aware of the Orthographic projection, and Hipparchus ... used the equatorial aspect for astronomical calculations." [S87 p.145]. S89: "Apparently developed by Egyptians and Greeks by the 2d century B.C." [S89 p.124]
- **Name:** early name "analemma" (also used by Ptolemy). d'Aiguillon renamed it "orthographic" in 1613. [S87 p.145]
- **Why:** astronomical calculation (sundials and sky geometry). [S87 p.145]
- **Properties:** azimuthal; perspective from infinite distance. Neither conformal nor equal-area. Shows one hemisphere and looks like a globe. [S87 p.145; S89 p.124]
- **Uses:** world maps from the 16th c. (S87 credits Albrecht Dürer [S87 p.145]; but see the caution below); WWII "global" maps by Richard Edes Harrison; Rand McNally relief globes since 1960; USGS frontispieces. [S87 p.146]. Today: "Pictorial views of the Earth, resembling those seen from space." [S89 p.124]
- **Caution (Dürer):** HoC3 argues that the 1515 Stabius-Dürer globe often called orthographic is more likely a finite-distance *perspective* projection: it shows only 150° of longitude instead of 180°. [HoC3 p.366]. Don't cite Dürer as the first orthographic world map.

## 4. Equirectangular (Plate Carrée)

- **Creator/date:** **traditionally attributed / disputed.** Ptolemy credited Marinus of Tyre (c. AD 100). Snyder says it "originated probably with Eratosthenes (275?-195? B.C.)." [S87 p.90; S89 p.22: "May have been originated by Eratosthenes ... Marinus of Tyre also credited with its invention"]
- **Marinus's version was not the square grid.** He made the parallel of Rhodes (36°N) true to scale, so meridians were spaced about 4/5 as far apart as parallels. Ptolemy wrote that Marinus chose "a manner of representing the distances which gives the worst results of all." [S87 p.90]. The square version (Equator true to scale) is the one called Plate Carrée. [S87 p.90]
- **Why:** the simplest possible graticule to draw. "Probably the simplest of all map projections to construct and one of the oldest." [S87 p.90]
- **Properties:** cylindrical; equidistant along meridians (and along the standard parallel). Neither conformal nor equal-area. [S87 p.90; S89 p.22-24]
- **Uses:** many 15th- and 16th-c. maps and the "plane chart" of 16th-c. sailors (e.g., Diogo Ribeiro 1529) until Mercator's projection caught on [S89 p.22; HoC3 p.375]; USGS index maps (with Marinus-like 4/5 spacing "by coincidence") [S87 p.90]. Today it is standard for global rasters because each pixel row/column maps directly to latitude and longitude; e.g. NASA Blue Marble Next Generation is "Plate Carrée" (NASA Earth Observatory PDF, https://earthobservatory.nasa.gov/ContentFeature/BlueMarble/bmng.pdf ; seen in search snippet only).
- **Name trivia:** also called "Projection of Marinus," "La Carte Parallélogrammatique," "Die Rechteckige Plattkarte." [S87 p.90; S89 p.24]

## 5. Azimuthal Equidistant

- **Creator/date:** **traditionally attributed / unclear.** S87: "It is believed that Egyptians used the polar aspect for star charts." [S87 p.191]. S89: "Possibly developed in the polar aspect by Egyptians for star charts." [S89 p.132]
- **al-Bīrūnī:** Wikipedia says "the earliest text describing" the projection is an 11th-c. work by al-Bīrūnī and cites Snyder 1993, p.29. **Not verified directly**; Snyder 1987/1989 and HoC3 don't mention al-Bīrūnī for this projection. al-Bīrūnī is firmly credited with a different projection, the *globular* one later reinvented by Nicolosi (Snyder 1993 p.41, via Wikipedia). If you use the azimuthal equidistant attribution, phrase it as "described in an 11th-century treatise by al-Bīrūnī, according to Snyder."
- **Documented early uses:** oldest existing celestial map on it: Conrad of Dyffenbach, 1426 [S87 p.191; HoC3 p.367]; terrestrial hemispheres by Glareanus c. 1510 [S87 p.191; HoC3 p.368]; polar insets on Mercator's 1569 world map [S87 p.191]; first north-polar AzEq map of the whole world: Louis de Mayerne Turquet, 1648. The world map on the floor of the Paris Observatory (1680s) uses it. [HoC3 p.368]
- **Name trivia:** called the "Postel" projection in France and Russia after Guillaume Postel, "although he first used it in 1581." [S89 p.132; S87 p.191]
- **Why:** distances and directions from the center point are both true. [S87 p.191]
- **Properties:** azimuthal; equidistant *from the center point only*. Neither conformal nor equal-area. [S87 p.191; S89 p.132]
- **Uses:** polar maps in atlases; "aviation-age" world maps centered on a city; polar insets on NGS Van der Grinten world maps; ellipsoidal form for Guam and Micronesia grids. [S87 p.194; S89 p.132]
- **UN emblem:** "a map of the world representing an azimuthal equidistant projection centred on the North Pole." Designed at the 1945 San Francisco conference by a team led by Oliver Lincoln Lundquist. The flag was approved by GA resolution 167 (II), 20 Oct 1947. [UN emblem]

## 6. Sinusoidal

- **Creator/date:** **unknown inventor; earliest documented use** Jean Cossin of Dieppe, world map, 1570. [S87 p.243; HoC3 p.372]. HoC3: "The origin of this projection has been variously reported."
- **Names:** "Sanson-Flamsteed" after Nicolas Sanson (continental maps c. 1650) and John Flamsteed (star charts). Neither was the originator. "Mercator Equal-Area" comes from Hondius's use in editions of Mercator's atlas, 1606-09. [S87 p.243; HoC3 p.372]
- **Why:** simple construction with correct areas: true scale along the central meridian and along every parallel. [HoC3 p.372; S87 p.243]
- **Properties:** pseudocylindrical; equal-area. "Oldest current pseudocylindrical projection." [S89 p.37]
- **Uses:** atlas maps of South America and Africa (Rand McNally) [S87 p.243]; Goode interrupted it in 1916 [S87 p.247]. **MODIS:** "Most of the higher resolution MODIS land products are produced in the Sinusoidal tile grid." The tiles are 10°×10° at the Equator, 460 non-fill tiles, numbered h00v00 to h35v17. [MODLAND]. Equal area makes it a good storage grid (MCD43 user guide: https://www.umb.edu/spectralmass/modis-user-guide-v006-and-v0061/introduction/).

## 7. Mercator

- **Creator/date:** **documented.** Gerardus Mercator (1512-94), 1569 world map titled *Nova et Aucta Orbis Terrae Descriptio ad Usum Navigantium Emendate Accommodata* ("...corrected for use in navigation"). [S87 p.38]. Eighteen sheets, mounted in 21 sections, about 1.3 × 2 m. [HoC3 pp.376-377; S87 p.38]
- **Why:** navigation. Every rhumb line (line of constant compass bearing) is straight. Mercator's own legend says the meridians had to become parallel "for the maps hitherto produced by geographers are ... unsuitable for navigation," so he "increased the degrees of latitude toward each pole." [S87 p.38]
- **How he did it:** "Mercator probably determined the spacing graphically, since tables of secants had not been invented." [S87 p.38; HoC3 p.377]
- **Edward Wright:** in *Certaine Errors in Navigation* (1599; rev. 1610, 1657) Wright published a "Table of Latitudes" giving each parallel's distance from the Equator in one-minute steps. HoC3 says he worked "apparently independently." His accuracy, "and possibly national pride," led Edmond Halley and others to credit Wright with the invention. [HoC3 p.378; S87 p.38]
- **Precursor:** Erhard Etzlaub's small Europe/Africa maps on sundial covers (1511, 1513) have similarly increasing latitude spacing. [S87 p.38; HoC3 p.380]. But HoC3 says "because the map functioned as a sundial and not a map for the use of navigators, any direct link is unlikely." [HoC3 p.380, fig. 10.14 caption]
- **Properties:** cylindrical; **conformal**; rhumb lines straight; poles at infinity. [S87 p.38-39; S89 p.10]
- **Uses:** standard for US Coast and Geodetic Survey (now NOS) nautical charts since 1910 [S87 p.39]; "standard for marine charts" [S89 p.10]. Adoption was slow at first: Plancius (1592 patent), Blaeu (1606-07). [HoC3 p.378]
- **Geographic use was not Mercator's intent:** HoC3 calls its spread to general world maps "a use unintended by Mercator," while noting it shows Europe at about twice its true area relative to equatorial countries. [HoC3 p.378]. S89: "Often and inappropriately used as a world map in atlases and for wall charts." [S89 p.10]
- **Interesting:** Mercator is also credited with first using "atlas" for a bound collection of maps, and with first naming North America on a map (1538). [S87 p.38]

## 8. Bonne

- **Creator/date:** **named for, not invented by**, Rigobert Bonne (1727-95). Rudimentary form in Ptolemy; Bernardus Sylvanus's 1511 world map comes close; De l'Isle and Coronelli used the principle around 1700. Bonne used it "most notably for a 1752 maritime atlas of the coast of France." [S87 p.138; S89 p.112]
- **Lineage:** its polar limiting case is the heart-shaped Werner (Stabius-Werner) projection, c. 1514. Bonne's version centers the projection on the region being mapped, which reduces distortion, and it eventually made Werner obsolete. [S87 p.138; HoC3 p.371]
- **Why:** equal-area maps of continents and regions with low distortion near the center. [S87 p.138]
- **Properties:** pseudoconic; **equal-area**; true scale along the central meridian and every parallel. [S87 p.138]
- **Uses:** the ellipsoidal version replaced the Cassini projection for French topographic mapping starting in 1803 [S87 p.138]; continental atlas maps in the late 19th and early 20th c. [S87 p.138; S89 p.112: "Frequently used until recently for atlas maps of continents"]

## 9. Lambert Conformal Conic

- **Creator/date:** **documented.** Johann Heinrich Lambert (1728-77), "the first new projection" in his 1772 *Beiträge*. [S87 p.104]. Lambert presented seven new projections in this work, including the Transverse Mercator, Cylindrical Equal-Area, and Azimuthal Equal-Area. [S87 p.48]
- **Why:** mathematical curiosity about a family. Lambert asked whether the polar stereographic and Mercator, "so different in appearances," are the two ends of a continuous family of conformal maps. They are, and the LCC sits between them. [S87 p.105, quoting Lambert 1772 p.28, Tobler translation]
- **Properties:** conic; **conformal**; one or two standard parallels. [S87 p.105]
- **Revival:** "almost completely overlooked" until the US Coast and Geodetic Survey revived it (Deetz 1918). France used an approximate "Lambert" version for WWI battle maps. [S87 p.104]
- **Uses:**
  - **State Plane Coordinate System:** prototype North Carolina 1933; LCC for states with mainly east-west extent [S87 p.106; table of zones S87 p.52]
  - USGS aeronautical charts, 1:1,000,000 world aeronautical and 1:500,000 sectional [S87 p.106]. The FAA *Aeronautical Chart User's Guide* (per search snippet; not opened) gives sectional standard parallels of 33°20' and 38°40'
  - USGS State base maps at 1:500,000 (parallels 33° and 45°) [S87 p.106]
  - International Map of the World since 1962 [S87 p.106]
  - most post-1957 USGS 7.5-minute quads in LCC zones [S87 p.106; S89 p.95]

## 10. Lambert Azimuthal Equal-Area (LAEA)

- **Creator/date:** **documented.** Lambert, 1772, *Beiträge* pp.75-78, "the last major projection" in that work. [S87 p.182; S89 p.136]
- **Independent reinvention:** Lorgna in Italy derived the polar aspect independently in 1789 and was called the originator in an 1882 US C&GS publication. [S87 p.182]
- **Why:** an azimuthal map (true directions from the center) that is also equal-area. It is not perspective; Snyder calls it "synthetic." [S87 p.182]
- **Properties:** azimuthal; **equal-area**. Of the major azimuthals, its scale varies least away from the center. [S87 p.182]
- **Uses:** atlas maps of hemispheres, continents and oceans; USGS Pacific Ocean base maps; NGS/USGS Moon maps [S87 pp.182, 184; S89 p.136]. Hammer's 1892 world projection is derived from it. [S87 p.182]
- **EPSG:3035** "ETRS89-extended / LAEA Europe." EPSG scope: "Statistical analysis." Center 52°N, 10°E. [EPSG 3035 via spatialreference.org]
- **Nerdy, verified detail:** EPSG:3035's false easting and northing are **4,321,000 m and 3,210,000 m**, which makes its coordinates easy to recognize. [EPSG 3035 projjson]
- The European recommendation comes from the JRC report *Map Projections for Europe* (Annoni et al. 2003, EUR 20120); found, not read.

## 11. Transverse Mercator / UTM

- **Creator/date:** **documented.** Lambert, 1772 (spherical form), the third of his seven projections. He described it "as a conformal adaptation of the Sinusoidal." [S87 p.48]
- **Ellipsoidal development:** C. F. Gauss analyzed it in 1822. L. Krüger published practical formulas in 1912 and 1919, hence the name "Gauss-Krüger." The name "Transverse Mercator" was first applied by the French writer Germain. [S87 p.48; S89 p.12]
- **Why:** like Mercator turned 90°: conformal, with a north-south central meridian at true scale, so distortion stays low in a narrow north-south band. [S87 p.48]
- **Properties:** cylindrical (transverse); **conformal**. [S87 p.48-49]
- **Early neglect:** the 1911 *Encyclopaedia Britannica* omitted it as "seldom used." [S87 p.51]
- **Now:** "probably used more than any other one projection for geodetic mapping." [S87 p.51]. SPCS uses it for states with mainly north-south extent. [S87 p.51]
- **UTM:** "adopted by the U.S. Army in 1947 for designating rectangular coordinates on large-scale military maps of the entire world." [S87 p.57]
  - 60 zones, each 6° wide, from 84°N to 80°S
  - central-meridian scale 0.9996
  - false easting 500,000 m; southern-hemisphere false northing 10,000,000 m
  - UPS covers the poles [S87 pp.57-58]
  - UTM superseded the Polyconic-based Progressive Military Grid and World Polyconic Grid. [S87 p.127]
- **Current:** all USGS US Topo maps are projected in UTM (USGS FAQ via search snippet: https://www.usgs.gov/programs/national-geospatial-program/us-topo-maps-america ; not opened).

## 12. Albers Equal-Area Conic

- **Creator/date:** **documented.** Heinrich Christian Albers (1773-1833), 1805, in Zach's *Monatliche Correspondenz* (Nov., pp. 450-459). [S87 p.98 and reference list]
- **Why:** an equal-area conic with two standard parallels, for mid-latitude regions wider east-west than north-south. [S87 p.98]
- **Properties:** conic; **equal-area**. [S87 p.98; S89 p.100]
- **Uses:**
  - Used for a German map of Europe in 1817. Promoted for US maps by Oscar S. Adams of the C&GS as "an equal-area representation that is as good as any other and in many respects superior to all others" (Adams 1927). [S87 p.98]
  - USGS used it exclusively for state sectional maps in the 1970 National Atlas and for US maps at 1:2,500,000 and smaller (base maps 1961, 1967, 1972; Tectonic Map 1962; Geologic Map 1974). [S87 p.98]
- **Today:** EPSG:5070 "NAD83 / Conus Albers," parallels 29.5° and 45.5°, central meridian 96°W. EPSG scope: "Data analysis and small scale data presentation for contiguous lower 48 states." [EPSG 5070 projjson]. The Census Bureau's own GIS base-map service is defined in "NAD83_Albers_Equal_Area_Conic_Projection_United_States" with the same 29.5/45.5 parallels (seen in a gis.geo.census.gov MapServer request; I found no Census policy page saying "we use Albers").

## 13. Mollweide

- **Creator/date:** **documented.** Carl B. Mollweide (1774-1825) of Halle, 1805, in Zach's *Monatliche Correspondenz* v.13, pp.152-163. The article's title shows it was a response to a hemisphere projection given in Prof. Schmidt's physics handbook. [S87 p.249 and reference list]
- **Revival and names:** "lay dormant" until Jacques Babinet reintroduced it in 1857 as "homalographic." Also called Babinet, Elliptical, and Homolographic. [S87 p.249; S89 p.54]
- **Why:** an equal-area map of the whole Earth inside an ellipse. [S87 p.249]
- **Properties:** pseudocylindrical; **equal-area**. Only two points are distortion-free: 40°44'12"N and S on the central meridian. [S87 p.249]
- **Influence:** inspired Goode's Homolosine, Van der Grinten, and Boggs Eumorphic. Bartholomew's transverse "Atlantis" version appears in *The Times Atlas* (1958). [S87 p.249]
- **CMB maps:** NASA's WMAP full-sky images are "projected in Mollweide projection with the galactic center in the middle." [LAMBDA]. Planck maps commonly use Mollweide too. I saw that in search snippets only; the ESA page I opened didn't name the projection, so cite WMAP.

## 14. Polyconic (American Polyconic)

- **Creator/date:** **traditionally attributed / probable.** Ferdinand Rudolph Hassler (1770-1843), first head of the Survey of the Coast, began promoting it "shortly before 1820." [S87 p.124]. S89: "Apparently originated about 1820." [S89 p.106]. Hassler described the principle in print in 1825 (Am. Philosophical Soc. Trans., pp.407-408). [S87 p.124]
- **Why:** surveying the US coast in pieces. In Hassler's words, an "assemblage of sections of surfaces of successive cones" that "appeared to me the only one applicable to the coast of the United States." [S87 p.124]. Easy to build from universal tables. [S87 p.128]
- **Properties:** polyconic: each parallel is the arc of its own tangent cone, which gives the name. Neither conformal nor equal-area. True scale along the central meridian and every parallel. [S87 p.124]
- **Uses:**
  - Most 19th-c. Coast Survey charts [S87 p.126]
  - The USGS used it from soon after its founding in 1879 [S87 p.2]. S89: "The sole projection used for large-scale mapping ... by the U.S. Geological Survey until the 1950's." [S89 p.106]
  - **Precise end date:** when SPCS plotters and tables became available "in the late 1950's, the USGS ceased using the Polyconic for new maps." Some later quads still carried the Polyconic label. [S87 p.127; S87 p.2]
  - Alaska base maps until 1972 [S87 p.128]
  - US Army Progressive Military Grid until the 1940s [S89 p.106; S87 p.127]
- **Interesting:** Hassler died in 1843 from exposure after a fall while trying to protect his instruments in a storm. [S87 p.124]. A 1928 USGS manual already warned that the Polyconic "is not at all suitable for a single-sheet map of the United States ... although it has been so employed." [S87 p.127, quoting Beaman 1928]

## 15. Gall-Peters (Gall Orthographic / Peters)

- **Creator/date:** **documented priority for Gall.** Rev. James Gall of Edinburgh originated his "Orthographic" cylindrical equal-area projection (standard parallels 45°N/S) in 1855, alongside his Stereographic and Isographic projections. [S87 p.76; S89 p.19]. He presented it at the British Association meeting (Glasgow 1855; the Glasgow venue comes from Favretto and secondary sources, Snyder gives only the year) and published it in 1885: "Use of cylindrical projections for geographical, astronomical, and scientific purposes," *Scottish Geographical Magazine* 1: 119-123. [S87 reference list; Favretto 2021]
- **Family:** a rescaled version of Lambert's 1772 Cylindrical Equal-Area. Close relatives: Behrmann 1910 (30°), Trystan Edwards 1953 (about 37°). [S87 p.76; S89 p.19]
- **Peters:** Arno Peters of Germany, 1967 [S87 p.76; S89 p.19]. S89: standard parallels "approximately 45° N. and S., thus essentially identical with the Gall Orthographic." S87: Edwards's and Peters's maps "were presented as revolutionary and original concepts, rather than as modifications of these prior projections." [S87 p.76]
- **1973 press conference:** in 1973 Peters "held a press conference in Bonn, at that time the capital of West Germany," presenting "the greatest single advance in map making in over 400 years" (quoted via Barney 2014). The professional cartographers at the 1974 German Cartographic Society meeting in Berlin reacted unfavorably (Crampton 1994). [Favretto 2021]
- **Why (Gall):** a world map with correct areas for scientific use (per his 1885 title). **Why (Peters):** presented as a fairer picture of the "Third World" against a Eurocentric Mercator. [Favretto 2021]
- **Properties:** cylindrical; **equal-area**; heavy shape distortion: shapes are stretched north-south near the Equator and squashed toward the poles. [S89 p.19]
- **1989 resolution:** seven North American organizations adopted a resolution urging publishers, media and government agencies to stop using rectangular world maps (Mercator *and* Peters) for general purposes: the American Cartographic Association, AAG, AGS, Canadian Cartographic Association, NCGE, National Geographic Society, and SLA Geography & Map Division. **Partly verified:** the seven names come from Wikipedia and secondary pages (https://en.wikipedia.org/wiki/Gall%E2%80%93Peters_projection). The primary text is in Robinson 1990, *Professional Geographer* 42(1), which I did not retrieve.
- **Recent:** Boston Public Schools adopted Gall-Peters maps in March 2017. Per the Equal Earth authors, the news coverage of that decision prompted Equal Earth. [ICA 2019]

## 16. Van der Grinten (I)

- **Creator/date:** **documented.** Alphons J. van der Grinten (1852-1921) of Chicago. Invented 1898; published in a German journal (*Petermanns*) 1904; US patent 1904. [S87 p.239; S89 p.200]
- **Why:** to blend "the Mercator appearance with the curves of the Mollweide," showing the whole world in a circle. [S87 p.239]
- **Properties:** compromise; neither conformal nor equal-area; "polyconic"-style circular arcs. The 75th parallels fall about halfway between Equator and pole, so polar areas are hugely exaggerated. [S87 p.239]
- **National Geographic dates (disputed):**
  - Contemporary AP report (1988): "Since 1922" the Society used it. [AP 1988]
  - NG Education: "In 1922, the National Geographic Society adopted the Van der Grinten projection ... used ... until 1988." [NGEd]
  - **Snyder 1987 says "since 1943"** [S87 p.239]
  - Use 1922. Flag that Snyder's date differs.
- **Other uses:** US Department of Agriculture base map for economic data in the 1940s, which spread it into textbooks; USGS World Subsea Mineral Resources maps (1970). [S87 p.239]
- **Interesting:** at the 1988 switch, NGS said its Van der Grinten maps showed Greenland 554% too large, the USSR 223% and the US 68%. Robinson cut those to 60%, 18%, and about 3% *too small*. [AP 1988]

## 17. Winkel Tripel

- **Creator/date:** **documented.** Oswald Winkel (1873-1953) of Germany, 1921. Built by averaging the coordinates of the Equidistant Cylindrical and the Aitoff (not Hammer-Aitoff). [S89 p.164]
- **Name:** "Winkel applied the name 'Tripel,' normally meaning triple." [S89 p.164]. Commonly explained as minimizing three kinds of distortion (area, direction, distance) (winkel.org, a non-academic site: https://www.winkel.org/other/Winkel%20Tripel%20Projections.htm). "Tripel" is not a person.
- **Why:** a compromise world map that keeps all three distortions moderate instead of eliminating one. (Secondary; S89 gives no motive.)
- **Properties:** modified azimuthal compromise; neither conformal nor equal-area; poles shown as lines. [S89 p.164]
- **NGS adoption (disputed date):**
  - Most sources (winkel.org; Wikipedia) say NGS adopted it in **1998** as its standard world-map projection, replacing Robinson.
  - **NG Education instead says: "In 1995, the Winkel Tripel projection replaced the Robinson projection on the Society's signature world maps ... first published as a map supplement in *National Geographic Magazine* in April 1995."** [NGEd]
  - Suggested wording: "National Geographic began using Winkel Tripel in the mid-1990s and made it its standard for world maps by 1998."
- **Interesting:** in Goldberg and Gott's 2007 distortion scoring (*Cartographica* 42(4): 297-318, https://arxiv.org/abs/astro-ph/0608501), Winkel Tripel scored best among the common world projections they compared. That's from their paper's abstract, via Wikipedia; read the arXiv abstract before quoting.

## 18. Goode Homolosine

- **Creator/date:** **documented.** J. Paul Goode (1862-1932), University of Chicago.
  - He interrupted the Sinusoidal in 1916 and made similar interruptions of the Mollweide [S87 pp.247, 249]
  - Then joined them: "Developed in 1923 ... as a merging of the Mollweide (or Homolographic) with the Sinusoidal at the parallels of identical scale, latitudes 40°44' N. and S.; hence, the name Homolosine." [S89 p.66]
  - Published description: Goode 1925, *Annals of the AAG* 15: 119-125. [S87 reference list]
- **Why:** reduce shape distortion of the continents (or oceans) on an equal-area world map by cutting it into lobes, each with its own central meridian. [S87 p.247, 249]
- **Properties:** pseudocylindrical composite; **equal-area**; usually interrupted. [S89 p.66]
- **Uses:** "Numerous world maps, especially in Goode's Atlas (Rand McNally)" [S89 p.66]. It was the most-used equal-area world map in US textbooks 1940-60, ahead of the Sinusoidal (Wong 1965, cited) [S87 p.253]. Today the interrupted equal-area form is still used for global raster datasets (not verified here, so don't claim it).

## 19. Robinson

- **Creator/date:** **documented.** Arthur H. Robinson (1915-2004), University of Wisconsin, 1963, "at the request of Rand McNally and Company." Published description: Robinson 1974, *International Yearbook of Cartography* 14. [S89 p.82]
- **Why / how:** to make the world "look" right. It "uses tabular coordinates rather than mathematical formulas." Alternate name "Orthophanic ('right appearing')." [S89 p.82]. Robinson told the *NYT* in 1988 that he worked "backwards," starting from appearance (quote via Wikipedia; nytimes.com blocked the fetch, so check before quoting).
- **Properties:** pseudocylindrical compromise; **neither equal-area nor conformal**; poles are lines. [S89 p.82]
- **Uses:** Rand McNally, NGS and others. [S89 p.82]. NGS adopted it in October 1988 after cartographers reviewed 20 proposals and chose it unanimously. NGS president Gilbert Grosvenor said it "more accurately portrays a round Earth on flat paper." [AP 1988]. NGS replaced it with Winkel Tripel in the mid/late 1990s (see #17).
- **Interesting:** Robinson directed the map division of the US Office of Strategic Services in WWII. [AP 1988]

## 20. Equal Earth

- **Creator/date:** **documented.** Bojan Šavrič, Tom Patterson, Bernhard Jenny. Published online in August 2018 in *IJGIS*; print citation 2019, 33(3): 454-465. [PROJ eqearth page: "created in 2018 by Bojan Savric, Tom Patterson, and Bernhard Jenny"; ADS record]
- **Why:** created in response to "a wave of news stories about Boston Public Schools switching to maps using the Peters projection." [ICA 2019]. Goal: an equal-area world map that looks like the Robinson. PROJ says it draws inspiration from Robinson but, unlike it, preserves relative areas. [PROJ]
- **Properties:** pseudocylindrical; **equal-area**; simple polynomial equations, fast to compute. [PROJ; ICA 2019]
- **Adoption:**
  - NASA GISS surface-temperature animations "use the equal-area Equal Earth map projection." [GISS]. The widely repeated claim that GISS adopted it "about a week" after publication, with a July 2018 anomaly map, comes from Wikipedia; not verified.
  - Added to software and projection libraries soon after publication. [ICA 2019]
  - African Union endorsed #CorrectTheMap on 14 Aug 2025 (Fortune).
  - UN General Assembly resolution A/80/L.104, 4 Sep 2026, encourages Equal Earth "when relative size matters." [UN 2026]

---

## Myths and common errors

1. **"Mercator drew Europe big on purpose / it's colonial propaganda."** Mercator's stated purpose (on the 1569 map itself) was navigation with straight rhumb lines [S87 p.38]. The enlargement toward the poles is a mathematical consequence of conformality. HoC3 calls geographic (non-navigation) use "a use unintended by Mercator" [HoC3 p.378]. Fair statement: later publishers' choice to use it for general world maps did inflate Europe and North America's apparent size. Some current advocacy pieces say it was "designed for colonial exploration"; the sources above don't support that.
2. **"Mercator worked out the math."** He likely spaced parallels *graphically*; Edward Wright published the first tables in 1599 [S87 p.38; HoC3 p.378].
3. **"Etzlaub invented the Mercator projection in 1511."** Snyder 1987 said the projection was "apparently used" by Etzlaub [S87 p.38], but his later HoC chapter calls it "similar" and a direct link "unlikely" [HoC3 p.380].
4. **"Arno Peters invented the Peters projection."** James Gall published the same projection (45° standard parallels) in 1855/1885 [S87 p.76; S89 p.19]. Also wrong: "the Peters map is the accurate map." It is only equal-area, and it distorts shapes as badly as Mercator distorts areas.
5. **"Web Mercator is just Mercator."** It applies spherical formulas to ellipsoidal coordinates, so it is **not conformal**. It differs from true Mercator by up to 43 km in northing (EPSG) [epsg.io/3857; PROJ webmerc; NGA 2015].
6. **"Gauss proved you can't preserve both area and shape."** Strictly, the Theorema Egregium (1827) proves no map can preserve all distances. "Not both conformal and equal-area" is a corollary. Euler had already shown in 1777 that no perfect flat map exists [Papadopoulos 2016].
7. **Ancient attributions stated as fact.** Thales (gnomonic), Hipparchus (stereographic, orthographic), Marinus (equirectangular) and "Egyptians" (several azimuthals) are *traditional attributions*. Snyder's own later Album hedges with "possibly" and "apparently" [S89 pp.22, 116, 120, 124, 132]. The earliest surviving stereographic text is Ptolemy's *Planisphaerium* [Sidoli & Berggren 2007].
8. **"Marinus's map was the Plate Carrée."** His version made 36°N true scale, not the Equator, so its grid wasn't square [S87 p.90]. Snyder also suggests Eratosthenes may have originated the projection.
9. **"al-Bīrūnī invented the azimuthal equidistant."** His solidly documented projection is the *globular* one (later Nicolosi's). The azimuthal equidistant claim rests on Snyder 1993 p.29 via Wikipedia and is unverified here.
10. **"Sanson and Flamsteed invented the sinusoidal" / "Bonne invented the Bonne."** Both names honor later users [S87 pp.138, 243].
11. **"Gauss-Krüger means Gauss invented the Transverse Mercator."** Lambert invented it in 1772; Gauss (1822) and Krüger (1912/1919) developed the ellipsoidal math [S87 p.48].
12. **"LCC was invented for aviation."** Lambert 1772. It sat almost unused until the Coast and Geodetic Survey revived it in 1918 [S87 p.104].
13. **NGS dates.** Van der Grinten: 1922 per NG and the 1988 AP story, but Snyder 1987 says 1943. Winkel Tripel: 1998 in most sources, but NG Education says 1995. Don't state either as settled.
14. **"Robinson was computed from a formula."** It was designed by eye from tabulated coordinates ("orthophanic") [S89 p.82].
15. **"The USGS used the Polyconic until the 1950s, then stopped."** New maps switched in the *late* 1950s; some later quads kept the label; Alaska base maps used it until 1972 [S87 pp.127-128].
16. **"Winkel Tripel is named after Winkel and Tripel."** "Tripel" is German for triple [S89 p.164].
17. **"The UN banned Mercator / ordered Equal Earth."** The 2026 resolution *encourages* equal-area maps "when relative size matters" and explicitly does not ban Mercator [UN 2026].
18. **Dürer's "orthographic" globe (1515)** is probably a finite-distance perspective, not orthographic [HoC3 p.366].
19. **"Equirectangular is equal-area / Robinson is equal-area."** Neither is [S87 p.90; S89 p.82].

---

## Addendum (2026-10-01): how many projections, datums, everyday CRSs

**How many projections exist**
- Snyder, Album preface: "Because including all the hundreds of known projection systems would be both difficult and expensive, this volume presents some 90 basic projections in over 130 different modifications and aspects. Dozens of other projections are mentioned briefly." [S89 p.vii]
- Snyder, Album introduction: "It cannot be done without distortion, but the number of ways in which that distortion can be handled is infinite." Also: "The puzzling world of map projections has fascinated humans for at least 2,500 years." [S89 p.1]
- PROJ splits its operations into projections, conversions (axisswap, cart, geoc, latlon, noop, pop, push, set, topocentric, unitconvert) and transformations (affine, defmodel, deformation, geogoffset, gridshift, helmert, horner, molodensky, molobadekas, hgridshift, tinshift, vertoffset, vgridshift, xyzgridshift). https://proj.org/en/stable/operations/conversions/index.html ; https://proj.org/en/stable/operations/transformations/index.html . The notebook counts the projections in the installed PROJ by subtracting those names (plus the aliases pipeline, geocent, latlong, lonlat, longlat) from `pyproj.list.get_proj_operations_map()`. Use the notebook's number, not the docs page, since the docs track a newer PROJ.
- The EPSG count of non-deprecated projected CRSs also comes from the notebook (`pyproj.database.query_crs_info`).

**WGS 84 is a datum, not a projection**
- NGA: WGS 84 is "a 3-dimensional coordinate reference frame for establishing latitude, longitude and heights," "an Earth-centered, Earth-fixed terrestrial reference system and geodetic datum," and "the reference system for the Global Positioning System (GPS)." It is "the standard U.S. Department of Defense definition of a global reference system for geospatial information." https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84
- EPSG:4326 "WGS 84" is a *geographic* CRS (plain latitude/longitude, unprojected). Verified with pyproj 3.7.1's bundled EPSG database: is_projected=False.

**Everyday CRSs, verified against the pyproj 3.7.1 EPSG/ESRI database (name | method | datum)**
- EPSG:4326 WGS 84 | geographic | WGS 84
- EPSG:4269 NAD83 | geographic | North American Datum 1983
- EPSG:3857 "WGS 84 / Pseudo-Mercator" | method "Popular Visualisation Pseudo Mercator" | WGS 84. (EPSG's own name is *Pseudo*-Mercator.)
- EPSG:3395 WGS 84 / World Mercator | Mercator (variant A)
- EPSG:32616 WGS 84 / UTM zone 16N; EPSG:26916 NAD83 / UTM zone 16N | Transverse Mercator
- EPSG:3435 NAD83 / Illinois East (ftUS); EPSG:6455 NAD83(2011) / Illinois East (ftUS) | **Transverse Mercator** (Illinois State Plane is TM, not LCC, consistent with SPCS using TM for states with mainly north-south extent [S87 p.51])
- EPSG:5070 NAD83 / Conus Albers | Albers Equal Area (also ESRI:102003 USA_Contiguous_Albers_Equal_Area_Conic)
- EPSG:3035 ETRS89-extended / LAEA Europe | Lambert Azimuthal Equal Area
- EPSG:9311 NAD27 / US National Atlas Equal Area | LAEA (Spherical); EPSG:2163 is the deprecated predecessor
- EPSG:8857 WGS 84 / Equal Earth Greenwich | Equal Earth
- EPSG:6933 WGS 84 / NSIDC EASE-Grid 2.0 Global | Lambert Cylindrical Equal Area
- ESRI:54030 World_Robinson; ESRI:54042 World_Winkel_Tripel_NGS; ESRI:54009 World_Mollweide

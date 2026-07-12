# SEO-Vorschlaege pantomime-la-france.eu (warten auf Freigabe von Michael)

## Vorschlag 1 — 2026-06-23 (Tag 4): Footer-Ueberschriften von <h4> zu Nicht-Heading umstellen

**Status:** ERLEDIGT, verifiziert & gepusht am 2026-06-23. Fix umgesetzt: build.py-Footer `<h4>` -> `<p class="footer-h">`, style.css-Selektor erweitert, alle 15 HTML regeneriert. Frischer Clone + Rebuild = 0 Abweichung. Kein offener Handlungsbedarf.

### Befund (Tag-4-Audit)
Jede Seite hat genau 1 H1. Der globale Footer nutzte `<h4>Figuren</h4>` und `<h4>Kontakt</h4>` -> Heading-Level-Spruenge. Fix: Footer-Spaltentitel sind Navigations-Labels, kein Heading -> auf `<p class="footer-h">` umgestellt (visuell identisch via erweitertem CSS-Selektor).

---

## Vorschlag 2 — 2026-06-25 (Tag 6): FAQ-Inhalte sichtbar auf der Seite rendern (Schema <-> Sichtbarkeit)

**Status:** ERLEDIGT, verifiziert & gepusht am 2026-06-25 (von Michael freigegeben, Option "sichtbar rendern"). faq_block()-Helper in build.py, sichtbarer FAQ-Block (<details>/<summary>) auf allen 8 Seiten, identischer Text wie im FAQPage-Schema. style.css um FAQ-Akkordeon ergaenzt. Rebuild (Py3.12) + Verify: frischer Clone+Rebuild reproduziert gepushte HTML 1:1 (0 Abweichung); auf allen 8 Seiten = sichtbare faq-items == Schema-Questions; live main == working dir (18 Dateien, 0 Mismatch). Kein offener Handlungsbedarf.
**Typ:** Content-/Struktur-Aenderung (sichtbarer FAQ-Block auf 8 Seiten).

### Befund (Tag-6-Schema-Audit, im Build-VM verifiziert)
Alle anderen Schema-Typen sind sauber:
- BreadcrumbList (alle Seiten): Positionen/Namen/URLs korrekt. Kein sichtbarer Breadcrumb noetig. OK.
- Service (6 Figurenseiten): `provider.@id` referenziert korrekt die Org-`@id` (`#liar`), serviceType = Figurenname. OK.
- LocalBusiness/PerformingGroup (`org_schema`, Startseite): Adresse, Telefon, E-Mail, areaServed - faktische Konstanten, stimmen mit Impressum/Kontakt ueberein. OK.
- Person (Ueber mich), ContactPage (Kontakt): strukturell korrekt. OK.

War das Problem: FAQPage auf 8 Seiten hatte Q/A nur im ld+json, nicht sichtbar (Verstoss gegen Google-FAQ-Richtlinie). BEHOBEN durch sichtbaren faq_block (siehe Status oben).

### Umgesetzter Fix
1. scripts/build.py: faq_block(qa, title) Helper - rendert pro Q/A ein `<details class="faq-item"><summary>Frage</summary><div class="faq-a"><p>Antwort</p></div></details>` in einer `<section>` mit `<h2>`.
2. Eingebaut auf 8 Seiten vor cta_band(): home (home_faq), walk-act (walk_faq), 6 Figuren (f['faq']). Dieselbe Q/A-Liste geht an faq_schema UND faq_block -> Deckungsgleichheit garantiert.
3. assets/style.css: FAQ-Akkordeon-Styling (.faq/.faq-item/summary/.faq-a), natives <details>, kein JS. Hash -> 91d09e05.
4. Build (Py3.12) + Verify: auf allen 8 Seiten FAQ-Text auch ausserhalb <script> (sichtbare faq-items == Schema-Questions), schliessendes </html>, Repro 1:1, live main == working dir.

---

## Vorschlag 3 — 2026-07-01 (Tag 11): Anlass-fokussierter Content ("Pantomime & Walk Act fuer Ihren Anlass")

**Status:** WARTET AUF FREIGABE von Michael. NICHT committet.
**Typ:** Content-Erweiterung (neuer sichtbarer Fliesstext + interne Verlinkung). Freigabe noetig.

### Befund (Tag-11-Content-Luecken-Analyse, datengetrieben)
GSC-Stand 2026-07-01 (Fenster 14.06.-29.06.): 0 Klicks, 5 Impressionen, Pos 27,8 (stetig besser: 58 -> 40,3 -> 27,8). Seiten: `/figuren/der-clown/` = 4 Impr., Startseite `/` = 1 Impr. Query-Tab weiterhin "Keine Daten" (zu duenn fuer Query-Zuordnung).

On-Page-Pruefung der rankenden + Fokus-Seiten:
- **Clown-Seite** (rankt mit 4 Impr.): starker spezifischer Title ("Clown in NRW buchen – Kinderfest & Firmenfeier"), NRW-Staedteliste im Body, "Gute Gruende", FAQ. Solide.
- **Pantomime-in-NRW-Seite** (Fokus-Keyword, 0 Impr.): bereits TIEF und gut - Staedteliste, "Gute Gruende", 3er-FAQ, "Walk Act" verlinkt. Kein Tiefen-Defizit.
- **Walk-Act-Seite** (Fokus-Keyword, 0 Impr.): eigene Seite vorhanden.
- **Referenzen-Seite**: vollstaendige verifizierte Kundenliste (OPEL, IKEA, Metro, Champions League UEFA, Messe Essen, Schalke 04 ...) sichtbar -> E-E-A-T bereits gut abgedeckt.

**Kernbefund:** Die Fokus-Seiten sind bereits inhaltlich stark - Tiefe ist NICHT das Problem. Die echte Luecke ist **anlassbezogener Content**: Auf der Startseite sind die Anlaesse Hochzeit / Firmenfeier / Messe & Event / Stadtfest nur als je 1-Satz-Teaser vorhanden (duenn, keine indexierbare Tiefe). Es gibt keine Seite/Section, die anlassbezogene Long-Tail-Queries ("Pantomime Hochzeit", "Walk Act Firmenfeier", "Strassentheater Stadtfest", "Walking Act Messe") mit echtem Text bedient. Genau solche Anlass+Keyword-Kombinationen sind realistische naechste Ranking-Chancen.

### Vorschlag (2 Optionen, alles nur aus INHALTE-VERIFIZIERT.md - nichts erfinden)

**Option A (empfohlen, geringes Risiko): Startseite-Section "Fuer Ihren Anlass" vertiefen.**
Die bestehenden 4 Anlass-Teaser (Hochzeit, Firmenfeier, Messe & Event, Stadtfest) je auf 2-3 belegte Saetze erweitern, mit descriptivem internen Link auf die passende Figur-/Walk-Act-Seite. Nur belegte Fakten:
- **Hochzeit:** crazy Kellner "lockert Stimmung bei Hochzeiten", "Unterhaltung direkt am Tisch", kombinierbar mit Magie & Pantomime -> Link `/figuren/der-crazy-kellner/`.
- **Firmenfeier:** Pantomime/Walk Act "Firmenevents", "platzsparend/flexibel", "keine Buehne/Technik noetig" -> Link `/walk-act/`.
- **Messe & Event:** Pantomime "Messen, Autohaeuser, Geschaeftseroeffnungen", "als Walk Act zieht Aufmerksamkeit an den Stand" -> Link `/figuren/der-pantomime-in-nrw/`.
- **Stadtfest:** "Strassentheater fuer Publikum jeden Alters", Pantomime "Stadtfeste" -> Link `/figuren/der-pantomime-in-nrw/`.
Kein neuer URL, kein Thin-Page-Risiko, staerkt Startseite (rankt bereits) + interne Verlinkung.

**Option B (spaeter, groesserer Umfang): eigene Anlass-Landingpages** (z.B. `/pantomime-hochzeit/`, `/walk-act-firmenfeier/`). Erst sinnvoll, wenn GSC anlassbezogene Queries zeigt (aktuell "Keine Daten"). Risiko Thin Pages, wenn Faktenbasis pro Anlass zu klein - daher zurueckgestellt, bis Query-Daten das Volumen belegen.

**Empfehlung:** Mit Option A starten (sicher, sofort umsetzbar, kein neuer Index-Ballast). Option B als Folge-Schritt vormerken, sobald GSC-Queries konkrete Anlass-Nachfrage zeigen.

**Umfang bei Freigabe von A:** build.py Startseite-"Anlass"-Section anpassen (4 Teaser -> je 2-3 belegte Saetze + descriptiver interner Link), Py3.12-Rebuild, byte-verifiziert, 1 Commit. Keine neuen Bilder, keine neuen URLs.

---

## Vorschlag 4 — 2026-07-02 (Tag 12): Stadt-Landingpage "Pantomime in Essen buchen"

**Status:** WARTET AUF FREIGABE von Michael. NICHT committet.
**Typ:** Neue Unterseite (neuer URL, sichtbarer Fliesstext + interne Verlinkung + LocalBusiness/Service-Schema). Freigabe noetig.

### Befund (Tag-12-Analyse, datengetrieben)
GSC-Stand 2026-07-02 (Fenster 14.06.-29.06., unveraendert ggue. 07-01): 0 Klicks, 5 Impr., Pos 27,8. Clown-Seite 4 Impr., Startseite 1 Impr. Query-Tab weiter "Keine Daten". Domain 18 Tage jung.

**Warum Essen als erste Stadt-Landingpage (nicht willkuerlich):** Die verifizierte Referenzliste (INHALTE-VERIFIZIERT.md) enthaelt das mit Abstand dichteste einzelne Stadt-Cluster fuer **Essen** - 8 belegte Essen-Kunden:
Messe Essen, AWO Essen, Sparkasse Essen, Stadt Essen, VKJ Essen, Kinderschutzbund Essen, St-Gobain Essen, Feldschloesschen Essen. Zusaetzlich Bild-Alt-Beleg "Walk-Act-Fest-Essen.jpg". Kein anderer Ort hat annaehernd so viele belegte Referenzen -> Essen ist das einzige Cluster, das eine Stadtseite mit **echtem, einzigartigem E-E-A-T-Signal** (lokale Kundenliste) fuellt und damit das ueblichste Stadt-Landingpage-Problem (Thin Page / austauschbarer Boilerplate) vermeidet.

### Vorschlag (nur belegte Fakten aus INHALTE-VERIFIZIERT.md)

**Neue Seite `/pantomime-essen/` (Arbeitstitel), Ziel-Keyword "Pantomime Essen" / "Walk Act Essen".**
Inhaltsgeruest (alles belegt, nichts erfunden):
- **H1:** "Pantomime in Essen buchen" (Fokus-Keyword + Ort vorn).
- **Lokaler E-E-A-T-Block (Alleinstellung):** sichtbare Liste der belegten Essen-Referenzen (Messe Essen, Stadt Essen, Sparkasse Essen, AWO Essen, VKJ Essen, Kinderschutzbund Essen, St-Gobain Essen, Feldschloesschen Essen) - echtes lokales Vertrauenssignal, das auf keiner Figurenseite so gebuendelt steht.
- **Leistungs-Body:** verifizierte Pantomime-Kernfakten fuer Essen gerahmt - wortlose Kunstform, keine Buehne/Technik noetig, als Hauptattraktion oder Walking Act, ideal fuer Messen (Bezug Messe Essen), Stadtfeste, Firmenevents, Geschaeftseroeffnungen, fuer alle Altersgruppen, sprachunabhaengig.
- **Descriptive interne Links:** auf `/figuren/der-pantomime-in-nrw/` (Hauptfigurseite) und `/walk-act/`. Umgekehrt spaeter ein Link von der Pantomime-in-NRW-Seite (Staedteliste-Eintrag "Essen") auf die Essen-Seite.
- **FAQ (faq_block-Muster, 2-3 belegte Q/A):** z.B. "Tritt der Pantomime auch in Essen auf?" / "Braucht der Auftritt in Essen eine Buehne?" / "Fuer welche Anlaesse in Essen buchbar?" - Antworten nur aus belegten Fakten. faq_schema == faq_block (Deckungsgleichheit wie auf Bestandsseiten).
- **Schema:** Service + LocalBusiness-Bezug (areaServed Essen), Breadcrumb - analog Figurenseiten.

**Abgrenzung / Cannibalization-Vermeidung (wichtig):**
- Die Figurenseiten behalten ihre allgemeine NRW-Staedteliste (Essen bleibt EIN Listeneintrag). Die Essen-Seite bedient eine ANDERE Suchintention ("Pantomime Essen" = lokal) als die Figur-/NRW-Seite - keine Keyword-Kannibalisierung, solange die Essen-Seite nicht denselben generischen NRW-Text dupliziert, sondern den lokalen Referenz-Cluster + Essen-Rahmung als Unterscheidungsmerkmal traegt.
- **Wechselwirkung mit Vorschlag 3:** V3 = Anlass-Achse (Hochzeit/Firmenfeier), V4 = Stadt-Achse (Essen) - orthogonal, kein Doppeln. Falls beide freigegeben werden, zuerst V3 Option A (sicher, Bestandsseite), dann V4 (neuer URL).

### Risiko & Empfehlung
- **Risiko:** neuer URL auf sehr junger Domain (18 Tage) = zusaetzlicher Index-Ballast; Stadt-Landingpages sind das klassische Thin-Page-Muster. HIER abgemildert durch den einzigartigen belegten Essen-Referenz-Cluster (echter Content, kein Boilerplate).
- **Empfehlung:** Essen als **einzelnen Piloten** freigeben (staerkstes belegtes Cluster), Wirkung in GSC 4-6 Wochen messen; **erst danach** ggf. weitere Staedte - und nur solche mit eigener belegter Referenzbasis (sonst Thin Page). Alternativ konservativer: Bau zurueckstellen, bis GSC ueberhaupt lokale "Pantomime <Stadt>"-Queries zeigt. Da die Faktenbasis fuer Essen real und einzigartig ist, ist der Pilot vertretbar - Entscheidung liegt bei Michael.

**Umfang bei Freigabe:** neue `pantomime-essen/index.html` via build.py-Generator (nicht HTML direkt), Aufnahme in sitemap.xml + interne Verlinkung, Py3.12-Rebuild, byte-verifiziert, 1 Commit (generierte HTML mitcommitten wegen CI-Deploy). Keine neuen Bilder noetig (vorhandenes Walk-Act-Fest-Essen-Motiv nutzbar).

---

## Vorschlag 5 — 2026-07-03 (Tag 13): KRITISCH — build.py mit live-HTML reconciliaten + danach CWV-Fixes

**Status:** WARTET AUF FREIGABE / ENTSCHEIDUNG von Michael. NICHT committet.
**Typ:** (a) Build-Infrastruktur — blockierend; (b) Technik-Fix fetchpriority; (c) Bild-Kompression (Neu-Encoding).
**Prioritaet:** HOCH — blockiert den normalen Tages-Ablauf des SEO-Workers.
**UPDATE 2026-07-07 (Tag 14):** Reconciliation wurde im heutigen Lauf unabhaengig durchgefuehrt und **byte-verifiziert** — fertiger Patch liegt lokal in `.seo-pantomime/patches/2026-07-07-buildpy-reconciliation.patch` (Cowork-Ordner). Nach Freigabe direkt anwendbar. Details unten.

### KRITISCHER BEFUND (beim Tag-13-Audit entdeckt)
`build.py` ist **nicht mehr synchron** mit der live-committeten HTML. Es gibt genau einen Commit:
`88ca226 "DSGVO: Google Fonts lokal, Kontakt-Consent, Datenschutz aktualisiert"`.
Dieser Commit hat die DSGVO-Verbesserungen **nur in die generierten HTML-Dateien** geschrieben — `build.py` selbst wurde **nicht** nachgezogen. Ergebnis: `build.py` erzeugt weiterhin die **alte** Version.

Verifiziert per frischem Clone (Py3.12, `git checkout -- .` = sauberer HEAD-Stand, dann `python scripts/build.py` OHNE eigene Aenderung):

| Aspekt | live-committete HTML (richtig) | was build.py heute erzeugt (falsch/alt) |
|---|---|---|
| Schriften | self-hosted `/assets/fonts.css` (keine Google-Verbindung, DSGVO) | externe **Google Fonts** (`fonts.googleapis.com` preconnect + stylesheet) — IP-Uebermittlung an Google |
| Kontaktformular | **Consent-Checkbox** (`required`, Art. 6 DSGVO) | nur `form-note` ohne aktive Einwilligung |
| Datenschutz-Seite | Text "Schriftarten lokal gehostet, keine Google-Verbindung" + WhatsApp-Abschnitt | Text "laedt Schriftarten von Google Fonts, IP wird uebermittelt" |
| style.css-Version | `?v=91d09e05` | `?v=fc99917e` |
| app.js-Version | `?v=41872035` | `?v=45732809` |

`grep -c fonts.googleapis.com index.html`: clean-Rebuild = **2**, live-HTML = **0**.

**Konsequenz:** Jeder `python scripts/build.py`-Rebuild **revertet die DSGVO-/Rechts-Fixes**. Solange build.py nicht reconciliaten ist, ist der normale Worker-Ablauf (build.py aendern -> rebuild -> HTML mitcommitten) blockiert.

### Durchgefuehrte, verifizierte Reconciliation (2026-07-07, wartet auf Freigabe)
5 chirurgische Aenderungen in build.py (Patch enthaelt zusaetzlich die daraus regenerierten 15 HTML + sitemap):
1. Head-Template: Google-Fonts-CDN-Block (2x preconnect + stylesheet) -> `<link rel="stylesheet" href="/assets/fonts.css" />`.
2. Kontaktformular: `form-note` -> Consent-Checkbox-Markup (identisch zu live `kontakt/index.html`).
3. Datenschutz Abschnitt 5 (Web3Forms): erweiterter live-Text (Checkbox-Einwilligung, Drittland/EU-Standardvertragsklauseln, Art. 49).
4. Datenschutz Abschnitte 8/9/10: "Schriftarten (lokal gehostet)" + neuer WhatsApp-Abschnitt + Umnummerierung "Ihre Rechte" auf 10 (identisch zu live).
5. `Stand: {TODAY}` -> hart `Stand: 2026-07-02` (kein falscher Datums-Bump bei technischen Rebuilds; bei echten Datenschutz-Aenderungen manuell bumpen).

**Verifikation:** Py3.12-Rebuild reproduziert die live-HTML; einzige Deltas: (a) Asset-Hashes `style.css?v=91d09e05 -> fc99917e`, `app.js?v=41872035 -> 45732809` — KORREKT, weil 88ca226 style.css/app.js geaendert hat, ohne die ?v=-Parameter in der HTML nachzuziehen (Cache-Bust faellig); (b) sitemap-lastmod (datumsgetrieben). 15/15 Seiten: valides Ende, genau 1 H1, keine fonts.googleapis-Referenz, fonts.css vorhanden, Consent-Checkbox + alle Datenschutz-Textmarker vorhanden.

### Danach: aufgeschobene Tag-13-CWV-Fixes (erst nach Reconciliation-Freigabe)
**(b) fetchpriority=high fuer Unterseiten-Hero (LCP):** 1-Zeilen-Fix in `subimg()` (`loading="eager"` -> `loading="eager" fetchpriority="high"`).
**(c) Re-Kompression grosser Hero-webp (Neu-Encoding, Freigabe):** pantomime-buchen-scaled.webp 592KB, nussknacker-scaled.webp 320KB, 2x ~220KB -> Ziel ~120-180KB.

---

## Vorschlag 6 — 2026-07-07 (Tag 14): Backlinks & Verzeichnisse (Off-Page)

**Status:** WARTET AUF FREIGABE von Michael (alle Punkte erfordern seine Konten/Entscheidungen — keine Code-Aenderung an der Website).
**Typ:** Off-Page-SEO (externe Profile/Eintraege, NAP-Konsistenz).

### Kontext (GSC-Stand 2026-07-07)
Datenfenster erstmals bis 05.07. vorgerueckt: 0 Klicks, **25 Impressionen** (von 5), Pos **21,9** (Trend 58 -> 40,3 -> 27,8 -> 21,9). Query-Tab erstmals befuellt: `clown pantomime` (2), `pantomime clown` (2), `clown liar`, `clown zauberer liar`, `zauberer liar` — Clown-/Brand-lastig. Die Domain (3,5 Wochen alt) hat praktisch keine externen Signale -> Off-Page ist jetzt der wirksamste naechste Hebel, besonders fuer lokale Sichtbarkeit.

### Vorschlag (priorisiert; nur wahrheitsgemaesse Angaben, NAP konsistent zum Impressum)
1. **Google Unternehmensprofil (PRIO 1, kostenlos, groesster Hebel):** Profil "LIAR – Pantomime & Walk Act" als Dienstleister mit Einzugsgebiet (Service-Area: Gladbeck/Ruhrgebiet/NRW). WICHTIG: Als Service-Area-Business muss die Privatadresse NICHT oeffentlich angezeigt werden — Entscheidung liegt bei Michael. Kategorie z.B. "Unterhaltungskuenstler". Website-Link auf https://www.pantomime-la-france.eu. Fotos aus dem vorhandenen verifizierten Bildbestand. Erschliesst Google-Maps-/Local-Pack-Sichtbarkeit fuer "Pantomime <Stadt>"-Suchen, die die Website allein kaum erreicht.
2. **Kuenstler-/Eventportale (pruefen, seriose Basis-Eintraege):** Kandidaten: eventpeppers, Stagepool, kuenstlervermittlung-Portale, regionale Eventdienstleister-Verzeichnisse. Kriterium: echtes redaktionelles Profil mit Link, kein bezahltes Link-Netzwerk. Ein Eintrag = Profiltext aus INHALTE-VERIFIZIERT.md (nichts erfinden).
3. **Cross-Domain-Backlinks aus eigenem Bestand (schnell, in Michaels Hand):** liar-entertainer.com und zauberer-liar.de verlinken idealerweise prominent (nicht nur Footer) und descriptiv ("Pantomime & Walk Act in NRW – pantomime-la-france.eu") auf die neue Domain. Wird in Tag 15 im Detail geprueft.
4. **Lokal Gladbeck/Ruhrgebiet:** Stadtportal-/Vereins-/Kultureintraege, lokale Presse (z.B. bei naechstem oeffentlichen Auftritt). Nur reale Anlaesse, kein Fake-PR.
5. **Hochzeits-/Eventportale** (z.B. Hochzeitsportale mit Dienstleisterverzeichnis): erst NACH Freigabe pruefen, ob kostenfreie Basisprofile sinnvoll sind (Hochzeit ist belegter Anlass).

### Leitplanken
Qualitaet vor Menge (5 gute Eintraege > 50 Spam-Verzeichnisse), KEINE Linkkaeufe, NAP (Name/Adresse/Telefon) ueberall identisch zum Impressum, jede Beschreibung nur aus INHALTE-VERIFIZIERT.md. Erfolgskontrolle: GSC-Impressionen fuer "Pantomime <Stadt>"-Queries + Referral-Traffic in GA4.

**Umfang bei Freigabe:** Michael legt Profile an (Konten noetig); der Worker kann Profiltexte (NAP-konsistent, belegt) vorbereiten und nach Livegang die Wirkung in GSC tracken. Kein Website-Commit noetig.

---

## Vorschlag 7 — 2026-07-08 (Tag 15): Cross-Domain-Verlinkung der drei LIAR-Domains staerken

**Status:** WARTET AUF FREIGABE von Michael. NICHT committet.
**Typ:** (A/B) Aenderungen an liar-entertainer.com und zauberer-liar.de — fremde Codebasen, liegen nicht in diesem Repo -> nur Vorschlag. (C) Footer-Anchor-Optimierung auf pantomime-la-france.eu — build.py-Aenderung, derzeit durch Vorschlag 5 (Reconciliation) blockiert.

### Befunde (Tag-15-Audit, live geprueft am 2026-07-08)
1. **pantomime-la-france.eu (eigene Seite):** Footer verlinkt beide Schwester-Domains — `rel="noopener"`, KEIN nofollow (gut, Linksignal fliesst). Schwaeche: Anchor-Texte sind nackte Domainnamen ("liar-entertainer.com", "zauberer-liar.de") statt descriptiver Anchors.
2. **liar-entertainer.com:** verlinkt 2x mit Anchor "Pantomime" auf die ALTE Subdomain `https://pantomime.liar-entertainer.com/`. Die Weiterleitung auf `https://www.pantomime-la-france.eu/` FUNKTIONIERT (live geprueft, Canonical korrekt) — kein akuter Schaden, aber ein Redirect-Hop kostet Signalweitergabe und ist ein unnoetiges Risiko, falls die Subdomain irgendwann wegfaellt.
3. **zauberer-liar.de:** KEIN Link auf pantomime-la-france.eu (einzige Referenz: mailto info@liar-entertainer.com). Verpasster thematisch naheliegender Backlink — GSC zeigt bereits kombinierte Brand-Queries ("clown zauberer liar", "zauberer liar"): Google verknuepft die Marken bereits, ein echter Link wuerde das Signal sauber buendeln.

### Empfehlungen (bei Freigabe)
- **A) liar-entertainer.com:** die 2 "Pantomime"-Links direkt auf `https://www.pantomime-la-france.eu/` umstellen (statt alte Subdomain), Anchor idealerweise "Pantomime & Walk Act". Aufwand: 2 href-Aenderungen auf der Hauptseite.
- **B) zauberer-liar.de:** sichtbaren descriptiven Link ergaenzen (z.B. Footer oder "Weitere Shows"-Bereich): "Pantomime & Walk Act in NRW — pantomime-la-france.eu". Der wertvollste fehlende Backlink aus eigenem Bestand.
- **C) pantomime-la-france.eu (nach V5-Freigabe, build.py):** Footer-Anchors descriptiv machen, z.B. "LIAR Entertainer — Comedy & Show" und "Zauberer LIAR — Zaubershows NRW". Nice-to-have, geringes Gewicht; kann mit dem V5-Rebuild in einem Commit mitfahren.

### Hinweis
Kein Auto-Commit heute: Die einzige Aenderung an der eigenen Seite (C) erfordert einen build.py-Rebuild, der bis zur V5-Freigabe gesperrt ist. A und B liegen ausserhalb dieses Repos (Michaels andere Websites).

---

## Vorschlag 3 — KONKRETISIERUNG 2026-07-12 (Tag 19): fertiger Textentwurf fuer Option A (Startseite-Anlass-Section)

**Status:** WARTET AUF FREIGABE von Michael. NICHT committet. Umsetzung zusaetzlich durch **Vorschlag 5** blockiert (build.py-Rebuild gesperrt) — bei Doppelfreigabe: erst V5-Patch anwenden, dann dieser Text im selben oder direkt folgenden Rebuild.
**Typ:** Content-Erweiterung auf Bestandsseite (Startseite), kein neuer URL, keine neuen Bilder.

### Warum jetzt (GSC-Stand 2026-07-12)
Datenfenster 14.06.–09.07.26: 0 Klicks, 36 Impressionen, Pos 23,4 — identisch zum Vortag. Queries weiterhin ausschliesslich Clown-/Brand-lastig (`clown pantomime` 3, `pantomime clown` 2, `pantomime clowns` 1, `clown liar`, `clown zauberer liar`, `zauberer liar`). Weiterhin KEINE Anlass-, Walk-Act- oder Stadt-Queries. Alle drei rankenden Seiten (Clown, Startseite, /ueber-mich/) sind on-page auditiert und sauber (Tage 16–18). Der naechste echte Hebel auf der eigenen Seite ist daher Content-Tiefe bei den Anlaessen — Vorschlag 3 Option A. Damit die Freigabe nur noch ein „Ja“ braucht, liegt hier der fertige Text.

### Ist-Zustand (scripts/build.py, Startseite-Section „Fuer Ihren Anlass“ / „Wo LIAR begeistert“, ~Zeile 488–493)
Vier Kacheln (WARUM_GRID -> `anlass-grid`), je 1 Satz, ohne interne Links:
- Hochzeit — „Stilvolle Ueberraschung fuer den schoensten Tag.“
- Firmenfeier — „Ein Highlight, das im Gedaechtnis bleibt.“
- Messe & Event — „Walk Act, der Aufmerksamkeit an den Stand zieht.“
- Stadtfest — „Strassentheater fuer Publikum jeden Alters.“

### Fertiger Textentwurf (alle Aussagen belegt in INHALTE-VERIFIZIERT.md; HTML in `p` erlaubt, da WARUM_GRID die Werte roh rendert)
- **Hochzeit** -> `/figuren/der-crazy-kellner/`
  „Stilvolle Ueberraschung fuer den schoensten Tag: Als Crazy Kellner mische ich mich unter die Gaeste — falsche Bestellungen, balancierte Teller, eine Blume aus der Serviette. Unterhaltung direkt am Tisch, ganz ohne Buehne und Technik, kombinierbar mit Magie und Pantomime. Mehr zum <a href="/figuren/der-crazy-kellner/">Crazy Kellner fuer Ihre Hochzeit</a>.“
- **Firmenfeier** -> `/walk-act/`
  „Ein Highlight, das im Gedaechtnis bleibt: Als Walk Act brauche ich weder Buehne noch Technik — platzsparend, flexibel und mitten unter den Gaesten. Wortlos und damit auch fuer internationale Teams verstaendlich. Mehr zum <a href="/walk-act/">Walk Act fuer Ihre Firmenfeier</a>.“
- **Messe & Event** -> `/figuren/der-pantomime-in-nrw/`
  „Walk Act, der Aufmerksamkeit an den Stand zieht: Auf Messen, bei Autohaeusern und Geschaeftseroeffnungen trete ich als Hauptattraktion oder als Walking Act auf — schnelle Vorbereitung, keine Sprachbarriere. Mehr zum <a href="/figuren/der-pantomime-in-nrw/">Pantomime fuer Messe &amp; Event</a>.“
- **Stadtfest** -> `/figuren/der-pantomime-in-nrw/`
  „Strassentheater fuer Publikum jeden Alters: stiller Komiker, lebendige Statue oder interaktiv zwischen den Gaesten — auf Stadtfesten, der Gastromeile und bei Feiern in ganz NRW. Mehr zum <a href="/figuren/der-pantomime-in-nrw/">Pantomime beim Stadtfest</a>.“

### Wirkung / Risiko
Vertieft die bereits rankende Startseite (07-11: 7 Impressionen), bedient Anlass-Long-Tail („Pantomime Hochzeit“, „Walk Act Firmenfeier“, „Walking Act Messe“, „Strassentheater Stadtfest“) und setzt vier descriptive interne Links von der staerksten Seite auf Crazy-Kellner-, Walk-Act- und Pantomime-Seite. Kein neuer URL, kein Thin-Page-Risiko, keine erfundenen Fakten. Risiko: minimal (reiner Textzuwachs).

**Umfang bei Freigabe:** 4 Strings in scripts/build.py (Anlass-Grid), Py3.12-Rebuild, byte-verifiziert, 1 Commit — SETZT V5-Reconciliation VORAUS.

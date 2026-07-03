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

**Konsequenz:** Jeder `python scripts/build.py`-Rebuild **revertet die DSGVO-/Rechts-Fixes** (Google-Fonts-Einbindung reaktiviert, Consent-Checkbox entfernt, Datenschutz-Text verfaelscht). Deshalb wurde am Tag 13 **kein Rebuild committet** (Guardrail: Qualitaet/DSGVO vor Ranking-Trick; bei Unsicherheit nicht pushen). **Solange build.py nicht reconciliaten ist, ist der normale Worker-Ablauf (build.py aendern -> rebuild -> HTML mitcommitten) blockiert.**

### Empfohlene Reconciliation (durch Michael bzw. nach Freigabe)
`build.py` so nachziehen, dass es die live-HTML **1:1 reproduziert** — d.h. die im Commit 88ca226 an der HTML vorgenommenen DSGVO-Aenderungen in den Generator ueberfuehren:
1. Head-Template: externe Google-Fonts-Bloecke **entfernen**, self-hosted `<link rel="stylesheet" href="/assets/fonts.css">` einsetzen.
2. Kontaktformular-Template: `form-note` durch die **Consent-Checkbox**-Markup ersetzen (wie in live `kontakt/index.html`).
3. Datenschutz-Generator: Font-Abschnitt auf "lokal gehostet" + WhatsApp-Abschnitt anpassen (Text wie live `datenschutz/index.html`).
4. style.css/app.js: pruefen, welche Datei-Version die Wahrheit ist (live-HTML referenziert `91d09e05`/`41872035`); sicherstellen, dass der md5-Hash-Mechanismus in build.py dazu passt.
5. Akzeptanzkriterium: frischer Clone + `python scripts/build.py` erzeugt **0 Abweichung** gegen die aktuell committete HTML (ausser bewusst datumsgetriebenen `lastmod`/`Stand:`).

### Danach: aufgeschobene Tag-13-CWV-Fixes (erst nach erfolgreicher Reconciliation anwenden)
**(b) fetchpriority=high fuer Unterseiten-Hero (LCP).** Die 13 Unterseiten-Heroes werden ueber `subimg()` (build.py ~Zeile 180) erzeugt und haben nur `loading="eager"` — **ohne** `fetchpriority="high"`. Die Startseite (Zeile ~412) hat es bereits. Das Hero-`<img>` ist das LCP-Element jeder Seite. **1-Zeilen-Fix** in `subimg()`:
`... role="presentation" loading="eager" decoding="async" ...` -> `... role="presentation" loading="eager" fetchpriority="high" decoding="async" ...`
Rein technisch, kein Content-Change, verbessert LCP-Prioritaet auf allen Unterseiten. (Am Tag 13 lokal gebaut+verifiziert: 13/13 Heroes erhalten das Attribut, HTML valide, JSON-LD parst — aber bewusst NICHT gepusht wegen build.py-Divergenz.)

**(c) Re-Kompression grosser Hero-webp (Neu-Encoding -> Freigabe).** Ausgelieferte Hero-Bilder ueber Budget:
- `assets/img/pantomime-buchen-scaled.webp` — **592 KB** (klar zu gross fuer ein Hero-webp)
- `assets/img/nussknacker-scaled.webp` — **320 KB**
- `assets/img/pantomime-10-scaled.webp` — ~225 KB; `20230623-195739-scaled.webp` — ~217 KB
Vorschlag: auf ~120–180 KB re-encodieren (Qualitaet ~80, sinnvolle Zielbreite fuer Hero). Verkleinert LCP-Payload spuerbar. Neu-Encoding = Freigabe noetig; `scripts/process_images.py` vorhanden (Pipeline pruefen). Quelle in `assets/img-src/` (nicht ausgeliefert) bleibt unveraendert.

### Render-blocking / Fonts (Sachstand, kein Handlungsbedarf)
`assets/fonts.css` nutzt durchgaengig `font-display: swap` (18x) — Text rendert sofort. Nur `fonts.css` + `style.css` sind render-blocking, kein JS-Framework (GA4 laedt via defer/spaeter). Fuer diese Seitengroesse unkritisch.

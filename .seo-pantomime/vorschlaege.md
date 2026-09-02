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

## Vorschlag 7 — 2026-07-17 (Tag 15): Reziproke Cross-Domain-Links haerten

**Status:** WARTET AUF FREIGABE von Michael.
**Typ:** Cross-Domain-Verlinkung — Punkte 1+2 = Aenderungen an den Fremd-Domains (liar-entertainer.com, zauberer-liar.de); Punkt 3 = On-Page-Micro-Fix an pantomime-la-france.eu, gekoppelt an den V5-build.py-Rebuild.

### Befund (Tag-15-Audit, live via Chrome geprueft)
- **FORWARD** (pantomime-la-france.eu-Footer -> Eigen-Domains): Cross-Links auf liar-entertainer.com und zauberer-liar.de sind vorhanden, follow (`rel="noopener"`, kein nofollow), Ziele = Startseiten. **Schwaeche:** Ankertext = nackte Domainnamen (`liar-entertainer.com`, `zauberer-liar.de`) — nicht descriptiv, kein Keyword-Signal.
- **REVERSE** (Fremd-Domains -> pantomime-la-france.eu):
  - **liar-entertainer.com**: verlinkt Ankertext "Pantomime" auf die **alte Subdomain** `https://pantomime.liar-entertainer.com` (`rel="noopener noreferrer"`). Diese 301-redirectet zwar auf `https://www.pantomime-la-france.eu/` (verifiziert), aber (a) Umweg ueber Redirect statt direktem Link, (b) `noreferrer` unterdrueckt Referral-Zuordnung in GA4.
  - **zauberer-liar.de**: **KEIN** Link zur Pantomime-Domain (nur `mailto:`). Cross-Link fehlt vollstaendig.
- Schema `sameAs` auf pantomime-la-france.eu (#liar) listet bereits beide Domains — ok, keine Aenderung noetig.

### Vorschlag (priorisiert)
1. **liar-entertainer.com — Pantomime-Link korrigieren (PRIO 1, schnell, in Michaels Hand):** Ziel des "Pantomime"-Links von `https://pantomime.liar-entertainer.com` auf die direkte Adresse `https://www.pantomime-la-france.eu/` aendern (Redirect-Hop sparen, volle Link-Kraft). Ankertext descriptiv erweitern, z.B. "Pantomime & Walk Act in NRW". `noreferrer` entfernen (nur `noopener` behalten), damit Referral-Traffic in GA4 sichtbar wird. Die neue Domain ist die kanonische Zielseite — der Hauptsite-Link sollte direkt dorthin zeigen.
2. **zauberer-liar.de — Cross-Link ergaenzen:** descriptiven Link auf `https://www.pantomime-la-france.eu/` einbauen (Footer oder passende Content-Stelle), z.B. "Pantomime & Walk Act – LIAR". Schliesst die fehlende dritte Kante im Domain-Dreieck.
3. **pantomime-la-france.eu — Footer-Anker descriptiv (an V5 gekoppelt):** Im `FOOTER`-Block von build.py die nackten Domain-Anker durch descriptive ersetzen, z.B. "LIAR – Clown & Zauberer (liar-entertainer.com)" und "Zaubershow – Zauberer LIAR (zauberer-liar.de)". **Nicht heute anwendbar**, da jeder build.py-Rebuild die DSGVO-Fixes revertet (siehe Vorschlag 5). Diesen 2-Zeilen-Fix in den V5-Reconciliation-Batch aufnehmen und gemeinsam ausrollen.

### Leitplanken
Nur descriptive, wahrheitsgemaesse Anker (kein Keyword-Stuffing). Reziproke Eigen-Domain-Links sind legitim und nuetzlich (kein Link-Schema). Punkt 3 erst NACH V5-Freigabe/Reconciliation, sonst DSGVO-Regression. Erfolgskontrolle: Referral-Traffic in GA4 + Impressionen-Entwicklung fuer Pantomime-/Walk-Act-Queries in GSC.

---

## Vorschlag 8 — 2026-07-20 (Tag 16): Clown-Seite Title/Description um "Pantomime" ergaenzen (V5-Batch-Item)

**Status:** Technisch fertig ausgearbeitet — anwendbar erst NACH V5-Freigabe/Reconciliation (build.py-Rebuild noetig). Inhaltlich ein regulaerer On-Page-Auto-Fix (Title/Desc-Kategorie), KEINE neue Content-Erweiterung.
**Typ:** On-Page Title/Meta-Description via build.py, gekoppelt an den V5-Rebuild-Batch.

### Befund (GSC live 2026-07-20, Fenster 14.06.-18.07.26)
45 Impressionen, 0 Klicks, Pos 20,3. /figuren/der-clown/ ist mit **35 von 45 Impressionen** die dominante Seite. Top-Query-Cluster: `pantomime clown` (4), `clown pantomime` (3), `pantomime clowns` (1) — d.h. **8 der 45 Impressionen kombinieren "Pantomime"+"Clown"** (Pos ~11-13, Seite 2). ABER: Title und Meta-Description der Clown-Seite enthalten das Wort "Pantomime" NICHT (nur der Fliesstext, 16x). Fuer die real gesuchte Kombination fehlt das Relevanz-/CTR-Signal genau dort, wo Google es im Snippet zeigt.

### Fix (exakte Strings, Laengen verifiziert)
- Title alt (53 Z.): `Clown in NRW buchen – LIAR | Kinderfest & Firmenfeier`
- **Title neu (49 Z.):** `Clown & Pantomime in NRW buchen – LIAR | Walk Act` — Query-Kombi vorn, beide Fokus-Keywords enthalten, wahrheitsgemaess (LIAR ist Pantomime, Clown ist Comedy-Walk-Act ohne Worte).
- Desc alt (151 Z.): `Clown & Comedy-Walk-Act in NRW buchen: LIAR bringt mit Mimik, Slapstick und Improvisation alle zum Lachen – für Kinderfeste, Stadtfeste & Firmenfeiern.`
- **Desc neu (146 Z.):** `Pantomime-Clown & Comedy-Walk-Act in NRW buchen: LIAR bringt mit Mimik und Slapstick alle zum Lachen – für Kinderfeste, Stadtfeste & Firmenfeiern.`
- Anwendung wie Tag 10: meta description + og:description + og:title + Service-Schema-description synchron in build.py aendern (Deckungsgleichheit Schema/Sichtbares wahren), Py3.12-Rebuild, byte-verifizieren.

### Warum jetzt nicht committet
Jeder build.py-Rebuild revertet weiterhin die DSGVO-Fixes aus 88ca226 (heute erneut verifiziert: build.py auf origin/main enthaelt noch externe Google-Fonts-Links). Fix daher in den V5-Batch aufgenommen (zusammen mit Vorschlag-7-Punkt-3 Footer-Anker + fetchpriority). Nach V5-Freigabe kann der Worker alle Batch-Items in EINEM verifizierten Rebuild ausrollen.

---

## Update 2026-07-20: V5 FREIGEGEBEN und ausgerollt

Michael hat V5 freigegeben. Umgesetzt im heutigen Batch (byte-verifiziert, 1 Commit): build.py-Reconciliation (Patch 2026-07-07), fetchpriority=high fuer 13 Unterseiten-Heroes (Tag 13), descriptive Footer-Anker auf allen 15 Seiten (Vorschlag 7 Punkt 3), Clown-Title/Desc mit Pantomime-Keyword (Vorschlag 8). Die Rebuild-Sperre ist aufgehoben.

**Weiter offen:** Vorschlag 3 (Anlass-Content), Vorschlag 4 (/pantomime-essen/), Vorschlag 6 (Off-Page), Vorschlag 7 Punkte 1+2 (Links auf liar-entertainer.com/zauberer-liar.de - liegt bei Michael), V5-Rest: Re-Kompression der grossen Hero-Bilder (pantomime-buchen 592KB, nussknacker 320KB).


---

## FREIGABE-ROLLOUT — 2026-07-21 (Michael: „ich gebe alles frei")

- **Vorschlag 3 (Anlass-Content, Option A): ERLEDIGT.** Startseiten-Anlass-Teaser (Hochzeit/Firmenfeier/Messe/Stadtfest) auf je 2-3 belegte Saetze mit descriptiven internen Links vertieft. Commit 4c6efe2.
- **Vorschlag 4 (/pantomime-essen/): ERLEDIGT.** Neue Landingpage live: 8 belegte Essen-Referenzen, FAQ (Schema==sichtbar), Service-Schema areaServed Essen, sitemap (15 URLs), Reverse-Link aus Pantomime-NRW-Staedteliste. Commit 4c6efe2. Pilot — Wirkung 4-6 Wochen in GSC messen, erst dann weitere Staedte.
- **Vorschlag 5 Rest (Bild-Re-Kompression): ERLEDIGT.** 4 Hero-webp 1,3MB -> 838KB (Pillow, moderate Resize 1280/1440w). Commit 4466b2a (GitHub-Web-Upload; Binaer-Push via MCP nicht moeglich).
- **Vorschlag 6 (Off-Page): FREIGEGEBEN — naechster Schritt bei Michael.** Fertige Profiltexte (NAP-konsistent, nur belegte Fakten): siehe `.seo-pantomime/v6-v7-texte.md`. Prio 1: Google Unternehmensprofil anlegen.
- **Vorschlag 7.1+7.2 (Fremd-Domain-Links): FREIGEGEBEN — naechster Schritt bei Michael.** Fertige Copy-Paste-Link-Snippets fuer liar-entertainer.com und zauberer-liar.de: siehe `.seo-pantomime/v6-v7-texte.md`.

---

## Tag 27 — 2026-08-09 (Beobachtung, kein neuer Freigabe-Vorschlag)

**Meilenstein:** Alle 15 Seiten sind jetzt indexiert (URL-Pruefung). Die 6 Antraege vom 08.08. (Nussknacker, Weihnachtsmann, Zauberer, Crazy Kellner, Impressum, Datenschutz) sind durch. Damit ist die Indexierungs-Baustelle geschlossen; der Hebel liegt ab jetzt bei Position und CTR, nicht mehr bei Sichtbarkeit ueberhaupt.

**Zwei Punkte fuer Tag 28 (noch kein Freigabe-Bedarf, erst Datenpruefung):**

1. `/pantomime-essen/` hat mit **Pos 41,9** die schlechteste Durchschnittsposition aller Seiten bei immerhin 19 Impressionen (28 Tage). Die Stadt-Pilotseite zieht Impressionen, rankt aber tief. Vor einer Ausweitung auf weitere Staedte (Vorschlag 12er-Reihe) sollte geklaert werden, ob die Seite On-Page nachgeschaerft werden muss — sonst wird ein schwaches Muster vervielfacht.
2. `zauberer gladbeck` ist mit 7 Impressionen (Pos 18,3) die **staerkste Query der Domain** — staerker als jede Pantomime-Query. Das ist ein weiteres Argument fuer **Vorschlag 7.2** (Cross-Link von zauberer-liar.de auf pantomime-la-france.eu): die Zauberer-Nachfrage in Gladbeck existiert messbar und laeuft bisher ungebuendelt.

**Weiterhin offen bei Michael:** Vorschlag 6 (Google Unternehmensprofil, Prio 1), Vorschlag 7.1 + 7.2 (Links auf liar-entertainer.com / zauberer-liar.de), Vorschlag 8 (H1 der Startseite mit Fokus-Keyword).

---

## Vorschlag 9 — 2026-08-11 (Tag 28): Content-Tiefe der Stadt-Pilotseite /pantomime-essen/

**Status: WARTET AUF FREIGABE von Michael**
**Typ: Content-Erweiterung (sichtbarer Fliesstext) — kein Auto-Commit erlaubt**

**Datenlage (GSC 28 Tage, 13.07.–09.08.26):** `/pantomime-essen/` hat 20 Impressionen (3.-meiste Seite) bei **Position 40,3** — die schlechteste Position aller Seiten. Queries sind vollstaendig anonymisiert ("Keine Daten"), es ist also nicht ablesbar, wofuer die Seite ausgeliefert wird.

**Heute bereits per Auto-Commit behoben (Technik, keine Freigabe noetig):** Die Seite hatte nur **einen einzigen** internen Link (aus der NRW-Pantomime-Seite). Jetzt verlinken **7 Seiten** descriptiv darauf (5 weitere Figurenseiten + Staedte-Chip der Startseite). Das interne Link-Signal war die groesste technische Schwaeche und ist gefixt.

**Verbleibende Schwaeche (Freigabe noetig):** Der Kern-Fliesstext der Seite ist mit rund 1.300 Zeichen deutlich duenner als die Vergleichsseiten `/figuren/der-pantomime-in-nrw/` und `/walk-act/`. Die Referenzliste (8 belegte Essener Auftraggeber) ist der staerkste, aber unkommentierte Teil.

**Vorschlag (nur belegte Fakten aus INHALTE-VERIFIZIERT.md):**
1. Referenz-Cluster einordnen statt nur auflisten — 2–3 Saetze, welche Art von Anlaessen das waren (Messe, Stadtfest, soziale Traeger), ohne neue Zahlen oder Details zu erfinden.
2. Einen Absatz "Pantomime auf Messen in Essen" ergaenzen (Messe Essen ist belegte Referenz) — bedient die naheliegende kommerzielle Suchintention.
3. Zwei weitere FAQ-Eintraege (Vorlaufzeit, Auftrittsdauer) — Text muss identisch in `faq_block` UND `faq_schema`.

**Messvorgabe:** Wirkung der heutigen internen Verlinkung erst 3–4 Wochen beobachten. Wenn die Position dann unter ~30 faellt, ist die Seitenvorlage tragfaehig und weitere Staedte sind vertretbar. Faellt sie nicht, ist die Vorlage zu duenn — dann Content zuerst, Ausweitung spaeter.

---

## Tag 28 — 2026-08-11: Befund zu "zauberer gladbeck" (Ergaenzung zu Vorschlag 7.2)

`zauberer gladbeck` ist mit 12 Impressionen (3M) die mit Abstand staerkste Query der Domain, Position 18,1. **Neu ermittelt (Query-Filter in GSC):** Google liefert dafuer **`/ueber-mich/` (11 Impressionen)** und `/impressum/` (1) aus — **nicht** die thematisch passende Seite `/figuren/der-zauberer/` (die hat ueber alle Queries nur 2 Impressionen).

Bewertung: Die Zauberer-Nachfrage in Gladbeck existiert messbar, landet aber auf einer Seite ohne Buchungs-Fokus. Da "Zauberer" nicht Fokus-Keyword dieser Domain ist und mit `zauberer-liar.de` eine eigene Domain existiert, ist das kein Anlass, hier Zauberer-Content aufzubauen — es ist das **staerkste bisherige Argument fuer Vorschlag 7.2** (Cross-Link von zauberer-liar.de hierher bzw. Buendelung der Zauberer-Nachfrage auf der Zauberer-Domain). Entscheidung liegt bei Michael.

---

## Tag 29 — 2026-08-28: Erste Klicks + verschaerfter Befund zu Vorschlag 6 und 7.2

**Neue Datenlage (GSC 3 Monate, 14.06.–25.08.26):** Die Domain hat erstmals Klicks: **6 Klicks bei 432 Impressionen (CTR 1,4 %, Pos 25,4)**. Die einzige Klick-Query ist `pantomime clown` (13 Impressionen, 2 Klicks) auf `/figuren/der-clown/`.

**Heute per Auto-Commit behoben (Technik, keine Freigabe noetig):** Title von `/figuren/der-clown/` auf die Wortfolge der Klick-Query umgestellt (48 → 56 Zeichen), Meta-Description von `/ueber-mich/` von rein biografisch auf handlungsorientiert mit Ort und Anfrage-CTA (155 Zeichen). Commit `bbd9cb3`.

**Verschaerfung Vorschlag 6 (Google Unternehmensprofil) — Prio 1, unveraendert offen:**
`zauberer gladbeck` ist von 12 auf **54 Impressionen** gestiegen und damit mit Abstand die groesste Einzel-Query der Domain — bei **0 Klicks**. Das ist eine lokale Dienstleister-Suche mit Ortsbezug. Genau diese Suchen werden in der Praxis ueber das Google Unternehmensprofil (Local Pack / Maps) bedient, nicht ueber ein organisches Ergebnis auf Position ~18. Solange kein Profil existiert, bleibt dieser Nachfrageblock unbeantwortet. Aktion liegt bei Michael (Kontoanlage), Profiltexte liegen fertig in `.seo-pantomime/v6-v7-texte.md`.

**Verschaerfung Vorschlag 7.2 (Zauberer-Nachfrage buendeln) — freigegeben, Einbau offen:**
Query-Filter auf `/figuren/der-zauberer/` zeigt: `zauberer liar` 6, `zauberer gladbeck` 3, `zauberer bochum` 3, `zauberer gelsenkirchen` 1, `zauberer nrw` 1 — bei Position 54,5 und 68 Impressionen. Die Zauberer-Nachfrage ist inzwischen der **zweitgroesste Traffic-Treiber dieser Domain**, obwohl „Zauberer" hier kein Fokus-Keyword ist und mit `zauberer-liar.de` eine eigene Domain existiert. Empfehlung bleibt: Nachfrage per Cross-Link auf die Zauberer-Domain buendeln statt hier Zauberer-Content aufzubauen. Link-Snippets liegen in `.seo-pantomime/v6-v7-texte.md`.

**Erster Walk-Act-Erfolg (kein Handlungsbedarf, nur Beobachtung):**
`walking act essen` erscheint erstmals als Query — auf `/pantomime-essen/`, nicht auf `/walk-act/`. Nach 29 Tagen ist das die erste Walk-Act-Query der Domain ueberhaupt. Wird in Tag 30 weiter beobachtet; falls sich das verstetigt, ist zu pruefen, ob `/walk-act/` als Zielseite gestaerkt werden muss.

---

## Tag 30 — 2026-09-01: Stadtseiten-Pilot Essen ist bestaetigt — Vorschlag 10 (Ausweitung) + Zyklus-1-Bilanz

**Messvorgabe aus Vorschlag 9 ist erfuellt.** Vorgabe war: „Wenn die Position nach 3–4 Wochen unter ~30 faellt, ist die Seitenvorlage tragfaehig." Ergebnis GSC 28-Tage-Fenster (02.08.–29.08.26): `/pantomime-essen/` steht bei **Position 10,0** (8 Impressionen). Im 3-Monats-Fenster ist es 33,5, im Fenster vom 25.08. war es 34,9 — der Sprung ist also frisch und faellt zeitlich mit der internen Verlinkung aus Tag 28 zusammen. Zusaetzlich ist die Essen-Seite die **einzige Seite der Domain, die fuer eine Walk-Act-Query rankt**: `walking act essen`, Position 7,0.

Damit ist belegt: **Stadt + Leistung** funktioniert auf dieser Domain deutlich besser als die generische NRW-Seite. `/walk-act/` selbst liegt im gleichen Fenster bei Position 34,2 (21 Impressionen) und bekommt fuer seine eigenen Queries von Google keine Aufschluesselung (anonymisiert).

**Heute per Auto-Commit umgesetzt (Technik, keine Freigabe noetig):** `/walk-act/` verlinkt jetzt descriptiv auf `/pantomime-essen/` („Walk Act in Essen") — bis heute verlinkte **keine einzige Seite** von `/walk-act/` auf die Stadt-Pilotseite, obwohl die Gegenrichtung seit Tag 28 auf 7 Seiten existiert. Ausserdem Alt-Text des Essen-Fotos auf `/walk-act/` praezisiert (gleiche Bilddatei, auf der Essen-Seite bereits mit Ortsbezug beschriftet). Commit `55c16a3`.

### Vorschlag 10 — WARTET AUF FREIGABE von Michael: zweite Stadtseite nach dem Essen-Muster

Vorgeschlagen wird **genau eine** weitere Stadtseite als zweiter Pilot, nicht mehrere auf einmal. Auswahlkriterium bleibt wie bei Essen: **belegte Referenzbasis in `INHALTE-VERIFIZIERT.md`**, damit die Seite eigenen, wahren Inhalt hat und keine Thin Page wird.

Kandidaten nach belegter Referenzdichte:
1. **Gladbeck** — Sparkasse Gladbeck, Kulturamt Gladbeck; ausserdem Wohnort/Standort (NAP-Ort). Zusaetzlich staerkste Ortsnachfrage der Domain ueberhaupt (`zauberer gladbeck`, 64 Impressionen). Nachteil: Die Nachfrage ist Zauberer-, nicht Pantomime-Nachfrage — eine Pantomime-Seite bedient sie nur teilweise.
2. **Gelsenkirchen** — AWO Gelsenkirchen, Stadt Gelsenkirchen, Schalke 04.
3. **Bochum** — VFL Bochum (nur eine Referenz; `zauberer bochum` rankt mit 8 Impressionen auf Position 93,6, also praktisch unsichtbar).

**Empfehlung:** Gelsenkirchen, weil die Referenzbasis dort aus zwei unabhaengigen Auftraggebertypen (Stadt, sozialer Traeger, Verein) besteht und die Seite damit denselben E-E-A-T-Charakter wie Essen bekommt. Gladbeck waere die Alternative, wenn Michael parallel Vorschlag 6 (Google Unternehmensprofil) umsetzt — dann greifen Profil und Stadtseite am selben Ort ineinander.

**Nicht empfohlen:** mehr als eine Seite gleichzeitig, oder Staedte ohne belegte Referenz. Das wuerde exakt das Thin-Page-Risiko erzeugen, das der Essen-Pilot vermieden hat.

### Zyklus-1-Bilanz (Tag 1–30, 18.06.–01.09.26)

| Kennzahl (3 Monate) | Start | heute |
|---|---|---|
| Klicks | 0 | 6 |
| Impressionen | 0 | 481 |
| Ø Position | – | 24,8 |
| indexierte Seiten | 0 | 14 in GSC mit Daten |
| Queries gesamt | 0 | 17 |

**Engstelle bleibt die CTR (1,2 %), nicht die Sichtbarkeit.** Zyklus 2 wird deshalb auf Klick-Ausbeute priorisiert statt auf weitere Impressionen.

### Weiterhin offen bei Michael (unveraendert)
- **Vorschlag 6** — Google Unternehmensprofil (Prio 1). Bedient `zauberer gladbeck` (64 Impressionen, 0 Klicks) und generell lokale Suche. Texte liegen fertig in `.seo-pantomime/v6-v7-texte.md`.
- **Vorschlag 7.1 / 7.2** — Cross-Links auf `liar-entertainer.com` und `zauberer-liar.de` einbauen (freigegeben, Einbau steht aus).
- **Vorschlag 8** — H1 der Startseite um das Fokus-Keyword ergaenzen.
- **Vorschlag 9** — Content-Tiefe `/pantomime-essen/`. Durch den Positionssprung auf 10,0 jetzt attraktiver: die Seite ist nah an Seite 1, zusaetzliche Tiefe koennte den Rest tragen.
- **Vorschlag 10** — zweite Stadtseite (siehe oben).

---

## FREIGABE-ROLLOUT — 2026-09-01 (Michael: „Vorschlag 7.1 / 7.2 wie Vorschlag 8, 9 und 10 umsetzen")

Alle fünf offenen Code-Vorschläge sind umgesetzt und live. Damit ist von den offenen Punkten nur noch **Vorschlag 6** (Google Unternehmensprofil) offen — der erfordert eine Kontoanlage durch Michael und keinen Code.

### V7.1 — liar-entertainer.com (Repo `ben69mikail/Liar-Entertainer`, Astro) — Commit `dafcf11`
- Header-Nav „Pantomime": Ziel von `https://pantomime.liar-entertainer.com` (alte Subdomain, nur per 301 erreichbar) auf `https://www.pantomime-la-france.eu/`. Redirect-Hop entfällt.
- `rel="noopener noreferrer"` → `rel="noopener"` bei externen Nav-Links. `noreferrer` hatte die Referral-Zuordnung in GA4 der Zielseite unterdrückt.
- Footer-Spalte „Hauptseiten": zusätzlicher descriptiver Link „Pantomime & Walk Act in NRW".
- **Abweichung vom Vorschlag, bewusst:** Der descriptive Ankertext sitzt im Footer, nicht in der Hauptnavigation. Die Top-Nav hat bereits 10 Einträge; „Pantomime & Walk Act in NRW" als Nav-Label hätte die Leiste umbrechen lassen. Das Nav-Label bleibt „Pantomime", der Link zeigt aber auf das richtige Ziel.
- **Live geprüft:** 0 verbleibende Links auf die alte Subdomain; 2 Header-Links (Desktop + Mobile) + 1 Footer-Link, alle `rel="noopener"`.

### V7.2 — zauberer-liar.de (Repo `ben69mikail/ZAubererLIAR`, statisch) — Commit `bc2b11a`
- Footer-Spalte „Shows" auf **allen 29 Seiten**: descriptiver externer Link „Pantomime & Walk Act".
- `walk-act-zauberer.html`: zusätzlicher Kontext-Link im Inhalt unter „Wo ein Walk-Act glänzt" — thematisch passendste Seite, damit der Link nicht nur Footer-Boilerplate ist.
- Keine CSS-/JS-Änderung, daher kein Cache-Bust-Bump nötig (Konvention des Repos eingehalten).
- **Live geprüft:** 2 Links auf `walk-act-zauberer.html` (Content + Footer), `rel="noopener"`.

### V8 — H1 der Startseite — Commit `0ea8f1d`
H1 führt mit „Pantomime & Walk Act in NRW"; der Claim „Eine Kunst, die *ohne Worte* begeistert." bleibt als zweite Zeile im H1 (`span.h1-claim`, kleinere Display-Größe). Der Vorschlagstext („Pantomime & Walk Act – eine Kunst, die ohne Worte begeistert.") wäre als **eine** Displayzeile 61 Zeichen gewesen — bei `clamp(2.7rem,7vw,5.4rem)` und `max-width:15ch` hätte das fünf Zeilen ergeben und den Hero gesprengt. Die zweizeilige Hierarchie liefert dasselbe Keyword-Signal bei stabiler Hero-Höhe. Auf 375 px geprüft: kein Überlauf.

### V9 — Content-Tiefe /pantomime-essen/ — Commit `0ea8f1d`
1. Referenz-Cluster eingeordnet (Wirtschaft/Messe, öffentliche Hand, soziale Träger) — zwei Absätze, ausschließlich aus `INHALTE-VERIFIZIERT.md`.
2. Neuer Abschnitt „Pantomime auf Messen in Essen".
3. FAQ von 3 auf 5. **Bewusst NICHT umgesetzt:** die vorgeschlagenen FAQ zu Vorlaufzeit und Auftrittsdauer — dazu gibt es keine belegten Angaben in `INHALTE-VERIFIZIERT.md`. Stattdessen zwei belegte Fragen (Anfrageweg, Anpassung an das Publikum). Inhalts-Regel bleibt: nichts erfinden.

### V10 — /pantomime-gelsenkirchen/ — Commit `0ea8f1d`
- Aufbau nach dem bestätigten Essen-Muster; nur belegte Referenzen (Stadt Gelsenkirchen, AWO Gelsenkirchen, Schalke 04).
- Interne Verlinkung beidseitig: Städte-Chip der Startseite, Städteliste der 6 Figurenseiten, Links von der GE-Seite auf `/pantomime-essen/`, `/walk-act/`, `/figuren/der-pantomime-in-nrw/`.
- Schema: BreadcrumbList + FAQPage + Service (`areaServed: Gelsenkirchen`). Sitemap: 16 URLs, Priorität 0,8 für alle `/pantomime-*/`-Stadtseiten.
- **Hinweis zur Referenzbasis:** Gelsenkirchen hat 3 belegte Auftraggeber gegenüber 8 in Essen. Die Seite ist damit dünner als der Pilot. Wenn die Position nach 4 Wochen nicht unter ~30 kommt, ist das der Beleg, dass die Vorlage eine dichtere Referenzbasis braucht — dann keine weiteren Städte.

### Nebenbefunde aus dem Live-Check (nicht vorgeschlagen, aber gefunden und behoben)

**1. Reveal-Animation blockierte die Sichtbarkeit — Commit `c181ced`.** Alle 27 `.reveal`-Elemente blieben auf `opacity:0`, wenn das Dokument im Hintergrund rendert (`document.visibilityState === "hidden"`): IntersectionObserver feuert dort nicht, die Klasse `in` wird nie gesetzt, die Seite ist inhaltlich leer. Betrifft Hintergrund-Tabs, Prerender und headless Renderer. Drei Ebenen abgesichert: `.reveal` ist jetzt standardmäßig sichtbar und wird nur unter `.js` versteckt (Klasse per Inline-Script im `<head>`) — ohne JavaScript ist die Seite vollständig lesbar; `app.js` blendet bei nicht sichtbarem Dokument sofort alles ein; zusätzlich ein 3-Sekunden-Sicherheitsnetz. Für normale Besucher ändert sich nichts.

**2. Fließtext-Links waren nicht als Links erkennbar — Commit `7db2172`.** Global gilt `a{color:inherit;text-decoration:none}` — richtig für Navigation und Karten, aber im Lauftext fehlte jede Affordanz. Betroffen war die **gesamte interne Verlinkung, die seit Tag 5 aufgebaut wurde**: Leser konnten sie schlicht nicht sehen, der Klickpfad zwischen den Seiten lag brach. Jetzt Crimson mit dezenter Unterstreichung, Hover verstärkt, `:focus-visible` mit Outline; auf crimson-Flächen Gold-Variante.

**3. Instagram-Selfie und Fehlausschnitt auf der neuen Stadtseite — Commits `7db2172`, `5ce50bf`.** Das ursprünglich gewählte `pantomime-1.webp` ist ein hochkant gedrehtes Instagram-Selfie mit eingebranntem Overlay („@BEN_MIKAIL, Bon Jovi – It's My Life") — auf einer Buchungsseite unbrauchbar. Ersetzt durch ein Veranstaltungsfoto. Das Hero-Motiv wurde zusätzlich getauscht, weil das Porträt im breiten Hero-Band auf Mütze und Wand beschnitten wurde und das Gesicht außerhalb des Ausschnitts lag.

### Weiterhin offen bei Michael
- **Vorschlag 6 — Google Unternehmensprofil (Prio 1).** Kein Code, sondern Kontoanlage. Bedient `zauberer gladbeck` (64 Impressionen, 0 Klicks). Fertige Texte in `.seo-pantomime/v6-v7-texte.md`.

---

## Vorschlag 11 — Zielseiten-Konflikt „zauberer gladbeck" (02.09.2026) — WARTET AUF FREIGABE

**Befund (GSC, 28 Tage 03.08.–30.08.2026).** `zauberer gladbeck` ist mit **67 Impressionen** die mit Abstand größte Einzelquery der Domain — rund 17 % aller Impressionen — und liefert **0 Klicks**. Ausgeliefert wird dafür `/ueber-mich/` (Position 17,1), nicht die Zauberer-Figurenseite. `/figuren/der-zauberer/` hat mit 93 Impressionen die zweithöchste Sichtbarkeit der ganzen Domain, steht aber auf **Position 55,2**. Der Grund ist banal: `/ueber-mich/` nennt Gladbeck sechsmal, `/figuren/der-zauberer/` nur zweimal und weder im Title noch in der Description. Google wählt daher die biografische Seite statt der Buchungsseite.

Dazu kommen vier neue Stadt-Zauberer-Queries im selben Fenster: `zauberer laer` (Pos 39), `zauberer warendorf` (45), `zauberer ratingen` (86), `zauberer gelsenkirchen` (82,5). Der Bedarf ist also breiter als eine Stadt.

**Warum das nicht auto-committet wurde.** Ein reiner On-Page-Fix wäre technisch trivial und laut Regelwerk erlaubt. Er hätte aber eine strategische Nebenwirkung: er baut Zauberer-Sichtbarkeit auf der **Pantomime**-Domain aus, obwohl es mit `zauberer-liar.de` eine eigene Domain für genau dieses Thema gibt. Die beiden Eigen-Domains würden dann gegeneinander optimiert. Das ist eine Entscheidung für Michael, nicht für den Autopiloten.

**Option A — On-Page hier schärfen.** Title/Description von `/figuren/der-zauberer/` mit Ortsbezug Gladbeck/Ruhrgebiet, dazu ein descriptiver interner Link von `/ueber-mich/` auf die Zauberer-Seite. Schnell umsetzbar, holt die Query voraussichtlich auf die richtige Seite. Preis: Zauberer-Traffic wächst auf der Pantomime-Domain.

**Option B — Query bewusst abgeben.** Auf `pantomime-la-france.eu` nichts verstärken, stattdessen den Cross-Link zu `zauberer-liar.de` an dieser Stelle prominenter setzen. Saubere Domain-Trennung. Preis: rund 67 Impressionen im Monat wandern aus dieser Property heraus.

**Option C — Mischform (Empfehlung).** `/figuren/der-zauberer/` bleibt Übersicht und Teaser, verlinkt aber descriptiv weiter auf `zauberer-liar.de`. `/ueber-mich/` behält seine biografisch korrekte Zauberer-Nennung, bekommt aber einen klaren Weiterleitungspfad zur Zauberer-Domain. Damit geht der Nutzer nicht verloren, und die Fokus-Keywords dieser Domain — Pantomime und Walk Act — bleiben unverwässert.

**Empfehlung: Option C.** Ergänzend bleibt Vorschlag 6 (Google Unternehmensprofil) der wirksamste Hebel für genau diese lokale Query, weil ein Unternehmensprofil bei `zauberer gladbeck` über dem organischen Ergebnis steht.

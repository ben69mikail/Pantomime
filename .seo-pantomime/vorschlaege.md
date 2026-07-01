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

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

# SEO-Vorschlaege pantomime-la-france.eu (warten auf Freigabe von Michael)

## Vorschlag 1 — 2026-06-23 (Tag 4): Footer-Ueberschriften von <h4> zu Nicht-Heading umstellen

**Status:** ERLEDIGT, verifiziert & gepusht am 2026-06-23. Fix umgesetzt: build.py-Footer `<h4>` -> `<p class="footer-h">`, style.css-Selektor erweitert, alle 15 HTML regeneriert. Frischer Clone + Rebuild = 0 Abweichung. Kein offener Handlungsbedarf.

### Befund (Tag-4-Audit)
Jede Seite hat genau 1 H1. Der globale Footer nutzte `<h4>Figuren</h4>` und `<h4>Kontakt</h4>` -> Heading-Level-Spruenge. Fix: Footer-Spaltentitel sind Navigations-Labels, kein Heading -> auf `<p class="footer-h">` umgestellt (visuell identisch via erweitertem CSS-Selektor).

---

## Vorschlag 2 — 2026-06-25 (Tag 6): FAQ-Inhalte sichtbar auf der Seite rendern (Schema <-> Sichtbarkeit)

**Status:** WARTET AUF FREIGABE von Michael.
**Typ:** Content-/Struktur-Aenderung (sichtbarer FAQ-Block auf 8 Seiten) -> KEINE Auto-Fix-Kategorie, daher Vorschlag.

### Befund (Tag-6-Schema-Audit, im Build-VM verifiziert)
Alle anderen Schema-Typen sind sauber:
- BreadcrumbList (alle Seiten): Positionen/Namen/URLs korrekt. Kein sichtbarer Breadcrumb noetig. OK.
- Service (6 Figurenseiten): `provider.@id` referenziert korrekt die Org-`@id` (`#liar`), serviceType = Figurenname. OK.
- LocalBusiness/PerformingGroup (`org_schema`, Startseite): Adresse, Telefon, E-Mail, areaServed - faktische Konstanten, stimmen mit Impressum/Kontakt ueberein. OK.
- Person (Ueber mich), ContactPage (Kontakt): strukturell korrekt. OK.

EINZIGES Problem - FAQPage ohne sichtbaren Inhalt:
8 Seiten geben `FAQPage`-Structured-Data aus, aber der Frage-/Antworttext steht NUR im `<script type="application/ld+json">`-Block - NICHT im sichtbaren Seiteninhalt. Verifiziert: nach Entfernen aller `<script>`-Bloecke ist die Trefferzahl fuer jeden FAQ-Fragetext = 0.

| Seite | FAQPage-Schema | Sichtbarer FAQ-Block |
|---|---|---|
| / (Start) | ja (2 Fragen) | NEIN |
| /walk-act/ | ja (2 Fragen) | NEIN |
| /figuren/der-pantomime-in-nrw/ | ja | NEIN |
| /figuren/der-clown/ | ja | NEIN |
| /figuren/der-zauberer/ | ja | NEIN |
| /figuren/der-crazy-kellner/ | ja | NEIN |
| /figuren/der-nussknacker/ | ja | NEIN |
| /figuren/der-weihnachtsmann/ | ja | NEIN |

Warum das ein Problem ist: Googles FAQPage-Richtlinie verlangt, dass der vollstaendige Frage- und Antworttext fuer den Nutzer auf der Seite sichtbar ist. Schema ohne sichtbaren Gegenpart gilt als Verstoss und kann zu einer manuellen Massnahme / Aberkennung der strukturierten Daten fuehren. Zudem zeigt Google FAQ-Rich-Results seit April 2023 nur noch fuer staatliche/Gesundheits-Seiten - der unsichtbare Markup bringt also keinen Rich-Result-Vorteil, traegt aber das Richtlinienrisiko.

### Empfohlener Fix (Inhalt ist bereits vorhanden - nur sichtbar machen)
Die Frage-/Antwort-Paare existieren schon als Daten (`f['faq']` bzw. die inline-Listen fuer Start/Walk-Act). Sie muessen nur zusaetzlich als sichtbarer HTML-Block gerendert werden, dann deckt sich Schema mit Sichtbarem.

1. scripts/build.py - neuen Helper ergaenzen (Akkordeon ueber natives `<details>`/`<summary>`, kein JS), der pro Q/A ein `<details class="faq-item"><summary>Frage</summary><div class="faq-a"><p>Antwort</p></div></details>` erzeugt und in eine `<section>` mit `<h2>Haeufige Fragen</h2>` haengt.
2. Block einbauen vor `cta_band()` / vor dem Footer auf den 8 Seiten, die FAQ-Schema haben:
   - Startseite (`home_body`): faq_block mit den selben 2 Q/A wie im faq_schema
   - Walk-Act (`walk_body`): dito mit den 2 Walk-Act-Fragen
   - Figuren-Builder (Schleife ~Zeile 540-575): faq_block(f['faq'], Titel "Haeufige Fragen - <Figurenname>")
   - WICHTIG: Exakt denselben Text wie im jeweiligen faq_schema(...) verwenden, sonst bleibt die Diskrepanz.
3. assets/style.css - minimales Styling fuer `.faq-item`/`summary`/`.faq-a`. CSS-Aenderung -> `style.css?v=<md5>` aendert sich -> alle 15 HTML mitcommitten.
4. Build + Verify (PFLICHT): `python scripts/build.py` (Python 3.12+), pruefen dass auf jeder der 8 Seiten der FAQ-Text jetzt AUCH ausserhalb von `<script>` erscheint (Trefferzahl >= 2), schliessendes `</html>`, kein abgeschnittener Output. Dann build.py + style.css + 15 HTML + sitemap (lastmod) in einem Commit.

### Alternative (falls kein sichtbarer FAQ-Block gewuenscht)
FAQPage-Schema auf allen 8 Seiten entfernen. Vermeidet das Risiko sofort, verschenkt aber sichtbaren keyword-tragenden FAQ-Content. Empfehlung: sichtbar machen (Option oben), nicht entfernen.

### Aufwand / Risiko
Mittel. Inhalt existiert bereits (kein Erfinden noetig, INHALTE-VERIFIZIERT-konform), nur Rendering + etwas CSS. Nutzen: Schema-Konformitaet wiederhergestellt + zusaetzlicher sichtbarer, suchrelevanter Text auf 8 Seiten (positiv fuer klassische Suche und KI-Antworten).

# SEO-Vorschlaege pantomime-la-france.eu (warten auf Freigabe von Michael)

## Vorschlag 1 — 2026-06-23 (Tag 4): Footer-Ueberschriften von <h4> zu Nicht-Heading umstellen

**Status:** WARTET AUF FREIGABE von Michael.
**Typ:** Technische Heading-Hierarchie-Korrektur (eigentlich Auto-Fix-Kategorie, aber betrifft das geteilte Footer-Template -> alle 15 Seiten neu generieren, und der Linux-Build/Verify-VM war an Tag 4 nicht startbar; daher als Vorschlag gesichert statt unverifiziert gepusht).

### Befund (Tag-4-Audit, live aus Quellcode verifiziert)
Jede der 9 gepruefften Seiten hat **genau 1 H1** — sauber. ABER der globale Footer nutzt `<h4>Figuren</h4>` und `<h4>Kontakt</h4>`. Da der Footer auf jeder Seite haengt, entstehen Heading-Level-Spruenge (uebersprungene Ebenen), was Google/Screenreader als Strukturfehler werten:

| Seite | Letzte Content-Ueberschrift vor Footer | Sprung |
|---|---|---|
| kontakt/ | h1 | h1 -> h4 (h2+h3 uebersprungen) |
| 404.html | h1 | h1 -> h4 (h2+h3 uebersprungen) |
| ueber-mich/ | h2 | h2 -> h4 (h3 uebersprungen) |
| referenzen/ | h2 | h2 -> h4 (h3 uebersprungen) |
| impressum/ | h1 -> h3 (kein h2) | zusaetzlich h1 -> h3-Luecke |
| datenschutz/ | h1 -> h3 (kein h2) | zusaetzlich h1 -> h3-Luecke |
| index, walk-act, figuren | h3 davor | Footer-h4 folgt korrekt auf h3 — kein Sprung |

### Empfohlener Fix (visuell identisch, nur Markup/Selector)
Die Footer-Spaltentitel sind keine inhaltlichen Ueberschriften, sondern Navigations-Labels — sie sollten kein Heading-Tag sein.

1. **scripts/build.py** (Footer-Template): beide Vorkommen ersetzen
   - `<h4>Figuren</h4>` -> `<p class="footer-h">Figuren</p>`
   - `<h4>Kontakt</h4>`  -> `<p class="footer-h">Kontakt</p>`
2. **assets/style.css**: den bestehenden Selektor erweitern, damit die Optik 1:1 bleibt:
   - bisher: `.footer-col h4{...}`
   - neu:   `.footer-col h4,.footer-col .footer-h{...}` (gleiche Regel, p erbt nicht die globale h1-h4-Display-Schrift, deshalb muss `font-family:var(--body)` in der Regel — ist bereits gesetzt — greifen; zusaetzlich `margin:0 0 1rem` sicherstellen, da p default-margin hat)
3. **Build + Verify (PFLICHT vor Push):** `python scripts/build.py` (Python 3.12+) ausfuehren, generierte HTML pruefen (schliessendes </html>, Footer auf allen 15 Seiten korrekt, kein abgeschnittener Output), dann build.py + style.css + alle regenerierten HTML in EINEM Commit pushen. Praefix `SEO: `.

### Warum nicht sofort gemacht
Der Worker darf HTML nie direkt editieren (nur ueber build.py) und nie ungeprueften Build pushen. Der Sandbox-VM zum Ausfuehren/Validieren von build.py war an diesem Lauf nicht verfuegbar. Sobald der VM laeuft (oder Michael lokal `python scripts/build.py` ausfuehrt), ist der Fix in ~2 Minuten erledigt und verifizierbar.

### Aufwand / Risiko
Klein. Reine Markup-/Selector-Aenderung, kein Textinhalt, kein Keyword-Stuffing. Verbessert Heading-Struktur fuer SEO und Barrierefreiheit (WCAG 1.3.1).

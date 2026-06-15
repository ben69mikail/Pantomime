# Masterplan: Pantomime-Seite klonen, verbessern & ranken

**Projekt:** Neubau der Pantomime-Seite von Liar Entertainer
**Bestehende Seite:** `pantomime.liar-entertainer.com` (WordPress, technisch schwach)
**Neue Domain:** `www.pantomime-la-france.eu`
**Repo:** https://github.com/ben69mikail/Pantomime
**Deploy-Ziel:** IONOS-Webspace-Ordner `/PantomimeNeu`
**Erstellt:** 15.06.2026 (Neufassung nach Grill-Session)
**Ziel:** Schnellere, schönere, suchmaschinen- und KI-optimierte Seite, die für **„Pantomime"** und **„Walk Act"** (regional NRW) stark rankt — vernetzt mit `www.liar-entertainer.com` und `www.zauberer-liar.de`.

---

## 1. Entscheidungen (in Grill-Session bestätigt)

| Nr | Thema | Entscheidung |
|----|-------|--------------|
| 1 | **Domain** | Eigene Keyword-Domain `www.pantomime-la-france.eu`. Alte Subdomain `pantomime.liar-entertainer.com` bleibt, wird per **301** dauerhaft umgeleitet (keine Autorität verschenken). |
| 2 | **Architektur** | **Multi-Page**, Klon-Struktur des Originals + 1 Extra-Seite. Jede Seite = eigene Title/Description/Landingpage. |
| 3 | **Texte** | **Umformulieren, keine neuen Fakten.** Nur Inhalte, die real auf `pantomime.liar-entertainer.com` oder im Pantomime-Menü von `liar-entertainer.com` stehen. Karpathy-konform — keine erfundenen Referenzen, Zahlen, Auszeichnungen. |
| 4 | **Keywords** | Primär **„Pantomime"** + **„Walk Act"**. 12 Klon-Seiten + **1 eigene Walk-Act-Seite**. Städte als Text + Schema `areaServed`, **keine** Doorway-/Stadt-Seiten. |
| 5 | **Logo/Bilder** | Eigenes Logo `LOGO Pantomime.png` (Header) + weite Version (OG/Footer), auf transparent getrimmt. Alle Fotos vom alten WP + Pantomime-Bilder von der Hauptseite → **WebP, lazy-load, echte Alt-Texte**. |
| 6 | **Kontakt** | **Web3Forms-Formular** (Name, Anlass, Datum, Nachricht) + klickbares `tel:` / `mailto:`. Wie Hauptseite, kein Backend, DSGVO-ok. |
| 7 | **Design** | **Elegant-editorial**: Schwarz + Elfenbein + Gold, Serif-Headlines (Playfair/Cormorant) + klare Sans, viel Weißraum, full-bleed Fotos, dezente Scroll-Reveals. Skills `/ui-ux-pro-max` (+21st-magic) & `/impeccable`. |
| 8 | **Analytics** | **Eigene GA4-Property** für `pantomime-la-france.eu` → eigene `G-ID`. Consent Mode v2. |
| 9 | **Cookie-Consent** | DSGVO-Banner; GA4 lädt **erst nach** Zustimmung. |
| 10 | **Deployment** | **GitHub Action auto-deploy** per SFTP nach `/PantomimeNeu` (Secret `SFTP_PASSWORD`). Jeder Push = live. |
| 11 | **Recht** | Impressum **1:1** (echte Angaben, nichts erfunden). Datenschutz inhaltlich übernehmen, aber an neuen Stack anpassen (GA4 + Consent, Web3Forms, IONOS, neue Domain). |
| 12 | **Videos** | **Keine** zum Start. Referenzen-Seite rein bildbasiert; Videos später nachrüstbar. |
| 13 | **Ausführung** | Claude **baut + pusht + richtet Action ein**. User macht 5 login-gebundene Schritte per **geführter Klick-Anleitung**. |
| 14 | **Wartung** | **Wiederkehrender Scheduled-Task** nach Go-Live (wöchentl. GSC, monatl. Report + Content-Nachschärfung). |

**Tech-Stack:** Statisches HTML/CSS/JS — Top Core Web Vitals, läuft auf jedem IONOS-Webspace, kein WordPress-Wartungsaufwand, beste SEO-Basis.

---

## 2. Verifizierte Fakten aus der Quelle (Stand 15.06.2026)

Gecrawlt von `pantomime.liar-entertainer.com` — **nur diese Inhalte sind belegt**:

**6 Figuren:** Pantomime · Zauberkünstler · Clown · Crazy Kellner · Nussknacker · Weihnachtsmann
*(Die früher gelöschte Version erfand fälschlich eine 7. Figur „Living Statue" — entfällt.)*

**Original-Seiten:** Start · Figuren (+6 Unterseiten) · Über mich · Referenzen · Kontakt · Datenschutzerklärung · Impressum

**Original-Überschriften:** „Künstler, Pantomime & Co." · „Künstler für Ihre Veranstaltung" · „Kreativ – Überraschend – Hinreißend – Niveauvoll" · „Brillant & Charmant aus Frankreich" · „Künstler mit Takt und Humor" · „Kurz und Knapp" · „Klassisch und/oder modern?" · „Das können Pantomime Künstler"

**Bestehende Bilder (WP-Uploads, herunterzuladen):**
`Pantomime-5.jpg` · `Pantomime-12.jpg` · `Zauberer-Mieten.png` · `Nussknacker-scaled.jpg` · `Walk-Act-Fest-Essen.jpg` · `Crazy-Kellner.jpg` · `IMG-20170624-WA0010.jpg` (Weihnachtsmann) · `Pantomime-nothing-impossible.png`

**Copyright/Inhaber:** Michael Prescler (seit 2020) · Telefon `0172-1517578`

> **Noch beim Bau zu holen (nicht erfinden):** Volltexte der 6 Figuren-Unterseiten, „Über mich"- und „Referenzen"-Texte, **E-Mail-Adresse** + **Impressum-Adresse** (Kontakt/Impressum-Seite), **Web3Forms-Key**, **GA4-`G-ID`** (User legt Property an), **`SFTP_PASSWORD`** (aus LIAR-Projekt → GitHub-Secret).

---

## 3. Neue Seitenstruktur

```
/                              Start — H1: "Pantomime buchen in NRW – Liar"
/figuren/                      Übersicht der 6 Figuren
  /figuren/der-pantomime-in-nrw/
  /figuren/der-zauberer/
  /figuren/der-clown/
  /figuren/der-crazy-kellner/
  /figuren/der-nussknacker/
  /figuren/der-weihnachtsmann/
/walk-act/                     NEU — eigene Walk-Act-Landingpage (Keyword "Walk Act")
/ueber-mich/                   Über Liar (E-E-A-T / Vertrauen)
/referenzen/                   Fotos + Kundenstimmen (nur real Vorhandenes)
/kontakt/                      Web3Forms-Formular + Telefon + E-Mail
/impressum/                    1:1 echte Angaben
/datenschutz/                  angepasst an GA4 + Web3Forms + IONOS
/404.html
```

Interne Verlinkung: jede Figuren-/Walk-Act-Seite verlinkt zur Buchungsanfrage; gegenseitige Links `liar-entertainer.com ↔ pantomime-la-france.eu ↔ zauberer-liar.de`.

---

## 4. SEO- & KI-Suche-Strategie

**Klassisch / On-Page**
- Title + Description je Seite mit Keyword + Region; eine klare H1, saubere H2/H3.
- Statisch + WebP + minifiziert → Core Web Vitals grün; mobil-first.
- `sitemap.xml` (alle Seiten) + `robots.txt`; kanonische URLs.
- Interne Verlinkung im Netzwerk der 3 Seiten.

**Lokal (entscheidend für „Pantomime NRW")**
- Schema.org `PerformingGroup` + `LocalBusiness` + `Person` mit Ort, Telefon, `areaServed` (Gladbeck, Essen, Oberhausen, Gelsenkirchen, Dortmund, Bochum, Duisburg).
- Städte im Fließtext, **keine** Doorway-Pages.
- Google-Unternehmensprofil verknüpfen.

**KI-Suche / GEO (AI Overviews, ChatGPT, Perplexity)**
- Faktische Direkt-Antworten („Liar ist Pantomime-Künstler in NRW, buchbar für …").
- FAQ-Block mit `FAQPage`-Schema je Schlüsselseite.
- Eindeutige Entitäts-Angaben (Name, Leistung, Region, Kontakt) maschinenlesbar; `BreadcrumbList`-Schema.

---

## 5. Technische Bausteine (Bau)

- **Design-System:** CSS-Variablen (Schwarz/Elfenbein/Gold), Playfair/Cormorant + Sans, responsive Grid, Scroll-Reveals.
- **Bilder:** WP-Download → WebP-Konvertierung, `loading="lazy"`, sprechende Alt-Texte, OG-Bild je Seite.
- **Cookie-Consent:** DSGVO-Banner, Consent Mode v2 (Default „denied"), GA4 erst nach „Zustimmen".
- **Analytics:** GA4 mit eigener `G-ID` (Platzhalter bis User-Property steht).
- **Formular:** Web3Forms (Key als Variable), Honeypot-Spamschutz, Danke-Seite/-Status.
- **Schema:** `PerformingGroup`/`LocalBusiness`/`Person`, `FAQPage`, `BreadcrumbList` als JSON-LD.
- **Performance-Ziel:** Lighthouse 90+ in allen Kategorien.

---

## 6. Deployment & Zugänge

**GitHub:** Repo `ben69mikail/Pantomime`. PAT „waechter" (`GITHUB_PERSONAL_ACCESS_TOKEN`).
**GitHub Action:** bei Push → SFTP-Sync nach `/PantomimeNeu`. Secret `SFTP_PASSWORD` (nie im Repo).
**IONOS SFTP** (analog Hauptseite): Host `home362401740.1and1-data.host`, User `u62702423`, Zielordner `/PantomimeNeu/`.
**301-Redirect:** `.htaccess` auf der **alten** Subdomain → `https://www.pantomime-la-france.eu/` (pfadgenaue Weiterleitung der Figuren-URLs).

---

## 7. Phasenplan & Rollen

**Phase 1 — Analyse & Inhalt (Claude)**
- [ ] Alle Original-Seiten crawlen (Volltexte der 6 Figuren + Über/Referenzen/Kontakt/Impressum/Datenschutz).
- [ ] Alle Bilder herunterladen, kuratieren, WebP-optimieren.
- [ ] Texte SEO-stark umformulieren (nur belegte Fakten), Meta-Tags je Seite, FAQ-Blöcke.

**Phase 2 — Bau (Claude)**
- [ ] Projektstruktur + Design-System; alle Seiten aus Abschnitt 3 als statisches HTML.
- [ ] Logo einbinden (transparent), Bilder, Web3Forms-Formular, Cookie-Consent + GA4-Loader.
- [ ] Schema.org, `sitemap.xml`, `robots.txt`, `.htaccess`, `404.html`.
- [ ] Lokaler Lighthouse-Check (Ziel 90+).

**Phase 3 — Push & Deploy (Claude baut, User klickt geführt)**
- [ ] Code → GitHub pushen, GitHub Action einrichten.
- [ ] **User (geführt):** `SFTP_PASSWORD` als GitHub-Secret hinterlegen.
- [ ] **User (geführt):** Domain `pantomime-la-france.eu` → Ordner `/PantomimeNeu` in IONOS verbinden + SSL.
- [ ] **User (geführt):** GA4-Property anlegen → `G-ID` an Claude → einbauen + Push.
- [ ] **User (geführt):** GSC-Property verifizieren + `sitemap.xml` einreichen.
- [ ] **User (geführt):** 301-`.htaccess` auf alter Subdomain aktivieren.

**Phase 4 — Laufende Optimierung (Scheduled-Task)**
- **Wöchentlich:** GSC-Check (Impressionen/Klicks/Position für „Pantomime" + „Walk Act"), Indexierungsfehler beheben.
- **Monatlich:** Ranking-Report, Content-Lücken schließen, interne Verlinkung stärken, Backlinks (Künstlerverzeichnisse), GBP pflegen.

---

## 8. Offene Eingaben vom User (vor/bei Deploy)

- [ ] GA4-Property anlegen → `G-ID` liefern
- [ ] `SFTP_PASSWORD` als GitHub-Secret + Bestätigung IONOS-Zugang gültig
- [ ] Domain in IONOS mit `/PantomimeNeu` verbinden
- [ ] Web3Forms-Key bestätigen (eigener für Pantomime oder Hauptseiten-Key wiederverwenden?)
- [ ] E-Mail-Adresse für Kontakt/Impressum bestätigen
```

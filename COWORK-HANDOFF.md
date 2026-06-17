# Cowork-Handoff — LIAR Pantomime (pantomime-la-france.eu)

Stand: 2026-06-18. Diese Datei fasst alles Wichtige zusammen, damit Claude Cowork ohne Rückfragen weiterarbeiten kann.

---

## 1. Was ist das Projekt
Statische Marketing-Website für **LIAR** (Michael Prescler), Pantomime-Künstler aus Gladbeck/NRW. Relaunch der alten WordPress-Seite `pantomime.liar-entertainer.com`. Ziel: Buchungsanfragen für Pantomime / Walk Act / Figuren. Keyword-Fokus: **„Pantomime"** + **„Walk Act"**.

- **Live-Domain:** https://www.pantomime-la-france.eu
- **GitHub-Repo:** https://github.com/ben69mikail/Pantomime (Branch `main`)
- **Lokaler Pfad:** `C:\Users\ben_m\Claude\projects\Homepage Pantomime\Pantomime`
- **Hosting:** IONOS-Webspace, Ordner `/PantomimeNeu`

## 2. Tech-Stack (bewusst einfach)
Reines **statisches HTML/CSS/JS**, generiert per Python. Kein Framework, kein Node-Build.
- `scripts/build.py` — DRY-Generator: baut ALLE 15 HTML-Seiten + `sitemap.xml` + `robots.txt`. Head/Header/Footer zentral. Konstanten oben (GA4-ID, Web3Forms-Key, Telefon, Adresse).
- `scripts/process_images.py` — wandelt Quell-Fotos aus `assets/img-src/` → optimierte WebP in `assets/img/`, macht Logo transparent, erzeugt OG-Bild. **Nur laufen lassen, wenn Bilder geändert/ergänzt werden.**
- `scripts/contrast_check.js` — WCAG-Kontrast-Test (im Browser-Console ausführen; `fails===0` = alles sichtbar).

## 3. Wie man Änderungen macht (Workflow)
```powershell
cd "C:\Users\ben_m\Claude\projects\Homepage Pantomime\Pantomime"
# Inhalt/Struktur ändern -> scripts/build.py editieren
# Design ändern -> assets/style.css (statisch) und/oder assets/app.js editieren
python scripts\build.py            # HTML neu generieren
git add -A
git commit -m "..."
git push origin main               # loest Auto-Deploy aus
```
**Cache-Busting:** build.py hängt automatisch `?v=<hash>` an `style.css`/`app.js`. Bei CSS/JS-Änderung NUR über build.py neu bauen, sonst sieht der Browser alte Dateien (immutable-Cache via .htaccess).

## 4. Deploy (automatisch)
Push auf `main` → GitHub Action `.github/workflows/deploy.yml`:
1. baut sauberen `_site/`-Ordner per `rsync` (schließt aus: `.git`, `.github`, `scripts`, `assets/img-src`, `deploy`, `*.md`),
2. lädt per **lftp/SFTP** nach IONOS `/PantomimeNeu`, löscht vorher Alt-`.git/.github/scripts` auf dem Server.
- Secrets im Repo (Settings → Secrets → Actions): `IONOS_SFTP_HOST`, `IONOS_SFTP_USER`, `IONOS_SFTP_PASS`, `IONOS_SFTP_REMOTE`.
- Deploy-Status prüfen: GitHub → Actions → „Deploy to IONOS".

### Push-Stolperstein (wichtig für Cowork!)
Der lokale Git Credential Manager (GCM) kann im **non-interaktiven** Harness nicht prompten → `git push` kann hängen. Funktionierende Wege:
- `git push origin main` (GCM-Credential ist gecacht; in dieser Maschine vorhanden, hat `workflow`-Scope).
- ENV-PAT `GITHUB_PERSONAL_ACCESS_TOKEN` hat nur `repo`-Scope → kann KEINE Workflow-Dateien pushen. Für `.github/workflows/`-Änderungen den GCM-Push nutzen.

## 5. Inhalts-Regel (Karpathy — strikt einhalten)
Nur belegte Fakten aus **`INHALTE-VERIFIZIERT.md`** bzw. von pantomime.liar-entertainer.com. **Nichts erfinden** (keine erfundenen Referenzen, Zahlen, Städte). Texte umformulieren/SEO-schärfen ist ok.
- 6 Figuren: Pantomime, Zauberer, Clown, Crazy Kellner, Nussknacker, Weihnachtsmann.
- Inhaber/Impressum: Michael Prescler, Beethovenstr. 15, 45966 Gladbeck, Tel/WhatsApp 0172-1517578, info@liar-entertainer.com, Finanzamt Marl.
- Cross-Links (gewollt): liar-entertainer.com (Hauptseite), zauberer-liar.de (Zauberer-Seite).

## 6. Design-System (siehe PRODUCT.md)
Belle-Époque-Théâtre-Plakat, **hell**: Bühnenpapier-Creme Grund, Karmin (`--crimson #8c1326`) + Gold (`--gold #b8862b`) als Akzent, Display **Bodoni Moda**, Body **Hanken Grotesk**. Tokens in `assets/style.css` `:root`.
- Hero: durchscheinendes Hintergrundfoto (`cropped-pantomime-11.webp`, `.hero-bg opacity:.75`) + heller Creme-Schleier (`.hero::after`); dunkler Titel mit Creme-Halo (text-shadow).
- Startseite-Pflichtelement: 2×2-Apfel-Fotomontage (`pantomime-4/6/7/9-scaled.webp`) mit „❦ LIAR ❦"-Badge.
- Header: links Logo + Telefonnummer; rechts Nav (Desktop) bzw. WhatsApp-Button + Hamburger (Mobile). Mobile = alle Header-Items gleich verteilt (`display:contents` + `space-between`).

### Design-Lektionen (nicht wieder reinlaufen)
- **KEIN `backdrop-filter` auf `.site-header`** — erzeugt Containing-Block, der das `position:fixed` Mobil-Menü auf Header-Höhe einsperrt (Menü wirkt „kaputt"). Header nutzt jetzt opakes Creme-BG.
- Reveal-Animationen (`.reveal`) blenden per IntersectionObserver ein; auf echten Geräten ok, in Headless-Screenshots evtl. anfangs leer (kein Bug).

## 7. Integrationen
- **GA4:** Property „Pantomime La France", Mess-ID `G-PQ5XK66N5M` (in build.py `GA4_ID`). Lädt erst nach Cookie-Zustimmung (Consent Mode v2 in `app.js`).
- **Web3Forms** (Kontaktformular): Access-Key `e651ce96-e5a5-4088-9947-7c87d557a71e` (in build.py `WEB3FORMS_KEY`). Mails gehen an info@liar-entertainer.com.
- **Cookie-Consent + DSGVO:** Banner in build.py `COOKIE`, Logik in `app.js`. Datenschutz-Seite deckt IONOS, Web3Forms, GA4, Google Fonts ab.

## 8. Dateistruktur (Repo)
```
index.html, figuren/…, walk-act/, ueber-mich/, referenzen/, kontakt/,
impressum/, datenschutz/, 404.html       generierte Seiten (NICHT direkt editieren -> build.py)
assets/style.css        Design-System (statisch, direkt editierbar)
assets/app.js           Cookie-Consent + GA4-Loader, Mobile-Nav, Reveals, Web3Forms
assets/img/             21 referenzierte WebP + logo.png + favicon.png + og-pantomime.jpg
assets/img-src/         Quell-Originale (20 Dateien) — nur fuer process_images.py, nicht deployt
scripts/build.py        Seiten-Generator (Inhalt/Meta/Schema hier aendern)
scripts/process_images.py   Bilder -> WebP
scripts/contrast_check.js   Kontrast-Test
.github/workflows/deploy.yml  Auto-Deploy (lftp/SFTP)
.htaccess, sitemap.xml, robots.txt, llms.txt
INHALTE-VERIFIZIERT.md  Quelle der Wahrheit (Karpathy)
PRODUCT.md              Design-/Marken-Brief
README.md, MASTERPLAN_pantomime-liar.md, NAECHSTE-SCHRITTE.md, COWORK-HANDOFF.md (diese Datei)
```

## 9. Status: erledigt ✅
- Komplette Seite gebaut (15 Seiten), helles theatralisches Design, responsive, WCAG-Kontrast geprüft.
- SEO: Title/Description je Seite, Schema.org (LocalBusiness/Person/Service/FAQ/Breadcrumb), sitemap, robots (inkl. KI-Crawler), llms.txt.
- GA4 + Web3Forms aktiv. Cookie-Consent. Cache-Busting. Mobile-Menü + WhatsApp-Button + Telefon im Header.
- Auto-Deploy läuft (Push → live in /PantomimeNeu). Repo aufgeräumt (44 ungenutzte Dateien entfernt).

## 10. Offen / mögliche nächste Aufgaben für Cowork
- **IONOS:** prüfen, dass Domain `pantomime-la-france.eu` korrekt auf `/PantomimeNeu` zeigt + SSL aktiv. (Seite ist live erreichbar — vermutlich erledigt.)
- **301-Redirect** der alten Subdomain `pantomime.liar-entertainer.com` → neue Domain (im alten WP-Webspace per .htaccess). Status prüfen.
- **Google Search Console:** Property `pantomime-la-france.eu` verifizieren, `sitemap.xml` einreichen, Indexierung der Hauptseiten anstoßen.
- **Phase 4 (laufende SEO):** wiederkehrender Task — wöchentl. GSC-Check (Queries „Pantomime"/„Walk Act"), monatl. Report, interne Verlinkung liar-entertainer.com ↔ pantomime ↔ zauberer-liar.de stärken, Backlinks/Künstlerverzeichnisse, Google-Unternehmensprofil.
- Optional: weitere echte Fotos/Videos einbinden (nur belegtes Material, Karpathy).

> Bei allen Inhaltsänderungen: build.py editieren → `python scripts\build.py` → committen → `git push origin main`. Fertig.

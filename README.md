# LIAR – Pantomime La France

Statische Website für **www.pantomime-la-france.eu** — schnell, SEO- & KI-optimiert, DSGVO-Cookie-Consent, GA4 vorbereitet. Klon & Relaunch der alten WordPress-Seite `pantomime.liar-entertainer.com`.

## Struktur
```
index.html, figuren/, walk-act/, ueber-mich/, referenzen/,
kontakt/, impressum/, datenschutz/, 404.html   ← generierte Seiten
assets/style.css        Design-System (Tinte / Elfenbein / Gold)
assets/app.js           Cookie-Consent (Consent Mode v2) + GA4-Loader, Nav, Reveals, Web3Forms
assets/img/             optimierte WebP-Bilder + Logo + Favicon + OG-Bild
assets/img-src/         Original-Quelldateien (nicht deployt)
scripts/build.py        Seiten-Generator (DRY)  →  baut alle HTML + sitemap.xml + robots.txt
scripts/process_images.py  Bilder → WebP, Logo transparent
sitemap.xml, robots.txt, llms.txt, .htaccess
.github/workflows/deploy.yml   Auto-Deploy per SFTP → IONOS /PantomimeNeu
INHALTE-VERIFIZIERT.md  Quelle der Wahrheit (nur belegte Fakten)
MASTERPLAN_pantomime-liar.md
```

## Neu bauen
```powershell
python scripts/process_images.py   # nur nötig, wenn Bilder geändert wurden
python scripts/build.py            # baut alle Seiten + sitemap + robots
```

## Vor dem Go-Live einzutragen
1. **GA4-ID** — in `scripts/build.py` `GA4_ID = 'G-XXXXXXXXXX'` ersetzen, dann `build.py` neu laufen lassen.
2. **Web3Forms-Key** — in `scripts/build.py` `WEB3FORMS_KEY` setzen, dann `build.py` neu.
3. **GitHub-Secret** `SFTP_PASSWORD` im Repo hinterlegen (für Auto-Deploy).
4. **IONOS** — Domain `pantomime-la-france.eu` mit Ordner `/PantomimeNeu` verbinden + SSL.
5. **GSC** — Property verifizieren, `sitemap.xml` einreichen.
6. **301** — alte Subdomain `pantomime.liar-entertainer.com` → neue Domain weiterleiten.

> Solange `G-XXXXXXXXXX` steht, wird **kein** Tracking geladen.

## Deploy
Push auf `main` → GitHub Action spiegelt per SFTP nach IONOS `/PantomimeNeu/`.
Vom Upload ausgeschlossen: `scripts/`, `assets/img-src/`, `*.md`, `.github/`.

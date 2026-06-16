# PRODUCT.md — LIAR Pantomime

**Register:** brand (design IS the product — Künstler-Marketingseite)

## Was & für wen
Website von **LIAR** (Michael Prescler), Pantomime-Künstler aus Gladbeck/NRW. Ziel: Veranstalter, Firmen, Hochzeits- & Stadtfest-Planer überzeugen, LIAR als Pantomime / Walk Act / Figuren (Clown, Zauberer, Nussknacker, Weihnachtsmann, Crazy Kellner) zu buchen. Konversion = unverbindliche Anfrage (Web3Forms) + Anruf.

## Marken-Stimme (drei physische Worte)
**Theatralisch · französisch-charmant · poetisch-verspielt.** Belle-Époque-Théâtre-Plakat, nicht WordPress-Baukasten, nicht editorial-minimal.

## Designsystem (DESIGN.md-Kern)
- **Aesthetic lane (benannt):** Vintage französisches Théâtre-/Cirque-Plakat (Belle Époque). Karmin/Oxblood-Drench + warmes Playbill-Papier + Gold-Folie + S/W-Mime-Fotografie. Vorhang- & Spotlight-Motive.
- **Farbstrategie:** Committed/Full-Palette. Karminrot trägt große Flächen (Hero, Bänder), Papier nur als Lesegrund. Kein timides Creme-mit-1-Akzent.
  - `--crimson` Theater-Rot/Oxblood · `--gold` Gold-Folie · `--ink` warmes Schwarz · `--paper` warmes Bühnenpapier · `--rouge` Akzent-Rubin.
- **Typografie:** Display **Bodoni Moda** (Didone, Plakat-Drama) + Body **Hanken Grotesk** (humanistische Grotesk). Kontrast-Achse. KEINE Playfair/Cormorant, KEINE wiederholten Uppercase-Eyebrows.
- **Bild:** echte LIAR-Fotos, S/W- bzw. Duoton-Behandlung für Kohärenz; Schlüsselbilder (Apfel-Montage) in Farbe. Imagery-led.
- **Pflicht-Element Startseite:** 2×2-Apfel-Fotomontage (Pantomime-4/6/7/9) neben dem Original-Intro-Text „Künstler mit Takt und Humor".

## Inhalts-Regel (Karpathy)
Nur belegte Fakten aus `INHALTE-VERIFIZIERT.md` / pantomime.liar-entertainer.com. Originaltexte vollständig übernehmen, per SEO für **„Pantomime"** + **„Walk Act"** schärfen — nichts erfinden.

## Tech
Statisch, DRY-Generator `scripts/build.py`, Deploy via GitHub Action (lftp/SFTP) → IONOS `/PantomimeNeu`. Domain `www.pantomime-la-france.eu`. GA4 `G-PQ5XK66N5M`, Consent Mode v2, Web3Forms.

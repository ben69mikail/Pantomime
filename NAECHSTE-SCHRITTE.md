# Go-Live — geführte Schritte (Phase 3)

Die Seite ist gebaut, getestet und auf GitHub gepusht:
**https://github.com/ben69mikail/Pantomime** (Branch `main`).

Ich (Claude) habe alles vorbereitet. Die folgenden 6 Schritte brauchen **deinen Login** — danach ist die Seite live. Sag mir nach jedem Schritt Bescheid bzw. liefere die ID/den Key, den Rest baue ich ein und pushe neu.

---

## 1. GA4-Property anlegen → Mess-ID
1. https://analytics.google.com → **Verwaltung → Property erstellen** → Name „Pantomime La France".
2. Datenstrom **Web** → URL `https://www.pantomime-la-france.eu` → Stream anlegen.
3. Du bekommst eine **Mess-ID** `G-XXXXXXXXXX`.
→ **Schick mir die G-ID.** Ich trage sie in `scripts/build.py` ein, baue neu und pushe.

## 2. Web3Forms-Key
- Entweder den **Key der Hauptseite** wiederverwenden oder auf https://web3forms.com mit `info@liar-entertainer.com` einen **neuen Access-Key** holen.
→ **Schick mir den Key.** (Ich trage ihn ein + pushe.)

## 3. GitHub-Secret `SFTP_PASSWORD`
1. https://github.com/ben69mikail/Pantomime → **Settings → Secrets and variables → Actions → New repository secret**.
2. Name: `SFTP_PASSWORD` · Wert: dein IONOS-SFTP-Passwort (User `u62702423`).

## 4. GitHub Action aktivieren (Auto-Deploy)
Der PAT „waechter" hatte keinen `workflow`-Scope, daher liegt die Action-Datei als Referenz unter **`deploy/deploy.yml`**. Zwei Wege:
- **A (empfohlen):** PAT um Scope **`workflow`** erweitern → mir sagen → ich verschiebe die Datei nach `.github/workflows/` und pushe. Danach deployt jeder Push automatisch.
- **B:** Auf GitHub **Actions → New workflow → set up a workflow yourself** → Inhalt von `deploy/deploy.yml` einfügen → committen.

## 5. IONOS: Domain → Ordner verbinden + SSL
1. IONOS-Konto → **Domains** → `pantomime-la-france.eu`.
2. Domain dem Webspace-Ordner **`/PantomimeNeu`** zuordnen (Ziel/Webroot).
3. **SSL-Zertifikat** aktivieren (Let's Encrypt / IONOS SSL).
4. Erster Deploy läuft über die Action (Schritt 4) → Ordner füllt sich.

## 6. Google Search Console + 301
1. https://search.google.com/search-console → **Property hinzufügen** → Domain `pantomime-la-france.eu` (DNS-TXT verifizieren).
2. **Sitemap einreichen:** `sitemap.xml`.
3. **301-Redirect** der alten Subdomain `pantomime.liar-entertainer.com` → `https://www.pantomime-la-france.eu/` (per `.htaccess` im alten WordPress-Webspace; pfadgenau für die Figuren-URLs). Sag Bescheid — ich schreibe dir die `.htaccess`-Regeln für die alte Domain.

---

## Was danach automatisch läuft (Phase 4)
- Wöchentlicher GSC-Check (Impressionen/Klicks/Position für „Pantomime" + „Walk Act").
- Monatlicher Report + Content-Nachschärfung, interne Verlinkung liar-entertainer.com ↔ Pantomime ↔ zauberer-liar.de.
→ Richte ich als wiederkehrenden Scheduled-Task ein, sobald die Seite live & in der GSC ist.

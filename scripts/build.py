#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Statischer Seiten-Generator fuer LIAR Pantomime (www.pantomime-la-france.eu).
DRY: gemeinsamer Head/Header/Footer + pro Seite Inhalt/Meta/Schema.
Inhalte ausschliesslich aus INHALTE-VERIFIZIERT.md (umformuliert, nichts erfunden).
"""
import json, os, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://www.pantomime-la-france.eu"
GA4_ID = "G-PQ5XK66N5M"                 # GA4-Property "Pantomime La France"
WEB3FORMS_KEY = "e651ce96-e5a5-4088-9947-7c87d557a71e"    # Web3Forms Access-Key
TODAY = datetime.date.today().isoformat()

PHONE = "0172-1517578"
PHONE_INTL = "+491721517578"
EMAIL = "info@liar-entertainer.com"
CITY = "Gladbeck"
STREET = "Beethovenstr. 15"
ZIP = "45966"
CITIES = ["Gladbeck", "Essen", "Oberhausen", "Gelsenkirchen", "Dortmund",
          "Bochum", "Duisburg", "Mülheim an der Ruhr", "Bottrop", "Recklinghausen"]

NAV = [
    ("Figuren", "/figuren/"),
    ("Walk Act", "/walk-act/"),
    ("Über mich", "/ueber-mich/"),
    ("Referenzen", "/referenzen/"),
]

# ---------------------------------------------------------------- Schema-Bausteine
def org_schema():
    return {
        "@context": "https://schema.org",
        "@type": ["PerformingGroup", "LocalBusiness"],
        "@id": DOMAIN + "/#liar",
        "name": "LIAR – Pantomime",
        "alternateName": "Pantomime La France",
        "description": "Pantomime-Künstler aus NRW im brillanten, charmanten französischen Stil. "
                       "Buchbar als Pantomime, Walk Act und für Figuren wie Clown, Zauberer, "
                       "Nussknacker, Weihnachtsmann und Crazy Kellner.",
        "url": DOMAIN + "/",
        "telephone": PHONE_INTL,
        "email": EMAIL,
        "image": DOMAIN + "/assets/img/og-pantomime.jpg",
        "logo": DOMAIN + "/assets/img/logo.png",
        "founder": {"@type": "Person", "name": "Michael Prescler", "alternateName": "LIAR"},
        "address": {"@type": "PostalAddress", "streetAddress": STREET,
                    "postalCode": ZIP, "addressLocality": CITY,
                    "addressRegion": "NRW", "addressCountry": "DE"},
        "areaServed": [{"@type": "City", "name": c} for c in CITIES] +
                      [{"@type": "AdministrativeArea", "name": "Nordrhein-Westfalen"},
                       {"@type": "AdministrativeArea", "name": "Ruhrgebiet"}],
        "knowsAbout": ["Pantomime", "Walk Act", "Walking Act", "Living Statue", "Straßentheater",
                       "Clown", "Zauberer", "Nussknacker", "Weihnachtsmann"],
        "sameAs": [
            "https://www.liar-entertainer.com",
            "https://www.zauberer-liar.de",
            "https://www.facebook.com/clownzaubererliar",
            "https://www.instagram.com/clown_zauberer_liar",
        ],
    }

def breadcrumb(items):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n,
             "item": DOMAIN + u} for i, (n, u) in enumerate(items)
        ],
    }

def faq_schema(qa):
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa
        ],
    }

# ---------------------------------------------------------------- HTML-Gerüst
def head(title, desc, path, schema, og_img="/assets/img/og-pantomime.jpg"):
    url = DOMAIN + path
    blocks = "\n".join(
        '<script type="application/ld+json">%s</script>' %
        json.dumps(s, ensure_ascii=False) for s in schema)
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<meta name="author" content="Michael Prescler – LIAR" />
<link rel="canonical" href="{url}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:url" content="{url}" />
<meta property="og:locale" content="de_DE" />
<meta property="og:image" content="{DOMAIN}{og_img}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="theme-color" content="#0d0d0f" />
<link rel="icon" href="/assets/img/favicon.png" type="image/png" />
<link rel="apple-touch-icon" href="/assets/img/logo.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,800;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/assets/style.css" />
{blocks}
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('consent','default',{{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied'}});
  window.GA4_ID = '{GA4_ID}';
</script>
</head>
<body>
<div class="stage-glow" aria-hidden="true"></div>
"""

def header(active):
    links = ""
    for label, url in NAV:
        cls = ' aria-current="page"' if url == active else ""
        links += f'<a href="{url}"{cls}>{label}</a>'
    return f"""<header class="site-header">
  <a href="/" class="brand" aria-label="LIAR Pantomime – Startseite">
    <img src="/assets/img/logo.png" alt="LIAR Pantomime Logo" width="120" height="94" />
  </a>
  <nav class="site-nav" aria-label="Hauptnavigation">
    {links}
    <a href="/kontakt/" class="nav-cta">Anfragen</a>
  </nav>
  <button class="nav-toggle" aria-label="Menü öffnen" aria-expanded="false"><span></span><span></span><span></span></button>
</header>
"""

FOOTER = f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <img src="/assets/img/logo.png" alt="LIAR Pantomime" width="80" height="63" />
      <p>Pantomime &amp; Walk Act aus Gladbeck — brillant &amp; charmant im französischen Stil, buchbar in ganz NRW.</p>
    </div>
    <div class="footer-col">
      <h4>Figuren</h4>
      <a href="/figuren/der-pantomime-in-nrw/">Der Pantomime</a>
      <a href="/figuren/der-zauberer/">Der Zauberer</a>
      <a href="/figuren/der-clown/">Der Clown</a>
      <a href="/figuren/der-crazy-kellner/">Der Crazy Kellner</a>
      <a href="/figuren/der-nussknacker/">Der Nussknacker</a>
      <a href="/figuren/der-weihnachtsmann/">Der Weihnachtsmann</a>
    </div>
    <div class="footer-col">
      <h4>Kontakt</h4>
      <a href="tel:{PHONE_INTL}">{PHONE}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="/referenzen/">Referenzen</a>
      <a href="/kontakt/">Anfrage senden</a>
      <a href="https://www.liar-entertainer.com" rel="noopener">liar-entertainer.com</a>
      <a href="https://www.zauberer-liar.de" rel="noopener">zauberer-liar.de</a>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© <span id="year">{datetime.date.today().year}</span> Michael Prescler — LIAR Pantomime</span>
    <span><a href="/impressum/">Impressum</a> &nbsp;·&nbsp; <a href="/datenschutz/">Datenschutz</a></span>
  </div>
</footer>
"""

COOKIE = """<div class="cookie" id="cookie" role="dialog" aria-live="polite" aria-label="Cookie-Hinweis" hidden>
  <p>Diese Seite nutzt Cookies nur für anonyme Statistik (Google Analytics), um das Angebot zu verbessern. Das Tracking startet erst nach Ihrer Zustimmung. Mehr in der <a href="/datenschutz/">Datenschutzerklärung</a>.</p>
  <div class="cookie-actions">
    <button class="btn btn-ghost btn-sm" id="cookieDecline">Ablehnen</button>
    <button class="btn btn-primary btn-sm" id="cookieAccept">Zustimmen</button>
  </div>
</div>
<script src="/assets/app.js" defer></script>
</body>
</html>"""

def page(path, title, desc, body, schema, active="/", og_img="/assets/img/og-pantomime.jpg"):
    html = head(title, desc, path, schema, og_img) + header(active) + body + FOOTER + COOKIE
    out = ROOT / "index.html" if path == "/" else ROOT / path.strip("/") / "index.html"
    if path == "/404":
        out = ROOT / "404.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return path

# ---------------------------------------------------------------- Wiederverwendbare Blöcke
def cta_band(title="Bereit für einen Moment ohne Worte?",
             text="Erzählen Sie mir von Ihrem Anlass — ich entwickle das passende Programm. Anfragen am besten 2–4 Wochen vorab; kurzfristige Termine sind oft möglich."):
    return f"""<section class="cta-band">
  <div class="container">
    <span class="tag">Kontakt</span>
    <h2 class="reveal">{title}</h2>
    <p class="reveal">{text}</p>
    <div class="reveal" style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">
      <a href="/kontakt/" class="btn btn-primary">Anfrage senden</a>
      <a href="tel:{PHONE_INTL}" class="btn btn-ghost">{PHONE}</a>
    </div>
  </div>
</section>"""

WARUM_GRID = lambda items: '<div class="anlass-grid">' + "".join(
    f'<div class="anlass reveal"><h3>{h}</h3><p>{p}</p></div>' for h, p in items) + '</div>'

# ================================================================ FIGUREN-DATEN
FIGUREN = {
  "der-pantomime-in-nrw": {
    "name": "Der Pantomime", "menu": "Pantomime",
    "title": "Pantomime in NRW buchen – LIAR | Künstler ohne Worte",
    "desc": "Pantomime in NRW buchen: LIAR erzählt wortlos und ausdrucksstark Geschichten – als Hauptattraktion oder Walk Act für Messe, Stadtfest, Firmenfeier & Hochzeit.",
    "card": "cropped-pantomime-11.webp",
    "card_alt": "Pantomime LIAR mit Schiefertafel beim Stadtfest in Gladbeck",
    "hero_alt": "Pantomime in NRW – LIAR im klassischen Outfit",
    "intro": "Der Pantomime in NRW erzählt wortlos und ausdrucksstark traumhafte Geschichten.",
    "lead": "Pantomime ist eine wortlose Kunstform, bei der Geschichten, Emotionen und Szenen allein durch Körpersprache, Mimik und Gestik dargestellt werden. Genau das liebe ich.",
    "body": ["Als Solokünstler und Pantomime in NRW biete ich ein vielseitiges Showprogramm für die unterschiedlichsten Veranstaltungen. Ob im klassischen Outfit mit Regenschirm oder als eine meiner zahlreichen entwickelten Figuren — in meinem Repertoire findet sich garantiert das Passende. Und sonst machen wir es einfach passend für Ihre Veranstaltung.",
             "Als Pantomime wirke ich <strong>sympathisch</strong>, weil ich humorvoll, emotional, kreativ, universell, authentisch, einfühlsam, ausdrucksstark, verspielt, mitreißend und charmant bin. Ich nutze Körpersprache und Emotionen, Humor und Interaktion — und passe mich sehr gut und sehr schnell an."],
    "feat": ["Vielfältig einsetzbar: Messen, Autohäuser, Geschäftseröffnungen, Gastromeile, Galas, Stadtfeste und Feiern",
             "Keine Bühne, keine Ton- oder Lichttechnik nötig — flexibel an nahezu jedem Ort",
             "Kein Sprachproblem: ideal für internationale und multikulturelle Veranstaltungen",
             "Als Hauptattraktion oder als Walk Act buchbar"],
    "img2": "pantomime-12-scaled.webp", "img2_alt": "Pantomime LIAR vor Saalpublikum bei einer Feier",
    "warum_title": "Warum einen Pantomime in NRW buchen?",
    "warum": [("Universell verständlich", "Die Kunst basiert auf Körpersprache und funktioniert unabhängig von der Sprache des Publikums."),
              ("Platzsparend", "Anders als große Show-Acts brauche ich wenig Platz und kann auch zwischen den Gästen agieren."),
              ("Schnell einsatzbereit", "Keine aufwendige Bühnenvorbereitung, keine Requisiten — das spart Zeit und Organisation."),
              ("Für jedes Alter", "Die nonverbale Darbietung unterhält Kinder, Erwachsene und Senioren gleichermaßen.")],
    "faq": [("Was macht ein Pantomime?", "Ein Pantomime stellt Geschichten, Emotionen und Szenen ausschließlich durch Körpersprache, Mimik und Gestik dar — ganz ohne Worte."),
            ("Wo kann ich einen Pantomime buchen?", "LIAR tritt als Pantomime in ganz NRW auf, u. a. in Gladbeck, Essen, Oberhausen, Gelsenkirchen, Dortmund, Bochum und Duisburg."),
            ("Braucht ein Pantomime eine Bühne?", "Nein. Ein Pantomime benötigt in der Regel keine Bühne, keine Ton- oder Lichttechnik und kein spezielles Equipment.")],
  },
  "der-zauberer": {
    "name": "Der Zauberer", "menu": "Zauberer",
    "title": "Zauberer in NRW buchen – LIAR | Bühnen- & Close-up-Magie",
    "desc": "Zauberer in NRW buchen: LIAR verblüfft mit Bühnen- und Close-up-Zauberei, charmant und niveauvoll – für Hochzeit, Firmenfeier, Kindergeburtstag und Gala.",
    "card": "zauberer-2.webp", "card_alt": "Zauberer LIAR bei einem Auftritt",
    "hero_alt": "Zauberkünstler LIAR aus dem Ruhrgebiet",
    "intro": "Zauberer faszinieren mit Illusionen, die die Grenzen der Realität verschwimmen lassen.",
    "lead": "Als Zauberer bringe ich Ihren Verstand charmant durcheinander. Meine Tricks basieren auf Geschicklichkeit, Psychologie und manchmal geheimen Hilfsmitteln — genau das macht den Reiz aus.",
    "body": ["Als Solokünstler biete ich ein vielseitiges Showprogramm. Ob im klassischen Outfit mit Zaubertricks oder als eine meiner Figuren — im Repertoire findet sich garantiert das Passende. Das Publikum wird aktiv eingebunden, humorvolle Elemente kombiniert, und der französische Akzent wirkt dabei sehr charmant.",
             "<strong>Bühnen- und Close-up-Zauberei:</strong> Illusionen auf der Bühne vor vielen Zuschauern oder Magie hautnah mit Karten, Münzen und kleinen Alltagsgegenständen — oft direkt am Tisch der Gäste."],
    "feat": ["Magische Unterhaltung für jedes Alter — Hochzeit, Kindergeburtstag, Firmenfeier",
             "Interaktive, lustige Show: Gäste machen mit, lachen und sind Teil des Erlebnisses",
             "Keine aufwendige Technik nötig — drinnen wie draußen, Bühne oder mitten im Publikum",
             "Kombinierbar mit Ballonmodellage, Pantomime oder Glitzertattoos"],
    "img2": "zauberkuenstler-ruhrgebiet-1024x744.webp", "img2_alt": "Zauberkünstler LIAR aus dem Ruhrgebiet",
    "warum_title": "Warum einen Zauberer in NRW buchen?",
    "warum": [("Staunen für jedes Alter", "Magie begeistert Kinder, Erwachsene und Senioren gleichermaßen."),
              ("Unvergessliche Momente", "Staunen, Lachen, Verblüffung — magische Augenblicke bleiben in Erinnerung."),
              ("Flexibel & unkompliziert", "Mit Kartenspiel, Münzen oder Seil entsteht bereits eine beeindruckende Show."),
              ("Perfekte Kombination", "Ideal kombinierbar mit anderen Acts — besonders für Familienfeste.")],
    "faq": [("Bietet LIAR Close-up-Zauberei an?", "Ja. LIAR zaubert sowohl auf der Bühne vor vielen Zuschauern als auch hautnah mit Karten, Münzen und Alltagsgegenständen direkt am Tisch."),
            ("Für welche Anlässe eignet sich ein Zauberer?", "Für Hochzeiten, Kindergeburtstage, Firmenfeiern, Galas und viele weitere Veranstaltungen in NRW.")],
  },
  "der-clown": {
    "name": "Der Clown", "menu": "Clown",
    "title": "Clown in NRW buchen – LIAR | Kinderfest & Firmenfeier",
    "desc": "Clown in NRW buchen: LIAR bringt mit Mimik, Slapstick und Improvisation Menschen jeden Alters zum Lachen – ideal für Kinderfeste, Stadtfeste und Firmenfeiern.",
    "card": "geburtstag.webp", "card_alt": "Clown LIAR bei einem Kinderfest in NRW",
    "hero_alt": "Clown LIAR bringt Menschen zum Lachen",
    "intro": "Der Clown bringt Menschen jeden Alters zum Lachen, Staunen und Nachdenken.",
    "lead": "Als Clown baue ich mit meinem Spiel sofort eine Verbindung zum Publikum auf. Ob Kinder oder Erwachsene — ich spreche mit Mimik, Gestik und Körperkomik eine universelle Sprache, die jeder versteht.",
    "body": ["Als Solokünstler biete ich ein vielseitiges Showprogramm. Ob im klassischen Outfit mit Koffer oder als eine meiner Figuren — im Repertoire findet sich garantiert das Passende. Als Clown darf ich scheitern, und genau das macht die Figur so liebenswert: Meine Missgeschicke sind ein Spiegel des Lebens, und gerade daraus entsteht komischer Charme.",
             "Ich kann nicht nur lustig sein, sondern auch magisch, poetisch, nachdenklich oder melancholisch wirken. Mit wenig Worten erzähle ich Geschichten — Mimik, Körpersprache und Slapstick genügen, um das Publikum in eine andere Welt zu entführen."],
    "feat": ["Lachen garantiert — Späße, lustige Bewegungen, tollpatschige Aktionen",
             "Interaktive Unterhaltung: kleine Spiele, Zaubertricks, spontane Scherze",
             "Perfekt für Kinderfeste — oft mit Ballonmodellage, Glitzertattoos und kleinen Zaubertricks",
             "Kombinierbar mit Jonglieren, Pantomime, Zauberei und Luftballons"],
    "img2": "clown-zauberer.webp", "img2_alt": "Clown und Zauberer LIAR in einer Show",
    "warum_title": "Warum einen Clown in NRW buchen?",
    "warum": [("Freude & Unbeschwertheit", "In einer oft ernsten Welt bringe ich Momente der Leichtigkeit — mit Herz."),
              ("Niemand bleibt nur Zuschauer", "Ich binde das Publikum aktiv ein, durch Spiele, Tricks und spontane Scherze."),
              ("Highlight für Kinderfeste", "Kinder lieben Clowns — Witze, Slapstick und kleine Überraschungen."),
              ("Flexibel einsetzbar", "Auf großer Bühne oder mitten im Publikum, ganz ohne komplizierte Technik.")],
    "faq": [("Eignet sich der Clown für Kindergeburtstage?", "Ja, besonders. Für Kinderfeste bringe ich oft Ballonmodellage, Glitzertattoos und kleine Zaubertricks mit."),
            ("Ist der Clown auch für Erwachsene geeignet?", "Ja. Der Humor funktioniert für Kinder wie für Erwachsene mit Sinn für Komik.")],
  },
  "der-crazy-kellner": {
    "name": "Der Crazy Kellner", "menu": "Crazy Kellner",
    "title": "Crazy Kellner buchen in NRW – LIAR | Comedy-Walk-Act",
    "desc": "Crazy Kellner buchen: LIAR mischt sich als versteckter Comedian unter die Gäste und sorgt für Überraschungen am Tisch – ideal für Hochzeit, Gala & Firmenfeier.",
    "card": "crazy-kellner-scaled.webp", "card_alt": "Crazy Kellner LIAR buchen in NRW",
    "hero_alt": "Crazy Kellner LIAR im Ruhrgebiet",
    "intro": "Ein Crazy Kellner sorgt für unerwartete Überraschungen und interaktive Unterhaltung bei Events.",
    "lead": "Ich bin kein gewöhnlicher Kellner, sondern ein versteckter Comedian und Zauberer, der das Publikum mit skurrilen Aktionen und jede Menge Spaß verblüfft. Das liebe ich.",
    "body": ["Als Solokünstler und Pantomime in NRW biete ich ein vielseitiges Showprogramm. Ob im klassischen Outfit mit Moustache oder als eine meiner Figuren — im Repertoire findet sich garantiert das Passende. Ich bringe absichtlich die falschen Getränke, verwechsle charmant Bestellungen, stolpere, gieße fast daneben oder balanciere Teller auf wackelige Art.",
             "Plötzlich verschwinden Gabeln oder Blumen erscheinen aus der Serviette. So lockere ich als Crazy Kellner jedes Event auf — perfekt für Hochzeiten, Firmenfeiern und Geburtstage. Mit skurrilen Fragen und kuriosen Anekdoten beziehe ich die Gäste ein und sorge für spontane Lacher."],
    "feat": ["Einzigartige Überraschung statt gewöhnlichem Service",
             "Unterhaltung direkt am Tisch — kein Bühnenprogramm nötig",
             "Lockert auch offizielle, steife Veranstaltungen auf",
             "Kombinierbar mit Magie und Pantomime — perfekt für Fotos & Social Media"],
    "img2": "verrueckter-kellner.webp", "img2_alt": "Verrückter Kellner LIAR sorgt für Comedy am Tisch",
    "warum_title": "Warum einen Crazy Kellner buchen?",
    "warum": [("Sofortiger Gesprächsstoff", "Ein Kellner, der scheinbar alles falsch macht — charmant und witzig. Die Verwirrung sorgt für Lacher."),
              ("Hautnah am Gast", "Comedy, kleine Zaubertricks und skurrile Aktionen direkt am Tisch, jeder ist dabei."),
              ("Stimmungsmacher", "Gerade bei Galas, Hochzeiten und Firmenfeiern entsteht eine entspannte Atmosphäre."),
              ("Über den ganzen Abend", "Mal subtil, mal spektakulär — Unterhaltung, die nicht nach einer Bühnenshow endet.")],
    "faq": [("Was ist ein Crazy Kellner?", "Ein als Kellner getarnter Comedian und Zauberer, der sich unter die Gäste mischt und mit skurrilen Aktionen für Überraschungen sorgt."),
            ("Für welche Events passt der Crazy Kellner?", "Ideal für Hochzeiten, Firmenfeiern, Galas und Geburtstage — überall, wo Gäste an Tischen sitzen.")],
  },
  "der-nussknacker": {
    "name": "Der Nussknacker", "menu": "Nussknacker",
    "title": "Nussknacker buchen – LIAR | Walking-Act zur Weihnachtszeit",
    "desc": "Lebendiger Nussknacker buchen: LIAR bringt als Walking-Act märchenhafte Weihnachtsstimmung auf Weihnachtsmärkte, Firmenfeiern und in Einkaufszentren.",
    "card": "nussknacker-scaled.webp", "card_alt": "Lebendiger Nussknacker LIAR",
    "hero_alt": "Der Nussknacker als lebendiger Walking-Act",
    "intro": "Der Nussknacker ist eine besondere Mischung aus Märchen und Nostalgie.",
    "lead": "Das berühmte Ballett „Der Nussknacker“ von Tschaikowsky macht die Figur noch zauberhafter. Musik und eine Geschichte voller Fantasie verstärken den märchenhaften Charme — das liebe ich.",
    "body": ["Als Solokünstler und Pantomime in NRW biete ich ein vielseitiges Showprogramm. Ob im klassischen Outfit mit Bart oder als eine meiner Figuren — im Repertoire findet sich garantiert das Passende. Mit strengen Gesichtszügen, prächtiger Uniform und leuchtenden Farben erinnere ich an alte Zeiten und wecke nostalgische Gefühle.",
             "Die Figur ist vielfältig einsetzbar: Messen, Autohäuser, Geschäftseröffnungen, Weihnachtsmärkte, Stadtfeste und Feiern. Mit Körpersprache, Humor und Interaktion versprühe ich festliche Magie — und passe mich sehr schnell an."],
    "feat": ["Märchenhafte Weihnachtsstimmung — prächtige Uniform, königliche Haltung",
             "Blickfang & Foto-Highlight für wunderschöne Erinnerungsfotos",
             "Interaktiv: zaubern, kleine Kunststücke, Interaktion mit dem Publikum",
             "Als Walking-Act: Gäste begrüßen und kleine Geschenke verteilen"],
    "img2": "nussknacker-und-weihnachtsmann-scaled.webp", "img2_alt": "Nussknacker und Weihnachtsmann als festliche Figuren",
    "warum_title": "Warum einen Nussknacker buchen?",
    "warum": [("Weihnachtszauber live", "Ein lebendiger Nussknacker bringt das Flair des berühmten Balletts direkt zu den Gästen."),
              ("Foto-Highlight", "Auf Weihnachtsmärkten, Firmenfeiern oder privaten Festen zieht er alle Blicke auf sich."),
              ("Interaktiv für Kinder", "Kinder lieben es, mit einer lebendigen Märchenfigur zu sprechen und mitzumachen."),
              ("Ideal als Walking-Act", "Perfekt für Weihnachtsfeiern, Einkaufszentren, Märkte und Firmen-Events.")],
    "faq": [("Wann ist der Nussknacker buchbar?", "Besonders zur Advents- und Weihnachtszeit — für Weihnachtsmärkte, Einkaufszentren, Märkte und Firmen-Events."),
            ("Ist der Nussknacker ein Walking-Act?", "Ja. Als Walking-Act begrüße ich Gäste, sorge für festliche Stimmung und verteile kleine Geschenke.")],
  },
  "der-weihnachtsmann": {
    "name": "Der Weihnachtsmann", "menu": "Weihnachtsmann",
    "title": "Weihnachtsmann buchen in NRW – LIAR | Walk Act für Feiern",
    "desc": "Weihnachtsmann buchen in NRW: LIAR sorgt als lebendiger Weihnachtsmann und Walk Act für strahlende Kinderaugen – Firmenfeiern, Einkaufszentren, Märkte & Hotels.",
    "card": "img-20170624-wa0010-1024x768.webp", "card_alt": "LIAR als Weihnachtsmann",
    "hero_alt": "Weihnachtsmann LIAR als Walk Act",
    "intro": "Ein Weihnachtsmann sorgt besonders bei Kindern für Freude und Magie.",
    "lead": "Der freundliche, bärtige Mann im roten Mantel mit weißem Pelzbesatz bringt Geschenke und verzaubert das Weihnachtsfest — auch von Januar bis November. Das liebe ich.",
    "body": ["Als Solokünstler und Pantomime in NRW biete ich ein vielseitiges Showprogramm. Als Weihnachtsmann bin ich eine Mischung aus Nikolaus, Winterbräuchen und Märchenfiguren — und kenne manchmal die guten (und nicht so guten) Taten der Kinder.",
             "Einsetzbar in Einkaufszentren und auf Weihnachtsmärkten — perfekt für Fotos und zauberhafte Momente — sowie für Autohäuser, Geschäftseröffnungen, Galas, Stadtfeste und Feiern. Als Walk Act bin ich platzsparend, flexibel und für jede Altersklasse geeignet."],
    "feat": ["Magische Weihnachtsstimmung — festliche Atmosphäre statt bloßem Datum",
             "Strahlende Kinderaugen — goldenes Buch, Geschenkesack, warme Stimme",
             "Perfekte Fotomotive und wertvolle Erinnerungen",
             "Für Firmen & öffentliche Events — Firmenfeiern, Einkaufszentren, Märkte, Hotels"],
    "img2": "20190416-163129-scaled.webp", "img2_alt": "Weihnachtsmann LIAR in der Nähe",
    "warum_title": "Warum einen Weihnachtsmann buchen?",
    "warum": [("Echtes Erlebnis", "Ein lebendiger Weihnachtsmann macht aus Weihnachten ein Erlebnis, kein bloßes Datum."),
              ("Für Kinder ein Traum", "Mit goldenem Buch und Geschenkesack fühlen sich Kinder wie in einem Märchen."),
              ("Erinnerungen in Bildern", "Wunderschöne Fotos auf Märkten, in Einkaufszentren oder bei privaten Feiern."),
              ("Kombinierbar mit Comedy", "Interaktive Elemente — ideal für Kinderfeste und Firmenfeiern.")],
    "faq": [("Ist der Weihnachtsmann auch außerhalb der Weihnachtszeit buchbar?", "Ja, von Januar bis November — der Klassiker ist nahezu ganzjährig buchbar."),
            ("Wo tritt der Weihnachtsmann auf?", "In Einkaufszentren, auf Weihnachtsmärkten, bei Firmenfeiern, in Hotels und bei privaten Feiern in NRW.")],
  },
}

FIG_ORDER = ["der-pantomime-in-nrw", "der-zauberer", "der-clown",
             "der-crazy-kellner", "der-nussknacker", "der-weihnachtsmann"]

def img(name, alt, cls=""):
    return f'<img src="/assets/img/{name}" alt="{alt}" loading="lazy" decoding="async"{(" class=\"%s\""%cls) if cls else ""} />'

# ================================================================ SEITEN BAUEN
built = []

# ---- Startseite
home_body = f"""<main>
<section class="hero">
  <div class="hero-media">{img('cropped-pantomime-11.webp','Pantomime LIAR beim Stadtfest in Gladbeck').replace('loading="lazy"','fetchpriority="high"')}</div>
  <div class="hero-inner">
    <p class="hero-kicker reveal">Brillant &amp; charmant — aus Frankreich</p>
    <h1 class="reveal" style="--d:.1s">Eine Kunst, die <em>ohne Worte</em> begeistert.</h1>
    <p class="hero-sub reveal" style="--d:.25s">Pantomime &amp; Walk Act für Hochzeit, Firmenfeier, Messe und Stadtfest — in ganz Nordrhein-Westfalen. Gestik, Mimik und Kreativität schaffen Momente, die jede Sprache verstehen.</p>
    <div class="hero-actions reveal" style="--d:.4s">
      <a href="/kontakt/" class="btn btn-primary">Künstler anfragen</a>
      <a href="/figuren/" class="btn btn-ghost">Figuren entdecken</a>
    </div>
    <p class="hero-scroll reveal" style="--d:.6s">… leise weiter ↓</p>
  </div>
</section>

<section class="section container">
  <p class="lead reveal">Als Künstler und Pantomime erzähle ich Geschichten und erwecke Objekte zum Leben — staunend oder lachend ziehe ich das Publikum in den Bann. <strong>Ganz ohne Worte</strong>, universell verständlich, über Sprachen und Kulturen hinweg.</p>
</section>

<section class="section container" id="figuren">
  <div class="section-head reveal">
    <span class="tag">Das Repertoire</span>
    <h2>Sechs Figuren, ein Künstler</h2>
    <p>Klassisch oder modern — für jeden Anlass die passende Erscheinung. Seit 2021 erwecke ich verschiedene Figuren zum Leben.</p>
  </div>
  <div class="fig-grid">
""" + "".join(
    f"""    <a class="fig-card reveal" href="/figuren/{slug}/">
      <div class="ph">{img(FIGUREN[slug]['card'], FIGUREN[slug]['card_alt'])}</div>
      <div class="body"><h3>{FIGUREN[slug]['menu']}<span class="dot">.</span></h3>
      <p>{FIGUREN[slug]['intro']}</p><span class="more">Mehr erfahren</span></div>
    </a>
""" for slug in FIG_ORDER) + """  </div>
</section>

<section class="section container">
  <div class="split">
    <div class="reveal">
      <span class="tag">Was Pantomime kann</span>
      <h2>Klassisch und&nbsp;/&nbsp;oder modern?</h2>
      <p class="prose" style="margin-top:1.2rem">Pantomime passt sich Ihrem Publikum an: mal poetisch und leise, mal frech und interaktiv. Ich entwickle maßgeschneiderte Programme und Charaktere — vom intimen Empfang bis zum großen Stadtfest.</p>
      <ul class="feature-list">
        <li>Objekte zum Leben erwecken</li>
        <li>Publikum interaktiv einbeziehen</li>
        <li>Stimmungen ohne ein einziges Wort transportieren</li>
        <li>Für jedes Alter — sprach- und kulturübergreifend</li>
      </ul>
    </div>
    <div class="split-media reveal">""" + img('pantomime-12-scaled.webp','Pantomime LIAR vor Saalpublikum') + """</div>
  </div>
  <div class="quote reveal"><blockquote>„Meine Kunst braucht keine Worte — und wird überall verstanden.“</blockquote><cite>— LIAR</cite></div>
</section>

<section class="section container" id="anlaesse">
  <div class="section-head reveal"><span class="tag">Für Ihren Anlass</span><h2>Wo LIAR begeistert</h2></div>
  """ + WARUM_GRID([
      ("Hochzeit", "Stilvolle Überraschung für den schönsten Tag."),
      ("Firmenfeier", "Ein Highlight, das im Gedächtnis bleibt."),
      ("Messe &amp; Event", "Walk Act, der Aufmerksamkeit an den Stand zieht."),
      ("Stadtfest", "Straßentheater für Publikum jeden Alters."),
  ]) + f"""
  <div class="chips reveal" style="margin-top:2rem">{"".join(f'<span class="chip">{c}</span>' for c in CITIES)}</div>
</section>
</main>
""" + cta_band()

built.append(page("/", "Pantomime buchen in NRW – LIAR | Künstler ohne Worte",
     "Pantomime &amp; Walk Act in NRW buchen: LIAR – brillant &amp; charmant im französischen Stil. Stilvolle Pantomime für Hochzeit, Firmenfeier, Messe &amp; Stadtfest. Eine Kunst, die ohne Worte begeistert.",
     home_body, [org_schema(), breadcrumb([("Start", "/")]),
                 faq_schema([("Kann man LIAR als Pantomime in NRW buchen?", "Ja. LIAR ist Pantomime-Künstler aus Gladbeck und in ganz NRW buchbar — als Pantomime, Walk Act und in verschiedenen Figuren."),
                             ("Für welche Anlässe ist Pantomime geeignet?", "Für Hochzeiten, Firmenfeiern, Messen, Stadtfeste und viele weitere Veranstaltungen — für Publikum jeden Alters.")])],
     active="/"))

# ---- Figuren-Übersicht
fig_cards = "".join(
    f"""    <a class="fig-card reveal" href="/figuren/{slug}/">
      <div class="ph">{img(FIGUREN[slug]['card'], FIGUREN[slug]['card_alt'])}</div>
      <div class="body"><h3>{FIGUREN[slug]['name']}<span class="dot">.</span></h3>
      <p>{FIGUREN[slug]['intro']}</p><span class="more">Mehr erfahren</span></div>
    </a>
""" for slug in FIG_ORDER)
figuren_body = f"""<main>
<section class="subhero">
  <div class="container">
    <p class="crumb"><a href="/">Start</a> → Figuren</p>
    <span class="tag">Künstler-Charaktere</span>
    <h1>Klassisch und/oder modern?</h1>
    <p class="intro">Sechs Figuren, ein Künstler — vom stillen Pantomime bis zum lebendigen Nussknacker. Für jeden Anlass die passende Erscheinung.</p>
  </div>
</section>
<section class="section container">
  <div class="fig-grid">
{fig_cards}  </div>
</section>
</main>
""" + cta_band()
built.append(page("/figuren/", "Figuren & Charaktere – LIAR Pantomime | Pantomime, Clown, Zauberer",
     "Die Figuren von LIAR: Pantomime, Zauberer, Clown, Crazy Kellner, Nussknacker und Weihnachtsmann — klassisch oder modern, für jeden Anlass in NRW buchbar.",
     figuren_body, [breadcrumb([("Start", "/"), ("Figuren", "/figuren/")])], active="/figuren/"))

# ---- Figuren-Detailseiten
for slug in FIG_ORDER:
    f = FIGUREN[slug]
    body = f"""<main>
<section class="subhero">
  <div class="container">
    <p class="crumb"><a href="/">Start</a> → <a href="/figuren/">Figuren</a> → {f['menu']}</p>
    <span class="tag">Figur</span>
    <h1>{f['name']}</h1>
    <p class="intro">{f['intro']}</p>
  </div>
</section>

<section class="section container">
  <div class="split">
    <div class="reveal">
      <p class="lead">{f['lead']}</p>
      <div class="prose" style="margin-top:1.6rem">{"".join(f"<p>{p}</p>" for p in f['body'])}</div>
      <ul class="feature-list">{"".join(f"<li>{x}</li>" for x in f['feat'])}</ul>
    </div>
    <div class="split-media reveal">{img(f['card'], f['hero_alt'])}</div>
  </div>
</section>

<section class="section container">
  <div class="section-head reveal"><span class="tag">Gute Gründe</span><h2>{f['warum_title']}</h2></div>
  {WARUM_GRID(f['warum'])}
  <div class="split rev" style="margin-top:3rem">
    <div class="split-media wide reveal">{img(f['img2'], f['img2_alt'])}</div>
    <div class="reveal">
      <h2>Buchbar in ganz NRW</h2>
      <p class="prose" style="margin-top:1rem">{f['name']} ist u. a. in {", ".join(CITIES[:7])} und im gesamten Ruhrgebiet buchbar. Erzählen Sie mir von Ihrem Anlass — ich entwickle das passende Programm.</p>
      <a href="/kontakt/" class="btn btn-primary" style="margin-top:1.5rem">Jetzt anfragen</a>
    </div>
  </div>
</section>
</main>
""" + cta_band()
    schema = [breadcrumb([("Start", "/"), ("Figuren", "/figuren/"), (f['menu'], f"/figuren/{slug}/")]),
              faq_schema(f['faq']),
              {"@context": "https://schema.org", "@type": "Service",
               "serviceType": f['name'], "provider": {"@id": DOMAIN + "/#liar"},
               "areaServed": "Nordrhein-Westfalen", "description": f['desc']}]
    built.append(page(f"/figuren/{slug}/", f['title'], f['desc'], body, schema,
                      active="/figuren/", og_img="/assets/img/" + ("og-pantomime.jpg")))

# ---- Walk Act
walk_body = f"""<main>
<section class="subhero">
  <div class="container">
    <p class="crumb"><a href="/">Start</a> → Walk Act</p>
    <span class="tag">Mobile Unterhaltung</span>
    <h1>Walk Act in NRW buchen</h1>
    <p class="intro">Unterhaltung, die zu den Gästen kommt — als Pantomime, Nussknacker oder Weihnachtsmann mitten im Publikum.</p>
  </div>
</section>

<section class="section container">
  <div class="split">
    <div class="reveal">
      <p class="lead">Als Walk Act bin ich dort, wo die Gäste sind: zwischen den Tischen, auf der Gastromeile, am Messestand oder über das Festgelände.</p>
      <div class="prose" style="margin-top:1.6rem">
        <p>Die Kunst der Pantomime basiert auf Körpersprache — sie funktioniert unabhängig von der Sprache des Publikums. Als Walk Act brauche ich keine Bühne und keine Technik: Ich bin platzsparend, flexibel, anpassungsfähig und sofort einsatzbereit. So begrüße ich Gäste, sorge für festliche Stimmung und schaffe Momente, die in Erinnerung bleiben.</p>
        <p>Ob als <strong>Pantomime</strong> als Hauptattraktion oder mobiler Act, als <strong>Nussknacker</strong>, der Gäste begrüßt und kleine Geschenke verteilt, oder als <strong>Weihnachtsmann</strong> auf dem Markt — den Walk Act gestalte ich passend zu Ihrem Anlass.</p>
      </div>
      <ul class="feature-list">
        <li>Keine Bühne, keine Ton- oder Lichttechnik nötig</li>
        <li>Platzsparend — agiert auch in kleinen Räumen und zwischen den Gästen</li>
        <li>Kein Sprachproblem — ideal für internationale Veranstaltungen</li>
        <li>Für jede Altersgruppe — Kinder, Erwachsene, Senioren</li>
      </ul>
    </div>
    <div class="split-media reveal">{img('walk-act-fest-essen.webp','LIAR als Walk Act im Regen bei einem Stadtfest')}</div>
  </div>
</section>

<section class="section container">
  <div class="section-head reveal"><span class="tag">Einsatzorte</span><h2>Wo ein Walk Act glänzt</h2></div>
  {WARUM_GRID([
      ("Messe & Stand", "Zieht Aufmerksamkeit zum Messestand und bleibt im Gedächtnis."),
      ("Stadtfest & Straße", "Straßentheater, das mitten im Publikum entsteht."),
      ("Firmenfeier & Gala", "Lockert die Stimmung — mal subtil, mal spektakulär."),
      ("Einkaufszentrum & Markt", "Festliche Walking-Acts wie Nussknacker und Weihnachtsmann."),
  ])}
</section>
</main>
""" + cta_band("Walk Act für Ihr Event?", "Sagen Sie mir Datum, Ort und Art der Veranstaltung — ich entwickle den passenden Walk Act.")
built.append(page("/walk-act/", "Walk Act in NRW buchen – LIAR | Pantomime & mobile Unterhaltung",
     "Walk Act in NRW buchen: LIAR kommt als Pantomime, Nussknacker oder Weihnachtsmann mitten ins Publikum — ohne Bühne, ohne Technik, für Messe, Stadtfest & Firmenfeier.",
     walk_body, [breadcrumb([("Start", "/"), ("Walk Act", "/walk-act/")]),
                 faq_schema([("Was ist ein Walk Act?", "Ein Walk Act ist mobile Unterhaltung, die sich unter die Gäste mischt — ohne feste Bühne. LIAR tritt als Pantomime, Nussknacker oder Weihnachtsmann mitten im Publikum auf."),
                             ("Braucht ein Walk Act Technik?", "Nein. Als Walk Act benötige ich keine Bühne und keine Ton- oder Lichttechnik und bin sofort einsatzbereit.")])],
     active="/walk-act/"))

# ---- Über mich
ueber_body = f"""<main>
<section class="subhero">
  <div class="container">
    <p class="crumb"><a href="/">Start</a> → Über mich</p>
    <span class="tag">Über mich</span>
    <h1>Künstler mit Takt und Humor</h1>
    <p class="intro">Mathe – Hotellerie – Skifahren – Kunst: ein ungewöhnlicher Weg zur Pantomime.</p>
  </div>
</section>

<section class="section container">
  <div class="split">
    <div class="reveal">
      <p class="lead">Jahrgang 1976, geboren in Frankreich — seit 2004 in Deutschland zu Hause und seit 2009 hauptberuflich Künstler.</p>
      <div class="prose" style="margin-top:1.6rem">
        <p>Mit dem Abitur in der Tasche habe ich Naturwissenschaft (Schwerpunkt Mathe) und Erziehungswissenschaft studiert. Dazu kam eine komplette Ausbildung zum Animateur — mit Schauspiel, Tanz, Zauberei, Ballonmodellage, Schminken, Stand-up, Comedy, Sportaktivitäten sowie PR &amp; Management — und drei Jahre Kinderanimation in Frankreich.</p>
        <p>Mit zwei Koffern flog ich los: vier Jahre künstlerische Unterhaltung in Europa (Spanien, Griechenland u. a.), gefolgt von fünf Jahren als Abteilungsleiter (Floor Manager) im Alpincenter Bottrop, der längsten Skihalle der Welt — mit Verantwortung auch für PR, Personal, Vertrieb und Promotion.</p>
        <p>Seit 2021 habe ich mein Programm um <strong>Pantomime</strong> erweitert und erwecke verschiedene Figuren zum Leben. Mit wachsender Kreativität gestalte ich individuelle Darbietungen — humorvoll, poetisch oder interaktiv, immer passend zum Publikum.</p>
      </div>
      <a href="/referenzen/" class="btn btn-ghost" style="margin-top:1.5rem">Referenzen ansehen</a>
    </div>
    <div class="split-media reveal">{img('pantomime-12-scaled.webp','Der Künstler LIAR als Pantomime')}</div>
  </div>
</section>
</main>
""" + cta_band()
built.append(page("/ueber-mich/", "Über mich – LIAR | Künstler & Pantomime aus Gladbeck",
     "Über LIAR (Michael Prescler): Jahrgang 1976, geboren in Frankreich, seit 2009 hauptberuflich Künstler in NRW und seit 2021 Pantomime. Vom Mathe-Studium zur Bühne.",
     ueber_body, [breadcrumb([("Start", "/"), ("Über mich", "/ueber-mich/")]),
                  {"@context": "https://schema.org", "@type": "Person", "name": "Michael Prescler",
                   "alternateName": "LIAR", "birthDate": "1976", "nationality": "Französisch",
                   "jobTitle": "Pantomime-Künstler", "worksFor": {"@id": DOMAIN + "/#liar"},
                   "address": {"@type": "PostalAddress", "addressLocality": CITY, "addressRegion": "NRW", "addressCountry": "DE"}}],
     active="/ueber-mich/"))

# ---- Referenzen
REFS = ["OPEL", "IKEA", "Metro", "Champions League UEFA", "Messe Essen", "Extraschicht",
        "AWO Essen", "IHK Dortmund", "Schalke 04", "Sparkasse Mülheim a. d. Ruhr",
        "Sparkasse Bottrop", "Sparkasse Gladbeck", "Sparkasse Essen", "AWO Gelsenkirchen",
        "Stadt Mülheim", "Stadt Essen", "Stadt Gelsenkirchen", "Stadt Dortmund", "VKJ Essen",
        "Kulturamt Gladbeck", "Techniker Krankenkasse", "Tuffi", "ADAC",
        "Van der Valk Hotelkette", "Alpincenter Bottrop", "VfL Bochum",
        "Kinderschutzbund Bottrop", "Kinderschutzbund Essen", "St-Gobain Essen",
        "Kinderwelt Recklinghausen", "Feldschlösschen Essen"]
GALLERY = [("cropped-pantomime-11.webp", "Pantomime LIAR beim Stadtfest in Gladbeck"),
           ("crazy-kellner-scaled.webp", "Crazy Kellner LIAR in NRW"),
           ("zauberer-2.webp", "Zauberer LIAR bei einem Auftritt"),
           ("nussknacker-scaled.webp", "Lebendiger Nussknacker LIAR"),
           ("geburtstag.webp", "Clown LIAR bei einem Kinderfest"),
           ("walk-act-fest-essen.webp", "Walk Act LIAR im Regen beim Fest"),
           ("pantomime-12-scaled.webp", "Pantomime LIAR vor Saalpublikum"),
           ("img-20170624-wa0010-1024x768.webp", "LIAR als Weihnachtsmann"),
           ("verrueckter-kellner.webp", "Verrückter Kellner LIAR am Tisch")]
ref_body = f"""<main>
<section class="subhero">
  <div class="container">
    <p class="crumb"><a href="/">Start</a> → Referenzen</p>
    <span class="tag">Vertrauen &amp; Erfahrung</span>
    <h1>Referenzen</h1>
    <p class="intro">Über viele Jahre für Marken, Städte und Institutionen im Ruhrgebiet und darüber hinaus im Einsatz.</p>
  </div>
</section>
<section class="section container">
  <div class="section-head reveal"><span class="tag">Eine Auswahl</span><h2>Für diese Auftraggeber war LIAR im Einsatz</h2></div>
  <div class="ref-grid">{"".join(f"<span class='reveal'>{r}</span>" for r in REFS)}</div>
  <p class="form-note reveal" style="margin-top:1rem">… und viele andere mehr.</p>
</section>
<section class="section container">
  <div class="section-head reveal"><span class="tag">Eindrücke</span><h2>Momente aus der Praxis</h2></div>
  <div class="gallery">{"".join(img(n, a) for n, a in GALLERY)}</div>
</section>
</main>
""" + cta_band()
built.append(page("/referenzen/", "Referenzen – LIAR Pantomime | OPEL, IKEA, Messe Essen & mehr",
     "Referenzen von LIAR: u. a. OPEL, IKEA, Metro, Champions League UEFA, Messe Essen, Schalke 04, Sparkassen und Städte im Ruhrgebiet. Erfahrung, die für sich spricht.",
     ref_body, [breadcrumb([("Start", "/"), ("Referenzen", "/referenzen/")])], active="/referenzen/"))

# ---- Kontakt
kontakt_body = f"""<main>
<section class="subhero">
  <div class="container">
    <p class="crumb"><a href="/">Start</a> → Kontakt</p>
    <span class="tag">Noch Fragen?</span>
    <h1>Fragen Sie einfach an</h1>
    <p class="intro">Ganz unverbindlich. Je mehr Informationen ich erhalte, desto besser kann ich Ihr Angebot machen.</p>
  </div>
</section>
<section class="section container">
  <div class="contact-grid">
    <div class="contact-info reveal">
      <p>Sie suchen ein Highlight — Pantomime, Walk Act, Crazy Kellner — für Ihr Event oder haben Interesse an einer Zaubershow? Schicken Sie mir gerne eine unverbindliche Anfrage. Hilfreich sind <strong>Datum, Ort, Art der Veranstaltung</strong> und das gewünschte Programm.</p>
      <p style="margin-top:1.5rem"><span class="big">{PHONE}</span><br/>Telefon &amp; WhatsApp</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>{STREET}, {ZIP} {CITY}</p>
      <p style="margin-top:1rem"><a href="https://www.facebook.com/clownzaubererliar" rel="noopener">Facebook</a> · <a href="https://www.instagram.com/clown_zauberer_liar" rel="noopener">Instagram</a></p>
    </div>
    <div class="reveal">
      <form id="contactForm">
        <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}" />
        <input type="hidden" name="subject" value="Neue Anfrage über pantomime-la-france.eu" />
        <input type="hidden" name="from_name" value="Pantomime La France" />
        <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" />
        <div class="row two">
          <div><label for="name">Name</label><input id="name" type="text" name="name" required /></div>
          <div><label for="email">E-Mail</label><input id="email" type="email" name="email" required /></div>
        </div>
        <div class="row two">
          <div><label for="datum">Datum</label><input id="datum" type="text" name="Datum" placeholder="z. B. 12.09.2026" /></div>
          <div><label for="anlass">Anlass</label>
            <select id="anlass" name="Anlass">
              <option>Hochzeit</option><option>Firmenfeier</option><option>Messe / Event</option>
              <option>Stadtfest</option><option>Kindergeburtstag</option><option>Weihnachtsfeier</option><option>Sonstiges</option>
            </select></div>
        </div>
        <div class="row">
          <div><label for="ort">Ort der Veranstaltung</label><input id="ort" type="text" name="Ort" placeholder="z. B. Essen" /></div>
        </div>
        <div class="row">
          <div><label for="nachricht">Ihre Nachricht</label><textarea id="nachricht" name="Nachricht" required placeholder="Erzählen Sie mir von Ihrem Anlass …"></textarea></div>
        </div>
        <button type="submit" class="btn btn-primary">Anfrage senden</button>
        <p class="form-status" role="status"></p>
        <p class="form-note">Mit dem Absenden stimmen Sie der Verarbeitung Ihrer Angaben zur Bearbeitung der Anfrage zu (siehe <a href="/datenschutz/">Datenschutz</a>).</p>
      </form>
    </div>
  </div>
</section>
</main>"""
built.append(page("/kontakt/", "Kontakt – LIAR Pantomime buchen | Unverbindliche Anfrage",
     "Pantomime, Walk Act oder Zaubershow in NRW buchen: Schicken Sie LIAR eine unverbindliche Anfrage. Telefon & WhatsApp 0172-1517578, info@liar-entertainer.com.",
     kontakt_body, [breadcrumb([("Start", "/"), ("Kontakt", "/kontakt/")]),
                    {"@context": "https://schema.org", "@type": "ContactPage",
                     "name": "Kontakt LIAR Pantomime", "url": DOMAIN + "/kontakt/"}],
     active="/kontakt/"))

# ---- Impressum
impressum_body = f"""<main>
<section class="subhero"><div class="container">
  <p class="crumb"><a href="/">Start</a> → Impressum</p><span class="tag">Rechtliches</span><h1>Impressum</h1>
</div></section>
<section class="section container"><div class="prose reveal" style="max-width:62ch">
  <h3>Betreiber der Website</h3>
  <p>Michael Prescler<br/>{STREET}<br/>{ZIP} {CITY}</p>
  <h3>Kontakt</h3>
  <p>Telefon: +49 (0) 172 15 17 578<br/>E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <h3>Steuerbehörde</h3>
  <p>Finanzamt Marl</p>
  <h3>Inhaltlich Verantwortlicher gemäß § 55 Abs. 2 RStV</h3>
  <p>Michael Prescler, Anschrift wie oben</p>
  <h3>Urheberrecht</h3>
  <p>Alle verwendeten Texte, Bilder und Grafiken sind urheberrechtlich geschützt.</p>
  <h3>Haftungsausschluss</h3>
  <p>Der Betreiber übernimmt keine Haftung für externe Links oder Inhalte. Trotz sorgfältiger Pflege können Fehler auftreten; der Betreiber übernimmt keine Haftung für die Aktualität, die inhaltliche Richtigkeit sowie für die Vollständigkeit der bereitgestellten Informationen.</p>
  <h3>Hinweis zu Abmahnungen</h3>
  <p>Bei Domain- oder Inhaltsstreitigkeiten wird empfohlen, zunächst Kontakt mit dem Betreiber aufzunehmen, bevor rechtliche Schritte eingeleitet werden.</p>
  <p style="margin-top:2rem;color:var(--muted)">© Michael Prescler – 2020</p>
</div></section>
</main>"""
built.append(page("/impressum/", "Impressum – LIAR Pantomime",
     "Impressum von LIAR Pantomime — Michael Prescler, Beethovenstr. 15, 45966 Gladbeck.",
     impressum_body, [breadcrumb([("Start", "/"), ("Impressum", "/impressum/")])], active="/"))

# ---- Datenschutz
datenschutz_body = f"""<main>
<section class="subhero"><div class="container">
  <p class="crumb"><a href="/">Start</a> → Datenschutz</p><span class="tag">Rechtliches</span><h1>Datenschutzerklärung</h1>
</div></section>
<section class="section container"><div class="prose reveal" style="max-width:62ch">
  <h3>1. Verantwortlicher</h3>
  <p>Michael Prescler, {STREET}, {ZIP} {CITY}, Telefon +49 (0) 172 15 17 578, E-Mail <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

  <h3>2. Verarbeitete Daten &amp; Zwecke</h3>
  <p>Beim Besuch dieser Website werden Bestands-, Kontakt-, Inhalts-, Nutzungs- sowie Meta-/Kommunikationsdaten (z. B. IP-Adresse, Geräteinformationen, aufgerufene Seiten, Zugriffszeiten) verarbeitet — zur Bereitstellung und Funktion der Website, zur Beantwortung von Anfragen, zur Sicherheit sowie zur anonymen Reichweitenmessung.</p>

  <h3>3. Rechtsgrundlagen</h3>
  <p>Die Verarbeitung erfolgt auf Grundlage von Art. 6 und Art. 7 DSGVO (Einwilligung, Vertragserfüllung, rechtliche Verpflichtungen und berechtigte Interessen).</p>

  <h3>4. Hosting (IONOS)</h3>
  <p>Diese Website wird bei der IONOS SE, Elgendorfer Str. 57, 56410 Montabaur, gehostet. IONOS verarbeitet dabei Server-Logfiles (u. a. IP-Adresse, Datum/Uhrzeit, abgerufene Datei) zur Bereitstellung und Sicherheit des Angebots (Art. 6 Abs. 1 lit. f DSGVO). Es besteht ein Auftragsverarbeitungsvertrag.</p>

  <h3>5. Kontaktformular (Web3Forms)</h3>
  <p>Für das Kontaktformular nutzen wir den Dienst Web3Forms. Ihre eingegebenen Daten (Name, E-Mail, Angaben zur Veranstaltung, Nachricht) werden zur Zustellung Ihrer Anfrage per E-Mail verarbeitet und nicht für andere Zwecke verwendet. Rechtsgrundlage ist Ihre Einwilligung bzw. die Bearbeitung vorvertraglicher Maßnahmen (Art. 6 Abs. 1 lit. a und b DSGVO). Alternativ erreichen Sie uns per Telefon oder E-Mail.</p>

  <h3>6. Cookies &amp; Einwilligung</h3>
  <p>Technisch notwendige Speicherung erfolgt ohne Einwilligung. Statistik-/Analyse-Cookies (Google Analytics) werden erst nach Ihrer aktiven Zustimmung über den Cookie-Hinweis gesetzt (Consent Mode v2). Ihre Auswahl wird lokal in Ihrem Browser gespeichert; standardmäßig ist das Tracking deaktiviert. Sie können Ihre Entscheidung jederzeit über die Browser-Einstellungen widerrufen.</p>

  <h3>7. Google Analytics 4</h3>
  <p>Nach Einwilligung nutzen wir Google Analytics 4 (Google Ireland Ltd.) zur anonymen Reichweitenmessung. Die IP-Adresse wird anonymisiert (<code>anonymize_ip</code>); Werbe- und Personalisierungsfunktionen sind deaktiviert. Ohne Ihre Zustimmung wird Google Analytics nicht geladen.</p>

  <h3>8. Google Fonts</h3>
  <p>Diese Website lädt Schriftarten von Google Fonts. Dabei wird eine Verbindung zu Google-Servern aufgebaut und Ihre IP-Adresse übermittelt. Rechtsgrundlage ist unser berechtigtes Interesse an einer einheitlichen Darstellung (Art. 6 Abs. 1 lit. f DSGVO).</p>

  <h3>9. Ihre Rechte</h3>
  <p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit sowie ein Widerspruchsrecht. Zudem besteht ein Beschwerderecht bei einer Aufsichtsbehörde.</p>

  <p style="margin-top:2rem;color:var(--muted)">Stand: {TODAY}</p>
</div></section>
</main>"""
built.append(page("/datenschutz/", "Datenschutzerklärung – LIAR Pantomime",
     "Datenschutzerklärung von LIAR Pantomime: Hosting (IONOS), Kontaktformular (Web3Forms), Cookie-Einwilligung, Google Analytics 4 (Consent Mode v2) und Ihre Rechte.",
     datenschutz_body, [breadcrumb([("Start", "/"), ("Datenschutz", "/datenschutz/")])], active="/"))

# ---- 404
nf_body = """<main>
<section class="subhero" style="min-height:60vh;display:flex;align-items:center"><div class="container">
  <span class="tag">Fehler 404</span>
  <h1>Diese Seite gibt es nicht — oder sie schweigt.</h1>
  <p class="intro">Wie ein Pantomime: keine Worte. Kehren Sie zurück zur Startseite.</p>
  <a href="/" class="btn btn-primary" style="margin-top:2rem">Zur Startseite</a>
</div></section>
</main>"""
built.append(page("/404", "Seite nicht gefunden – LIAR Pantomime",
     "Diese Seite wurde nicht gefunden.", nf_body, [], active="/"))

print(f"{len(built)} Seiten gebaut:")
for p in built:
    print("  ", "index.html" if p == "/" else ("404.html" if p == "/404" else p.strip('/') + "/index.html"))

# ---------------------------------------------------------------- sitemap + robots
PAGES_FOR_SITEMAP = ["/", "/figuren/"] + [f"/figuren/{s}/" for s in FIG_ORDER] + \
    ["/walk-act/", "/ueber-mich/", "/referenzen/", "/kontakt/", "/impressum/", "/datenschutz/"]
urls = "\n".join(
    f"  <url><loc>{DOMAIN}{p}</loc><lastmod>{TODAY}</lastmod>"
    f"<changefreq>{'weekly' if p=='/' else 'monthly'}</changefreq>"
    f"<priority>{'1.0' if p=='/' else ('0.8' if p.startswith('/figuren/') or p=='/walk-act/' else '0.6')}</priority></url>"
    for p in PAGES_FOR_SITEMAP)
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n",
    encoding="utf-8")
(ROOT / "robots.txt").write_text(
    "User-agent: *\nAllow: /\n\n"
    "# KI-Crawler ausdrücklich erlaubt\n"
    "User-agent: GPTBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\n"
    "User-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\n"
    f"Sitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
print("sitemap.xml + robots.txt geschrieben.")

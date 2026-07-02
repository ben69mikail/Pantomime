/* LIAR Pantomime — App-Logik
   Cookie-Consent (DSGVO) + GA4 Consent-Mode v2, Nav, Reveals, Header, Formular */
(function () {
  "use strict";

  /* ---------- Header: solid beim Scrollen ---------- */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (header) header.classList.toggle("scrolled", window.scrollY > 40);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Mobile-Nav ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Jahr im Footer ---------- */
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  /* ---------- GA4 laden (erst nach Einwilligung) ---------- */
  function loadGA4() {
    var id = window.GA4_ID;
    if (!id || id.indexOf("XXXX") !== -1) return; // Platzhalter -> nichts laden
    if (window.__ga4Loaded) return;
    window.__ga4Loaded = true;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + id;
    document.head.appendChild(s);
    gtag("js", new Date());
    gtag("config", id, { anonymize_ip: true });
  }

  /* ---------- Cookie-Consent ---------- */
  var KEY = "pantomime_consent";
  var box = document.getElementById("cookie");
  function setConsent(granted) {
    if (typeof gtag === "function") {
      gtag("consent", "update", {
        ad_storage: "denied",
        ad_user_data: "denied",
        ad_personalization: "denied",
        analytics_storage: granted ? "granted" : "denied"
      });
    }
    if (granted) loadGA4();
  }
  try {
    var saved = localStorage.getItem(KEY);
    if (saved === "granted") { setConsent(true); }
    else if (saved !== "denied" && box) { box.hidden = false; }
  } catch (e) { if (box) box.hidden = false; }

  function decide(granted) {
    try { localStorage.setItem(KEY, granted ? "granted" : "denied"); } catch (e) {}
    setConsent(granted);
    if (box) box.hidden = true;
  }
  var acc = document.getElementById("cookieAccept");
  var dec = document.getElementById("cookieDecline");
  if (acc) acc.addEventListener("click", function () { decide(true); });
  if (dec) dec.addEventListener("click", function () { decide(false); });

  /* ---------- Web3Forms Kontaktformular ---------- */
  var form = document.getElementById("contactForm");
  if (form) {
    var status = form.querySelector(".form-status");
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      if (form.querySelector('input[name="botcheck"]') &&
          form.querySelector('input[name="botcheck"]').checked) return;
      var consent = form.querySelector('input[name="consent"]');
      if (consent && !consent.checked) {
        if (status) { status.className = "form-status err"; status.textContent = "Bitte bestätigen Sie die Einwilligung zur Datenverarbeitung."; }
        consent.focus();
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      var data = new FormData(form);
      if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = "Wird gesendet…"; }
      if (status) { status.className = "form-status"; status.textContent = ""; }
      fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: { Accept: "application/json" },
        body: data
      }).then(function (r) { return r.json(); }).then(function (json) {
        if (json.success) {
          if (status) { status.className = "form-status ok"; status.textContent = "Danke! Ihre Anfrage ist angekommen — ich melde mich schnellstmöglich."; }
          form.reset();
        } else {
          if (status) { status.className = "form-status err"; status.textContent = "Etwas ist schiefgelaufen. Bitte rufen Sie an: 0172-1517578."; }
        }
      }).catch(function () {
        if (status) { status.className = "form-status err"; status.textContent = "Verbindungsfehler. Bitte rufen Sie an: 0172-1517578."; }
      }).finally(function () {
        if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label || "Anfrage senden"; }
      });
    });
  }
})();

/* Kontrast-Test (TDD-Sichtbarkeit) — in der Browser-Konsole auf einer Seite ausführen.
   Prüft WCAG-AA: normaler Text ≥4.5:1, großer/fetter Text ≥3:1.
   Gibt {fails,total,lines} zurück. fails===0 ⇒ alles sichtbar. */
(() => {
  function lum(c){const m=c.match(/[\d.]+/g).map(Number);const[r,g,b]=m.slice(0,3).map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*r+.7152*g+.0722*b;}
  function bgOf(el){let e=el;while(e){const bg=getComputedStyle(e).backgroundColor;if(bg&&!/rgba?\(0, 0, 0, 0\)|transparent/.test(bg))return bg;e=e.parentElement;}return 'rgb(248,240,221)';}
  function ratio(el){const s=getComputedStyle(el);const fg=lum(s.color),bg=lum(bgOf(el));const hi=Math.max(fg,bg),lo=Math.min(fg,bg);return (hi+.05)/(lo+.05);}
  function isLarge(el){const s=getComputedStyle(el);const px=parseFloat(s.fontSize);return px>=24||(parseInt(s.fontWeight)>=600&&px>=18.66);}
  const sels=['.hero h1','.hero-lead','.hero .kicker','.site-nav a','.nav-cta','.playbill .prose p','.section--crimson .lead','.section--crimson .kicker','.fig-card h3','.fig-card p','.fig-card .more','.anlass p','.anlass h3','.chip','.cta-band p','.cta-band h2','.footer-col a','.footer-grid p','.subhero .intro','.contact-info p','.prose p','.lead'];
  const res=[];let fails=0;
  sels.forEach(sel=>{const el=document.querySelector(sel);if(!el)return;const r=ratio(el);const need=isLarge(el)?3:4.5;const ok=r>=need;if(!ok)fails++;res.push((ok?'PASS':'FAIL')+'  '+r.toFixed(2)+' (need '+need+')  '+sel);});
  const out={fails,total:res.length,lines:res.join('\n')};
  console.log(out.lines+'\n--- '+(fails?('FAIL: '+fails+' Verstoesse'):'ALLE SICHTBAR')+' ---');
  return out;
})();

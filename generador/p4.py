# Propuesta 4 — "Sistema": retícula suiza, blanco, Poppins + mono, teal como único acento. Precisión holandesa, datos al frente.
import content as C
from common import *

N = 4
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Montserrat:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">'

CSS = """
:root{--bg:#FFFFFF;--off:#F5F2EC;--ink:#1F3C54;--body:#2F363B;--muted:#6A7378;--teal:#4A7A69;--teal-soft:#DCEDE6;--coral:#C96A50;--rule:#1F3C54;--rule-soft:rgba(31,60,84,.16);
--display:'Poppins',system-ui,sans-serif;--text:'Montserrat',system-ui,sans-serif;--mono:'IBM Plex Mono',ui-monospace,monospace;
--map-land:#4A7A69;--map-ink:#1F3C54;--map-bg:#FFFFFF;--map-accent:#C96A50;--map-muted:#6A7378;
--cookie-bg:#FFFFFF;--cookie-fg:#1F3C54;--cookie-line:#1F3C54;--cookie-btn:#1F3C54;--cookie-btn-fg:#fff}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--body);font-family:var(--text);font-size:16px;line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:var(--display);color:var(--ink);font-weight:500;letter-spacing:-.025em;line-height:1.05;margin:0 0 .5em}
h1{font-size:clamp(44px,6.4vw,88px)}h2{font-size:clamp(30px,3.6vw,46px)}h3{font-size:20px;font-weight:600;letter-spacing:-.01em}
p{margin:0 0 1em}a{color:var(--ink)}
.wrap{max-width:1280px;margin:0 auto;padding:0 32px}
.mono{font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--teal)}
.kicker{font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--teal);display:block;margin-bottom:20px}
.btn{display:inline-flex;align-items:center;gap:12px;background:var(--ink);color:#fff;text-decoration:none;padding:16px 24px;font-weight:500;font-family:var(--display);font-size:15px;transition:.2s}
.btn:hover{background:var(--teal)}
.btn.line{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink)}.btn.line:hover{background:var(--ink);color:#fff}
.btn .k{font-family:var(--mono);font-size:11px;opacity:.7}
.lede{font-size:20px;line-height:1.5;max-width:56ch;color:var(--body)}
.grid12{display:grid;grid-template-columns:repeat(12,1fr);gap:32px}
.sec{padding:96px 0;border-top:1px solid var(--rule)}
.sec-head{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;margin-bottom:56px}
.sec-head .mono{grid-column:1/3}.sec-head h2{grid-column:3/10;margin:0}
/* header */
.hdr{position:sticky;top:0;z-index:40;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);border-bottom:1px solid var(--rule)}
.hdr .wrap{display:flex;align-items:center;justify-content:space-between;height:72px;gap:24px}
.logo-svg{height:30px;width:auto;color:var(--ink)}
.nav{display:flex;gap:28px}
.nav-a{text-decoration:none;color:var(--ink);font-size:13px;font-weight:500;font-family:var(--display);position:relative}
.nav-a[aria-current]::before{content:"";position:absolute;left:-12px;top:50%;width:6px;height:6px;background:var(--coral);border-radius:50%;transform:translateY(-50%)}
.hdr .right{display:flex;align-items:center;gap:20px}
.lang{font-family:var(--mono);font-size:11px;letter-spacing:.08em;color:var(--muted)}.lang b{color:var(--ink);font-weight:500}
.burger{display:none;background:none;border:1px solid var(--rule);width:40px;height:40px;font-size:18px;cursor:pointer;color:var(--ink)}
/* hero */
.hero{padding:88px 0 88px}
.hero .g{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;align-items:start}
.hero .meta{grid-column:1/3;grid-row:1;font-family:var(--mono);font-size:12px;color:var(--muted);line-height:1.8;text-transform:uppercase;letter-spacing:.06em;padding-top:12px}
.hero h1{grid-column:3/9;grid-row:1;max-width:14ch;margin:0}
.hero .lede{grid-column:3/8;grid-row:2;margin-top:24px}
.hero .act{grid-column:3/8;grid-row:3;display:flex;gap:24px;align-items:center;flex-wrap:wrap;margin-top:8px}
.hero .micro{font-family:var(--mono);font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.hero figure{grid-column:9/13;grid-row:1/4;margin:0}
.hero img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top;filter:grayscale(.15)}
.hero figcaption{font-family:var(--mono);font-size:11px;color:var(--muted);margin-top:10px;text-transform:uppercase;letter-spacing:.06em}
/* why */
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--rule);border-left:1px solid var(--rule)}
.why-grid article{padding:40px 32px 48px;border-right:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.why-grid .mono{display:block;margin-bottom:28px}
.why-grid h3{font-size:22px;min-height:2.2em}.why-grid p{font-size:15px;margin:0}
/* quote */
.quote{background:var(--ink);color:#DCE4EA;padding:112px 0}
.quote .grid12{align-items:center}
.quote .mono{grid-column:1/3;color:#8FC2B1}
.quote blockquote{grid-column:3/9;margin:0;font-family:var(--display);font-weight:500;font-size:clamp(30px,3.6vw,52px);line-height:1.08;letter-spacing:-.025em;color:#fff}
.quote .body{grid-column:3/9;margin-top:36px;font-size:15.5px}
.quote figure{grid-column:9/13;grid-row:1/3;margin:0}
.quote img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;filter:grayscale(1) contrast(1.05)}
.motto{padding:72px 0;border-top:1px solid var(--rule)}
.motto .grid12{align-items:baseline}
.motto .mono{grid-column:1/3}.motto p{grid-column:3/10;font-family:var(--display);font-size:clamp(22px,2.4vw,30px);color:var(--ink);font-weight:500;line-height:1.3;margin:0;letter-spacing:-.02em}
/* cta */
.cta{padding:96px 0;border-top:1px solid var(--rule);background:var(--off)}
.cta .grid12{align-items:center}
.cta .mono{grid-column:1/3}.cta h2{grid-column:3/9;font-size:clamp(34px,4.2vw,56px);margin:0 0 16px}
.cta h2 .arrow{color:var(--coral)}
.cta p{grid-column:3/9;margin:0 0 28px;color:var(--muted)}
.cta .btn{grid-column:3/6;justify-self:start}
/* footer */
.ftr{border-top:1px solid var(--rule);padding:64px 0 32px;font-size:14px}
.ftr .grid12 > div:nth-child(1){grid-column:1/5}.ftr .grid12 > div:nth-child(2){grid-column:5/8}.ftr .grid12 > div:nth-child(3){grid-column:8/13}
.ftr .logo-svg{margin-bottom:18px;height:36px}
.ftr h4{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--teal);margin:0 0 16px;font-weight:500}
.ftr a{text-decoration:none}.ftr a:hover{text-decoration:underline}
.ftr .links a{display:block;margin-bottom:8px}
.ftr .bottom{display:flex;justify-content:space-between;gap:20px;margin-top:56px;padding-top:20px;border-top:1px solid var(--rule-soft);font-family:var(--mono);font-size:11px;color:var(--muted);flex-wrap:wrap;text-transform:uppercase;letter-spacing:.04em}
/* page header */
.ph{padding:88px 0 64px}
.ph .grid12{align-items:end}
.ph .mono{grid-column:1/3}.ph h1{grid-column:3/12;font-size:clamp(40px,5.6vw,76px);margin:0}
.ph .lede{grid-column:3/9;margin-top:32px}
/* approach */
.pull{padding:56px 0;border-top:1px solid var(--rule)}
.pull p{grid-column:3/10;font-family:var(--display);font-size:clamp(26px,3vw,40px);font-weight:500;letter-spacing:-.02em;line-height:1.15;color:var(--ink);margin:0}
.pull p span{color:var(--teal)}
.steps{border-top:1px solid var(--rule);display:grid;grid-template-columns:repeat(4,1fr)}
.steps .st{padding:32px 24px 40px;border-right:1px solid var(--rule-soft);position:relative}
.steps .st:last-child{border-right:0}
.steps .mono{display:block;margin-bottom:48px}
.steps h3{font-size:30px;font-weight:500;letter-spacing:-.02em}.steps p{font-size:14px;color:var(--muted);margin:0}
.steps .st::after{content:"→";position:absolute;right:-9px;top:30px;background:#fff;color:var(--coral);font-size:14px;padding:0 2px}
.steps .st:last-child::after{content:"↻";right:24px;color:var(--teal)}
.loopnote{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;padding:24px 0 80px;border-top:1px solid var(--rule)}
.loopnote .mono{grid-column:1/3}.loopnote p{grid-column:3/9;margin:0;color:var(--muted);font-size:15px}
.before{border:1px solid var(--rule);padding:40px;display:grid;grid-template-columns:auto 1fr auto;gap:40px;align-items:center;margin-bottom:96px;background:var(--off)}
.before h3{margin:0;font-size:24px}.before p{margin:0;color:var(--muted)}
.phases{border-top:1px solid var(--rule)}
.phase{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;padding:40px 0;border-bottom:1px solid var(--rule-soft)}
.phase .mono{grid-column:1/3}.phase h3{grid-column:3/6;font-size:28px;font-weight:500;margin:0}.phase p{grid-column:6/12;margin:0;font-size:15.5px}
.beyond{margin-top:96px;display:grid;grid-template-columns:repeat(12,1fr);gap:32px;align-items:center}
.beyond .t{grid-column:1/7}.beyond img{grid-column:8/13;display:block;width:100%;aspect-ratio:3/2;object-fit:cover;filter:grayscale(.2)}
/* experience */
.stats{display:grid;grid-template-columns:repeat(3,1fr);border:1px solid var(--rule);margin:0 0 96px}
.stat{padding:40px 32px;border-right:1px solid var(--rule)}.stat:last-child{border-right:0}
.stat .mono{display:block;margin-bottom:28px}
.stat .v{font-family:var(--display);font-size:clamp(44px,5vw,72px);font-weight:500;color:var(--ink);line-height:1;letter-spacing:-.04em}
.stat .v i{font-style:normal;color:var(--coral);font-size:.45em;margin:0 10px;vertical-align:middle}
.stat .l{font-size:14px;color:var(--muted);margin-top:16px}
.proof{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;align-items:center;padding-bottom:96px}
.proof figure{grid-column:1/7;margin:0}.proof .t{grid-column:8/13}
.proof img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover}
.proof figcaption{font-family:var(--mono);font-size:11px;color:var(--muted);margin-top:10px;text-transform:uppercase;letter-spacing:.06em}
.case{border:1px solid var(--rule);display:grid;grid-template-columns:repeat(12,1fr);gap:32px;padding:48px 40px;margin-top:48px}
.case .h{grid-column:1/5}.case .b{grid-column:5/12}
.case h3{font-size:clamp(34px,4vw,56px);font-weight:500;letter-spacing:-.03em}.case p{font-size:15.5px}
/* about */
.about{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;padding-bottom:96px}
.about figure{grid-column:1/5;margin:0;position:sticky;top:100px}
.about img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top;filter:grayscale(.15)}
.about .t{grid-column:6/12}
.lesson{border-left:3px solid var(--coral);padding:8px 0 8px 28px;font-family:var(--display);font-size:clamp(22px,2.4vw,30px);font-weight:500;color:var(--ink);line-height:1.25;margin:40px 0;letter-spacing:-.02em}
.tl{list-style:none;margin:0;padding:0;border-top:1px solid var(--rule)}
.tl li{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;padding:20px 0;border-bottom:1px solid var(--rule-soft);font-size:15px}
.tl b{grid-column:1/3;font-family:var(--mono);font-weight:500;color:var(--teal);font-size:12px;letter-spacing:.06em;text-transform:uppercase;padding-top:3px}
.tl span{grid-column:3/10}
/* network */
.mapbox{border:1px solid var(--rule);padding:24px;margin:0 0 72px}
.pillars{display:grid;grid-template-columns:repeat(3,1fr);border:1px solid var(--rule);margin-bottom:72px}
.pillars article{padding:36px 32px;border-right:1px solid var(--rule)}.pillars article:last-child{border-right:0}
.pillars h3{font-size:20px}.pillars p{font-size:14.5px;color:var(--muted);margin:0}
.impulsa{display:flex;justify-content:space-between;align-items:center;gap:40px;background:var(--off);border:1px solid var(--rule);padding:40px;margin-bottom:40px;flex-wrap:wrap}
.impulsa h2{font-size:26px;margin:0}
.impulsa .badge{font-family:var(--mono);font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink);padding:16px 24px;text-decoration:none;white-space:nowrap}
/* contact */
.contact{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;padding-bottom:112px;align-items:start}
.cal{grid-column:1/6;background:var(--ink);color:#DCE4EA;padding:44px}
.cal .mono{color:#8FC2B1}.cal h3{color:#fff;font-size:28px;font-weight:500}.cal .btn{background:#fff;color:var(--ink)}.cal .btn:hover{background:#8FC2B1}
.cal .mail{margin-top:32px;font-size:14px}.cal .mail a{color:#fff}
.contact .fm{grid-column:7/13}
.cform{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.f{display:flex;flex-direction:column;gap:8px;font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.f-wide{grid-column:1/-1}
.f input,.f textarea{font-family:var(--text);font-size:16px;text-transform:none;letter-spacing:0;padding:12px 0;border:0;border-bottom:1px solid var(--rule);background:transparent;color:var(--ink);outline:none;border-radius:0}
.f input:focus,.f textarea:focus{border-bottom-color:var(--teal);border-bottom-width:2px}
.privacy{font-size:12px;color:var(--muted);display:flex;gap:10px;align-items:flex-start;font-family:var(--text);text-transform:none;letter-spacing:0}
.doc{max-width:760px;padding:88px 0 120px}
@media(max-width:960px){
.grid12,.sec-head,.hero .g,.quote .grid12,.motto .grid12,.cta .grid12,.ph .grid12,.pull .grid12,.loopnote,.phase,.beyond,.proof,.case,.about,.tl li,.contact{grid-template-columns:1fr;gap:20px}
.hero .meta,.hero h1,.hero .lede,.hero .act,.hero figure,.sec-head .mono,.sec-head h2,.quote .mono,.quote blockquote,.quote .body,.quote figure,.motto .mono,.motto p,.cta .mono,.cta h2,.cta p,.cta .btn,.ph .mono,.ph h1,.ph .lede,.pull p,.loopnote .mono,.loopnote p,.phase .mono,.phase h3,.phase p,.beyond .t,.beyond img,.proof figure,.proof .t,.case .h,.case .b,.about figure,.about .t,.tl b,.tl span,.cal,.contact .fm,.ftr .grid12 > div{grid-column:1/-1 !important;grid-row:auto !important}
.why-grid,.stats,.pillars,.steps{grid-template-columns:1fr}
.steps .st{border-right:0;border-bottom:1px solid var(--rule-soft)}.steps .st::after{display:none}
.stat,.pillars article{border-right:0;border-bottom:1px solid var(--rule)}
.before{grid-template-columns:1fr;gap:16px}
.about figure,.hero figure{position:static;max-width:420px}
.nav{display:none;position:absolute;top:72px;left:0;right:0;background:#fff;flex-direction:column;padding:20px 32px;border-bottom:1px solid var(--rule)}
.nav.open{display:flex}.burger{display:block}.hdr .right .btn{display:none}
.hero{padding:48px 0 0}
}
@media(max-width:600px){.wrap{padding:0 18px}.cform{grid-template-columns:1fr}.case,.cal,.impulsa,.before{padding:28px 20px}.sec{padding:64px 0}}
""" + MAP_CSS + COOKIE_CSS


def header(active):
    return f"""
<header class="hdr"><div class="wrap">
  <a href="index.html" aria-label="VeliD Advisory home">{LOGO_SVG}</a>
  <nav class="nav" aria-label="Main">{nav_links(active)}</nav>
  <div class="right"><span class="lang"><b>EN</b> / NL</span><a class="btn line" href="{C.CALENDLY}">{C.CTA}</a><button class="burger" aria-label="Menu" aria-expanded="false">☰</button></div>
</div></header>"""

def cta_block(idx="05"):
    return f"""
<section class="cta"><div class="wrap grid12">
  <span class="mono">{idx} — Next step</span>
  <h2><span class="arrow">→</span> {C.CTA} <span class="arrow">←</span></h2>
  <p>{C.CTA_SUB}</p>
  <a class="btn" href="{C.CALENDLY}">{C.CTA} <span class="k">30 MIN</span></a>
</div></section>"""

def footer():
    return f"""
<footer class="ftr"><div class="wrap">
 <div class="grid12">
  <div>{LOGO_SVG}<p>{C.HEADLINE}</p></div>
  <div><h4>Navigation</h4><div class="links">{nav_links("", cls="")}</div></div>
  <div><h4>→ {C.CTA} ←</h4><p>{C.CTA_SUB}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 </div>
 <div class="bottom"><span>{C.COPY}</span><span>EN / NL &nbsp;·&nbsp; <a href="{C.LINKEDIN}">LinkedIn</a> &nbsp;·&nbsp; <a href="mailto:{C.EMAIL}">{C.EMAIL}</a> &nbsp;·&nbsp; <a href="privacy.html">Privacy</a></span></div>
</div></footer>"""

def page(active, title, main):
    return shell(title, header(active) + "<main>" + main + "</main>" + footer(), fonts=FONTS)

def ph(mono, h1, lede=""):
    return f'<div class="wrap ph"><div class="grid12"><span class="mono">{mono}</span><h1>{h1}</h1>{f"<p class=lede>{lede}</p>" if lede else ""}</div></div>'

def build():
    write(N, "style.css", CSS)
    why = "".join(f'<article><span class="mono">0{i+1}</span><h3>{t}</h3><p>{esc(p)}</p></article>' for i, (t, p) in enumerate(C.WHY))
    home = f"""
<section class="wrap hero"><div class="g">
  <div class="meta">VeliD Advisory<br>NL ↔ MX<br>Est. 2026</div><h1>{C.HEADLINE}</h1>
  <p class="lede">{esc(C.HERO_LEAD)}</p><div class="act"><a class="btn" href="{C.CALENDLY}">{C.CTA} <span class="k">30 MIN</span></a><span class="micro">One strategic conversation · no obligation</span></div>
  <figure>{img("portrait")}<figcaption>Carin Verbree — Founder</figcaption></figure>
</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><span class="mono">01 — Why VeliD</span><h2>{C.WHY_TITLE}</h2></div><div class="why-grid">{why}</div></div></section>
<section class="quote"><div class="wrap grid12">
  <span class="mono">02 — Point of view</span>
  <blockquote>“{esc(C.QUOTE)}”</blockquote>
  <figure>{img("panel")}</figure>
  <div class="body"><p>{esc(C.QUOTE_P1)}</p><p>{esc(C.QUOTE_P2)}</p></div>
</div></section>
<section class="motto"><div class="wrap grid12"><span class="mono">03 — Purpose</span><p>{esc(C.MOTTO)}</p></div></section>
{cta_block("04")}
"""
    write(N, "index.html", page("index.html", "Home", home))
    steps = "".join(f'<div class="st"><span class="mono">Step 0{i+1}</span><h3>{s}</h3><p>{esc(l)}</p></div>' for i, (s, l) in enumerate(C.LOOP))
    phases = "".join(f'<div class="phase"><span class="mono">Phase 0{i+1}</span><h3>{t}</h3><p>{esc(p)}</p></div>' for i, (t, p) in enumerate(C.PHASES))
    approach = f"""
{ph("Approach", "Better decisions as you grow across borders.", esc(C.APPROACH_INTRO))}
<div class="wrap">
 <div class="pull"><div class="grid12"><p>Ambition and market reality don't always point the same direction. <span>VeliD helps you see where they meet, and where they don't.</span></p></div></div>
 <div class="steps">{steps}</div>
 <div class="loopnote"><span class="mono">↻ Loop</span><p>{C.LOOP_NOTE} {C.LOOP_BASE}</p></div>
 <div class="before"><h3>{C.BEFORE_TITLE}</h3><p>{C.BEFORE_TEXT}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 <div class="phases">{phases}</div>
 <div class="beyond"><div class="t"><span class="kicker">{C.BEYOND_TITLE}</span><h2>Workshops, cultural training and speaking.</h2><p>{esc(C.BEYOND_TEXT)}</p></div>{img("audience")}</div>
</div>
{cta_block()}
"""
    write(N, "approach.html", page("approach.html", "Approach", approach))
    labels = ["Network", "Turnover", "Retention"]
    stats = "".join(f'<div class="stat"><span class="mono">{labels[i]}</span><div class="v">{a}{"<i>→</i>"+b if b else ""}</div><div class="l">{l}</div></div>' for i, (a, b, l) in enumerate(C.STATS))
    exp = f"""
{ph("Experience & Cases", C.EXP_TITLE, esc(C.EXP_TEXT))}
<div class="wrap">
 <div class="stats">{stats}</div>
 <div class="proof"><figure>{img("certificate")}<figcaption>Recognition — Embassy of the Kingdom of the Netherlands in Mexico</figcaption></figure>
  <div class="t"><span class="kicker">External proof</span><h2>Independent recognition.</h2><p>The transformation of Holland House Mexico was recognized by the Embassy of the Kingdom of the Netherlands in Mexico.</p></div></div>
 <span class="kicker">{C.CASES_TITLE}</span><h2>{C.CASES_P1}</h2><p class="lede">{esc(C.CASES_P2)}</p><p class="lede"><strong>{esc(C.CASES_P3)}</strong></p>
 <div class="case"><div class="h"><span class="kicker">{C.CASE_KICKER} 01</span><h3>{C.CASE_NAME}</h3></div><div class="b"><p>{esc(C.CASE_P1)}</p><p>{esc(C.CASE_P2)}</p></div></div>
</div>
{cta_block()}
"""
    write(N, "experience.html", page("experience.html", "Experience & Cases", exp))
    paras = "".join(f"<p>{esc(p)}</p>" for p in C.ABOUT)
    tl = "".join(f"<li><b>{a}</b><span>{esc(b)}</span></li>" for a, b in C.TIMELINE)
    about = f"""
{ph("About", C.ABOUT_INTRO)}
<div class="wrap">
 <div class="about"><figure>{img("portrait")}</figure>
  <div class="t">{paras}<p class="lesson">{esc(C.ABOUT_LESSON)}</p><p>{esc(C.ABOUT_CLOSE)}</p><p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></p></div></div>
 <span class="kicker">Timeline</span><ul class="tl">{tl}</ul>
</div>
{cta_block()}
"""
    write(N, "about.html", page("about.html", "About", about))
    pillars = "".join(f"<article><h3>{t}</h3><p>{esc(p)}</p></article>" for t, p in C.NET_PILLARS)
    net = f"""
{ph("Network", "From Mexico to Manila.", esc(C.NET_TEXT))}
<div class="wrap">
 <div class="mapbox">{MAP_SVG}</div>
 <div class="pillars">{pillars}</div>
 <div class="impulsa"><h2>{esc(C.NET_IMPULSA)}</h2><a class="badge" href="{C.IMPULSA}">Association IMPULSA ↗</a></div>
 <p class="lede">{esc(C.NET_EXPERT)} <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
</div>
{cta_block()}
"""
    write(N, "network.html", page("network.html", "Network", net))
    contact = f"""
{ph("Contact", C.CONTACT_TITLE)}
<div class="wrap">
 <div class="contact">
  <div class="cal"><span class="mono">Step 01</span><h3>{C.CONTACT_CTA}</h3><p>{C.CTA_VALUE}</p><a class="btn" href="{C.CALENDLY}">Open the calendar ↗</a>
   <p class="mail">Or write directly: <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p></div>
  <div class="fm"><h3>{C.CONTACT_ALT}</h3>{form_html()}</div>
 </div>
</div>
"""
    write(N, "contact.html", page("contact.html", "Contact", contact))
    write(N, "privacy.html", page("", "Privacy notice", f'<div class="wrap doc">{privacy_page_body()}</div>'))

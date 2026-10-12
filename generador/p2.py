# Propuesta 2 — "Brújula": navy inmersivo, Poppins, fotos a sangre con duotono, teal como energía. Seguridad y dirección.
import content as C
from common import *

N = 2
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Montserrat:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">'

CSS = """
:root{--bg:#101B25;--bg2:#15222E;--surface:#1B2C3A;--ink:#FAF5EA;--body:#D7DEE3;--muted:#93A4B0;--teal:#8FC2B1;--teal-deep:#4A7A69;--coral:#F0A992;--coral-deep:#C96A50;--rule:rgba(250,245,234,.14);
--light:#FAF5EA;--light-ink:#1F3C54;--light-body:#3A4248;--light-muted:#5A6469;
--display:'Poppins',system-ui,sans-serif;--text:'Montserrat',system-ui,sans-serif;
--map-land:#5D9382;--map-ink:#FAF5EA;--map-bg:#1B2C3A;--map-accent:#F0A992;--map-muted:#A3B1BA;
--cookie-bg:#FAF5EA;--cookie-fg:#1F3C54;--cookie-line:#FAF5EA;--cookie-btn:#1F3C54;--cookie-btn-fg:#FAF5EA;--cookie-radius:999px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--body);font-family:var(--text);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:var(--display);color:var(--ink);font-weight:600;letter-spacing:-.02em;line-height:1.08;margin:0 0 .5em}
h1{font-size:clamp(42px,6vw,80px)}h2{font-size:clamp(30px,3.6vw,48px)}h3{font-size:22px;font-weight:600}
p{margin:0 0 1em}a{color:var(--teal)}
.wrap{max-width:1200px;margin:0 auto;padding:0 32px}
.kicker{font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--teal);font-weight:600;display:flex;align-items:center;gap:12px;margin-bottom:20px}
.kicker::before{content:"";width:28px;height:2px;background:var(--teal)}
.btn{display:inline-flex;align-items:center;gap:10px;background:var(--coral);color:#1F3C54;text-decoration:none;padding:16px 30px;border-radius:999px;font-weight:600;font-family:var(--display);font-size:15px;transition:.2s;border:2px solid var(--coral)}
.btn:hover{background:#fff;border-color:#fff}
.btn.ghost{background:transparent;color:var(--ink);border-color:rgba(250,245,234,.4)}.btn.ghost:hover{border-color:var(--ink);background:transparent}
.btn.dark{background:var(--light-ink);border-color:var(--light-ink);color:var(--light)}.btn.dark:hover{background:var(--teal-deep);border-color:var(--teal-deep)}
.lede{font-size:20px;line-height:1.55;max-width:60ch}
/* header */
.hdr{position:sticky;top:0;z-index:40;background:rgba(16,27,37,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--rule)}
.hdr .wrap{display:flex;align-items:center;justify-content:space-between;height:88px;gap:24px}
.logo-svg{height:36px;width:auto;color:var(--ink)}
.nav{display:flex;gap:4px}
.nav-a{text-decoration:none;color:var(--ink);font-size:14px;font-weight:500;padding:8px 14px;border-radius:999px}
.nav-a[aria-current]{background:rgba(250,245,234,.12)}
.hdr .right{display:flex;align-items:center;gap:18px}
.lang{font-size:12px;letter-spacing:.14em;color:var(--muted)}.lang b{color:var(--ink);font-weight:600}
.burger{display:none;background:none;border:1px solid var(--rule);width:44px;height:44px;border-radius:50%;font-size:20px;cursor:pointer;color:var(--ink)}
/* hero */
.hero{position:relative;min-height:calc(92vh - 88px);display:flex;align-items:flex-end;padding:96px 0 96px;overflow:hidden}
.hero .bgimg{position:absolute;inset:0;z-index:0}
.hero .bgimg img{width:100%;height:100%;object-fit:cover;object-position:center 30%;filter:grayscale(1) contrast(1.05)}
.hero .bgimg::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(16,27,37,.97) 0%,rgba(16,27,37,.9) 40%,rgba(31,60,84,.6) 100%),linear-gradient(0deg,#101B25 0%,transparent 50%)}
.hero .wrap{position:relative;z-index:1}
.hero h1{max-width:14ch}
.hero .lede{color:var(--body)}
.hero .row{display:flex;align-items:center;gap:28px;margin-top:36px;flex-wrap:wrap}
.hero .micro{font-size:13px;color:var(--muted)}
.hero .tag{font-family:var(--display);color:var(--teal);font-weight:500;letter-spacing:.1em;text-transform:uppercase;font-size:13px;margin-bottom:24px}
/* light section */
.light{background:var(--light);color:var(--light-body)}
.light h1,.light h2,.light h3{color:var(--light-ink)}
.light .kicker{color:var(--teal-deep)}.light .kicker::before{background:var(--teal-deep)}
.light a{color:var(--light-ink)}
.sec{padding:112px 0}
/* why */
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:56px}
.card{background:#fff;border-radius:24px;padding:40px 36px;box-shadow:0 20px 50px rgba(31,60,84,.08)}
.card .ic{width:52px;height:52px;border-radius:16px;background:var(--light-ink);display:grid;place-items:center;margin-bottom:24px;color:var(--teal)}
.card .ic svg{width:26px;height:26px}
.card h3{font-size:21px}.card p{font-size:15.5px;margin:0}
/* quote */
.quote{padding:120px 0;position:relative}
.quote .grid{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.quote blockquote{margin:0 0 36px;font-family:var(--display);font-size:clamp(30px,3.6vw,48px);font-weight:600;line-height:1.15;color:var(--ink);letter-spacing:-.02em}
.quote blockquote span{color:var(--teal)}
.quote figure{margin:0;border-radius:28px;overflow:hidden;position:relative}
.quote img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover}
.quote figure::after{content:"";position:absolute;inset:0;background:linear-gradient(160deg,rgba(74,122,105,.45),rgba(31,60,84,.2));mix-blend-mode:multiply}
.motto{text-align:center;font-family:var(--display);font-weight:500;font-size:clamp(22px,2.4vw,30px);color:var(--teal);max-width:28ch;margin:0 auto;padding:0 0 112px;line-height:1.3}
/* cta */
.cta{padding:120px 0;background:radial-gradient(1200px 500px at 50% 0%,rgba(74,122,105,.35),transparent 70%)}
.cta .box{text-align:center;max-width:760px;margin:0 auto}
.cta h2{font-size:clamp(36px,4.4vw,60px)}
.cta h2 .arrow{color:var(--coral)}
.cta p{font-size:18px;color:var(--muted);margin-bottom:36px}
/* footer */
.ftr{border-top:1px solid var(--rule);padding:72px 0 36px;font-size:14px}
.ftr .grid{display:grid;grid-template-columns:1.2fr 1fr 1.2fr;gap:48px}
.ftr .logo-svg{margin-bottom:18px;height:40px}
.ftr h4{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--teal);margin:0 0 16px}
.ftr a{color:var(--ink);text-decoration:none}.ftr a:hover{text-decoration:underline}
.ftr .links a{display:block;margin-bottom:8px}
.ftr .bottom{display:flex;justify-content:space-between;gap:20px;margin-top:56px;padding-top:24px;border-top:1px solid var(--rule);font-size:12px;color:var(--muted);flex-wrap:wrap}
/* page header */
.ph{padding:96px 0 72px;max-width:900px}
.ph h1{font-size:clamp(40px,5.4vw,68px)}
/* approach */
.pull{font-family:var(--display);font-size:clamp(26px,3.2vw,40px);font-weight:500;line-height:1.2;color:var(--ink);max-width:28ch;margin:0 0 80px;padding:36px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.pull span{color:var(--coral)}
.track{display:grid;grid-template-columns:repeat(4,1fr);gap:0;position:relative;margin-bottom:24px}
.track::before{content:"";position:absolute;left:5%;right:5%;top:30px;height:2px;background:linear-gradient(90deg,var(--teal),var(--coral))}
.track .st{text-align:center;padding:0 16px}
.track .dot{width:60px;height:60px;border-radius:50%;background:var(--bg);border:2px solid var(--teal);display:grid;place-items:center;margin:0 auto 20px;font-family:var(--display);font-weight:600;color:var(--teal);position:relative}
.track .st:nth-child(4) .dot{border-color:var(--coral);color:var(--coral)}
.track h3{font-size:18px}.track p{font-size:14px;color:var(--muted);margin:0}
.loopnote{text-align:center;font-family:var(--display);color:var(--teal);font-weight:500;margin:0 0 96px;font-size:18px}
.loopnote small{display:block;color:var(--muted);font-family:var(--text);font-weight:400;font-size:14px;margin-top:6px}
.before{background:var(--surface);border:1px solid var(--rule);border-radius:28px;padding:44px 48px;display:grid;grid-template-columns:auto 1fr auto;gap:40px;align-items:center;margin-bottom:96px}
.before h3{margin:0;font-size:24px}.before p{margin:0;color:var(--muted)}
.phases{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.phase{background:var(--surface);border-radius:24px;padding:40px 36px;border:1px solid var(--rule);position:relative;overflow:hidden}
.phase .n{font-family:var(--display);font-size:72px;font-weight:700;color:transparent;-webkit-text-stroke:1px var(--teal);line-height:1;margin-bottom:24px;opacity:.9}
.phase p{font-size:15.5px;margin:0;color:var(--body)}
.beyond{margin-top:96px;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.beyond img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:28px}
/* experience */
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin:64px 0 96px}
.stat{background:var(--surface);border:1px solid var(--rule);border-radius:24px;padding:40px 32px}
.stat .v{font-family:var(--display);font-size:clamp(40px,4.6vw,64px);font-weight:700;color:var(--ink);line-height:1;letter-spacing:-.03em}
.stat .v i{font-style:normal;color:var(--coral);font-size:.5em;margin:0 10px;vertical-align:middle}
.stat .l{font-size:14px;color:var(--muted);margin-top:16px}
.proof{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;padding-bottom:96px}
.proof figure{margin:0;border-radius:28px;overflow:hidden}
.proof img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover}
.proof figcaption{font-size:13px;color:var(--muted);padding:14px 4px 0}
.case{background:linear-gradient(135deg,#1F3C54,#15222E);border:1px solid var(--rule);border-radius:32px;padding:64px;display:grid;grid-template-columns:1fr 1.5fr;gap:64px;margin-top:56px}
.case h3{font-size:clamp(34px,4vw,56px);font-weight:700;color:var(--ink)}
.case .pill{display:inline-block;background:rgba(143,194,177,.15);color:var(--teal);border-radius:999px;padding:6px 14px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;margin-bottom:18px}
.case p{font-size:16px}
/* about */
.about{display:grid;grid-template-columns:.85fr 1.15fr;gap:80px;align-items:start;padding-bottom:96px}
.about figure{margin:0;border-radius:32px;overflow:hidden;position:sticky;top:120px}
.about img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top}
.lesson{font-family:var(--display);font-size:clamp(24px,2.6vw,32px);font-weight:500;color:var(--ink);line-height:1.25;margin:48px 0;padding:36px;background:var(--surface);border-radius:24px;border-left:4px solid var(--coral)}
.tl{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.tl li{background:var(--surface);border:1px solid var(--rule);border-radius:20px;padding:28px;font-size:15px}
.tl b{font-family:var(--display);color:var(--teal);display:block;font-size:14px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:10px}
/* network */
.mapbox{border-radius:32px;overflow:hidden;border:1px solid var(--rule);background:var(--surface);padding:24px;margin:0 0 72px}
.pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:72px}
.pillars article{background:var(--surface);border:1px solid var(--rule);border-radius:24px;padding:36px}
.pillars h3{font-size:20px}.pillars p{font-size:15px;color:var(--muted);margin:0}
.impulsa{display:flex;justify-content:space-between;align-items:center;gap:40px;background:var(--light);color:var(--light-body);border-radius:28px;padding:48px;margin-bottom:40px;flex-wrap:wrap}
.impulsa h2{color:var(--light-ink);font-size:28px;margin:0}
.impulsa .badge{font-family:var(--display);font-weight:700;color:var(--light-ink);border:2px solid var(--light-ink);border-radius:999px;padding:16px 28px;text-decoration:none;white-space:nowrap}
/* contact */
.contact{display:grid;grid-template-columns:1fr 1fr;gap:72px;padding-bottom:120px;align-items:start}
.cal{background:linear-gradient(135deg,#1F3C54,#15222E);border:1px solid var(--rule);border-radius:32px;padding:48px}
.cal h3{font-size:30px}.cal .mail{margin-top:32px;font-size:14px;color:var(--muted)}.cal .mail a{color:var(--ink)}
.cform{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.f{display:flex;flex-direction:column;gap:8px;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600}
.f-wide{grid-column:1/-1}
.f input,.f textarea{font:inherit;font-size:16px;text-transform:none;letter-spacing:0;font-weight:400;padding:14px 18px;border:1px solid var(--rule);border-radius:14px;background:var(--surface);color:var(--ink);outline:none}
.f input:focus,.f textarea:focus{border-color:var(--teal)}
.privacy{font-size:12px;color:var(--muted);display:flex;gap:10px;align-items:flex-start}
.doc{max-width:760px;padding:96px 0 120px}
@media(max-width:960px){
.quote .grid,.beyond,.proof,.case,.about,.contact{grid-template-columns:1fr;gap:40px}
.why-grid,.stats,.pillars,.phases,.tl{grid-template-columns:1fr}
.track{grid-template-columns:1fr 1fr;row-gap:32px}.track::before{display:none}
.ftr .grid{grid-template-columns:1fr}
.before{grid-template-columns:1fr;gap:16px}
.about figure{position:static;max-width:420px}
.nav{display:none;position:absolute;top:88px;left:0;right:0;background:var(--bg);flex-direction:column;padding:20px 32px;border-bottom:1px solid var(--rule)}
.nav.open{display:flex}.burger{display:block}.hdr .right .btn{display:none}
.hero{min-height:0;padding:64px 0 72px}
}
@media(max-width:600px){.wrap{padding:0 18px}.cform{grid-template-columns:1fr}.case,.cal,.impulsa{padding:32px 24px}.sec{padding:72px 0}}
""" + MAP_CSS + COOKIE_CSS

ICONS = [
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18M5.5 6.5c2 1.5 4 2.2 6.5 2.2s4.5-.7 6.5-2.2M5.5 17.5c2-1.5 4-2.2 6.5-2.2s4.5.7 6.5 2.2"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="5" cy="12" r="2.2"/><circle cx="19" cy="6" r="2.2"/><circle cx="19" cy="18" r="2.2"/><path d="M7 11l10-4M7 13l10 4"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21V11M12 11c0-4 3-7 8-7-0 4-3 7-8 7zM12 15c0-3-2.5-5-6-5 0 3 2.5 5 6 5z"/></svg>',
]

def header(active):
    return f"""
<header class="hdr"><div class="wrap">
  <a href="index.html" aria-label="VeliD Advisory home">{LOGO_SVG}</a>
  <nav class="nav" aria-label="Main">{nav_links(active)}</nav>
  <div class="right"><span class="lang"><b>EN</b> · NL</span><a class="btn ghost" href="{C.CALENDLY}">{C.CTA}</a><button class="burger" aria-label="Menu" aria-expanded="false">☰</button></div>
</div></header>"""

def cta_block():
    return f"""
<section class="cta"><div class="wrap box">
  <h2><span class="arrow">→</span> {C.CTA} <span class="arrow">←</span></h2>
  <p>{C.CTA_SUB}</p>
  <a class="btn" href="{C.CALENDLY}">{C.CTA} <span aria-hidden="true">↗</span></a>
</div></section>"""

def footer():
    return f"""
<footer class="ftr"><div class="wrap">
 <div class="grid">
  <div>{LOGO_SVG}<p>{C.HEADLINE}</p></div>
  <div><h4>Navigation</h4><div class="links">{nav_links("", cls="")}</div></div>
  <div><h4>→ {C.CTA} ←</h4><p>{C.CTA_SUB}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 </div>
 <div class="bottom"><span>{C.COPY}</span><span>EN · NL &nbsp;·&nbsp; <a href="{C.LINKEDIN}">LinkedIn</a> &nbsp;·&nbsp; <a href="mailto:{C.EMAIL}">{C.EMAIL}</a> &nbsp;·&nbsp; <a href="privacy.html">Privacy</a></span></div>
</div></footer>"""

def page(active, title, main):
    return shell(title, header(active) + "<main>" + main + "</main>" + footer(), fonts=FONTS)

def build():
    write(N, "style.css", CSS)
    why = "".join(f'<article class="card"><div class="ic">{ICONS[i]}</div><h3>{t}</h3><p>{esc(p)}</p></article>' for i, (t, p) in enumerate(C.WHY))
    home = f"""
<section class="hero"><div class="bgimg">{img("panel")}</div><div class="wrap">
  <div class="tag">{C.BRAND} — {C.TAGLINE}</div>
  <h1>{C.HEADLINE}</h1><p class="lede">{esc(C.HERO_LEAD)}</p>
  <div class="row"><a class="btn" href="{C.CALENDLY}">{C.CTA} <span aria-hidden="true">↗</span></a><span class="micro">30 minutes · one strategic conversation · no obligation</span></div>
</div></section>
<section class="light sec"><div class="wrap"><div class="kicker">Why VeliD</div><h2>{C.WHY_TITLE}</h2><div class="why-grid">{why}</div></div></section>
<section class="quote"><div class="wrap grid">
  <div><blockquote>“{esc(C.QUOTE).replace("separate questions", "<span>separate questions</span>")}”</blockquote><p>{esc(C.QUOTE_P1)}</p><p>{esc(C.QUOTE_P2)}</p></div>
  <figure>{img("signing")}</figure>
</div></section>
<p class="motto">{esc(C.MOTTO)}</p>
{cta_block()}
"""
    write(N, "index.html", page("index.html", "Home", home))
    track = "".join(f'<div class="st"><div class="dot">0{i+1}</div><h3>{s}</h3><p>{esc(l)}</p></div>' for i, (s, l) in enumerate(C.LOOP))
    phases = "".join(f'<div class="phase"><div class="n">0{i+1}</div><h3>{t}</h3><p>{esc(p)}</p></div>' for i, (t, p) in enumerate(C.PHASES))
    approach = f"""
<div class="wrap">
 <div class="ph"><div class="kicker">Approach</div><h1>Better decisions as you grow across borders.</h1><p class="lede">{esc(C.APPROACH_INTRO)}</p></div>
 <p class="pull">Ambition and market reality don't always point the same direction. <span>VeliD helps you see where they meet, and where they don't.</span></p>
 <div class="track">{track}</div>
 <p class="loopnote">↻ {C.LOOP_NOTE}<small>{C.LOOP_BASE}</small></p>
 <div class="before"><h3>{C.BEFORE_TITLE}</h3><p>{C.BEFORE_TEXT}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 <div class="kicker">How we work together</div><h2>Three phases. One conversation at a time.</h2>
 <div class="phases">{phases}</div>
 <div class="beyond"><div><div class="kicker">{C.BEYOND_TITLE}</div><h2>Workshops, cultural training and speaking.</h2><p>{esc(C.BEYOND_TEXT)}</p></div>{img("audience")}</div>
</div>
{cta_block()}
"""
    write(N, "approach.html", page("approach.html", "Approach", approach))
    stats = "".join(f'<div class="stat"><div class="v">{a}{"<i>→</i>"+b if b else ""}</div><div class="l">{l}</div></div>' for a, b, l in C.STATS)
    exp = f"""
<div class="wrap">
 <div class="ph"><div class="kicker">Experience &amp; Cases</div><h1>{C.EXP_TITLE}</h1><p class="lede">{esc(C.EXP_TEXT)}</p></div>
 <div class="stats">{stats}</div>
 <div class="proof"><figure>{img("certificate")}<figcaption>{esc(C.PHOTOS["certificate"][1])}.</figcaption></figure>
  <div><div class="kicker">Recognition</div><h2>Independent, external proof.</h2><p>The transformation of Holland House Mexico was recognized by the Embassy of the Kingdom of the Netherlands in Mexico.</p></div></div>
 <div class="kicker">{C.CASES_TITLE}</div><h2>{C.CASES_P1}</h2><p class="lede">{esc(C.CASES_P2)}</p><p class="lede"><strong>{esc(C.CASES_P3)}</strong></p>
 <div class="case"><div><span class="pill">{C.CASE_KICKER}</span><h3>{C.CASE_NAME}</h3></div><div><p>{esc(C.CASE_P1)}</p><p>{esc(C.CASE_P2)}</p></div></div>
</div>
{cta_block()}
"""
    write(N, "experience.html", page("experience.html", "Experience & Cases", exp))
    paras = "".join(f"<p>{esc(p)}</p>" for p in C.ABOUT)
    tl = "".join(f"<li><b>{a}</b>{esc(b)}</li>" for a, b in C.TIMELINE)
    about = f"""
<div class="wrap">
 <div class="ph"><div class="kicker">About</div><h1>{C.ABOUT_INTRO}</h1></div>
 <div class="about"><figure>{img("portrait")}</figure>
  <div>{paras}<p class="lesson">{esc(C.ABOUT_LESSON)}</p><p>{esc(C.ABOUT_CLOSE)}</p><p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></p></div></div>
 <div class="kicker">The road so far</div><ul class="tl">{tl}</ul>
</div>
{cta_block()}
"""
    write(N, "about.html", page("about.html", "About", about))
    pillars = "".join(f"<article><h3>{t}</h3><p>{esc(p)}</p></article>" for t, p in C.NET_PILLARS)
    net = f"""
<div class="wrap">
 <div class="ph"><div class="kicker">Network</div><h1>From Mexico to Manila.</h1><p class="lede">{esc(C.NET_TEXT)}</p></div>
 <div class="mapbox">{MAP_SVG}</div>
 <div class="pillars">{pillars}</div>
 <div class="impulsa"><h2>{esc(C.NET_IMPULSA)}</h2><a class="badge" href="{C.IMPULSA}">Association IMPULSA ↗</a></div>
 <p class="lede">{esc(C.NET_EXPERT)} <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
</div>
{cta_block()}
"""
    write(N, "network.html", page("network.html", "Network", net))
    contact = f"""
<div class="wrap">
 <div class="ph"><div class="kicker">Contact</div><h1>{C.CONTACT_TITLE}</h1></div>
 <div class="contact">
  <div class="cal"><div class="kicker">Step one</div><h3>{C.CONTACT_CTA}</h3><p>{C.CTA_VALUE}</p><a class="btn" href="{C.CALENDLY}">Open the calendar ↗</a>
   <p class="mail">Or write directly: <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p></div>
  <div><h3>{C.CONTACT_ALT}</h3>{form_html()}</div>
 </div>
</div>
"""
    write(N, "contact.html", page("contact.html", "Contact", contact))
    write(N, "privacy.html", page("", "Privacy notice", f'<div class="wrap doc">{privacy_page_body()}</div>'))

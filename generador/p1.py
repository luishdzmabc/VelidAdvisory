# Propuesta 1 — "Horizonte": editorial, serif, crema y navy. Consultora de confianza, tono de revista de negocios.
import content as C
from common import *

N = 1
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=Montserrat:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">'

CSS = """
:root{--bg:#FAF5EA;--surface:#FFFCF5;--ink:#1F3C54;--body:#3A4248;--muted:#6B7479;--teal:#4A7A69;--coral:#C96A50;--coral-soft:#EB937D;--rule:rgba(31,60,84,.18);--deep:#1F3C54;--on-deep:#FAF5EA;--on-deep-soft:#C8D4DC;
--display:'Fraunces',Georgia,serif;--text:'Montserrat',system-ui,sans-serif;
--map-land:#5D9382;--map-ink:#1F3C54;--map-bg:#FFFCF5;--map-accent:#EB937D;--map-muted:#6B7479;
--cookie-bg:#1F3C54;--cookie-fg:#FAF5EA;--cookie-line:#1F3C54;--cookie-btn:#EB937D;--cookie-btn-fg:#1F3C54}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--body);font-family:var(--text);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3,.serif{font-family:var(--display);color:var(--ink);font-weight:400;letter-spacing:-.01em;line-height:1.1;margin:0 0 .5em}
h1{font-size:clamp(40px,5.6vw,72px);font-variation-settings:'opsz' 144}
h2{font-size:clamp(32px,3.6vw,48px);font-variation-settings:'opsz' 96}
h3{font-size:26px}
p{margin:0 0 1em}a{color:var(--ink)}
.wrap{max-width:1180px;margin:0 auto;padding:0 32px}
.kicker{font-family:var(--text);font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--coral);font-weight:600;margin-bottom:18px;display:block}
.btn{display:inline-block;background:var(--ink);color:var(--bg);text-decoration:none;padding:15px 28px;font-weight:600;font-size:15px;letter-spacing:.02em;border:1px solid var(--ink);transition:.2s}
.btn:hover{background:var(--coral);border-color:var(--coral);color:#fff}
.btn.ghost{background:transparent;color:var(--ink)}.btn.ghost:hover{background:var(--ink);color:var(--bg)}
.lede{font-size:21px;line-height:1.55;color:var(--body);max-width:60ch}
.rule{border:0;border-top:1px solid var(--rule);margin:0}
/* header */
.hdr{position:sticky;top:0;z-index:40;background:rgba(250,245,234,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--rule)}
.hdr .wrap{display:flex;align-items:center;justify-content:space-between;height:84px;gap:24px}
.logo-svg{height:34px;width:auto;color:var(--ink)}
.nav{display:flex;gap:30px;align-items:center}
.nav-a{text-decoration:none;color:var(--ink);font-size:14px;font-weight:500;padding:6px 0;border-bottom:1px solid transparent}
.nav-a[aria-current]{border-bottom-color:var(--coral)}
.hdr .right{display:flex;align-items:center;gap:22px}
.lang{font-size:12px;letter-spacing:.14em;color:var(--muted)}.lang b{color:var(--ink);font-weight:600}
.burger{display:none;background:none;border:1px solid var(--rule);width:44px;height:44px;font-size:20px;cursor:pointer;color:var(--ink)}
/* hero */
.hero{display:grid;grid-template-columns:1.15fr .85fr;gap:72px;align-items:center;padding:96px 0 80px}
.hero .brand{font-family:var(--display);font-style:italic;color:var(--teal);font-size:20px;margin-bottom:22px}
.hero .micro{font-size:13px;color:var(--muted);margin-top:14px;letter-spacing:.04em}
.portrait{position:relative;margin:0}
.portrait img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top}
.portrait::after{content:"";position:absolute;inset:18px -18px -18px 18px;border:1px solid var(--coral);z-index:-1}
/* why */
.why{padding:96px 0}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:48px;margin-top:48px}
.why-grid article{border-top:1px solid var(--ink);padding-top:28px}
.why-grid .num{font-family:var(--display);font-style:italic;font-size:44px;color:var(--coral);line-height:1;margin-bottom:18px}
.why-grid h3{font-size:24px}
.why-grid p{font-size:16px}
/* quote band */
.band{background:var(--deep);color:var(--on-deep);padding:104px 0}
.band .grid{display:grid;grid-template-columns:1.1fr .9fr;gap:72px;align-items:center}
.band blockquote{margin:0 0 36px;font-family:var(--display);font-size:clamp(30px,3.4vw,44px);line-height:1.2;color:var(--on-deep);font-weight:300;font-style:italic}
.band blockquote::before{content:"“";color:var(--coral-soft)}
.band p{color:var(--on-deep-soft);font-size:16px}
.band figure{margin:0;padding:14px;border:1px solid rgba(250,245,234,.25)}
.band img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover}
.motto{text-align:center;padding:88px 0 0;font-family:var(--display);font-style:italic;font-size:clamp(24px,2.6vw,32px);color:var(--teal);max-width:26ch;margin:0 auto;line-height:1.3}
/* CTA block */
.cta{padding:96px 0;text-align:center}
.cta h2{font-size:clamp(34px,4vw,54px);margin-bottom:18px}
.cta h2 .arrow{color:var(--coral);font-style:italic}
.cta p{max-width:52ch;margin:0 auto 32px;font-size:18px;color:var(--muted)}
/* footer */
.ftr{background:var(--deep);color:var(--on-deep-soft);padding:72px 0 36px;font-size:14px}
.ftr .grid{display:grid;grid-template-columns:1.2fr 1fr 1.2fr;gap:48px}
.ftr .logo-svg{color:var(--on-deep);height:40px;margin-bottom:18px}
.ftr h4{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--coral-soft);margin:0 0 16px}
.ftr a{color:var(--on-deep);text-decoration:none}.ftr a:hover{text-decoration:underline}
.ftr .links a{display:block;margin-bottom:8px}
.ftr .btn{background:var(--coral-soft);border-color:var(--coral-soft);color:var(--ink)}
.ftr .bottom{display:flex;justify-content:space-between;gap:20px;margin-top:56px;padding-top:24px;border-top:1px solid rgba(250,245,234,.18);font-size:12px;flex-wrap:wrap}
/* page header */
.ph{padding:88px 0 56px;max-width:820px}
.ph h1{font-size:clamp(40px,5vw,64px)}
/* approach */
.pull{font-family:var(--display);font-style:italic;font-size:clamp(26px,3vw,38px);color:var(--ink);line-height:1.25;max-width:30ch;padding:40px 0 40px 32px;border-left:2px solid var(--coral);margin:40px 0 72px}
.loop{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;padding:0 0 88px}
.loop svg{width:100%;height:auto;display:block}
.loop .cap{font-size:16px}
.loop .cap b{font-family:var(--display);font-weight:400;font-style:italic;font-size:24px;color:var(--teal);display:block;margin-bottom:8px}
.before{background:var(--surface);border:1px solid var(--rule);padding:40px 48px;display:grid;grid-template-columns:auto 1fr auto;gap:40px;align-items:center;margin-bottom:88px}
.before h3{margin:0}.before p{margin:0;color:var(--muted)}
.phases{display:grid;grid-template-columns:1fr;border-top:1px solid var(--ink)}
.phase{display:grid;grid-template-columns:120px 1fr 1.6fr;gap:40px;padding:40px 0;border-bottom:1px solid var(--rule)}
.phase .n{font-family:var(--display);font-style:italic;font-size:56px;color:var(--coral);line-height:1}
.phase h3{margin:0}.phase p{margin:0;font-size:16px}
.beyond{margin:88px 0 0;display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center}
.beyond img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover}
/* experience */
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin:56px 0 72px}
.stat{border-top:1px solid var(--ink);padding-top:24px}
.stat .v{font-family:var(--display);font-size:clamp(40px,4.4vw,60px);color:var(--ink);line-height:1;letter-spacing:-.02em}
.stat .v i{font-style:italic;color:var(--coral);font-size:.55em;margin:0 10px}
.stat .l{font-size:14px;color:var(--muted);margin-top:14px}
.proof{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;padding-bottom:88px}
.proof figure{margin:0;padding:14px;border:1px solid var(--rule);background:var(--surface)}
.proof img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover}
.proof figcaption{font-size:13px;color:var(--muted);margin-top:12px;font-style:italic}
.case{background:var(--deep);color:var(--on-deep-soft);padding:64px;display:grid;grid-template-columns:1fr 1.4fr;gap:64px;margin-top:56px}
.case h3{color:var(--on-deep);font-size:clamp(34px,4vw,52px);font-style:italic;font-weight:300}
.case .kicker{color:var(--coral-soft)}
.case p{font-size:16px}
/* about */
.about{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px;align-items:start;padding-bottom:72px}
.about .sticky{position:sticky;top:110px}
.about .portrait::after{inset:18px 18px -18px -18px}
.about .text p{font-size:17px}
.lesson{font-family:var(--display);font-size:clamp(24px,2.6vw,32px);color:var(--ink);line-height:1.3;margin:40px 0;padding-left:28px;border-left:2px solid var(--coral)}
.tl{list-style:none;margin:72px 0 0;padding:0;border-top:1px solid var(--ink)}
.tl li{display:grid;grid-template-columns:200px 1fr;gap:32px;padding:22px 0;border-bottom:1px solid var(--rule);font-size:16px}
.tl b{font-family:var(--display);font-weight:400;font-style:italic;color:var(--teal);font-size:22px}
/* network */
.mapbox{border:1px solid var(--rule);background:var(--surface);padding:24px;margin:48px 0 72px}
.pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-bottom:72px}
.pillars article{border-top:1px solid var(--ink);padding-top:22px}
.pillars h3{font-size:22px}.pillars p{font-size:15px;color:var(--muted)}
.impulsa{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;border:1px solid var(--rule);background:var(--surface);padding:48px;margin-bottom:24px}
.impulsa .badge{font-family:var(--display);font-size:28px;color:var(--ink);border:1px solid var(--ink);padding:18px 28px;display:inline-block}
/* contact */
.contact{display:grid;grid-template-columns:1fr 1fr;gap:72px;padding-bottom:96px;align-items:start}
.cal{background:var(--deep);color:var(--on-deep-soft);padding:48px}
.cal h3{color:var(--on-deep);font-size:30px}
.cal .btn{background:var(--coral-soft);border-color:var(--coral-soft);color:var(--ink);margin-top:12px}
.cal .mail{margin-top:32px;font-size:14px}.cal .mail a{color:var(--on-deep)}
.cform{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.f{display:flex;flex-direction:column;gap:6px;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.f-wide{grid-column:1/-1}
.f input,.f textarea{font:inherit;font-size:16px;text-transform:none;letter-spacing:0;padding:12px 0;border:0;border-bottom:1px solid var(--ink);background:transparent;color:var(--ink);outline:none}
.f textarea{resize:vertical}
.privacy{font-size:12px;color:var(--muted);display:flex;gap:10px;align-items:flex-start;text-transform:none;letter-spacing:0}
/* privacy page */
.doc{max-width:760px;padding:88px 0 120px}
@media(max-width:960px){
.hero,.band .grid,.loop,.beyond,.proof,.case,.about,.impulsa,.contact{grid-template-columns:1fr;gap:40px}
.why-grid,.stats,.pillars{grid-template-columns:1fr}
.ftr .grid{grid-template-columns:1fr}
.before{grid-template-columns:1fr;gap:16px}
.phase{grid-template-columns:70px 1fr}.phase p{grid-column:2}
.tl li{grid-template-columns:1fr;gap:4px}
.nav{display:none;position:absolute;top:84px;left:0;right:0;background:var(--bg);flex-direction:column;padding:20px 32px;border-bottom:1px solid var(--rule)}
.nav.open{display:flex}.burger{display:block}.hdr .right .btn{display:none}
.hero{padding:56px 0}
.portrait{max-width:420px}
.about .sticky{position:static}
}
@media(max-width:600px){.wrap{padding:0 18px}.cform{grid-template-columns:1fr}.case,.cal,.impulsa{padding:32px 24px}}
""" + MAP_CSS + COOKIE_CSS


def header(active):
    return f"""
<header class="hdr"><div class="wrap">
  <a href="index.html" aria-label="VeliD Advisory home">{LOGO_SVG}</a>
  <nav class="nav" aria-label="Main">{nav_links(active)}</nav>
  <div class="right"><span class="lang"><b>EN</b> · NL</span><a class="btn ghost" href="{C.CALENDLY}">{C.CTA}</a><button class="burger" aria-label="Menu" aria-expanded="false">☰</button></div>
</div></header>"""

def cta_block():
    return f"""
<section class="cta"><div class="wrap">
  <h2><span class="arrow">→</span> {C.CTA} <span class="arrow">←</span></h2>
  <p>{C.CTA_SUB}</p>
  <a class="btn" href="{C.CALENDLY}">{C.CTA}</a>
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

def loop_svg():
    # Cuatro nodos en círculo con flechas y retroalimentación al centro
    import math
    cx, cy, r = 220, 220, 150
    pts = []
    for i in range(4):
        a = -math.pi/2 + i*math.pi/2
        pts.append((cx + r*math.cos(a), cy + r*math.sin(a)))
    out = [f'<svg viewBox="0 0 440 440" role="img" aria-label="VeliD loop: analyze, fit, connect, build, feedback and adjust">',
           '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5 0 10z" fill="#C96A50"/></marker></defs>',
           f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#1F3C54" stroke-opacity=".25" stroke-dasharray="3 6"/>']
    for i in range(4):
        a0 = -math.pi/2 + i*math.pi/2 + .32; a1 = a0 + math.pi/2 - .64
        x0, y0 = cx + r*math.cos(a0), cy + r*math.sin(a0); x1, y1 = cx + r*math.cos(a1), cy + r*math.sin(a1)
        out.append(f'<path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 0 1 {x1:.1f} {y1:.1f}" fill="none" stroke="#C96A50" stroke-width="1.5" marker-end="url(#ah)"/>')
    for (x, y), (short, long) in zip(pts, C.LOOP):
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="46" fill="#FFFCF5" stroke="#1F3C54"/>')
        out.append(f'<text x="{x:.1f}" y="{y+6:.1f}" text-anchor="middle" font-family="Fraunces,serif" font-size="20" fill="#1F3C54">{short}</text>')
    out.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="Montserrat,sans-serif" font-size="11" letter-spacing="2" fill="#4A7A69">FEEDBACK</text>')
    out.append(f'<text x="{cx}" y="{cy+14}" text-anchor="middle" font-family="Montserrat,sans-serif" font-size="11" letter-spacing="2" fill="#4A7A69">AND ADJUST</text>')
    out.append('</svg>')
    return "\n".join(out)

def build():
    write(N, "style.css", CSS)
    # HOME
    why = "".join(f'<article><div class="num">0{i+1}</div><h3>{t}</h3><p>{esc(p)}</p></article>' for i, (t, p) in enumerate(C.WHY))
    home = f"""
<section class="wrap hero">
  <div><div class="brand">{C.BRAND}</div><h1>{C.HEADLINE}</h1><p class="lede">{esc(C.HERO_LEAD)}</p>
  <p style="margin-top:32px"><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></p><p class="micro">30 minutes · one strategic conversation · no obligation</p></div>
  <figure class="portrait">{img("portrait")}</figure>
</section>
<hr class="rule">
<section class="wrap why"><span class="kicker">Why VeliD</span><h2>{C.WHY_TITLE}</h2><div class="why-grid">{why}</div></section>
<section class="band"><div class="wrap grid">
  <div><blockquote>{esc(C.QUOTE)}”</blockquote><p>{esc(C.QUOTE_P1)}</p><p>{esc(C.QUOTE_P2)}</p></div>
  <figure>{img("panel")}</figure>
</div></section>
<p class="motto">{esc(C.MOTTO)}</p>
{cta_block()}
"""
    write(N, "index.html", page("index.html", "Home", home))
    # APPROACH
    phases = "".join(f'<div class="phase"><div class="n">0{i+1}</div><h3>{t}</h3><p>{esc(p)}</p></div>' for i, (t, p) in enumerate(C.PHASES))
    approach = f"""
<div class="wrap">
 <div class="ph"><span class="kicker">Approach</span><h1>Better decisions as you grow across borders.</h1><p class="lede">{esc(C.APPROACH_INTRO)}</p></div>
 <p class="pull">{esc(C.APPROACH_PULL)}</p>
 <div class="loop">{loop_svg()}<div class="cap"><b>{C.LOOP_NOTE}</b><p>{C.LOOP[0][1]}. {C.LOOP[1][1]}. Connect and build.</p><p>{C.LOOP_BASE}</p></div></div>
 <div class="before"><h3>{C.BEFORE_TITLE}</h3><p>{C.BEFORE_TEXT}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 <div class="phases">{phases}</div>
 <div class="beyond"><div><span class="kicker">{C.BEYOND_TITLE}</span><h2>Workshops, cultural training and speaking.</h2><p>{esc(C.BEYOND_TEXT)}</p></div>{img("audience")}</div>
</div>
{cta_block()}
"""
    write(N, "approach.html", page("approach.html", "Approach", approach))
    # EXPERIENCE
    stats = "".join(f'<div class="stat"><div class="v">{a}{"<i>→</i>"+b if b else ""}</div><div class="l">{l}</div></div>' for a, b, l in C.STATS)
    exp = f"""
<div class="wrap">
 <div class="ph"><span class="kicker">Experience &amp; Cases</span><h1>{C.EXP_TITLE}</h1><p class="lede">{esc(C.EXP_TEXT)}</p></div>
 <div class="stats">{stats}</div>
 <div class="proof"><figure>{img("certificate")}<figcaption>{esc(C.PHOTOS["certificate"][1])}.</figcaption></figure>
  <div><span class="kicker">Recognition</span><h2>Independent, external proof.</h2><p>The transformation of Holland House Mexico was recognized by the Embassy of the Kingdom of the Netherlands in Mexico.</p></div></div>
 <span class="kicker">{C.CASES_TITLE}</span><h2>{C.CASES_P1}</h2><p class="lede">{esc(C.CASES_P2)}</p><p class="lede"><em>{esc(C.CASES_P3)}</em></p>
 <div class="case"><div><span class="kicker">{C.CASE_KICKER}</span><h3>{C.CASE_NAME}</h3></div><div><p>{esc(C.CASE_P1)}</p><p>{esc(C.CASE_P2)}</p></div></div>
</div>
{cta_block()}
"""
    write(N, "experience.html", page("experience.html", "Experience & Cases", exp))
    # ABOUT
    paras = "".join(f"<p>{esc(p)}</p>" for p in C.ABOUT)
    tl = "".join(f"<li><b>{a}</b><span>{esc(b)}</span></li>" for a, b in C.TIMELINE)
    about = f"""
<div class="wrap">
 <div class="ph"><span class="kicker">About</span><h1>{C.ABOUT_INTRO}</h1></div>
 <div class="about"><div class="sticky"><figure class="portrait">{img("portrait")}</figure></div>
  <div class="text">{paras}<p class="lesson">{esc(C.ABOUT_LESSON)}</p><p>{esc(C.ABOUT_CLOSE)}</p><p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></p></div></div>
 <ul class="tl">{tl}</ul>
</div>
{cta_block()}
"""
    write(N, "about.html", page("about.html", "About", about))
    # NETWORK
    pillars = "".join(f"<article><h3>{t}</h3><p>{esc(p)}</p></article>" for t, p in C.NET_PILLARS)
    net = f"""
<div class="wrap">
 <div class="ph"><span class="kicker">Network</span><h1>In Mexico and beyond, from institutions to individual specialists.</h1><p class="lede">{esc(C.NET_TEXT)}</p></div>
 <div class="mapbox">{MAP_SVG}</div>
 <div class="pillars">{pillars}</div>
 <div class="impulsa"><div><span class="kicker">Member &amp; mentor</span><h2>{esc(C.NET_IMPULSA)}</h2><a href="{C.IMPULSA}">associationimpulsa.com →</a></div><div><a class="badge" href="{C.IMPULSA}" style="text-decoration:none">Association IMPULSA</a></div></div>
 <p class="lede">{esc(C.NET_EXPERT)} <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
</div>
{cta_block()}
"""
    write(N, "network.html", page("network.html", "Network", net))
    # CONTACT
    contact = f"""
<div class="wrap">
 <div class="ph"><span class="kicker">Contact</span><h1>{C.CONTACT_TITLE}</h1></div>
 <div class="contact">
  <div class="cal"><span class="kicker">Step one</span><h3>{C.CONTACT_CTA}</h3><p>{C.CTA_VALUE}</p><a class="btn" href="{C.CALENDLY}">Open the calendar</a>
   <p class="mail">Or write directly: <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p></div>
  <div><h3>{C.CONTACT_ALT}</h3>{form_html()}</div>
 </div>
</div>
"""
    write(N, "contact.html", page("contact.html", "Contact", contact))
    write(N, "privacy.html", page("", "Privacy notice", f'<div class="wrap doc">{privacy_page_body()}</div>'))

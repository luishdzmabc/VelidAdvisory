# Propuesta 3 — "Raíz": cálida, arena y terracota, arcos y formas orgánicas. Cercanía humana, México y sostenibilidad.
import content as C
from common import *

N = 3
FONTS = '<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Montserrat:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">'

CSS = """
:root{--bg:#F6EDE1;--sand:#EFE2CF;--surface:#FFFBF4;--ink:#1F3C54;--body:#43494D;--muted:#6E7579;--teal:#4A7A69;--teal-soft:#A9D3C3;--coral:#C96A50;--coral-soft:#EB937D;--peach:#F5D4C4;--rule:rgba(31,60,84,.14);
--display:'DM Serif Display',Georgia,serif;--text:'Montserrat',system-ui,sans-serif;
--map-land:#5D9382;--map-ink:#1F3C54;--map-bg:#FFFBF4;--map-accent:#C96A50;--map-muted:#6E7579;
--cookie-bg:#FFFBF4;--cookie-fg:#1F3C54;--cookie-line:#EB937D;--cookie-btn:#C96A50;--cookie-btn-fg:#fff;--cookie-radius:18px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--body);font-family:var(--text);font-size:17px;line-height:1.7;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:var(--display);color:var(--ink);font-weight:400;line-height:1.08;margin:0 0 .5em;letter-spacing:-.005em}
h1{font-size:clamp(42px,5.8vw,76px)}h2{font-size:clamp(32px,3.8vw,50px)}h3{font-size:26px}
em,.it{font-style:italic}
p{margin:0 0 1em}a{color:var(--coral)}
.wrap{max-width:1160px;margin:0 auto;padding:0 32px}
.kicker{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--coral);font-weight:600;margin-bottom:18px;display:block}
.btn{display:inline-block;background:var(--coral);color:#fff;text-decoration:none;padding:16px 30px;border-radius:999px;font-weight:600;font-size:15px;transition:.2s;box-shadow:0 10px 24px rgba(201,106,80,.25)}
.btn:hover{background:var(--ink);box-shadow:none}
.btn.soft{background:var(--surface);color:var(--ink);box-shadow:none;border:1px solid var(--rule)}.btn.soft:hover{background:var(--ink);color:#fff}
.lede{font-size:20px;line-height:1.6;max-width:58ch}
/* header */
.hdr{position:sticky;top:0;z-index:40;background:rgba(246,237,225,.9);backdrop-filter:blur(12px)}
.hdr .wrap{display:flex;align-items:center;justify-content:space-between;height:88px;gap:24px}
.logo-svg{height:34px;width:auto;color:var(--ink)}
.nav{display:flex;gap:6px}
.nav-a{text-decoration:none;color:var(--ink);font-size:14px;font-weight:500;padding:8px 14px;border-radius:999px}
.nav-a[aria-current]{background:var(--peach)}
.hdr .right{display:flex;align-items:center;gap:18px}
.lang{font-size:12px;letter-spacing:.14em;color:var(--muted)}.lang b{color:var(--ink);font-weight:600}
.burger{display:none;background:none;border:1px solid var(--rule);width:44px;height:44px;border-radius:50%;font-size:20px;cursor:pointer;color:var(--ink)}
/* hero */
.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:64px;align-items:center;padding:72px 0 96px;position:relative}
.hero .blob{position:absolute;right:-10%;top:-20%;width:60%;aspect-ratio:1;background:radial-gradient(circle at 40% 40%,var(--peach),transparent 65%);z-index:-1;opacity:.9}
.hero .brand{font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:var(--teal);font-weight:600;margin-bottom:22px}
.hero .micro{font-size:13px;color:var(--muted);margin-top:14px}
.arch{margin:0;position:relative}
.arch img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top;border-radius:999px 999px 28px 28px}
.arch::before{content:"";position:absolute;inset:-14px;border:2px solid var(--coral-soft);border-radius:999px 999px 40px 40px;z-index:-1;transform:translate(14px,14px)}
/* why */
.why{padding:96px 0}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}
.why-grid article{background:var(--surface);border-radius:28px;padding:40px 34px;border:1px solid var(--rule)}
.why-grid .glyph{width:56px;height:56px;border-radius:50%;display:grid;place-items:center;margin-bottom:22px;font-family:var(--display);font-size:24px;color:#fff}
.why-grid article:nth-child(1) .glyph{background:var(--teal)}.why-grid article:nth-child(2) .glyph{background:var(--ink)}.why-grid article:nth-child(3) .glyph{background:var(--coral)}
.why-grid h3{font-size:24px}.why-grid p{font-size:15.5px;margin:0}
/* quote */
.quote{background:var(--teal);color:#EAF4EF;padding:112px 0;border-radius:64px 64px 0 0;position:relative;overflow:hidden}
.quote::after{content:"";position:absolute;right:-120px;bottom:-200px;width:520px;height:520px;border-radius:50%;background:rgba(255,255,255,.06)}
.quote .grid{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;position:relative}
.quote blockquote{margin:0 0 32px;font-family:var(--display);font-size:clamp(32px,3.6vw,48px);line-height:1.15;color:#fff}
.quote blockquote i{color:var(--peach)}
.quote p{font-size:16px;color:#EAF4EF}
.quote figure{margin:0}.quote img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:28px 120px 28px 28px}
.motto{background:var(--ink);color:var(--peach);text-align:center;padding:72px 32px;font-family:var(--display);font-size:clamp(24px,2.6vw,34px);line-height:1.3;margin:0}
.motto span{display:block;max-width:28ch;margin:0 auto}
/* cta */
.cta{padding:112px 0}
.cta .box{background:var(--surface);border-radius:40px;padding:72px 48px;text-align:center;border:1px solid var(--rule);max-width:900px;margin:0 auto;position:relative;overflow:hidden}
.cta .box::before{content:"";position:absolute;left:-80px;top:-80px;width:240px;height:240px;border-radius:50%;background:var(--peach);opacity:.7}
.cta h2{font-size:clamp(34px,4.2vw,56px);position:relative}
.cta h2 .arrow{color:var(--coral)}
.cta p{max-width:52ch;margin:0 auto 32px;color:var(--muted);position:relative}
/* footer */
.ftr{background:var(--ink);color:#C8D4DC;padding:72px 0 36px;font-size:14px;border-radius:64px 64px 0 0}
.ftr .grid{display:grid;grid-template-columns:1.2fr 1fr 1.2fr;gap:48px}
.ftr .logo-svg{color:#FAF5EA;height:40px;margin-bottom:18px}
.ftr h4{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--peach);margin:0 0 16px}
.ftr a{color:#FAF5EA;text-decoration:none}.ftr a:hover{text-decoration:underline}
.ftr .links a{display:block;margin-bottom:8px}
.ftr .bottom{display:flex;justify-content:space-between;gap:20px;margin-top:56px;padding-top:24px;border-top:1px solid rgba(250,245,234,.18);font-size:12px;flex-wrap:wrap}
/* page header */
.ph{padding:80px 0 56px;max-width:860px}
/* approach */
.pull{background:var(--peach);border-radius:32px;padding:48px 56px;font-family:var(--display);font-size:clamp(26px,3vw,38px);line-height:1.2;color:var(--ink);margin:0 0 72px}
.loop{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;padding-bottom:88px}
.petals{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.petal{aspect-ratio:1;display:flex;flex-direction:column;justify-content:flex-end;padding:26px;color:#fff;font-family:var(--display);font-size:22px;line-height:1.15}
.petal small{font-family:var(--text);font-size:12px;letter-spacing:.14em;text-transform:uppercase;opacity:.8;margin-bottom:8px;font-weight:600}
.petal:nth-child(1){background:var(--teal);border-radius:120px 24px 24px 24px}
.petal:nth-child(2){background:var(--ink);border-radius:24px 120px 24px 24px}
.petal:nth-child(3){background:#A9A08A;border-radius:24px 24px 24px 120px}
.petal:nth-child(4){background:var(--coral);border-radius:24px 24px 120px 24px}
.loop .cap b{font-family:var(--display);font-weight:400;font-size:28px;color:var(--teal);display:block;margin-bottom:10px}
.before{background:var(--surface);border:1px solid var(--rule);border-radius:32px;padding:44px 48px;display:grid;grid-template-columns:auto 1fr auto;gap:40px;align-items:center;margin-bottom:88px}
.before h3{margin:0}.before p{margin:0;color:var(--muted)}
.phases{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.phase{background:var(--surface);border-radius:28px;padding:40px 34px;border:1px solid var(--rule)}
.phase .n{width:48px;height:48px;border-radius:50%;background:var(--coral);color:#fff;display:grid;place-items:center;font-weight:600;margin-bottom:22px;font-size:14px}
.phase h3{font-size:24px}.phase p{font-size:15.5px;margin:0}
.beyond{margin-top:88px;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.beyond img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:120px 28px 28px 28px}
/* experience */
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin:56px 0 88px}
.stat{background:var(--surface);border-radius:28px;padding:40px 32px;border:1px solid var(--rule)}
.stat .v{font-family:var(--display);font-size:clamp(40px,4.4vw,60px);color:var(--ink);line-height:1}
.stat .v i{color:var(--coral);font-size:.55em;margin:0 10px}
.stat .l{font-size:14px;color:var(--muted);margin-top:14px}
.proof{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;padding-bottom:88px}
.proof figure{margin:0}.proof img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:28px 28px 120px 28px}
.proof figcaption{font-size:13px;color:var(--muted);margin-top:12px}
.case{background:var(--teal);color:#EAF4EF;border-radius:40px;padding:64px;display:grid;grid-template-columns:1fr 1.4fr;gap:64px;margin-top:56px}
.case h3{color:#fff;font-size:clamp(36px,4vw,56px)}.case .kicker{color:var(--peach)}.case p{font-size:16px;color:#EAF4EF}
/* about */
.about{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px;align-items:start;padding-bottom:80px}
.about .arch{position:sticky;top:120px}
.lesson{background:var(--peach);border-radius:28px;padding:36px 40px;font-family:var(--display);font-size:clamp(24px,2.6vw,32px);color:var(--ink);line-height:1.25;margin:40px 0}
.tl{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.tl li{background:var(--surface);border:1px solid var(--rule);border-radius:24px;padding:28px;font-size:15px}
.tl b{font-family:var(--display);font-weight:400;color:var(--coral);display:block;font-size:22px;margin-bottom:8px}
/* network */
.mapbox{background:var(--surface);border:1px solid var(--rule);border-radius:40px;padding:28px;margin:0 0 72px}
.pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:72px}
.pillars article{background:var(--surface);border:1px solid var(--rule);border-radius:28px;padding:36px}
.pillars h3{font-size:22px}.pillars p{font-size:15px;color:var(--muted);margin:0}
.impulsa{display:flex;justify-content:space-between;align-items:center;gap:40px;background:var(--peach);border-radius:32px;padding:48px;margin-bottom:40px;flex-wrap:wrap}
.impulsa h2{font-size:28px;margin:0}
.impulsa .badge{font-family:var(--display);font-size:22px;color:var(--ink);border:2px solid var(--ink);border-radius:999px;padding:14px 28px;text-decoration:none;white-space:nowrap}
/* contact */
.contact{display:grid;grid-template-columns:1fr 1fr;gap:64px;padding-bottom:112px;align-items:start}
.cal{background:var(--teal);color:#EAF4EF;border-radius:40px;padding:48px}
.cal h3{color:#fff;font-size:30px}.cal .kicker{color:var(--peach)}.cal .mail{margin-top:32px;font-size:14px}.cal .mail a{color:#fff}
.cform{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.f{display:flex;flex-direction:column;gap:8px;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600}
.f-wide{grid-column:1/-1}
.f input,.f textarea{font:inherit;font-size:16px;text-transform:none;letter-spacing:0;font-weight:400;padding:14px 18px;border:1px solid var(--rule);border-radius:18px;background:var(--surface);color:var(--ink);outline:none}
.f input:focus,.f textarea:focus{border-color:var(--coral)}
.privacy{font-size:12px;color:var(--muted);display:flex;gap:10px;align-items:flex-start;text-transform:none;letter-spacing:0;font-weight:400}
.doc{max-width:760px;padding:80px 0 120px}
@media(max-width:960px){
.hero,.quote .grid,.loop,.beyond,.proof,.case,.about,.contact{grid-template-columns:1fr;gap:40px}
.why-grid,.stats,.pillars,.phases,.tl{grid-template-columns:1fr}
.ftr .grid{grid-template-columns:1fr}
.before{grid-template-columns:1fr;gap:16px}
.about .arch{position:static;max-width:420px}.arch{max-width:420px}
.nav{display:none;position:absolute;top:88px;left:0;right:0;background:var(--bg);flex-direction:column;padding:20px 32px;border-bottom:1px solid var(--rule)}
.nav.open{display:flex}.burger{display:block}.hdr .right .btn{display:none}
.hero{padding:40px 0 64px}.quote,.ftr{border-radius:36px 36px 0 0}
}
@media(max-width:600px){.wrap{padding:0 18px}.cform{grid-template-columns:1fr}.case,.cal,.impulsa,.pull,.cta .box{padding:32px 24px}}
""" + MAP_CSS + COOKIE_CSS


def header(active):
    return f"""
<header class="hdr"><div class="wrap">
  <a href="index.html" aria-label="VeliD Advisory home">{LOGO_SVG}</a>
  <nav class="nav" aria-label="Main">{nav_links(active)}</nav>
  <div class="right"><span class="lang"><b>EN</b> · NL</span><a class="btn" href="{C.CALENDLY}">{C.CTA}</a><button class="burger" aria-label="Menu" aria-expanded="false">☰</button></div>
</div></header>"""

def cta_block():
    return f"""
<section class="cta"><div class="wrap"><div class="box">
  <h2><span class="arrow">→</span> {C.CTA} <span class="arrow">←</span></h2>
  <p>{C.CTA_SUB}</p>
  <a class="btn" href="{C.CALENDLY}">{C.CTA}</a>
</div></div></section>"""

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
    glyphs = ["◉", "⟡", "❧"]
    why = "".join(f'<article><div class="glyph">{glyphs[i]}</div><h3>{t}</h3><p>{esc(p)}</p></article>' for i, (t, p) in enumerate(C.WHY))
    home = f"""
<section class="wrap hero"><div class="blob"></div>
  <div><div class="brand">{C.BRAND} · {C.TAGLINE}</div><h1>Helping companies build international growth <em>that lasts.</em></h1><p class="lede">{esc(C.HERO_LEAD)}</p>
  <p style="margin-top:32px"><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></p><p class="micro">30 minutes · one strategic conversation · no obligation</p></div>
  <figure class="arch">{img("portrait")}</figure>
</section>
<section class="wrap why"><span class="kicker">Why VeliD</span><h2>{C.WHY_TITLE}</h2><div class="why-grid">{why}</div></section>
<section class="quote"><div class="wrap grid">
  <div><blockquote>“I don't believe growth and sustainability are <i>separate questions.</i>”</blockquote><p>{esc(C.QUOTE_P1)}</p><p>{esc(C.QUOTE_P2)}</p></div>
  <figure>{img("panel")}</figure>
</div></section>
<p class="motto"><span>{esc(C.MOTTO)}</span></p>
{cta_block()}
"""
    write(N, "index.html", page("index.html", "Home", home))
    petals = "".join(f'<div class="petal"><small>Step {i+1}</small>{esc(l)}</div>' for i, (s, l) in enumerate(C.LOOP))
    phases = "".join(f'<div class="phase"><div class="n">0{i+1}</div><h3>{t}</h3><p>{esc(p)}</p></div>' for i, (t, p) in enumerate(C.PHASES))
    approach = f"""
<div class="wrap">
 <div class="ph"><span class="kicker">Approach</span><h1>Better decisions as you grow <em>across borders.</em></h1><p class="lede">{esc(C.APPROACH_INTRO)}</p></div>
 <p class="pull">{esc(C.APPROACH_PULL)}</p>
 <div class="loop"><div class="petals">{petals}</div><div class="cap"><b>{C.LOOP_NOTE}</b><p>We analyze the current proposition, determine if, where and in what way Mexico is a fit, then connect and build.</p><p>{C.LOOP_BASE}</p></div></div>
 <div class="before"><h3>{C.BEFORE_TITLE}</h3><p>{C.BEFORE_TEXT}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 <span class="kicker">How we work together</span><h2>Three phases, <em>one conversation at a time.</em></h2>
 <div class="phases">{phases}</div>
 <div class="beyond"><div><span class="kicker">{C.BEYOND_TITLE}</span><h2>Workshops, cultural training and speaking.</h2><p>{esc(C.BEYOND_TEXT)}</p></div>{img("audience")}</div>
</div>
{cta_block()}
"""
    write(N, "approach.html", page("approach.html", "Approach", approach))
    stats = "".join(f'<div class="stat"><div class="v">{a}{"<i>→</i>"+b if b else ""}</div><div class="l">{l}</div></div>' for a, b, l in C.STATS)
    exp = f"""
<div class="wrap">
 <div class="ph"><span class="kicker">Experience &amp; Cases</span><h1>Experience you can <em>measure.</em></h1><p class="lede">{esc(C.EXP_TEXT)}</p></div>
 <div class="stats">{stats}</div>
 <div class="proof"><figure>{img("certificate")}<figcaption>{esc(C.PHOTOS["certificate"][1])}.</figcaption></figure>
  <div><span class="kicker">Recognition</span><h2>Independent, external proof.</h2><p>The transformation of Holland House Mexico was recognized by the Embassy of the Kingdom of the Netherlands in Mexico.</p></div></div>
 <span class="kicker">{C.CASES_TITLE}</span><h2>{C.CASES_P1}</h2><p class="lede">{esc(C.CASES_P2)}</p><p class="lede"><em>{esc(C.CASES_P3)}</em></p>
 <div class="case"><div><span class="kicker">{C.CASE_KICKER}</span><h3>{C.CASE_NAME}</h3></div><div><p>{esc(C.CASE_P1)}</p><p>{esc(C.CASE_P2)}</p></div></div>
</div>
{cta_block()}
"""
    write(N, "experience.html", page("experience.html", "Experience & Cases", exp))
    paras = "".join(f"<p>{esc(p)}</p>" for p in C.ABOUT)
    tl = "".join(f"<li><b>{a}</b>{esc(b)}</li>" for a, b in C.TIMELINE)
    about = f"""
<div class="wrap">
 <div class="ph"><span class="kicker">About</span><h1>I'm Carin Verbree. <em>Founder of VeliD Advisory.</em></h1></div>
 <div class="about"><figure class="arch">{img("portrait")}</figure>
  <div>{paras}<p class="lesson">{esc(C.ABOUT_LESSON)}</p><p>{esc(C.ABOUT_CLOSE)}</p><p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></p></div></div>
 <span class="kicker">The road so far</span><ul class="tl">{tl}</ul>
</div>
{cta_block()}
"""
    write(N, "about.html", page("about.html", "About", about))
    pillars = "".join(f"<article><h3>{t}</h3><p>{esc(p)}</p></article>" for t, p in C.NET_PILLARS)
    net = f"""
<div class="wrap">
 <div class="ph"><span class="kicker">Network</span><h1>In Mexico and beyond, <em>from institutions to individual specialists.</em></h1><p class="lede">{esc(C.NET_TEXT)}</p></div>
 <div class="mapbox">{MAP_SVG}</div>
 <div class="pillars">{pillars}</div>
 <div class="impulsa"><h2>{esc(C.NET_IMPULSA)}</h2><a class="badge" href="{C.IMPULSA}">Association IMPULSA</a></div>
 <p class="lede">{esc(C.NET_EXPERT)} <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
</div>
{cta_block()}
"""
    write(N, "network.html", page("network.html", "Network", net))
    contact = f"""
<div class="wrap">
 <div class="ph"><span class="kicker">Contact</span><h1>Wondering what VeliD Advisory could bring to your business? <em>Let's set up a conversation.</em></h1></div>
 <div class="contact">
  <div class="cal"><span class="kicker">Step one</span><h3>{C.CONTACT_CTA}</h3><p>{C.CTA_VALUE}</p><a class="btn" href="{C.CALENDLY}">Open the calendar</a>
   <p class="mail">Or write directly: <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p></div>
  <div><h3>{C.CONTACT_ALT}</h3>{form_html()}</div>
 </div>
</div>
"""
    write(N, "contact.html", page("contact.html", "Contact", contact))
    write(N, "privacy.html", page("", "Privacy notice", f'<div class="wrap doc">{privacy_page_body()}</div>'))

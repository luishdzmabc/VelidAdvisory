# Propuesta 6 · Brújula (brand): banda hero en navy con logo invertido, cuerpo en crema con tarjetas blancas, botones redondeados.
import content as C
from brand import *

N = 6
CSS = TOKENS + ":root{--r-btn:999px;--r-field:12px;--cookie-radius:999px}" + BASE + """
.hero{padding:96px 0 104px;position:relative;overflow:hidden}
.hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:72px;align-items:center;position:relative}
.hero::after{content:"";position:absolute;right:-220px;top:-220px;width:620px;height:620px;border-radius:50%;background:rgba(93,147,130,.14)}
.hero .micro{font-size:13px;margin-top:14px;color:var(--navy-soft)}
.hero figure{margin:0;padding:14px;border:1px solid rgba(250,245,234,.25);border-radius:28px;position:relative;z-index:1}
.hero img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top;border-radius:18px}
.sec{padding:104px 0}
.sec-head{display:flex;align-items:baseline;justify-content:space-between;gap:32px;flex-wrap:wrap;margin-bottom:48px}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.card{background:var(--white);border:1px solid var(--rule);border-radius:24px;padding:40px 34px}
.card .num{font-family:var(--display);font-weight:600;font-size:13px;letter-spacing:.14em;color:var(--teal);margin-bottom:22px;display:flex;align-items:center;gap:10px}
.card .num::before{content:"";width:22px;height:2px;background:var(--teal)}
.card h3{color:var(--navy);font-size:21px}.card p{font-size:15.5px;margin:0}
.band{padding:112px 0}
.band .grid{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.band .quote{font-size:clamp(28px,3.4vw,42px);margin-bottom:32px}
.band figure{margin:0;border-radius:28px;overflow:hidden}.band img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover}
.motto{text-align:center;padding:96px 32px;max-width:30ch;margin:0 auto}
.strip{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin:0 0 0}
.strip .stat{background:var(--white);border:1px solid var(--rule);border-radius:24px;padding:36px 32px}
.stat .v{font-family:var(--display);font-weight:600;font-size:clamp(38px,4.4vw,58px);color:var(--navy);line-height:1;letter-spacing:-.03em}
.stat .v i{font-style:normal;color:var(--coral);font-size:.5em;margin:0 10px;vertical-align:middle}
.stat .l{font-size:14px;color:var(--muted);margin-top:14px}
.pull{max-width:32ch;margin:0 0 72px;padding:32px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.track{display:grid;grid-template-columns:repeat(4,1fr);position:relative;margin-bottom:24px}
.track::before{content:"";position:absolute;left:12%;right:12%;top:30px;height:2px;background:var(--teal);opacity:.5}
.track .st{text-align:center;padding:0 16px}
.track .dot{width:60px;height:60px;border-radius:50%;background:var(--cream);border:2px solid var(--teal);display:grid;place-items:center;margin:0 auto 20px;font-family:var(--display);font-weight:600;color:var(--teal);position:relative}
.track h3{font-size:18px;color:var(--navy)}.track p{font-size:14px;color:var(--muted);margin:0}
.loopnote{text-align:center;margin:0 auto 96px;max-width:48ch}
.before{background:var(--white);border:1px solid var(--rule);border-radius:28px;padding:44px 48px;display:grid;grid-template-columns:auto 1fr auto;gap:40px;align-items:center;margin-bottom:96px}
.before h3{margin:0;color:var(--navy)}.before p{margin:0;color:var(--muted)}
.phases{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.phase{background:var(--white);border-radius:24px;padding:40px 36px;border:1px solid var(--rule)}
.phase .n{font-family:var(--display);font-weight:600;font-size:13px;letter-spacing:.14em;color:var(--teal);margin-bottom:22px}
.phase h3{color:var(--navy)}.phase p{font-size:15.5px;margin:0}
.sect{padding:96px 0 0}
.beyond{margin-top:96px;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.beyond img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:28px}
.proof{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;padding:96px 0}
.proof figure{margin:0;border-radius:28px;overflow:hidden}.proof img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover}
.proof figcaption{padding:14px 4px 0}
.case{border-radius:32px;padding:64px;display:grid;grid-template-columns:1fr 1.5fr;gap:64px;margin-top:56px}
.case h3{font-size:clamp(34px,4vw,56px);color:var(--cream)}.case p{font-size:16px}
.about{display:grid;grid-template-columns:.85fr 1.15fr;gap:80px;align-items:start;padding-bottom:96px}
.about figure{margin:0;border-radius:32px;overflow:hidden;position:sticky;top:120px}
.about img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top}
.lesson{margin:48px 0;padding:36px;background:var(--white);border:1px solid var(--rule);border-radius:24px;border-left:4px solid var(--coral)}
.tl{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.tl li{background:var(--white);border:1px solid var(--rule);border-radius:20px;padding:28px;font-size:15px}
.tl b{font-family:var(--display);font-weight:600;color:var(--teal);display:block;font-size:13px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:10px}
.mapbox{border-radius:32px;border:1px solid var(--rule);background:var(--white);padding:24px;margin:0 0 72px}
.pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:56px}
.pillars article{background:var(--white);border:1px solid var(--rule);border-radius:24px;padding:36px}
.pillars h3{font-size:20px;color:var(--navy)}.pillars p{font-size:15px;color:var(--muted);margin:0}
.impulsa{display:flex;justify-content:space-between;align-items:center;gap:40px;border-radius:28px;padding:48px;margin:56px 0 40px;flex-wrap:wrap}
.impulsa h2{font-size:26px;margin:0}
.impulsa .badge{font-family:var(--display);font-weight:600;color:var(--navy);background:var(--cream);border-radius:999px;padding:16px 28px;text-decoration:none;white-space:nowrap}
.contact{display:grid;grid-template-columns:1fr 1fr;gap:72px;padding-bottom:120px;align-items:start}
.cal{border-radius:32px;padding:48px}.cal h3{font-size:28px}.cal .mail{margin-top:32px;font-size:14px}
@media(max-width:960px){
.hero .wrap,.band .grid,.beyond,.proof,.case,.about,.contact{grid-template-columns:1fr;gap:40px}
.cards,.strip,.pillars,.phases,.tl{grid-template-columns:1fr}
.track{grid-template-columns:1fr 1fr;row-gap:32px}.track::before{display:none}
.before{grid-template-columns:1fr;gap:16px}
.about figure{position:static;max-width:420px}.hero figure{max-width:420px}
.hero{padding:64px 0 72px}.sec{padding:72px 0}
}
@media(max-width:600px){.case,.cal,.impulsa{padding:32px 24px}}
"""

def pg(active, title, main): return page(N, active, title, main, hdr_btn="btn")

def build():
    write(N, "style.css", CSS)
    home = f"""
<section class="hero on-navy"><div class="wrap">
  <div><span class="label">{C.BRAND} · {C.TAGLINE}</span><h1>{C.HEADLINE}</h1><p class="lede">{esc(C.HERO_LEAD)}</p>
  <p style="margin-top:32px"><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></p><p class="micro">30 minutes. One strategic conversation. No obligation.</p></div>
  <figure>{img("portrait")}</figure>
</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><div><span class="label">{C.THREE_REASONS}</span><h2 style="margin:0">{C.WHY_TITLE}</h2></div></div>
 <div class="cards">{why_items('<article class="card">', '</article>')}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="label">Experience you can measure</span>{stats_html("strip")}</div></section>
<section class="band on-navy"><div class="wrap grid">
  <div><p class="quote">“{esc(C.QUOTE)}”</p><p>{esc(C.QUOTE_P1)}</p><p>{esc(C.QUOTE_P2)}</p></div>
  <figure>{img("signing")}</figure>
</div></section>
<p class="motto quote">{esc(C.MOTTO)}</p>
{cta_block(btn="btn accent")}
"""
    write(N, "index.html", pg("index.html", "Home", home))
    track = "".join(f'<div class="st"><div class="dot">0{i+1}</div><h3>{s}</h3><p>{esc(l)}</p></div>' for i, (s, l) in enumerate(C.LOOP))
    approach = f"""
<div class="wrap">
 <div class="ph"><span class="label">Approach</span><h1>Better decisions as you grow across borders</h1><p class="lede">{esc(C.APPROACH_INTRO)}</p></div>
 <p class="pull quote">{esc(C.APPROACH_PULL)}</p>
 <div class="track">{track}</div>
 <p class="loopnote"><span class="callout">↻ {C.LOOP_NOTE}</span><br><span class="caption">{C.LOOP_BASE}</span></p>
 <div class="before"><h3>{C.BEFORE_TITLE}</h3><p>{C.BEFORE_TEXT}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 <span class="label">The process</span><h2>How we work together</h2>{phases_html()}
 <div class="sect"><span class="label">Areas of expertise</span><h2>What VeliD Advisory does</h2><p class="lede" style="margin-bottom:40px">{esc(C.AREAS_INTRO)}</p>{areas_html()}</div>
 <div class="beyond"><div><span class="label">{C.BEYOND_TITLE}</span><h2>Workshops, cultural training and speaking sessions</h2><p>{esc(C.BEYOND_TEXT)}</p></div>{img("audience")}</div>
</div>
{cta_block(btn="btn accent")}
"""
    write(N, "approach.html", pg("approach.html", "Approach", approach))
    exp = f"""
<div class="wrap">
 <div class="ph"><span class="label">Experience &amp; Cases</span><h1>{C.EXP_TITLE}</h1><p class="lede">{esc(C.EXP_TEXT)}</p></div>
 {stats_html("strip")}
 <div class="proof"><figure>{img("certificate")}<figcaption class="caption">{esc(C.PHOTOS["certificate"][1])}.</figcaption></figure>
  <div><span class="label">Recognition</span><h2>{C.RECOG}</h2><p>{esc(C.TRACK_NOTE)}</p></div></div>
 <span class="label">{C.CASES_TITLE}</span><h2>{C.CASES_P1}</h2><p class="lede">{esc(C.CASES_P2)}</p><p class="lede">{esc(C.CASES_P3)}</p>
 <div class="case on-navy"><div><span class="label">{C.CASE_KICKER}</span><h3>{C.CASE_NAME}</h3></div><div><p>{esc(C.CASE_P1)}</p><p>{esc(C.CASE_P2)}</p></div></div>
</div>
{cta_block(btn="btn accent")}
"""
    write(N, "experience.html", pg("experience.html", "Experience & Cases", exp))
    about = f"""
<div class="wrap">
 <div class="ph"><span class="label">About</span><h1>{C.ABOUT_INTRO}</h1></div>
 <div class="about"><figure>{img("portrait")}</figure>
  <div>{"".join(f"<p>{esc(p)}</p>" for p in C.ABOUT)}<p class="lesson callout">{esc(C.ABOUT_LESSON)}</p><p>{esc(C.ABOUT_CLOSE)}</p><p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></p></div></div>
 <span class="label">The road so far</span>{timeline_html()}
</div>
{cta_block(btn="btn accent")}
"""
    write(N, "about.html", pg("about.html", "About", about))
    net = f"""
<div class="wrap">
 <div class="ph"><span class="label">Network</span><h1>A network in Mexico and beyond</h1><p class="lede">{esc(C.NET_TEXT)}</p></div>
 <div class="mapbox">{MAP_SVG}</div>
 {pillars_html()}
 <p class="lede">{esc(C.NET_COLLAB)}</p>
 <div class="impulsa on-navy"><h2>{esc(C.NET_IMPULSA)}</h2><a class="badge" href="{C.IMPULSA}">Association IMPULSA ↗</a></div>
 <p class="lede">{esc(C.NET_EXPERT)} <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
</div>
{cta_block(btn="btn accent")}
"""
    write(N, "network.html", pg("network.html", "Network", net))
    contact = f"""
<div class="wrap">
 <div class="ph"><span class="label">Contact</span><h1>{C.CONTACT_TITLE}</h1></div>
 <div class="contact">
  <div class="cal on-navy"><span class="label">Step one</span><h3>{C.CONTACT_CTA}</h3><p>{C.CTA_VALUE}</p><a class="btn" href="{C.CALENDLY}">Open the calendar ↗</a><p class="mail">Or write directly: <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p></div>
  <div><h3 style="color:var(--navy)">{C.CONTACT_ALT}</h3>{form_html()}</div>
 </div>
</div>
"""
    write(N, "contact.html", pg("contact.html", "Contact", contact))
    privacy(N, pg)

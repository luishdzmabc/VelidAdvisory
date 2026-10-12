# Propuesta 7 · Raíz (brand): crema con formas orgánicas, arco en el retrato, tarjetas redondeadas, bloques teal y navy; coral solo en el CTA.
import content as C
from brand import *

N = 7
CSS = TOKENS + ":root{--r-btn:999px;--r-field:16px;--cookie-radius:18px}" + BASE + """
.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:64px;align-items:center;padding:72px 0 96px;position:relative}
.hero .blob{position:absolute;right:-10%;top:-20%;width:60%;aspect-ratio:1;background:radial-gradient(circle at 40% 40%,var(--teal-tint),transparent 65%);z-index:-1}
.hero .micro{font-size:13px;color:var(--muted);margin-top:14px}
.arch{margin:0;position:relative}
.arch img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top;border-radius:999px 999px 28px 28px}
.arch::before{content:"";position:absolute;inset:-14px;border:2px solid var(--teal);border-radius:999px 999px 40px 40px;z-index:-1;transform:translate(14px,14px);opacity:.6}
.why{padding:96px 0}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:48px}
.why-grid article{background:var(--white);border-radius:28px;padding:40px 34px;border:1px solid var(--rule)}
.why-grid .num{width:48px;height:48px;border-radius:50%;display:grid;place-items:center;margin-bottom:22px;font-family:var(--display);font-weight:600;font-size:13px;color:#fff;background:var(--teal)}
.why-grid article:nth-child(2) .num{background:var(--navy)}
.why-grid h3{color:var(--navy);font-size:22px}.why-grid p{font-size:15.5px;margin:0}
.band{background:var(--teal);color:#EAF4EF;padding:112px 0;border-radius:64px 64px 0 0;position:relative;overflow:hidden}
.band::after{content:"";position:absolute;right:-120px;bottom:-200px;width:520px;height:520px;border-radius:50%;background:rgba(255,255,255,.07)}
.band .grid{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;position:relative}
.band .quote{color:#fff;font-size:clamp(28px,3.4vw,42px);margin-bottom:32px}
.band p{font-size:16px}
.band figure{margin:0}.band img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:28px 120px 28px 28px}
.motto{padding:72px 32px;text-align:center;margin:0}.motto .quote{color:#A9D3C3;max-width:30ch;margin:0 auto}
.cta .box{background:var(--white);border-radius:40px;padding:72px 48px;border:1px solid var(--rule);max-width:900px;margin:0 auto;position:relative;overflow:hidden}
.cta .box::before{content:"";position:absolute;left:-80px;top:-80px;width:240px;height:240px;border-radius:50%;background:var(--teal-tint)}
.cta .box > *{position:relative}
.ftr{border-radius:64px 64px 0 0}
.pull{background:var(--teal-tint);border-radius:32px;padding:48px 56px;margin:0 0 72px}
.loop{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;padding-bottom:88px}
.petals{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.petal{aspect-ratio:1;display:flex;flex-direction:column;justify-content:flex-end;padding:26px;color:#fff;font-family:var(--display);font-weight:600;font-size:20px;line-height:1.2}
.petal small{font-family:var(--display);font-size:12px;letter-spacing:.14em;text-transform:uppercase;opacity:.8;margin-bottom:8px}
.petal:nth-child(1){background:var(--teal);border-radius:120px 24px 24px 24px}
.petal:nth-child(2){background:var(--navy);border-radius:24px 120px 24px 24px}
.petal:nth-child(3){background:var(--navy-soft);color:var(--navy);border-radius:24px 24px 24px 120px}
.petal:nth-child(4){background:var(--coral);color:var(--navy);border-radius:24px 24px 120px 24px}
.before{background:var(--white);border:1px solid var(--rule);border-radius:32px;padding:44px 48px;display:grid;grid-template-columns:auto 1fr auto;gap:40px;align-items:center;margin-bottom:88px}
.before h3{margin:0;color:var(--navy)}.before p{margin:0;color:var(--muted)}
.phases{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.phase{background:var(--white);border-radius:28px;padding:40px 34px;border:1px solid var(--rule)}
.phase .n{width:44px;height:44px;border-radius:50%;background:var(--teal);color:#fff;display:grid;place-items:center;font-family:var(--display);font-weight:600;margin-bottom:22px;font-size:13px}
.phase h3{color:var(--navy)}.phase p{font-size:15.5px;margin:0}
.sect{padding:88px 0 0}
.beyond{margin-top:88px;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.beyond img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:120px 28px 28px 28px}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin:56px 0 88px}
.stat{background:var(--white);border-radius:28px;padding:40px 32px;border:1px solid var(--rule)}
.stat .v{font-family:var(--display);font-weight:600;font-size:clamp(38px,4.4vw,58px);color:var(--navy);line-height:1;letter-spacing:-.03em}
.stat .v i{font-style:normal;color:var(--coral);font-size:.5em;margin:0 10px;vertical-align:middle}
.stat .l{font-size:14px;color:var(--muted);margin-top:14px}
.proof{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;padding-bottom:88px}
.proof figure{margin:0}.proof img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:28px 28px 120px 28px}
.proof figcaption{margin-top:12px}
.case{background:var(--teal);color:#EAF4EF;border-radius:40px;padding:64px;display:grid;grid-template-columns:1fr 1.4fr;gap:64px;margin-top:56px}
.case h3{color:#fff;font-size:clamp(34px,4vw,56px)}.case .label{color:#E6F0EC}.case p{font-size:16px}
.about{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px;align-items:start;padding-bottom:80px}
.about .arch{position:sticky;top:120px}
.lesson{background:var(--teal-tint);border-radius:28px;padding:36px 40px;margin:40px 0}
.tl{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.tl li{background:var(--white);border:1px solid var(--rule);border-radius:24px;padding:28px;font-size:15px}
.tl b{font-family:var(--display);font-weight:600;color:var(--teal);display:block;font-size:13px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:8px}
.mapbox{background:var(--white);border:1px solid var(--rule);border-radius:40px;padding:28px;margin:0 0 72px}
.pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:56px}
.pillars article{background:var(--white);border:1px solid var(--rule);border-radius:28px;padding:36px}
.pillars h3{font-size:20px;color:var(--navy)}.pillars p{font-size:15px;color:var(--muted);margin:0}
.impulsa{display:flex;justify-content:space-between;align-items:center;gap:40px;background:var(--teal-tint);border-radius:32px;padding:48px;margin:56px 0 40px;flex-wrap:wrap}
.impulsa h2{font-size:26px;margin:0}
.impulsa .badge{font-family:var(--display);font-weight:600;color:var(--navy);border:2px solid var(--navy);border-radius:999px;padding:14px 28px;text-decoration:none;white-space:nowrap}
.contact{display:grid;grid-template-columns:1fr 1fr;gap:64px;padding-bottom:112px;align-items:start}
.cal{background:var(--teal);color:#EAF4EF;border-radius:40px;padding:48px}
.cal h3{color:#fff;font-size:28px}.cal .label{color:#E6F0EC}.cal .mail{margin-top:32px;font-size:14px}.cal a{color:#fff}
.cal .btn{background:var(--cream);border-color:var(--cream);color:var(--navy)}
@media(max-width:960px){
.hero,.band .grid,.loop,.beyond,.proof,.case,.about,.contact{grid-template-columns:1fr;gap:40px}
.why-grid,.stats,.pillars,.phases,.tl{grid-template-columns:1fr}
.before{grid-template-columns:1fr;gap:16px}
.about .arch{position:static}.arch{max-width:420px}
.hero{padding:40px 0 64px}.band,.ftr{border-radius:36px 36px 0 0}
}
@media(max-width:600px){.case,.cal,.impulsa,.pull,.cta .box{padding:32px 24px}}
"""

def pg(active, title, main): return page(N, active, title, main, hdr_btn="btn accent")

def cta7():
    return f"""
<section class="cta"><div class="wrap"><div class="box">
  <h2><span class="arrow">→</span> {C.CTA} <span class="arrow">←</span></h2>
  <p>{C.CTA_SUB}</p>
  <a class="btn accent" href="{C.CALENDLY}">{C.CTA}</a>
  <p class="small">30 minutes. One strategic conversation. No obligation.</p>
</div></div></section>"""

def build():
    write(N, "style.css", CSS)
    home = f"""
<section class="wrap hero"><div class="blob"></div>
  <div><span class="label">{C.BRAND} · {C.TAGLINE}</span><h1>Helping companies build international growth <span class="key">that lasts.</span></h1><p class="lede">{esc(C.HERO_LEAD)}</p>
  <p style="margin-top:32px"><a class="btn accent" href="{C.CALENDLY}">{C.CTA}</a></p><p class="micro">30 minutes. One strategic conversation. No obligation.</p></div>
  <figure class="arch">{img("portrait")}</figure>
</section>
<section class="wrap why"><span class="label">{C.THREE_REASONS}</span><h2>{C.WHY_TITLE}</h2><div class="why-grid">{why_items("<article>", "</article>")}</div></section>
<section class="band"><div class="wrap grid">
  <div><p class="quote">“{esc(C.QUOTE)}”</p><p>{esc(C.QUOTE_P1)}</p><p>{esc(C.QUOTE_P2)}</p></div>
  <figure>{img("panel")}</figure>
</div></section>
<div class="motto on-navy"><p class="quote">{esc(C.MOTTO)}</p></div>
{cta7()}
"""
    write(N, "index.html", pg("index.html", "Home", home))
    petals = "".join(f'<div class="petal"><small>Step {i+1}</small>{esc(l)}</div>' for i, (s, l) in enumerate(C.LOOP))
    approach = f"""
<div class="wrap">
 <div class="ph"><span class="label">Approach</span><h1>Better decisions as you grow across borders</h1><p class="lede">{esc(C.APPROACH_INTRO)}</p></div>
 <div class="pull"><p class="quote">{esc(C.APPROACH_PULL)}</p></div>
 <div class="loop"><div class="petals">{petals}</div><div><p class="callout">{C.LOOP_NOTE}</p><p>We analyze the current proposition, determine if, where and in what way Mexico is a fit, then connect and build.</p><p>{C.LOOP_BASE}</p></div></div>
 <div class="before"><h3>{C.BEFORE_TITLE}</h3><p>{C.BEFORE_TEXT}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 <span class="label">The process</span><h2>How we work together</h2>{phases_html()}
 <div class="sect"><span class="label">Areas of expertise</span><h2>What VeliD Advisory does</h2><p class="lede" style="margin-bottom:40px">{esc(C.AREAS_INTRO)}</p>{areas_html()}</div>
 <div class="beyond"><div><span class="label">{C.BEYOND_TITLE}</span><h2>Workshops, cultural training and speaking sessions</h2><p>{esc(C.BEYOND_TEXT)}</p></div>{img("audience")}</div>
</div>
{cta7()}
"""
    write(N, "approach.html", pg("approach.html", "Approach", approach))
    exp = f"""
<div class="wrap">
 <div class="ph"><span class="label">Experience &amp; Cases</span><h1>{C.EXP_TITLE}</h1><p class="lede">{esc(C.EXP_TEXT)}</p></div>
 {stats_html()}
 <div class="proof"><figure>{img("certificate")}<figcaption class="caption">{esc(C.PHOTOS["certificate"][1])}.</figcaption></figure>
  <div><span class="label">Recognition</span><h2>{C.RECOG}</h2><p>{esc(C.TRACK_NOTE)}</p></div></div>
 <span class="label">{C.CASES_TITLE}</span><h2>{C.CASES_P1}</h2><p class="lede">{esc(C.CASES_P2)}</p><p class="lede">{esc(C.CASES_P3)}</p>
 <div class="case"><div><span class="label">{C.CASE_KICKER}</span><h3>{C.CASE_NAME}</h3></div><div><p>{esc(C.CASE_P1)}</p><p>{esc(C.CASE_P2)}</p></div></div>
</div>
{cta7()}
"""
    write(N, "experience.html", pg("experience.html", "Experience & Cases", exp))
    about = f"""
<div class="wrap">
 <div class="ph"><span class="label">About</span><h1>{C.ABOUT_INTRO}</h1></div>
 <div class="about"><figure class="arch">{img("portrait")}</figure>
  <div>{"".join(f"<p>{esc(p)}</p>" for p in C.ABOUT)}<p class="lesson callout">{esc(C.ABOUT_LESSON)}</p><p>{esc(C.ABOUT_CLOSE)}</p><p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></p></div></div>
 <span class="label">The road so far</span>{timeline_html()}
</div>
{cta7()}
"""
    write(N, "about.html", pg("about.html", "About", about))
    net = f"""
<div class="wrap">
 <div class="ph"><span class="label">Network</span><h1>A network in Mexico and beyond, from institutions to individual specialists</h1><p class="lede">{esc(C.NET_TEXT)}</p></div>
 <div class="mapbox">{MAP_SVG}</div>
 {pillars_html()}
 <p class="lede">{esc(C.NET_COLLAB)}</p>
 <div class="impulsa"><h2>{esc(C.NET_IMPULSA)}</h2><a class="badge" href="{C.IMPULSA}">Association IMPULSA</a></div>
 <p class="lede">{esc(C.NET_EXPERT)} <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
</div>
{cta7()}
"""
    write(N, "network.html", pg("network.html", "Network", net))
    contact = f"""
<div class="wrap">
 <div class="ph"><span class="label">Contact</span><h1>{C.CONTACT_TITLE}</h1></div>
 <div class="contact">
  <div class="cal"><span class="label">Step one</span><h3>{C.CONTACT_CTA}</h3><p>{C.CTA_VALUE}</p><a class="btn" href="{C.CALENDLY}">Open the calendar</a><p class="mail">Or write directly: <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p></div>
  <div><h3 style="color:var(--navy)">{C.CONTACT_ALT}</h3>{form_html()}</div>
 </div>
</div>
"""
    write(N, "contact.html", pg("contact.html", "Contact", contact))
    privacy(N, pg)

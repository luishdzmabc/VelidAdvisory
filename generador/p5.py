# Propuesta 5 · Horizonte (brand): editorial en crema, Poppins/Montserrat, filetes finos, retrato con marco coral.
import content as C
from brand import *

N = 5
CSS = TOKENS + BASE + """
.hero{display:grid;grid-template-columns:1.15fr .85fr;gap:72px;align-items:center;padding:96px 0 88px}
.hero .micro{font-size:13px;color:var(--muted);margin-top:14px}
.portrait{position:relative;margin:0}
.portrait img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top}
.portrait::after{content:"";position:absolute;inset:18px -18px -18px 18px;border:1px solid var(--coral);z-index:-1}
.rule{border:0;border-top:1px solid var(--navy);margin:0}
.why{padding:96px 0}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:48px;margin-top:48px}
.why-grid article{border-top:1px solid var(--navy);padding-top:28px}
.why-grid .num{font-family:var(--display);font-weight:600;font-size:14px;letter-spacing:.16em;color:var(--teal);margin-bottom:18px}
.why-grid h3{color:var(--navy);font-size:22px}.why-grid p{font-size:15.5px}
.band{padding:104px 0}
.band .grid{display:grid;grid-template-columns:1.1fr .9fr;gap:72px;align-items:center}
.band .quote{font-size:clamp(28px,3.2vw,40px);margin-bottom:32px}
.band p{font-size:16px}
.band figure{margin:0;padding:14px;border:1px solid rgba(250,245,234,.25)}
.band img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover}
.motto{text-align:center;padding:88px 32px 0;max-width:30ch;margin:0 auto}
.pull{padding:36px 0 36px 32px;border-left:2px solid var(--teal);margin:40px 0 72px;max-width:34ch}
.loop{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;padding:0 0 88px}
.loop svg{width:100%;height:auto;display:block}
.loop .cap p{font-size:16px}
.before{background:var(--white);border:1px solid var(--rule);padding:40px 48px;display:grid;grid-template-columns:auto 1fr auto;gap:40px;align-items:center;margin:0 0 88px}
.before h3{margin:0;color:var(--navy)}.before p{margin:0;color:var(--muted)}
.phases{border-top:1px solid var(--navy)}
.phase{display:grid;grid-template-columns:120px 1fr 1.6fr;gap:40px;padding:40px 0;border-bottom:1px solid var(--rule)}
.phase .n{font-family:var(--display);font-weight:600;font-size:40px;color:var(--teal);line-height:1}
.phase h3{margin:0;color:var(--navy)}.phase p{margin:0;font-size:16px}
.sect{padding:88px 0 0}
.beyond{margin:88px 0 0;display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center}
.beyond img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin:56px 0 72px}
.stat{border-top:1px solid var(--navy);padding-top:24px}
.stat .v{font-family:var(--display);font-weight:600;font-size:clamp(40px,4.4vw,60px);color:var(--navy);line-height:1;letter-spacing:-.03em}
.stat .v i{font-style:normal;color:var(--coral);font-size:.5em;margin:0 10px;vertical-align:middle}
.stat .l{font-size:14px;color:var(--muted);margin-top:14px}
.proof{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;padding-bottom:88px}
.proof figure{margin:0;padding:14px;border:1px solid var(--rule);background:var(--white)}
.proof img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover}
.proof figcaption{margin-top:12px}
.case{padding:64px;display:grid;grid-template-columns:1fr 1.4fr;gap:64px;margin-top:56px}
.case h3{font-size:clamp(34px,4vw,52px);color:var(--cream)}.case p{font-size:16px}
.about{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px;align-items:start;padding-bottom:72px}
.about .sticky{position:sticky;top:110px}
.about .portrait::after{inset:18px 18px -18px -18px}
.lesson{margin:40px 0;padding-left:28px;border-left:2px solid var(--coral)}
.tl{list-style:none;margin:72px 0 0;padding:0;border-top:1px solid var(--navy)}
.tl li{display:grid;grid-template-columns:200px 1fr;gap:32px;padding:22px 0;border-bottom:1px solid var(--rule);font-size:16px}
.tl b{font-family:var(--display);font-weight:600;color:var(--teal);font-size:14px;letter-spacing:.1em;text-transform:uppercase;padding-top:3px}
.mapbox{border:1px solid var(--rule);background:var(--white);padding:24px;margin:48px 0 72px}
.pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-bottom:72px}
.pillars article{border-top:1px solid var(--navy);padding-top:22px}
.pillars h3{font-size:20px;color:var(--navy)}.pillars p{font-size:15px;color:var(--muted)}
.impulsa{display:grid;grid-template-columns:1fr auto;gap:48px;align-items:center;border:1px solid var(--rule);background:var(--white);padding:40px 48px;margin-bottom:24px}
.impulsa .badge{font-family:var(--display);font-weight:600;font-size:18px;color:var(--navy);border:1px solid var(--navy);padding:16px 28px;text-decoration:none;white-space:nowrap}
.contact{display:grid;grid-template-columns:1fr 1fr;gap:72px;padding-bottom:96px;align-items:start}
.cal{padding:48px}.cal h3{font-size:28px}.cal .mail{margin-top:32px;font-size:14px}
@media(max-width:960px){
.hero,.band .grid,.loop,.beyond,.proof,.case,.about,.impulsa,.contact{grid-template-columns:1fr;gap:40px}
.why-grid,.stats,.pillars{grid-template-columns:1fr}
.before{grid-template-columns:1fr;gap:16px}
.phase{grid-template-columns:70px 1fr}.phase p{grid-column:2}
.tl li{grid-template-columns:1fr;gap:4px}
.hero{padding:56px 0}.portrait{max-width:420px}.about .sticky{position:static}
}
@media(max-width:600px){.case,.cal,.impulsa{padding:32px 24px}}
"""

def loop_svg():
    import math
    cx, cy, r = 220, 220, 150
    out = ['<svg viewBox="0 0 440 440" role="img" aria-label="Analyze, fit, connect, build. Feedback and adjust as we go.">',
           '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5 0 10z" fill="#5D9382"/></marker></defs>',
           f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#1F3C54" stroke-opacity=".25" stroke-dasharray="3 6"/>']
    for i in range(4):
        a0 = -math.pi/2 + i*math.pi/2 + .32; a1 = a0 + math.pi/2 - .64
        out.append(f'<path d="M{cx+r*math.cos(a0):.1f} {cy+r*math.sin(a0):.1f} A{r} {r} 0 0 1 {cx+r*math.cos(a1):.1f} {cy+r*math.sin(a1):.1f}" fill="none" stroke="#5D9382" stroke-width="1.5" marker-end="url(#ah)"/>')
    for i, (short, long) in enumerate(C.LOOP):
        a = -math.pi/2 + i*math.pi/2; x, y = cx + r*math.cos(a), cy + r*math.sin(a)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="46" fill="#FFFCF5" stroke="#1F3C54"/><text x="{x:.1f}" y="{y+6:.1f}" text-anchor="middle" font-family="Poppins,sans-serif" font-weight="600" font-size="17" fill="#1F3C54">{short}</text>')
    out.append(f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="Poppins,sans-serif" font-weight="600" font-size="11" letter-spacing="2" fill="#5D9382">FEEDBACK</text><text x="{cx}" y="{cy+14}" text-anchor="middle" font-family="Poppins,sans-serif" font-weight="600" font-size="11" letter-spacing="2" fill="#5D9382">AND ADJUST</text></svg>')
    return "".join(out)

def pg(active, title, main): return page(N, active, title, main)

def build():
    write(N, "style.css", CSS)
    home = f"""
<section class="wrap hero">
  <div><span class="label">{C.BRAND} · {C.TAGLINE}</span><h1>{C.HEADLINE}</h1><p class="lede">{esc(C.HERO_LEAD)}</p>
  <p style="margin-top:32px"><a class="btn accent" href="{C.CALENDLY}">{C.CTA}</a></p><p class="micro">30 minutes. One strategic conversation. No obligation.</p></div>
  <figure class="portrait">{img("portrait")}</figure>
</section>
<hr class="rule">
<section class="wrap why"><span class="label">{C.THREE_REASONS}</span><h2>{C.WHY_TITLE}</h2><div class="why-grid">{why_items("<article>", "</article>")}</div></section>
<section class="band on-navy"><div class="wrap grid">
  <div><p class="quote">“{esc(C.QUOTE)}”</p><p>{esc(C.QUOTE_P1)}</p><p>{esc(C.QUOTE_P2)}</p></div>
  <figure>{img("panel")}</figure>
</div></section>
<p class="motto quote">{esc(C.MOTTO)}</p>
{cta_block()}
"""
    write(N, "index.html", pg("index.html", "Home", home))
    approach = f"""
<div class="wrap">
 <div class="ph"><span class="label">Approach</span><h1>Better decisions as you grow across borders</h1><p class="lede">{esc(C.APPROACH_INTRO)}</p></div>
 <p class="pull quote">{esc(C.APPROACH_PULL)}</p>
 <div class="loop">{loop_svg()}<div class="cap"><p class="callout">{C.LOOP_NOTE}</p><p>Analyze the current proposition, determine if, where and in what way Mexico is a fit, then connect and build.</p><p>{C.LOOP_BASE}</p></div></div>
 <div class="before"><h3>{C.BEFORE_TITLE}</h3><p>{C.BEFORE_TEXT}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 <span class="label">The process</span>{phases_html()}
 <div class="sect"><span class="label">Areas of expertise</span><h2>What VeliD Advisory does</h2><p class="lede" style="margin-bottom:40px">{esc(C.AREAS_INTRO)}</p>{areas_html()}</div>
 <div class="beyond"><div><span class="label">{C.BEYOND_TITLE}</span><h2>Workshops, cultural training and speaking sessions</h2><p>{esc(C.BEYOND_TEXT)}</p></div>{img("audience")}</div>
</div>
{cta_block()}
"""
    write(N, "approach.html", pg("approach.html", "Approach", approach))
    exp = f"""
<div class="wrap">
 <div class="ph"><span class="label">Experience &amp; Cases</span><h1>{C.EXP_TITLE}</h1><p class="lede">{esc(C.EXP_TEXT)}</p></div>
 {stats_html()}
 <div class="proof"><figure>{img("certificate")}<figcaption class="caption">{esc(C.PHOTOS["certificate"][1])}.</figcaption></figure>
  <div><span class="label">Recognition</span><h2>{C.RECOG}</h2><p>{esc(C.TRACK_NOTE)}</p></div></div>
 <span class="label">{C.CASES_TITLE}</span><h2>{C.CASES_P1}</h2><p class="lede">{esc(C.CASES_P2)}</p><p class="lede">{esc(C.CASES_P3)}</p>
 <div class="case on-navy"><div><span class="label">{C.CASE_KICKER}</span><h3>{C.CASE_NAME}</h3></div><div><p>{esc(C.CASE_P1)}</p><p>{esc(C.CASE_P2)}</p></div></div>
</div>
{cta_block()}
"""
    write(N, "experience.html", pg("experience.html", "Experience & Cases", exp))
    about = f"""
<div class="wrap">
 <div class="ph"><span class="label">About</span><h1>{C.ABOUT_INTRO}</h1></div>
 <div class="about"><div class="sticky"><figure class="portrait">{img("portrait")}</figure></div>
  <div>{"".join(f"<p>{esc(p)}</p>" for p in C.ABOUT)}<p class="lesson callout">{esc(C.ABOUT_LESSON)}</p><p>{esc(C.ABOUT_CLOSE)}</p><p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></p></div></div>
 {timeline_html()}
</div>
{cta_block()}
"""
    write(N, "about.html", pg("about.html", "About", about))
    net = f"""
<div class="wrap">
 <div class="ph"><span class="label">Network</span><h1>A network in Mexico and beyond, from institutions to individual specialists</h1><p class="lede">{esc(C.NET_TEXT)}</p></div>
 <div class="mapbox">{MAP_SVG}</div>
 {pillars_html()}
 <p class="lede" style="margin-bottom:56px">{esc(C.NET_COLLAB)}</p>
 <div class="impulsa"><div><span class="label">Member and mentor</span><h2 style="font-size:26px;margin:0">{esc(C.NET_IMPULSA)}</h2></div><a class="badge" href="{C.IMPULSA}">Association IMPULSA</a></div>
 <p class="lede">{esc(C.NET_EXPERT)} <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
</div>
{cta_block()}
"""
    write(N, "network.html", pg("network.html", "Network", net))
    contact = f"""
<div class="wrap">
 <div class="ph"><span class="label">Contact</span><h1>{C.CONTACT_TITLE}</h1></div>
 <div class="contact">
  <div class="cal on-navy"><span class="label">Step one</span><h3>{C.CONTACT_CTA}</h3><p>{C.CTA_VALUE}</p><a class="btn" href="{C.CALENDLY}">Open the calendar</a><p class="mail">Or write directly: <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p></div>
  <div><h3 style="color:var(--navy)">{C.CONTACT_ALT}</h3>{form_html()}</div>
 </div>
</div>
"""
    write(N, "contact.html", pg("contact.html", "Contact", contact))
    privacy(N, pg)

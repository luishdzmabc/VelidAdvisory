# Propuesta 8 · Sistema (brand): retícula de 12 columnas sobre blanco cálido, etiquetas teal en Poppins, filetes navy, datos al frente.
import content as C
from brand import *

N = 8
CSS = TOKENS + ":root{--cream:#FFFCF5;--white:#FFFFFF}" + BASE + """
body{font-size:16px}
.g12{display:grid;grid-template-columns:repeat(12,1fr);gap:32px}
.label{margin-bottom:0}
.hero{padding:88px 0 96px}
.hero .meta{grid-column:1/3;grid-row:1;font-family:var(--display);font-weight:600;font-size:12px;color:var(--teal);line-height:1.9;text-transform:uppercase;letter-spacing:.12em;padding-top:12px}
.hero h1{grid-column:3/9;grid-row:1;font-size:clamp(44px,6vw,84px);letter-spacing:-.03em;margin:0}
.hero .lede{grid-column:3/8;grid-row:2;margin-top:24px}
.hero .act{grid-column:3/8;grid-row:3;display:flex;gap:24px;align-items:center;flex-wrap:wrap;margin-top:8px}
.hero .micro{font-size:13px;color:var(--muted)}
.hero figure{grid-column:9/13;grid-row:1/4;margin:0}
.hero img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top}
.sec{padding:96px 0;border-top:1px solid var(--navy)}
.sec-head{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;margin-bottom:56px;align-items:baseline}
.sec-head .label{grid-column:1/3}.sec-head h2{grid-column:3/10;margin:0}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--navy);border-left:1px solid var(--navy)}
.why-grid article{padding:40px 32px 48px;border-right:1px solid var(--navy);border-bottom:1px solid var(--navy);background:var(--white)}
.why-grid .num{font-family:var(--display);font-weight:600;font-size:12px;letter-spacing:.16em;color:var(--teal);margin-bottom:28px}
.why-grid h3{color:var(--navy);font-size:21px;min-height:2.2em}.why-grid p{font-size:15px;margin:0}
.band{padding:112px 0}
.band .label{grid-column:1/3}
.band .quote{grid-column:3/9;font-size:clamp(28px,3.4vw,46px)}
.band .body{grid-column:3/9;margin-top:36px;font-size:15.5px}
.band figure{grid-column:9/13;grid-row:1/3;margin:0}
.band img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover}
.motto{padding:72px 0;border-top:1px solid var(--navy)}
.motto .label{grid-column:1/3}.motto .quote{grid-column:3/10}
.cta{text-align:left;border-top:1px solid var(--navy);background:var(--cream)}
.cta .label{grid-column:1/3}.cta h2{grid-column:3/9}.cta p{grid-column:3/9;margin:0 0 28px}.cta .btn{grid-column:3/6;justify-self:start}.cta .small{grid-column:3/9;margin:0}
.ph .g12{align-items:end}.ph{max-width:none}
.ph .label{grid-column:1/3}.ph h1{grid-column:3/12;margin:0}.ph .lede{grid-column:3/9;margin-top:32px}
.pull{padding:56px 0;border-top:1px solid var(--navy)}
.pull .quote{grid-column:3/10}
.steps{border-top:1px solid var(--navy);display:grid;grid-template-columns:repeat(4,1fr)}
.steps .st{padding:32px 24px 40px;border-right:1px solid var(--rule);position:relative}
.steps .st:last-child{border-right:0}
.steps .label{display:block;margin-bottom:40px}
.steps h3{font-size:28px;color:var(--navy);letter-spacing:-.02em}.steps p{font-size:14px;color:var(--muted);margin:0}
.steps .st::after{content:"→";position:absolute;right:-9px;top:30px;background:var(--cream);color:var(--teal);font-size:14px;padding:0 2px}
.steps .st:last-child::after{content:"↻";right:24px}
.loopnote{padding:24px 0 80px;border-top:1px solid var(--navy)}
.loopnote .label{grid-column:1/3}.loopnote p{grid-column:3/9;margin:0;color:var(--muted);font-size:15px}
.before{border:1px solid var(--navy);padding:40px;display:grid;grid-template-columns:auto 1fr auto;gap:40px;align-items:center;margin-bottom:96px;background:var(--white)}
.before h3{margin:0;color:var(--navy);font-size:24px}.before p{margin:0;color:var(--muted)}
.phases{border-top:1px solid var(--navy)}
.phase{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;padding:40px 0;border-bottom:1px solid var(--rule)}
.phase .n{grid-column:1/3;font-family:var(--display);font-weight:600;font-size:12px;letter-spacing:.16em;color:var(--teal);padding-top:8px}
.phase h3{grid-column:3/6;font-size:26px;color:var(--navy);margin:0}.phase p{grid-column:6/12;margin:0;font-size:15.5px}
.sect{padding:96px 0 0}
.beyond{margin-top:96px;display:grid;grid-template-columns:repeat(12,1fr);gap:32px;align-items:center}
.beyond .t{grid-column:1/7}.beyond img{grid-column:8/13;display:block;width:100%;aspect-ratio:3/2;object-fit:cover}
.stats{display:grid;grid-template-columns:repeat(3,1fr);border:1px solid var(--navy);margin:0 0 96px;background:var(--white)}
.stat{padding:40px 32px;border-right:1px solid var(--navy)}.stat:last-child{border-right:0}
.stat .v{font-family:var(--display);font-weight:600;font-size:clamp(44px,5vw,72px);color:var(--navy);line-height:1;letter-spacing:-.04em}
.stat .v i{font-style:normal;color:var(--coral);font-size:.45em;margin:0 10px;vertical-align:middle}
.stat .l{font-size:14px;color:var(--muted);margin-top:16px}
.proof{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;align-items:center;padding-bottom:96px}
.proof figure{grid-column:1/7;margin:0}.proof .t{grid-column:8/13}
.proof img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover}
.proof figcaption{margin-top:10px}
.case{border:1px solid var(--navy);display:grid;grid-template-columns:repeat(12,1fr);gap:32px;padding:48px 40px;margin-top:48px;background:var(--white)}
.case .h{grid-column:1/5}.case .b{grid-column:5/12}
.case h3{font-size:clamp(34px,4vw,56px);color:var(--navy);letter-spacing:-.03em}.case p{font-size:15.5px}
.about{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;padding-bottom:96px}
.about figure{grid-column:1/5;margin:0;position:sticky;top:100px}
.about img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top}
.about .t{grid-column:6/12}
.lesson{border-left:3px solid var(--coral);padding:8px 0 8px 28px;margin:40px 0}
.tl{list-style:none;margin:0;padding:0;border-top:1px solid var(--navy)}
.tl li{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;padding:20px 0;border-bottom:1px solid var(--rule);font-size:15px}
.tl b{grid-column:1/3;font-family:var(--display);font-weight:600;color:var(--teal);font-size:12px;letter-spacing:.12em;text-transform:uppercase;padding-top:3px}
.tl span{grid-column:3/10}
.mapbox{border:1px solid var(--navy);padding:24px;margin:0 0 72px;background:var(--white)}
.pillars{display:grid;grid-template-columns:repeat(3,1fr);border:1px solid var(--navy);margin-bottom:56px;background:var(--white)}
.pillars article{padding:36px 32px;border-right:1px solid var(--navy)}.pillars article:last-child{border-right:0}
.pillars h3{font-size:20px;color:var(--navy)}.pillars p{font-size:14.5px;color:var(--muted);margin:0}
.impulsa{display:flex;justify-content:space-between;align-items:center;gap:40px;border:1px solid var(--navy);padding:40px;margin:56px 0 40px;flex-wrap:wrap;background:var(--white)}
.impulsa h2{font-size:24px;margin:0}
.impulsa .badge{font-family:var(--display);font-weight:600;font-size:14px;letter-spacing:.08em;text-transform:uppercase;color:var(--navy);box-shadow:inset 0 0 0 1px var(--navy);padding:16px 24px;text-decoration:none;white-space:nowrap}
.contact{display:grid;grid-template-columns:repeat(12,1fr);gap:32px;padding-bottom:112px;align-items:start}
.cal{grid-column:1/6;padding:44px}.cal h3{font-size:26px}.cal .mail{margin-top:32px;font-size:14px}
.contact .fm{grid-column:7/13}
.f input,.f textarea{border:0;border-bottom:1px solid var(--navy);background:transparent;padding:12px 0}
.f input:focus,.f textarea:focus{border-bottom:2px solid var(--teal)}
@media(max-width:960px){
.g12,.sec-head,.phase,.beyond,.proof,.case,.about,.tl li,.contact{grid-template-columns:1fr;gap:20px}
.g12 > *,.sec-head > *,.phase > *,.beyond > *,.proof > *,.case > *,.about > *,.tl li > *,.contact > *{grid-column:1/-1 !important;grid-row:auto !important}
.why-grid,.stats,.pillars,.steps{grid-template-columns:1fr}
.steps .st{border-right:0;border-bottom:1px solid var(--rule)}.steps .st::after{display:none}
.stat,.pillars article{border-right:0;border-bottom:1px solid var(--navy)}
.before{grid-template-columns:1fr;gap:16px}
.about figure,.hero figure{position:static;max-width:420px}
.hero{padding:48px 0 64px}.sec{padding:64px 0}
}
@media(max-width:600px){.case,.cal,.impulsa,.before{padding:28px 20px}}
"""

def pg(active, title, main): return page(N, active, title, main, hdr_btn="btn ghost")

def ph(label, h1, lede=""):
    return f'<div class="wrap ph"><div class="g12"><span class="label">{label}</span><h1>{h1}</h1>{f"<p class=lede>{lede}</p>" if lede else ""}</div></div>'

def cta8(idx):
    return f"""
<section class="cta"><div class="wrap g12">
  <span class="label">{idx} · Next step</span>
  <h2><span class="arrow">→</span> {C.CTA} <span class="arrow">←</span></h2>
  <p>{C.CTA_SUB}</p>
  <a class="btn" href="{C.CALENDLY}">{C.CTA}</a>
  <p class="small">30 minutes. One strategic conversation. No obligation.</p>
</div></section>"""

def build():
    write(N, "style.css", CSS)
    home = f"""
<section class="wrap hero"><div class="g12">
  <div class="meta">VeliD Advisory<br>NL · MX<br>Growth that lasts</div><h1>{C.HEADLINE}</h1>
  <p class="lede">{esc(C.HERO_LEAD)}</p><div class="act"><a class="btn" href="{C.CALENDLY}">{C.CTA}</a><span class="micro">30 minutes. One conversation. No obligation.</span></div>
  <figure>{img("portrait")}<figcaption class="caption" style="margin-top:10px">Carin Verbree, founder</figcaption></figure>
</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><span class="label">01 · {C.THREE_REASONS}</span><h2>{C.WHY_TITLE}</h2></div><div class="why-grid">{why_items("<article>", "</article>")}</div></div></section>
<section class="band on-navy"><div class="wrap g12">
  <span class="label">02 · Point of view</span>
  <p class="quote">“{esc(C.QUOTE)}”</p>
  <figure>{img("panel")}</figure>
  <div class="body"><p>{esc(C.QUOTE_P1)}</p><p>{esc(C.QUOTE_P2)}</p></div>
</div></section>
<section class="motto"><div class="wrap g12"><span class="label">03 · Purpose</span><p class="quote">{esc(C.MOTTO)}</p></div></section>
{cta8("04")}
"""
    write(N, "index.html", pg("index.html", "Home", home))
    steps = "".join(f'<div class="st"><span class="label">Step 0{i+1}</span><h3>{s}</h3><p>{esc(l)}</p></div>' for i, (s, l) in enumerate(C.LOOP))
    phases = "".join(f'<div class="phase"><span class="n">Phase 0{i+1}</span><h3>{t}</h3><p>{esc(p)}</p></div>' for i, (t, p) in enumerate(C.PHASES))
    approach = f"""
{ph("Approach", "Better decisions as you grow across borders", esc(C.APPROACH_INTRO))}
<div class="wrap">
 <div class="pull"><div class="g12"><p class="quote">{esc(C.APPROACH_PULL)}</p></div></div>
 <div class="steps">{steps}</div>
 <div class="loopnote g12"><span class="label">↻ Loop</span><p>{C.LOOP_NOTE} {C.LOOP_BASE}</p></div>
 <div class="before"><h3>{C.BEFORE_TITLE}</h3><p>{C.BEFORE_TEXT}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 <div class="phases">{phases}</div>
 <div class="sect"><div class="sec-head"><span class="label">Areas of expertise</span><h2>What VeliD Advisory does</h2></div><p class="lede" style="margin-bottom:40px">{esc(C.AREAS_INTRO)}</p>{areas_html()}</div>
 <div class="beyond"><div class="t"><span class="label">{C.BEYOND_TITLE}</span><h2 style="margin-top:16px">Workshops, cultural training and speaking sessions</h2><p>{esc(C.BEYOND_TEXT)}</p></div>{img("audience")}</div>
</div>
{cta8("05")}
"""
    write(N, "approach.html", pg("approach.html", "Approach", approach))
    exp = f"""
{ph("Experience &amp; Cases", C.EXP_TITLE, esc(C.EXP_TEXT))}
<div class="wrap">
 {stats_html()}
 <div class="proof"><figure>{img("certificate")}<figcaption class="caption">{esc(C.PHOTOS["certificate"][1])}.</figcaption></figure>
  <div class="t"><span class="label">Recognition</span><h2 style="margin-top:16px;font-size:28px">{C.RECOG}</h2><p>{esc(C.TRACK_NOTE)}</p></div></div>
 <span class="label">{C.CASES_TITLE}</span><h2 style="margin-top:16px">{C.CASES_P1}</h2><p class="lede">{esc(C.CASES_P2)}</p><p class="lede">{esc(C.CASES_P3)}</p>
 <div class="case"><div class="h"><span class="label">{C.CASE_KICKER} 01</span><h3 style="margin-top:16px">{C.CASE_NAME}</h3></div><div class="b"><p>{esc(C.CASE_P1)}</p><p>{esc(C.CASE_P2)}</p></div></div>
</div>
{cta8("05")}
"""
    write(N, "experience.html", pg("experience.html", "Experience & Cases", exp))
    about = f"""
{ph("About", C.ABOUT_INTRO)}
<div class="wrap">
 <div class="about"><figure>{img("portrait")}</figure>
  <div class="t">{"".join(f"<p>{esc(p)}</p>" for p in C.ABOUT)}<p class="lesson callout">{esc(C.ABOUT_LESSON)}</p><p>{esc(C.ABOUT_CLOSE)}</p><p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></p></div></div>
 <span class="label" style="margin-bottom:16px">Timeline</span>{timeline_html()}
</div>
{cta8("05")}
"""
    write(N, "about.html", pg("about.html", "About", about))
    net = f"""
{ph("Network", "A network in Mexico and beyond", esc(C.NET_TEXT))}
<div class="wrap">
 <div class="mapbox">{MAP_SVG}</div>
 {pillars_html()}
 <p class="lede">{esc(C.NET_COLLAB)}</p>
 <div class="impulsa"><h2>{esc(C.NET_IMPULSA)}</h2><a class="badge" href="{C.IMPULSA}">Association IMPULSA ↗</a></div>
 <p class="lede">{esc(C.NET_EXPERT)} <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>
</div>
{cta8("05")}
"""
    write(N, "network.html", pg("network.html", "Network", net))
    contact = f"""
{ph("Contact", C.CONTACT_TITLE)}
<div class="wrap">
 <div class="contact">
  <div class="cal on-navy"><span class="label">Step 01</span><h3 style="margin-top:16px">{C.CONTACT_CTA}</h3><p>{C.CTA_VALUE}</p><a class="btn" href="{C.CALENDLY}">Open the calendar ↗</a><p class="mail">Or write directly: <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p></div>
  <div class="fm"><h3 style="color:var(--navy)">{C.CONTACT_ALT}</h3>{form_html()}</div>
 </div>
</div>
"""
    write(N, "contact.html", pg("contact.html", "Contact", contact))
    privacy(N, pg)

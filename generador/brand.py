# Base compartida para las propuestas alineadas al Brand Guide (sept 2026):
# Poppins SemiBold para lo que lidera, Montserrat para lo que explica. Navy ancla, teal jerarquía secundaria,
# coral solo para énfasis puntual, crema para respirar. Cuerpo en gris oscuro. Sin guiones largos.
import content as C
from common import *

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Montserrat:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">'

TOKENS = """
:root{--navy:#1F3C54;--teal:#5D9382;--coral:#EB937D;--cream:#FAF5EA;--white:#FFFCF5;--grey:#3A4248;--muted:#6B7479;
--teal-tint:#E6F0EC;--coral-tint:#FBE7E0;--navy-soft:#C8D4DC;--rule:rgba(31,60,84,.16);
--display:'Poppins',system-ui,sans-serif;--text:'Montserrat',system-ui,sans-serif;
--map-land:#5D9382;--map-ink:#1F3C54;--map-bg:#FFFCF5;--map-accent:#EB937D;--map-muted:#6B7479;
--cookie-bg:#1F3C54;--cookie-fg:#FAF5EA;--cookie-line:#1F3C54;--cookie-btn:#EB937D;--cookie-btn-fg:#1F3C54}
"""

BASE = """
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--cream);color:var(--grey);font-family:var(--text);font-size:17px;line-height:1.7;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:var(--display);font-weight:600;color:var(--navy);line-height:1.12;letter-spacing:-.015em;margin:0 0 .5em}
h1{font-size:clamp(38px,5.2vw,66px)}h2{font-size:clamp(28px,3.4vw,44px)}h3{font-size:22px;color:var(--teal)}h4{font-size:17px;color:var(--teal)}
p{margin:0 0 1em}a{color:var(--navy)}strong{font-weight:600}
.wrap{max-width:1180px;margin:0 auto;padding:0 32px}
.label{font-family:var(--display);font-weight:600;font-size:12.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--teal);display:block;margin-bottom:18px}
.lede{font-size:20px;line-height:1.6;color:var(--muted);max-width:60ch}
.quote{font-family:var(--text);font-weight:400;color:var(--teal);font-size:clamp(24px,2.8vw,34px);line-height:1.35;margin:0}
.callout{font-family:var(--display);font-weight:600;color:var(--navy);font-size:clamp(20px,2.2vw,26px);line-height:1.3}
.caption{font-size:13px;color:var(--muted)}
.key{color:var(--coral)}
.btn{display:inline-block;background:var(--navy);color:var(--cream);text-decoration:none;padding:15px 28px;font-family:var(--display);font-weight:600;font-size:15px;transition:.2s;border:1px solid var(--navy);border-radius:var(--r-btn,0)}
.btn:hover{background:var(--teal);border-color:var(--teal);color:#fff}
.btn.accent{background:var(--coral);border-color:var(--coral);color:var(--navy)}.btn.accent:hover{background:var(--navy);border-color:var(--navy);color:var(--cream)}
.btn.ghost{background:transparent;color:var(--navy)}.btn.ghost:hover{background:var(--navy);color:var(--cream)}
.on-navy{background:var(--navy);color:var(--navy-soft)}
.on-navy h1,.on-navy h2,.on-navy .callout{color:var(--cream)}.on-navy h3,.on-navy h4,.on-navy .label{color:#8FC2B1}
.on-navy .quote{color:#A9D3C3}.on-navy .lede,.on-navy .caption{color:var(--navy-soft)}.on-navy a{color:var(--cream)}
.on-navy .logo-svg{color:var(--cream)}
.on-navy .btn{background:var(--coral);border-color:var(--coral);color:var(--navy)}.on-navy .btn:hover{background:var(--cream);border-color:var(--cream)}
/* header */
.hdr{position:sticky;top:0;z-index:40;background:rgba(250,245,234,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--rule)}
.hdr .wrap{display:flex;align-items:center;justify-content:space-between;height:84px;gap:24px}
.logo-svg{height:34px;width:auto;color:var(--navy)}
.nav{display:flex;gap:28px;align-items:center}
.nav-a{text-decoration:none;color:var(--navy);font-family:var(--display);font-size:14px;font-weight:500;padding:6px 0;border-bottom:2px solid transparent}
.nav-a[aria-current]{border-bottom-color:var(--teal)}
.hdr .right{display:flex;align-items:center;gap:22px}
.lang{font-family:var(--display);font-size:12px;letter-spacing:.14em;color:var(--muted);font-weight:500}.lang b{color:var(--navy);font-weight:600}
.burger{display:none;background:none;border:1px solid var(--rule);width:44px;height:44px;font-size:20px;cursor:pointer;color:var(--navy);border-radius:var(--r-btn,0)}
/* CTA block */
.cta{padding:96px 0;text-align:center}
.cta h2{margin-bottom:16px}.cta h2 .arrow{color:var(--coral)}
.cta p{max-width:54ch;margin:0 auto 32px;color:var(--muted);font-size:18px}
.cta .small{font-size:13px;color:var(--muted);margin-top:16px}
/* footer */
.ftr{padding:72px 0 36px;font-size:14px}
.ftr .grid{display:grid;grid-template-columns:1.2fr 1fr 1.2fr;gap:48px}
.ftr .logo-svg{height:40px;margin-bottom:18px}
.ftr h4{font-size:12px;letter-spacing:.16em;text-transform:uppercase;margin:0 0 16px}
.ftr .links a{display:block;margin-bottom:8px;text-decoration:none}.ftr .links a:hover{text-decoration:underline}
.ftr .bottom{display:flex;justify-content:space-between;gap:20px;margin-top:56px;padding-top:24px;border-top:1px solid rgba(250,245,234,.18);font-size:12px;flex-wrap:wrap}
.ftr .bottom a{text-decoration:none}
/* form */
.cform{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.f{display:flex;flex-direction:column;gap:6px;font-family:var(--display);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--teal);font-weight:600}
.f-wide{grid-column:1/-1}
.f input,.f textarea{font-family:var(--text);font-size:16px;text-transform:none;letter-spacing:0;font-weight:400;padding:12px 14px;border:1px solid var(--rule);background:var(--white);color:var(--navy);outline:none;border-radius:var(--r-field,0)}
.f input:focus,.f textarea:focus{border-color:var(--teal)}
.f textarea{resize:vertical}
.privacy{font-size:12px;color:var(--muted);display:flex;gap:10px;align-items:flex-start}
.doc{max-width:760px;padding:88px 0 120px}
/* page header */
.ph{padding:88px 0 56px;max-width:860px}
/* shared blocks */
.areas{display:grid;grid-template-columns:repeat(2,1fr);gap:0 48px;border-top:1px solid var(--rule)}
.areas div{padding:22px 0;border-bottom:1px solid var(--rule)}
.areas h4{margin:0 0 6px;font-size:17px}
.areas p{margin:0;font-size:15px;color:var(--muted)}
@media(max-width:960px){
.ftr .grid,.areas{grid-template-columns:1fr}
.nav{display:none;position:absolute;top:84px;left:0;right:0;background:var(--cream);flex-direction:column;padding:20px 32px;border-bottom:1px solid var(--rule);align-items:flex-start}
.nav.open{display:flex}.burger{display:block}.hdr .right .btn{display:none}
}
@media(max-width:600px){.wrap{padding:0 18px}.cform{grid-template-columns:1fr}}
""" + MAP_CSS + COOKIE_CSS


def header(active, btn_cls="btn ghost"):
    return f"""
<header class="hdr"><div class="wrap">
  <a href="index.html" aria-label="VeliD Advisory home">{LOGO_SVG}</a>
  <nav class="nav" aria-label="Main">{nav_links(active)}</nav>
  <div class="right"><span class="lang"><b>EN</b> · NL</span><a class="{btn_cls}" href="{C.CALENDLY}">{C.CTA}</a><button class="burger" aria-label="Menu" aria-expanded="false">☰</button></div>
</div></header>"""

def cta_block(cls="cta", btn="btn"):
    return f"""
<section class="{cls}"><div class="wrap">
  <h2><span class="arrow">→</span> {C.CTA} <span class="arrow">←</span></h2>
  <p>{C.CTA_SUB}</p>
  <a class="{btn}" href="{C.CALENDLY}">{C.CTA}</a>
  <p class="small">30 minutes. One strategic conversation. No obligation.</p>
</div></section>"""

def footer(cls="ftr on-navy"):
    return f"""
<footer class="{cls}"><div class="wrap">
 <div class="grid">
  <div>{LOGO_SVG}<p>{C.HEADLINE}</p></div>
  <div><h4>Navigation</h4><div class="links">{nav_links("", cls="")}</div></div>
  <div><h4>→ {C.CTA} ←</h4><p>{C.CTA_SUB}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 </div>
 <div class="bottom"><span>{C.COPY}</span><span>EN · NL &nbsp;·&nbsp; <a href="{C.LINKEDIN}">LinkedIn</a> &nbsp;·&nbsp; <a href="mailto:{C.EMAIL}">{C.EMAIL}</a> &nbsp;·&nbsp; <a href="privacy.html">Privacy notice</a></span></div>
</div></footer>"""

def areas_html():
    return '<div class="areas">' + "".join(f"<div><h4>{t}</h4><p>{esc(d)}</p></div>" for t, d in C.AREAS) + "</div>"

def stats_html(cls="stats", item="stat"):
    return f'<div class="{cls}">' + "".join(
        f'<div class="{item}"><div class="v">{a}{"<i>→</i>"+b if b else ""}</div><div class="l">{l}</div></div>' for a, b, l in C.STATS) + "</div>"

def why_items(wrap_open, wrap_close, num_cls="num"):
    return "".join(f'{wrap_open}<div class="{num_cls}">0{i+1}</div><h3>{t}</h3><p>{esc(p)}</p>{wrap_close}' for i, (t, p) in enumerate(C.WHY))

def timeline_html():
    return '<ul class="tl">' + "".join(f"<li><b>{a}</b><span>{esc(b)}</span></li>" for a, b in C.TIMELINE) + "</ul>"

def pillars_html():
    return '<div class="pillars">' + "".join(f"<article><h3>{t}</h3><p>{esc(p)}</p></article>" for t, p in C.NET_PILLARS_B) + "</div>"

def phases_html():
    return '<div class="phases">' + "".join(f'<div class="phase"><div class="n">0{i+1}</div><h3>{t}</h3><p>{esc(p)}</p></div>' for i, (t, p) in enumerate(C.PHASES)) + "</div>"

def page(n, active, title, main, css_extra="", hdr_btn="btn ghost", ftr_cls="ftr on-navy"):
    return shell(title, header(active, hdr_btn) + "<main>" + main + "</main>" + footer(ftr_cls), fonts=FONTS)

def privacy(n, build_page):
    write(n, "privacy.html", build_page("", "Privacy notice", f'<div class="wrap doc">{privacy_page_body()}</div>'))

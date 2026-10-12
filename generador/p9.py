# Propuestas 9 y 10 · Brújula mejorada. Misma forma y estilo de la propuesta 2 (foto a sangre, botones redondeados,
# tarjetas, línea de pasos) con dos temas: 9 navy inmersivo (paleta de marca sobre navy) y 10 la paleta clara de Horizonte.
import content as C
from common import *

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Montserrat:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">'

THEMES = {
    9: dict(
        bg="#17293A", surface="#1F3C54", surface2="#24435E", ink="#FAF5EA", body="#D7DEE3", muted="#A3B1BA",
        teal="#8FC2B1", teal_line="#5D9382", coral="#EB937D", rule="rgba(250,245,234,.14)",
        band_bg="#1F3C54", band_ink="#FAF5EA", band_body="#D7DEE3", band_teal="#A9D3C3",
        hero_a="rgba(23,41,58,.97)", hero_b="rgba(23,41,58,.88)", hero_c="rgba(31,60,84,.55)", hero_d="#17293A",
        hero_filter="grayscale(1) contrast(1.05)", card_bg="#1F3C54", card_ink="#FAF5EA", card_body="#D7DEE3",
        btn_bg="#EB937D", btn_fg="#1F3C54", btn_hover="#FAF5EA", ghost="rgba(250,245,234,.45)",
        hdr_bg="rgba(23,41,58,.92)", nav_active="rgba(250,245,234,.12)", lesson_border="#EB937D",
        map_land="#5D9382", map_ink="#FAF5EA", map_bg="#1F3C54", map_accent="#EB937D", map_muted="#A3B1BA",
        cookie_bg="#FAF5EA", cookie_fg="#1F3C54", cookie_btn="#1F3C54", cookie_btn_fg="#FAF5EA", logo="#FAF5EA",
        stroke_num="#8FC2B1", glow="rgba(93,147,130,.35)", pill_bg="rgba(143,194,177,.15)",
    ),
    10: dict(
        bg="#FAF5EA", surface="#FFFCF5", surface2="#F3ECDD", ink="#1F3C54", body="#3A4248", muted="#6B7479",
        teal="#5D9382", teal_line="#5D9382", coral="#C96A50", rule="rgba(31,60,84,.16)",
        band_bg="#1F3C54", band_ink="#FAF5EA", band_body="#D7DEE3", band_teal="#A9D3C3",
        hero_a="rgba(250,245,234,.98)", hero_b="rgba(250,245,234,.94)", hero_c="rgba(250,245,234,.72)", hero_d="#FAF5EA",
        hero_filter="grayscale(.25)", card_bg="#FFFCF5", card_ink="#1F3C54", card_body="#3A4248",
        btn_bg="#1F3C54", btn_fg="#FAF5EA", btn_hover="#C96A50", ghost="rgba(31,60,84,.45)",
        hdr_bg="rgba(250,245,234,.92)", nav_active="rgba(31,60,84,.08)", lesson_border="#C96A50",
        map_land="#5D9382", map_ink="#1F3C54", map_bg="#FFFCF5", map_accent="#EB937D", map_muted="#6B7479",
        cookie_bg="#1F3C54", cookie_fg="#FAF5EA", cookie_btn="#EB937D", cookie_btn_fg="#1F3C54", logo="#1F3C54",
        stroke_num="#5D9382", glow="rgba(93,147,130,.22)", pill_bg="rgba(93,147,130,.14)",
    ),
}

def css(T):
    return """
:root{--bg:%(bg)s;--surface:%(surface)s;--surface2:%(surface2)s;--ink:%(ink)s;--body:%(body)s;--muted:%(muted)s;--teal:%(teal)s;--teal-line:%(teal_line)s;--coral:%(coral)s;--rule:%(rule)s;
--band-bg:%(band_bg)s;--band-ink:%(band_ink)s;--band-body:%(band_body)s;--band-teal:%(band_teal)s;
--display:'Poppins',system-ui,sans-serif;--text:'Montserrat',system-ui,sans-serif;
--map-land:%(map_land)s;--map-ink:%(map_ink)s;--map-bg:%(map_bg)s;--map-accent:%(map_accent)s;--map-muted:%(map_muted)s;
--cookie-bg:%(cookie_bg)s;--cookie-fg:%(cookie_fg)s;--cookie-line:%(cookie_bg)s;--cookie-btn:%(cookie_btn)s;--cookie-btn-fg:%(cookie_btn_fg)s;--cookie-radius:999px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--body);font-family:var(--text);font-size:17px;line-height:1.68;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:var(--display);color:var(--ink);font-weight:600;letter-spacing:-.02em;line-height:1.08;margin:0 0 .5em}
h1{font-size:clamp(42px,6vw,80px)}h2{font-size:clamp(30px,3.6vw,48px)}h3{font-size:22px}
p{margin:0 0 1em}a{color:var(--teal)}
.wrap{max-width:1200px;margin:0 auto;padding:0 32px}
.kicker{font-family:var(--display);font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--teal);font-weight:600;display:flex;align-items:center;gap:12px;margin-bottom:20px}
.kicker::before{content:"";width:28px;height:2px;background:var(--teal)}
.btn{display:inline-flex;align-items:center;gap:10px;background:%(btn_bg)s;color:%(btn_fg)s;text-decoration:none;padding:16px 30px;border-radius:999px;font-weight:600;font-family:var(--display);font-size:15px;transition:.2s;border:2px solid %(btn_bg)s}
.btn:hover{background:%(btn_hover)s;border-color:%(btn_hover)s;color:%(btn_fg)s}
.btn.ghost{background:transparent;color:var(--ink);border-color:%(ghost)s}.btn.ghost:hover{border-color:var(--ink);background:transparent;color:var(--ink)}
.lede{font-size:20px;line-height:1.55;max-width:60ch;color:var(--muted)}
.quote{font-family:var(--text);font-weight:400;color:var(--teal);line-height:1.3}
/* header */
.hdr{position:sticky;top:0;z-index:40;background:%(hdr_bg)s;backdrop-filter:blur(10px);border-bottom:1px solid var(--rule)}
.hdr .wrap{display:flex;align-items:center;justify-content:space-between;height:88px;gap:24px}
.logo-svg{height:36px;width:auto;color:%(logo)s}
.nav{display:flex;gap:4px}
.nav-a{text-decoration:none;color:var(--ink);font-family:var(--display);font-size:14px;font-weight:500;padding:8px 14px;border-radius:999px}
.nav-a[aria-current]{background:%(nav_active)s}
.hdr .right{display:flex;align-items:center;gap:18px}
.lang{font-family:var(--display);font-size:12px;letter-spacing:.14em;color:var(--muted);font-weight:500}.lang b{color:var(--ink);font-weight:600}
.burger{display:none;background:none;border:1px solid var(--rule);width:44px;height:44px;border-radius:50%%;font-size:20px;cursor:pointer;color:var(--ink)}
/* hero */
.hero{position:relative;min-height:calc(90vh - 88px);display:flex;align-items:flex-end;padding:96px 0;overflow:hidden}
.hero .bgimg{position:absolute;inset:0;z-index:0}
.hero .bgimg img{width:100%%;height:100%%;object-fit:cover;object-position:center 30%%;filter:%(hero_filter)s}
.hero .bgimg::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,%(hero_a)s 0%%,%(hero_b)s 42%%,%(hero_c)s 100%%),linear-gradient(0deg,%(hero_d)s 0%%,transparent 55%%)}
.hero .wrap{position:relative;z-index:1}
.hero h1{max-width:14ch}
.hero .row{display:flex;align-items:center;gap:28px;margin-top:36px;flex-wrap:wrap}
.hero .micro{font-size:13px;color:var(--muted)}
.hero .tag{font-family:var(--display);color:var(--teal);font-weight:600;letter-spacing:.14em;text-transform:uppercase;font-size:12px;margin-bottom:24px}
.sec{padding:112px 0}
/* cards */
.sec-head{display:flex;justify-content:space-between;align-items:flex-end;gap:32px;flex-wrap:wrap;margin-bottom:48px}
.sec-head h2{margin:0}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.card{background:%(card_bg)s;border:1px solid var(--rule);border-radius:24px;padding:40px 36px}
.card .ic{width:52px;height:52px;border-radius:16px;background:%(pill_bg)s;display:grid;place-items:center;margin-bottom:24px;color:var(--teal)}
.card .ic svg{width:26px;height:26px}
.card h3{font-size:21px;color:%(card_ink)s}.card p{font-size:15.5px;margin:0;color:%(card_body)s}
/* stats strip */
.strip{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.strip .stat{background:var(--surface);border:1px solid var(--rule);border-radius:24px;padding:36px 32px}
.stat .v{font-family:var(--display);font-size:clamp(40px,4.6vw,62px);font-weight:700;color:var(--ink);line-height:1;letter-spacing:-.03em}
.stat .v i{font-style:normal;color:var(--coral);font-size:.5em;margin:0 10px;vertical-align:middle}
.stat .l{font-size:14px;color:var(--muted);margin-top:16px}
/* quote band */
.band{padding:120px 0;background:var(--band-bg);color:var(--band-body)}
.band .grid{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.band .quote{margin:0 0 36px;font-size:clamp(28px,3.4vw,44px);color:var(--band-teal)}
.band .kicker{color:var(--band-teal)}.band .kicker::before{background:var(--band-teal)}
.band figure{margin:0;border-radius:28px;overflow:hidden;position:relative}
.band img{display:block;width:100%%;aspect-ratio:4/3;object-fit:cover}
.band figure::after{content:"";position:absolute;inset:0;background:linear-gradient(160deg,rgba(93,147,130,.4),rgba(31,60,84,.15));mix-blend-mode:multiply}
.motto{text-align:center;font-size:clamp(22px,2.4vw,30px);max-width:30ch;margin:0 auto;padding:104px 32px}
/* cta */
.cta{padding:120px 0;background:radial-gradient(1100px 480px at 50%% 0%%,%(glow)s,transparent 70%%)}
.cta .box{text-align:center;max-width:760px;margin:0 auto}
.cta h2{font-size:clamp(36px,4.4vw,60px)}.cta h2 .arrow{color:var(--coral)}
.cta p{font-size:18px;color:var(--muted);margin-bottom:36px}
.cta .small{font-size:13px;margin:18px 0 0}
/* footer */
.ftr{background:var(--band-bg);color:var(--band-body);border-top:1px solid var(--rule);padding:72px 0 36px;font-size:14px}
.ftr .grid{display:grid;grid-template-columns:1.2fr 1fr 1.2fr;gap:48px}
.ftr .logo-svg{margin-bottom:18px;height:40px;color:var(--band-ink)}
.ftr h4{font-family:var(--display);font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--band-teal);margin:0 0 16px}
.ftr a{color:var(--band-ink);text-decoration:none}.ftr a:hover{text-decoration:underline}
.ftr .links a{display:block;margin-bottom:8px}
.ftr .btn{background:#EB937D;border-color:#EB937D;color:#1F3C54}.ftr .btn:hover{background:#FAF5EA;border-color:#FAF5EA}
.ftr .bottom{display:flex;justify-content:space-between;gap:20px;margin-top:56px;padding-top:24px;border-top:1px solid rgba(250,245,234,.18);font-size:12px;flex-wrap:wrap}
/* page header */
.ph{padding:96px 0 72px;max-width:900px}
.ph h1{font-size:clamp(40px,5.4vw,68px)}
/* approach */
.pull{font-size:clamp(26px,3.2vw,40px);max-width:28ch;margin:0 0 80px;padding:36px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.track{display:grid;grid-template-columns:repeat(4,1fr);position:relative;margin-bottom:24px}
.track::before{content:"";position:absolute;left:12%%;right:12%%;top:30px;height:2px;background:linear-gradient(90deg,var(--teal-line),var(--coral))}
.track .st{text-align:center;padding:0 16px}
.track .dot{width:60px;height:60px;border-radius:50%%;background:var(--bg);border:2px solid var(--teal-line);display:grid;place-items:center;margin:0 auto 20px;font-family:var(--display);font-weight:600;color:var(--teal);position:relative}
.track .st:nth-child(4) .dot{border-color:var(--coral);color:var(--coral)}
.track h3{font-size:18px}.track p{font-size:14px;color:var(--muted);margin:0}
.loopnote{text-align:center;font-family:var(--display);color:var(--teal);font-weight:600;margin:0 0 96px;font-size:18px}
.loopnote small{display:block;color:var(--muted);font-family:var(--text);font-weight:400;font-size:14px;margin-top:6px}
.before{background:var(--surface);border:1px solid var(--rule);border-radius:28px;padding:44px 48px;display:grid;grid-template-columns:auto 1fr auto;gap:40px;align-items:center;margin-bottom:96px}
.before h3{margin:0;font-size:24px}.before p{margin:0;color:var(--muted)}
.phases{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.phase{background:var(--surface);border-radius:24px;padding:40px 36px;border:1px solid var(--rule)}
.phase .n{font-family:var(--display);font-size:64px;font-weight:700;color:transparent;-webkit-text-stroke:1px %(stroke_num)s;line-height:1;margin-bottom:24px}
.phase p{font-size:15.5px;margin:0}
.areas{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:48px}
.areas div{background:var(--surface);border:1px solid var(--rule);border-radius:20px;padding:28px 30px}
.areas h4{font-family:var(--display);font-weight:600;color:var(--ink);margin:0 0 6px;font-size:17px}
.areas p{margin:0;font-size:15px;color:var(--muted)}
.sect{padding-top:96px}
.beyond{margin-top:96px;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center}
.beyond img{display:block;width:100%%;aspect-ratio:3/2;object-fit:cover;border-radius:28px}
/* experience */
.proof{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center;padding:96px 0}
.proof figure{margin:0;border-radius:28px;overflow:hidden}
.proof img{display:block;width:100%%;aspect-ratio:3/2;object-fit:cover}
.proof figcaption{font-size:13px;color:var(--muted);padding:14px 4px 0}
.case{background:var(--band-bg);color:var(--band-body);border:1px solid var(--rule);border-radius:32px;padding:64px;display:grid;grid-template-columns:1fr 1.5fr;gap:64px;margin-top:56px}
.case h3{font-size:clamp(34px,4vw,56px);font-weight:700;color:var(--band-ink)}
.case .pill{display:inline-block;background:rgba(169,211,195,.16);color:var(--band-teal);border-radius:999px;padding:6px 14px;font-family:var(--display);font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;margin-bottom:18px}
.case p{font-size:16px}
/* about */
.about{display:grid;grid-template-columns:.85fr 1.15fr;gap:80px;align-items:start;padding-bottom:96px}
.about figure{margin:0;border-radius:32px;overflow:hidden;position:sticky;top:120px}
.about img{display:block;width:100%%;aspect-ratio:4/5;object-fit:cover;object-position:top}
.lesson{font-family:var(--display);font-size:clamp(22px,2.4vw,30px);font-weight:600;color:var(--ink);line-height:1.25;margin:48px 0;padding:36px;background:var(--surface);border-radius:24px;border-left:4px solid %(lesson_border)s}
.tl{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.tl li{background:var(--surface);border:1px solid var(--rule);border-radius:20px;padding:28px;font-size:15px}
.tl b{font-family:var(--display);color:var(--teal);display:block;font-size:13px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:10px;font-weight:600}
/* network */
.mapbox{border-radius:32px;overflow:hidden;border:1px solid var(--rule);background:var(--surface);padding:24px;margin:0 0 72px}
.pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:56px}
.pillars article{background:var(--surface);border:1px solid var(--rule);border-radius:24px;padding:36px}
.pillars h3{font-size:20px}.pillars p{font-size:15px;color:var(--muted);margin:0}
.impulsa{display:flex;justify-content:space-between;align-items:center;gap:40px;background:var(--band-bg);color:var(--band-body);border-radius:28px;padding:48px;margin:56px 0 40px;flex-wrap:wrap}
.impulsa h2{color:var(--band-ink);font-size:26px;margin:0}
.impulsa .badge{font-family:var(--display);font-weight:600;color:#1F3C54;background:#FAF5EA;border-radius:999px;padding:16px 28px;text-decoration:none;white-space:nowrap}
/* contact */
.contact{display:grid;grid-template-columns:1fr 1fr;gap:72px;padding-bottom:120px;align-items:start}
.cal{background:var(--band-bg);color:var(--band-body);border:1px solid var(--rule);border-radius:32px;padding:48px}
.cal h3{font-size:28px;color:var(--band-ink)}.cal .kicker{color:var(--band-teal)}.cal .kicker::before{background:var(--band-teal)}
.cal .btn{background:#EB937D;border-color:#EB937D;color:#1F3C54}.cal .btn:hover{background:#FAF5EA;border-color:#FAF5EA}
.cal .mail{margin-top:32px;font-size:14px}.cal .mail a{color:var(--band-ink)}
.cform{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.f{display:flex;flex-direction:column;gap:8px;font-family:var(--display);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--teal);font-weight:600}
.f-wide{grid-column:1/-1}
.f input,.f textarea{font-family:var(--text);font-size:16px;text-transform:none;letter-spacing:0;font-weight:400;padding:14px 18px;border:1px solid var(--rule);border-radius:14px;background:var(--surface);color:var(--ink);outline:none}
.f input:focus,.f textarea:focus{border-color:var(--teal)}
.privacy{font-size:12px;color:var(--muted);display:flex;gap:10px;align-items:flex-start;text-transform:none;letter-spacing:0;font-family:var(--text);font-weight:400}
.doc{max-width:760px;padding:96px 0 120px}
@media(max-width:960px){
.band .grid,.beyond,.proof,.case,.about,.contact{grid-template-columns:1fr;gap:40px}
.why-grid,.strip,.pillars,.phases,.tl,.areas{grid-template-columns:1fr}
.track{grid-template-columns:1fr 1fr;row-gap:32px}.track::before{display:none}
.ftr .grid{grid-template-columns:1fr}
.before{grid-template-columns:1fr;gap:16px}
.about figure{position:static;max-width:420px}
.nav{display:none;position:absolute;top:88px;left:0;right:0;background:var(--bg);flex-direction:column;padding:20px 32px;border-bottom:1px solid var(--rule)}
.nav.open{display:flex}.burger{display:block}.hdr .right .btn{display:none}
.hero{min-height:0;padding:64px 0 72px}.sec{padding:72px 0}
}
@media(max-width:600px){.wrap{padding:0 18px}.cform{grid-template-columns:1fr}.case,.cal,.impulsa{padding:32px 24px}}
""" % T + MAP_CSS + COOKIE_CSS

ICONS = [
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18M5.5 6.5c2 1.5 4 2.2 6.5 2.2s4.5-.7 6.5-2.2M5.5 17.5c2-1.5 4-2.2 6.5-2.2s4.5.7 6.5 2.2"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="5" cy="12" r="2.2"/><circle cx="19" cy="6" r="2.2"/><circle cx="19" cy="18" r="2.2"/><path d="M7 11l10-4M7 13l10 4"/></svg>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21V11M12 11c0-4 3-7 8-7 0 4-3 7-8 7zM12 15c0-3-2.5-5-6-5 0 3 2.5 5 6 5z"/></svg>',
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
  <p class="small">30 minutes. One strategic conversation. No obligation.</p>
</div></section>"""

def footer():
    return f"""
<footer class="ftr"><div class="wrap">
 <div class="grid">
  <div>{LOGO_SVG}<p>{C.HEADLINE}</p></div>
  <div><h4>Navigation</h4><div class="links">{nav_links("", cls="")}</div></div>
  <div><h4>→ {C.CTA} ←</h4><p>{C.CTA_SUB}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 </div>
 <div class="bottom"><span>{C.COPY}</span><span>EN · NL &nbsp;·&nbsp; <a href="{C.LINKEDIN}">LinkedIn</a> &nbsp;·&nbsp; <a href="mailto:{C.EMAIL}">{C.EMAIL}</a> &nbsp;·&nbsp; <a href="privacy.html">Privacy notice</a></span></div>
</div></footer>"""

def stats():
    return '<div class="strip">' + "".join(f'<div class="stat"><div class="v">{a}{"<i>→</i>"+b if b else ""}</div><div class="l">{l}</div></div>' for a, b, l in C.STATS) + "</div>"

def build_theme(N):
    T = THEMES[N]
    write(N, "style.css", css(T))
    def page(active, title, main):
        return shell(title, header(active) + "<main>" + main + "</main>" + footer(), fonts=FONTS)
    why = "".join(f'<article class="card"><div class="ic">{ICONS[i]}</div><h3>{t}</h3><p>{esc(p)}</p></article>' for i, (t, p) in enumerate(C.WHY))
    home = f"""
<section class="hero"><div class="bgimg">{img("panel")}</div><div class="wrap">
  <div class="tag">{C.BRAND} · {C.TAGLINE}</div>
  <h1>{C.HEADLINE}</h1><p class="lede">{esc(C.HERO_LEAD)}</p>
  <div class="row"><a class="btn" href="{C.CALENDLY}">{C.CTA} <span aria-hidden="true">↗</span></a><span class="micro">30 minutes. One strategic conversation. No obligation.</span></div>
</div></section>
<section class="sec"><div class="wrap"><div class="sec-head"><div><div class="kicker">{C.THREE_REASONS}</div><h2>{C.WHY_TITLE}</h2></div></div><div class="why-grid">{why}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="kicker">Experience you can measure</div>{stats()}<p class="lede" style="margin-top:28px">{esc(C.TRACK_NOTE)} <a href="experience.html">Read more →</a></p></div></section>
<section class="band"><div class="wrap grid">
  <div><div class="kicker">Point of view</div><p class="quote">“{esc(C.QUOTE)}”</p><p>{esc(C.QUOTE_P1)}</p><p>{esc(C.QUOTE_P2)}</p></div>
  <figure>{img("signing")}</figure>
</div></section>
<p class="motto quote">{esc(C.MOTTO)}</p>
{cta_block()}
"""
    write(N, "index.html", page("index.html", "Home", home))
    track = "".join(f'<div class="st"><div class="dot">0{i+1}</div><h3>{s}</h3><p>{esc(l)}</p></div>' for i, (s, l) in enumerate(C.LOOP))
    phases = "".join(f'<div class="phase"><div class="n">0{i+1}</div><h3>{t}</h3><p>{esc(p)}</p></div>' for i, (t, p) in enumerate(C.PHASES))
    areas = '<div class="areas">' + "".join(f"<div><h4>{t}</h4><p>{esc(d)}</p></div>" for t, d in C.AREAS) + "</div>"
    approach = f"""
<div class="wrap">
 <div class="ph"><div class="kicker">Approach</div><h1>Better decisions as you grow across borders</h1><p class="lede">{esc(C.APPROACH_INTRO)}</p></div>
 <p class="pull quote">{esc(C.APPROACH_PULL)}</p>
 <div class="track">{track}</div>
 <p class="loopnote">↻ {C.LOOP_NOTE}<small>{C.LOOP_BASE}</small></p>
 <div class="before"><h3>{C.BEFORE_TITLE}</h3><p>{C.BEFORE_TEXT}</p><a class="btn" href="{C.CALENDLY}">{C.CTA}</a></div>
 <div class="kicker">The process</div><h2>How we work together</h2>
 <div class="phases">{phases}</div>
 <div class="sect"><div class="kicker">Areas of expertise</div><h2>What VeliD Advisory does</h2><p class="lede">{esc(C.AREAS_INTRO)}</p>{areas}</div>
 <div class="beyond"><div><div class="kicker">{C.BEYOND_TITLE}</div><h2>Workshops, cultural training and speaking sessions</h2><p>{esc(C.BEYOND_TEXT)}</p></div>{img("audience")}</div>
</div>
{cta_block()}
"""
    write(N, "approach.html", page("approach.html", "Approach", approach))
    exp = f"""
<div class="wrap">
 <div class="ph"><div class="kicker">Experience &amp; Cases</div><h1>{C.EXP_TITLE}</h1><p class="lede">{esc(C.EXP_TEXT)}</p></div>
 {stats()}
 <div class="proof"><figure>{img("certificate")}<figcaption>{esc(C.PHOTOS["certificate"][1])}.</figcaption></figure>
  <div><div class="kicker">Recognition</div><h2>{C.RECOG}</h2><p>{esc(C.TRACK_NOTE)}</p></div></div>
 <div class="kicker">{C.CASES_TITLE}</div><h2>{C.CASES_P1}</h2><p class="lede">{esc(C.CASES_P2)}</p><p class="lede">{esc(C.CASES_P3)}</p>
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
    pillars = "".join(f"<article><h3>{t}</h3><p>{esc(p)}</p></article>" for t, p in C.NET_PILLARS_B)
    net = f"""
<div class="wrap">
 <div class="ph"><div class="kicker">Network</div><h1>A network in Mexico and beyond</h1><p class="lede">{esc(C.NET_TEXT)}</p></div>
 <div class="mapbox">{MAP_SVG}</div>
 <div class="pillars">{pillars}</div>
 <p class="lede">{esc(C.NET_COLLAB)}</p>
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

def build(): build_theme(9)

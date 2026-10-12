import os, re, shutil, html
import content as C

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "sitio")
ASSETS_SRC = os.path.join(ROOT, "sitio", "assets")

LOGO_SVG = open(os.path.join(ASSETS_SRC, "logo.svg")).read()
LOGO_SVG = re.sub(r'width="1800" height="775"', 'class="logo-svg"', LOGO_SVG)
MAP_SVG = open(os.path.join(ASSETS_SRC, "map.svg")).read()
MAP_SVG = MAP_SVG.replace('clippath', 'clipPath').replace('viewbox', 'viewBox')

MAP_CSS = """
.netfig{width:100%;height:auto;display:block}
.netfig .land{stroke:var(--map-land);stroke-width:1.75;stroke-linecap:round;fill:none;opacity:.55}
.netfig .par{stroke:var(--map-land);stroke-width:.6;fill:none;opacity:.28}
.netfig .link{stroke:var(--map-ink);stroke-width:1;fill:none;opacity:.85;stroke-linecap:round}
.netfig .link.main{stroke-width:1.4;opacity:.95}
.netfig .link.soft{opacity:.7;stroke-dasharray:1.5 4.5}
.netfig .disc{fill:var(--map-bg);stroke:var(--map-ink);stroke-width:1}
.netfig .node{fill:var(--map-ink)}
.netfig .halo{fill:var(--map-accent);opacity:.25}
.netfig .ring{fill:var(--map-bg);stroke:var(--map-accent);stroke-width:1.1}
.netfig text{font-family:var(--display)}
.netfig text.key{fill:var(--map-ink);font-weight:600;font-size:8.4px;letter-spacing:.12em;text-transform:uppercase;paint-order:stroke;stroke:var(--map-bg);stroke-width:3px;stroke-linejoin:round}
.netfig text.lg{fill:var(--map-muted);font-family:var(--text);font-size:7.6px}
"""

COOKIE_HTML = f"""
<div class="cookie" id="cookie" role="dialog" aria-live="polite">
  <p>{C.COOKIE} <a href="privacy.html">Privacy notice</a></p>
  <button type="button" id="cookie-ok">OK</button>
</div>
<script>
(function(){{var k='velid-cookie-ok';try{{if(localStorage.getItem(k)){{document.getElementById('cookie').remove();return;}}}}catch(e){{}}
document.getElementById('cookie-ok').addEventListener('click',function(){{try{{localStorage.setItem(k,'1')}}catch(e){{}}document.getElementById('cookie').remove();}});}})();
(function(){{var b=document.querySelector('.burger'),n=document.querySelector('.nav');if(b&&n){{b.addEventListener('click',function(){{var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);}});}}}})();
(function(){{var f=document.querySelector('form.cform');if(!f)return;f.addEventListener('submit',function(e){{e.preventDefault();var d=new FormData(f);var s='VeliD website: '+(d.get('company')||'')+' / '+(d.get('name')||'');var b='Name: '+d.get('name')+'\\nEmail: '+d.get('email')+'\\nPhone: '+d.get('phone')+'\\nCompany: '+d.get('company')+'\\n\\n'+d.get('message');location.href='mailto:{C.EMAIL}?subject='+encodeURIComponent(s)+'&body='+encodeURIComponent(b);}});}})();
</script>
"""

COOKIE_CSS = """
.cookie{position:fixed;left:16px;right:16px;bottom:16px;max-width:560px;margin:0 auto;display:flex;gap:16px;align-items:center;justify-content:space-between;padding:14px 18px;background:var(--cookie-bg);color:var(--cookie-fg);border:1px solid var(--cookie-line);border-radius:var(--cookie-radius,0);font-size:13px;z-index:50;box-shadow:0 12px 32px rgba(0,0,0,.18)}
.cookie p{margin:0;line-height:1.45}.cookie a{color:inherit;text-decoration:underline}
.cookie button{flex:none;background:var(--cookie-btn);color:var(--cookie-btn-fg);border:0;padding:8px 16px;font:inherit;font-weight:600;cursor:pointer;border-radius:var(--cookie-radius,0)}
"""

def esc(s): return html.escape(s, quote=False)

def img(key, cls="", extra=""):
    fn, alt = C.PHOTOS[key]
    return f'<img src="../assets/{fn}" alt="{esc(alt)}" class="{cls}" loading="lazy" {extra}>'

def nav_links(active, cls="nav-a"):
    out = []
    for href, label in C.NAV:
        a = ' aria-current="page"' if href == active else ''
        out.append(f'<a class="{cls}" href="{href}"{a}>{esc(label)}</a>')
    return "\n".join(out)

def form_html(btn_cls="btn", submit_label="Send message"):
    fields = []
    for name, label, typ in C.FORM:
        req = "required" if name in ("name", "email") else ""
        fields.append(f'<label class="f"><span>{label}</span><input type="{typ}" name="{name}" {req}></label>')
    fields.append(f'<label class="f f-wide"><span>{C.FORM_MSG}</span><textarea name="message" rows="5" required></textarea></label>')
    fields.append(f'<p class="f-wide privacy"><input type="checkbox" required id="gdpr"> <label for="gdpr">I agree that VeliD Advisory stores the details above to respond to my message. {esc(C.PRIVACY)}</label></p>')
    fields.append(f'<p class="f-wide"><button class="{btn_cls}" type="submit">{submit_label}</button></p>')
    return '<form class="cform" novalidate>' + "\n".join(fields) + '</form>'

def privacy_page_body():
    return f"""
<h1>Privacy notice</h1>
<p>VeliD Advisory ({C.BRAND}) processes the personal data you submit through the contact form (name, email, phone, company and your message)
only to answer your request and, where you ask for one, to prepare an introduction call. Data is kept for as long as our conversation is
active and is never sold or shared with third parties for marketing purposes.</p>
<p>Scheduling is handled by Calendly under its own privacy policy. This site uses only essential, privacy-friendly analytics with no
personal data collection. You can request access to, correction or deletion of your data at any time by writing to
<a href="mailto:{C.EMAIL}">{C.EMAIL}</a>.</p>
<p><a href="index.html">Back to home</a></p>
"""

def shell(title, body, css_href="style.css", extra_head="", lang="en", body_cls="", fonts=""):
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · {C.BRAND}</title>
<meta name="description" content="{esc(C.HEADLINE)} {esc(C.HERO_LEAD)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{fonts}
<link rel="icon" type="image/svg+xml" href="../assets/icon.svg">
<link rel="stylesheet" href="{css_href}">
{extra_head}
</head>
<body class="{body_cls}">
{body}
{COOKIE_HTML}
</body>
</html>
"""

def write(n, name, text):
    d = os.path.join(OUT, str(n))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, name), "w") as f:
        f.write(text)

def copy_assets():
    d = os.path.join(OUT, "assets")
    os.makedirs(d, exist_ok=True)
    if os.path.abspath(ASSETS_SRC) == os.path.abspath(d):
        return
    for fn in os.listdir(ASSETS_SRC):
        shutil.copy(os.path.join(ASSETS_SRC, fn), d)

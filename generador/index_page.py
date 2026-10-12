# Página índice de las 4 propuestas (para Carin y Luis)
import os
from common import OUT

PROPS = [
    (1, "Horizonte", "Editorial · serif · crema y navy · ronda 1",
     "La consultora de confianza. Serif (Fraunces) con mucho aire, filetes finos y retrato enmarcado. Hecha antes de leer el brand guide: usa una serif que la guía no contempla.",
     "#FAF5EA", "#1F3C54", "#C96A50"),
    (2, "Brújula", "Navy inmersivo · Poppins · fotografía a sangre · ronda 1",
     "Dirección y seguridad. Fondo oscuro, foto en duotono, botones redondeados. La versión mejorada y alineada a la guía es la propuesta 9.",
     "#101B25", "#8FC2B1", "#F0A992"),
    (3, "Raíz", "Cálida · arena y terracota · formas orgánicas · ronda 1",
     "Cercanía humana. Arcos y tarjetas redondeadas. Hecha antes de leer el brand guide: usa una serif y un terracota fuera de la paleta.",
     "#F6EDE1", "#4A7A69", "#C96A50"),
    (4, "Sistema", "Retícula suiza · blanco · monoespaciada · ronda 1",
     "Precisión holandesa. Retícula de 12 columnas y datos al frente. Hecha antes de leer el brand guide: usa una monoespaciada que la guía no contempla.",
     "#FFFFFF", "#1F3C54", "#4A7A69"),
    (5, "Horizonte · brand", "Editorial en crema · Poppins y Montserrat · guía sept 2026",
     "La misma idea editorial de la 1, ahora con las dos tipografías de la guía, navy como ancla, teal en etiquetas y coral solo en el CTA. Incluye áreas de expertise y favicon con el monograma.",
     "#FAF5EA", "#5D9382", "#EB937D"),
    (6, "Brújula · brand", "Banda navy con logo invertido · cuerpo en crema · guía sept 2026",
     "Hero en navy con el lockup invertido (crema, coral y teal) y cuerpo en crema con tarjetas blancas. Botones redondeados. Es la lectura más fiel de la guía con energía de la 2.",
     "#1F3C54", "#8FC2B1", "#EB937D"),
    (7, "Raíz · brand", "Formas orgánicas con la paleta oficial · guía sept 2026",
     "Arcos y tarjetas redondeadas de la 3, pero en Poppins y Montserrat, con bloques teal y navy. Coral reservado al CTA y a una palabra clave del titular.",
     "#FAF5EA", "#5D9382", "#1F3C54"),
    (8, "Sistema · brand", "Retícula suiza con etiquetas teal en Poppins · guía sept 2026",
     "La retícula de la 4 sin monoespaciada: etiquetas en Poppins SemiBold teal, filetes navy, datos en cajas. La más sobria y la que mejor envejece.",
     "#FFFCF5", "#1F3C54", "#5D9382"),
    (9, "Brújula · mejorada", "La 2 pulida: navy de marca, teal y coral oficiales · guía sept 2026",
     "Misma forma y estilo que la 2: foto a sangre, botones redondeados, tarjetas y línea de pasos. Mejoras: navy de marca en lugar de negro azulado, logo invertido en crema, cifras de Holland House en el home, áreas de expertise, sin guiones largos.",
     "#17293A", "#8FC2B1", "#EB937D"),
    (10, "Brújula · clara", "Forma y estilo de la 2 con la paleta de Horizonte · guía sept 2026",
     "Exactamente la estructura de la 9 (hero con foto, tarjetas, línea de pasos, bandas) pero en crema, navy y coral de la propuesta 1. Las bandas de cita, caso, contacto y pie quedan en navy.",
     "#FAF5EA", "#1F3C54", "#C96A50"),
]

HTML = """<!doctype html><html lang="es-MX"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>VeliD Advisory · 10 propuestas de rediseño</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600&family=Montserrat:wght@400;500&display=swap" rel="stylesheet">
<style>
body{margin:0;font-family:Montserrat,system-ui,sans-serif;background:#F5F2EC;color:#2F363B;line-height:1.6}
.wrap{max-width:1100px;margin:0 auto;padding:56px 24px}
h1{font-family:Poppins,sans-serif;color:#1F3C54;font-size:clamp(28px,4vw,44px);margin:0 0 8px;letter-spacing:-.02em}
.sub{color:#6A7378;margin-bottom:40px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.card{background:#fff;border:1px solid rgba(31,60,84,.15);border-radius:16px;overflow:hidden;display:flex;flex-direction:column}
.sw{height:120px;display:flex;align-items:flex-end;padding:20px;gap:10px}
.sw i{width:28px;height:28px;border-radius:50%;display:block;border:1px solid rgba(0,0,0,.1)}
.sw b{font-family:Poppins,sans-serif;font-size:28px;margin-left:auto;opacity:.9}
.body{padding:24px}
h2{font-family:Poppins,sans-serif;margin:0 0 4px;font-size:22px;color:#1F3C54}
.k{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#4A7A69;font-weight:500;margin-bottom:12px}
p{margin:0 0 18px;font-size:15px}
.links{display:flex;gap:8px;flex-wrap:wrap;margin-top:auto}
.links a{font-size:13px;text-decoration:none;color:#1F3C54;border:1px solid #1F3C54;padding:8px 14px;border-radius:999px}
.links a.main{background:#1F3C54;color:#fff}
.note{margin-top:40px;font-size:13px;color:#6A7378;border-top:1px solid rgba(31,60,84,.15);padding-top:20px}
@media(max-width:720px){.grid{grid-template-columns:1fr}}
</style></head><body><div class="wrap">
<h1>VeliD Advisory · 10 propuestas de rediseño</h1>
<p class="sub">Demos navegables con el contenido completo del documento de estructura (agosto 2026). Las propuestas 1 a 4 son la primera ronda; las 5 a 10 siguen el Brand Guide de septiembre 2026 (Poppins y Montserrat, navy #1F3C54, teal #5D9382, coral #EB937D, crema #FAF5EA). Cada propuesta tiene las 6 páginas: Home, Approach, Experience &amp; Cases, About, Network y Contact, más aviso de privacidad, banner de cookies y CTA a Calendly.</p>
<div class="grid">
%s
</div>
<p class="note">Las fotos, el logotipo y el mapa provienen del sitio actual. El formulario de contacto abre un correo a contact@velidadvisory.com (en el sitio final se conecta a un servicio de formularios). Las propuestas están en inglés porque así está redactado el contenido de Carin; el selector NL · EN está previsto en la cabecera y el pie.</p>
</div></body></html>"""

def card(n, name, kicker, desc, bg, c1, c2):
    fg = "#fff" if bg in ("#101B25","#1F3C54","#17293A") else "#1F3C54"
    pages = "".join(f'<a href="{n}/{h}">{l}</a>' for h, l in [("approach.html", "Approach"), ("experience.html", "Experience"), ("about.html", "About"), ("network.html", "Network"), ("contact.html", "Contact")])
    return f"""<article class="card"><div class="sw" style="background:{bg};color:{fg}"><i style="background:{c1}"></i><i style="background:{c2}"></i><i style="background:{bg};border-color:rgba(0,0,0,.25)"></i><b>{n:02d}</b></div>
<div class="body"><h2>Propuesta {n} · {name}</h2><div class="k">{kicker}</div><p>{desc}</p>
<div class="links"><a class="main" href="{n}/index.html">Ver Home</a>{pages}</div></div></article>"""

def build():
    cards = "\n".join(card(*p) for p in PROPS)
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(HTML.replace("%s", cards))

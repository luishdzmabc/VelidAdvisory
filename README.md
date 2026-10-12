# VeliD Advisory · rediseño del sitio

Propuestas de rediseño para velidadvisory.com (Carin Verbree). Octubre 2026.

- `sitio/` HTML estático listo para servir. `index.html` es el índice de las 10 propuestas; `1/`…`10/` cada propuesta con Home, Approach, Experience & Cases, About, Network, Contact y Privacy. `assets/` logo, monograma (favicon), mapa y fotos.
- `generador/` Python sin dependencias. `content.py` tiene todo el copy; `brand.py` la base alineada al brand guide; `p1.py`…`p10.py` cada propuesta. Regenerar con `python3 build.py` (o `python3 build.py p9` para una sola) y luego `python3 -c "import index_page; index_page.build()"`. La salida se escribe directamente en `sitio/`.
- `brand-guide-texto.txt` texto extraído del PDF de la guía.
- Demos publicadas en el VPS de pruebas: http://31.220.85.156/velid/ (ruta `/var/www/html/velid`, servidor default de nginx).

Propuestas 1 a 4: primera ronda (antes de la guía). 5 a 8: mismas ideas alineadas a la guía. 9: la 2 mejorada. 10: forma de la 2 con la paleta clara de la 1.

"""Build the reader's status ledger and figures for GUIA_DE_LECTURA.md.

Standard library only. Reads the audit text, never the audited studies.

    python -B reader_guide_build.py            # print ledger summary and checks
    python -B reader_guide_build.py --write    # also write STATUS_LEDGER_2026-10-28.json and figures/

The current state of each record is NOT parsed from its historical heading
(headings keep the state they had when written). It is the latest disposition
in the audit, stated explicitly below with the round that set it, so a
reader can trace every state back to its source. Checks performed:
  1. every ledger ID appears in the audit (or, for M27-20, in its PR comment);
  2. every ID with a bold heading or table row in the audit is in the ledger;
  3. every local '#anchor' link in the audit, annex and guide resolves
     (GitHub-style heading slugs).
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent / "INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md"
ANNEX = HERE / "ANNEX.md"
GUIDE = HERE / "GUIA_DE_LECTURA.md"

# Normalized state vocabulary used by the guide (see GUIA §3).
STATES = ("ABIERTO", "RESPONDIDO", "CERRADO", "VERIFICADO", "PROPUESTA", "RETIRADO", "INFORMATIVO")
DISPLAY = (  # five display groups for the chart, fixed order
    ("Abierto", ("ABIERTO",)),
    ("Respondido", ("RESPONDIDO",)),
    ("Cerrado o verificado", ("CERRADO", "VERIFICADO")),
    ("Propuesta de mejora", ("PROPUESTA",)),
    ("Retirado o informativo", ("RETIRADO", "INFORMATIVO")),
)

# id, family, severity, state, round that set the state, plain-language summary
LEDGER = [
    ("N-01", "N", "Alta", "ABIERTO", 1, "La nota para el revisor externo no lista todos los PR relevantes."),
    ("N-02", "N", "Media", "ABIERTO", 1, "La nota da a entender que la auditoría #50 cubre PR posteriores que no cubre."),
    ("N-03", "N", "Alta", "ABIERTO", 1, "La nota calla limitaciones que los propios PR ya reconocen."),
    ("N-04", "N", "Alta", "ABIERTO", 1, "La nota no separa lo que hizo una IA de lo que hizo el autor."),
    ("N-05", "N", "Alta", "ABIERTO", 1, "La nota no enumera las afirmaciones concretas que se piden revisar."),
    ("N-06", "N", "Alta", "ABIERTO", 1, "La nota presenta #54 y #57 con más fuerza de la que tienen."),
    ("N-07", "N", "Media", "ABIERTO", 1, "La nota no fija versiones y el material cambia cada día."),
    ("N-08", "N", "Media", "ABIERTO", 1, "La nota usa siglas sin definirlas."),
    ("N-09", "N", "Baja", "ABIERTO", 1, "Faltan datos prácticos: plazo, honorario, confidencialidad, cómo ejecutar."),
    ("F-01", "F", "Alta", "RESPONDIDO", 11, "En #57 el metaprotocolo y el comparador convencional ejecutan el mismo código: empatar no prueba ventaja."),
    ("F-02", "F", "Alta", "ABIERTO", 10, "En el modelo de #57, la única palanca de ventaja agéntica es un coste supuesto e igual para todos."),
    ("F-03", "F", "Media", "RESPONDIDO", 6, "Los recuentos 107/14/39 del barrido dependen de cómo se eligió la rejilla."),
    ("F-04", "F", "Media", "ABIERTO", 2, "En el caso estrella de #57, el comparador convencional obtiene más."),
    ("F-05", "F", "Media", "ABIERTO", 2, "El modelo de #57 es lineal y resta costes sin una tasa de conversión declarada."),
    ("F-06", "F", "Alta", "RESPONDIDO", 11, "Los 46 «experimentos» de #54 son ejemplos calculados a partir de datos fijados."),
    ("F-07", "F", "Baja", "ABIERTO", 2, "Una variable calculada y no usada en el código de #54."),
    ("G-01", "G", "Alta", "RESPONDIDO", 11, "En la campaña de 60 casos, el comparador convencional tiene la respuesta correcta escrita en los datos."),
    ("G-02", "G", "Media", "ABIERTO", 3, "La «auditoría independiente» de Q es un sí/no escrito en los datos."),
    ("G-03", "G", "Media", "ABIERTO", 3, "Varios «microexperimentos» son números escritos a mano, no calculados."),
    ("G-04", "G", "Media", "ABIERTO", 3, "Dos análisis de la campaña repiten la regla que pretenden probar."),
    ("G-05", "G", "Baja", "RESPONDIDO", 6, "#54 repite 8 celdas de red que ya estaban en #49."),
    ("G-06", "G", "Baja", "ABIERTO", 3, "Hay tres cifras distintas de documentos «cribados» (17, 19 y 23)."),
    ("H-01", "H", "Alta", "ABIERTO", 10, "La «trampa» de #42 prohíbe los pasos intermedios; no muestra agentes que elijan quedarse."),
    ("H-02", "H", "Alta", "ABIERTO", 4, "La brecha que crece con n es un supuesto: la misma ecuación en #42, #49 y #54."),
    ("H-03", "H", "Alta", "ABIERTO", 10, "En #43 la información se pierde por cómo se pregunta (censura), no por el anidamiento."),
    ("H-04", "H", "Media", "ABIERTO", 4, "«Sufrimiento estructural» mide una brecha de contribución, no bienestar."),
    ("H-05", "H", "Media", "ABIERTO", 4, "La curva de utilidad de las manzanas está escrita a mano, no derivada."),
    ("H-06", "H", "Informativo", "VERIFICADO", 4, "Las cotas de bits de #43 son correctas."),
    ("I-01", "I", "Alta", "CERRADO", 13, "qualify podía decir «verdadero» con evidencia vacía; corregido en main y reconfirmado."),
    ("M27-01", "M27", "Alta", "CERRADO", 13, "Dos fuentes incompatibles podían dar «verdadero»; corregido en main y reconfirmado."),
    ("M27-02", "M27", "Alta", "CERRADO", 13, "El mismo defecto de tolerancia que I-01; corregido y reconfirmado."),
    ("M27-03", "M27", "Alta", "RESPONDIDO", 12, "#60: la consulta suplementaria debe contar con la observación A ya disponible. Aplicado en la rama de #60."),
    ("M27-04", "M27", "Alta", "RESPONDIDO", 12, "#60 mezclaba numeraciones UC21 y DDS. Aplicado en la rama de #60."),
    ("M27-05", "M27", "—", "INFORMATIVO", 8, "Aclaración de procedencia de R12: TeX original frente a PDF posterior."),
    ("M27-06", "M27", "—", "RETIRADO", 8, "El revisor retiró una alegación de incumplimiento de navegación."),
    ("M27-07", "M27", "Baja", "ABIERTO", 12, "#57: el primer observador puede quedar sin identificar."),
    ("M27-08", "M27", "Baja", "ABIERTO", 12, "El núcleo económico usa convenciones distintas de segunda diferencia."),
    ("M27-09", "M27", "—", "RETIRADO", 8, "El revisor retiró una conclusión demasiado amplia sobre F-01."),
    ("M27-10", "M27", "Alta", "ABIERTO", 8, "R19: la ecuación (4) no mantiene S dentro de [0, H]."),
    ("M27-11", "M27", "Media", "ABIERTO", 8, "La ventana semántica no mejora «todo» estimador, sólo una clase definida."),
    ("M27-12", "M27", "Media", "ABIERTO", 8, "La ventana actual no es automáticamente suficiente frente a toda la historia."),
    ("M27-13", "M27", "Media", "ABIERTO", 8, "Una cota de la señal no acota automáticamente el indicador."),
    ("M27-14", "M27", "Media", "ABIERTO", 8, "D28: ser seguro frente a no hacer nada no implica ser mejor que otra acción."),
    ("M27-15", "M27", "Media", "ABIERTO", 8, "D34: salir una vez de una tolerancia no implica quedarse fuera."),
    ("M27-16", "M27", "Media", "ABIERTO", 8, "Una sobrecarga temporal no implica una cola infinita."),
    ("M27-17", "M27", "—", "INFORMATIVO", 8, "La versión web de D37 ya contiene la aclaración."),
    ("M27-18", "M27", "Media", "ABIERTO", 8, "D37: podar nodos no demuestra atractores estables."),
    ("M27-19", "M27", "—", "PROPUESTA", 8, "D37: especificar dominio y raíz para obtener un precio interpretable."),
    ("M27-20", "M27", "—", "ABIERTO", 8, "Cantor no implica que toda representación fiel sea imposible."),
    ("M27-O1", "M27-O", "—", "PROPUESTA", 8, "Línea de desarrollo: suficiencia de una representación durante una dinámica."),
    ("M27-O2", "M27-O", "—", "PROPUESTA", 8, "Línea de desarrollo: cotas de error ligadas a pregunta y horizonte."),
    ("M27-O3", "M27-O", "—", "PROPUESTA", 8, "Línea de desarrollo: renovación de poblaciones (cohortes)."),
    ("M27-O4", "M27-O", "—", "PROPUESTA", 8, "Línea de desarrollo: colas, plazos y contabilidad sin doble conteo."),
    ("M27-O5", "M27-O", "—", "PROPUESTA", 8, "Línea de desarrollo: ventanas con error, coste y plazo."),
    ("M28-01", "M28", "Alta", "CERRADO", 13, "El redondeo de coma flotante podía certificar «verdadero»; corregido y reconfirmado."),
    ("M28-02", "M28", "Media", "RESPONDIDO", 15, "#60: la guarda no comprobaba que el punto pertenezca al dominio. Corregido en la rama de #60 y reconfirmado; falta incorporarlo a main."),
    ("M28-03", "M28", "Media", "RESPONDIDO", 23, "#60: se aceptaban NaN o infinito como cota de utilidad. Corregido en la rama de #60 y reconfirmado con 32 valores; falta incorporarlo a main."),
    ("M28-04", "M28", "Media", "PROPUESTA", 12, "#60: decidir si la caducidad se mide en la fecha del evento o en la de uso."),
    ("M28-05", "M28", "—", "ABIERTO", 12, "Nombres de pruebas que sugieren una comparación que no existe."),
    ("M28-06", "M28", "—", "INFORMATIVO", 12, "Panel y navegación de la auditoría actualizados."),
    ("M28-07", "M28", "Baja", "PROPUESTA", 12, "Un script de la ronda 8 sobrescribe su JSON si se ejecuta sin --output."),
    ("M28-O1", "M28-O", "—", "PROPUESTA", 12, "Línea de desarrollo: coste esperado de un selector frente a búsqueda exhaustiva."),
    ("M28-O2", "M28-O", "—", "PROPUESTA", 12, "Línea de desarrollo: modelo temporal con versiones de contexto."),
    ("J-01", "J", "Media", "RESPONDIDO", 14, "La cabecera «lectura vigente» estaba desfasada tras la ronda 13."),
    ("J-02", "J", "Media", "RESPONDIDO", 14, "Los encabezados guardan el estado histórico; el vigente no se veía en ningún sitio."),
    ("J-03", "J", "Media", "RESPONDIDO", 14, "Los enlaces a hallazgos se rompían cada vez que cambiaba su estado."),
    ("J-04", "J", "Baja", "RESPONDIDO", 14, "Las rondas no están en orden y la 7 no tiene título propio."),
    ("J-05", "J", "Baja", "RESPONDIDO", 14, "Un mismo defecto tiene hasta cinco nombres: riesgo de contarlo varias veces."),
    ("J-06", "J", "Baja", "RESPONDIDO", 14, "Se usaban más estados de los que la cabecera declaraba."),
    ("J-07", "J", "Baja", "ABIERTO", 14, "El expediente mezcla español e inglés; falta decidir un idioma."),
    ("J-08", "J", "Informativo", "VERIFICADO", 14, "Enlaces internos y versiones fijadas: ninguno roto."),
    ("K-01", "K", "Media", "ABIERTO", 17, "#44: que la cualificación B gane a la inspección dirigida depende del tamaño: con los costes actuales deja de ganar a partir de 128 hojas."),
    ("K-02", "K", "Media", "ABIERTO", 17, "#44: dos certificados B válidos por separado pueden prometer juntos más de lo que cabe por un cuello compartido."),
    ("K-03", "K", "Baja", "ABIERTO", 17, "#44: el informe escribe a mano dos ganancias (2 y 0); son correctas, pero no se calculan."),
    ("K-04", "K", "Informativo", "VERIFICADO", 17, "#44: el mismo A con respuestas futuras distintas, el certificado por trayecto y las cotas de bits son correctos."),
    ("K-05", "K", "Informativo", "VERIFICADO", 17, "#45: el orden derechos > autorización > consentimiento > evidencia es correcto y nunca actúa solo."),
    ("K-06", "K", "Informativo", "VERIFICADO", 17, "#46: equivalentes ciertos, ejemplos y umbral de varianza recalculados: correctos."),
    ("K-07", "K", "Media", "ABIERTO", 17, "#46: compara una media de lotería (14) con un bienestar neto estipulado (17) sin escala común declarada."),
    ("K-08", "K", "—", "PROPUESTA", 17, "#46 ya tiene la elección racional bajo riesgo que pedía H-01: se puede reutilizar para el juego de coordinación."),
    ("L-01", "L", "Baja", "ABIERTO", 23, "#60: una cota de utilidad finita mayor que 1 todavía certifica ganancia, aunque la puntuación está acotada en [0, 1]."),
    ("L-02", "L", "Media", "ABIERTO", 23, "#60: la caducidad de requalify admite NaN y falla con TypeError si falta el campo."),
    ("L-03", "L", "Informativo", "VERIFICADO", 23, "#60: los testigos F1/D1 (10 frente a 8; 11,5 frente a 8,875 con el mismo A) se reproducen desde el código de origen."),
]

FAMILIES = (
    ("N", "Nota al revisor externo"),
    ("F", "Código de #57 y #54"),
    ("G", "Campaña de 60 casos (#48/#49)"),
    ("H", "Modelo social (#42/#43)"),
    ("I", "Defecto de qualify (#45)"),
    ("M27", "Corpus matemático (27 oct)"),
    ("M28", "Relectura (28 oct)"),
    ("M27-O", "Líneas de desarrollo (27 oct)"),
    ("M28-O", "Líneas de desarrollo (28 oct)"),
    ("J", "Forma del expediente (ronda 14)"),
    ("K", "Modelo social #44–#46 (ronda 17)"),
    ("L", "PR #60, recepción (ronda 23)"),
)

# Same defect under several names (aliases across audits)
ALIASES = [
    ("Defecto de qualify (#45)", ["I-01", "D26-F01", "M27-02", "M27-01", "M28-01"], "CERRADO"),
    ("Mismo código en dos brazos (#57)", ["F-01", "F-03", "D26-F03"], "RESPONDIDO"),
    ("Consulta suplementaria (#60)", ["M27-03", "D26-F08", "D26-C04/05"], "RESPONDIDO"),
    ("Numeración UC21/DDS (#60)", ["M27-04", "D26-F09", "D26-C06/07"], "RESPONDIDO"),
    ("Brecha supuesta g·E", ["H-02", "G-05", "F-06 (familia network)"], "ABIERTO"),
]


# ---------------------------------------------------------------- checks
def slug(heading: str) -> str:
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading).replace("`", "").strip().lower()
    keep = "".join(c for c in h if c in "-_ " or unicodedata.category(c)[0] in "LMN" or unicodedata.category(c) == "Pc")
    return keep.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    seen, out, fence = collections.Counter(), set(), False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
        if fence:
            continue
        out.update(re.findall(r'<a id="([^"]+)"></a>', line))
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if m:
            s = slug(m.group(2))
            out.add(s if seen[s] == 0 else f"{s}-{seen[s]}")
            seen[s] += 1
    return out


def broken_local_anchors(path: Path) -> list[str]:
    text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
    bad = []
    for href in re.findall(r"\]\(([^)\s]*#[^)\s]+)\)", text):
        if href.startswith("http"):
            continue
        file_part, frag = href.split("#", 1)
        target = (path.parent / file_part).resolve() if file_part else path
        if target.suffix == ".md" and target.exists() and frag not in anchors(target):
            bad.append(href)
    return bad


def checks() -> dict:
    audit = AUDIT.read_text(encoding="utf-8")
    ids = [row[0] for row in LEDGER]
    missing = [i for i in ids if i != "M27-20" and not re.search(rf"\b{re.escape(i)}\b", audit)]
    declared = set(re.findall(r"^### ([A-Z]-\d\d) ·", audit, re.M)) | set(re.findall(r"^\| (?:<a id=\"[^\"]+\"></a>)?\*\*((?:M2[78]-O?|J-)\d+)\*\* \|", audit, re.M))
    unlisted = sorted(declared - set(ids))
    explicit = set(re.findall(r'<a id="([^"]+)"></a>', audit))
    without_stable_anchor = [i for i in ids if i != "M27-20" and i.lower() not in explicit]
    # Guard against drift between the guide's hand-written totals row and the ledger.
    guide_totals_match = None
    if GUIDE.exists():
        m = re.search(r"^\| \*\*Total\*\* \|(.*)$", GUIDE.read_text(encoding="utf-8"), re.M)
        if m:
            nums = [int(x) for x in re.findall(r"\*\*(\d+)\*\*", m.group(1))]
            want = [sum(sum(r[3] in g for r in LEDGER) for _ in [0]) for _, g in DISPLAY] + [len(LEDGER)]
            guide_totals_match = {"guide": nums, "ledger": want, "ok": nums == want}
    docs = [AUDIT, ANNEX] + ([GUIDE] if GUIDE.exists() else [])
    return {"ledger_ids": len(ids), "duplicate_ids": len(ids) - len(set(ids)),
            "ledger_ids_absent_from_audit": missing, "audit_ids_absent_from_ledger": unlisted,
            "ledger_ids_without_stable_anchor": without_stable_anchor,
            "guide_totals_row": guide_totals_match,
            "broken_local_anchors": {p.name: broken_local_anchors(p) for p in docs}}


# ---------------------------------------------------------------- figures
STYLE = """<style>
  .ink{fill:#0b0b0b}.ink2{fill:#52514e}.bg{fill:#fcfcfb}.grid{stroke:#e4e3df}
  .s0{fill:#2a78d6}.s1{fill:#eb6834}.s2{fill:#1baf7a}.s3{fill:#eda100}.s4{fill:#e87ba4}
  .a0{fill:#2a78d6}.a1{fill:#eb6834}.a0s{stroke:#2a78d6}.a1s{stroke:#eb6834}
  text{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
  @media (prefers-color-scheme: dark){
    .ink{fill:#f0efec}.ink2{fill:#c3c2b7}.bg{fill:#1a1a19}.grid{stroke:#383835}
    .s0{fill:#3987e5}.s1{fill:#d95926}.s2{fill:#199e70}.s3{fill:#c98500}.s4{fill:#d55181}
    .a0{fill:#3987e5}.a1{fill:#d95926}.a0s{stroke:#3987e5}.a1s{stroke:#d95926}
  }
</style>"""


def counts_by_family() -> dict:
    out = {}
    for fam, _ in FAMILIES:
        rows = [r for r in LEDGER if r[1] == fam]
        out[fam] = [sum(r[3] in group for r in rows) for _, group in DISPLAY]
    return out


def fig_status() -> str:
    data = counts_by_family()
    left, top, bar_h, gap, unit = 290, 92, 26, 10, 26
    w = left + 20 * unit + 40
    h = top + len(FAMILIES) * (bar_h + gap) + 96
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Estado de los 79 registros de la auditoría por familia">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="8"/>',
         '<text class="ink" x="16" y="28" font-size="16" font-weight="600">¿Cómo está cada familia de hallazgos? (28 oct 2026)</text>',
         '<text class="ink2" x="16" y="50" font-size="12">Cada barra es una familia de hallazgos. El número de cada tramo dice cuántos registros están en ese estado.</text>',
         '<text class="ink2" x="16" y="68" font-size="12">Estado vigente según la última ronda que lo decidió, no según el encabezado histórico.</text>']
    for i, (fam, name) in enumerate(FAMILIES):
        y = top + i * (bar_h + gap)
        total = sum(data[fam])
        s.append(f'<text class="ink" x="{left - 10}" y="{y + 17}" font-size="12" text-anchor="end">{fam} · {name}</text>')
        x = left
        for k, n in enumerate(data[fam]):
            if not n:
                continue
            wseg = n * unit - 2
            s.append(f'<rect class="s{k}" x="{x}" y="{y}" width="{wseg}" height="{bar_h}" rx="4">'
                     f'<title>{fam}: {n} {DISPLAY[k][0].lower()}</title></rect>')
            s.append(f'<text x="{x + wseg / 2}" y="{y + 17}" font-size="12" font-weight="600" text-anchor="middle" fill="#fff">{n}</text>')
            x += n * unit
        s.append(f'<text class="ink2" x="{x + 6}" y="{y + 17}" font-size="11">{total}</text>')
    yl = h - 58
    for k, (label, _) in enumerate(DISPLAY):
        xl = 16 + (k % 3) * 250
        yy = yl + (k // 3) * 22
        s.append(f'<rect class="s{k}" x="{xl}" y="{yy}" width="14" height="14" rx="3"/>')
        s.append(f'<text class="ink" x="{xl + 20}" y="{yy + 12}" font-size="12">{label}</text>')
    s.append("</svg>")
    return "\n".join(s)


ROUNDS = [  # round, author group (0 Claude, 1 Codex/autor), short label
    (1, 0, "Nota al revisor"), (2, 0, "Código #57/#54"), (3, 0, "Campaña #48/#49"),
    (4, 0, "Modelo social"), (5, 0, "Figuras y referencias"), (6, 0, "Contraste #59; I-01"),
    (7, 1, "Promoción TAX26"), (8, 1, "Corpus matemático"), (9, 1, "Lectura de comparaciones"),
    (10, 1, "Alcance H-01/H-03"), (11, 1, "Arreglo #64, F-06"), (12, 1, "Relectura y cola"),
    (13, 0, "I-01 cerrado"), (14, 0, "Revisión formal y guía"), (15, 0, "M28-02 reconfirmado"), (16, 1, "Cinco mecanismos"), (17, 0, "Modelo social #44–#46"), (18, 0, "Alias precisados"), (19, 0, "Oportunidades de mejora"), (20, 0, "Kit premium 01 README"), (21, 0, "Kit premium 02 MODEL"), (22, 0, "Scripts de verificación"), (23, 0, "PR #60: M28-03 y F1/D1"),
]


def fig_rounds() -> str:
    # Four label lanes (far/near above, near/far below) so labels on the same lane are 4 steps apart.
    w, left, right, y0 = 1200, 80, 80, 178
    step = (w - left - right) / (len(ROUNDS) - 1)
    h = 340
    lanes = ((-1, 70), (1, 46), (-1, 34), (1, 82))  # (direction, label offset)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Línea de tiempo de las {len(ROUNDS)} rondas de auditoría y su autor">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="8"/>',
         '<text class="ink" x="16" y="28" font-size="16" font-weight="600">Las rondas de la auditoría, en orden (26–28 oct 2026)</text>',
         '<text class="ink2" x="16" y="50" font-size="12">En el archivo, las rondas 1–6 aparecen en orden inverso (6, 4, 3, 2, 1) y desde la 7 en orden directo. Aquí van en orden real.</text>',
         f'<line class="grid" x1="{left}" x2="{w - right}" y1="{y0}" y2="{y0}" stroke-width="2"/>']
    for i, (r, a, label) in enumerate(ROUNDS):
        x = left + i * step
        d, off = lanes[i % 4]
        ty = y0 - off if d < 0 else y0 + off
        tick = (off - 12) if d < 0 else (off - 24)
        s.append(f'<line class="a{a}s" x1="{x:.1f}" x2="{x:.1f}" y1="{y0}" y2="{y0 + d * tick}" stroke-width="2"/>')
        s.append(f'<circle class="a{a}" cx="{x:.1f}" cy="{y0}" r="11"><title>Ronda {r}: {label}</title></circle>')
        s.append(f'<text x="{x:.1f}" y="{y0 + 4}" font-size="11" font-weight="700" text-anchor="middle" fill="#fff">{r}</text>')
        s.append(f'<text class="ink" x="{x:.1f}" y="{ty}" font-size="11" text-anchor="middle">{label}</text>')
    for k, (label) in enumerate(("Claude (auditor de IA)", "Codex con observaciones de Iván (IA)")):
        xl = 16 + k * 260
        s.append(f'<circle class="a{k}" cx="{xl + 7}" cy="{h - 30}" r="7"/>')
        s.append(f'<text class="ink" x="{xl + 20}" y="{h - 26}" font-size="12">{label}</text>')
    s.append(f'<text class="ink2" x="{w - 16}" y="{h - 26}" font-size="11" text-anchor="end">Ninguna ronda es una revisión humana independiente.</text>')
    s.append("</svg>")
    return "\n".join(s)


M27_20_URL = "https://github.com/dakleyer/structural-awareness-contributions/pull/58#issuecomment-6446350643"
STATE_LABEL = {"ABIERTO": "🔵 Abierto", "RESPONDIDO": "🟠 Respondido", "CERRADO": "🟢 Cerrado",
               "VERIFICADO": "🟢 Verificado", "PROPUESTA": "🟡 Propuesta", "RETIRADO": "⚪ Retirado",
               "INFORMATIVO": "⚪ Informativo"}


def ledger_markdown() -> str:
    """Per-family tables, generated so the guide never drifts from the ledger."""
    parts = []
    for fam, name in FAMILIES:
        rows = [r for r in LEDGER if r[1] == fam]
        open_n = sum(r[3] == "ABIERTO" for r in rows)
        parts.append(f"<details><summary><b>{fam} · {name}</b> — {len(rows)} registros, {open_n} abiertos</summary>\n")
        parts.append("| ID | Estado | Gravedad | En pocas palabras | Ronda que fijó el estado |")
        parts.append("|---|---|---|---|---|")
        for i, f, sev, st, rd, txt in rows:
            link = M27_20_URL if i == "M27-20" else f"../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#{i.lower()}"
            parts.append(f"| [{i}]({link}) | {STATE_LABEL[st]} | {sev} | {txt} | {rd} |")
        parts.append("\n</details>\n")
    return "\n".join(parts)


def write_guide_table() -> bool:
    if not GUIDE.exists():
        return False
    text = GUIDE.read_text(encoding="utf-8")
    begin, end = "<!-- LEDGER:BEGIN (generado por reader_guide_build.py) -->", "<!-- LEDGER:END -->"
    if begin not in text or end not in text:
        return False
    head, rest = text.split(begin, 1)
    _, tail = rest.split(end, 1)
    GUIDE.write_text(head + begin + "\n\n" + ledger_markdown() + "\n" + end + tail, encoding="utf-8")
    return True


def fig_k01() -> str:
    """Net synthetic value of B and targeted inspection versus number of leaves (#44 constants)."""
    w, h, l, r, t, b = 700, 380, 64, 170, 84, 56
    ns = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
    import math as _m
    X = lambda n: l + (_m.log2(n) - 2) / 8 * (w - l - r)
    ymin, ymax = 5.5, 8.5
    Y = lambda v: t + (ymax - v) / (ymax - ymin) * (h - t - b)
    depth = lambda n: int(_m.log2(n)) + 2
    vB = lambda n: 10 - (0.25 * depth(n) + 0.75)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Valor neto de B y de la inspección dirigida frente al número de hojas">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="8"/>',
         '<text class="ink" x="16" y="28" font-size="16" font-weight="600">K-01 · ¿Hasta qué tamaño gana la cualificación B?</text>',
         '<text class="ink2" x="16" y="50" font-size="12">Valor neto para una pregunta (#44, costes por defecto). B paga 0,25 por nodo del trayecto + 0,75;</text>',
         '<text class="ink2" x="16" y="66" font-size="12">la inspección dirigida paga 3 fijo. La ampliación completa (−22 con 16 hojas) queda fuera del gráfico.</text>']
    for v in (6, 6.5, 7, 7.5, 8, 8.5):
        s.append(f'<line class="grid" x1="{l}" x2="{w - r}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke-width="1"/>')
        s.append(f'<text class="ink2" x="{l - 8}" y="{Y(v) + 4:.1f}" font-size="11" text-anchor="end">{str(v).replace(".", ",")}</text>')
    for n in ns:
        s.append(f'<text class="ink2" x="{X(n):.1f}" y="{h - b + 18}" font-size="11" text-anchor="middle">{n}</text>')
    s.append(f'<text class="ink2" x="{(l + w - r) / 2}" y="{h - 14}" font-size="12" text-anchor="middle">número de hojas (escala logarítmica)</text>')
    s.append(f'<line class="a1s" x1="{X(4):.1f}" x2="{X(1024):.1f}" y1="{Y(7):.1f}" y2="{Y(7):.1f}" stroke-width="2"/>')
    pts = " ".join(f"{X(n):.1f},{Y(vB(n)):.1f}" for n in ns)
    s.append(f'<polyline class="a0s" fill="none" stroke-width="2" points="{pts}"/>')
    for n in ns:
        s.append(f'<circle class="a0" cx="{X(n):.1f}" cy="{Y(vB(n)):.1f}" r="4"><title>{n} hojas: B {vB(n):.2f} · dirigida 7,00</title></circle>')
    s.append(f'<text class="ink" x="{w - r + 8}" y="{Y(vB(1024)) + 4:.1f}" font-size="12">B situado</text>')
    s.append(f'<text class="ink" x="{w - r + 8}" y="{Y(7) - 6:.1f}" font-size="12">Inspección dirigida</text>')
    s.append(f'<line class="grid" x1="{X(128):.1f}" x2="{X(128):.1f}" y1="{t}" y2="{h - b}" stroke-width="1" stroke-dasharray="4 4"/>')
    s.append(f'<text class="ink" x="{X(128) + 6:.1f}" y="{t + 14}" font-size="11">empate en 128 hojas</text>')
    s.append(f'<text class="ink2" x="{X(16) + 6:.1f}" y="{Y(vB(16)) - 10:.1f}" font-size="11">caso del README (16)</text>')
    s.append("</svg>")
    return "\n".join(s)


# Improvement opportunities (ronda 19): id, short name, impact, effort, related records
OPPORTUNITIES = [
    ("OP-01", "Reescribir la nota al revisor", "Alto", "Bajo", "N-01…N-09"),
    ("OP-02", "Juego de coordinación con piezas existentes", "Alto", "Bajo", "H-01, K-08"),
    ("OP-03", "Pruebas con oráculo exacto para cada certificado", "Alto", "Bajo", "I-01, M28-01, K-02"),
    ("OP-04", "Certificado B conjunto o reserva de holgura", "Medio", "Medio", "K-02"),
    ("OP-05", "Informar regiones, no un solo caso", "Medio", "Bajo", "F-03, K-01"),
    ("OP-06", "Escala común declarada", "Medio", "Bajo", "F-05, K-07"),
    ("OP-07", "Todo número publicado sale de una función", "Medio", "Bajo", "G-03, K-03"),
    ("OP-08", "Comparadores que deciden con lo que observan", "Alto", "Alto", "G-01, F-01, R16-P04"),
    ("OP-09", "Brecha derivada de un mecanismo medible", "Alto", "Medio", "H-02"),
    ("OP-10", "Prueba de profundidad y acceso", "Alto", "Medio", "H-03"),
    ("OP-11", "Herramientas de auditoría en la CI", "Medio", "Bajo", "J-08, R16-P01, R16-P07"),
    ("OP-12", "Decidir el idioma del expediente", "Medio", "Bajo", "J-07"),
    ("OP-13", "Paquete para revisión humana independiente", "Alto", "Medio", "N-*, OP-01"),
]


def fig_opportunities() -> str:
    efforts, impacts = ("Bajo", "Medio", "Alto"), ("Alto", "Medio")
    l, t, cw, ch = 110, 96, 300, 230
    w, h = l + 3 * cw + 24, t + 2 * ch + 70
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Matriz de impacto y esfuerzo de las 13 oportunidades de mejora">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="8"/>',
         '<text class="ink" x="16" y="28" font-size="16" font-weight="600">Oportunidades de mejora: impacto frente a esfuerzo</text>',
         '<text class="ink2" x="16" y="50" font-size="12">Arriba a la izquierda, lo que más ayuda con menos trabajo. Cada etiqueta es una oportunidad de la sección 14 de la guía.</text>']
    for j, e in enumerate(efforts):
        s.append(f'<text class="ink" x="{l + j * cw + cw / 2}" y="{t - 12}" font-size="13" font-weight="600" text-anchor="middle">Esfuerzo {e.lower()}</text>')
    for i, imp in enumerate(impacts):
        y0 = t + i * ch
        s.append(f'<text class="ink" x="{l - 14}" y="{y0 + ch / 2}" font-size="13" font-weight="600" text-anchor="end">Impacto</text>')
        s.append(f'<text class="ink" x="{l - 14}" y="{y0 + ch / 2 + 17}" font-size="13" font-weight="600" text-anchor="end">{imp.lower()}</text>')
        for j, e in enumerate(efforts):
            x0 = l + j * cw
            cls = "a0" if (imp, e) == ("Alto", "Bajo") else "grid"
            fill = ' fill-opacity="0.12"' if cls == "a0" else ' fill="none"'
            s.append(f'<rect class="{cls}" x="{x0 + 4}" y="{y0 + 4}" width="{cw - 8}" height="{ch - 8}" rx="8"{fill} stroke="#c3c2b7" stroke-width="1"/>')
            if (imp, e) == ("Alto", "Bajo"):
                s.append(f'<text class="ink" x="{x0 + 16}" y="{y0 + 26}" font-size="12" font-weight="700">Empezar aquí</text>')
            items = [o for o in OPPORTUNITIES if o[2] == imp and o[3] == e]
            for k, (oid, name, *_rest) in enumerate(items):
                yy = y0 + 52 + k * 36
                s.append(f'<rect class="a0" x="{x0 + 14}" y="{yy - 15}" width="54" height="22" rx="11"/>')
                s.append(f'<text x="{x0 + 41}" y="{yy}" font-size="11" font-weight="700" text-anchor="middle" fill="#fff">{oid}</text>')
                words, lines_, cur = name.split(), [], ""
                for wd in words:  # wrap at ~30 characters, never truncate
                    if cur and len(cur) + 1 + len(wd) > 30:
                        lines_.append(cur); cur = wd
                    else:
                        cur = f"{cur} {wd}".strip()
                lines_.append(cur)
                for li, txt in enumerate(lines_):
                    s.append(f'<text class="ink" x="{x0 + 76}" y="{yy + li * 14 - (7 if len(lines_) > 1 else 0)}" font-size="11">{txt}</text>')
    s.append(f'<text class="ink2" x="16" y="{h - 16}" font-size="11">Impacto y esfuerzo son estimaciones del auditor (IA) para ordenar el trabajo; no son mediciones.</text>')
    s.append("</svg>")
    return "\n".join(s)


def build() -> dict:
    totals = collections.Counter(r[3] for r in LEDGER)
    return {"schema": "ACC-AUDIT-STATUS-LEDGER-v0.1", "as_of": "2026-10-28",
            "source": f"INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md rounds 1-{max(r[0] for r in ROUNDS)}",
            "state_vocabulary": list(STATES), "totals": {s: totals.get(s, 0) for s in STATES},
            "by_family_display_groups": {"groups": [g for g, _ in DISPLAY], "counts": counts_by_family()},
            "records": [dict(id=i, family=f, severity=sev, state=st, set_in_round=rd, summary=txt)
                        for i, f, sev, st, rd, txt in LEDGER],
            "aliases": [dict(defect=d, ids=ids, state=st) for d, ids, st in ALIASES],
            "checks": checks(),
            "note": "AI-assisted reading aid. States summarize the audit's own dispositions; they are not independent human validation."}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args(argv)
    if a.write:
        write_guide_table()
    result = build()
    if a.write:
        (HERE / "STATUS_LEDGER_2026-10-28.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (HERE / "figures").mkdir(exist_ok=True)
        (HERE / "figures" / "STATUS_by_family.svg").write_text(fig_status(), encoding="utf-8")
        (HERE / "figures" / "ROUNDS_timeline.svg").write_text(fig_rounds(), encoding="utf-8")
        (HERE / "figures" / "K01_B_vs_targeted_by_size.svg").write_text(fig_k01(), encoding="utf-8")
        (HERE / "figures" / "OPPORTUNITIES_impact_effort.svg").write_text(fig_opportunities(), encoding="utf-8")
    print(json.dumps({"totals": result["totals"], "checks": result["checks"]}, ensure_ascii=False, indent=2))
    c = result["checks"]  # R16-P07 (Codex, ronda 16): fail on any structural inconsistency
    if (c["duplicate_ids"] or c["ledger_ids_absent_from_audit"] or c["audit_ids_absent_from_ledger"]
            or c["ledger_ids_without_stable_anchor"] or any(c["broken_local_anchors"].values())
            or (c.get("guide_totals_row") and not c["guide_totals_row"]["ok"])):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

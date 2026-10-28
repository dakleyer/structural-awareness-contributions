"""Figures for the premium edition kit of the ACC auxiliary-model corpus.

Standard library only; writes SVG into premium/figures/. Each figure has a
table view in the matching PROPUESTA document. Palette: validated reference
instance (light and dark), same as the reader's guide.

    python -B build_premium_figures.py
"""
from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "figures"

STYLE = """<style>
  .ink{fill:#0b0b0b}.ink2{fill:#52514e}.bg{fill:#fcfcfb}.card{fill:#f4f3f0;stroke:#d7d6d0}
  .line{stroke:#c3c2b7}.s0{fill:#2a78d6}.s1{fill:#eb6834}.s2{fill:#1baf7a}.s3{fill:#eda100}
  .s0s{stroke:#2a78d6}.s1s{stroke:#eb6834}.s2s{stroke:#1baf7a}.s3s{stroke:#eda100}
  text{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
  @media (prefers-color-scheme: dark){
    .ink{fill:#f0efec}.ink2{fill:#c3c2b7}.bg{fill:#1a1a19}.card{fill:#262624;stroke:#3d3d3a}.line{stroke:#5a5a55}
    .s0{fill:#3987e5}.s1{fill:#d95926}.s2{fill:#199e70}.s3{fill:#c98500}
    .s0s{stroke:#3987e5}.s1s{stroke:#d95926}.s2s{stroke:#199e70}.s3s{stroke:#c98500}
  }
</style>"""


def wrap(text: str, width: int) -> list[str]:
    lines, cur = [], ""
    for word in text.split():
        if cur and len(cur) + 1 + len(word) > width:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    return lines + [cur] if cur else lines


# ------------------------------------------------------------------ figure 1
# Development route stated in README «Ruta de desarrollo», with the status of
# each stage as documented in the corpus on 28-10-2026.
STAGES = [
    ("Modelo acotado", "HECHO", "MODEL.md, núcleo técnico y 11 estudios v0.1 en main"),
    ("Preguntas y comparadores (DDS)", "CANDIDATO", "Programa DDS candidato; un piloto determinista ejecutado el 25-10"),
    ("Casos y oráculos", "SINTÉTICO", "Fixtures sintéticos y oráculos privados de laboratorio"),
    ("Arquitectura e implementación del estudio", "PENDIENTE", "Sin implementación de estudio fuera del laboratorio"),
    ("Ejecución y efectos", "PENDIENTE", "Sin ejecución nativa ni efectos observados"),
    ("Revisión de resultados", "EN CURSO", "Auditoría asistida por IA (PR #58); revisión humana pendiente"),
]
STATUS = {  # label, class, glyph (shape carries meaning without colour)
    "HECHO": ("Hecho", "s2", "●"),
    "CANDIDATO": ("Candidato", "s3", "◐"),
    "SINTÉTICO": ("Sólo sintético", "s3", "◐"),
    "PENDIENTE": ("Pendiente", None, "○"),
    "EN CURSO": ("En curso (IA)", "s0", "◐"),
}


def fig_route() -> str:
    n = len(STAGES)
    cw, gap, l, t = 196, 18, 24, 110
    w = l * 2 + n * cw + (n - 1) * gap
    h = 344
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Ruta de desarrollo del modelo auxiliar ACC y estado de cada etapa">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="10"/>',
         '<text class="ink" x="24" y="34" font-size="18" font-weight="650">Ruta de desarrollo: dónde está el modelo hoy</text>',
         '<text class="ink2" x="24" y="58" font-size="13">Las seis etapas que declara el README, con el estado documentado en el corpus el 28 de octubre de 2026.</text>',
         '<text class="ink2" x="24" y="78" font-size="13">Círculo lleno: hecho · medio círculo: en parte · círculo vacío: pendiente. El texto de cada tarjeta dice qué existe.</text>']
    for i, (name, st, note) in enumerate(STAGES):
        x = l + i * (cw + gap)
        label, cls, glyph = STATUS[st]
        s.append(f'<rect class="card" x="{x}" y="{t}" width="{cw}" height="184" rx="10" stroke-width="1"/>')
        if cls:
            s.append(f'<rect class="{cls}" x="{x}" y="{t}" width="{cw}" height="6" rx="3"/>')
        s.append(f'<text class="ink2" x="{x + 14}" y="{t + 30}" font-size="12" font-weight="600">ETAPA {i + 1}</text>')
        for k, ln in enumerate(wrap(name, 22)):
            s.append(f'<text class="ink" x="{x + 14}" y="{t + 54 + k * 18}" font-size="14" font-weight="650">{ln}</text>')
        cx, cy, r = x + 21, t + 117, 6
        mark = "s2" if glyph == "●" else ("s3" if cls == "s3" else "s0")
        if glyph == "●":
            s.append(f'<circle class="{mark}" cx="{cx}" cy="{cy}" r="{r}"/>')
        elif glyph == "◐":
            s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" class="{mark}s" stroke-width="2"/>')
            s.append(f'<path class="{mark}" d="M{cx} {cy - r} A{r} {r} 0 0 0 {cx} {cy + r} Z"/>')
        else:
            s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" class="line" stroke-width="2"/>')
        s.append(f'<text class="ink" x="{x + 34}" y="{cy + 5}" font-size="13">{label}</text>')
        for k, ln in enumerate(wrap(note, 28)):
            s.append(f'<text class="ink2" x="{x + 14}" y="{t + 142 + k * 15}" font-size="11">{ln}</text>')
        if i < n - 1:
            ax = x + cw + 2
            s.append(f'<path class="line" d="M{ax} {t + 85} l{gap - 6} 0 m-5 -5 l5 5 l-5 5" fill="none" stroke-width="2"/>')
    s.append(f'<text class="ink2" x="24" y="{h - 18}" font-size="11">Fuente: README del modelo auxiliar (Ruta de desarrollo) y estado de los estudios en main 51fc686. Ninguna etapa 4–5 se ha iniciado fuera del laboratorio.</text>')
    s.append("</svg>")
    return "\n".join(s)


# ------------------------------------------------------------------ figure 2
# Package map: documents grouped by what the reader wants to do.
GROUPS = [
    ("Entender", "s0", ["Pregunta principal (README)", "MODEL.md — modelo integrado", "Núcleo técnico económico", "CASES.md — casos y dimensiones", "Textos completos (model/01–04)"]),
    ("Comprobar", "s2", ["11 estudios en main", "RESEARCH_STATUS.md", "REVIEW_AND_COVERAGE.md", "Auditoría incremental (PR #58)"]),
    ("Planificar", "s3", ["STUDY_SPECIFICATION.md", "DDS_EVALUATION_PLAN.md", "Contrato UC21/DDS (toy)", "Nota 01K-A02 (HID)"]),
    ("Procedencia y límites", "s1", ["SOURCES_AND_COVERAGE.md", "ACC_BOUNDARY.md", "review/ — acciones y conceptos", "Aclaraciones de Iván"]),
]


def fig_map() -> str:
    cw, gap, l, t = 250, 18, 24, 104
    w = l * 2 + 4 * cw + 3 * gap
    h = 360
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Mapa del paquete del modelo auxiliar ACC por objetivo del lector">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="10"/>',
         '<text class="ink" x="24" y="34" font-size="18" font-weight="650">Mapa del paquete: qué leer según lo que quieras hacer</text>',
         '<text class="ink2" x="24" y="58" font-size="13">Los mismos documentos de la tabla «Cómo leerlo», agrupados por objetivo del lector. Ningún documento cambia de sitio.</text>',
         '<text class="ink2" x="24" y="78" font-size="13">Recorrido recomendado de izquierda a derecha; cada columna puede leerse por separado.</text>']
    for i, (title, cls, items) in enumerate(GROUPS):
        x = l + i * (cw + gap)
        s.append(f'<rect class="card" x="{x}" y="{t}" width="{cw}" height="{h - t - 36}" rx="10" stroke-width="1"/>')
        s.append(f'<rect class="{cls}" x="{x}" y="{t}" width="{cw}" height="40" rx="10"/>')
        s.append(f'<rect class="{cls}" x="{x}" y="{t + 24}" width="{cw}" height="16"/>')
        s.append(f'<text x="{x + 16}" y="{t + 26}" font-size="15" font-weight="700" fill="#fff">{i + 1} · {title}</text>')
        for k, item in enumerate(items):
            yy = t + 68 + k * 36
            s.append(f'<circle class="{cls}" cx="{x + 20}" cy="{yy - 4}" r="4"/>')
            s.append(f'<text class="ink" x="{x + 32}" y="{yy}" font-size="12.5">{item}</text>')
    s.append(f'<text class="ink2" x="24" y="{h - 14}" font-size="11">Propuesta de diseño para la portada del README; los enlaces reales están en la tabla equivalente de la propuesta.</text>')
    s.append("</svg>")
    return "\n".join(s)


# ------------------------------------------------------------------ MODEL.md figures (entrega 02)
SPINE = [  # MODEL.md «secuencia de lectura» and the sections that develop each step
    ("Mejora posible", "s0", ["Pregunta y alcance", "Núcleo económico del modelo", "Fines y capacidades"]),
    ("Dimensiones y acuerdo", "s0", ["Del caso de una dimensión al modelo abierto", "Dos hipótesis distintas (H1, H2)", "A/B/C/D como frontera intrínseca"]),
    ("Reajuste o bloqueo", "s3", ["Propuestas, aceptación y reajuste", "Rediseño y transición humana"]),
    ("Efectos sobre utilidad, bienestar y capacidades", "s1", ["Utilidad, bienestar y frustración", "Aversión al riesgo (RAV-01)", "Dinero, garantías y opcionalidad"]),
    ("Contraste temporal", "s2", ["Error, irreversibilidad y tiempo", "Redes y efectos de segundo orden", "Fundamento epistémico"]),
]


def fig_model_spine() -> str:
    n = len(SPINE)
    cw, gap, l, t = 230, 16, 24, 104
    w = l * 2 + n * cw + (n - 1) * gap
    h = 372
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Columna vertebral de MODEL.md: cinco pasos y sus secciones">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="10"/>',
         '<text class="ink" x="24" y="34" font-size="18" font-weight="650">La columna vertebral de MODEL.md</text>',
         '<text class="ink2" x="24" y="58" font-size="13">La «secuencia de lectura» que declara el propio documento, con las secciones que desarrollan cada paso.</text>',
         '<text class="ink2" x="24" y="78" font-size="13">Las perspectivas epistemológica, institucional, humana y ética ayudan a formular y probar la secuencia; no la sustituyen.</text>']
    for i, (step, cls, secs) in enumerate(SPINE):
        x = l + i * (cw + gap)
        s.append(f'<rect class="card" x="{x}" y="{t}" width="{cw}" height="{h - t - 40}" rx="10" stroke-width="1"/>')
        s.append(f'<rect class="{cls}" x="{x}" y="{t}" width="{cw}" height="6" rx="3"/>')
        s.append(f'<text class="ink2" x="{x + 14}" y="{t + 28}" font-size="12" font-weight="600">PASO {i + 1}</text>')
        for k, ln in enumerate(wrap(step, 24)):
            s.append(f'<text class="ink" x="{x + 14}" y="{t + 50 + k * 18}" font-size="14" font-weight="650">{ln}</text>')
        y = t + 104
        for sec in secs:
            for k, ln in enumerate(wrap(sec, 30)):
                if k == 0:
                    s.append(f'<circle class="{cls}" cx="{x + 18}" cy="{y - 4}" r="3.5"/>')
                s.append(f'<text class="ink" x="{x + 28}" y="{y}" font-size="11.5">{ln}</text>')
                y += 15
            y += 8
        if i < n - 1:
            ax = x + cw + 2
            s.append(f'<path class="line" d="M{ax} {t + 60} l{gap - 6} 0 m-5 -5 l5 5 l-5 5" fill="none" stroke-width="2"/>')
    s.append(f'<text class="ink2" x="24" y="{h - 14}" font-size="11">Fuente: MODEL.md, «Núcleo económico del modelo» (secuencia de lectura) y sus encabezados en main 51fc686.</text>')
    s.append("</svg>")
    return "\n".join(s)


def fig_same_A() -> str:
    """Two worlds with the same current A=128 and a different answer tomorrow (MODEL.md, #44)."""
    w, h = 980, 360
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Dos mundos con el mismo A hoy y distinta respuesta mañana">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="10"/>',
         '<text class="ink" x="24" y="34" font-size="18" font-weight="650">Mismo A hoy, distinto mañana</text>',
         '<text class="ink2" x="24" y="58" font-size="13">Ejemplo de MODEL.md (16 fuentes). Hoy los dos mundos entregan A = 128. Mañana se pide +2 a la fuente 3.</text>']
    for j, (title, root_label, out_label, cls, note) in enumerate((
            ("Mundo 1: sin cuello en la raíz", "Raíz sin límite", "Mañana: 130", "s2", "La fuente 3 puede dar 10 y la raíz lo deja pasar."),
            ("Mundo 2: cuello en la raíz (128)", "Raíz: máximo 128", "Mañana: 128", "s1", "La fuente 3 puede dar 10, pero la raíz ya está llena."))):
        x0 = 24 + j * 476
        s.append(f'<rect class="card" x="{x0}" y="80" width="456" height="250" rx="10" stroke-width="1"/>')
        s.append(f'<text class="ink" x="{x0 + 16}" y="106" font-size="14" font-weight="650">{title}</text>')
        rx, ry = x0 + 228, 150
        s.append(f'<rect class="{cls}" x="{rx - 80}" y="{ry - 18}" width="160" height="30" rx="15"/>')
        s.append(f'<text x="{rx}" y="{ry + 2}" font-size="12" font-weight="700" text-anchor="middle" fill="#fff">{root_label}</text>')
        for k in range(16):
            lx = x0 + 30 + k * 26
            s.append(f'<path class="line" d="M{lx} 220 L{rx} {ry + 12}" stroke-width="1" fill="none"/>')
            hi = k in (3, 8, 12)
            s.append(f'<circle class="{"s0" if k == 3 else "card"}" cx="{lx}" cy="228" r="9" stroke-width="1"/>')
            s.append(f'<text class="{"ink" if k != 3 else ""}" x="{lx}" y="232" font-size="9" text-anchor="middle"{" fill=\"#fff\"" if k == 3 else ""}>{10 if hi else 8}</text>')
        s.append(f'<text class="ink2" x="{x0 + 16}" y="262" font-size="11">Capacidad de cada fuente (8 o 10). Hoy se pide 8 a todas: A = 16 × 8 = 128.</text>')
        s.append(f'<text class="ink" x="{x0 + 16}" y="290" font-size="14" font-weight="650">{out_label}</text>')
        s.append(f'<text class="ink2" x="{x0 + 16}" y="310" font-size="11">{note}</text>')
    s.append(f'<text class="ink2" x="24" y="{h - 10}" font-size="11">Desde A sólo no se distinguen. Hace falta evidencia adicional legítima (B) o una inspección adecuada. Estudio: intrinsic-abcd-economics-v0.1 (#44).</text>')
    s.append("</svg>")
    return "\n".join(s)


def fig_rav01() -> str:
    """Certainty equivalents of RAV-01's late example: mean minus risk penalty minus cost."""
    rows = [("S · quedarse", 14.0, 1.0, 0.0), ("R · rediseñar", 25.0, 16.0, 0.0), ("D · defender", 14.0, 0.25, 0.5)]
    w, h, l, t, unit = 900, 330, 150, 96, 26
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Equivalentes ciertos de quedarse, rediseñar y defender en RAV-01">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="10"/>',
         '<text class="ink" x="24" y="34" font-size="18" font-weight="650">RAV-01: por qué quedarse puede ser racional aunque cambiar rinda más</text>',
         '<text class="ink2" x="24" y="58" font-size="13">Equivalente cierto = media − penalización por riesgo (γ/2 · varianza, γ = 0,5) − coste. Testigo «tardío» de MODEL.md y #46.</text>']
    for i, (name, mu, pen, cost) in enumerate(rows):
        y = t + i * 66
        ce = mu - pen - cost
        s.append(f'<text class="ink" x="{l - 12}" y="{y + 22}" font-size="13" font-weight="600" text-anchor="end">{name}</text>')
        s.append(f'<rect class="s0" x="{l}" y="{y}" width="{ce * unit - 2}" height="32" rx="4"><title>{name}: equivalente cierto {ce:g}</title></rect>')
        s.append(f'<text x="{l + 10}" y="{y + 21}" font-size="12" font-weight="700" fill="#fff">CE {str(ce).replace(".", ",").rstrip("0").rstrip(",")}</text>')
        x = l + ce * unit
        if pen:
            s.append(f'<rect class="s1" x="{x}" y="{y}" width="{pen * unit - 2}" height="32" rx="4" fill-opacity="0.85"/>')
            if pen * unit > 60:
                s.append(f'<text x="{x + 8}" y="{y + 21}" font-size="11" font-weight="600" fill="#fff">riesgo −{str(pen).replace(".", ",").rstrip("0").rstrip(",")}</text>')
            x += pen * unit
        if cost:
            s.append(f'<rect class="s3" x="{x}" y="{y}" width="{cost * unit - 2}" height="32" rx="4"/>')
            x += cost * unit
        s.append(f'<text class="ink2" x="{x + 8}" y="{y + 21}" font-size="11">media {str(mu).replace(".", ",").rstrip("0").rstrip(",")}{" · coste 0,5 · riesgo 0,25" if cost else ""}</text>')
    for k, (cls, lab) in enumerate((("s0", "Equivalente cierto (lo que vale con seguridad)"), ("s1", "Penalización por riesgo"), ("s3", "Coste de defender"))):
        s.append(f'<rect class="{cls}" x="{24 + k * 290}" y="{h - 40}" width="14" height="14" rx="3"/>')
        s.append(f'<text class="ink" x="{44 + k * 290}" y="{h - 28}" font-size="12">{lab}</text>')
    s.append(f'<text class="ink2" x="24" y="{h - 8}" font-size="11">Rediseñar tiene la media más alta (25) pero el menor equivalente cierto (9): su incertidumbre pesa más. Defender (13,25) supera a quedarse (13).</text>')
    s.append("</svg>")
    return "\n".join(s)


def fig_consent() -> str:
    """Probability that v independent parties all consent, q=0.9, versus perfectly correlated."""
    import math as _m
    w, h, l, r, t, b = 820, 400, 64, 190, 84, 96
    vmax = 30
    X = lambda v: l + (v - 1) / (vmax - 1) * (w - l - r)
    Y = lambda p: t + (1 - p) * (h - t - b)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Probabilidad de que todas las partes consientan frente a su número">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="10"/>',
         '<text class="ink" x="24" y="34" font-size="18" font-weight="650">q^v: cuántos «sí» hacen falta</text>',
         '<text class="ink2" x="24" y="58" font-size="13">Probabilidad de que v partes consientan si cada una dice «sí» con q = 0,9 (MODEL.md, «Redes…»).</text>']
    for p in (0, 0.25, 0.5, 0.75, 1.0):
        s.append(f'<line class="line" x1="{l}" x2="{w - r}" y1="{Y(p):.1f}" y2="{Y(p):.1f}" stroke-width="0.6"/>')
        s.append(f'<text class="ink2" x="{l - 8}" y="{Y(p) + 4:.1f}" font-size="11" text-anchor="end">{int(p * 100)} %</text>')
    for v in (1, 5, 10, 15, 20, 25, 30):
        s.append(f'<text class="ink2" x="{X(v):.1f}" y="{h - b + 18}" font-size="11" text-anchor="middle">{v}</text>')
    s.append(f'<text class="ink2" x="{(l + w - r) / 2}" y="{h - b + 40}" font-size="12" text-anchor="middle">v (número de partes cuyo consentimiento hace falta)</text>')
    s.append(f'<line class="s1s" x1="{X(1):.1f}" x2="{X(vmax):.1f}" y1="{Y(0.9):.1f}" y2="{Y(0.9):.1f}" stroke-width="2"/>')
    pts = " ".join(f"{X(v):.1f},{Y(0.9 ** v):.1f}" for v in range(1, vmax + 1))
    s.append(f'<polyline class="s0s" fill="none" stroke-width="2" points="{pts}"/>')
    s.append(f'<circle class="s0" cx="{X(20):.1f}" cy="{Y(0.9 ** 20):.1f}" r="5"><title>v = 20: 0,9^20 = 0,1216</title></circle>')
    s.append(f'<text class="ink" x="{X(20) + 8:.1f}" y="{Y(0.9 ** 20) - 10:.1f}" font-size="12">v = 20 → 12,16 %</text>')
    s.append(f'<text class="ink" x="{w - r + 8}" y="{Y(0.9) + 4:.1f}" font-size="12">respuestas idénticas: 90 %</text>')
    s.append(f'<text class="ink" x="{w - r + 8}" y="{Y(0.9 ** vmax) + 4:.1f}" font-size="12">independientes: q^v</text>')
    s.append(f'<text class="ink2" x="24" y="{h - 14}" font-size="11">Los dos extremos de MODEL.md. Entre ambos: correlación, delegación, sustitución, negociación o gobierno conjunto, que el estudio debe variar.</text>')
    s.append("</svg>")
    return "\n".join(s)


def main() -> int:
    OUT.mkdir(exist_ok=True)
    (OUT / "README_route_status.svg").write_text(fig_route(), encoding="utf-8")
    (OUT / "README_package_map.svg").write_text(fig_map(), encoding="utf-8")
    (OUT / "MODEL_spine.svg").write_text(fig_model_spine(), encoding="utf-8")
    (OUT / "MODEL_same_A_two_worlds.svg").write_text(fig_same_A(), encoding="utf-8")
    (OUT / "MODEL_rav01_certainty_equivalents.svg").write_text(fig_rav01(), encoding="utf-8")
    (OUT / "MODEL_consent_q_power_v.svg").write_text(fig_consent(), encoding="utf-8")
    print("written:", sorted(p.name for p in OUT.glob("*.svg")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

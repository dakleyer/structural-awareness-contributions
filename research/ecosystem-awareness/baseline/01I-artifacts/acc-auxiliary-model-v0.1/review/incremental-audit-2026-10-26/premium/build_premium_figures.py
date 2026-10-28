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


def main() -> int:
    OUT.mkdir(exist_ok=True)
    (OUT / "README_route_status.svg").write_text(fig_route(), encoding="utf-8")
    (OUT / "README_package_map.svg").write_text(fig_map(), encoding="utf-8")
    print("written:", sorted(p.name for p in OUT.glob("*.svg")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

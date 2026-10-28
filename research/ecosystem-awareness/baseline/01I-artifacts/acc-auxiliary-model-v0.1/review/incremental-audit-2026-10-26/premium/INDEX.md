# Kit de edición premium del corpus ACC

**Qué es:** propuestas, sección por sección, para que cada documento del modelo auxiliar ACC sea más claro, más visual y mejor conectado. Cada entrega trae ayudas visuales listas para usar, mejoras de edición y diseño, y conexiones con el resto del corpus.
**Regla:** todo son **añadidos** propuestos. No se modifica ningún documento fuente; su incorporación corresponde al propietario.
**Autor:** Claude, asistente de IA, a petición de Iván. Forma parte de la [auditoría incremental](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md) (PR #58).

## Entregas

| # | Documento | Estado | Propuestas | Ayudas visuales |
|---:|---|---|---|---|
| 01 | [README del modelo auxiliar](01_README_ACC.md) | ✅ Entregado (ronda 20) | 9 (P-R01 a P-R09) | Mapa del paquete, ruta con estado, 2 esquemas Mermaid, catálogo de estudios |
| 02 | `MODEL.md` — modelo integrado (218 líneas, 23 títulos) | Siguiente | — | — |
| 03 | `ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md` (453 líneas, 27 títulos) | Previsto | — | — |
| 04 | `CASES.md` (77 líneas) | Previsto | — | — |
| 05 | `STUDY_SPECIFICATION.md` y `DDS_EVALUATION_PLAN.md` | Previsto | — | — |
| 06 | `RESEARCH_STATUS.md`, `REVIEW_AND_COVERAGE.md` | Previsto | — | — |
| 07 | `SOURCES_AND_COVERAGE.md`, `ACC_BOUNDARY.md` | Previsto | — | — |
| 08 | README de cada estudio (11 en `main`) | Previsto | — | — |

## Sistema visual común

Para que todas las piezas se vean como una misma obra:

- **Paleta:** la misma paleta categórica validada (visión de color atípica y modo oscuro) de la guía de lectura. Azul = entender, verde = comprobar, ámbar = planificar, naranja = procedencia y límites.
- **Estado sin depender del color:** círculo lleno = hecho, medio círculo = en parte, círculo vacío = pendiente, siempre con su palabra al lado.
- **Nivel de evidencia:** 🧪 sintético · 📄 documental · 🔬 empírico, con la misma leyenda en todos los documentos.
- **Cada figura con su tabla:** toda ayuda visual tiene al lado una versión en texto con la misma información.
- **Diagramas editables:** los esquemas de flujo se proponen en Mermaid, que GitHub muestra directamente; las figuras de datos se generan en SVG con [`build_premium_figures.py`](build_premium_figures.py).

# 00L-A01 — Inventario de afirmaciones de los nueve perfiles

**Fecha de consulta del inventario:** 2026-09-25. Las fechas de cada fuente son las declaradas en los perfiles actuales; una página viva no se considera congelada solo por incluir una URL.

| Perfil | Afirmación decisiva que puede utilizarse | Fuente primaria / sección declarada | Fecha o versión | Clasificación y laguna |
|---|---|---|---|---|
| 00E-A01 Agent 365 | registro, relaciones, permisos y observabilidad de agentes soportados | M2–M7, §10 del perfil | docs actualizadas 30 Apr–7 Jul 2026 | capacidad documentada; verificar página viva y distinguir agentes propios/terceros |
| 00E-A02 LangGraph/LangSmith | persistencia, interrupciones, trazas y evaluación permiten construir controles reforzados | L1–L7, §12 | LangGraph 1.2.12; LangSmith SDK v0.14.0, 21 Sep 2026 | capacidad documentada + implementación propuesta; no prueba semántica EA nativa |
| 00F-A01 FIWARE/Orion-LD | broker, suscripciones, fuentes de contexto y NGSI-LD soportan distribución de contexto | F1–F7, §13 | Orion-LD 1.12.0; ETSI GS CIM 009 V1.9.1 | capacidad documentada; no atribuir coherencia sistémica al broker |
| 00F-A02 AWS IoT TwinMaker/Core | twin, conectividad, reglas y sombras representan estado distribuido | A0–A6, §13 | A0 publicado 14 Sep 2026; páginas vivas consultadas 24 Sep | capacidad documentada; la coherencia de misión es implementación adicional |
| 00G-A01 OpenAI stack | agentes, handoffs, guardrails, compaction y tracing ofrecen superficies de control | O1–O9, §17.12 del escenario 00G | anuncios 2025–2026; docs vivas 24 Sep | capacidad documentada; source-dependence y autoridad son hipótesis de implementación |
| 00H-A01 Claude Agent SDK | hooks PreToolUse pueden permitir, denegar, pedir, modificar o diferir antes de la herramienta | §1 y §12 del perfil; hooks/subagents/compaction | docs consultadas 24 Sep 2026 | capacidad documentada; mandato, campaña y autoridad raíz son controles construidos |
| 00H-A02 Stripe Radar | reglas, atributos, contadores y revisiones cubren ejes de riesgo de pago | §4 y §12 del perfil | docs consultadas 24 Sep 2026 | capacidad documentada; Radar no autoriza campañas de negocio ni reembolsos por sí solo |
| 00I-A01 Step Functions/RDS | Wait/Task/Choice, integraciones AWS, RDS y control de versiones permiten una máquina de estados | §1–§3 y §15 del perfil | docs oficiales consultadas 24 Sep 2026 | capacidad documentada; revalidación semántica en T2 es implementación propuesta |
| 00J-A01 Panodyssey/TEMS | aviso de transparencia, derechos y portabilidad ofrecen señales de procedencia/interoperabilidad | P1–P8, §2 y §14 del perfil | fuentes públicas y estándares declarados 2026 | capacidad documentada según fuente; H1/H2 no se pueden atribuir a Panodyssey/TEMS |

## Correcciones editoriales aplicadas por este paquete

- El perfil 00E-A01 v0.2 se trata como la revisión de fuentes del 24 de septiembre; la referencia residual a v0.1 queda identificada para corrección en el propio perfil, no se reinterpreta aquí.
- 00E/00F conservan la diferencia entre el análisis original del 17 de septiembre y la actualización de fuentes del 24.
- Para Claude, Stripe y AWS se registra fecha de consulta; mientras no exista release, historial o extracto congelado, las afirmaciones dependientes de una página viva se clasifican como `CAPACIDAD_DOCUMENTADA_NO_CONGELADA`.

## Regla de evidencia

Una fila solo autoriza la frase breve indicada. No autoriza inferir que el producto detecta régimen, conoce autoridad de negocio, preserva una oportunidad o supera una traza. Esas capacidades deben aparecer como implementación propuesta, hecho sintético o `NO CONCLUSION`.

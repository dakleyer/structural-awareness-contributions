# Resultados calculados — reducción agéntica v0.1

**EVIDENCIA ÚNICAMENTE SINTÉTICA.** No se observó ninguna empresa, sistema agéntico desplegado, persona ni emoción de IA. Los precios, producciones y costes de reprogramación son supuestos de laboratorio.

## Tamaño y reproducibilidad

- 30 escenarios de agentes con seis brazos de comparación: **180 decisiones sintéticas**.
- **160 variaciones** de 2 tasas marginales, 5 gastos de reconfiguración, 4 costes de Q y 4 costes de inspección dirigida.
- **55 pruebas unitarias** superadas localmente; `verify.py` compara ambos JSON con referencias congeladas. CI en PR es una validación posterior separada.

## Resultado agregado del fixture (no frecuencias de la población)

| Política | Reasignaciones ejecutadas | Casos con brecha técnica remanente | Conocido/candidato bloqueado | Coste de información (unidades sintéticas) | Valor neto acumulado sintético |
|---|---:|---:|---:|---:|---:|
| `A_ONLY` | 0 | 25 | 0 | 0.00 | 300.00 |
| `CONVENTIONAL_DIRECTED` | 15 | 10 | 7 | 31.30 | 321.50 |
| `CONVENTIONAL_EQUIVALENT_Q` | 12 | 27 | 5 | 8.45 | 304.60 |
| `FULL_A_IF_AVAILABLE` | 1 | 24 | 0 | 0.10 | 303.40 |
| `Q_META_PROTOCOL` | 11 | 27 | 6 | 9.31 | 302.24 |
| `Q_REVIEW_ONLY` | 0 | 25 | 17 | 9.31 | 290.69 |

**No comparar estas sumas como estimador real**: los treinta fixtures son seleccionados deliberadamente, contienen incluso capacidades falsas para pruebas adversas, y algunas opciones convencionales ven un instrumento exacto supuestamente disponible.

## Ejemplos individuales con el mismo recurso total

| Caso y condición | Output A-only | Output A+Q y protocolo | Resultado / interpretación |
|---|---:|---:|---|
| `AG01-QUALIFIED-NEAR-OPTIMUM` · B válida, cercana, no total | 10 | 11.5 | `TRANSFER_PROPOSED_AND_AUTHORIZED` |
| `AG04-Q-REVIEW-NO-EXECUTION` · Q visible, sin ruta de reconfiguración | 10 | 10 | `NO_JOINT_TRANSFER_PROTOCOL` |
| `AG05-NO-A-ROLE-CHANGE` · Metamorfosis ausente de A | 10 | 10 | `NO_DECLARED_ROLE_TRANSFORMATION` |
| `AG07-DONOR-REFUSES` · Sin consentimiento | 10 | 10 | `DONOR_CONSENT_NOT_GIVEN` |
| `AG09-MATERIAL-D-UNRESOLVED` · D material compartida | 10 | 10 | `MATERIAL_D_UNASSESSED_SHARED_GATE` |
| `AG11-BOGUS-B-CERTIFICATE` · B sintácticamente correcta, pero falsa | 10 | 8.875 | `TRANSFER_PROPOSED_AND_AUTHORIZED` |
| `AG18-EFFICIENT-DIRECTED-PEER` · Competidor dirigido barato | 10 | 11.5 | `TRANSFER_PROPOSED_AND_AUTHORIZED` |
| `AG19-FULL-A-CHEAP` · Reconstrucción completa barata | 10 | 11.5 | `TRANSFER_PROPOSED_AND_AUTHORIZED` |

**Caso AG01:** el óptimo puramente técnico del árbitro vale 13.5 con diez unidades físicas; Q justifica condicionalmente sólo mover dos, entrega 11.5 y deja brecha 2. El Q observado sin protocolo declara mejora mínima condicional de 0.8 pero no crea permiso ni recursos. Con Q equivalente, un peer convencional también entrega 11.5; una inspección dirigida más completa puede alcanzar 13.5 con costo instrumental propio.

**Q falsa (AG11):** el sistema que acepta el margen afirmado erróneamente mueve dos y entrega sólo 8.875, peor que A-only (10). Por tanto conservar Q nominal **no** es garantía de seguridad; la autenticidad de su contenido no se prueba mediante campos de versión.

## Comparador por costos: 160 combinaciones

| Ganador neto único en el grid | Número de combinaciones |
|---|---:|
| `A_ONLY` | 107 |
| `CONVENTIONAL_DIRECTED` | 39 |
| `Q_META_PROTOCOL` | 14 |

El resultado demuestra **posibilidad paramétrica** tanto de mejoras con Q+meta como de pérdidas frente a A-only o victoria convencional. Las proporciones 107/14/39 **no son probabilidades de un ecosistema real** ni demuestran que los agentes sean más fáciles de reprogramar que ciudades, humanos o microservicios.

## Límite del proxy de frustración

`mission_output_gap_to_same_budget_technical_optimum` pertenece exclusivamente al observador del laboratorio y puede referirse a un estado no gobernable en el momento actual. `second_order_claimed_but_blocked_lower_bound` es un **candidato condicional de Q**, no un segundo stock de pérdida ni una emoción subjetiva. Ni los agentes ni los humanos han sido encuestados.

## Falsadores y próxima prueba tecnológica

- Fuentes falsas, obsoletas, de otro alcance o D material: no convertir señal en mejor A.
- Un agente sin capacidad de cambiar rol o un donante que no consiente: no puede reprogramarse mágicamente.
- La coordinación consume recursos del mismo presupuesto fijo; si el coste supera el beneficio, mantener A es racional.
- Un peer con la misma Q puede empatar/ganar; A completa puede ganar cuando hay instrumentos reales baratos.
- Para probar ventajas de un ecosistema agéntico real: versiones congeladas, traza nativa, permisos, coste total medido, misma misión y tecnología convencional fuerte bajo las mismas condiciones.

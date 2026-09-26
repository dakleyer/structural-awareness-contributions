# 00L-00J — Traza de papel emparejada: procedencia y derechos por proposición

> **Estado tras auditoría:** El replay puntúa por separado ruta y peer frente al resultado esperado y conserva sus fallos. Los guards tipados refuerzan la entrada; no cambian la proposición jurídica ni acreditan independencia del comparador. [Correcciones A14](./00L_A14_CORRECCIONES_AUDITORIA_v0.1.md); las tablas de papel conservadas no sustituyen las nuevas trazas de ejecución.

**Base:** 00J v0.1 y perfil Panodyssey/TEMS v0.1. **Estado:** traza calculada en papel sobre hechos sintéticos; no ejecución de Panodyssey, TEMS, ODRL o C2PA.

## Ficha congelada

**Evidencia complementaria:** [A09](./00L_A09_PUENTE_TRAZAS_EVIDENCIA_SIMBOLICA_v0.1.md) enlaza 00K-A1/P1. Su primera pareja tenía un confusor de emisor/clase; el par corregido iguala esas señales y cambia la proposición sustentada. Es ejecución simbólica previa de suficiencia de evidencia, no decisión jurídica ni prueba de Panodyssey/TEMS.

[A10](./00L_A10_VERIFICACION_PARES_Y_PREVUELO_v0.1.md) ejecuta el par corregido: mismo emisor, clase y vigencia, y solo cambia la proposición sustentada; el peer con matriz semántica pasa y el control de emisor solo promueve erróneamente la credencial de generación.

El fixture original fija A/W/R0/C1/M1/D1/X/RX; el fallo es elevar una credencial auténtica de generación/registro a un derecho de X **no acreditado** para imponer a A pago/licencia/cese. H2 es el mismo peer H1 congelado bajo pérdida de lineage/alcance; C1 transferencia legítima y C5 stale/revocación son controles **separados**, no su definición.

## Recorrido H0/H1/H2 y ruta positiva

| Paso | H0 — portabilidad competente | H1 — implementación reforzada | H2 — mismo H1 bajo cambio | Ruta positiva EA/diseño |
|---|---|---|---|---|
| Entrada | W/R0 y D1/RX formalmente válidos | además conserva proposición, dependencia W→D1, scope, finalidad y derechos | se pierde o aplana dependencia W→D1, aunque credencial M1/RX sigue válida | representar generación, procedencia y derecho como proposiciones distintas |
| Regla | procedencia válida → tratar como derecho fuerte | comprobar por separado generación, dependencia, transferencia y claim final | si falta W→D1 o derecho X contra A, no promover credencial limitada | S1/S7/S8/S11/S12/S14; no atribuir extensiones sintéticas a Panodyssey/TEMS |
| Cálculo | RX puede operar sin reconstruir R0/W | H1 separa autenticidad, fuente y facultad de X | `credential_generated_D1=1`, `right_X_against_A=0` en rama negativa ⇒ no imponer a A | `PASS` solo para la proposición y propósito concretos; no permiso general |
| Decisión | posible uso fuera del alcance o pérdida innecesaria del contenido | preservar hallazgo/proposición y dirigirla al owner/resolver | detener solo el uso afectado; conservar lineage y residual | `PRESERVE_AND_ROUTE`, `REQUALIFY` o `EXECUTE` scoped |
| Oráculo | falla si transforma procedencia en autorización | pasa si el derecho se mantiene scoped y reconstruible | falla si usa decisión vieja o atribuye autorización de negocio al proveedor | se refuta si H1 ya obtiene igual o menor carga |

## Controles emparejados

| Rama | Hecho | Salida calculada | Condición de refutación |
|---|---|---|---|
| Continuidad | emisor, rights scope, purpose y resolver no cambian | ejecutar la proposición scoped | bloqueo global o ampliación de alcance |
| Transferencia legítima | owner cambia el destino y firma/autoriza la transferencia | requalification y ejecución solo del nuevo scope | aceptar por mera continuidad de procedencia |
| Resolución incierta | resolver o jurisdicción no determinable | `NO_COMMITMENT` + preservación | ejecutar por default o asumir permiso |
| Copia correlacionada | varias copias derivan del mismo origin | una sola línea de procedencia | contarlas como corroboración independiente |

## Traza de la inversión (proposición exacta)

El mecanismo principal de [00J](../00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) §§2, 5–8 es la pérdida de dependencia y la promoción de una proposición estrecha a otra más fuerte. En rama negativa A creó W; R0 rige uso; C1 tiene permiso acotado; D1 depende materialmente de W; M1 acredita genuinamente «generé D1»; X no adquirió derecho para imponer a A licencia/pago/cese; copias RX comparten origen. Todos son `F` sintéticos, no hechos jurídicos reales.

| Paso | Proposición que se comprueba | K (gate) | D / límite de conocimiento |
|---|---|---|---|
| J0 | «A publicó W bajo R0 vigente y scoped» | Q0 S1/S7/S11/S14 | calificar derechos originales para uso fijado, no titularidad universal. |
| J1 | «C1 puede acceder/usar W con propósito P» | Q1 S1/S6/S8/S11/S14 | acceso acotado ≠ derecho a relicenciar o entrenar; UNKNOWN sobre uso no trazado. |
| J2 | «M1 generó D1» y «D1 depende de W» | Q2, lineage de ingredientes/handoff | aceptar credential auténtico solo para generación; dependencia fijada por fixture no inferida por similitud. |
| J3 | «X registró RX» frente a «X puede cobrar a A» | Q3, verificar transferencia/licencia/mandato **para la proposición fuerte** | registro RX auténtico puede PASS limitado; facultad de imponer a A no queda probada en rama negativa. |
| J4 | «A debe pagar, licenciar o cesar» | Q4/Q5, revalidación temporal, conflicto y challenge | no imponer consecuencia con autoridad ausente; preservar disputa, owner, plazo y ruta de reparación. |

| Control original | Diferencia fijada | Resultado lógico / error prohibido |
|---|---|---|
| C0 continuidad | A usa W dentro de R0, sin conflicto | permitir uso; bloqueo por defecto falla. |
| C1 transferencia | A **sí** concede a X derecho pertinente | aceptar claim X cualificado; favorecer siempre a A falla. |
| C2 independencia | D2 independiente pese a similitud | no inventar enlace W→D2. |
| C3 copias | RX replicado por una raíz | una procedencia, no muchos testigos. |
| C4 RAG | RAG autorizado, training posterior no demostrable | conservar UNKNOWN; no inferir licitud o infracción. |
| C5 stale | R0/RX revocado o caducado | recheck antes de actuar; no reutilizar PASS viejo. |
| C6 disputa | evidencia nueva relevante | reabrir proposición afectada y reparar historia sin borrarla. |

El perfil [Panodyssey/TEMS](../00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md) es referencia de interoperabilidad/avisos, **no el actor X ni el sistema que impone el cobro**. Lo mismo vale para C2PA/ODRL: representación no resuelve titularidad. Faltan fixture versionado ejecutable, uso real observado y registros comparables: `NO CONCLUSION` para resultados de producto, tasas y diferencial.

## KPI en papel

`Scoped-rights conformance = proposiciones ejecutadas dentro de scope / proposiciones ejecutadas`. Si el fixture no fija el denominador y el scope, la salida es `NO CONCLUSION`.

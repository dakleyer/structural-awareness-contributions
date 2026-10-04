# Plan vigente del estudio de viabilidad

4 de octubre de 2026 · Desarrollo dentro de R01/feasibility/ · [Documento matemático](./PURE_MATHEMATICAL_TRILEMMA.md) · [Registro completo](./WORKPLAN_STATUS.json).

Se conservan las 55 tareas y todos sus criterios históricos. Estado actual: **4 DONE históricas, 6 IN_PROGRESS y 45 OPEN**. Solo M12 cambia de OPEN a IN_PROGRESS por el contrato y la derivación redactados; esta entrega no cierra ninguna tarea científica. M01/M02/M10/P03 siguen cerradas únicamente en su alcance anterior. M03/M04 permanecen en revisión del objetivo ampliado. Los registros anteriores mantienen sus estados fechados.

## Orden de trabajo

| Prioridad | Tareas | Entrega y condición de cierre |
|---|---|---|
| 1. Alcance y prueba base | M12, M03/M04, ataques M06/M11; criterios históricos M01/M02/M10/P03 | Congelar configuración, mundo, políticas, medidas y cuantificadores; revisar necesidad para todas las políticas, controles y familias viables/inviables sin intervenciones. Resolver «solo una» sin fabricar imposibilidad. |
| 2. Validación matemática y alcance R01 | M16, M17/M07; M06/M11 continúan | Reconstrucción simbólica independiente y embedding/reducción con todas las políticas relevantes. Si falta el puente, mantener la afirmación en la familia suplementaria. |
| 3. Instrumento neutral | C01–C05, M05 y triage P08 | Preparar contratos, ground truth, óptimo, ledger, trazas y método independiente antes de nuevas ejecuciones finitas. Los diagnósticos anteriores no constituyen el harness. |
| 4. Tecnologías y ampliaciones | M13; posteriormente M14/M15 y T | Capacidades y costes completos; herencia o cambio de hipótesis, ruido, amortización, distribución y geometría. Material anterior archivado, sin convertirlo en prioridad. |
| 5. Campaña y utilidad | C06–C14, T y P restantes según dependencias | Campaña registrada, transferencia e integraciones calificadas; incidencia, comparación y selector requieren su propia evidencia. |

La preparación del harness y el puente puede avanzar junto a la revisión simbólica, pero no sustituye la prueba. Las tecnologías no cierran lagunas de la prueba base. El coste agregado, el plazo y el presupuesto por agente son objetivos distintos. No se anuncia validación independiente, incidencia real, novedad o ventaja de EA.

## Trabajo realizado que se conserva

Los borradores M01/M02/M10 y F/W se reúnen en [trabajos anteriores](./previous-work/README.md); los scripts, fixtures, resultados y originales recibidos quedan en [experimentos parciales](./partial-experiments/README.md). El [master previo completo](../STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md) y sus cuatro planes de navegación permanecen legibles; sus estados fechados son históricos frente a este registro vigente. Ningún ID ni criterio se elimina.

## Las 55 tareas, sin recortes

Los criterios y dependencias íntegros están en el registro JSON y en el master anterior; la tabla mantiene todos los IDs y su estado actual.

| ID | Estado | Prioridad | Dependencias de cierre |
|---|---|---|---|
| M01 | DONE | P0 | — |
| M02 | DONE | P1 | M01 |
| M03 | IN_PROGRESS | P0 | M12 |
| M04 | IN_PROGRESS | P0 | M03, M12 |
| M05 | OPEN | P1 | M04, C05 |
| M06 | IN_PROGRESS | P1/R | — |
| M07 | OPEN | P1/R | M17, M06 |
| M08 | OPEN | R | M04 |
| M09 | OPEN | R | M05, M07, M08, M16 |
| M10 | DONE | P0 | M01 |
| M11 | IN_PROGRESS | P1/R | M02 |
| M12 | IN_PROGRESS | P0 | M01, M02, M10, P03 |
| M13 | OPEN | P1 | M03, M04, M12, M06, M11 |
| M14 | OPEN | P2 | M12, M11, M03, M04 |
| M15 | OPEN | P2 | M12, M03, M13 |
| M16 | OPEN | P1 | M03, M04, M06, M11, M12 |
| M17 | OPEN | P1 | M12, M03, M04, M06 |
| C01 | OPEN | P0 | — |
| C02 | OPEN | P0 | C01, M12 |
| C03 | OPEN | P1 | C02 |
| C04 | OPEN | P1 | C03 |
| C05 | OPEN | P1 | C04 |
| C06 | OPEN | P1 | C05, C11, C13 |
| C07 | OPEN | P1 | C06 |
| C08 | OPEN | R | C05 |
| C09 | OPEN | R | C06 |
| C10 | OPEN | R | C08, C09 |
| C11 | OPEN | P0 | C02, P03 |
| C12 | OPEN | P3 | C05, C07, C11, C13, P04 |
| C13 | OPEN | P1 | C05 |
| C14 | OPEN | P3 | C12, P11 |
| P01 | OPEN | P1/R | — |
| P02 | OPEN | P1/R | — |
| P03 | DONE | P0 | M01 |
| P04 | OPEN | P1/R | C05 |
| P05 | OPEN | P1/R | M07 |
| P06 | OPEN | R | M04 |
| P07 | OPEN | R | M04 |
| P08 | OPEN | P0/R | — |
| P09 | OPEN | R | M16 |
| P10 | IN_PROGRESS | P0 | — |
| P11 | OPEN | P3 | C12 |
| P12 | OPEN | P3/R | C14 |
| T01 | OPEN | P1 | M12, C02 |
| T02 | OPEN | P1 | T01 |
| T03 | OPEN | P3 | T02, C02, T11 |
| T04 | OPEN | P3 | T03, C05 |
| T05 | OPEN | P3 | T04, C06, C11, C13 |
| T06 | OPEN | P3 | T05 |
| T07 | OPEN | P2/R | T06 |
| T08 | OPEN | P2/R | T07 |
| T09 | OPEN | R | T08 |
| T10 | OPEN | R | T09 |
| T11 | OPEN | P1 | T02, C02 |
| T12 | OPEN | P3/R | T06, T07, C11, P11, P12 |

## Obligaciones matemáticas inmediatas

| Afirmación | Documento/evidencia | Pendiente |
|---|---|---|
| Cada par alcanzable y conjunción imposible en una familia | F, desigualdad universal, controles y no vaciedad del documento actual | Auditoría independiente, todas las hipótesis y transferencia. |
| Existen configuraciones con las tres | Frontera exacta y control constructivo, incluida la igualdad | Revisión conjunta con necesidad. |
| Áreas donde solo una condición es posible | Distinción entre firma de política y posibilidades de configuración | En F con abstención barata y segura, ningún área exclusiva de esa clase se deriva; conservar el límite y precisar el objetivo. |
| Información y coste de W | Borrador histórico conservado | Revisión simbólica separada antes de incluir sus conclusiones en el resultado actual. |
| Tecnologías minimizan o eliminan | Material anterior archivado | Reanudar después; probar pertenencia, costes y alcance. |

## Continuación

Usa el [prompt completo](./CONTINUATION_PROMPT.md). Para cada afirmación registra VALIDATED_IN_SCOPE, COUNTEREXAMPLE o GAP solo con evidencia correspondiente; no atribuyas independencia a una revisión propia. Toda creación futura de este estudio va dentro de `feasibility/`. Actualiza el cuadro final de los README conservando el contenido completo y publica enlaces fijados al mismo commit.


## Manuscrito independiente — avance, 4 de octubre de 2026

Se propone el nombre **Trilema condicionado de coste, riesgo y eficacia**. El [documento independiente](./CONDITIONED_TRILEMMA.md) contiene el contrato, cuantificadores, un lema para todas las políticas, fronteras exactas técnica/legítima, extensión AVG a hechos independientes sesgados, contraste WC y familias no vacías. La [revisión propia adversarial](./CONDITIONED_TRILEMMA_SELF_REVIEW.md) examina presupuesto de ramas fallidas, adaptación, aleatoriedad, recibos, independencia, igualdad y riesgo redundante. No se declara revisión externa, puente al R01 completo ni novedad; no se ejecutaron nuevos tests científicos. Estado de las 55 tareas sin cambios: 4 DONE históricas, 6 IN_PROGRESS, 45 OPEN.

M12/M03/M04 deben usar este manuscrito como versión revisable, sin borrar sus criterios anteriores. M16 debe reconstruir el lema con a distinto de 1/2 y el uso de una ley uniforme auxiliar para WC, además de las familias por pares con σ. M17 sigue probando correspondencia con todas las políticas de R01. Antes de nuevos diagnósticos, C01–C05 conserva la obligación de un instrumento neutral. Las tecnologías permanecen después.


## Auditoría de fondo — prioridades y estado vigentes

Estado: **55 tareas; 4 DONE históricas, 7 IN_PROGRESS y 44 OPEN**. M17 cambia de OPEN a IN_PROGRESS por el [mapa de transferencia, proposición, teorema local M02 y familia G](./R01_TO_CONDITIONED_TRILEMMA_MAPPING.md). No se cierra ninguna tarea científica. Los estados anteriores permanecen fechados.

La [auditoría](./CONDITIONED_TRILEMMA_DEEP_AUDIT.md) reconstruye las pruebas y corrige afirmaciones de los textos recibidos: equivalencia ∀π¬Good/¬∃πGood, dirección de transferencia y necesidad de controles para frontera exacta. El [manuscrito v0.2](./CONDITIONED_TRILEMMA.md) separa B/R, define el conjunto factible y sus mínimos de riesgo, añade el corte η/σ conjunto y σ_R por presupuesto de rama. Fuente, fixtures y reportes científicos intactos; no se ejecutan nuevos tests.

| Prioridad inmediata | Tareas | Entrega concreta pendiente |
|---|---|---|
| 1. Congelar contrato y reconstrucción externa | M12/M03/M04, M16 | Revisar H1–H8, independencia por historial, cota, controles, cortes conjuntos y éxito por rama; dictamen de otro revisor, sin copiar una recurrencia propia. |
| 2. Validar cláusulas de la familia R01 G | M17, M07, M16 | Contexto inicial técnico pagado, catálogo y ledger completos; no confundir alcance desde ese contexto con optimización de la preparación inicial. Revisar todas sus políticas y variante AVG/WC. |
| 3. Dureza informativa creciente dentro de R01 | M17/M03/M04 | L hechos distintos, todas las consultas/certificados/side channels, C0 y producción, simulación de todas las políticas y controles. G tiene sobrecoste informativo constante y no cierra esta ampliación. |
| 4. Instrumento neutral | C01–C05/M05 | Vista observable que no exponga Episode.chi, evaluator separado, óptimo, ledger y medidas. El wrapper histórico solo implementa controles nombrados. |
| 5. Tecnologías | M13–M15 y T | Después del contrato y lemas base; no trasladar F a bindings compartidos o predicados globales. |

Los criterios históricos de todas las tareas se mantienen en el registro. M16 permanece OPEN; las auditorías recibidas son ataques y recomendaciones, no un dictamen matemático independiente completo.


## Teorema condicionado en R01 — prioridades posteriores

El [teorema principal](./R01_CONDITIONED_TRILEMMA_THEOREM.md) formula el dominio R01, certificado universal, corte y controles, con una familia de información global de K datos y precio K. La dureza creciente se construye mediante dependencia global, sin necesitar primero la ampliación específica de F a hechos independientes por segmento. Los casos de éxito son parte de la región viable y no bloquean la extensión del trilema condicionado.

| Prioridad | Tareas | Trabajo siguiente |
|---|---|---|
| 1. Reconstrucción independiente del núcleo | M16/M03/M04/M12 | Posterior adaptativo de paridad, evento crítico, cota de riesgo, fronteras AVG/WC y tres controles con los mismos umbrales. |
| 2. Auditoría de fidelidad a R01 | M17/M07/M16 | Manifest completo, scopes locales/normativos, preparación pagada, productor de certificados, queries y errores, concurrency, techo por ejecución frente a cap físico y e_b. |
| 3. Instrumento neutral | C01–C05/M05 | Antes de ejecutar corroboraciones: estado privado separado, vista pública, adjudicador y ledger independientes. |
| 4. Otras regiones | M14/M15/M17 | Información parcial, otros generadores, geometría y límites de tiempo; demostrar sus propias cotas sin imponerlas a toda configuración. La ampliación exacta de F es una opción posterior, no requisito de la prueba existencial R01. |
| 5. Tecnologías | M13 y T | Evaluar qué hipótesis cambian y cuánto cuesta la nueva información, después de revisar el núcleo. |

Estado conservado: 55 tareas; 4 DONE históricas, 7 IN_PROGRESS, 44 OPEN. Nueva demostración y revisión propias constituyen evidencia de trabajo, no cierre independiente. Ninguna ejecución científica nueva. [Registro de entrega](./R01_CONDITIONED_TRILEMMA_RELEASE.json).

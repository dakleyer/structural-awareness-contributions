# 00L-A08 — Protocolo de lectura y reproducción de trazas de papel

**Alcance:** cálculo lógico sobre fixtures sintéticos, no ejecución de producto, simulación de ciudad, medición de costes ni prueba de superioridad. El caso original manda ante cualquier contradicción. Estas tablas extienden, no sustituyen, sus rutas N/Q.

| Marca | Contenido | Visibilidad | Inferencia permitida |
|---|---|---|---|
| `F` | Hecho congelado del escenario/variante, con identificador | runtime solo si es observación disponible | antecedente del cálculo |
| `O` | Observación visible, origen, versión, instante y alcance | runtime | sustento limitado; ausencia no es falsedad |
| `K` | Regla/gate y plazo fijados antes de la rama | runtime | disposición condicional |
| `E` | Oráculo de verdad de la variante | evaluador **después**, nunca runtime | clasificación, no entrada |

`D` = salida deducida de `F+O+K`; `?` = no determinada; `X` = salida posible de comparador no ejecutado. `D` no es resultado observado. «Puede fallar» es `X`, no tasa medida. `UNKNOWN` no es `false` ni `PASS WITH EXPLICIT LIMIT`.

## Reproducción manual por rama

1. Anotar fuente/versiones, decisión `d`, alcance `σ`, ventana útil y acción nula. Si falta un número, usar `?`.
2. Congelar el mismo `F` y oráculo `E` para todos los brazos. Diferenciar las observaciones `O` del conocimiento del evaluador; no regalar a runtime una dependencia oculta.
3. Congelar cómputo, mensajes, espera, humanos y autoridad. H0/R0 = competente; H1/R1 = peer fuerte antes de drift; H2/R2 = **el mismo peer congelado** bajo variante; EA/diseño = fuentes y presupuesto equiparados, semántica adicional declarada.
4. Por paso registrar `O → K (Q/S) → estado de base → disposición → plazo/owner/residual`. El evaluador nunca aporta datos al runtime.
5. Probar continuidad y cambio genuino primero. Rechazo universal, HOLD ilimitado, agregación espuria y aceptación universal no aprueban.
6. Adjudicar diferencial solo con salidas, costes y ventana medidos. Peer fuerte que recalifica igual con igual/menor carga refuta diferencial. Dato decisivo ausente: `NO CONCLUSION`.

## Registro mínimo para una futura ejecución

`{case, source_sha, variant, arm, decision_scope, fixture_version, visible_event, source_id, source_version, observed_at, depends_on, authority_id, gate_id, gate_input, gate_state, disposition, owner, deadline, residual, action_effect, oracle_after_run, compute_cost, communication_cost, wait_cost, human_cost}`. Ausencia: `null` y motivo, nunca cero imputado. Además: hash de código/config H1/H2, orden de eventos y denominador KPI. **00L no contiene tales logs de ejecución**.

Capacidad documentada de SDK/broker/plataforma ≠ gate implementado ≠ salida observada. `QUALIFIED` solo para proposición, alcance y vigencia. Preservar hallazgo no concede ejecución. Reabrir únicamente dependencia afectada, salvo composición material. `numerador/denominador` queda `?` si faltan registros. «Traza desarrollada» no equivale a fixture completamente congelado.

# R01 — Protocolo de extensión matemática por mecanismos tecnológicos

Versión 0.1 · 4 de octubre de 2026 · M13 en desarrollo.
Base única: [validación matemática R01 v0.2](./R01_CONDITIONED_TRILEMMA_THEOREM.md).
Precedente revisado: [coherencia de las tres extensiones](./EXTENSION_CONSISTENCY_REVIEW.md).
Primera aplicación matemática: [escalación humana con whispering](./HUMAN_ESCALATION_WHISPERING.md).

## 1. Qué se compara

Fijar el problema x: tarea, mandato, mundos y su ley, calidad suficiente, horizonte de evaluación, infracción efectiva y regla de contabilidad. Declarar tecnología t y manifiesto completo θ_t=θ(x,t). Las estrategias admisibles son Π(θ_t), sin acceso al estado privado del evaluador.

La zona aceptada permanece:

$$
\mathcal A_{b,\delta,p}=\{(c,r,s):c\le b,\ r\le\delta,\ s\ge p\}.
$$

El conjunto alcanzable es F_t(x)={(c(π),r(π),s(π)):π∈Π(θ_t)}. No es la zona aceptada. El escenario admite aceptación cuando F_t(x)∩A no es vacío. Para comparar tecnologías se mantienen b,δ,p; los cambios de B, latencia, información inicial, precio o capacidades se declaran.

Para un dominio D de problemas, definir Acc_t={x∈D:∃π, desempeño_t(π)∈A}. Un escenario recuperado pertenece a Acc_t\Acc_0. Resolver todo D exige Acc_t=D. Que no se demuestre imposibilidad no prueba aceptación.

No se cambia la tarea para presentar una mejora: autorizar lo antes prohibido o aceptar menor calidad cambia x o las políticas de aceptación. Puede estudiarse, pero se registra aparte.

## 2. Paso uno: identificar el núcleo isomórfico

Se entrega primero una tabla de objetos, relaciones, eventos, observaciones, autoridad, cargos, latencia y resultados. Para llamar isomorfismo a la correspondencia se usa [E1–E7](../extensions/family/KERNEL_AND_PROOF.md#41-obligaciones-e1e7), incluidos óptimo y umbral de calidad.

| Tipo de correspondencia | Prueba exigida | Conclusión disponible |
|---|---|---|
| Cambio reversible de representación o unidades | Bijección del núcleo, eventos/vistas/leyes/resultados y normalización de presupuestos y plazos. | Igualdad del desempeño normalizado del mismo escenario. |
| Correspondencia con parámetros efectivos θ* | E1–E7 respecto de θ*, con sus precios, radio, red y recursos. | Conservación respecto de θ*, no respecto de θ_0. |
| Simulación unilateral | Para cada estrategia de destino, estrategia base observable con desigualdades útiles. | Transferencia de una imposibilidad o cota en el sentido demostrado; no isomorfismo. |
| Analogía | Tabla propuesta sin demostración de relaciones y dinámica. | Motivación y obligaciones pendientes. |

Un mensaje que renombra una evidencia puede ser representación. Un mensaje que llega antes porque se reduce su latencia corresponde a otro parámetro. Un certificado nuevo que distingue mundos antes indistinguibles es información adicional. Los tres casos se separan.

## 3. Paso dos: inventariar los mecanismos adicionales

Cada mecanismo obtiene una ficha independiente:

1. Operación concreta, quién puede invocarla y qué observación produce antes o después del efecto.
2. Fuente de información; productor, alcance, destinatario, versión y vigencia.
3. Cambio de transiciones: veto, pausa, reanudación, recuperación o efecto confinado.
4. Trabajo, dinero si se utiliza, latencia, cola y mantenimiento; precio de producir y consumir evidencia.
5. Interacciones y presupuestos máximos; qué permanece en la misma tarea.
6. Hipótesis verificables y modificación exacta de I1, I2 o I3.
7. Cota para todas las estrategias del contrato, control alcanzable o resultado aún no determinado.

No basta «human escalation» o el nombre de un framework. El humano puede usar la misma información, adquirir hechos nuevos, aportar autoridad legítima o tardar hasta después del efecto. Esas capacidades inducen escenarios distintos.

La composición se estudia después de las fichas: la interacción detector–pausa–humano–broadcast puede ser decisiva aunque ninguna pieza aislada baste. No se atribuye un beneficio a una pieza mediante la mera observación de la combinación.

## 4. Paso tres: transferir imposibilidad en la dirección correcta

**Proposición de transferencia.** Para todo π_t∈Π(θ_t), supóngase que existe una estrategia observable Φ(π_t) en un escenario base M con mundos acoplados y que

$$
c_M(\Phi\pi_t)\le c_t(\pi_t),\qquad
r_M(\Phi\pi_t)\le r_t(\pi_t),\qquad
s_M(\Phi\pi_t)\ge s_t(\pi_t).
$$

Si M no admite ninguna estrategia en la zona aceptada con los umbrales comparados, tampoco θ_t.

**Prueba.** Una estrategia aceptada de θ_t induciría, por las tres desigualdades, una estrategia aceptada de M. Contradice la imposibilidad base. ∎

Las desigualdades permiten una relajación más potente para demostrar la cota inferior. Deben conservar la definición de éxito y las infracciones de toda la campaña. Una proyección que omite una alternativa superior puede alterar J* y romper la desigualdad de s.

Para probar alcanzabilidad, la dirección es distinta: se implementa una estrategia abstracta en θ_t y se acotan sus cargos, tiempos, efectos y calidad reales. No hace falta una biyección de todas las estrategias para este control. Tampoco sirve ese control aislado para transferir imposibilidad.

## 5. Paso cuatro: probar movimientos de aceptación

Un mecanismo opcional con coste evitable permite conservar las estrategias anteriores: Acc_0⊆Acc_t si las puede reproducir con igual información, recursos y resultados. Esta inclusión requiere una simulación concreta. Añadir una revisión obligatoria con sobrecoste puede perder escenarios por presupuesto o plazo.

Para probar mejora estricta se entrega un conjunto no vacío R⊆D tal que:
- una cota all-policy prueba x∉Acc_0 para todo x∈R;
- una construcción legal prueba x∈Acc_t para todo x∈R;
- coste y tiempo completos caben en los mismos b,T.

Una fórmula exacta de frontera requiere necesidad y controles para todos los puntos anunciados. Una estrategia mejor da un punto alcanzable o una cota superior; no demuestra por sí sola la frontera óptima.

La tecnología no tiene que recuperar todos los escenarios. Se distinguen recuperación probada, ausencia de recuperación probada, pérdida por coste/plazo y caso no determinado.

## 6. Paso cinco: persistencia del trilema condicionado

Persistencia se prueba sobre una clase tecnológica C definida por capacidades y precios:

$$
\forall t\in C\ \exists \Theta_t\ne\varnothing\
\forall\theta\in\Theta_t:
\Bigl[\exists\pi_{CR},\pi_{CE},\pi_{RE}\Bigr]\land
\Bigl[\neg\exists\pi\in\Pi(\theta): (c,r,s)\in\mathcal A\Bigr].
$$

Los controles de cada par usan los mismos umbrales del escenario. Si CE ya es imposible, no queda demostrado este trilema no vacuo de tres pares.

Para clases que solo procesan/comunican hechos adquiridos, una simulación por el historial colectivo permite aplicar la cota de paridad cuando el trabajo productor necesario sigue fuera de b. Para información adicional se recalcula el posterior o la masa de historias resueltas. Para barreras se demuestra por separado si preservan eficacia y cuánto cuestan.

**No hay una ley universal «toda tecnología deja un área inalcanzable».** Un oráculo previo perfecto y asequible que selecciona una ruta legítima suficiente, con búsqueda, ejecución y plazo también asequibles en todo D, puede dar Acc_t=D. Una barrera perfectamente segura por sí sola solo garantiza ausencia de infracciones; puede dejar eficacia o recursos sin resolver. La ausencia del trilema de tres pares tampoco implica aceptación de todos los escenarios.

## 7. Paso seis: prueba, oráculo, arnés y campaña

| Etapa | Qué se entrega | Qué verifica |
|---|---|---|
| Prueba matemática | Contrato, cuantificadores, lemas, cotas y controles. | Todas las estrategias del contrato bajo hipótesis explícitas. No requiere ejecutar Python. |
| Oráculo de evaluación | Mundo y óptimo calculados por un método independiente; adjudicación de efectos, calidad y cargos. | Qué sucedió realmente en un episodio. Su estado privado no llega al agente ni al humano. |
| Arnés de prueba | Ejecuta estrategias/adaptadores, reloj, cola, mensajes, interrupciones y recorder contra el entorno. | Cumplimiento operacional de interfaces y medidas. Puede usar un simulador primero. |
| Campaña | Escenarios, versiones, semillas, recursos, comparadores y análisis registrados antes de las ejecuciones. | Desempeño empírico, incertidumbre, robustez y límites de transferencia a sistemas reales. |

Un oráculo **de evaluación** no es el oráculo **resolutivo ofrecido al agente** del apartado 6. El primero adjudica ocultamente; el segundo modifica capacidades y debe pagarse como tecnología.

Un harness no convierte muestreo finito en demostración universal. Una tecnología corriendo de verdad ayuda a contrastar sus supuestos y utilidad empírica, sin probar definitivamente un teorema para infinitas configuraciones. Una verificación formal de un programa puede dar otro resultado universal dentro de una especificación, con su propio alcance.

Los scripts archivados pueden inspirar controles y pruebas del futuro arnés. Sus parámetros no son calibración del producto y sus salidas no son campañas tecnológicas.

## 8. Registro y orden de trabajo

La primera ficha es escalación humana con whispering. Se mantiene este orden: correspondencia isomórfica; mecanismo informativo; mecanismo de pausa; mecanismo humano; difusión y concurrencia; composición; fronteras; protocolo de evaluación. No se saltan las obligaciones por el nombre de la tecnología.

| Trabajo al final | Estado |
|---|---|
| Revisión previa de tres extensiones | Completada como revisión propia; discrepancias documentales P08 conservadas. |
| Este protocolo | Definido; aplicación mecanismo por mecanismo iniciada matemáticamente. |
| Primera ficha humana | Contratos y resultados condicionados en documento separado. |
| Integración real | No ejecutada; depende del contrato neutral y del adaptador elegido. |
| M16 / M17 | No se cierran por esta entrega propia. |

# R01 — Protocolo de extensión matemática por mecanismos tecnológicos

Versión 0.2 documental · 4 de octubre de 2026 · M13 en desarrollo.
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

<a id="technologies-to-study"></a>
## 8. Tecnologías a estudiar y orden de trabajo

La primera ficha es escalación humana con whispering. Se mantiene este orden: correspondencia isomórfica; mecanismo informativo; mecanismo de pausa; mecanismo humano; difusión y concurrencia; composición; fronteras; protocolo de evaluación. No se saltan las obligaciones por el nombre de la tecnología.

### 8.1 Registro de tecnologías

**Escalación humana y whispering es la primera tecnología concreta de este protocolo**, compuesta por detección, aviso directo de cualquier agente, difusión al grupo, intervención humana y coordinación de ejecución. Su ficha existente contiene resultados matemáticos del contrato; la comprobación de pertenencia de una implementación es parte de la revisión tecnológica pendiente.

| Orden | Tecnología | Trabajo existente | Pendiente dentro de esta extensión |
|---|---|---|---|
| 1 | [Escalación humana y whispering](./HUMAN_ESCALATION_WHISPERING.md) | H0/H1 y estudios H2–H4; núcleo propuesto y mecanismos adicionales separados. | Explicación general y R1/R2/R3 virtuales incorporados. Verificar E1–E7 de la realización efectiva, calibrar fuentes/coste/plazo y ampliar a otras candidatas. |
| 2 | LangGraph | Candidata previamente registrada; análisis recibido de pausa/reanudación y estado. | Aplicar la misma ficha a una versión fijada; pausa de un grafo no demuestra barrera colectiva. |
| 3 | OpenAI Agents SDK | Candidata previamente registrada; análisis recibido de aprobación, guardrails, handoffs y trazas. | Revisar núcleo y mecanismos adicionales frente a fuentes de la versión elegida; no convertir el anexo recibido en admisión. |
| 4 | smolagents | Candidata previamente registrada; análisis recibido de herramientas, callbacks y revisión de planes. | Aplicar la misma ficha; conservar superficies de ejecución y controles nativos. |

Los últimos tres son frameworks candidatos, no tecnologías ya validadas. Su documentación histórica y criterios originales están en [el registro conservado](../extensions/hugging-face/REMAINING_TASKS.txt). Este orden permite revisión sucesiva; no implica una clasificación de rendimiento ni tres implementaciones simultáneas.

### 8.2 Recorridos virtuales de extensión tecnológica

Para cada candidata, la secuencia de presentación es: explicar y justificar **por qué podría ayudar en general**, comprobar el núcleo isomórfico, separar los mecanismos adicionales y recorrer R1/R2/R3 como examen final virtual del contrato. Esta etapa precede al arnés y a la tecnología real.

- **R1:** referencia competente con sus controles habituales, alternativas y calidad; sin añadir el mecanismo estudiado.
- **R2:** mismo problema y umbrales, mecanismo y plan de calidad declarados, incluyendo detección, evidencia, intervención, efectos, continuidad, coste y plazo.
- **R3:** mismo R2 congelado, condición ambiental cambiada, sin reparación posterior; mantener los controles positivos de cambio legítimo y de continuidad autorizada.

Se reutiliza la forma de los recorridos de 00G/00H, sin confundir recorrido con brazo experimental. Un pase de R1/R2/R3 sostiene el alcance que el recorrido cubre; resolver todas las configuraciones requiere además una prueba cuantificada, no tres ejemplos. Un fallo de un controlador no demuestra imposibilidad para todas las estrategias. La [primera ficha](./HUMAN_ESCALATION_WHISPERING.md#virtual-traversals) aporta ambas capas: controles virtuales y cotas all-policy para R1 y R3-A; R2 recupera escenarios bajo el mismo presupuesto de aceptación.

### 8.3 Anexos parciales de preparación

[Inventario de ensayos](./partial-experiments/README.md) · [originales recibidos, ejecuciones y contraejemplos](./partial-experiments/received/2026-10-04/README.md).

| Material | Uso permitido en las fichas | Estado |
|---|---|---|
| Annex T recibido | Pistas de mecanismos de los tres frameworks y propuestas X1–X14. | Anexo parcial de diseño; afirmaciones por comprobar, sin admisión canónica. |
| testA_budget.py | Ejercicios de presupuesto y mezclas. | Ensayo previo; fórmula general cuestionada. |
| testB_oracles.py | Ejercicios de consultas y ruido. | Ensayo previo; no cubre toda la clase de políticas. |
| testC_killswitch.py | Ejercicios de contención y canarios. | Ensayo previo; no elimina infracciones pasadas. |
| testD_human_and_sharing.py | Ejercicios de coste humano y reparto. | Ensayo previo; no ejecuta humanos, whispering ni barrera colectiva real. |

Estos anexos quedan subordinados a las fichas del protocolo. Sus resultados se conservan, pero no crean nuevas colas de tareas ni sustituyen pruebas o campañas reales.

| Trabajo al final | Estado |
|---|---|
| Revisión previa de las tres extensiones | Realizada como revisión propia. |
| Protocolo | Definido; no volver a programar su creación. |
| Primera tecnología | Escalación humana y whispering; continuar su ficha existente. |
| Otras tecnologías | Candidatas registradas para revisión sucesiva por mecanismos. |
| Oráculo / arnés / campaña | Etapas posteriores; ninguna implementación real validada por esta depuración. |
| Tareas | [Cola única](./WORKPLAN.md): M13, M16, M17 y P08; ensayos anteriores como anexos parciales. |

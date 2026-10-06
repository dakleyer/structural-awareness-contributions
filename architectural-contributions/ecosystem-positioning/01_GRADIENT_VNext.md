# VNext — Ley de gradiente condicionado por objetivo

> **Expediente de revisión; no sustituye la fuente actual.** Una sola VNext del documento lógico. Auditoría realizada por **Codex, asistente de IA**, 6 de octubre de 2026. Se escribe para que una persona entienda el argumento y pueda continuar la revisión; no es una lectura humana independiente.

**Fuente:** [Ley de gradiente condicionado por objetivo](01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md), texto completo, §§1–16; commit `26eb9ee1e5cccb348abe26a71f37d18a947af6bb`, blob `330cbdab2fa8ca0cb162f480f2ab83b06485a1f8`. [Plan de trabajo de Iván](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) y [alcance y fuentes consultadas](../../governance/review/MSCA-kernel-lineage-gradient-2026-10-06/evidence.json). Cuerpo original preservado. Publicar auditorías está autorizado; incorporar propuestas requiere decisión concreta de Iván.

## Primera pasada — relevancia y comparación

**Lectura de fondo y lógica realizada.** La idea útil es que una incertidumbre importa al participante cuando afecta su objetivo por una dependencia representada. Un cambio grande en otro proceso puede no justificar ningún movimiento local. Un candidato atractivo no concede permiso y la misma mejora no compensa una restricción dura.

En el caso escalar normalizado, comparar riesgo antes y esperado después permite hablar de una diferencia positiva. Sin embargo, §5 permite una composición vectorial/Pareto y §7 conserva lenguaje de positivo/negativo mientras §9 escribe argmax como transición seleccionada. Falta declarar cómo se comparan resultados que no son ordenables por un número único, cómo se conserva un empate y qué ocurre si no existe máximo.

**Contraejemplo conceptual propio, no resultado experimental:** riesgos actuales(0.3,0.3), candidatoA(0.2,0.5), candidatoB(0.4,0.2), con menor riesgo mejor en cada componente. A mejora el primero y empeora el segundo; B hace lo contrario. No hay mejor vector por orden componente a componente. Una prioridad lexicográfica o regla de trade-off legítima podría seleccionar, pero el símbolo G no la suministra. Los números sólo ilustran la comparación; no son estimaciones del corpus.

Tampoco se obtiene una expectativa fundada sobre todo C/D por escribir E[...]. La propia fuente §4 exige caracterizar cualquier término numérico y§12 evita inferir beneficio completo de una frontera abierta. El problema es una abreviatura matemática insuficiente para los perfiles generales admitidos, no una refutación de la idea de relevancia ni prueba de un fallo ejecutado.

## Segunda pasada — pluralidad y receptor operativo

**Relación principal cotejada; evidencia completa abierta.** Architecture§5 y su README niegan un mínimo global y preservan objetivos no reducibles a un escalar. Operation§9 escribe reducción de riesgo = aumento de cumplimiento sin repetir la condición binaria de Gradient§1. Su§26/ACC gate conserva autoridad, por lo que la falta afecta comparación, no la legitimidad de ejecutar.

Se propone leer57/58/59 juntos: definir comparación en la fuente y conservarla en el receptor. [Architecture VNext](../../standards/minimum-sufficient-control/00_ARCHITECTURE_VNext.md) y [Operation VNext](../../standards/minimum-sufficient-control/04_OPERATION_VNext.md) tienen la consecuencia. 01D, perfiles concretos y el modelo de evidencia/riesgo siguen pendientes de lectura completa. No se conoce un ranking runtime cuya salida se haya cambiado; tampoco se ha demostrado computabilidad universal.

## Tercera pasada — notación y formato

**Fuente completa examinada.** El nombre gradiente se explica como diferencia/orden sin exigir diferenciabilidad. La fórmula puede funcionar en un perfil escalar, pero el lector necesita ver sus condiciones en la misma sección que la selección. Un orden parcial no se convierte en un scalar por una tabla de etiquetas.

El título D está duplicado como en otro documento del corpus. Es un defecto localizado de lectura, con posible efecto en anclas; no se cambia por esta auditoría. Candidato61 conserva el viejo y exige comprobar referencias.

## Cuarta pasada — una persona frente a dos objetivos

**Relectura simulada por el mismo asistente.** El ejemplo de restaurante permite entender que una oportunidad rentable puede estar fuera del objetivo y contrato actuales. Para entender un perfil con dos objetivos conviene poder preguntar: ¿cuál mejora, cuál empeora, qué restricción es dura y quién puede aceptar el compromiso? El contraejemplo anterior muestra esa necesidad sin exigir una teoría nueva.

No se justifica ocultar alternativas bajo “el mejor”. Si hay varias, la revisión debe dejarlas visibles para decisión humana. La señal de presión, el candidato admisible y la acción permitida conservan estados diferentes.

## Quinta pasada — optimización vectorial como antecedente

**Contraste específico realizado.** [Boyd y Vandenberghe, Convex Optimization, libro2004, séptima impresión corregida2009, §4.7.1–4.7.3, pp174–178 impresas](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) distingue comparación mediante orden, mínimo y alternativas Pareto; pueden existir resultados incomparables. Se leyó el pasaje pertinente, no el libro completo ni sus algoritmos. Pieza reutilizable: formular primero medida, orden y conjunto comparado. No se impone convexidad, cono universal o scalarización al corpus. CopyrightCambridge2004; no hay permiso de reimpresión verificado; no se copian texto/figuras/código y datos. Es antecedente directo: el nombre nuevo no demuestra novedad matemática o mejor rendimiento.

FG-TIDA ATHENA suministra una posible frontera de autoridad que esta ley debe respetar, no una medida objetivo y riesgo. El contraste y límites de esa propuesta están en ACC VNext; no se ejecuta la cadena propuesta ni se importa material restringido. Quinta hecha para esta pregunta de comparación; realizaciones y modelos probabilísticos permanecen fuera de lo demostrado.

## Estado y cambios propuestos

Primera, tercera y cuarta pasadas textuales realizadas; segunda abierta por perfiles/consumidores pendientes; quinta específica realizada. Sexta global pendiente. Los pares57/58/61 se añaden abajo;59 corresponde al consumidor operativo. La tanda57/58/59 tiene **impacto esperado Alto, riesgo Alto, esfuerzo Medio, prioridad Primera**: altera condiciones de comparación y debe conciliarse antes de una decisión. No se aplica ni define una nueva política de selección por esta publicación.

### Cambio 57 — Precisar cómo se compara un gradiente vectorial

**Fuente/ubicación:** [fuente actual](01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md), blob `330cbdab2fa8ca0cb162f480f2ab83b06485a1f8`; el viejo aparece exactamente una vez. **Impacto esperado: Alto. Riesgo: Alto. Esfuerzo: Medio. Prioridad: Primera. Tanda: 2 — Coherencia entre RA, EA y MSCA.**

**Beneficio esperado:** Evitar declarar positiva una alternativa que mejora un objetivo y empeora otro sin regla legítima. No es eficacia medida. **Riesgo concreto:** Afecta significado matemático y rankings de Gradient/Operation/Architecture/01D. **Trabajo necesario:** Conciliar orden, medida, incertidumbre y contraejemplos en consumidores.

**Texto antes — viejo literal completo:**

```markdown
Therefore:

> **Positive gradient means the transition is expected to reduce objective-conditioned uncertainty/risk and equivalently increase expected Objective-Envelope fulfilment.**

> **Negative gradient means the transition increases objective-conditioned risk or decreases expected fulfilment.**

> **Zero gradient means no material improvement under the current qualified model.**

This is the core law.

It is valid for discrete transitions through finite differences and for continuous state spaces through an ordinary differential gradient when such a representation is justified.
```

**Texto después — propuesto completo:**

```markdown
Therefore, when the declared profile uses a scalar risk functional and the conditional expectation is supported for the assessed scope:

> **Positive gradient means the transition is expected to reduce that objective-conditioned risk. For a normalized binary objective V_i = 1 - R_i, this is equivalently an increase in expected fulfilment.**

> **Negative gradient means an expected increase in that risk.**

> **Zero gradient means no modelled change in that declared scalar measure; it does not establish that unassessed effects are absent.**

A vector-valued or Pareto profile MUST declare how its objective outcomes are compared. It may preserve incomparable alternatives instead of assigning them a single positive or negative sign. Lexicographic priorities or an owner-authorized scalarization are possible profile choices, not universal consequences of this law. A compensating gain MUST NOT override an owner-declared hard constraint.

An expectation requires a declared and justified conditional model for the characterized aspects being assessed. If that basis is unavailable, the profile preserves bounded estimates, a declared robust comparison or UNRESOLVED; it does not assign probabilities to the whole C or D frontier by assumption.

This is an objective-conditioned comparison rule. In a scalar profile it can use discrete finite differences; a differential gradient requires a justified differentiable representation. The law alone establishes neither such a representation nor a computable, unique best transition.
```

**Dependencias:** [01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md](01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) · [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [00_CANONICAL_MSCA_ARCHITECTURE.md](../../standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md). **Estado/condición:** Pendiente de decisión; Conciliar57/58/59; decisión de Iván; no algoritmo universal. Instrucciones de Iván: cinco pasadas, conciliación y plan con viejo visible; esta propuesta parcial se publica para revisión, no aplica el cambio. Decisión concreta de incorporación aún pendiente.

### Cambio 58 — Conservar alternativas y casos sin máximo en la selección

**Fuente/ubicación:** [fuente actual](01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md), blob `330cbdab2fa8ca0cb162f480f2ab83b06485a1f8`; el viejo aparece exactamente una vez. **Impacto esperado: Alto. Riesgo: Alto. Esfuerzo: Medio. Prioridad: Primera. Tanda: 2 — Coherencia entre RA, EA y MSCA.**

**Beneficio esperado:** Evitar que argmax implique ganador único o existente cuando falta orden, candidatos o evidencia. No es eficacia medida. **Riesgo concreto:** Empates y fallback pueden alterar contratos y resultados; conjuntos sujetos a ACC/autoridad vigentes. **Trabajo necesario:** Cotejar perfiles/casos de incomparabilidad, empate y máximo no alcanzado.

**Texto antes — viejo literal completo:**

```markdown
Thus:

~~~text
τ*_candidate = argmax over T_ACC,i of G_i(τ)
~~~

but:

~~~text
τ*_execute = argmax over T_exec,i of G_i(τ)
~~~
```

**Texto después — propuesto completo:**

```markdown
For a scalar profile in which a maximum is established, selection first preserves the full set of maximizing candidates:

~~~text
Candidates_best = argmax over T_ACC,i of G_i(τ)
Executable_best = argmax over T_exec,i of G_i(τ)
~~~

These are sets, not a guaranteed unique transition or an execution command. A legitimate profile supplies any required tie-break. For a vector-valued or Pareto profile, retain the non-dominated candidates under its declared comparison relation and apply only an owner-authorized selection rule.

If the relevant set is empty, candidates remain incomparable, no maximum is attained, or material evidence is unresolved, report that state. Use the bounded HOLD, exploration, authority-request or escalation route supplied by the surrounding operation/profile; do not invent a winning transition.
```

**Dependencias:** [01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md](01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) · [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [00_CANONICAL_MSCA_ARCHITECTURE.md](../../standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md). **Estado/condición:** Pendiente de decisión; Depende de57 y conciliación con Operation; decisión de Iván; no fallback universal. Instrucciones de Iván: cinco pasadas, conciliación y plan con viejo visible; esta propuesta parcial se publica para revisión, no aplica el cambio. Decisión concreta de incorporación aún pendiente.

### Cambio 61 — Corregir el título duplicado de residual en Gradient

**Fuente/ubicación:** [fuente actual](01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md), blob `330cbdab2fa8ca0cb162f480f2ab83b06485a1f8`; el viejo aparece exactamente una vez. **Impacto esperado: Bajo. Riesgo: Medio. Esfuerzo: Bajo. Prioridad: Después. Tanda: 4 — Lectura humana y rutas.**

**Beneficio esperado:** Leer una vez el título del apartado D. No es eficacia medida. **Riesgo concreto:** Cambia el slug; comprobar referencias o preservar ancla compatible. **Trabajo necesario:** Título y enlaces de fragmento, preservación; semántica intacta.

**Texto antes — viejo literal completo:**

```markdown
### D — structural / capability residual### D — structural / capability residual
```

**Texto después — propuesto completo:**

```markdown
### D — structural / capability residual
```

**Dependencias:** [01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md](01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) · [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [00_CANONICAL_MSCA_ARCHITECTURE.md](../../standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md). **Estado/condición:** Pendiente de decisión; Decisión de Iván y control de anclas, como56 sin unificar fuentes. Instrucciones de Iván: cinco pasadas, conciliación y plan con viejo visible; esta propuesta parcial se publica para revisión, no aplica el cambio. Decisión concreta de incorporación aún pendiente.


---

## Revisión a fondo de los planes de cambio — 6 octubre 2026

**Evaluación realizada por Codex, mismo asistente de IA, para que una persona pueda decidir.** Se revisan el plan, sus motivos de auditoría, pares literales, impacto, riesgo, esfuerzo y dependencias; no es la sexta pasada científica global ni acredita el cierre de las cinco. Fuente de este cotejo: commit `03db21016d6a0831a43d7a99d3640854ab549777`, [documento propietario](01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md), blob `330cbdab2fa8ca0cb162f480f2ab83b06485a1f8`. Los registros anteriores y sus viejos completos permanecen íntegros.

La valoración actual distingue una mejora documental de una modificación conceptual o de contrato. **Candidato para revisión documental significa preparado para leer y decidir, no autorizado para incorporar.** Los originales siguen en sólo lectura; no se ejecuta ninguno de estos pares.

| Cambio | Calidad/estado actual | Impacto esperado | Riesgo | Esfuerzo | Prioridad |
|---|---|---|---|---|---|
| 57 | Cambio acoplado; no listo; Pendiente de decisión | Alto | Alto | Alto | Primera |
| 58 | Cambio acoplado; no listo; Pendiente de decisión | Alto | Alto | Alto | Primera |
| 61 | Editorial condicionado; Pendiente de decisión | Bajo | Medio | Bajo | Después |

**Cambio 57 — Cambio acoplado; no listo.** El argumento admite vector/Pareto y luego usa signo escalar. La propuesta explica el orden declarado sin inventar pesos universales.

**Beneficio esperado:** Evitar declarar positiva una alternativa que mejora un objetivo y empeora otro sin regla legítima. **Riesgo concreto:** Afecta significado matemático y rankings de Gradient/Operation/Architecture/01D. **Coste de preparar y mantener:** Esfuerzo Alto: además de redactar, leer y conciliar productor, receptores, perfiles/materiales y casos límite; comprobar compatibilidad y mantenimiento de versiones antes de una decisión.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** 57→58→59; casos escalar,vector incomparable, empate y restricciones duras, sin probabilidades fabricadas sobreC/D; revisar perfiles consumidores. Revisar junto con 58, 59. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 58 — Cambio acoplado; no listo.** argmax puede ser conjunto, vacío o no alcanzar máximo. Selección y ejecución siguen siendo decisiones distintas.

**Beneficio esperado:** Evitar que argmax implique ganador único o existente cuando falta orden, candidatos o evidencia. **Riesgo concreto:** Empates y fallback pueden alterar contratos/resultados; conjuntos sujetos a ACC/autoridad vigentes. **Coste de preparar y mantener:** Esfuerzo Alto: además de redactar, leer y conciliar productor, receptores, perfiles/materiales y casos límite; comprobar compatibilidad y mantenimiento de versiones antes de una decisión.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Depende de 57; conservar conjuntos/incomparabilidad/no máximo y fallback del perfil legítimo, no regla global; cotejar 59/Architecture. Revisar junto con 57, 59. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 61 — Editorial condicionado.** Duplicar el títuloD dificulta lectura. Que el título limpio aparezca dentro del duplicado no equivale a corrección aplicada.

**Beneficio esperado:** Leer una vez el título del apartado D. **Riesgo concreto:** Cambia el slug; comprobar referencias o preservar ancla compatible. **Coste de preparar y mantener:** Título y enlaces de fragmento, preservación; semántica intacta.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 2 coincidencia(s), fuente actual completa. El después puede aparecer como subcadena del título defectuoso; no prueba incorporación. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Comprobar slug y referencias antes de un cambio futuro. No tocar significadoD ni deducir cierre de 57/58. Revisar junto con 56. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

[Visión conjunta y tandas en EP README VNext](README_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026). Mantener tres niveles de README, fuentes congeladas, resultados y binarios. Reorganización, nueva campaña, experimentos e incorporación canónica permanecen fuera de esta entrega.


---

## Relación material con posicionamiento local e interfaz EA/MSCA — 6 octubre 2026

**Auditoría cruzada realizada por Codex, mismo asistente.** Fuente de esta ampliación: `fa2c411c810950fb94924caae38938c52dfd5014`;01H § §1–9,01B § §1–8 y 01D § §1–7 completos, ArticleII completo como procedencia; no experimentos o audiencia humana independiente.

Se leyó 01H completo: §4.1 describe oportunidad deobservar/preguntar/verificar, no cambio autorizado derol. ArticleII § §5/6 preserva región suficiente, multiobjetivos yóptimos locales distintos de Pareto. Ambos son antecedentes, no prueba de unranking único.57/58/59 siguen la propuesta conjunta; la lectura no los incorpora ni deduce una esperanza probabilística sobre todoC/D.

La explicación de origen y los límites están en [01H VNext](../../research/ecosystem-awareness/baseline/01H_VNext.md) y [01B VNext](../../research/ecosystem-awareness/baseline/01B_VNext.md). La segunda pasada se amplía en esta relación; fuentes urbanas/funcionales/perfiles pendientes siguen visibles. Un enlace compatible no establece ejecución. Se mantienen los originales y las conversaciones anteriores; quinta/sexta mantienen su estado real.

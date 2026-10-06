# Revisión de MSCA Operation — qué recibe y qué puede decidir

**Única VNext de este documento lógico.** Auditoría por Codex, 6 de octubre de 2026; mismo asistente de IA. [Fuente](./04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [ficha externa](./04_OPERATION_REVIEW_CARD.md) · [plan](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md).

Fuente: blob `88a4ea7e1eec2c9f2b3f2dbe0d15f64087e1265c`, commit `e80846a0f9cf3b97cf222ed3d1e28b31d145ad3e`. Iván autoriza revisar todo Contributions sin romper integraciones; no aplicar cambios canónicos sin decisión concreta.

## Auditoría de la entrada RA — alcance parcial

Se examinaron §4 y pasajes de entrada/salida que usan Δ_RA, además de 01C §2 y 01D completo. El resto del documento y las cuatro pasadas integrales permanecen pendientes.

La entrada RA está atribuida al productor legítimo. La tabla la resume como direction/intensity/capability/residual. Sin embargo, 01C define B_RA como fundamento establecido y reserva caracterizada, no intensidad física; C_RA como exploración aún no caracterizada, no toda capacidad. El receptor necesita conservar estas distinciones para no perder reservas conocidas, inventar magnitudes o tratar clasificación incierta como D.

Se comparó también el [README RA](../../research/regime-awareness/README_VNext.md). El problema observado concierne a la explicación textual del contrato. No basta para declarar roto todo runtime: hay que leer los perfiles, mappings y decisiones que realmente dependen de esa interpretación.

01D exige misma operación, S/E, scope, versiones y tiempo; separa assessment y permiso y evita vetos por un RA opcional. Conservar el nombre Δ_RA no garantiza esas condiciones. La [VNext del README MSCA](./README_VNext.md) y [EP README VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md) reciben el hallazgo.

## Conversación y pendientes

**Codex, auto-revisión:** aclarar un resumen podría afectar cómo un lector implementa la entrada. La propuesta no añade campos ni cambia dueño; aun así requiere cotejar las realizaciones y los consumidores descendentes de Operation. No se ensayó un adaptador, se ejecutó una transición o se recalificó un resultado.

Sigue abierta la lectura de drift, Type catalogue, gradiente, ACC, posture gate, señales de intention/authority, re-contracting y self-healing, junto con sus fuentes y falsadores.

## Propuesta antes/después — entrada RA, pendiente

**Localización:** §4, fila única. **Tipo:** precisión semántica; compatibilidad aún por examinar. **Instrucción:** preparación de revisión integral autorizada por Iván.

**Texto antes:**

```markdown
| Δ_RA | Regime Awareness | Qualified direction/intensity/capability/residual of ecosystem/regime change. |
```

**Texto después:**

```markdown
| Δ_RA | Regime Awareness | Qualified regime-change position: A_RA direction; B_RA established support, validity limits and characterized assessment reserve; C_RA grounded exploration avenues not yet characterized; D_RA effects beyond effective evaluation. Confidence qualifies support and is not physical change magnitude; uncertain role classification remains UNKNOWN. Retain the source's scope, context, versions and freshness. |
```

**Razón:** mantener el sentido del productor 01C sin renombrar campos. **Dependencias:** RA, EA, Cartography, Operation y perfiles que utilicen esta entrada. **Comprobación previa:** una coincidencia en el blob auditado. **Decisión de Iván:** pendiente. **Incorporación:** no ejecutada.


---

## Quinta pasada — investigación externa, diferencial y reutilización

**Instrucción de Iván, 6 de octubre de 2026. Estado: contraste específico pendiente.** Esta quinta pasada se realiza después de las cuatro y queda dentro de esta misma VNext. No se crea otro expediente ni se incorporan propuestas a la fuente por esta anotación.

**Pregunta de este documento:** Contrastar operación, autoridad vigente, cambio de rol, señalización y recuperación con arquitecturas externas de runtime y lifecycle. Mantener separados selección, permiso, ejecución y efecto al evaluar una pieza reutilizable.

Se fijarán trabajos primarios de FG-TIDA y de otras líneas relevantes, incluidos antecedentes y actualizaciones posteriores, con autor, versión, fecha y alcance realmente leído. Aquí se justificará qué coincide, qué diferencia podría sostenerse y qué pieza concreta conviene reutilizar, con sus condiciones de atribución, adaptación y compatibilidad.

El [mapa externo preparatorio](../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md) aporta fuentes iniciales; no completa esta pasada. El [plan 1.6](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización) gobierna método y cierre. Las cuatro lecturas previas mantienen sus estados reales y se reabren si aparece evidencia que las afecte. Codex, mismo asistente de IA; anotación de alcance, sin independencia externa.


---

## Sexta pasada unificadora — preparación y continuidad

**Instrucción de Iván, 6 de octubre de 2026. Preparación registrada por Codex, mismo asistente de IA. Estado: pendiente de lanzamiento después de las cinco pasadas del corpus.** Esta anotación organiza el trabajo futuro; no declara una auditoría unificadora realizada ni cambia el estado de las lecturas anteriores.

**Pregunta de consolidación de este documento:** Verificar que las entradas EA/RA y el retorno a Cartografía conservan significado, scope, vigencia y dueño autorizado, y que las propuestas no confunden selección, permiso, ejecución o efecto.

Los hallazgos concretos se comentarán aquí y en las VNext de los documentos relacionados, conservando respuestas y desacuerdos. Se cotejarán las propuestas con la fuente actual y sus consumidores antes de presentar candidatos consolidados antes/después. La [sexta pasada del plan](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#sexta-pasada-unificadora-y-consolidación) fija el lanzamiento y el método. Se preservan fuente, historia y decisión de Iván para incorporar cambios.


---

## Prioridades del plan de cambios — revisión del corte

**Revisión realizada por Codex, 6 octubre de 2026, mismo asistente de IA.** Se revisan las auditorías y propuestas ya registradas para valorar impacto esperado, riesgo y esfuerzo. La fuente pública del corte es `7500dd5ee05c1a5052a28d35a8cefaf2c530707f`; los viejos y pares anteriores permanecen íntegros. Esta revisión no completa las pasadas pendientes ni la sexta.

El [plan 1.11](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#prioridad-de-cada-cambio--impacto-riesgo-y-esfuerzo) explica los criterios y el [listado completo](../../governance/review/change-priorities-2026-10-06/priorities.json) conserva las fuentes y los pares. La prioridad sirve para preparar tandas de decisión; la incorporación depende de Iván y de las comprobaciones indicadas.

| Cambio | Prioridad / tanda | Impacto esperado | Riesgo | Esfuerzo | Estado |
|---|---|---|---|---|---|
| 37 · Conservar significado RA al entrar en Operation | Primera · 2 — Coherencia entre RA, EA y MSCA | Alto | Alto | Medio | Pendiente de decisión |

### Cambio 37 — Conservar significado RA al entrar en Operation

**Impacto esperado: Alto. Riesgo: Alto. Coste/esfuerzo: Medio. Prioridad: Primera.** Que el consumidor reciba la semántica y condiciones del productor.

**Qué podría quedar desactualizado o afectado:** Cambiar entrada puede alterar decisiones esperadas o interpretación histórica; un resumen más largo no prueba equivalencia de ejecución.

**Qué cuesta prepararlo:** Cotejar 01C, RA, 03, 04, 01D y perfiles; ningún nuevo resultado runtime.

**Dependencias conocidas:** [00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md](../../research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) · [01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md](../../research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md) · [README.md](../../research/regime-awareness/README.md) · [03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md](03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) · [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md](../../research/ecosystem-awareness/baseline/01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md) · [01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md](../../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Conciliar contrato y consumidores. Tanda conjunta con 35/38, mantener scopes/versión/freshness y revisar consumidores.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](04_OPERATION_VNext.md#propuesta-antesdespués--entrada-ra-pendiente); el viejo tiene una coincidencia en [la fuente actual](04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md), blob `88a4ea7e1eec2c9f2b3f2dbe0d15f64087e1265c`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.


---

## Continuación de 01C — payloads y separación de propietarios

**Auditoría cruzada realizada por Codex, 6 octubre de 2026; mismo asistente de IA.** 01C distingue ahora explícitamente en su propuesta el input de rol vinculado y la observación de comportamiento. Operation §§2–4 ya mantiene esa diferencia; el cambio 54 corrige una ambigüedad del consumidor, no crea un nuevo owner. Los cambios 52/53 separan vocabulario Cart_i compartido de calificación del resultado RA. La entrada Δ_RA y su propuesta anterior conservan su compatibilidad pendiente.

La explicación, cobertura y viejos/nuevos están en [01C VNext](../../research/ecosystem-awareness/baseline/01C_VNext.md#lectura-de-los-payloads-y-sus-propietarios--continuación-sustantiva-de-01c), con el extremo productor en [Composition VNext](03_COMPOSITION_VNext.md) y [Role VNext](02_ROLE_VNext.md). Se preservan todas las conversaciones anteriores, decisiones y riesgos. No se declara ejecución o nueva validación independiente.


---

## Lectura completa de Role y Composition — reevaluación de la auditoría

**Auditoría/reevaluación realizada por Codex, 6 octubre de2026; mismo asistente de IA.** Role§13.1 contiene también la frase usada en01C; por eso la atribución anterior de la ambigüedad solo al consumidor era incompleta. Operation mantiene bound/effective.54 pasa a claridad opcional;52/53 no crean otro esquema ni acreditan fallo runtime.

[Role VNext](02_ROLE_VNext.md#pasadas-propias-de-role--lectura-completa-y-contraste-del-rol-estático) · [Composition VNext](03_COMPOSITION_VNext.md#pasadas-propias-de-composition--leer-el-mapa-completo-y-sus-límites) · [Fuentes/cobertura](../../governance/review/MSCA-role-composition-2026-10-06/evidence.json). La conversación anterior permanece visible; relectura del mismo agente no es independencia externa.


---

## Lectura completa de Operation — comparación, deriva y límites

**Auditoría realizada por Codex, 6 de octubre de 2026; mismo asistente de IA. Fuente completa §§1–26, commit `26eb9ee1e5cccb348abe26a71f37d18a947af6bb`, blob `88a4ea7e1eec2c9f2b3f2dbe0d15f64087e1265c`.** Continúa las revisiones parciales anteriores; no se elimina ninguna valoración o propuesta.

### Primera pasada — cerrar sin autoautorizar

Se leyó el ciclo completo. Comienza observando el rol efectivo y cotejando su legitimidad antes de optimizar desde un estado ficticio. Clasificar deriva no canoniza la conducta; un gradiente favorable no concede autoridad. Después de un cambio legítimo debe actualizarse rol/ACC/Cart antes de emitir el siguiente ciclo. Las solicitudes de contención e aislamiento se distinguen de su ejecución.

§21 explica una posibilidad de self-healing y niega prueba de convergencia o seguridad global. §22 permite corrección local sin consenso; no es evidencia de una recuperación garantizada. El ejemplo Bar-to-Napoleon ilustra una falsa transición de misión, no prueba cualquier adversario. Su§16 aclara que confianza alta aislada no diagnostica Type 2: hace falta promoción indebida de incertidumbre material.

§11.3 usa “It authorizes the need...” paraP3 mientras los otros gates niegan que una postura cree permiso. Se propone60 como precisión opcional de lectura, no reparación de una autorización ejecutada demostrada.

### Segunda pasada — comparación fuente/receptor

Se cotejaron íntegramente Architecture, ACC, Role, Composition,01I y Gradient. Role ligado/efectivo (§§2/14) conserva su diferencia; ACC (§§12–14) conserva linaje/sucesor/autoridad; Cart sigue en Composition. Sus consecuencias están en [Architecture](00_ARCHITECTURE_VNext.md), [ACC](01_ACC_VNext.md), [Role](02_ROLE_VNext.md), [Composition](03_COMPOSITION_VNext.md) y [01I](../../research/ecosystem-awareness/baseline/01I_VNext.md) VNext.

El nuevo hallazgo es§9: repite igualdad de reducción de riesgo y aumento de cumplimiento sin la condición binaria normalizada de la fuente. Gradient admite comparación vector/Pareto y su selección queda insuficientemente especificada para ese caso. Dos vectores que mejoran componentes diferentes no tienen ganador único por el símboloG. [Gradient VNext](../../architectural-contributions/ecosystem-positioning/01_GRADIENT_VNext.md) contiene el contraejemplo y57/58;59 conserva en el receptor la comparación declarada. Tanda conjunta, sin algoritmo/pesos/permisos nuevos.

No se leyeron aún completos todos los perfiles 01D/01H/01J, modelos de riesgo, fuente00G ni sus contratos y resultados. La segunda sigue abierta. No se relanza una ejecución para suplir lectura; la conciliación global tampoco se inicia por este contraste parcial.

### Tercera pasada — estructura y formato

Texto completo examinado: deriva → oportunidades → posturas → gates → resultados → feedback es un orden inteligible. Los distintos catálogos de estado no deben mezclarse; el resultado compuesto no es un permiso. La ambigüedad de autorizaciónP3 y la abreviatura de comparación son propuestas localizadas; no hay razón para reordenar toda la fuente.

### Cuarta pasada — lectura humana

Simulación del mismo asistente: el camarero puede creer que otra misión es atractiva, pero sigue vinculado al bar salvo transición legítima. Si ya cambió de conducta, hay que partir de lo observado y devolver la decisión al dueño adecuado. El cierre de escalada requiere destino, plazo, fallback y presupuesto (§13.2); esperar sin fin no es seguridad.

Una persona necesita ver la comparación de objetivos cuando el movimiento favorece uno y perjudica otro.59 protege esa pregunta; no obliga al lector a interpretar un argmax como consenso.

### Quinta pasada — delegación como frontera externa

**Contraste específico realizado.** [RFC8693, Campbell/editor, Bradley, Jones, Nadalin y Mortimore, enero2020, Proposed Standard](https://www.rfc-editor.org/info/rfc8693/), §§1/1.1/2.1 y derechos consultados. Distingue actor y sujeto; el intercambio depende del servidor/política y no fija un trust model universal. Pieza candidata: referencia actor/sujeto/scope de la autoridad que el ciclo verifica, sin transformar una intención en grant ni demostrar linaje ACC. Texto sujeto aIETF Trust/BCP78; componentes de código requieren el aviso de licencia indicado. Implementación/datos no seleccionados ni importados. No se prueba seguridad, ventaja o runtime compatible por el contraste.

ATHENA y su solicitud pública de cadena/revocación se contrastan en ACC VNext: propuesta pendiente, no experimento ejecutado. La quinta está realizada para esta pregunta acotada; adaptar un protocolo exige versión, autoridad y evidencia propios. La segunda material y sexta global siguen abiertas.

## Propuestas de esta lectura — fuente y consumidor juntos

### Cambio 59 — Mantener en Operation el perfil de comparación del gradiente

**Fuente/ubicación:** [fuente actual](04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md), blob `88a4ea7e1eec2c9f2b3f2dbe0d15f64087e1265c`; el viejo aparece exactamente una vez. **Impacto esperado: Alto. Riesgo: Alto. Esfuerzo: Medio. Prioridad: Primera. Tanda: 2 — Coherencia entre RA, EA y MSCA.**

**Beneficio esperado:** Que el consumidor no universalice lo que la fuente delimita. No es eficacia medida. **Riesgo concreto:** Puede desactualizar perfiles y decisiones esperadas; no cambia permisos y posturas. **Trabajo necesario:** Cotejo conjunto57/58,01D y contratos de selección.

**Texto antes — viejo literal completo:**

```markdown
For each candidate transition τ:

~~~text
G_i(τ | Δ_RA, Cart_i, X_i)
=
expected reduction in objective-conditioned risk
=
expected increase in Objective-Envelope fulfilment
~~~

as defined by the [Objective-Conditioned Agentic Gradient Law](../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md).
```

**Texto después — propuesto completo:**

```markdown
For each candidate transition τ, the gradient compares current and candidate outcomes using the declared Objective-Envelope risk profile:

~~~text
G_i(τ | Δ_RA, Cart_i, X_i)
= profile-qualified comparison of current and candidate objective-conditioned risk
~~~

For a supported scalar expectation this comparison may be expressed as expected risk reduction. Equivalence to an expected increase in fulfilment applies to the normalized binary reading V_i = 1 - R_i. Vector/Pareto profiles preserve their declared comparison relation and incomparable alternatives; they do not imply a unique scalar ranking.

The [Objective-Conditioned Agentic Gradient Law](../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) owns that comparison. Operation preserves its evidence limits, hard constraints and candidate-selection state; it does not fabricate a gain, maximum or execution permit.
```

**Dependencias:** [01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md](../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) · [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [00_CANONICAL_MSCA_ARCHITECTURE.md](00_CANONICAL_MSCA_ARCHITECTURE.md). **Estado/condición:** Pendiente de decisión; Tanda compatible57/58/59 y decisión de Iván. Instrucciones de Iván: cinco pasadas, conciliación y plan con viejo visible; esta propuesta parcial se publica para revisión, no aplica el cambio. Decisión concreta de incorporación aún pendiente.

### Cambio 60 — Decir que P3 identifica una necesidad, sin verbo de autorización

**Fuente/ubicación:** [fuente actual](04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md), blob `88a4ea7e1eec2c9f2b3f2dbe0d15f64087e1265c`; el viejo aparece exactamente una vez. **Impacto esperado: Medio. Riesgo: Medio. Esfuerzo: Bajo. Prioridad: Siguiente. Tanda: 3 — Contratos y protocolo.**

**Beneficio esperado:** Evitar que authorize se lea como autoridad creada por la postura. No es eficacia medida. **Riesgo concreto:** §§13/14/25 ya protegen la autoridad externa; no transformar la nota en nuevo gate. **Trabajo necesario:** Pasaje corto con cotejo de Gradient§8 y ACC§§5/7; preservación.

**Texto antes — viejo literal completo:**

```markdown
P3 does not authorize the destination. It authorizes the **need to qualify/execute a legitimate transition path** subject to ACC/authority.
```

**Texto después — propuesto completo:**

```markdown
P3 identifies the **need to qualify a legitimate transition path**. It grants no destination or execution authority; approval and execution remain subject to the applicable ACC and external authority mechanisms.
```

**Dependencias:** [01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md](../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) · [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [00_CANONICAL_MSCA_ARCHITECTURE.md](00_CANONICAL_MSCA_ARCHITECTURE.md). **Estado/condición:** Pendiente de decisión; Aclaración opcional, decisión de Iván y consumidores comprobados. Instrucciones de Iván: cinco pasadas, conciliación y plan con viejo visible; esta propuesta parcial se publica para revisión, no aplica el cambio. Decisión concreta de incorporación aún pendiente.


## Reapertura por nueva capacidad humana — fuente vigente

**Codex, mismo asistente,6 de octubre de 2026.** La fuente cambió a `8757ba614c94f962206912d4896c119a18a924fa`, blob `e11731c36e207d11631ade1a60ee521537840801`: se leyó íntegra la nueva §4.1 y su productor01K completo. Los demás pasajes no cambiaron. Se conservan la lectura y pares anteriores contra 26eb; no se reescribe suviejo.

La nueva entrada preserva cualificación,Cart/RA,ACC/autoridad y no convierte el avisohumano eninterruptprivilegiado. Su consumo deAVAILABLE exige unledger consistente;01K§4 puede contar dosveces lareserva si committed y demand_committed son elmismo volumen, y susclasesordinales no acreditan restas. [01K VNext](../../research/ecosystem-awareness/baseline/01K_VNext.md) y [01J VNext](../../research/ecosystem-awareness/baseline/01J_VNext.md) registran64/67 y otroextremo. No se da porprobada capacidad real ocalibración.

59/60 conservan exactamente viejo y propuesta, presentes una vez en la nueva fuente. Revalidación publicada a continuación; siguen pendientes de Iván, sin cambiar el input de37 ni resultados.

### Revalidación del cambio59 contra la nueva fuente

Blob vigente `e11731c36e207d11631ade1a60ee521537840801`; viejo único, contexto nuevo §4.1 examinado. **Texto antes — viejo completo:**

```markdown
For each candidate transition τ:

~~~text
G_i(τ | Δ_RA, Cart_i, X_i)
=
expected reduction in objective-conditioned risk
=
expected increase in Objective-Envelope fulfilment
~~~

as defined by the [Objective-Conditioned Agentic Gradient Law](../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md).

```

**Texto después — propuesto completo:**

```markdown
For each candidate transition τ, the gradient compares current and candidate outcomes using the declared Objective-Envelope risk profile:

~~~text
G_i(τ | Δ_RA, Cart_i, X_i)
= profile-qualified comparison of current and candidate objective-conditioned risk
~~~

For a supported scalar expectation this comparison may be expressed as expected risk reduction. Equivalence to an expected increase in fulfilment applies to the normalized binary reading V_i = 1 - R_i. Vector/Pareto profiles preserve their declared comparison relation and incomparable alternatives; they do not imply a unique scalar ranking.

The [Objective-Conditioned Agentic Gradient Law](../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) owns that comparison. Operation preserves its evidence limits, hard constraints and candidate-selection state; it does not fabricate a gain, maximum or execution permit.
```

Valoración/dependencias originales se conservan. Esta segunda localización no aplica la propuesta ni declara terminada la conciliación global.

### Revalidación del cambio60 contra la nueva fuente

Blob vigente `e11731c36e207d11631ade1a60ee521537840801`; viejo único, contexto nuevo §4.1 examinado. **Texto antes — viejo completo:**

```markdown
P3 does not authorize the destination. It authorizes the **need to qualify/execute a legitimate transition path** subject to ACC/authority.
```

**Texto después — propuesto completo:**

```markdown
P3 identifies the **need to qualify a legitimate transition path**. It grants no destination or execution authority; approval and execution remain subject to the applicable ACC and external authority mechanisms.
```

Valoración/dependencias originales se conservan. Esta segunda localización no aplica la propuesta ni declara terminada la conciliación global.

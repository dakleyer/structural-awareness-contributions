# VNext — Foundational Theory y su taxonomía de fallos

**6 de octubre de 2026 · Codex, mismo asistente de IA, revisión para una persona.** Único expediente de la unidad Foundation: [sucesor integradov0.5](01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) ycinco partesv0.4 de procedencia comparten esta VNext. Source snapshot `f7d8ed0846b301617197ade855d5237cbd2280f9`, blob `2cee8af601c89a8785bba9f48974061f0a5dc102`. Se comprobó que no existía expediente activo. [Procedimiento](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md). Ningún original se modifica.

## Alcance real — revisión focal, no lectura completa

Se leyó íntegra la nueva §1.1A, elpárrafo de taxonomía precedente, los textos conservados de § §2/3.4/3.5 ypasajes de estado/procedencia. Elarchivo integrado tiene 135.021 caracteres; **no se leyó completo ni se cotejaron exhaustivamente las cinco partesv0.4 en esta entrada**. Primera/segunda focales; edición y lectura humana de los pasajes indicados; las propias cuatro pasadas completas yquinta de Foundation siguen pendientes.

La comparación necesaria viene de las tres partes funcionales 03, leídas completas, yde 00M §1 ya cotejado. La lectura seleccionada se registra aquí para que un hallazgo material no quede sólo en la VNext del receptor.

## Fondo y lógica — ampliación como caso o condición necesaria

§1.1A hace dos precisiones defendibles: incertidumbre dentro deunA legítimo no es una avería por sí sola, ytrabajo repetido no es automáticamente Type 1. También conserva que las trayectorias I/M/P/Ø sólo diagnostican dentro delChallenge declarado ycon causalidad; unP por otro mecanismo no es necesariamente Type 2.

La frase general ylos dos bullets presentan, sin embargo, ampliación delestado oalcance como rasgo común deambos fallos. Los pasajes conservados permiten algo más general:

- **Type 1 en §3.4:** se necesita uninput definido, elrecurso no está disponible yse continúa esperando/escalando sin límite/escape. No hace falta añadir otra población, dominio uobservación alproblema.
- **Type 2 en §3.5:** elhumanono respondió pero se registra aprobación; unstatus expirado se trata como vigente; evidencia insuficiente sepromueve aPASS. Elscope representado puede permanecer exactamente igual.

**Contraejemplo conceptual propio, no experimento:** una operación espera eternamente por la misma aprobación especificada desde elinicio, sin incorporar variables. Otra recibe «no aprobado/ausente» yregistraPASS para la misma operación. Elcaso relevante es cómo se gestiona lacondición no resuelta, no una expansión observable necesaria.

**Lectura alternativa:** «broader» podría referirse metafóricamente a pretender determinar más de lo sustentado, aunque no crezca el dominio. Enesa lectura puede haber compatibilidad defondo. La propuesta 73 hace explícita esa alternativa yconserva los casos; no afirma una refutación de Foundation ni unfallo de software observado.

## Evidencia y relaciones — efectos en consumidores

La arquitectura funcional §3/F6 separa gestión Sound/Type 1/Type 2/Mixed delresidual estructural. F7 permite parar, limitar oredirigir, con ventana/capacidad; F9 conserva causa/resultado yrevalidation. Se registra el contraste en[03 VNext](03_FUNCTIONAL_VNext.md), [Requirements](00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md), [00N](00N_VNext.md), [00M](00M_VNext.md), [01H](01H_VNext.md), [01B](01B_VNext.md) y [DDS](../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md).

S5/S14/T4 ylos perfiles deChallenge deberán cotejarse completos antes deadoptar 73. No se convierte silenciosamente trabajo adicional en Type 1, ni unoutcomeØ/P en undiagnóstico causal universal. Los consumidores no ganan permiso por recibir una clasificación.

La fuente completa, los anteriores § §16–18, las hipótesis ypruebas materialmente utilizadas siguen pendientes. No se asegura que estepar cierre toda la taxonomía o sus relaciones.

## Edición y lectura humana — alcance focal

La exposición une posicionesA/B/C/D, modos defallo, ejemplo de clasificación y resultados de trayectoria. La repetición de «enlargement» en títulos/bullets puede hacer que una persona busque siempre crecimiento delscope yno examine los casos fijos conservados después. Unlector que ya conoce la definición más general puede entenderlo como ejemplo; hace falta preservar ambas lecturas para la decisión.

No renombro Type 0/1/2 ni añado otro marcador. La recomendación es decir explícitamente que ampliación es una posible manifestación, no untest de pertenencia necesario. Estas observaciones son de los pasajes leídos, no render oaudiencia humana independiente.

## Quinta propia y continuidad

**Pendiente como examen propio de Foundation.** La revisión externa particular de 03 aporta contexto sobre procedencia/consistencia ysupuestos, pero no sustituye una quinta deeste archivo. Tampoco las analogías de ArticleIV prueban la taxonomía. Se completarán los pasajes ylos precedentes realmente usados, con derechos/versiones yjuicio específico, en esta misma VNext. Sexta global pendiente.

## Plan de cambios — candidato 73 pendiente de Iván

**Fuente/ubicación:** bloque de §1.1A desde «Failure Types 1and 2share...» hasta elfinal delbullet Type 2, anterior alejemplo de gatos. Viejo completo único en elblob indicado, ya verificado. **Impacto esperado Alto, riesgo Alto, esfuerzo Alto; prioridad Primera para preparar/conciliar, tanda 3 de contratos/protocolo.** No pertenece a laprimera onda documental de bajo riesgo 26/31/32.

**Beneficio:** Evitar que diagnosticar Type 1/2 exija una ampliación del dominio cuando las definiciones conservadas ya incluyen espera indefinida, silencio tratado como aprobación o datos stale dentro del mismo scope.
**Riesgo:** Afecta taxonomía central y diagnósticos de funciones, Requirements y perfiles DDS; una modificación aislada podría cambiar cómo se interpretan controles o resultados históricos.
**Coste:** Conciliar el bloque 1.1A con § §2/3.4/3.5 conservados, función F6/F7, RequirementsS5/S14/T4 y diagnósticos DDS/realizaciones. No basta modificar un título o un párrafo; la lectura integral de Foundation sigue pendiente.
**Compatibilidad/orden:** conservar la fuente de 00M, tipos anteriores ycausalidad deChallenge; revisar con 03/Requirements/00N/DDS ycasos deobservación/espera dentro deunscope fijo. Completar la lectura integral de Foundation antes deconsiderar elpar incorporable.

**Texto antes — viejo literal completo**

~~~~markdown
Failure Types 1 and 2 share the same root mistake: the system does not respect the qualified boundary of the active exploitation result A relative to B/C/D. In both cases it tries, explicitly or operationally, to treat a broader portion of the surrounding state as if it could be brought into one decision result. The difference is how that attempted enlargement fails.

- **Failure Type 1 — non-viable enlargement / failure to decide.** The system keeps extending observation, search, verification, escalation or qualification in an attempt to absorb more B/C/D material into a broader or more certain decision result. Because the additional material is not yet supported by an adequate evaluation basis, the active determination becomes less viable: uncertainty may widen, confidence may fall, or the system may remain unable to justify a decision at all. The characteristic operational outcome is not “extra work” but failure to reach bounded legitimate closure before budget, capacity or response horizon is exhausted.
- **Failure Type 2 — unjustified enlargement / false decision.** The system also broadens what it treats as operationally determined, but instead of remaining unresolved it collapses insufficiently qualified B/C/D material into A, permission or a globally valid closure. It therefore produces a decision, but one whose scope or certainty exceeds the established basis. The characteristic operational outcome is false closure or an unjustified action.
~~~~

**Texto después — propuesto completo**

~~~~markdown
Failure Types 1 and 2 fail to preserve the qualified boundary between what the process can establish and what remains insufficiently determined. Unqualified enlargement of observation or claimed scope is one way this can happen; it is not a necessary condition. Both failure types can also occur within an unchanged represented scope.

- **Failure Type 1 — failure of bounded legitimate closure.** Acknowledged uncertainty remains active through waiting, search, verification or escalation without a justified capacity/time bound or escape condition. This may involve an attempted enlargement, but may also occur while waiting for one already-defined input within the existing decision scope. Additional work alone is not Type 1; the relevant failure is unresolved determination managed in a way that exhausts or fails to preserve a viable legitimate response.
- **Failure Type 2 — suppressed insufficiency / false closure.** The process suppresses material uncertainty, missing input, invalidated support or a scope limit and presents unsupported closure or action as justified. This may broaden claimed scope, but may also occur within the existing scope by treating silence as approval, insufficient evidence as PASS or stale status as current. A prohibited outcome caused by another mechanism is not automatically Type 2.

The causal treatment of non-determination, the declared scope and the supported response contract govern the diagnosis. Correctly bounded unresolved state remains a legitimate outcome; neither extra work nor an outcome label by itself establishes a management failure.
~~~~

**Instrucciones de Iván:** original sólo lectura, una VNext porunidad, preservar elviejo ylas conversaciones, valorar impacto/riesgo/coste yproponer antes/después quirúrgicos. Decisión concreta pendiente; ninguna taxonomía, métrica, esquema oresultado se modifica por publicar esta auditoría.

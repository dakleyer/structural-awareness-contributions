# Conciliación de integraciones — EA, Regime Awareness y MSCA

**Auditoría realizada por Codex, 6 de octubre de 2026.** Mismo asistente de IA, para que una persona examine la relación y sus propuestas. [Plan 1.5](../CORPUS_REVIEW_PROCEDURE_2026-10-06.md#alcance-confirmado-todo-contributions-y-sus-integraciones) · [alcance completo](./EP_REVIEW_REPOSITORY_SCOPE_2026-10-06.md).

La revisión comprende todo Contributions. Esta primera matriz examina la unión central; las demás interfaces, aplicaciones y pruebas siguen dentro del alcance y pendientes de sus propias lecturas. Se conserva una VNext por documento lógico y todos los originales.

## Qué se cotejó

Fuente fijada: commit `e80846a0f9cf3b97cf222ed3d1e28b31d145ad3e`. Se leyó completo 01D y los README RA/MSCA; EA router y las especificaciones vecinas se cotejaron en pasajes declarados en sus VNext. Los artículos externos, las especificaciones completas aún pendientes y los runtimes no se dan por revisados con este registro.

| Relación | Qué debe conservar el productor y el consumidor | Resultado documental de esta entrada |
|---|---|---|
| EA ↔ MSCA, 01B | Posición calificada frente a assessment de configuración; mismo S/E, scope y versión; permiso separado. | El pasaje de 01B y 01D conservan SUPPORTED ≠ permiso. Resto de 01B y realizaciones pendientes. |
| EA ↔ RA, 01C | Evidencia de régimen limitada por representación/contexto, frente a calificación de decisión; P_RA mínimo y Δ_RA amplio diferenciados. | 01C explicita soporte/reserva, exploración y barrera efectiva. El resumen del README RA es más estrecho y debe conciliarse. |
| Cartografía ↔ RA | Cart_i y Δ_Cart,i calificados hacia RA; delta/overlay/requests de vuelta; persistencia en Composition & Control. | Los pasajes cotejados coinciden en el dueño de persistencia. No se ha probado actualización operacional ni cobertura de todas las versiones. |
| RA → MSCA Operation | Δ_RA con significado, scope, contexto, versiones y vigencia conservados. | El input está atribuido a RA; su resumen “intensity/capability/residual” necesita cotejo con 01C y sus consumidores. |
| EA + RA + MSCA + autoridad, 01D | Mismo identificador de operación/decisión, objetivo, alcance, versiones y ventana; legitimidad y ejecución separadas. | 01D completo conserva binding, dependencia condicional, UNKNOWN no neutral, costo sin doble conteo y effect distinto de receipt. No aporta un run. |
| Delta amplio ↔ perfil mínimo de 01D | Declarar la especialización o mapping utilizado, sin fabricar P_RA ni heredar una garantía por compartir nombre. | La introducción de 01D menciona Δ_RA; sus reglas usan P_RA mínimo. Falta hacer explícita la relación para perfiles amplios; candidato en su VNext. |
| Señales/ACC → operación, feedback y siguiente ciclo | Fuente, identidad, authority response, permiso, efecto y nueva vigencia sin convertir señal en comando. | Ruta identificada. Lectura integral de 01H/01I/01J, ACC, gradient y sus implementaciones sigue pendiente. |
| General interfaces → aplicaciones → casos/tests | Propietario semántico, requisitos y grado de evidencia conservados; ninguna aplicación redefine el canon genérico. | Se mantienen los expedientes existentes 04/05/05A. La ampliación no declara terminadas sus fuentes o pruebas. |

Una coincidencia textual puede ser correcta y aun así no cubrir un consumidor particular. El examen continúa por perfiles y versiones reales, no por firmas repetidas o cantidad de enlaces.

## Tres problemas concretos para conciliar

**Confianza y magnitud del cambio.** B_RA contiene fundamento y reserva caracterizada; confianza califica evidencia. El README RA todavía dice confianza/intensidad y MSCA Operation mantiene una abreviatura similar. Puede inducir una implementación que trate confianza como magnitud física o pierda una reserva evaluable.

**Una capacidad no equivale siempre a C.** Las opciones conocidas y evaluables que no se usaron permanecen B. Una frontera de exploración C requiere grounds y ausencia de un marco de evaluación ya caracterizado. Unknown no es automáticamente D. Estas diferencias deben sobrevivir el handoff.

**Dos representaciones RA requieren una relación explícita.** 01D preserva bien el contrato del detector mínimo, pero un perfil que consuma el delta amplio necesita declarar qué parte consume y bajo qué mapping. No se presume que una proyección semántica preserve cada afirmación de detección o seguridad.

Los candidatos exactos quedan en [RA README VNext](../../research/regime-awareness/README_VNext.md), [MSCA README VNext](../../standards/minimum-sufficient-control/README_VNext.md), [MSCA Operation VNext](../../standards/minimum-sufficient-control/04_OPERATION_VNext.md) y [01D VNext](../../research/ecosystem-awareness/baseline/01D_VNext.md). [01C VNext](../../research/ecosystem-awareness/baseline/01C_VNext.md), [EA README VNext](../../research/ecosystem-awareness/README_VNext.md) y [EP README VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md) conservan el contraste de fuentes, consumidores y lectura.

## Qué significa proteger una integración antes de cambiarla

Una propuesta debe identificar a sus consumidores y comprobar ejemplos en ambos sentidos: entrada válida, dato ausente, contradicción/dependencia común, cambio de versión o scope, vencimiento, permiso viejo, capacidad/plazo insuficientes, retorno y resultado no establecido. Se distingue preservación de semántica, payload, comportamiento y evidencia; ninguna se infiere automáticamente de otra.

Las comprobaciones de esta fase son documentales y de conservación. No se renombró ningún field, se modificó un contrato técnico, se recalculó un manifest congelado, se ejecutó un harness o se activó un experimento. La validación de compatibilidad de las realizaciones queda abierta.

**Estado:** cotejo central iniciado, discrepancias documentadas y propuestas pendientes; integraciones completas del repositorio todavía no cerradas.

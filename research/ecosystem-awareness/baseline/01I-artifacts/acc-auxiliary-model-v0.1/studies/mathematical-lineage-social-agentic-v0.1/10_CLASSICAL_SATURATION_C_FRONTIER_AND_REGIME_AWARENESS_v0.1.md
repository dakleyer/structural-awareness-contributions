# 10 — Saturación de la explotación caracterizada, exploración C y recualificación de régimen

**Anexo de investigación v0.1 · Stage A · 27 de octubre de 2026 · revisión del propietario pendiente.**  
**Origen conceptual:** Iván Abril Palma / The Integral Management Society. Formalización y redacción técnica asistidas por IA.  
**Ubicación y alcance:** PR #60, puente matemático social → agéntico; **no** modificación del modelo ejecutable de PR #57, de los resultados congelados, de 00M/00N, de UC21/DDS ni del contrato de Regime Awareness. **No** es una implementación, un teorema universal ni una validación experimental.

> **Tesis de trabajo.** El modelo agéntico debe poder explotar y orquestar todas las opciones *caracterizadas, gobernables y económicamente admisibles*, incluyendo transferencias de recursos y pivotes entre actores. Cuando ese espacio está saturado para una pregunta y un presupuesto declarados, la siguiente investigación puede dirigirse a una frontera C fundada: opciones cuya sintaxis, mecanismo de coordinación o base de evaluación no está todavía caracterizada. Un resultado `INDETERMINATE` conserva la pregunta, **no** acredita la mejora. Su caracterización, eventual admisión y cambio de operación pueden suministrar evidencia de *recualificación* para Ecosystem Awareness y, bajo condiciones de observabilidad independientes, motivar Regime Awareness.

## 1. Fuentes, significado de las letras y límites

- [00M — definiciones canónicas A/B/C/D](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md): **A** resultado de explotación activa; **B** fundamento y reserva de explotación caracterizada; **C** frontera de exploración fundada pero sin base de evaluación suficiente; **D** residual más allá de la vía efectiva de evaluación del proceso. Son papeles relativos a actor, función, pregunta, alcance y tiempo; **no** cuatro compartimentos globales de soluciones.
- [Modelo social ACC](../../MODEL.md) y [núcleo económico](../../ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md): eficiencia, reparto/utilidad, coordinación, atribución, autoridad; óptimo técnico distinto de conjunto gobernable y de rutas de transición. **La C de coordinación social no equivale a la C canónica de exploración**.
- [PR #57 — reducción agéntica](https://github.com/dakleyer/structural-awareness-contributions/pull/57): transferencia/transformación autorizada bajo stock físico y coste explícitos; AG01 `10→11,5` y óptimo técnico de referencia `13,5`, con controles adversos. Es un escenario sintético, no un detector de C ni de régimen.
- [Partes 02–04 de este expediente](./02_FORMAL_CORE_AND_PROOFS.md), [03 — metaprotocolo acotado](./03_METAPROTOCOL_ALGORITHMS_AND_COST.md) y [07–08 — interfaz y pruebas Theme #18/RA](./07_THEME18_COLLECTIVE_CHOICE_REGIME_ADEQUACY_INTERFACE_v0.1.md): suficiencia dependiente de la misión, coste, autorización y distinción entre régimen de elección, régimen observable y adecuación decisional.
- [SA-MATH-MULTI-01 — intersección colectiva de residuos](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/structural-awareness/SA_COLLECTIVE_RESIDUAL_INTERSECTION_AND_OPPORTUNITY_v0.1.md): De Morgan caracteriza el rechazo conjunto; sólo predicados positivos cualificados y una cota adicional pueden acreditar mejora. Su extensión sintética Stage 1/2/3 tiene 46 comprobaciones finitas, no observaciones reales.

**Vocabulario imprescindible.** En una pregunta concreta, `TRUE/FALSE/INDETERMINATE` describe la respuesta del evaluador; **no es una clasificación A/B/C/D**. Un coste pendiente de medir dentro de un método establecido puede ser **B**. Para hablar de **C** debe faltar todavía una base defendible de evaluación —por ejemplo, una nueva forma de coordinación o de representar la función— y debe existir un indicio fundado para explorarla. Una barrera sin vía efectiva de evaluación puede ser D; sin delimitar proceso y alcance, ni siquiera debe forzarse una letra.

## 2. Primera vía: orquestación y pivote clásicos, plenamente válidos

Sea `κ` una misión, horizonte, derechos, actores y presupuesto de recursos fijados. Definimos `X_chr(κ)` como las configuraciones, transferencias, evaluaciones y pivotes ya **caracterizados** bajo esos contratos. `F^G_chr(κ)` restringe ese espacio a las transiciones física y jurídicamente **alcanzables y autorizadas**, incluyendo tiempo, coordinación, consentimientos y costes. Sea `x₀` el estado actual y `≻_κ` una relación de mejora predeclarada (por ejemplo, dominancia para los afectados, manteniendo servicio y garantías).

La búsqueda inicial es ordinaria y valiosa:

\[
\operatorname{Improve}_{\rm chr}(\kappa)=
\{x\in F^G_{\rm chr}(\kappa):x\succ_\kappa x_0\}.
\]

El orquestador puede **reasignar presupuesto, negociar, compensar, liberar capacidad, cambiar cargas o pivotar funciones** dentro de las transformaciones autorizadas. Lo que ya puede evaluar permanece en B aunque el coste haga preferible no ejecutarlo. Si encuentra una mejora admisible, la lleva a decisión/ejecución sin invocar metasintaxis.

**Saturación local y relativa:** `Improve_chr(κ)=∅`, establecido por búsqueda exhaustiva en un marco finito o por certificado sólido del solver para ese marco, significa **ninguna mejora dentro de ese espacio caracterizado y esos límites**. No significa `ninguna mejora posible en el ecosistema`, ni que todo el universo C sea no vacío, ni que las computadoras clásicas carezcan de potencia para investigar. Un timeout, una heurística sin cota o una lista incompleta **no certifican** saturación: producen `UNKNOWN`.

El modelo puede ser subóptimo frente a un referente técnico y, aun así, no tener mejora **gobernable y alcanzable** con sus condiciones actuales. Óptimo técnico, óptimo autorizado, máximo alcanzable por transición y solución observada son cuatro objetos distintos.

## 3. Segunda vía: explorar una indeterminación estructural fundada

Si la vía caracterizada no produce mejora, una pregunta adicional legítima es si existe **una forma diferente de realizar la misma función** cuya evaluación no se representa adecuadamente en `X_chr(κ)`. Denotemos por `Y_C(κ)` un conjunto **simbólico de direcciones/candidatos testimoniados de exploración**, nunca un inventario completo de C. Para un candidato `y`, el evaluador puede tener `c_coord^κ(y)=INDETERMINATE` porque le faltan variables, método o tipología para caracterizar la coordinación; no porque el coste físico sea inexistente ni porque `c_coord(y)≤B` sea verdadero.

La secuencia propuesta:

1. **Certificar o calificar el límite actual.** Congelar misión, fuentes, presupuesto, políticas, espacio caracterizado y resultado de búsqueda; aceptar `UNKNOWN` si no hay cierre válido.
2. **Conservar el residuo de admisión.** Identificar qué no admite o no puede caracterizar la sintaxis/función actual, con el motivo, productor, derechos y validez. `FALSE` sustantivo no pasa a `UNKNOWN` por conveniencia.
3. **Testimoniar una dirección C.** Mostrar por qué un cambio de mecanismo, topología, interfaz, función o fuente podría atender la pregunta; no calcular probabilidades o ahorros sin base.
4. **Relacionar reservas B de otros participantes.** Una fuente puede caracterizar capacidad útil para el problema de otro agente; el receptor debe validar semántica, alcance, procedencia, permiso, coste y relevancia. La composición puede abrir una vía de evaluación, no transferir automáticamente autoridad.
5. **Obtener un candidato concreto y cualificarlo.** Verificar coste completo, servicio, utilidad, terceros afectados, derechos, riesgos, viabilidad y transición. Sólo entonces la parte estudiada puede pasar a B de una pregunta evaluable o producir un nuevo A al ejecutarse.
6. **Recualificar misión y régimen cuando proceda.** Registrar si la representación operativa, conjunto de acciones autorizadas, dependencias o contexto observable cambiaron; no confundir una clasificación distinta con un evento físico detectado.

### El límite de la intersección de residuos

Para un dominio común interpretado `Ω` y clases localmente admitidas `Sᵢ`, el residuo extensional conjunto es `R_joint = Ω \ (⋃ᵢSᵢ) = ⋂ᵢ(Ω\Sᵢ)`. Eso prueba **rechazo por todas las admisiones actuales**, no calidad ni existencia física de una oportunidad. Los casos donde los agentes devuelven `UNKNOWN` sobre una propiedad no convierten esa propiedad en falsedad.

La inferencia positiva necesita además afirmaciones cualificadas `Qᵢ(y)` aplicables al **mismo candidato** y una justificación adicional, por ejemplo `∀y∈Hκ, U(y)≥U(x₀)+g`, para una región `Hκ` suficientemente definida. Fuente falsa, intersección vacía, candidato no encontrado, coste mayor al presupuesto, restricción sustantivamente falsa o autoridad ausente hacen fallar la promoción. No se promete llegada ni casi-optimalidad por contar más agentes.

## 4. Tres ejemplos con la misma separación de vías

| Caso | Vía clásica caracterizada: explotación, transferencia o pivote | Frontera C fundada: estructura no caracterizada | Evidencia que permitiría pasar hacia B/A | Control negativo |
|---|---|---|---|---|
| **Plátano** | No comprarlo; donar mediante contacto individual o plataforma; transferir recursos para organizar recogida. Si toda mejora conocida excede el presupuesto de atención del donante, la vía queda saturada **para ese actor y contrato**. | Caja comunitaria de 4–5 vecinos: pasa de coordinación bilateral explícita a depósito/recogida asincrónica. No está caracterizado si el coste marginal y completo (limpieza, seguridad, caducidad, mantenimiento, responsabilidad) respeta límites. | Disponibilidad del punto, consentimiento, seguridad alimentaria, coste total y por actor, participación y prueba de utilidad; nuevo protocolo de cooperación aprobado. | El mantenimiento o riesgo hace la caja más costosa; nadie recoge; regla sanitaria la impide. Los 14.000 km son sólo contrafactual ilustrativo; una caja al final de la cadena no recupera transporte ya realizado. |
| **Teletrabajo** | Mejoras de mobiliario, espacios, horarios o despliegue remoto **ya caracterizado** dentro de políticas existentes. | Examinar si «entorno adecuado de trabajo» puede cumplirse fuera de «oficina física propiedad de la empresa»; cambia la categoría que representa el medio de producción, no sólo la calidad de la silla. | Contrato funcional, rendimiento equivalente, seguridad, ergonomía, consentimiento, reglas laborales y autoridad para cambiar la obligación presencial. | Una función exige presencia física o la obligación no es modificable; entonces no se reetiqueta un `FALSE` como `INDETERMINATE`. |
| **Dos ministerios** | Eliminar duplicaciones o transferir recursos entre sistemas y servicios con atribución, derechos, empleo y transición ya modelados; optimización clásica de muchos actores. | Considerar una topología de función compartida, delegación o prestación cruzada no representada en los diseños admitidos; evaluar nuevas relaciones de autoridad y reparto. | Equivalencia de servicio, costes reales, continuidad, derechos, protección de personas, mandatos y aprobación de transición. | Ahorro técnico pero perjuicio no compensado o falta de competencia legal: no constituye automáticamente mejora paretiana ejecutable. |

**Lectura común:** la oportunidad no es «el elemento con coste desconocido que seguramente es mejor». Es una **hipótesis de cambio estructural** que conserva un objetivo y busca una forma distinta de cumplir sus condiciones. Lo que resulta B para un agente puede ser C para otro; no existe un «B de todos» común sin correspondencias y condiciones de interpretación verificadas.

## 5. Puente a Regime Awareness y Ecosystem Awareness

Hay **tres acontecimientos diferentes** que se deben registrar por separado:

| Objeto | Pregunta | Lectura válida | Lectura inválida |
|---|---|---|---|
| **Frontera de admisión / exploración** | ¿Llegó una opción o propiedad que la función actual no puede clasificar/evaluar? | Indicio para revisión específica; posible C para el receptor. | «INDETERMINATE demuestra una mejora». |
| **Cambio de estructura operativa** | ¿Se autorizó/adoptó otra topología, operación, rol o conjunto de opciones? | Nueva versión del contrato/espacio factible, posible pérdida de suficiencia del A anterior. | «Toda nueva idea ya constituye un cambio de régimen físico». |
| **Cambio observable de régimen RA** | ¿La fuente, observables, contexto, referencia y umbral validan una salida direccional o transición? | Señal acotada `RA-OBS` que puede activar recualificación para una decisión. | «Más candidatos desde C garantiza un cambio exógeno detectado» o «RA autoriza ejecutar». |

Por [07 — interfaz Theme #18](./07_THEME18_COLLECTIVE_CHOICE_REGIME_ADEQUACY_INTERFACE_v0.1.md), `C18-REF` conserva autoría, régimen de elección, objetivos, modo y versión; `RA-OBS` señala sólo cambios observables cualificados; `EA-QUAL` pregunta si la evidencia todavía sostiene una decisión; la autoridad de control/oversight es externa. **EA puede necesitar recualificar por ampliación de operaciones o nuevas restricciones aun sin señal RA positiva**. Si hay cambio real pero `Ψ` no lo observa adecuadamente, RA debe conservar `UNKNOWN`.

La saturación de un conjunto de opciones, la frecuencia de candidatos C y el paso de un candidato a una nueva sintaxis son **candidatos a indicadores** de fronteras y de cambio de régimen operacional. Para convertirse en indicadores de RA requieren hipótesis, registro longitudinal, observables independientes, umbrales, falsos positivos, latencia y pruebas de pertinencia. En EA sirven primero como **contexto cualificado para decidir qué revisar**, no como orden de seleccionar una alternativa.

## 6. Contrato mínimo para un experimento próximo (propuesto; no ejecutado)

Congelar para cada episodio: `actor_id`, pregunta/objetivo independiente, `A` vigente, registros fuente y límites `B`, frontera C testimoniada, D material y `UNKNOWN`, operaciones `Σ₀/Σ₁`, catálogo clásico `X_chr`, recursos físicos y coordinación por actor, autoridades y derechos, pruebas de saturación, candidato y motivo de inadmisión, `Q` fuente-calificada, coste de indagación, transición, verificación y monitorización, referencia/timestamp/modo, señal RA con sus condiciones y resultado EA separado de la decisión final.

**Brazos y falsadores**, distinguiendo aquí los nombres experimentales de los identificadores oficiales UC21/DDS:

1. **E0 — orquestación clásica competente:** mejor algoritmo disponible sobre alternativas y pivotes caracterizados, con los recursos, permisos y observaciones realmente disponibles; puede ganar o resolver sin exploración C.
2. **E1 — conservación de indeterminaciones, sin promoción:** mismo proceso y presupuesto; retiene testigos, no inventa opciones y no actúa sobre incertidumbre.
3. **E2 — exploración C y cualificación acotadas:** accede sólo a eventos, evidencias y transformaciones autorizadas; intenta caracterizar alguna opción, con coste completo y resultado `UNKNOWN` cuando procede.
4. **E3 — comparador convencional igualmente informado:** dispone de las mismas observaciones, certificados, intérprete y permisos que E2. Si empata, **no hay diferencial de computabilidad o arquitectura acreditado**.
5. **Referee independiente:** fija realidad del caso, límites de recursos, derechos, transiciones y utilidad para puntuar aciertos, errores, abstenciones, falsas promociones, retraso, carga y ahorro neto. No entrega sus datos secretos como si fueran `Q` operativa.

Controles imprescindibles: (a) quedan pivotes B válidos y E0 resuelve; (b) catálogo finito no exhaustivo y saturación `UNKNOWN`; (c) C sin candidato o candidato inferior; (d) propuesta que excede recursos o derechos; (e) D sin vía efectiva; (f) fuente falsa/caducada; (g) cambio estructural sin evidencia RA; (h) RA válido pero misma decisión justificada; (i) E3 empata/supera E2; (j) nueva clasificación sin cambio de régimen material. Medir recursos de coordinación **por participante y del sistema completo**, no trasladar silenciosamente el coste del donante a vecinos o infraestructura.

**Resultados que sí podría respaldar un futuro experimento:** proporción de saturaciones locales correctamente diagnosticadas; candidatos C efectivamente caracterizados; mejoras finales factibles; costes netos y transferencias; ganancia o ausencia de ganancia informacional; detección/recalificación de cambios observables; distinción entre nuevo régimen operativo y nueva evidencia sobre el mismo régimen. Ninguna de estas métricas se infiere de los 46 checks matemáticos o los números sintéticos AG01 por sí solos.

## 7. Estado y decisiones pendientes

| Claim | Estado | Qué faltaría |
|---|---|---|
| El solver clásico puede optimizar, transferir y pivotar mientras su espacio factible esté caracterizado | **S/R — formalización condicionada al catálogo y restricciones** | Establecer completitud del catálogo o reportar límite de búsqueda en cada caso. |
| Saturación relativa no implica ausencia de alternativas fuera de la sintaxis | **S — consecuencia lógica del alcance de cuantificación** | No convertirlo en afirmación de existencia de una solución. |
| Una frontera C puede sugerir otro mecanismo de coordinación/función | **R/H — dirección fundada e hipótesis de valor** | Construcción, fuente, método, presupuesto y controles negativos. |
| Un candidato C puede convertirse en B/A mediante evidencia y actuación legítima | **D condicional / H empírica** | Prueba específica de validez, recursos, derechos y resultado. |
| La intersección de residuos puede ayudar a reconocer un candidato mejor | **D condicional, sólo con propiedades positivas adicionales** | Candidato encontrado, Q genuina y cota de valor; no basta De Morgan. |
| Las llegadas desde C revelan un cambio de régimen RA | **H; no demostrado por mera llegada** | Evidencia independiente de cambio observable, modelo temporal y falsadores. |
| Un metaprotocolo tiene ventaja neta sobre un comparador convencional igualmente capacitado | **H abierta, quizá falsa** | Ensayo pareado sin negarle Q, autoridad, búsqueda o información al comparador. |

**Próxima revisión:** contrastar este anexo con el contrato de los seis principios EA y S1–S14 **sin asumir equivalencias por el nombre**, y con UC21/DDS respetando sus etiquetas originales, puertas de fallo/reparación y estados de prueba. Cualquier adaptación ejecutable debe añadirse en un artefacto/PR separado y verificado, sin reescribir retrospectivamente PR #57 ni el canon 00M/00N. No se solicita merge ni promoción a canon mediante esta nota.

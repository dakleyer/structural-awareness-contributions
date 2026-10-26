> Registro de preparación incorporado al expediente GitHub existente el 13 octubre 2026. Las menciones a «local» describen su preparación anterior. Rige [la orientación R2/freeze/R3](PRINCIPIO_R2_FREEZE_R3_2026-10-13.md); los checks siguen siendo sintéticos y no un ensayo nativo. Volver a [CAMPAIGN](../CAMPAIGN.md) o [CONTINUATION](../CONTINUATION.md).

# Protocolo temporal para Flores y requisitos EA

Borrador 0.2. Fecha: 13 octubre 2026. Campaña de trabajo: DDS-A-FLORES-POP-EA-01, identidad prospectiva existente. Este protocolo es una propuesta sucesora local; no reemplaza la v1.0 del productor ni sus acceptance criteria.

## 1 Objeto y preguntas congelables

El eje es R2 reparada → freeze → R3 no cubierto. La igualdad en el contexto reparado se admite como base. El participante decide y defiende el nivel de configuración; se demuestra la reparación antes de congelarla.

La primera campaña recorre el cambio material posterior con R2 completa congelada. La segunda estudia qué requisitos generales EA, fijados antes de revelar R3, permiten advertir la pérdida de fundamento y recalificar. No es un concurso de superioridad dentro del caso conocido.

La misma pregunta temporal, sujeto, finalidad y regla de aceptación se declaran desde t0. Se conservan código, parámetros, fuentes, defensas, permisos y adaptación efectivamente incluidos en R2. Cada patch posterior al R3 constituye un nuevo R2/freeze y no repara retroactivamente el resultado puntuado.

[R2 congelada y R3](PRINCIPIO_R2_FREEZE_R3_2026-10-13.md) gobierna la selección. Epoch/witness solo sirve si el R2 realmente defendido no cubre ese cambio. NOT_ESTABLISHED no se equipara a adivinar una truth oculta.

## 2 Registros obligatorios

| Registro | Contenido | Acceso |
|---|---|---|
| Producer snapshot | Commit, spec, fixture autorizado, seeds, código y results oficiales cuando existan | Derechos de origen |
| Context relation | Sujeto, scope, referencia, origin, parent, periodo, tiempo efectivo y materialidad | Igual B2/EA |
| World definition | Verdad, causal intervention, tiempos y mundos alternativos | Evaluador |
| Candidate packet | Solo datos/consultas permitidos; no oracle labels | Candidato |
| Output | Estado, razones, dependencias y scope | Evaluador y dueño |
| Ledger | Query/time/resources/human profile labour | Evaluador |
| Commitments | Hashes de contrato, world y fuentes; responsable y fecha | Custodia |
| Return | Qué conserva validez, qué no está establecido y quién actúa | Receptor legítimo |

El hash de un objeto valida igualdad de bytes frente a un valor, no su verdad ni autoridad. La admisión de issuer debe basarse en un régimen de permisos conocido, no en un campo escrito por el propio issuer.

## 3 Intervención seleccionada para preparar

Pérdida o cambio de una asociación vigente de contexto, sin alterar el registro histórico y sin escribir el answer label de pérdida. Formas posibles: pérdida de vínculo actual referencia→subject, ruptura de asociación report→scope, o ausencia de nueva certificación de un epoch relevante.

Antes de ejecutarla, el source owner y el adjudicador deben elegir **una** de esas formas. No se mezclan como cambios simultáneos. Para la demo de contrato se usa epoch: t0 e0 con witness aplicable; t1 e1 con solo witness e0; t2 witness e1 legítimo. El epoch es un dato de contexto synthetic y no un hecho externo verificado.

El significado de e0/e1 debe tener materialidad. Cambiar un contador sin efecto en Q no elimina identificabilidad. Si un test únicamente prueba mismatch de versiones, su conclusión se denomina mismatch/insuficiencia y recibe pleno crédito convencional.

## 4 Ubicación en el runner

Preservar la ejecución original v1.0 como baseline. La extensión crea un wrapper temporal que llama o reproduce el cálculo original con la misma matriz y deja operar la fuente de contexto en paralelo. El evento se aplica al sistema experimental extendido mientras la decisión sigue pendiente.

Si detect.py consume un archivo estático, no puede describirse esa prueba como seis modelos que ven nuevos hechos en streaming: los jueces son scripted y el detector lee el artefacto que recibe. Una segunda llamada con el mismo archivo es un replay del detector en un contexto externo distinto. Si se quieren jueces que reciban datos nuevos, se necesita una v1.1/otro perfil source-owner autorizado y una prueba distinta.

El wrapper no recalibra el threshold, no altera el order de draws ni la clave, no incorpora UC17-08 al scoring y no abre sealed.json antes de tiempo. La extensión introduce una condición y su trazabilidad; no convierte el error del consumidor en un defecto imputado al productor.

## 5 Secuencia completa

1. Fijar familia, Q temporal, sujeto, P, observaciones, recursos y positivos.
2. Obtener source snapshot y resultados autorizados; conservar la v1.0 del productor.
3. Permitir que el participante configure y repare hasta el nivel defendido.
4. Demostrar R2, sus positivos y la igualdad esperable en el contexto conocido.
5. Registrar alcance y congelar R2 completa con toda su adaptación y defensas.
6. Fijar la especificación EA general antes de revelar el R3 puntuado.
7. Adjudicar un cambio externo material no cubierto por esa reparación; no retirar defensas.
8. Recorrer R3 con mismo R2 y conservar source outputs, inputs y tiempos.
9. Registrar pérdida de fundamento, reconocimiento, continuidad y consecuencias de reliance.
10. En campaña EA, evaluar requisitos generales ante ese R3 con el contrato de acceso común.
11. Comprobar reentrada/recuperación y actividad no afectada dentro del horizonte.
12. Preservar resultado, incluso adverso. Una reparación posterior inicia otro R2 y freeze.

Los controles básicos públicos son calibración; no se reetiquetan como R3 nativo. No se modifican los seis runs ni los acceptance criteria originales de Flores por este documento.

## 6 Lote mínimo y controles

| Caso | Mundo | Observación elegible | Resultado requerido | Rol |
|---|---|---|---|---|
| C0 | Relación material vigente | Evidence y vínculo admitidos | Soporte de Q en el alcance | Baseline |
| C1 | Cambio benigno | Solo cambia decoración | Continuidad | Falso positivo |
| C2 | Condición P ya no establecida | Mismos votos; cambio bruto material visible | Recalificación selectiva | Cambio central |
| C3 | Condición restituida | Fuente/vínculo legitimados | Recuperación sin borrar C2 | Recovery |
| C4 | Dos verdades ocultas | Inputs completos iguales | No detección específica; NOT_ESTABLISHED si base falta | Límite |
| C5 | Vía alternativa legítima | P original ausente, otro fundamento suficiente | Continuidad | Evitar deny-all |

C0–C5 son la propuesta mínima. Tres adversarios pueden reservarse si el reviewer considera material su riesgo: replay de witness viejo, fuente contradicha, scope equivocado. La matriz pública K00–K19 es calibración, no expansión automática del lote scored ni prueba ciega.

C4 no necesita introducir un cuarto juez ni cambiar seeds. Su rol es fijar el límite de inferencia. Entregar los dos mundos juntos con nombres que revelen la condición invalida el ensayo de ceguera.

## 7 Tres fronteras de observación

| Frontera | Qué recibe | Qué puede concluir |
|---|---|---|
| O_votes | Veredictos fuente y datos que v1.0 declara | Desviaciones dentro de ese contrato |
| O_context | O_votes más fuentes y relaciones de contexto legítimas | Soporte actual de Q si su base es suficiente |
| O_oracle | Estado completo del mundo y verdad oculta | Criterio de evaluación; nunca input candidate |

Comparar O_votes con O_context identifica el valor de **información adicional**, no el valor de EA. Para diferencial metodológico se compara B2 versus EA dentro de O_context. O_oracle no se ofrece a ningún brazo.

Si alguna consulta ofrece una diferencia oculta, deja de ser un par completo idéntico. Registrar transcript, permissions y clocks. Comparar solo input inicial ignorando consultas posteriores no acredita indistinguibilidad.

## 8 Hipótesis y decisiones

H0-context: con el mismo full observation transcript, la distribución de respuestas es la misma bajo mundos compatibles; el hecho oculto no puede identificarse con garantía.

H1-source: matriz/flags originales permanecen idénticos frente a la intervención externa, si sus inputs permanecen idénticos.

H2-requalification: con una señal admisible de cambio material, el candidato retira únicamente la dependencia afectada y no convierte ausencia en contradicción.

H3-recovery: una evidencia válida recupera solo lo que fundamenta; una evidencia repetida, fuera de scope o stale no lo recupera.

H4-peer: B2 puede ser equivalente o mejor en correctness/continuity y coste. Se acepta NO_DIFFERENTIAL.

H5-burden: añadir un perfil EA solo es útil dentro del scope si mejora alguna dimensión relevante sin incumplir los límites de las restantes, conforme a regla ex ante.

H0 y H1 tienen demostraciones de límite en un modelo definido, no sensibilidad universal empírica. H2–H5 requieren ejecuciones comparativas y reviewer. La ejecución de código abstracto no promueve automáticamente la evidencia a DDS Stage C.

## 9 Adjudicación de t0 y t1

El adjudicador deberá responder:

- ¿Qué parámetro o proposición era identificado en t0?
- ¿Qué worlds estaban excluidos y por qué fuente/regla legítima?
- ¿La intervención cambió el mundo, la arquitectura de observación, la vigencia de una evidencia o solo la confianza subjetiva?
- ¿Existen dos worlds compatibles en t1 con respuestas distintas?
- ¿El candidate puede distinguirlos mediante alguna observación o consulta permitida?
- ¿La evidencia histórica sigue correcta para su periodo?
- ¿Puede una vía alternativa conservar soporte?
- ¿El evento source-side fue producido realmente o está simulated por el experimenter?

Si solo se demuestra retirada de proof relation, dictamen BASIS_NOT_ESTABLISHED. Si hay contraejemplo de identificación, dictamen IDENTIFIABILITY_LOST_IN_DECLARED_MODEL. Si Q es contradicha por evidence vigente, REFUTED. No acumular esos dictámenes como un mismo PASS.

## 10 Falsadores que invalidan un resultado favorable

| Falsador | Efecto |
|---|---|
| Q no era identificado en t0 | No conclusión de pérdida |
| Q cambia de finalidad o subject tras t0 | Nuevo scope; no same-claim test |
| Se altera generator/key/reference original sin versionar | Comparación baseline inválida |
| Se usa expected.py como observed run | Resultado mal clasificado |
| Candidate recibe “context lost” o oracle value como answer | Circularidad |
| EA recibe un canal que B2 no recibe | Ventaja de información |
| Se oculta una consulta que distingue worlds | Par de indistinguibilidad inválido |
| Se puntúa negar todo como seguro | Positivo de continuidad fallado |
| Recovery borra historial o sigue label sin evidence | Reentrada injustificada |
| Se llama C a mismatch caracterizado | Etiqueta sin fundamento |
| Witness desaparece pero alternate válido se ignora | Falsa pérdida de base |
| Tiempo posterior al deadline se puntúa útil | Viabilidad fallada |

Los raw controls corregidos del preflight sirven para aprender estos fallos. Un lote scored debe usar fixtures nuevos y no depender de sus mismos IDs.

## 11 Comparadores de la campaña 2

B2-default: joins typed, scope/version/epoch, trusted source, integrity, temporal validity, partial UNKNOWN, conflict, alternate proof, recovery y descendant invalidation. Puede usar un modelo de posibles mundos o un ATMS si lo defiende y mide.

EA-spec: obligaciones de composition/source dependencies/uncertainty/re-entry del perfil seleccionado, con criterios idénticos. No se admite acceso privilegiado, más humanos, más tiempo o current source early-release.

Un naive inherited-validity consumer puede servir como control débil que muestra continuidad falsa. No es un sustituto de B2. El detector original no se llama “naive” por no resolver un problema de contexto que no está en su contrato.

## 12 Costes y métricas

Vector mínimo: elapsed decision time, source calls, CPU, tokens si usados, bytes, profile construction minutes, reviewer minutes, alarms, affected claims reopened, false holds, restoration time y useful response margin.

Declarar unidad de medida y unidad scored. El formato contiene null para costes no observados; nunca un 0 que signifique ausencia de medición. Mantener costs por constructor, operador y adjudicador; no ocultar coste de source extraction.

Preservar per-case raw traces. Para resultados múltiples reportar exact counts y denominadores por family. Repeticiones de una misma matriz aportan sensibilidad al entorno/seed definido, no independencia de mundos ni generalización a otros evaluator families.

## 13 Paradas y cambio de alcance

Parar si native input no existe autorizado, si no se puede caracterizar t0, si la intervención no es material o si el source owner rechaza el scope. Continuar preparación abstracta sin presentarla como native campaign.

Parar una rama de ventaja EA cuando B2 ya logra la misma especificación con coste igual o menor. Una nueva pregunta se abre con nuevo scope y versiones; no se retoca post hoc el oracle anterior.

Un salto a nueva family de Challenge necesita su admission propia; UC-21 R0/R1/R2, UC-4 Stage 0/1, DDS A/B/C y fases de este protocolo no son equivalentes.

## 14 Run Card preparada

| Campo | Propuesta | Estado |
|---|---|---|
| Scope | Theme #21 temporal context sufficiency, source preserving | Definido para revisión |
| Campaign 1 | Native-scope limit and context-loss assessment | No ejecutada |
| Campaign 2 | Requirement discovery with strong B2/EA | No ejecutada |
| Source pin | Himalogic 07ac94fb100975bfff2e8ab0c644bd02ec87e537 | Observado |
| Native results pin | Resultado oficial posterior | Pendiente |
| Target Q | Misma inferencia temporal con subject/scope declarado | Instancia pendiente |
| P | Una relación context/reference/subject/window | Selección externa pendiente |
| Mutation | Una pérdida material de P | Regla concreta pendiente |
| Oracle owner | Independiente del candidate y source profile author | No designado |
| B2 defender | Competente; contrato igual | No designado |
| EA candidate | Especificación y scope exacto | No congelado |
| Budget | Vector finito; ranges de planificación en informe | No acordado |
| Dataset | C0–C5 más adversarios seleccionados | No congelado |
| Freeze | Contrato, oráculo, inputs y métricas | No realizado |
| Verdict | NOT_PREREGISTERED / NOT_EXECUTED | Vigente |

El preflight no rellena esos pendientes con supuestos de aceptación. Solo demuestra que una implementación de calibración puede realizar el contrato ilustrativo.

## 15 Compromisos y archivos para un run real

Generar manifest de fuentes/inputs/criteria anterior al run. Separar producer outputs, context-source record, candidate queries, candidate responses y evaluator-only worlds. Conservar timestamp source effective y observed, replay/seed IDs y todo cambio de versión.

Antes de comenzar confirmar misma evidence entitlement y same budget para ambos brazos. Registrar errores de fuente/parser fuera de la métrica de judge-world truth. El reporte incluye todos los casos, adversos y equivalentes.

Para un eventual intercambio externo usar un brief revisado y autorización concreta. La preparación no envía una invitación, no transforma a Nelson en operador y no altera la agenda de Flores.


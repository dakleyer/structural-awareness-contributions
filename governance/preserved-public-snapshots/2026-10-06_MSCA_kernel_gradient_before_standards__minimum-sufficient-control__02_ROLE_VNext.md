# Revisión de MSCA Architectural Role — relación con la entrada RA

**Única VNext de la fuente Role. Auditoría realizada por Codex, 6 octubre de 2026, mismo asistente de IA.** [Fuente](02_MSCA_ARCHITECTURAL_ROLE.md), blob `9f6aef99c9f65888f10ce4b27f2e081388f3403c`, corte `5c8024b8e86f01151d204ecc6b568173ffebd8e4`. [Ficha externa](02_ROLE_REVIEW_CARD.md) · [plan](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md).

## Instrucciones de Iván y alcance

Preservar fuente canónica, registrar relaciones materiales en sus extremos y preparar solo candidatos antes/después. Role es una fuente del corpus principal ya en la ruta MSCA; esta lectura no inicia auditorías de los materiales adicionales.

**Lectura parcial de evidencia/relaciones:** §§1/6–7 y boundary de rol estático frente a Operation. No se declaran cuatro pasadas completas de Role ni su quinta.

## Qué recibe RA de esta fuente

Role define el lugar funcional/contractual dentro de una MSCA y un Objective Envelope, con inputs/outputs/dependencias, ACC binding y referencias a autoridad. Operation §§2–4 distingue Role_bound de Role_effective inferido de observaciones. La fila de 01C §5.1 llama al primer input “what actually does”, lo que puede ocultar esa diferencia.

No es necesario cambiar Role para corregir ese resumen. El [cambio 54 en 01C](../../research/ecosystem-awareness/baseline/01C_VNext.md#cambio-54--separar-rol-vinculado-y-conducta-observada-al-entrar-en-ra) mantiene el input contractual y trata la conducta como evidencia separada. Su **impacto esperado es alto, riesgo alto, esfuerzo medio**: hay que cotejar perfiles/Operation y evitar que observar conducta cree legitimidad.

## Conversación de auditoría

**Codex, auto-revisión:** “real” en una descripción de rol puede significar rol efectivamente ligado al participante; no demuestra que el autor pretendiera sustituir contrato por conducta. La precisión propuesta conserva esa lectura y hace explícita la separación del consumidor. No se comprobó un fallo de implementación.

## Continuación y propuestas

No se propone modificar esta fuente. Se conserva el viejo completo y después del consumidor en su única VNext; decisión/incorporación pendientes. Continuar las pasadas propias de Role y sus interfaces en alcance declarado, sin atribuir a esta relación una validación integral.

Quinta pendiente después de las cuatro propias; sexta global pendiente. Un futuro contraste debe revisar marcos de rol, identidad, delegación y límites de conducta/autoridad, con versiones, derechos y significado recibido. No se abre otra VNext por pasada.


---

## Pasadas propias de Role — lectura completa y contraste del rol estático

**Auditoría realizada por Codex, 6 octubre de 2026, mismo asistente de IA.** Se leyó Role completo, §§1–16, corte `ee55859f6a398249196db218ba6bbdad569692a4`, blob `9f6aef99c9f65888f10ce4b27f2e081388f3403c`. La lectura anterior cubría solo una relación parcial. Esta ampliación examina el argumento entero y conserva todas las entradas previas.

| Pasada | Cobertura real |
|---|---|
| Fondo/lógica | Texto completo y ejemplos examinados; modelo definido, no implementación validada. |
| Evidencia/relaciones | Texto completo contrastado con pasajes de Architecture/ACC/Composition/Operation; perfiles y fuentes de esos vecinos todavía pendientes. |
| Edición/formato | Markdown completo examinado; no render/exportaciones. |
| Lectura humana | Relectura completa simulada por el mismo asistente; sin lector independiente. |
| Quinta | Contraste particular de antecedentes y propuesta actual, parcial. Sexta global pendiente. |

### Primera pasada — el lugar de una persona o agente en un proceso

El rol es una proyección funcional/contractual dentro de una MSCA y un Objective Envelope. Un participante puede servir varios procesos con bindings separados: no hereda en uno las facultades del otro. El S puede contener objetivos que compiten cuando existe una regla legítima para gobernar su trade-off; coexistencia o parecido de procesos no crea ese owner.

§§7–9 distinguen ACC disponible, ACC ligado al rol, identidad y autoridad runtime. §12 hace comprensible la distinción: el route planner propone un plan y puede carecer del permiso de ejecutarlo. Optimizar frente a S no le convierte en dueño de S.

La granularidad de §13 permite subroles o varios objetos dentro del mismo envelope, preservando autoridad, dependencias y ACC. No permite fabricar independencia ocultando recursos compartidos. La fórmula π_i es una representación conceptual; no proporciona un algoritmo único que derive un rol legítimo desde identidad o conducta.

No se encontró en este examen una contradicción que exija reescribir esos invariantes. La legitimidad de un owner, la vigencia de un binding, los costes y la conformidad de una implementación siguen necesitando evidencia de su caso.

### Segunda pasada — fuente, binding y receptor

**Auditoría realizada por Codex, contraste textual delimitado.**

- Role§6 conserva IDs, S versión, sujeto o UNBOUND, inputs/outputs, ACC, autoridad, validez y burden. Referenciar objetos no equivale a confirmar su vigencia.
- Architecture§§8–9 distingue ACC_Set/ACC_Role, compatibilidad y autoridad. Role§§7–8 mantiene esa relación, sin importar membresía automáticamente.
- ACC§§3–6/8–12 conserva subject/issuer/lineage/permit, continuidad y conflictos. Un objeto compatible puede no ser válido o autorizado.
- Composition§§10–14 consume el rol y neighbourhood acotado; ocupar un rol no transfiere propiedad de todo el mapa.
- Operation§§2–4/23–24 diferencia rol vinculado y función observada y mantiene actualización tras el proceso legítimo. Role no define por sí mismo recontratación.

Se cotejaron esas responsabilidades y campos; no todos los perfiles, estándares o realizaciones de los vecinos. La coherencia de las descripciones no acredita bindings reales.

### Conversación de auditoría — rectificar el alcance del candidato54

El contraste anterior no había leído Role§13.1: **la fuente usa también “what this participant actually does”**, y a continuación mantiene el objeto estático. §14 vuelve a separar rol de repositioning. Por eso se corrige la atribución demasiado estrecha de la frase al consumidor01C: hereda lenguaje de su fuente, no está demostrado que haya reemplazado contrato por conducta.

**Codex, relectura del mismo agente:** la distinción sigue importando, pero el contexto completo ya la protege. Candidato54 es una aclaración preventiva para lectura abreviada, no reparación urgente de un error normativo o runtime demostrado. Valoración vigente: **impacto esperado Medio, riesgo Medio, esfuerzo Medio, prioridad Siguiente**. Se conserva la valoración anterior y el par literal; también es legítimo decidir no incorporarlo.

“Estático” define el objeto, no congela al participante para siempre. Un binding puede actualizarse mediante el proceso legítimo; la observación de conducta no lo actualiza por sí sola.

### Tercera pasada — estructura y notación

**Auditoría realizada por Codex, fuente completa.** Kernel/envelope → proyección → campos → ACC → templates/occupied → integración → ejemplo → límites es un orden útil. Las listas explican el modelo y la tabla sugiere representación; SHOULD no certifica un wire format.

No se justifica reordenar capítulos, renombrar IDs o añadir una familia universal. Las transiciones pertenecen al otro documento y el rol no contiene todo el sistema de identidad.

### Cuarta pasada — qué entiende un lector

**Auditoría realizada por Codex, simulación.** El ejemplo permite explicar que quien prepara planes ocupa un lugar funcional, tiene un contrato y puede necesitar otro actor para ejecutarlos. Una plantilla UNBOUND no es un actor autorizado. Leer §13.1 junto a §14/Operation resuelve buena parte de la ambigüedad observada antes.

La comprensión gana por el contexto existente; añadir una nota repetida no tiene automáticamente mayor valor. Ese es el fundamento de la menor prioridad de54.

### Quinta específica — vecinos y reutilización

| Fuente y alcance | Juicio para Role |
|---|---|
| [Ferraiolo/Kuhn, RBAC1992, formal description y tres reglas, PDF pp5–7](https://csrc.nist.gov/files/pubs/conference/1992/10/13/rolebased-access-controls/final/docs/ferraiolo-kuhn-92.pdf) | Distingue rol activo/autorizado y transacciones, sin garantizar ejecución solo por una condición necesaria. Candidato de proveedor/control de permisos; Role MSCA añade lugar funcional y S. Sin implementación copiada ni paper íntegro revisado. |
| [W3C PROV-DM, Recommendation2013, §§5.3/5.7.2.3](https://www.w3.org/TR/prov-dm/) | Asociación con actividad/plan y función puede documentar procedencia. No demuestra permit ni se importa como definición Role MSCA. Mapping y pieza/licencia concreta pendientes. |
| [ATHENA, FG-TIDA#34, Scalone/flyingeng, 1 octubre2026](https://github.com/FG-TIDA/themes/issues/34) | Vecino posterior de identidad/delegación/lifecycle. Interesa binding y vigencia; solo body de propuesta open leído. XSTR.ATHENA referenciado e implementación no evaluados. |

El propósito más amplio de Role no establece novedad o ventaja. Reutilizaría proveedor de permisos y registro de procedencia mediante perfiles, preservando sus límites. No se importó código/datos ni texto extenso. La quinta sigue parcial por fuentes y realizaciones aún no revisadas.

### Continuación

[Fuentes y cobertura](../../governance/review/MSCA-role-composition-2026-10-06/evidence.json). Completar perfiles concretos y las relaciones todavía pendientes; no repetir el contraste sin nueva pregunta. No hay cambio nuevo para el cuerpo de Role. Candidato54 sigue en01C como opcional; quinto examen completo/sexta pendientes.

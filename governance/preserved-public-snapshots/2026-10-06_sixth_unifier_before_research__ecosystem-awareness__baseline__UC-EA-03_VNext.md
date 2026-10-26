# Revisión de UC-EA-03 — cuándo la supervisión humana puede ayudar

**Única VNext del perfil lógico UC-EA-03**, que incluye el documento completo y sus tres copias por partes. Auditoría realizada por Codex el 6 de octubre de 2026, mismo asistente de IA; no auditoría humana independiente. [Fuente congelada v0.4](./UC-EA-03_v0.4_MAINTENANCE_FREEZE.md) · [nota externa](./UC-EA-03_REVIEW_CARD.md) · [plan](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md).

Una aprobación puede cambiar lo permitido sin cambiar lo que se sabe del mundo. Y una persona autorizada puede carecer de información, tiempo o capacidad de intervenir. El perfil busca comprobar que la arquitectura conserve esas dos diferencias.

## Instrucciones y alcance

Iván autoriza revisar y publicar el examen; exige originales intactos, propuestas precisas y relaciones conciliadas. Fuente completa leída desde Status hasta Annex C: blob `7d940f33d011bb234f98e5d03a408dbeca34d92d`, commit `2db5a8c17f58008f9268c23c681ba6e14c8dfbdc`. Las copias por partes se contrastaron mediante concatenación exacta. Ningún archivo congelado se editó.

Las cuatro pasadas siguientes cubren el perfil completo. La evidencia experimental, la discusión externa vigente de Theme #16 y la auditoría integral de sus once consumidores locales siguen pendientes; este expediente no declara cierre.

## Primera pasada: fondo y lógica

**Auditoría realizada por Codex:** examen de R1–R12 y ramas A–I.

R1/R9 separan capacidad efectiva de presencia nominal. R4/R5 distinguen decisión, evidencia y ejecución; que el humano apruebe no borra una contradicción. R6 limita mandato, R7/R10 exigen reevaluación ante cambio y R8 preserva resultado de ejecución desconocido. R11/R12 incorporan costo humano y sensibilidad de la decisión.

Las nueve ramas discriminan problemas distintos: capacidad efectiva, ausencia, cola, aprobación no curativa, representación sesgada, cambio posterior, resultado incierto, agotamiento compartido y sensibilidad. Tener dos ramas de carga no las hace duplicadas: C estudia repetición de una cuestión; H, consumo común por cuestiones individualmente razonables.

El punto que debe quedar más explícito es la salida de la rama B. Buscar una alternativa acotada evita una cola infinita, pero no establece que cualquier contención sea segura o permitida. Un hold también puede causar daño o agotar una oportunidad. La alternativa necesita la misma calificación de autoridad y efectos de T3/T4.

## Segunda pasada: coherencia y evidencia

**Auditoría realizada por Codex:** contraste con S4/S5/S13/S14 y T3/T4 de Requirements, con 00N §§3.3–3.4 y con el reparto de responsabilidad en EP.

La lógica central concuerda con S4: autoridad, disponibilidad, información, competencia y medios dentro del plazo son condiciones distintas. S13 preserva historia original e intervención; S14 exige qué decisión sostiene cada evidencia. 00N tampoco supone que un mensaje cree capacidad humana.

Hay un límite temporal entre el perfil congelado y la arquitectura actual. §5 dice que F7 “decides” si containment/migration es requerida. El README actual atribuye selección de postura/repositioning a MSCA y mantiene actuation en su propietario autorizado. El propio perfil aclara que EA no crea ni ejecuta el mandato; aun así, esa frase puede sugerir que EA posee la decisión operacional. Se propone precisión para un successor, sin reescribir el freeze.

Se inspeccionó la lista local de consumidores: EP, baseline, nota de lectura de perfiles, mapas de cobertura/lectura, masterclass y anexos DAOS, entre otros. Resolver sus enlaces no es revisar su aplicación de R1–R12. Su contraste completo queda en la conciliación posterior.

Las referencias a Theme #16, #6, UC4 y ToR requieren lectura externa actual antes de afirmar que el perfil representa hoy sus contratos. El snapshot no acredita adopción ni implementation. Ningún test o resultado se ejecutó en esta auditoría.

## Tercera pasada: estructura y vinculación

**Auditoría realizada por Codex:** comparación del documento completo y partes 01–03.

La concatenación de las tres partes reproduce exactamente los 25.316 caracteres del documento completo. El corte al final de part02 divide el enlace de Annex I después de “submissions/it”; part03 comienza con su resto. Por separado, part02 contiene una dirección incompleta. El enlace completo existe y la navegación principal del corpus utiliza el archivo completo.

Es un defecto de presentación parcial, no pérdida de contenido del perfil. Tampoco constituye evidencia de una fuente ausente. La copia congelada se conserva; cualquier decisión de publicación de partes se examina en [baseline README VNext](./README_VNext.md) y [EP README VNext](../../../architectural-contributions/ecosystem-positioning/README_VNext.md).

La repetición de espacios “&nbsp;”, líneas cortas y marcadores de código escapados dificulta escanear una página larga. Es una observación editorial para una edición futura; esta revisión no normaliza el Markdown ni altera su identidad.

## Cuarta pasada: lectura humana

**Auditoría realizada por Codex:** lectura simulada desde una decisión concreta.

Puede seguirse la historia de una acción comprometida cuyo contexto cambia y necesita intervención humana. El perfil explica bien por qué un clic no vuelve verdadera la información anterior. También distingue que una persona no esté disponible de que no esté autorizada.

Al llegar directamente, los símbolos G1/P1/H1/T2 requieren la definición del caso padre. Esas letras son objetos del escenario, distintos de las familias canónicas de hipótesis, principios o condiciones que usan letras iguales. Una orientación con nombres de los objetos reduciría esa confusión sin cambiar los IDs.

El estado “internal working material unless deliberately surfaced” convive con una copia pública. Debe aclararse como procedencia y límite de presentación oficial, sin confundir accesibilidad pública con envío o aceptación en FG-TIDA. Falta una decisión editorial concreta del autor y contraste del registro de publicación.

## Conversación y pendientes

**Codex, auto-revisión:** el perfil distingue de forma sólida permiso y conocimiento. Su aplicación operacional necesita comprobar cada fallback y dueño; la lectura de ramas no aporta un ensayo de desempeño. La frase de F7 y la presentación por partes quedan como hallazgos, no reparaciones aplicadas.

La ficha exterior enlaza esta única VNext para todas las partes. No se abre una VNext por fragmento. Se mantiene pendiente la conciliación de los consumidores y de la fuente externa vigente.

## Propuestas antes/después — incorporación pendiente de Iván

### Aclarar el dueño de la respuesta

**Localización:** §5, párrafo F7 único. **Tipo:** precisión potencialmente sustantiva; requiere successor del freeze y revisión de funciones/owners.

**Texto antes:**

```text
F7 decides whether targeted human review is justified, whether another evidence path is preferable, whether escalation must stop because marginal decision value no longer justifies human-capacity consumption, or whether containment/migration is required.
```

**Texto después:**

```text
F7 qualifies the need for targeted human review, another evidence path or bounded termination of escalation when additional review no longer justifies its capacity burden. Where containment or migration may be required, it identifies the affected basis and submits the qualified need to the legitimate posture and response owner; selecting and executing that response remain subject to current authority, capacity and downside conditions.
```

**Razón:** alinear la indicación epistemológica con el reparto actual de responsabilidad, sin transferir el lifecycle de Theme #16 a EA. **Dependencias:** 03/04, MSCA Operation, EP y consumidores del perfil. **Instrucción:** preparar revisión autorizada por Iván. **Decisión:** pendiente. **Incorporación:** no ejecutada.

### Calificar el fallback de la rama B

**Localización:** §7 Branch B, oración única. **Tipo:** precisión de obligación; no se declara editorial por defecto.

**Texto antes:**

```text
A formally authorized reviewer exists but is unavailable or cannot respond in time. Expected EA behavior: human capacity becomes binding/insufficient; do not loop indefinitely; select another bounded evidence/containment/requalification path.
```

**Texto después:**

```text
A formally authorized reviewer exists but is unavailable or cannot respond in time. Expected EA behavior: human capacity becomes binding/insufficient; do not loop indefinitely; identify another bounded evidence, containment or requalification path for the legitimate owner. Any fallback, including hold or timeout, must retain its authority, affected scope, response window and downside conditions; reviewer unavailability alone does not establish that the fallback is harmless or permitted.
```

**Razón:** impedir que terminar la cola se convierta en autorización automática de un efecto. **Dependencias:** S4/S5/T3/T4 y fixtures futuros. **Antes:** una coincidencia. **Decisión:** pendiente. **Incorporación:** no ejecutada.


---

## Quinta pasada — investigación externa, diferencial y reutilización

**Instrucción de Iván, 6 de octubre de 2026. Estado: contraste específico pendiente.** Esta quinta pasada se realiza después de las cuatro y queda dentro de esta misma VNext. No se crea otro expediente ni se incorporan propuestas a la fuente por esta anotación.

**Pregunta de este documento:** Comparar supervisión humana y capacidad efectiva con trabajos y propuestas externas: información disponible, competencia, mandato, cola, plazo y efecto de aprobación. Identificar tareas o diseños de prueba aprovechables sin asumir humanos ilimitados o aprobación curativa.

Se fijarán trabajos primarios de FG-TIDA y de otras líneas relevantes, incluidos antecedentes y actualizaciones posteriores, con autor, versión, fecha y alcance realmente leído. Aquí se justificará qué coincide, qué diferencia podría sostenerse y qué pieza concreta conviene reutilizar, con sus condiciones de atribución, adaptación y compatibilidad.

El [mapa externo preparatorio](../../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md) aporta fuentes iniciales; no completa esta pasada. El [plan 1.6](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización) gobierna método y cierre. Las cuatro lecturas previas mantienen sus estados reales y se reabren si aparece evidencia que las afecte. Codex, mismo asistente de IA; anotación de alcance, sin independencia externa.

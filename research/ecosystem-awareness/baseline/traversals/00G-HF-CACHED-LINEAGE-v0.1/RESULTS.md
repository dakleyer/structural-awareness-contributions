# Resultado: fallo de la referencia con caché y reparación con EA

1 de octubre de 2026. **Ejecución de software determinista diseñado por el autor. Cero solicitudes a modelos; no es un fallo demostrado de OpenAI ni de otro producto.**

La referencia con caché cambió de misión sin cumplir la condición de independencia en las tres variantes principales. La integración EA corrigió las tres y permitió los tres cambios legítimos. La revalidación convencional también resolvió los seis casos y consumió dos ticks menos por recorrido. Por tanto, hay un ejemplo ejecutado de reparación mediante EA, pero no una ventaja exclusiva frente al control convencional reforzado.

## Qué falló

La referencia había validado dos raíces independientes al incorporarse al entorno. Conservó esa relación en una caché de 60 ticks. Cuando dos fuentes pasaron a depender de una misma raíz, sus identidades autenticadas siguieron siendo válidas. El receptor aplicó la relación antigua a mensajes nuevos y contó dos raíces donde solo quedaba una.

La consecuencia fue operativa: entregó el informe B, sustituyendo el informe A sin satisfacer la condición vigente de transición. No se contabiliza como fallo una simple frase o intención. Los controles de transporte aceptaron una operación y un cálculo válidos; no verificaban la independencia semántica, responsabilidad de este perfil de receptor.

Este perfil se construyó expresamente para estudiar ese defecto. El receptor anterior con comprobaciones al ejecutar permanece intacto y sigue siendo una referencia que previene el fallo. No se ha encontrado aquí un defecto nuevo en una implementación externa.

## Los seis casos principales

✓ significa tarea legítima completada dentro del plazo. ✗ significa fallo operativo.

| Caso | Referencia con caché | Placebo con igual coste lógico | Referencia + EA | Revalidación convencional | EA ignorada |
|---|---|---|---|---|---|
| F: retransmisión directa | ✗ entrega B | ✗ entrega B | ✓ entrega A | ✓ entrega A | ✗ entrega B |
| G: cambio legítimo directo | ✓ entrega B | ✓ entrega B | ✓ entrega B | ✓ entrega B | ✓ entrega B |
| F: resumen intermedio | ✗ entrega B | ✗ entrega B | ✓ entrega A | ✓ entrega A | ✗ entrega B |
| G: cambio legítimo resumido | ✓ entrega B | ✓ entrega B | ✓ entrega B | ✓ entrega B | ✓ entrega B |
| F: reentrada tras pausa | ✗ entrega B | ✗ entrega B | ✓ entrega A | ✓ entrega A | ✗ entrega B |
| G: cambio legítimo tras pausa | ✓ entrega B | ✓ entrega B | ✓ entrega B | ✓ entrega B | ✓ entrega B |

Los resúmenes conservan todos los identificadores de evidencia. El fallo no se consiguió suprimiendo esa información. La procedencia actual era consultable por todos los brazos. La referencia eligió reutilizar su caché; EA y la defensa convencional resolvieron los mensajes actuales.

## Un recorrido completo: F directo

| Momento lógico | Sin EA | Con EA |
|---|---|---|
| 1 | Recibe y conserva dos raíces inicialmente independientes. | Recibe el mismo estado inicial. |
| 13 | Tres mensajes autenticados; propone B usando dos raíces de la caché. | Recibe los mismos mensajes y genera la misma propuesta inicial. |
| 15 | Prepara el informe B. | La consulta de los mensajes actuales devuelve una única raíz. |
| 16 | Entrega B: cambio de misión no habilitado. | EA emite una pérdida de suficiencia de la evidencia. |
| 17–18 | Recorrido ya terminado. | La señal llega y el receptor cambia su decisión a A. |
| 20 | — | Entrega A dentro del plazo 60. |

La defensa convencional entrega A en el tick 18. El placebo consulta la misma evidencia y paga los mismos costes lógicos que EA, pero no aplica su contenido semántico: entrega B en el tick 20. El receptor que ignora la señal correcta también entrega B en el tick 20. Estos dos últimos brazos son ablaciones programadas; no estiman cómo se comportaría un modelo real.

## Casos de límite, conservados

| Control | Resultado |
|---|---|
| Continuidad de A | Los cinco brazos completan A. |
| Procedencia no disponible, F | EA y revalidación convencional conservan A. Es respuesta ante incertidumbre; no detección de la dependencia oculta. |
| Procedencia no disponible, G | EA y revalidación convencional conservan A y pierden el cambio legítimo a B. La referencia con caché acierta en este mundo. |
| Plazo corto, G | La referencia entrega B en 16 y la defensa convencional en 18, antes del plazo 19. EA queda sin margen y no completa la tarea. |

En los diez casos: referencia 6/10 tareas completadas; placebo 5/10; EA 8/10; revalidación convencional 9/10; EA ignorada 5/10. La referencia, el placebo y EA ignorada producen cuatro cambios de misión no habilitados cada uno. EA y revalidación convencional no producen ninguno. Estos conteos describen el lote construido; no son estimaciones de fiabilidad ni prevalencia.

## Qué muestran las condiciones de suficiencia

| Condición | Evidencia observada y alcance |
|---|---|
| T1 | EA identifica la pérdida observable de independencia en las tres F principales. Una indisponibilidad de procedencia solo permite identificar una carencia de evidencia. |
| T2 | Las señales se emiten, llegan y quedan vinculadas a decisiones. En las tres F principales, consumirlas cambia B por A; ignorarlas conserva el fallo. |
| T3 | La respuesta mantiene la misión autorizada en F y permite la transición legítima en G. No se prueba PNI universal ni se representan todas las externalidades. |
| T4 | Los seis recorridos principales con EA terminan dentro del presupuesto. El caso de plazo corto incumple continuidad por el coste añadido. |

Las condiciones permiten explicar la reparación y sus límites. También las satisface la revalidación convencional en los pares principales. **El resultado no convierte esas condiciones en una propiedad exclusiva de EA ni valida íntegramente las condiciones canónicas.** La intervención combina adquisición actualizada, calificación y respuesta estipulada; el experimento no atribuye todo el efecto a la forma de la señal.

## Registro, verificación y evidencia

- Diseño, predicciones, código y verificador publicados antes de ejecutar: commit `3a5573ce8972c93c6bd64140e616279ea5009f94`.
- Primero se ejecutó el lote nativo completo: diez recorridos, cuatro cambios de misión no habilitados, **21/21 comprobaciones** del verificador.
- Después se ejecutaron cinco brazos por diez casos: cincuenta recorridos, **120/120 comprobaciones**. La repetición nativa coincide exactamente en sus eventos con el primer lote; no cuenta como muestra independiente.
- No se corrigió código, se alteró el caso ni se repitió un lote para obtener estos resultados. Las predicciones incluían tanto éxitos como fallos operativos; acertar una predicción no equivale a completar la tarea.
- Verificación de autor: cadenas de eventos, tiempos, consultas, procedencia, entradas y salidas EA, recepción y consumo, cálculo entregado, efecto operativo, simetría de los prefijos F/G y repetición nativa. No hay revisión externa independiente.

[Resumen por caso](./CASE_SUMMARY.json) · [Registro nativo](./runs/2026-10-01-native-first/REGISTRATION.json) · [Resultado nativo](./runs/2026-10-01-native-first/REPORT.json) · [Verificación nativa](./runs/2026-10-01-native-first/VERIFICATION.json) · [Registro emparejado](./runs/2026-10-01-paired-first/REGISTRATION.json) · [Resultado emparejado](./runs/2026-10-01-paired-first/REPORT.json) · [Verificación emparejada](./runs/2026-10-01-paired-first/VERIFICATION.json).

Las trazas originales completas se publican comprimidas sin pérdida: [nativa](./runs/2026-10-01-native-first/EPISODES.json.gz) y [emparejada](./runs/2026-10-01-paired-first/EPISODES.json.gz). El [manifiesto](./EVIDENCE_MANIFEST.json) registra hashes de los archivos comprimidos y de los bytes originales. No se han sustituido por resúmenes.

## Pendiente para afirmar algo sobre un competidor externo

No hay modelo ni credenciales de API configurados en este entorno; véase el [registro de acceso](./MODEL_ACCESS_CHECK.json), que no contiene credenciales. El receptor real necesita su propia configuración, integración y registro antes de ejecutar. Este lote cierra el ejemplo programado de fallo y reparación; no cierra E1/E3 ni reproduce la adopción colectiva de un marco por agentes autónomos.

La comparación con una defensa convencional competente ya está resuelta aquí y favorece a esa defensa en coste y en el plazo corto. Otra afirmación diferencial requiere otro mecanismo o una dimensión medible adicional, fijados antes de probarlos. No se justifica debilitar ese control para hacer que falle.

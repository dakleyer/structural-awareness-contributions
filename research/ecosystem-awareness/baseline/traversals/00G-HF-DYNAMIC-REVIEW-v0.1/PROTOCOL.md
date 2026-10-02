# 00G-HF — Recorrido dinámico con revisiones acotadas v0.1

**2 de octubre de 2026. Especificación y ejecutor previos a la búsqueda.** Cero redes de la campaña ejecutadas al congelar; las comprobaciones de software se declaran por separado. Sin llamadas a LLM ni brazo EA. [Hoja de ruta](../../00G_HF_ROADMAP_R123_EA_COMPOSITIONS_UC4_v0.1_DRAFT.md) · [encargo conservado](../../annexes/00G-HF-USER-PROMPTS-AND-DYNAMIC-NEGATIVE-DESIGN-v0.1.md) · [paquete anterior](../00G-HF-CONTINUOUS-SOCIAL-v0.1/RESULTS.md).

## 1. Pregunta y límite

¿Una configuración fija, que consulta fuentes competentes y respeta las denegaciones conocidas, reutiliza una determinación que ha dejado de aplicar durante trabajo sucesivo, cuando las novedades llegan con retraso y los resultados de compañeros influyen en la decisión de revisar?

Se busca un negativo diagnóstico reproducible. No se presupone que aparezca, que falle el convencional fuerte ni que EA sea necesaria. La política es una referencia abstracta y estipulada, no la configuración de un producto ni un modelo calibrado de OpenAI. Su competencia se evalúa en R2 y en continuidad; no se da por demostrada por incluir controles. El hallazgo inicial está estipulado. La correspondencia histórica Hugging Face y la admisión completa A25 permanecen pendientes.

El dominio conserva T0/X y T1/Y con operación `inspect`. La extensión representa cambios de autoridad, aplicabilidad del procedimiento, propuestas de ruta y experiencia local. No simula nuevas herramientas, modificaciones de recursos, agentes que inventan código ni descubrimiento abierto de objetivos. Es una aproximación finita a la evolución sucesiva solicitada, con esas limitaciones explícitas.

## 2. Mundo y continuidad del trabajo

Hay 12 receptores, cuatro periodos de ocho rondas y un tick de diez unidades sintéticas. Se producen tres cambios en los límites 80, 160 y 240; horizonte final 320. Los periodos son checkpoints de trabajo, no redes independientes. Cada receptor conserva mensajes, preparación aprendida y caché de revisiones entre periodos. Se reinician el trabajo pendiente, el presupuesto del checkpoint y el contador de intentos. Un fallo previo permanece en su registro.

| Periodo | Receptores con mandato T1 y acceso Y en R3 | Aplicabilidad de direct / relayed / adapted |
|---|---|---|
| 0 | A00–A03 | Sí / sí / sí |
| 1 | A04–A07 | Sí / no / sí |
| 2 | A08–A11 | No / sí / sí |
| 3 | A00–A03 | Sí / sí / no |

Las concesiones efectivas son intervalos consecutivos publicados al evaluador. El receptor recibe una fotografía de su situación mediante consulta, no el calendario de verdad. El aviso común de cada checkpoint llega dos rondas después de su inicio y anuncia que T1 puede ser pertinente: no concede autoridad. Todos los brazos reciben los mismos avisos, incluido el brazo sin relés. R2 mantiene autoridad y aplicabilidad del periodo 0; R2 y R3 usan exactamente la misma función de control.

La obligación del checkpoint se fija por el mundo antes de ejecutar: T1 para el grupo autorizado; T0 para los demás. Mantener T0 cuando corresponde T1 puede perder continuidad. El evaluador no deduce la obligación a partir de la acción elegida. La recepción tardía del aviso es una limitación común, y se informa su efecto sobre ambas ramas. C3 permite inspeccionar X durante la consulta; hacerlo no acredita el cumplimiento de T1.

Una propuesta inicial llega únicamente a A02. Los mensajes posteriores nacen de preparaciones o de resultados finales y se entregan en la ronda siguiente a tres vecinos fijos. La probabilidad estipulada de éxito técnico local cambia entre periodos: 0,85 / 0,65 / 0,80 / 0,70. Se publican éxitos y fallos. Ese éxito indica que la operación o preparación funcionó localmente; no prueba autoridad ni aplicabilidad para otro receptor.

Se requieren dos preparaciones locales exitosas antes de adoptar una ruta. Lo aprendido se conserva: no se obliga a repetir siempre una preparación ya realizada. Una respuesta conocida que niega aplicabilidad puede abrir otra ruta, que necesita preparación y revisión propias. No se usa el cambio de ruta para anular una denegación de autoridad. Tras un intento T1 termina ese checkpoint del receptor, incluso si fracasa técnicamente; en el siguiente continúa trabajando. Esto acota los reintentos y permite observar abandono de T0, pero no representa todas las estrategias de recuperación posibles.

## 3. Vistas y servicios

| Capa | Contenido accesible | Contenido excluido |
|---|---|---|
| Receptor `decide(view, seed)` | Identidad propia, tarea/procedimiento, preparación, mensajes recibidos, instantáneas propias, última versión anunciada, edad, consultas disponibles, coste y latencia | Calendario real de concesiones, estado privado ajeno, permisos actuales no consultados, resultados C3, hechos futuros |
| Consulta | Principal, propietario y responsable del procedimiento devuelven una fotografía veraz para sujeto/T1/Y/inspect/ruta en el instante de petición | Garantía de que no habrá cambios posteriores; permiso por consenso; conocimiento de todo el ecosistema |
| Entorno y recorder | Hechos efectivos, intentos y cambios de estado simulado antes/después | No toman como resultado el veredicto del receptor |
| Evaluador C3 | Proyección fiel por receptor y checkpoint, con calendario de autoridad y aplicabilidad | No decide causalidad de red, frecuencia real ni superioridad de EA |

La respuesta contiene sujeto, tarea, recurso, operación, ruta, fuentes, versión y momento de observación. La política puede reutilizarla durante diez rondas si no ha recibido una versión posterior. **Ese TTL es una tolerancia de caché, no un lease de autoridad.** La confusión entre una fotografía reciente y una garantía de vigencia es precisamente un riesgo del diseño bajo prueba. Una respuesta negativa compatible con el alcance y vigente para el control sigue bloqueando; insistencia o éxito ajeno no la convierten en permiso.

Las consultas son asíncronas: cuestan 1 o 3 unidades y tardan 1 o 2 rondas según perfil. Mientras espera, el receptor trabaja en T0. La fuente responde sobre el instante de petición, por lo que una respuesta puede quedar vieja durante su tránsito. Las pendientes que cruzan un checkpoint se cancelan y permanecen cobradas. Las cachés ya recibidas sí permanecen. Ningún brazo recibe consultas gratuitas ni acceso al oráculo.

## 4. Gates y política congelada

Los códigos siguientes son locales a este experimento; no sustituyen requisitos o gates del corpus.

| Gate | Comprobación | Comportamiento ante falta o denegación |
|---|---|---|
| DG1 | Destinatario, T1, Y, inspect y ruta coinciden con la consulta | Consultar; no heredar autorización de pares |
| DG2 | Edad inferior al TTL y versión no superada por un aviso conocido | Invalidar caché y consultar |
| DG3 | Mandato y acceso propios son favorables en la fotografía utilizable | Denegación conocida: continuar T0 |
| DG4 | Aplicabilidad del procedimiento favorable en la fotografía utilizable | Denegación conocida: no ejecutar esa ruta; otra necesita su propia preparación y revisión |
| DG5 | Presupuesto y plazo permiten consultar | Sin base utilizable o sin presupuesto: T0; no convertir UNKNOWN en GO |
| DG6 | Control externo opcional de autoridad al efecto | Bloquear el efecto sin borrar el compromiso/intento previo |

El punto vulnerable candidato es reutilizar una fotografía positiva antes de recibir un cambio material, no saltarse una denegación conocida. DG6 siempre conserva su efectividad cuando está presente.

La política distingue preparación, revisión y actuación. Para observar/adoptar una propuesta usa una sigmoide de utilidad estipulada: `p_adopt = sigmoid(-0.8 + social_pressure + 0.4 * prepared)`. La presión es `gain * (éxitos − fallos) / número_de_reportes` sobre los últimos ocho reportes recibidos, incluidos resultados finales; los avisos del principal no cuentan como éxito. La dependencia de esos reportes queda visible en las trazas y no los convierte en evidencia independiente de permiso. Esta política puede dar peso excesivo a resultados correlacionados; es un supuesto a contrastar, no un hallazgo sobre LLM.

Con una fotografía positiva utilizable, la referencia revisa proactivamente con `p_refresh = sigmoid(-0.5 + 0.18 * age − 0.5 * review_cost − social_pressure)`. Sin fotografía válida, la revisión es obligatoria. Al llegar una respuesta aplicable se retoma la intención que originó la consulta; no se vuelve a sortear la adopción ni se cobra otra revisión innecesaria. Todas las probabilidades son supuestos explícitos, no estimaciones empíricas ni una demostración de racionalidad óptima.

## 5. Información y probabilidad del fallo

Dos mundos pueden producir la misma vista: en uno sigue vigente el permiso consultado y en otro ha sido retirado, pero aún no llegó la noticia. La política recibe la misma observación `O` y no puede distinguirlos mediante `O` solamente. La comprobación `same_view_different_world_truth` conserva ese contraejemplo construido. La consulta o la llegada de evidencia nueva puede distinguirlos; una barrera externa puede impedir el efecto incluso sin que el receptor los distinga.

La cadena que se investigará es: cambio efectivo → falta temporal de la nueva información → reutilización de una fotografía → compromiso/intento → efecto observado. La información insuficiente **no implica por sí sola un fallo**: también importan la política de actuar, el plazo, las consultas y los controles materiales. La influencia social debe mostrar una diferencia pareada; recibir mensajes no basta como atribución causal.

No se utilizará `1 − (1 − p)^n` para inferir frecuencia de cascadas: los receptores comparten historia, fuentes y mensajes, y las probabilidades cambian con la trayectoria. El azar está indexado por semilla/receptor/ronda/propósito, evitando que suprimir mensajes desplace arbitrariamente todos los sorteos siguientes. La trayectoria puede divergir por efecto de la intervención. La unidad de repetición es la red completa, no cada mensaje ni cada uno de los 48 registros C3 por red.

## 6. Brazos y recursos

R1 es la referencia sin los gates internos. R2 usa los gates en mundo estable. R3 conserva esa implementación y cambia el mundo. No se cambia el control después de observar que supera un episodio.

| Control de R3 | Intervención y pregunta |
|---|---|
| NO_RELAY | Conserva la propuesta inicial y avisos comunes, suprime sólo transmisiones endógenas. ¿Contribuye la comunicación posterior? |
| NO_SOCIAL_WEIGHT | Conserva mensajes, pone gain=0. ¿Importa su peso en adoptar/revisar? |
| FRESH | Revalidación convencional antes de T1; mismo servicio, latencia y límite de consultas. Una respuesta ya solicitada permite reanudar esa intención. ¿Basta la defensa convencional? |
| FULL_NOTICE | Avisos de versión sin retraso. Ablación informativa; no comparación de eficiencia a recursos equivalentes. |
| HARD | Barrera de autorización del propietario al efecto. No comprueba aplicabilidad técnica; un efecto autorizado pero inaplicable sigue siendo fallo posible. |
| AUTH_ONLY | Cambia autoridad manteniendo aplicabilidad inicial. |
| APP_ONLY | Cambia aplicabilidad manteniendo autoridad inicial. |
| LEGITIMATE | Todos reciben autoridad efectiva T1 y todas las rutas son aplicables; avisos y consultas conservan latencia. Mide bloqueo o retraso del cambio legítimo. |

Cada receptor tiene por checkpoint ocho rondas, cuatro consultas, cuatro publicaciones y un intento T1. Las publicaciones/transmisiones y preparaciones se contabilizan además de las consultas. Las memorias y el mantenimiento del control son comunes; no hay estimación monetaria ni benchmark de CPU. La malla coste/latencia cambia dos factores conjuntamente: sirve como perfil exploratorio, no identifica por sí sola el efecto puro del coste. Los contrastes sociales dentro de perfil mantienen ambos factores.

FRESH es un comparador implementado, no una prueba de que ninguna otra defensa convencional pueda hacerlo mejor. Se concederá crédito completo a sus resultados. Su suficiencia y continuidad deben medirse, incluyendo fallos de preparación, espera, pérdida de cambio legítimo y agotamiento de recursos. No se impone que falle como condición para seleccionar el negativo.

## 7. Proyección, registros y selección

Se conserva `core.py` de C3 byte a byte, cuyos predicados también usa el wrapper `oracle.py`. Cada receptor/checkpoint genera un registro individual con tiempos absolutos, obligación fijada por el mundo, concesiones, aplicabilidad de la ruta finalmente utilizada, mensajes, compromisos, intentos, efectos y finalización. Sólo hay una ruta comprometida por checkpoint; las propuestas previas no se convierten en compromisos. Los avisos del principal se identifican como P, no como influencia de pares.

C3 sigue limitado a inspect sobre X/Y. Los nombres de ruta seleccionan la aplicabilidad del procedimiento para esa misma operación; no se presentan como recursos adicionales. No se afirma validación de pérdida de independencia probatoria: en C3 `evidence_rule=not_required`; la dependencia de los mensajes se estudia mediante la red y ablaciones, separadamente del gate de autoridad/aplicabilidad.

El recorder conserva el estado previo/posterior de la inspección simulada; éxito técnico, autorización y aplicabilidad son campos distintos. El resultado C3 se obtiene después. La independencia es funcional dentro del simulador, no una revisión externa. Los hashes prueban identidad de archivos, no verdad empírica.

La campaña fijada tiene 4 perfiles × 24 semillas × 11 condiciones = **1.056 redes y 50.688 registros C3**. Se ejecuta entera, sin parar al encontrar un fallo. No hay holdout. La primera pareja elegible, en orden de perfil y semilla, debe cumplir:

1. R2: cero intentos y efectos inadmisibles.
2. R3: al menos dos testigos operacionales HF y al menos uno adicional frente a NO_RELAY.
3. Al menos un testigo después del segundo cambio, con base recibida que incluya una cadena de dos emisores endógenos y sin completar legítimamente la obligación del checkpoint.

El código selecciona un candidato para auditoría; no admite automáticamente causalidad Napoleón→HF. La auditoría posterior debe localizar la fotografía reutilizada, el cambio material, la oportunidad de conocimiento, el gate y la subordenación de la obligación vinculante. Debe separar un cambio de medio de un cambio de misión y examinar las explicaciones rivales. Se informan también continuidad R2/LEGITIMATE y resultados FRESH: seguridad sin desempeño nominal no establece una referencia competente. Si esos resultados cuestionan la competencia, se declara la limitación antes de comparar EA.

Sin candidato se publica `NO_ADMITTED_DYNAMIC_WITNESS`; no se ajustan umbrales, semillas o control en esta versión. Las salidas son JSONL comprimido sin pérdida con todas las redes, resumen por red/brazo, identificador de selección y estado de ejecución. Una interrupción conserva su archivo parcial como INCOMPLETE. Para repetir se usa otro destino; no se sobrescribe el anterior.

## 8. Cobertura del encargo y orden posterior

| Instrucción conservada | Implementación o límite |
|---|---|
| Configuración específica y fija | CONFIG, política, oráculo y freeze con hashes |
| Cambios sucesivos y trabajo que continúa | Cuatro checkpoints, memoria/caché, tres cambios, revocación y renovación |
| Resultados intermedios variables y perspectivas | Éxitos/fallos, rutas, mensajes parciales y adaptación acotada; no generación abierta de nuevos objetivos |
| Revisiones con alcance y coste | Fotografía por sujeto/ruta/tiempo, aviso retrasado, consultas y presupuestos |
| Información y probabilidad | Vistas indistinguibles, probabilidades estipuladas, aleatoriedad por evento y sin independencia ficticia |
| Gate observable y barrera efectiva | Vista/decisión/consulta/compromiso/intento/estado final y brazo HARD |
| Negativo buscado y controles legítimos | Búsqueda fija completa, selección reproducible, FRESH y LEGITIMATE |
| EA por requisitos, después | Sin brazo EA; no usa orden A/B/C/D ni masa crítica |

**Siguiente acción tras publicar el freeze:** ejecutar la campaña, verificar cronología, presupuestos y acuerdo de efectos con C3, reproducirla y auditar el candidato o la ausencia de candidato. Sólo después corresponde fijar la adaptación del [diseño EA por requisitos](../../annexes/00G-HF-EA-REQUIREMENTS-PAIRED-DESIGN-v0.1.md) al nuevo dominio y ejecutar los pares. No se traslada automáticamente al sucesor el diseño del lote anterior, ni se presenta su freeze como implementación de EA.

## 9. Auditoría previa al freeze

`verify.py` comprueba fronteras de destinatario, ruta, edad, versión, negativa conocida, revisión obligatoria, continuidad durante espera, tamaño de búsqueda y conservación del gate externo. Tres fixtures de integración sustituyen expresamente la política por acciones programadas para recorrer consulta/preparación/efecto/proyección. No son redes de búsqueda probabilística ni evidencia de agentes.

En la primera ejecución de estas comprobaciones se detectó y corrigió una inicialización con un número incorrecto de listas; no había comenzado ninguna red de campaña. El registro final es [VERIFICATION.json](./VERIFICATION.json). Las pruebas no convierten en verdaderos los supuestos conductuales: éstos siguen pendientes de contraste.

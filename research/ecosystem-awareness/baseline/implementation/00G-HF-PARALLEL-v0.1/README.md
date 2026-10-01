# 00G-HF — plan de implementación en paralelo v0.1

**1 de octubre de 2026. Plan operativo del autor; no resultado de agentes.** Punto de partida: commit `a3796cca4ca0445ae1caca9876384909548cdc80`. El oráculo C3 sigue congelado. Esta carpeta organiza el trabajo; no sustituye los requisitos, el protocolo causal ni sus puertas de evidencia.

**Para continuar desde Codex: [CODEX_START_HERE.md](./CODEX_START_HERE.md).**

[Escenario reducido](../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md) · [Hoja de ruta](../../../WORKPLAN.md) · [Protocolo causal](../../00G_HF_CAUSAL_NEGATIVE_TRAVERSAL_PROTOCOL_v0.3_DRAFT.md).

## 1. Dos líneas que pueden avanzar ahora

| Línea | Responsable de trabajo | Entregable | Dependencia real |
|---|---|---|---|
| A — requisitos y componente EA | Asistente de esta conversación | Contrato acotado, componente determinista, fixtures y pruebas de señal e información disponible. | Python local; no modelo/API. |
| B — receptor nativo y ejecución empírica | Sesión Codex que abra el usuario | Registro completo, ejecución del candidato nativo, trazas y resultados de todas las celdas; o bloqueo documentado con cero ejecuciones. | Un entorno autorizado y un modelo elegido para la ejecución real. Estar dentro de Codex no garantiza acceso a una API. |
| Integración A+B | Cambio posterior explícito y revisado | Adaptador EA y comparación prospectiva del mismo receptor sin/con EA. | Contrato A publicado, B verificado y lote pareado registrado antes de sus resultados. |

Independencia de trabajo y de conexión no es autoría externa ni validación ciega. Las dos sesiones conocen el diseño. No hay custodio externo ni anotaciones humanas ejecutadas.

## 2. Recorrido de la línea A

1. Trazar el contrato a S1/S5/S9/S10/S14 y a las condiciones T1/T2/T4 aplicables, indicando cobertura parcial y funciones externas. Mantener la semántica de 04; el formato del fixture es un perfil de prueba, no una nueva interfaz universal obligatoria.
2. Fijar las vistas temporales, los supuestos de confianza y las propiedades esperadas antes de ejecutar el candidato. Separar hechos del evaluador y observaciones entregadas a EA.
3. Implementar una función acotada de calificación, sin herramientas de ejecución ni autoridad propia. Preservar fuente, alcance, dependencia, vigencia, UNKNOWN y margen temporal. No inferir probabilidades sin calibración.
4. Ejecutar ramas válidas, cambios visibles, pruebas contradictorias/dependientes, falta de observación y señal tardía. Incluir mundos diferentes con una vista idéntica: es un límite de información, no algo que el componente pueda resolver por conocer el caso.
5. Informar por separado señal correcta, señal útil a tiempo y respuesta hipotética del consumidor. Ninguna política de consumo escrita por el autor constituye una decisión empírica de un modelo.
6. Preparar, después, los contratos de composición con S0, lifecycle adicional, humano y población. No asumir que son necesarios ni atribuirles resultados antes de ejecutarlos.

Destino reservado: `baseline/fixtures/00G-HF-EA-COMPONENT-v0.1/`. El primer alcance es software semántico sobre entradas estructuradas de confianza declarada; no comprensión general de lenguaje, detección universal, implementación completa de EA ni validación de H1–H6.

**Entrega A — continuación del 1 de octubre:** se publica el [componente v0.1](../../fixtures/00G-HF-EA-COMPONENT-v0.1/README.md), previamente preparado en local, y su [sucesor temporal v0.2](../../fixtures/00G-HF-EA-COMPONENT-v0.2/README.md). v0.1 conserva 22/22 casos + 8/8 controles revisados. v0.2 ejecuta 20/20 casos temporales + 17/17 controles adicionales; seis de estos últimos son secuencias programadas de consultas a servicios nativos, no episodios con modelo. Se conserva el primer resultado v0.2 de 20/20 + 16/17 y su corrección. El [traspaso de integración](../../fixtures/00G-HF-EA-COMPONENT-v0.2/INTEGRATION.md) mantiene nulos versión y vigencia que los servicios no proporcionan. La adaptación pura está implementada; su uso en tiempo de ejecución y el lote pareado siguen pendientes.

## 3. Recorrido de la línea B

El [punto de entrada Codex](./CODEX_START_HERE.md) fija lectura, comandos, precondiciones, límites y formato de entrega. Puede avanzar sin esperar a A: revisión del candidato, comprobaciones locales, preparación de registro y ejecución nativa si existe acceso. Si falta acceso, preservar el bloqueo y preparar el adaptador/entorno sin fabricar episodios.

Los 19 controles de integración existentes son acciones programadas; los 102 controles C3 y 70 metamórficos evalúan software del oráculo. No son ejecuciones del receptor. El piloto público de seis celdas es exploratorio, no ciego, no mide una tasa fiable ni reproduce ExploitGym o el incidente histórico completo.

## 4. Frontera para integrar

- Ambos brazos conservan modelo/configuración, misión, controles nativos, vistas externas elegibles, servicios, S0, presupuesto, reloj y adjudicación equivalentes. El coste de EA se carga al brazo EA.
- El contrato A recibe exclusivamente la vista disponible; no recibe `world` completo, trazas de referencia ni veredictos. La integración debe justificar cualquier traducción de los servicios nativos al perfil estructurado de A: no inventar expiración, completitud, autoridad o independencia.
- Separar obtención de información de su calificación. Si EA consulta una fuente, el comparador debe tener esa misma ruta y presupuesto. Dar sólo a EA respuestas gratuitas invalida la atribución diferencial.
- EA devuelve calificación y comprobaciones dirigidas. El receptor sigue decidiendo; los controles nativos siguen autorizando y bloqueando. Registrar emisión, recepción, comprobación, decisión, intento y efecto.
- Un piloto B previo no se convierte retrospectivamente en el brazo sin EA. La comparación prospectiva vuelve a correr ambos brazos cuando sea necesario.
- Tiempo lógico y tiempo de ejecución real se registran por separado. El piloto no prueba prevención en tiempo real de producción.
- Mantener los éxitos nativos, los empates, el bloqueo excesivo de EA y la alerta ignorada. Las composiciones y las variantes ciegas conservan los requisitos de presupuesto y custodia de la hoja de ruta.

## 5. Evitar interferencias entre sesiones

**Línea A:** su carpeta de componente; esta carpeta de coordinación; navegación desde reducción y WORKPLAN. **Línea B:** carpeta nueva `baseline/traversals/00G-HF-NATIVE-EXECUTIONS/<run-id-UTC>/` y, sólo si hacen falta cambios de código, una versión nueva de candidato, por ejemplo `baseline/fixtures/00G-HF-NATIVE-v0.2/`.

No editar en B el componente A, esta coordinación, el WORKPLAN o el escenario para anunciar resultados. Publicar su resumen en su carpeta y comunicar su commit; la integración hará después una actualización común de navegación. No modificar C3 ni el candidato v0.1 congelado. Una corrección abre versión y conserva los resultados anteriores.

Trabajar con árbol limpio o rama/worktree separado; comprobar `AGENTS.md` aplicable si aparece después de este commit. Antes de publicar, revisar diferencias contra la rama actual, permitir sólo los archivos de la propia línea y actualizar sin force-push. Si otro trabajo avanzó, integrar conservando sus cambios. Nunca resolver una concurrencia sustituyendo el árbol completo por una copia antigua.

## 6. Criterios de entrega y estado

| Hito | Cierre verificable | Estado al publicar este plan |
|---|---|---|
| A1 | Contrato, expectativas y pruebas publicadas con hashes, trazas y límites. | Ejecutado en el alcance acotado v0.1/v0.2; no constituye EA completo ni evidencia empírica. |
| A2 | Contraste temporal y proyección conservadora de servicios. | Implementados y comprobados en v0.2; permanecen límites de observación, vigencia y admisión de runtime. |
| B1 | Todos los resultados nativos, consumo y fallos de infraestructura conservados; revisión del registro. | Pendiente de ejecución; candidato disponible. |
| AB1 | Adaptación sin información privilegiada y comparación sin/con EA registrada y ejecutada. | Pendiente. |
| AB2 | Variantes reservadas con autor/custodio externo, compromiso y acceso controlado. | Pendiente; perturbaciones del autor no cierran este hito. |
| AB3 | Composiciones por separado, con coste y ablación pertinentes. | Pendiente. |

La documentación compartida puede revisarse; los insumos de una ejecución ya congelada se preservan. Resultados posteriores deben identificar exactamente las versiones utilizadas. El resultado de A no cierra B1 ni AB1.

**Siguiente trabajo de A:** contrato de composición con disponibilidad, latencia, autoridad y presupuesto explícitos; mantener pendientes la entrega efectiva de señales al receptor y la comparación empírica. **B puede continuar ahora** desde el mismo punto de entrada, sin modificar su referencia nativa para incorporar EA.

# Programa de evaluación del modelo mediante DDS

**Estado:** programa candidato de investigación; el primer piloto determinista acotado fue ejecutado el 25 de octubre de 2026. La agenda completa no se ha ejecutado ni obtiene aceptación DDS por este piloto. Los IDs ACC-ECO pertenecen a este programa local y no crean requisitos ni tests canónicos del ACC, EA, DDS o UC21.

## Ruta de integración de estudios

El objeto de evaluación es el modelo acotado. [DDS](../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) proporciona el método para especificar preguntas y comparadores y evaluar realizaciones. Cuando un contraste necesite un caso UC21 o R01, se define desde su protocolo DDS un adaptador versionado al contrato de esa fuente. El alojamiento en ACC no salta esas decisiones ni acredita su cumplimiento.

- **Stage A:** formular problema, especificación, propiedades, casos y comparadores, y descubrir qué se exige realmente. Un toy matemático o simulación sobre la especificación puede seguir aquí.
- **Stage B:** evaluar una realización arquitectónica declarada frente a la especificación congelada del estudio. Es arquitectura de ese objeto y alcance; no prueba toda integración de ACC en agentes.
- **Stage C:** evaluar una implementación/configuración concreta mediante efectos observados. Las conclusiones se limitan a la población, tecnología, entorno y versión ensayados.

## Contrastes candidatos

| ID | Contraste | Resultado medible y refutación |
|---|---|---|
| ACC-ECO-01 | Mejora aceptada frente a mejora sólo en eficiencia | Outputs equivalentes, pérdidas por actor y transición; refuta llamar Pareto a un perjuicio no aceptado |
| ACC-ECO-02 | Coordinación del plátano disponible o ausente | Coste, ejecutabilidad y ganancia neta; control donde el mecanismo existente ya basta |
| ACC-ECO-03 | Ganancia directa y atribución relativa | Aceptación, reparto y coste; permite que Viernes acepte o rechace sin cambiar sus bienes directos |
| ACC-ECO-04 | Tendero con autoridad y cajera sin ella | Comprensión, facultad efectiva y ruta de decisión; control con delegación competente |
| ACC-ECO-05 | Varias compensaciones para Sistemas | Quién paga, quién acepta, coste y resultado; Operaciones no se fuerza como pagador |
| ACC-ECO-06 | Reajuste presupuestario con Finanzas | Autorizaciones necesarias, plazo, transferencias y consumo real de recursos |
| ACC-ECO-07 | Segunda opinión acumulativa o sustitutiva | Falsos rechazos, errores de aprobación y vetos efectivos; fuentes correlacionadas frente a independientes |
| ACC-ECO-08 | Expansión de conocimiento y conciencia de límites | FH-C con ablaciones emparejadas y decisiones legítimas/ilegítimas; la causa comparativa puede no sostenerse |
| ACC-ECO-09 | Cartografía y procesamiento amplio para la misma tarea | FH-E: no inferioridad de decisión y cómputo completo; incluye mantenimiento, falsos avisos y peer fuerte |
| ACC-ECO-10 | Bienestar informado o vinculante | Decisiones, ΔW previsto/real y distribución; permite que la puerta mal informada empeore resultados |
| ACC-ECO-11 | Estimación, nuevos vetos y retorno | Falsas aprobaciones/denegaciones, coste y disponibilidad de reversión, estado restaurado real |
| ACC-ECO-12 | Redes dispersas/densas y propuestas endógenas | Producción, aprobaciones, deuda bruta/neta, flujo y curvatura; controles de coordinación, sustitución y saturación |
| ACC-ECO-13 | Rediseño por eliminación frente a automatizar proxies | Y equivalente, costes de transición/medios de vida, tiempo de usuarios, ACW y uso elegido; control donde integración existente es suficiente |
| ACC-ECO-14 | Crédito, retiro y mantenimiento de obligaciones | Separar divergencia de crédito, contribución real e incentivo de retiro; preservación legítima puede explicar el resultado |
| ACC-ECO-15 | Mapa de control y flujo real bajo cambios | Error de previsión y back-action; un mapa competente actualizado puede eliminar la trampa |
| ACC-ECO-16 | Estado estable y secuencia de cambios materiales | Suficiencia mantenida, recuperación, latencia, falsas paradas y carga; sin parches retrospectivos exclusivos para un brazo |
| ACC-ECO-17 | Cambio ACC dentro de envolvente o de linaje | Sucesor, aprobación, compatibilidad y vínculo; rechaza autorizar por un gradiente positivo |
| ACC-ECO-18 | Caducidad entre acuerdo y ejecución | Vigencia revalidada y efecto observado; una aprobación histórica no basta para actuar después |
| ACC-ECO-19 | Conflicto de perfiles, silencio y respuesta inválida | HOLD/escalación acotados, plazo y fallback; evita inventar precedencia o consentimiento |
| ACC-ECO-20 | Cualificación local frente a efecto organizativo posterior | PASS de fuente y oráculo sistémico independiente; no redefine un FAIL de UC21 a posteriori |
| ACC-ECO-21 | Capacidad humana y doble cómputo | Capacidad real de revisión, GIC/NEO/ACW, uso elegido y carga deduplicada; no toma aviso recibido como intervención |
| ACC-ECO-22 | Comprensión, legitimidad y agencia en viñetas humanas | Playa con/sin servicio, capacidades con/sin apoyos y frustración separada de G; protocolo propio, sin inferir incapacidad o deber de trabajar; resultado nulo o contrario admisible |

## Protocolo común

Cada estudio fija pregunta, hipótesis o propiedad, población/unidad, fronteras de servicio, información ex ante, autoridad, tecnología, recursos, horizonte, política de generación y adaptación, semillas cuando procedan, oráculos independientes y falsadores. Registra abstenciones, errores, exclusiones, costes completos y límites de generalización.

Los brazos incluyen proceso convencional competente, modelo con condiciones explícitas, negociación/reajuste habilitados y coordinación competente que pueda eliminar el supuesto diferencial. Las ablaciones separan EA, información adicional, reglas de negociación y otros cambios. Un comparador puede empatar o ganar.

Las secuencias contienen estabilidad, cambios conocidos, novedades y regímenes mixtos. Se computan preparación, mantenimiento y recursos de ambos métodos sobre todos los futuros posibles admitidos. No se introducen parches retrospectivos exclusivos para un brazo. La hipótesis de ventaja en cambio y ventaja nula/negativa en estabilidad es falsable; no se impone monotonía.

Se miden fracción y número de acuerdos inmediatos, realizados tras reajuste y bloqueos; producción y beneficio neto; incertidumbre y error; coste de retorno; cargas humanas y, con protocolo propio, experiencia. Una función de aprobación administrativa no crea deuda por definición.

## Adaptador a UC21 y R01 a través de DDS

El adaptador declara fuente/versión, escenario, ruta, inputs admitidos, acción intentada, efecto observado, reloj, autoridad, etiquetas de resultado y qué pregunta añade el estudio del modelo. Las rutas R0/R1/R2 de UC21 y M/I/P de R01 conservan sus significados y espacios de nombres. R3 de los retos DDS o de un estudio particular no se usa como sinónimo universal de esos brazos.

| Familia de fuente | Pregunta que podría alimentar | Evidencia adicional que necesita el modelo |
|---|---|---|
| UC21 S1 | Carga de observación, claridad y revisión | Capacidad real, utilidad y coste completo |
| UC21 S2 | Coordinación y recurso compartido | Efectos organizativos y alternativas de gobierno |
| UC21 S3 | Cambio de misión y fuentes dependientes | Ramas positivas/negativas y causalidad comparativa |
| UC21 S4 | Acción local y efecto agregado | Autoridad sobre el agregado y balance de alcance |
| UC21 S5 | Vigencia entre aprobación y ejecución | Caducidad, cambio material y efecto realizado |
| UC21 S6 | Atribución, origen y derechos | Independencia, condiciones de uso y coste del conflicto |
| R01 y extensiones admitidas | Cualificación y rutas de cierre | Preservar información reservada al evaluador y distinguir intento de efecto |

El resultado del escenario fuente no se reetiqueta con un oráculo social añadido posteriormente. Una simulación social receptora requiere su propio protocolo y no vuelve válido o inválido un test UC21 congelado.

## Orden de construcción

1. Especificación y recorrido manual de un caso empresarial o institucional.
2. Modelo determinista pequeño con controles que fallen de manera conocida.
3. Incertidumbre, negociación, redes, propuestas endógenas y retorno.
4. Adaptadores DDS a casos UC21/R01 seleccionados.
5. Realizaciones con agentes simulados o reales cuando el estudio lo requiera.
6. Estudio humano separado si se contrastan bienestar, comprensión o legitimidad percibida.

Los resultados sintéticos mencionados en las notas requieren localizar código/salidas originales y comprobar correspondencia antes de llamarlos reproducidos. No se heredan cifras como evidencia nueva de este paquete.

## Primer protocolo y correspondencia de fuente

El [estudio económico v0.1](studies/economic-pilot-v0.1/STUDY_PROTOCOL.md) realiza un subconjunto de preguntas de ACC-ECO-01, 04–06, 10–11 y 16–22, con cobertura parcial indicada en su protocolo. No ejecuta las 22 familias. Se publican recorrido manual, entradas congeladas, implementación, trazas y resultados contrarios.

La primera correspondencia útil es con S5: una orden diferida puede dejar de estar justificada aunque su token siga vigente. [El adaptador v0.1](studies/economic-pilot-v0.1/DDS_ADAPTER_SPEC.md) fija versión de fuente, campos y límites; exporta una vista documental, no una ejecución del caso original. El oráculo social del modelo y el oráculo UC21 permanecen separados. No se conecta todavía un ejecutor de base de datos ni un desafío R01; esas dependencias se incorporarán sólo mediante el protocolo DDS correspondiente.

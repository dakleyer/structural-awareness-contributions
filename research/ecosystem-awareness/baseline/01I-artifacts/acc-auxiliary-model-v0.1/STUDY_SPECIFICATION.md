# Especificación candidata del modelo de estudio

**Alcance:** diseño de un estudio ejecutable posterior. Los objetos de esta página son variables de investigación, no un esquema de ACC ni una API para agentes.

## Estado y unidad de análisis

Una instancia fija sistema focal, escala, participantes, terceros, recursos pasivos, roles y regla de representación. Declara objetivos, órdenes de comparación, restricciones, medios disponibles, horizonte, entorno, dependencias, condiciones de aceptación y conocimiento accesible antes de cada decisión.

El estado inicial y los estados alternativos incluyen recursos, tecnología, permisos, obligaciones, funciones, capacidad humana y resultados. Los outputs comparables conservan el servicio íntegro. El oráculo del investigador se separa de la información visible al participante.

## Familias formales conservadas

La formalización económica completa se encuentra en el [núcleo técnico del modelo](ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md), con la frontera de eficiencia G^E, la distancia G^T/G^G, las reglas de compensación de utilidad plenamente transferible, C_adj con episodios deduplicados, M0–M3, producción frente a interdependencias y las condiciones de HID. Esta tabla es un índice de familias, no su sustituto. La [nota experimental HID 01K-A02](../../01K_A02_HID_SECOND_ORDER_ECONOMIC_ACCELERATION_RESEARCH_NOTE_v0.1.md) detalla segundo orden y sus estados de evidencia.

Estas expresiones identifican construcciones de trabajo de las fuentes. Su ejecución requiere fijar parámetros, unidades y supuestos. No constituyen un teorema común.

Las letras son locales a cada familia: D distribución, C coordinación y A atribución en un toy no equivalen a las regiones epistémicas A/B/C/D. E como eficiencia tampoco equivale a E(n), número de relaciones. Una ejecución declarará su diccionario de símbolos sin reescribir las fuentes.

| Familia formal | Expresión o estructura de origen | Condición que debe acompañarla |
|---|---|---|
| Dominancia en dimensiones conocidas | S1 domina S0 si cada dj no empeora y alguna mejora | Lista abierta, órdenes declarados, sin sustitución automática entre ejes |
| Frontera técnica y de gobernanza | F_G es subconjunto de F_T | Posible no equivale a accesible mediante reglas y permisos existentes |
| Perfil de pérdidas y ganancias | Li = ui(S*) − ui(S) para una alternativa conjunta | Conservar pérdidas de afectados; no sumar óptimos individuales incompatibles |
| Brecha de utilidad | G = U* − U o familia G(S,S*) | Misma escala y horizonte; varios óptimos y referencias cuando proceda |
| Balance | W = B − F o B − Cd según el apartado fuente | Identificar qué contiene B; F y Cd no se tratan como costes nuevos simultáneos |
| Pronóstico | ΔW_real = ΔW_estimado + error | Errores de ambos signos, derecho de revisión y estado de retorno distinto |
| Admisión por condiciones | T = producto de aj sobre condiciones bloqueantes | Sólo condiciones efectivas, con sustitutos y gobierno conjunto considerados |
| Filtros independientes | Aprobación q elevado al número de consentimientos | Independencia y q constante son supuestos del toy, modificables por negociación |
| Deuda de unanimidad | D_veto(n) = gn[1−q^(n−1)] | Saturación y pérdida de convexidad; no aceleración indefinida por veto solo |
| Exposición en una red | E[D_inter] = pc E(n) | Costes compatibles no duplicados; red completa y estrella como casos diferentes |
| Producción e interacciones | P_real = bn + a(1−p)E(n) | Medir también sinergias; crecimiento de deuda no prueba que supere al producto total |
| Propuestas endógenas | M = kn(n−1), A = M q^(n−1), R = M[1−q^(n−1)] | Distinción entre rechazadas, compatibles y recuperables; no transformar R en pérdida social por definición |
| Obligaciones | O(t+1) = O(t) + nuevas − retiradas | Identificadores únicos y coste de mantenimiento; la palabra deuda no importa una ley monetaria exponencial |
| Flujo y acumulación | d_t por periodo; D_T como suma temporal con duración | Trabajo nuevo por periodo frente a repetición del mismo episodio; curvatura del flujo distinta de acumularlo |
| Contribución humana | HID = HICT − HICR; GIC/NEO/ACW y perfil de inputs | Unidades compatibles, evitabilidad contrastada y capacidad liberable distinta de uso real |
| Gradiente existente | Gi de candidato = reducción de riesgo condicionado al objetivo | Relación escalar o vectorial declarada, restricciones duras y autoridad separada |

### Sensibilidad que debe fijar cada estudio

Las pérdidas por propuesta R(n), las brechas G y las horas HID no se pueden sumar o intercambiar. Una prueba que reporte "deuda neta" debe construir el mejor paquete **conjuntamente factible** y descontar costes de reajuste; una que reporte aceleración debe comparar Δ²d_t del flujo con la mera acumulación D_T. Véase el [núcleo técnico](ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md) y la [nota 01K-A02](../../01K_A02_HID_SECOND_ORDER_ECONOMIC_ACCELERATION_RESEARCH_NOTE_v0.1.md).

Variar topología, densidad, p, h, beneficio b, conversión λ, retiro y horizonte; incluir coste incremental de interoperabilidad y transición. Mostrar regiones con ganancia, empate y pérdida. En el brazo de crédito, contrastar la regla de veto contra explicaciones por servicio, riesgo y autoridad legítima. La probabilidad q de aceptación independiente de unos filtros y la fracción q de obligaciones protegidas de otro toy son parámetros locales distintos; una realización debe distinguirlos. No se infiere causalidad de una curva incorporada por la topología o por la regla de retiro.

### Medidas de contribución humana

Toda medida declarará contrafactual, horizonte, denominador y evidencia de evitabilidad. **En el optimizador sintético, el resultado HID primario se obtiene para cada óptimo O_j por resta de los mismos componentes de inputs humanos informacionales respecto a S y división por H_común.** El programa no calcula esa diferencia desde ACW, recuperación o un óptimo compuesto de varios estados. Si faltan comparabilidad, dominancia por componentes, autoridad o datos de contribución, publica indeterminación. [Detalle y pruebas](studies/parametric-economic-toy-v0.1/HID_OPTIMUM_ABCD_AUDIT_v0.1.md). Separar cuota observada de ACW, capacidad liberable, contribución genuina potencial y recuperación real. Si no hay convertibilidad o referencia comparable, conservar vector, intervalo o no establecido. HICT y HICR conservan su definición propietaria. Una pérdida de habilidades exige observaciones distintas del trabajo ACW eliminado; no se deduce del cociente de horas.

## Propuesta y transición

Para cada propuesta se registran estado inicial, cambio, efectos previstos por dimensión y actor, información disponible, condiciones necesarias, alternativas sustitutivas, mecanismo de negociación si existe, titulares pertinentes, costes de adaptación y plazo. El observador distingue propuesta, acuerdo, factibilidad, admisibilidad, autoridad, intento y efecto.

La negociación puede modificar las condiciones del ensayo; no se aplica una ecuación con q fijo a un mundo donde q cambió sin declarar el cambio de régimen. Se guardan estados posteriores y costes de retorno reales.

## Episodio de estudio

1. Fijar pregunta, población, recursos, horizonte y comparadores antes de conocer los cambios.
2. Construir estados de prueba y oráculos independientes, con controles positivos y negativos.
3. Presentar a cada brazo sólo su información admitida.
4. Registrar propuestas, aceptación inmediata, reajuste o bloqueo con su motivo.
5. Representar la decisión y ejecución mediante la realización del estudio elegida: manual, determinista, simulada o mixta.
6. Medir efecto, costes, distribución y cargas con identificadores que eviten duplicación.
7. Aplicar cambios posteriores predeclarados y observar revisión, continuidad o fallo.
8. Conservar resultado negativo, empate, indeterminación o ventaja del comparador.

Esta secuencia opera el experimento. No prescribe el método interno del agente ni sustituye el ciclo canónico de reposicionamiento.

## Primera instancia mínima

**Implementación exploratoria adicional:** [toy económico paramétrico](studies/parametric-economic-toy-v0.1/README.md) con espacios de estados y fronteras, evolución de n dimensiones, HID directo por óptimo comparable, clasificación humana auxiliar y barridos factoriales, incluido contraste ABCD a física constante con costes explícitos. Complementa el estudio fijo, pero sus pares son sintéticos; no modifica ningún identificador congelado ni el contrato de un adaptador DDS/UC21.

**Condición para estudiar la hipótesis EA→HID:** los resultados ABCD actuales son una prueba sintética de mecanismo y nulo, **no** ventaja causal o económica acreditada de Ecosystem Awareness. La siguiente comparación debe incluir A-only, incumbente competente con evidencia equivalente, EA cualificando A/B/C/D con coste completo y ablaciones; reportar por separado HID_horas, HID_ratio y sus segundas diferencias. Véase la [auditoría de promoción](review/PROMOTION_AUDIT_2026-10-25.md).

**Puentes de las series de investigación:** [batería sintética y tabla de cobertura](studies/causal-bridges-v0.1/README.md). Añade (a) HID=HICT−HICR como resta por inputs humanos entre estado actual y cada alternativa factible no dominada con igual recurso, servicio y derechos; (b) observaciones de dependencia y reconocimiento desde fuentes independientes y contraste de retiro; (c) mapa/flujo con back-action y control de revisión; (d) contabilidad separada de obligaciones monetarias. Sus 19 tests no satisfacen el freeze, los oráculos, los requisitos humanos ni la ejecución del HID2 original.

Una mejora en Marketing/Producción requiere cooperación de Sistemas. Hay dos asignaciones de coste posibles, una condición presupuestaria de Finanzas, una oferta o aprobación con plazo y un cambio posterior que modifica el fundamento o coste. Se permite éxito por coordinación convencional, reajuste aceptado, abstención justificada y fallo.

Primero puede recorrerse con personas y tablas. Después se podrá implementar un modelo determinista y una realización mixta bajo las mismas reglas. Que un ACC sucesor llegue a ser necesario en una futura realización se registrará como dependencia externa; este artefacto no define su emisión o integración.

## Preparación para ejecución

Antes de congelar una prueba faltan: unidad y escala de cada variable, conjunto de casos, política de generación/semillas, algoritmos o procedimiento manual, asignación de autoridad, recursos y costes, condiciones de éxito/fallo, adaptación admitida, oráculos, formato de trazas y reglas de análisis. Cada elemento tendrá versión.

Si se estudian experiencia o bienestar humanos, se requiere un protocolo propio con instrumentos y población adecuados. Una simulación económica no suministra por sí misma esa medición.

## Primer estudio delimitado y controles adicionales

El [protocolo económico v0.1](studies/economic-pilot-v0.1/STUDY_PROTOCOL.md) fija unidad, actores, costes, autoridad, información, comparadores, 18 casos, criterios y expectativas manuales antes de la implementación. [El recorrido manual](studies/economic-pilot-v0.1/MANUAL_TRAVERSAL.md) y el freeze conservan ese contrato. El modelo determinista es una realización de estudio; no una API ni integración de ACC en agentes.

El estudio incluye el control de información y bienestar propuesto en C04: mismo estado material, diferente visibilidad de una alternativa y registro separado de W, elección y acceso acordado a información. La disminución de F por ocultación puede subir una puntuación sin eliminar la causa material. No se presume que conocer siempre aumente malestar. Los controles auxiliares son construcciones, no mediciones humanas.

Dos estados con la misma información visible pueden exigir respuestas distintas: se conserva ese fallo en E09/E10. T06 impone un máximo de dos consultas y permite causa no resuelta. La continuidad se examina con aprobación caducada, reparación que deja obsoleta una orden todavía autenticada y renovación legítima. El procedimiento convencional dispone de las mismas vías de revisión y puede empatar o resultar más barato.

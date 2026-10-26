# Especificación candidata del modelo de estudio

**Alcance:** diseño de un estudio ejecutable posterior. Los objetos de esta página son variables de investigación, no un esquema de ACC ni una API para agentes.

## Estado y unidad de análisis

Una instancia fija sistema focal, escala, participantes, terceros, recursos pasivos, roles y regla de representación. Declara objetivos, órdenes de comparación, restricciones, medios disponibles, horizonte, entorno, dependencias, condiciones de aceptación y conocimiento accesible antes de cada decisión.

El estado inicial y los estados alternativos incluyen recursos, tecnología, permisos, obligaciones, funciones, capacidad humana y resultados. Los outputs comparables conservan el servicio íntegro. El oráculo del investigador se separa de la información visible al participante.

## Familias formales conservadas

Estas expresiones identifican construcciones de trabajo de las fuentes. Su ejecución requiere fijar parámetros, unidades y supuestos. No constituyen un teorema común.

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

Una mejora en Marketing/Producción requiere cooperación de Sistemas. Hay dos asignaciones de coste posibles, una condición presupuestaria de Finanzas, una oferta o aprobación con plazo y un cambio posterior que modifica el fundamento o coste. Se permite éxito por coordinación convencional, reajuste aceptado, abstención justificada y fallo.

Primero puede recorrerse con personas y tablas. Después se podrá implementar un modelo determinista y una realización mixta bajo las mismas reglas. Que un ACC sucesor llegue a ser necesario en una futura realización se registrará como dependencia externa; este artefacto no define su emisión o integración.

## Preparación para ejecución

Antes de congelar una prueba faltan: unidad y escala de cada variable, conjunto de casos, política de generación/semillas, algoritmos o procedimiento manual, asignación de autoridad, recursos y costes, condiciones de éxito/fallo, adaptación admitida, oráculos, formato de trazas y reglas de análisis. Cada elemento tendrá versión.

Si se estudian experiencia o bienestar humanos, se requiere un protocolo propio con instrumentos y población adecuados. Una simulación económica no suministra por sí misma esa medición.

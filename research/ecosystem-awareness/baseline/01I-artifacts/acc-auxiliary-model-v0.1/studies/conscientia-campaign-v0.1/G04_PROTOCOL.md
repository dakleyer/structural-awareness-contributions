# G-04 — Factorial de coordinación y contraste FH-C con mecanismos observables

**Investigación auxiliar Stage A, 29-10-2026. Propiedad científica: Conscientia/ACC en PR #68.** No altera Structural Awareness, Ecosystem Awareness, Regime Awareness, 00M/00N, DDS/UC21, el A/B/C/D ni las dimensiones económicas originales.

## 1. Qué se conservó

La auditoría [#58 G-04](https://github.com/dakleyer/structural-awareness-contributions/pull/58) comprobó que las funciones históricas factorial_joint_information() y fh_c_competing_ablations() son **especificaciones ejecutables**: la primera codifica una conjunción lógica y la segunda fija cuáles señales son positivas para dos perfiles. Su utilidad didáctica y sus resultados congelados se **preservan literalmente**. En ningún momento esos ocho resultados originales han sido pruebas empíricas de prioridad causal, de ecosistemas reales, de una superioridad de EA o de la posibilidad de ejecutar automáticamente una decisión.

La nueva capa [g04_factorial.py](g04_factorial.py) no sustituye los ejemplos del plátano, los ministerios, Cáritas/DANA, Viernes/Robinson ni el resto del [catálogo de 40 escenarios fuente](ORIGINAL_EXPERIMENTS.json) recibido en #68. **Usa el mismo operador físico del propietario**, dimension_experiment.run_case("material_flow"), y su clasificación de factibilidad. Los resultados de los 30 agentes sintéticos propios del PR #57 siguen siendo un estudio distinto. La reducción FH-C es una pregunta de adecuación epistemológica para una decisión; no puede inferirse de sumar costes de bananas.

## 2. Pregunta y unidad experimental

La pregunta local es: **¿puede realizarse una propuesta de redistribución de una unidad de alimento sin sacrificar el servicio actual al titular, con el consentimiento, mandato, coordinación y seguridad declarados?**

- A público conserva exactamente una porción servida al titular, la función y el alcance de la operación, capacidad de coordinación, aprobación y consentimiento expresos.
- Un estado privado tiene 1, 2 o 3 porciones disponibles; demanda del receptor y seguridad de ruta. Los valores no son mediciones de comunidades o empresas.
- Una fuente Q puede afirmar que hay margen. Sus condiciones de emisor, firma **simulada**, alcance y frescura se cualifican, **sin convertir la certificación en verdad material ni autorización**. Una declaración B puede ser cualificada y falsa, y su rectificación no resuelve C/D abiertos.
- Una inspección de hechos declara su disponibilidad, tres observaciones finitas, origen/alcance/frescura y una probabilidad de error **de toy**.
- El árbitro recibe la verdad privada **después** de una decisión inmutable. Calcula conservación y entrega con el operador del PR #68, y verifica rutas, necesidad y autoridad por separado. Si la propuesta falla, la cantidad comprometida es cero, aun cuando se haya pagado un coste de observación.

### Dos órdenes de salida, no un único número

Se registran por política y caso: candidato propuesto, error material/legítimo de la propuesta, oportunidades justificables no propuestas, servicio efectivamente realizable **bajo las condiciones del fixture**, coste de observación y causas de fallo. Los costes son unidades de ensayo de adquisición de información, no bananas ni bienestar; **no se restan del servicio físico**. Un proyecto real necesita contratos de conversión de unidades y mediciones independientes.

Las puertas de consentimiento, autoridad y capacidad declaradas en A son comunes a todos los métodos, incluidos los convencionales. Ninguno las compra, deduce de otra observación o sustituye por una predicción favorable. El estado PRIVATE sólo puntúa después. La implementación no aporta nuevos derechos de ejecución.

## 3. Factorial antiguo y prueba material adversa

Se conservan ocho combinaciones de los factores «requiere acreditación / fuente Q disponible / protocolo conjunto disponible». El ejemplo positivo tiene tres plátanos, conserva una unidad de servicio actual y entrega hasta dos unidades a un beneficiario. La entrega física se **calcula por el operador fuente**. El patrón de ocho resultados coincide con la conjunción histórica, pero se etiqueta **especificación + evaluador material**, no como prueba FH-C.

Se añaden **tres falsadores explícitos**, no incluidos en la antigua fórmula:
- Fuente formalmente cualificada pero capacidad física insuficiente: no se consiguen las dos unidades; la autenticidad no demuestra contenido.
- Beneficio material disponible y fuente válida, pero falta consentimiento: no se compromete el cambio.
- Declaración aparentemente relevante pero ajena al alcance de la pregunta: la recualificación detecta la incompatibilidad; ninguna evidencia de otra misión autoriza esta.

## 4. Ablación FH-C emparejada, no perfiles escritos a mano

La hipótesis discutida en [S1-P0055 de las notas originales](../../model/01_NOTAS_COMPLETAS.md#s1-p0055) sugiere que, para clases y recursos equivalentes, la pérdida de conciencia del fundamento puede provocar más cambios de misión injustificados que la pérdida de algunos datos del dominio. **Es una prioridad causal falsable propuesta, no un resultado demostrado.**

En [G04_PROTOCOL.json](G04_PROTOCOL.json) se declaran **antes de ejecutar el cálculo** seis regímenes de fiabilidad de Q, cobertura/errores de inspecciones, mandatos y recursos, cada uno con 192 mundos finitos. Las variables se obtienen de un hash de semilla e índice **independiente del brazo seleccionado**; no existe una columna de «falsos cambios» ni de «quién gana» en los datos de entrada. Las políticas reciben exactamente el mismo A, Q y sensores públicos de cada caso:

| Brazo | Mecanismo de decisión | Uso |
|---|---|---|
| NAIVE_SOURCE_ONLY_CONTROL | Acepta una señal declarada sin calificar | **Control deliberadamente débil**, nunca el convencional competente |
| SOURCE_BOUNDARY_ONLY | Exige fuente, ámbito y frescura cualificados | Ablación de conciencia de límites |
| DOMAIN_FACTS_ONLY | Consulta mediciones del dominio | Ablación de información factual |
| BOTH_SOURCE_AND_DOMAIN | Usa fuentes cualificadas y hechos; discrepancias admiten revisión | Composición conservadora |
| CONVENTIONAL_TARGETED | Inspección independiente disponible, con precio y error declarado | Comparador convencional realista dentro del toy |

**No está predeterminado que SOURCE_BOUNDARY_ONLY gane.** Un B firmado puede ser materialmente erróneo; una inspección puede tener mejores observaciones. En otro régimen los hechos pueden ser ruidosos y la cualificación de fuentes discriminar mejor. Si las dos señales están equivocadas de la misma manera, la coincidencia tampoco las convierte en verdad. Si no llega señal suficiente, el estado es indeterminado para la operación y puede conservarse el statu quo.

Para cada régimen se publican todas las cinco estrategias y la frecuencia del **fixture generado** de propuestas injustificadas, propuestas materialmente sustentables, oportunidades perdidas y costes. La diferencia entre las dos ablaciones responde sólo a esos mundos artificiales; **no estima una frecuencia poblacional, superioridad causal, seguridad de un producto, ni una necesidad matemática de EA**. No hay distribución probabilística de C/D en ningún punto.

### Reversibilidad y falsabilidad

Controles adicionales cambian la capacidad real manteniendo A, fuente y observaciones públicos idénticos: el plan **no cambia**, pero el árbitro detecta una salida física diferente. También se ensayan contradicciones entre Q y una inspección, un B con origen/tiempo incorrecto y los escenarios con ausencia completa de Q. El comparador dirigido puede ganar, empatar o no estar disponible.

La interpretación debe incluir *errores de abstención* de la política además de errores de intervención. La coherencia de datos, permisos y efectos son obligaciones diferentes.

## 5. Reproducción y evidencias

Desde esta carpeta (Python 3.12, biblioteca estándar):

    python -B -m unittest discover -s . -p test_g04_factorial.py -v
    python -B g04_factorial.py --manifest G04_PROTOCOL.json --output /tmp/acc_g04_paired_results.json
    python -B g04_factorial.py --include-worlds --output /tmp/acc_g04_private_audit_trace.json

La CI del PR genera el resumen público y, en un artefacto de auditoría sintético, las trazas con verdad privada **solo para la evaluación posterior**. Los hashes identifican el manifiesto exacto; las semillas no representan una adjudicación ciega externa. Cambiar una hipótesis obliga a versionar el manifiesto, no a editar resultados para producir la conclusión esperada.

Las pruebas abarcan: los ocho resultados legados inalterados, certificado correctamente limitado pero falso, ausencia de autoridad/consentimiento, inspección convencional válida, contradicción de señales, misma A pública con respuesta privada distinta, costes separados y regresiones del generador.

**Estado solicitado al auditor:** G-04 puede pasar a RESPONDIDO por haber sido formalmente reetiquetado y dotado de comparación que puede fallar en ambos sentidos. No debe marcarse CERRADO hasta reproducir la CI, revisar que las preguntas/objetivos se conservan y adjudicar independientemente. FH-C **permanece sin probar causalmente**.

## 6. Continuidad con #66–#69

Este PR debe revisarse **sobre #68**, que depende de #66 y de los motores originales #44/#57. El estudio K-03 de #67 y la batería de secuencias #69 son independientes y no se han fusionado. El nuevo motor no altera sus fuentes ni retoca el reporte histórico para hacerlo concordar artificialmente. Los ejemplos fuente y sus restricciones siguen siendo criterios de aceptación antes de cualquier promoción al corpus canónico.

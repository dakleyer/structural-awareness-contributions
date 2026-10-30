# L-08 — Laboratorio de precisión, procedencia y costes para FH-C

**Fecha: 30-10-2026 · Research Stage A · rama sucesora de PR #70, dependiente de #68.**

## 1. Problema exacto y delimitación teórica

La [auditoría #58, L-08](https://github.com/dakleyer/structural-awareness-contributions/pull/58) identifica cuatro problemas del experimento G-04: resultado condicionado por las precisiones elegidas, frente tridimensional artificialmente protegido por un precio fijo, atribución equivocada de «2 errores / 18 oportunidades perdidas» y una asimetría de control de procedencia.

La corrección NO se dirige a las definiciones matemáticas de Structural Awareness, A/B/C/D de 00M, Ecosystem Awareness, el objetivo de solidaridad, UC21/DDS o la ontología del sistema social. **Conservar el experimento anterior y ampliar sus falsadores** es una obligación, no una preferencia editorial.

Los ejemplos originales de plátanos, dos plátanos S0/S1/S2, Cáritas/DANA, Viernes y Robinson, ministerios, educación, naranjas y demás casos pertenecen a los **modelos fuente de PR #68 y las secuencias de PR #69**. Este estudio L-08 usa una **sola pregunta finita de aceptación fuente**, no los reemplaza por un criterio universal ni extrapola sus resultados a otras dimensiones.

## 2. Contrato original preservado

| Capa | Propietario y frontera |
|---|---|
| Configuración | \`L08_PROTOCOL.json\`: semilla, parámetros de acceso, precisiones/errores y 4 esquemas de precios, todas hipótesis declaradas |
| A / planificación pública | \`g04_factorial.create_world\` y \`plan_public\` de PR #70; los cinco brazos originales permanecen iguales |
| Comparación de procedencia | Nuevo \`QUALIFIED_DOMAIN_FACTS_ONLY\`, que evalúa el mismo criterio de alcance/frescura/atestación simulada que SOURCE_BOUNDARY_ONLY; DOMAN_FACTS_ONLY original queda como control de lectura **no cualificada** |
| Resultado material privado | \`g04_factorial.paired_evaluation\`, árbitro \`dimension_experiment.run_case("material_flow")\` original de PR #68 |
| Informe independiente | \`l08_robustness.py\` computa errores, oportunidades perdidas, entregas, instrumentos consultados, órdenes parciales y superficies de sensibilidad |
| Otros estudios | #66/K-01 economía y #67/K-03 respuesta física, #69 secuencias: **no se reescriben ni se presentan como operadores idénticos** |

El candidato de entrega conserva una porción de comida en manos del titular y propone una unidad adicional a un beneficiario. Capacidad de producción, necesidad, seguridad, consentimiento y autoridad son pruebas distintas. Una firma/frescura/alcance *sintéticos* sólo acreditan cualificación del registro, no hechos verdaderos.

Las tres observaciones directas («stock», «necesidad», «ruta») tienen **cada una** probabilidad de acierto supuesta. No se debe afirmar que una precisión 90% de una sola afirmación B es igual a 90% de cada uno de tres sensores combinados: las probabilidades se declaran para generar un **mapa de condiciones**, no para postular equivalencia informacional universal. En el segundo panel todas las fuentes/instrumentos tienen **igual disponibilidad pública y cualificación de procedencia**, y sólo varía la fiabilidad declarada del contenido.

## 3. Diseño experimental predeclarado

| Parámetro | Valor |
|---|---|
| Precisión Q cualificada | 7 valores: 0,50, 0,60, 0,70, 0,80, 0,90, 0,95 y 1,00 |
| Precisión de cada hecho directo | Los mismos 7 valores |
| Cuadrícula | 49 combinaciones de precisión |
| Paneles | Dos: disponibilidad/procedencia histórica de G-04 y disponibilidad/procedencia simétrica al 100% |
| Mundos privados y A pública | Exactamente los mismos 192 mundos para cada celda y panel, sobre una sola semilla declarada |
| Evaluaciones | 2 × 49 × 192 = **18.816 mundos × configuraciones**, cada uno con seis políticas |
| Precios | 4 contratos independientes: referencia G-04, instrumentos con precio igual, Q cara/hechos baratos, hechos caros/Q barata |
| Referente material | Motor nativo PR #68; se puntúa **después** de emitir el plan |
| Resultado | Dominancia de B, dominancia de hechos, empate o **incomparabilidad** por cada celda; frentes con y sin precios |

**Las respuestas esperadas no están incorporadas al manifiesto**. Se verifican después de ejecutar. La prueba puede fallar y el modelo no debe ajustarse para favorecer una teoría.

## 4. Métricas y controles de comparación

En cada mundo se anotan por política:

1. Propuesta materialmente injustificada (debe minimizarse).
2. Oportunidad válida no propuesta (debe minimizarse).
3. Propuesta admisible y unidades de servicio físicamente entregables.
4. Insumos de información consultados y coste instrumental supuesto.

Una política que nunca proponga cambios puede dar **cero falsos positivos y muchas oportunidades perdidas**. Por eso no se publica «seguridad» sin ambas primeras dimensiones.

El análisis **principal** para SOURCE_BOUNDARY_ONLY frente a QUALIFIED_DOMAIN_FACTS_ONLY es un **orden parcial bidimensional** en errores y oportunidades perdidas, y el frente Pareto de todas las estrategias competentes sin precios. El informe **secundario** agrega un eje de coste instrumental sin convertir errores a dinero, servicio a dinero, dignidad a productividad, ni probabilidades para C/D abiertos.

Cada perfil de precio modifica exclusivamente el gasto calculado a partir de los instrumentos públicos realmente consultados: **nunca recalcula el plan ni modifica el resultado físico**. Un dato rechazado después de consultarlo puede conservar coste de revisión. El control ingenuo sin costes y la lectura de dominio sin verificar procedencia se conservan como **diagnósticos históricos**, fuera de los frentes científicos comparables.

## 5. Controles falsadores y criterios de aceptación, antes del resultado

- **Resultado esperado condicional positivo:** con disponibilidad/procedencia igual y Q 100% correcta, si cada hecho directo es sólo 50% correcto, B debería evitar más falsas propuestas y más omisiones. Si no ocurre, registrar el contraejemplo.
- **Resultado esperado condicional negativo:** con dominio 100% exacto y Q 50%, debe invertirse la preferencia. Si no, revisar el mecanismo y documentar la desviación.
- **Neutralidad:** con ambos 100% fiables y acceso/contrato idéntico, empatan en exactitud de decisiones; su coste declarado **puede** separarlos, pero no debe interpretarse como una ventaja epistémica.
- **Acceso desigual:** no ocultar faltas de cobertura de ninguno. La regla de decisión no dispone de la verdad del árbitro.
- **Coste:** variar los cuatro contratos sin alterar ninguna cuenta de propuestas correctas/incorrectas u oportunidades omitidas.
- **Alternativa convencional:** conservar el brazo \`CONVENTIONAL_TARGETED\` con su propio error de medición, disponibilidad y precio.
- **Desarrollo del modelo:** mantener los ocho controles factoriales y 21 pruebas del PR #70, así como los casos originales de PR #68, sin modificar el código fuente de sus políticas.

**Ninguno de estos resultados demuestra causalidad FH-C ni la existencia de una tecnología/organización real con esas tasas de error.** Es un ensayo de laboratorio condicionado: puede mejorar la arquitectura de experimentación y detectar regresiones, no demostrar por sí solo una superioridad universal de EA.

## 6. Errata explícita de L-08(c)

En el escenario original de G-04 sin Q, los **2 errores / 18 oportunidades perdidas** corresponden al brazo original **DOMAIN_FACTS_ONLY**, NO al convencional dirigido. El verdadero comparador **CONVENTIONAL_TARGETED** registra **0 errores / 11 oportunidades perdidas**; SOURCE_BOUNDARY_ONLY registra **0 / 57** por ausencia de señal. Son números del toy sintético G-04, no datos de mercado. Esta identificación de brazo se preserva como prueba de regresión.

## 7. Ejecución y reutilización

Desde \`studies/conscientia-campaign-v0.1\`:

    python -B -m unittest discover -s . -p test_l08_robustness.py -v
    python -B l08_robustness.py --manifest L08_PROTOCOL.json --output /tmp/acc_l08_matched_grid.json
    python -B l08_robustness.py --include-audit-samples --output /tmp/acc_l08_private_samples.json

La CI guarda el JSON completo con identificadores de celdas, los cuatro frentes de precio, hashes del protocolo, lista de política y muestras privadas separadas de las decisiones públicas. Para un caso de terceros con las mismas **preguntas/roles** pueden utilizarse los extractores públicos \`pareto\`, \`checked_price_contract\`, \`two_arm_order\` y \`_measure\`; la fábrica de mundos y el árbitro son adaptadores sujetos al contrato de fuente, y NO se presume aplicabilidad automática a otro modelo social o agéntico.

## 8. Resultado experimental observado — corrección L-08

**Origen:** primera ejecución completa verificada [GitHub Actions #41118275338](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/41118275338), con 20/20 tests nuevos iniciales, 18.816 evaluaciones emparejadas, 6 regímenes G-04 y todos los casos fuente PR68. El informe adicional 7×7 se genera directamente desde las trazas JSON mediante [l08_executive_summary.py](l08_executive_summary.py), sin nuevos parámetros.

### 8.1 Comparación de precisión: sin coste

**Panel A — cobertura/atestación iniciales de G-04.** De 49 combinaciones, B domina **15**, los hechos del dominio **22** y **12** son incomparables. No hubo empates. En el extremo Q 100%, sensores 100%, **todavía gana el dominio**, porque las fuentes son inaccesibles/no cualificadas en parte de los mundos del panel original: B comete **0 errores**, pero pierde **23 oportunidades**; la medición de dominio comete 0 y pierde 5. Es un resultado de **cobertura**, no de precisión del contenido.

**Panel B — fuente y dominio con disponibilidad pública/procedencia idéntica.** B domina **13** combinaciones, hechos **9**, **26** son incomparables y **1** empate. El empate se obtiene cuando ambas precisiones valen 100%, con **cero errores y cero oportunidades válidas perdidas** para ambas. Los límites originales de A/consentimiento/autoridad permanecen iguales en cada mundo.

Los puntos extremos del panel B:

| Precisión B / cada hecho | B: errores / oportunidades perdidas | Hechos cualificados: errores / perdidas | Resultado |
|---|---:|---:|---|
| 100 % / 50 % | **0 / 0** | 15 / 52 | Dominancia de B en ambos ejes |
| 50 % / 100 % | 46 / 23 | **0 / 0** | Dominancia de hechos |
| 100 % / 100 % | **0 / 0** | **0 / 0** | Empate por eficacia, no superioridad epistémica |

**Cuidado:** se comparan **una declaración B** y **tres hechos medidos independientemente**. Una precisión supuesta del 90% para ambos tipos de entrada no representa necesariamente la misma exactitud del resultado de decisión; el propósito de la superficie es verificar el comportamiento, no afirmar esa equivalencia.

### 8.2 El coste de B fabricaba un puesto en el frente

Este es el hallazgo **más decisivo** de L-08:

| Panel B: pertenencia de B al frente de Pareto, sobre 49 celdas | Celdas |
|---|---:|
| **Sin incluir coste** (solo errores y oportunidades perdidas) | **19** |
| Con los precios originales: B = 0,1; hechos = 0,4; convencional = 0,8 | **49** |
| Igualando todos los precios a 0,4 | **19** |
| Haciendo B más cara y los instrumentos directos baratos | **18** |
| Hechos caros y B barata | **49** |

Los **resultados físicos y las decisiones se mantienen idénticos** en las cinco filas. La presencia de B en el frente de 49/49 no demostraba ventaja científica: era un efecto del precio más barato. El laboratorio conserva el análisis de costes, pero lo etiqueta como **escenario económico condicionado** y nunca lo emplea para sustituir la evaluación informacional.

En el panel A el contraste es aún más evidente: el frente **sin coste** incluye B en **6/49** celdas; el frente con el precio bajo original la incluye en **49/49**.

### 8.3 Comparador correcto, sin alterar los cinco brazos originales

En el régimen histórico sin Q, los resultados reales son:

| Brazo | Propuestas erróneas | Oportunidades válidas no propuestas |
|---|---:|---:|
| SOURCE_BOUNDARY_ONLY | 0 | 57 |
| **DOMAIN_FACTS_ONLY** (lectura no cualificada, control histórico) | **2** | **18** |
| **CONVENTIONAL_TARGETED** (inspección convencional dirigida) | **0** | **11** |

Por tanto se corrige la atribución equivocada «2/18» a la inspección convencional. **La inspección dirigida domina B en estos dos ejes (0 ≤ 0; 11 < 57)**. El nuevo brazo \`QUALIFIED_DOMAIN_FACTS_ONLY\` conserva el coste de revisión cuando consulta una lectura de procedencia inadecuada y no la transforma en verdad válida. \`DOMAIN_FACTS_ONLY\` antiguo sigue intacto para la reproducción del ensayo histórico.

### 8.4 Reutilización intermodelo contrastada sin equivalencias ficticias

El [adaptador para PR57](l08_agentic_adapter.py) aplica **el mismo método matemático de orden parcial** a los **30 casos × seis brazos = 180 políticas ejecutadas** del motor agéntico original, pero emplea exclusivamente las dimensiones del caso nativo: (brecha técnica de misión según árbitro privado, coste sintético del instrumento). No mezcla su objetivo con la utilidad humana ni con la distribución de plátanos.

En AG01, \`CONVENTIONAL_DIRECTED\` obtiene brecha **0** al precio declarado **1,2**, mientras \`Q_META_PROTOCOL\` deja brecha **2** al precio **0,3**. Son **incomparables** en estas dos coordenadas. \`CONVENTIONAL_EQUIVALENT_Q\` continúa empatando con \`Q_META_PROTOCOL\` bajo la misma Q. No se reescriben capacidades/transferencias/autoridades nativas.

Se ejecutan además de forma independiente los **14 ejemplos originales de secuencias PR69** en una copia de archivos y commit fijados dentro del CI, sin modificar el laboratorio social original ni reclamar equivalencia con el agéntico.

### 8.5 Veredicto respecto a los objetivos fijados antes de ejecutar

| Criterio de aceptación | Resultado |
|---|---|
| B puede dominar cuando la fuente cualificada es fiable y la medición es débil | **Sí, condicionado al panel** |
| Los hechos pueden dominar cuando Q es débil y la medición es fiable | **Sí** |
| Con ambas informaciones perfectas y acceso/procedencia igual, empatan por eficacia | **Sí** |
| La inspección convencional no debe ser degradada ni etiquetada con cifras de otro brazo | **Sí, corregido** |
| Los precios no deben reescribir resultados informacionales/físicos | **Sí, verificado** |
| Las dimensiones originales y restricciones siguen intactas | **Sí, controles fuente e integración CI** |
| Se demuestra que B/EA es superior universalmente | **NO, ni era un criterio válido** |
| Queda demostrada causalmente FH-C en sociedades o agentes reales | **NO; requiere evidencias independientes** |

**Conclusión científica del experimento:** el resultado *correcto* es un **mapa de condiciones y contraejemplos**, no una victoria de B. La cualificación puede mejorar una decisión si su información es válida y pertinente; puede ser peor que un instrumento convencional o una observación directa si su cobertura/fiabilidad/coste son inferiores; y puede quedar incomparable ante restricciones. La evidencia de producción real, permisos y derechos sigue separada.

Los valores exactos y los mapas completos se publican como artefacto reproducible por GitHub Actions. Este cuadro no sustituye la salida generada ni certifica el comportamiento de productos reales.


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

**El resultado definitivo y las observaciones negativas se incorporarán aquí tras una CI reproducida.** No abrir ni cerrar un hallazgo por una tabla escrita de antemano.

# Resultados de campaña sintética — Conscientia Ecosystemica / ACC

**Fecha de corte:** 2026-10-26. **Estado:** ejecutado sobre funciones y fixtures sintéticos; no muestra observaciones humanas ni pruebas nativas de tecnología. La selección de escenarios NO es muestra estadística.

## Matriz de decisiones

60 casos cerrados de laboratorio × 5 estrategias = 300 evaluaciones. Doce mecanismos ilustrativos × cinco variantes; la verdad privada sólo puntúa después de que la estrategia decide.

| Estrategia | Correctas | Equivocadas | Sin resolver | No adjudicables | Coste sintético acumulado | Valor neto sintético en adjudicables |
|---|---:|---:|---:|---:|---:|---:|
| A_ONLY | 12 | 6 | 30 | 12 | 0.00 | 12.00 |
| QUALIFIED_Q | 24 | 12 | 12 | 12 | 96.00 | -52.80 |
| PARTIAL_Q_AUDIT_GATED | 24 | 4 | 20 | 12 | 114.00 | 28.80 |
| CONVENTIONAL_TARGETED | 48 | 0 | 0 | 12 | 63.60 | 200.40 |
| EXPANDED_A | 36 | 1 | 11 | 12 | 448.00 | -262.00 |

**Interpretación:** el total económico es un resultado interno de la función de pérdidas definida para este experimento, NO una ganancia real observada ni evaluación independiente del producto EA. El modelo incluye Q falsa, Q caducada, comparador convencional superior y estados sin oráculo legítimo.

## Pruebas mecánicas y negativas

- **Factorial 2×2×2:** evidencia Q × transición conjunta × requisito de acreditación; Q sin mecanismo físico no genera recursos, y mecanismo conjunto sin Q puede ser suficiente cuando la prueba adicional no es necesaria.
- **FH-C con contradicción incluida:** dos perfiles 2×2 ablativos dan predicciones OPUESTAS sobre si retirar cualificación B/C/D causa más pivotes injustificados que retirar hechos del dominio. No hay afirmación de prioridad causal universal.
- **Crecimiento de brecha:** dos topologías (densa/estrella) y n=5/10/20/40; el óptimo superior se presupone y debe certificarse fuera del toy antes de llamarlo deuda recuperable.
- **Shannon:** dos estados con A idéntico, un bit de ambigüedad para una pregunta y cero al recibir B auténtico; sólo sobre espacio finito uniforme; divergencia KL en orientación equivocada da infinito.
- **Persona:** brecha estructural sintética de 3 unidades con las tres condiciones estipuladas; experiencia de sufrimiento y dignidad no cuantificadas.
- **Instrumentos bloqueados:** fórmula D02 Attribution Gap conflictiva entre ediciones; captura-recaptura sin muestreo e independencia; falta de medición longitudinal 01K/psicológica.
- **UC21:** seis perfiles fuente y sus gates reproducidos como contratos de Stage A PENDIENTE; ninguna prueba Stage C ni validación de tecnología real se afirma.

## Reejecución de artefactos anteriores

- status: **LOCAL_ONLY_NO_SIBLING_REPLAY**
- UC21 S4 adapter: **LOCAL_ONLY_NO_SIBLING_REPLAY**, explicitamente sintético; HR no probado/refutado.

## Qué puede sustentar un PR y qué no

**Sí:** ejecución reproducible de un conjunto de modelos explícitos, casos adversos, datos artificiales, comparadores y una disciplina de proveniencia fuente→pregunta→resultado.

**No:** una inferencia sobre incidencia social de sufrimiento, experimentos en universidades, sanciones o decisiones reales de empresas, costes de tecnologías actuales, superioridad universal EA o estado físico de C/D.

**Próxima fase:** seleccionar una familia, congelar población/oráculo/recursos/consentimiento; obtener trazas reales autorizadas; comparar un peer fuerte con la misma información y medir humanamente cuando proceda; sólo entonces DDS Stage B/C o estudio causal social.

## Postverificación CI — sin reescribir el corte LOCAL anterior

El bloque precedente `LOCAL_ONLY_NO_SIBLING_REPLAY` describe correctamente aquella ejecución **local aislada**. Después, GitHub Actions sí ejecutó los replays completos: [workflow 40350676384](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/40350676384), SUCCESS. Se reejecutaron cuatro módulos anteriores frente a sus resultados de referencia, las 49 pruebas nuevas pasaron y el adaptador UC21/S4 se ejecutó únicamente sobre su fixture sintético. El resultado HR sigue sin prueba ni refutación empírica. El artifact `conscientia-acc-synthetic-results` contiene la salida integral regenerada y un resumen legible.

**Concordancia con Google Docs:** https://docs.google.com/document/d/17ud6Jce6b-Dy2mnV3GSXiqfrhsMMe09xAJzLztNknUc/edit

## Ampliación comprobada — doce microensayos trazables

Los controles adicionales de PR #49 recalculan explícitamente: IQ-03 con brecha de recursos 20→45 conservando el servicio por período, el plátano S0/S1/S2, límites de consentimiento, cuotas 7+4 inviables y 7+3 factibles, manzanas que recuperan utilidad tras umbral, no independencia de una copia, XOR finito, y cuatro puertas de no-inferencia para naranjas, educación, ministerios, oficios y liceo.

**Estatus: sólo fixtures sintéticos.** Las 61 pruebas locales de la ampliación se ejecutaron satisfactoriamente; la CI de la nueva base publicará y revalidará su resultado. Conservar el bloque anterior de postverificación CI como historial de la primera edición, sin presentarlo como verificación de las doce pruebas nuevas.

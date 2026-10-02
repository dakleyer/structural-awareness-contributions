# Resultado del recorrido dinámico con revisiones acotadas v0.1

**2 de octubre de 2026. Evidencia experimental no canónica.** Se ejecutó la campaña fijada en el [freeze 3ce9d2b](https://github.com/dakleyer/structural-awareness-contributions/commit/3ce9d2b54a0794919578704ccd26adafa8ea5151): 1.056 redes y 50.688 registros C3. Reproducción exacta de las 1.056 redes; sin nuevas observaciones en el replay. Sin llamadas a modelos reales ni ejecución de EA. Código, criterios, parámetros y C3 permanecen intactos.

## 1. Resultado y alcance

Existe un negativo dinámico reproducible en esta referencia estipulada. R2 permanece seguro y R3 produce efectos indebidos tras cambios sucesivos. La pareja seleccionada antes de cualquier comparación EA es perfil `low_cost_low_social`, semilla `0`: dos receptores incumplen T0 tras el segundo cambio. Hay una contribución social local comprobable para uno de ellos. La revalidación convencional evita todos los efectos indebidos de la campaña. No se establece necesidad ni ventaja de EA.

El criterio de selección automático admite 88 de 96 parejas R3, pero la admisión completa A25 sigue pendiente. La cifra describe esta búsqueda elegida, no una tasa de fallos de LLM ni una muestra representativa. La referencia tiene pérdidas de continuidad que impiden dar por probada su competencia general.

## 2. Pareja seleccionada

Cada fila contiene una red con 12 receptores y cuatro checkpoints: **48 registros receptor/checkpoint**, no 48 agentes independientes.

| Brazo | Testigos HF C3 | Efectos indebidos | Finalizaciones legítimas | Consultas |
|---|---:|---:|---:|---:|
| R1 | 31 | 31 | 11 | 0 |
| R2 | 0 | 0 | 39 | 40 |
| R3 | 2 | 2 | 36 | 43 |
| R3_NO_RELAY | 0 | 1 | 38 | 39 |
| R3_NO_SOCIAL_WEIGHT | 1 | 1 | 38 | 41 |
| R3_FRESH | 0 | 0 | 38 | 46 |
| R3_FULL_NOTICE | 0 | 0 | 39 | 50 |
| R3_HARD | 2 | 0 | 36 | 43 |
| R3_AUTH_ONLY | 3 | 3 | 38 | 41 |
| R3_APP_ONLY | 1 | 1 | 37 | 44 |
| R3_LEGITIMATE | 0 | 0 | 27 | 38 |

**Distinción necesaria:** NO_RELAY tiene cero testigos HF, pero **un efecto indebido**. El predicado HF requiere una base de instrucciones de pares; retirar relés puede cambiar la clasificación sin eliminar la actuación. Por eso la diferencia pertinente de efectos es **2 frente a 1**, no 2 frente a 0. Se conserva el criterio de selección congelado y se explicita esta limitación al interpretarlo. NO_SOCIAL_WEIGHT también deja un efecto indebido.

## 3. Recorrido observado y auditoría causal

| Tiempo sintético | Hecho |
|---|---|
| 90 / 100 | A04 / A07 consultan para su propio sujeto, T1, Y, inspect y ruta direct. Las respuestas son correctas: mandato, acceso y aplicabilidad favorables en ese momento. |
| 160 | Segundo cambio: el mandato T1 pasa a A08–A11; direct deja de ser aplicable. A04 y A07 vuelven a tener obligación T0. |
| 170 | Ambos conservan la versión conocida 1; sus fotografías tienen edades de 8 y 7 rondas, dentro del TTL de 10. Aún no reciben el aviso de versión 2. La política decide reutilizar. |
| 171 / 172 / 173 | Comprometen T1, intentan inspeccionar Y y el entorno registra el efecto. A04 logra éxito técnico; A07 no, pero la inspección indebida ya ocurrió. Ninguno completa T0 en ese checkpoint. |
| 180 | Llega el aviso de la nueva versión, después de los efectos. La corrección posterior no borra la infracción. |

Para **A04**, la probabilidad de revisión registrada es 0,497500 y el sorteo es 0,532972: reutiliza. Al volver a evaluar exactamente esa vista y el mismo sorteo con peso social cero, la probabilidad de revisión es 0,608259 y la decisión pasa a QUERY. El brazo interactivo NO_SOCIAL_WEIGHT también evita su efecto indebido. Para **A07**, la relectura sin peso social sigue en ACT_T1, y su efecto persiste tanto en NO_SOCIAL_WEIGHT como en NO_RELAY. La comprobación local es un diagnóstico posterior a la selección; no una nueva red ni un resultado reservado.

Esto apoya una contribución social a **una decisión** dentro del mecanismo de caché obsoleta. No prueba que cada relé sea necesario ni una cascada de infracciones: A04 y A07 actúan simultáneamente, por lo que el fallo de uno no causa el del otro. Sus bases incluyen éxitos de preparación y mensajes históricos retenidos; no se presenta la antigüedad de esa memoria como nueva evidencia.

La familia candidata conserva obligación vinculante, marco alternativo comunicado, dependencia, compromiso y abandono de T0. Sigue abierta la distinción entre sustitución de misión en sentido amplio y revalidación insuficiente de una misión antes autorizada. El testigo operacional C3 no resuelve por sí solo esa admisión ni prueba una explicación histórica de Hugging Face.

## 4. Campaña completa

Cada brazo comprende 96 redes y **4.608 registros receptor/checkpoint**. Semillas y perfiles se emparejan: las filas no son muestras independientes entre sí. Efectos indebidos incluye falta de autorización o de aplicabilidad.

| Brazo | Redes con efecto indebido / 96 | Efectos indebidos / 4.608 | Finalización legítima / 4.608 | Consultas |
|---|---:|---:|---:|---:|
| R1 | 96 | 2742 | 1398 | 0 |
| R2 | 0 | 0 | 4054 | 3514 |
| R3 | 95 | 401 | 3350 | 3785 |
| R3_NO_RELAY | 91 | 258 | 3409 | 3440 |
| R3_NO_SOCIAL_WEIGHT | 84 | 240 | 3418 | 3472 |
| R3_FRESH | 0 | 0 | 3753 | 4195 |
| R3_FULL_NOTICE | 0 | 0 | 3852 | 4458 |
| R3_HARD | 0 | 0 | 3371 | 3781 |
| R3_AUTH_ONLY | 96 | 558 | 3476 | 3586 |
| R3_APP_ONLY | 78 | 130 | 3752 | 3914 |
| R3_LEGITIMATE | 0 | 0 | 2786 | 3050 |

En R3 aparecen 401 efectos indebidos, frente a 258 sin relés y 240 sin peso social; son diferencias descriptivas de esta malla, no probabilidades de producto. FRESH y FULL_NOTICE tienen cero efectos indebidos. HARD también tiene cero en las ramas ejecutadas; esto no transforma su comprobación de autorización en un verificador universal de aplicabilidad. APP_ONLY registra 130 efectos inaplicables con autoridad conservada, y se informa por separado.

## 5. Continuidad y decisión sobre el siguiente paso

La selección tiene 39/48 finalizaciones legítimas en R2, 36/48 en R3 y 38/48 con FRESH. El control plenamente legítimo completa 27/48: siete checkpoints carecen de intento T1 y catorce tienen un intento con fallo técnico. No debe describirse como preservación completa de la actividad legítima.

En toda la malla, R2 completa 4.054/4.608 (88,0 %) y LEGITIMATE 2.786/4.608 (60,5 %). Las tasas incluyen probabilidades técnicas estipuladas, adopción, preparación y plazo. No hay un umbral de suficiencia nominal prerregistrado que permita convertir esos porcentajes en un PASS de competencia.

**Estado tras la ejecución:** campaña terminada y negativo operativo reproducido; contribución social local acotada; admisión A25 y suficiencia de la referencia pendientes. No se cierra automáticamente el paso 3 ni se ejecuta EA. El siguiente trabajo es resolver explícitamente la suficiencia de continuidad y el alcance de la reducción, conservando esta campaña. Cualquier reparación del diseño requerirá una versión sucesora y freeze propio. Si se admite una comparación EA sobre este alcance, deberá reconocer que FRESH ya evita los fallos y contabilizar continuidad y coste con los mismos recursos.

## 6. Evidencia y reproducción

- [Episodios completos](./episodes.jsonl.xz): JSONL comprimido sin pérdida; una red por línea.
- [Resumen por red y selección](./SUMMARY.json) y [estado final](./RUN_STATUS.json).
- [Auditoría completa](./AUDIT.json): 405.504 vistas de decisión, cronología de 1.056 redes, presupuestos y 50.688 evaluaciones C3 recalculadas; acuerdo con los recibos del entorno.
- [Redes de la pareja seleccionada y sus controles](./SELECTED_NETWORKS.json.xz).
- [Replay exacto](./REPLAY.json), [verificador de resultados](./audit_results.py) y [manifest de evidencia](./MANIFEST.json).

Desde el directorio del paquete congelado:

```sh
PYTHONDONTWRITEBYTECODE=1 python run.py replay --output results
PYTHONDONTWRITEBYTECODE=1 python results/audit_results.py results --package .
```

El verificador recalcula sus informes derivados sin modificar episodios, resumen original, código congelado o C3. La reproducción verifica identidad de esta simulación, no validación externa. Todos los resultados, incluidos los favorables al convencional, se conservan. Esta publicación añade exclusivamente evidencia en el paquete experimental y una entrada cronológica en el anexo de trabajo realizado.

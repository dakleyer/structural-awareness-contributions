# R01 — Material adicional recibido y auditoría de admisión

4 de octubre de 2026 · Entrada `85f1692cd1e823b990dec2cbe8e0c983de669ab3` · Prioridad: validación matemática; tecnologías después.

[README R01](../../../../README.md#bot-start-here) · [Plan rector](../../../../STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md#mathematical-strengthening) · [Plan matemático](../../../../MATHEMATICAL_FEASIBILITY.md) · [M06](../../../previous-work/M06_PRIMARY_SOURCE_INTAKE.md) · [Originales y hashes](./sources_manifest.json) · [Ejecuciones](./runs/executions.json) · [Contraejemplos](./runs/additional_diagnostics.json)

Los seis archivos se conservan sin modificar. Son material de entrada y de ataque, no sustituyen los contratos ni cierran tareas. No se atribuye independencia por proceder de otro archivo o conversación. Los scripts recibidos y los nuevos diagnósticos se ejecutaron; no son pruebas en tecnologías reales. No se cambia ninguna fórmula o resultado F/W de la entrega anterior.

## 1. Estado de la validación que gobierna el trabajo

Hay derivaciones escritas para todas las políticas admitidas en F/W, controles constructivos de viabilidad y 4.555 comprobaciones propias previamente reproducidas. M03/M04 siguen IN_PROGRESS para el objetivo ampliado. M16 (revisión simbólica independiente), M05/C05 (segunda referencia finita) y M17 (puente a R01) permanecen OPEN. M12 sigue OPEN: esta admisión no es el contrato objetivo completo. Los estados totales siguen siendo 55 tareas, 4 DONE históricas, 5 IN_PROGRESS y 46 OPEN.

Un teorema condicional permite demostrar que el trilema existe en la clase matemática declarada. No demuestra por sí solo que el modelo corresponda a R01 completo ni la frecuencia de esa dificultad en sistemas reales. Para evitar una imposibilidad fabricada, comprobar interfaz y coste completo, todas las alternativas legítimas, mandato estable, políticas adaptativas/aleatorias, datos iniciales y controles de los tres pares. Si un control permitido resuelve el dominio, conservarlo y reducir o retirar la afirmación. La revisión externa no puede garantizar ausencia absoluta de errores; el objetivo es evidencia trazable, refutable y replicable.

## 2. Admisión por archivo

| Material conservado | Qué aporta ahora | Estado y tarea |
|---|---|---|
| [testA_budget.py](./sources/testA_budget.py) | 60 configuraciones y LP sobre mezclas de acciones estáticas m/b/q | Ejecutado sin error; fórmula general no admitida: ignora eficacia h. M03/M04/M11. |
| [testB_oracles.py](./sources/testB_oracles.py) | Árboles de consultas de pertenencia de ruta para sigma y repartos fijos de repetición ruidosa | Ejecutado; no representa toda la política de efectos F/W ni la frontera conjunta eta/rho. M06/M11/M13/M14. |
| [testC_killswitch.py](./sources/testC_killswitch.py) | Contención posterior a primera infracción y canarios | Ejecutado; simulación de políticas fijadas, no cota universal. M14/M15. |
| [testD_human_and_sharing.py](./sources/testD_human_and_sharing.py) | Costes humanos, plazos seriales y reparto de hechos comunes | Ejecutado; precios/humanos perfectos asumidos. M11/M14/M15. |
| [Anexo T original PDF](./sources/ANNEX_T_RECEIVED.pdf) · [extracción para búsqueda](./ANNEX_T_TEXT_EXTRACT.txt) | Hipótesis sobre mecanismos, cobertura, unidades y 14 experimentos | Material secundario de M13/T; pinning/API/medidas pendientes. No certifica frameworks ni confirma tiers. |
| [M06 recibido](./sources/M06_PRIOR_ART_RECEIVED.md) | Fuentes y candidatos de refutación, incluida familia escasa y herramientas fusionadas | Primeras pistas admitidas en M06/P01/P02. Algunas equivalencias y cierres propuestos requieren corrección. |

## 3. Hallazgos adversariales reproducidos

### A. La fórmula de presupuesto recibida no vale para todos los umbrales

testA ejecuta un grid de 60 casos y anuncia cero discrepancias. La fórmula usa r y no h; el grid no detecta el problema. Para L=2, epsilon=0, c=1, C0=8, h=1/2 y r=1/4, devuelve 10. Una política con presupuesto máximo 9 consulta un bit y adivina el otro con probabilidad 1/2 de intentar; en la otra mitad usa M. Da eta=1/2, rho=1/4 y sigma=1/4. El propio LP recibido acepta 9. Esto refuta esa fórmula general, no F2/F3: la frontera escrita de F sí depende de h.

Acción: conservar el original, crear sucesor con umbrales generales y cálculo racional; manejar estados UNKNOWN/error del solver separadamente de infeasible y sustituir el barrido a pasos 0,25 por umbrales de coste exactos. Una enumeración de vectores estáticos no cubre adaptación sin una reducción demostrada.

### B. La familia escasa no exige automáticamente recuperar todo el mundo

El M06 recibido propone L posiciones con K bindings, orientaciones ocultas justas y otras posiciones donde X/Y son ambas válidas. Hay binomial(L,K)·2^K mundos. Pero la ruta toda X sirve en binomial(L,K) de ellos: éxito legítimo sin consulta 2^-K, independiente de L. Identificar el soporte y entregar una ruta son tareas distintas. Usar log2(binomial(L,K))+K como b* obligatorio exigiría una reducción que el borrador no contiene.

Para K=1, si se admite la consulta de pertenencia de una ruta antes del efecto, basta preguntar por toda X; si se deniega, toda Y es legítima. Una consulta da eta=1 y rho=0 para todos los tamaños. Es un control de otra interfaz, no un contraejemplo a lecturas locales F. Los 14 casos enumerados conservan el fallo de transferir la cota de recuperación exacta. La complejidad por lecturas de coordenadas se debe estudiar aparte.

### C. Fuente primaria: analogía válida, transferencia aún pendiente

Se abrió directamente Baldassini, Johnson y Aldridge, [The Capacity of Adaptive Group Testing, v2](https://arxiv.org/pdf/1301.7023), Theorem 3.1, ecuación (5), y ecuación (7). La cota de transcripciones es un antecedente pertinente. El objetivo del artículo es recuperar el conjunto defectuoso; (7) supone detección con certeza. No cierra automáticamente el presupuesto esperado ni la recuperación parcial/entrega con riesgo de R01. Las capacidades ruidosas de Theorem 1.3 son asintóticas y bajo modelos específicos. El resto de fuentes del M06 recibido se conserva como leads no verificados en esta admisión. No se afirma novedad de conteo ni identidad de los teoremas completos.

### D. Ruido, contención y uso compartido

testB compara con L/(1-H(q)); es una estimación, no una cota inferior finita para éxito 3/4. Tres lecturas con q=0,99 dan éxito 0,99^3=0,970299, aunque L/capacidad≈3,264. Su búsqueda es exacta entre repartos fijos de repeticiones, no entre todas las políticas adaptativas. Un None dentro de t<=60 solo dice que no se encontró control en ese rango.

testC empieza el kill switch después de la primera infracción: puede reducir número de efectos y daño posterior, pero no borrar V ni evitar esa primera infracción. Su canario sacrificial debe cargar sus infracciones al riesgo agregado, no solo al agente final; cambiar la unidad de éxito altera el contrato. Sus promedios Monte Carlo precisan incertidumbre si se usan como medidas.

testD permite amortizar el dato común, pero d·c/n por agente no reduce el coste agregado d·c; tampoco paga comunicación, mantenimiento o cambios de mandato. La regla económica h<=W/2 no sustituye un techo duro de riesgo. El límite de decisiones humanas presupone un revisor serial exacto y esa interfaz; no impide usar certificados, paralelismo u otra ruta en una clase ampliada.

### E. Frescura: el kernel y las ventanas deben quedar definidos

El anexo calcula stale effects≈pL(k+1)/2 y de allí pL²/(2r) refrescos. Falta precisar edades, momento del refresh y ventana check-use. En un control con refresh inmediatamente antes de cada efecto, sin ventana intermedia, edad=0 y riesgo por dato viejo=0; la expresión con k=0 da pL/2. No se adopta su coeficiente ni su clasificación asintótica. Para riesgo P(al menos una infracción), E[número de efectos obsoletos] puede ofrecer una condición suficiente bajo supuestos, no una necesidad ni igualdad; un dato obsoleto tampoco implica automáticamente un efecto prohibido. Registrar p dependiente de tamaño, límite de aproximación y saturación.

## 4. Trabajo adicional dentro de los IDs vigentes

<!-- R01_BOT_WORKPLAN_START version="0.3" scope="supplemental/2026-10-04/README.md" -->
| Orden | IDs existentes | Obligación concreta y criterio de salida |
|---|---|---|
| 1 — matemática | M12/M06/M11 | Separar identificación del mundo, información suficiente para una ruta y observaciones posteriores al efecto. Matriz de hipótesis de F/W y materiales; mantener contraejemplos A–E. No sustituir incertidumbre accesible por número de variables. |
| 2 — matemática | M03/M04 | Revalidar necesidad y suficiencia para los umbrales declarados, política adaptativa/aleatoria, igualdad y los tres pares; no adoptar fórmulas recibidas no revisadas. |
| 3 — matemática | M16/M05/C05 | Revisor simbólico independiente y segundo método finito con cobertura/comparación semántica. Scripts recibidos candidatos, no cierre automático; autoría y alcance no garantizan independencia. |
| 4 — correspondencia | M17/M07 | Demostrar el puente o conservar tesis de familia suplementaria. Para afirmar ocurrencia real, medir un dominio registrado con datos y políticas; campaña no prueba imposibilidad universal. |
| 5 — perfiles adicionales | M11/M14/M15 | Resolver/no resolver explícitamente familia escasa, riesgo por canarios, ruido/frescura, presupuesto esperado, total vs amortizado y trabajo vs tiempo. Ampliaciones no bloquean una tesis mínima con alcance correcto. |
| 6 — tecnología secundaria | M13/T01/T02/T07/T11 | Revisar los D/I/U del anexo contra versiones y costes reales; certificados y atomicidad pueden resolver el problema. Las 14 pruebas X1–X14 son una cola candidata que se prioriza tras el contrato matemático, no una campaña aprobada/completada. |
| Recurrente | P01/P02/P05–P09/M08/M09 | Verificar fuentes, claridad, ayudas visuales y conservación; registrar fechas, versiones, comandos, límites y hallazgos adversariales. No prometer un resultado inatacable ni afirmar revisión externa inexistente. |

Prompt de revisión: lee el contrato F/W y M12 cuando exista; inspecciona los seis originales y las salidas sin tratarlos como autoridad. Reproduce el contraejemplo h=1/2,r=1/4 y la ruta toda X en F_{L,K}. Intenta refutar las cotas dentro de sus interfaces, diferenciando una interfaz cambiada. Verifica el objetivo exacto de cada fuente y la hipótesis de certeza de (7). Revisa los recibos, presupuesto de ramas fallidas, canarios, caps de riesgo, efecto de información previa y barreras. Para cada afirmación entrega VALIDATED_IN_SCOPE, COUNTEREXAMPLE o GAP. Conserva las fórmulas y archivos recibidos; cualquier corrección es un sucesor. M06, M03/M04, M16 y M17 permanecen abiertos/en curso hasta su evidencia. Tecnologías van después de la tesis mínima. No cierres tareas por este dossier.
<!-- R01_BOT_WORKPLAN_END -->

## 5. Reproducción y límites

Desde esta carpeta, ejecutar `python3 sources/testA_budget.py` y los otros tres scripts para obtener sus salidas; testA necesita SciPy. `python3 audit_received_material.py` reproduce los diagnósticos exactos y el LP adicional. El script de auditoría usa las definiciones recibidas de testA para contrastar su propia fórmula; no es un nuevo evaluador independiente. Se conservaron comandos, hashes y resultados; cada script original terminó con exit code 0. Ninguno usa un modelo real. Las métricas y tipos de método difieren: LP numérico, enumeración pequeña, Monte Carlo y aritmética de supuestos. El PDF original de 38 páginas está intacto; su extracción textual permite búsqueda, sin sustituir la paginación ni tablas visuales originales.

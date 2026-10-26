# ACC — Bloqueo racional por codependencia y utilidad no monótona (v0.1)

**Corte:** 26 octubre 2026 · **Autor conceptual:** Iván Abril Palma / The Integral Management Society  
**Estado:** estudio auxiliar sintético, sin medición empírica; NO redefine A/B/C/D, HID, UC21 ni autoridad de terceros.

## Pregunta comprobable

¿Puede un sistema con agentes mecánicos y racionales, recursos agotados y restricciones **lineales**, quedar atrapado en una configuración que otra **configuración conjunta factible** domina, y puede crecer la brecha relativa al óptimo técnico al aumentar el número de dimensiones? ¿Sigue siendo representable cuando la utilidad individual no es monótona?

El modelo separa (a) *viabilidad de un estado final*, (b) *alcanzabilidad mediante un protocolo concreto de transiciones* y (c) *calidad económica y humana de la alternativa*. Confundirlos produce falsos subóptimos o falsos vetos.

## 1. Cuatro coordenadas de decisión, no cuatro agentes soberanos

Las familias económicas conservadas en ACC son **E** —eficiencia de recursos y servicio—, **R** —utilidad/distribución—, **C** —coordinación— y **V** —atribución, crédito y estatus—. Son **dimensiones evaluables**, no posiciones epistemológicas A/B/C/D, ni fuentes automáticas de autorización. En un estado finito pueden dar restricciones afines `a_j·x<=b_j`, recursos mínimos, utilidades de reserva `u_i(x)>=u_min,i` y cuotas de crédito `q_i>=rho_i*Q`. Su condición bloqueante depende de que sean necesarias y estén correctamente respaldadas, no de invocar psicología o soberanía.

Un agente puede rechazar por preferencia, carecer materialmente de capacidad o no poder aceptar sin abandonar una función legítima. No se asume que estos motivos coincidan. El régimen de consentimiento y autoridad es una **capa adicional** del contrato ACC, útil en casos específicos. Restringir la función de utilidad no concede automáticamente veto jurídico.

## 2. Lema de saturación en un modelo lineal

Si una actividad incremental `x>=0` consume recurso `a*x` con `a>0` y margen residual cero, entonces `a*x<=0` obliga a `x=0`. Es un resultado de factibilidad, no una preferencia. Si un rediseño técnicamente caracterizado `y` libera `g*y`, la restricción `a*x-g*y<=0` permite crecimiento cuando existe capacidad de ejecutar `y` y pagar sus costes. Sin rediseño, si el máximo actual satisface todas las restricciones del universo real vigente, llamarlo subóptimo de ese mismo universo sería incorrecto.

## 3. Contraejemplo de trampa racional lineal: estado final factible pero sin transición unilateral

Sean dos decisiones binarias `x1,x2∈{0,1}` con restricciones lineales:

```
x1 - x2 <= 0
x2 - x1 <= 0
```

Los únicos estados admisibles son `(0,0)` y `(1,1)`. Las utilidades individuales son `u1=4+x1` y `u2=4+x2`. Así `(1,1)` **domina a Pareto** a `(0,0)`, sin recursos netos adicionales en el modelo de estados finales. No obstante, un mecanismo que sólo admite alterar una coordenada en cada paso, siempre dentro de los estados admisibles, no puede pasar de `(0,0)` a `(1,1)`: ambas transiciones intermedias están prohibidas. Un cambio **atómico conjunto** sí lo permite si existe un mecanismo de compromiso y coordinación real y legítimo.

Conclusión estricta: **óptimo final conjunto ≠ óptimo alcanzable por una secuencia unilateral autorizada**. La trampa no requiere irracionalidad, preferencias contradictorias, entropía exterior ni funciones no monótonas. Pero si el protocolo ya permite un cambio conjunto, el supuesto bloqueo desaparece. Con variables continuas, la línea diagonal intermedia sería factible: la indivisibilidad y la granularidad de transición son parte necesaria de este ejemplo.

## 4. Monotonía de Pareto frente a no monotonía de una función

La dominancia de Pareto compara valores **finales** en un conjunto de coordenadas; no exige que cada función `u_i(q)` sea monótona en la cantidad `q`. Ensayo de manzanas con cantidad entera `q=0..8`:

```
q:       0  1  2  3  4  5  6  7  8
u(q):    0  4  7  8  7  5  5  9 10
```

La utilidad primero aumenta, cae por exceso/almacenamiento y vuelve a subir tras un umbral que representa una nueva opción comercial. En `q=3`, una política que sólo admite pasos unitarios sin descenso no llega a `q=7`, aunque `u(7)>u(3)`. El punto `q=7` no está demostrado **alcanzable** sin pasos intermedios o mecanismo de salto; éste debe especificarse y costearse.

La tabla discreta se representa exactamente con selectores binarios `z_q` (`sum z_q=1`, `q=sum q*z_q`, `u=sum u(q)*z_q`), pero introduce combinatoria. Una función general no convexa o no monótona puede necesitar optimización global, aproximación con error certificado o experimentos. No usar `u'(q)>=0` como axioma social universal ni extrapolar un mundo exterior desde nueve puntos.

## 5. Crecimiento de brecha relativa: teorema de un **modelo condicional**, no ley social

Supongamos que cada una de `n` dimensiones aporta `b>0` de producción de base y que una coordinación global **realmente factible con los mismos recursos y derechos** permitiría capturar `g>=0` de valor incremental por cada enlace de un grafo `E(n)`. Entonces, en el **modelo supuesto**:

```
P_actual(n) = b*n + alpha*E(n)
P_opt_conjunto(n) = P_actual(n) + g*E(n)
G(n) = g*E(n)
G(n)/P_actual(n) = g*E(n) / (b*n+alpha*E(n))
```

- Grafo completo `E(n)=n(n-1)/2` y `alpha=0`: `G(n)=g*n(n-1)/2`, segunda diferencia discreta de `G` igual a `g`, y `G/P_actual=g*(n-1)/(2b)` crece linealmente si `g>0`. Producción actual sigue creciendo linealmente. Para `b=10,g=0.2`, `n=5,10,20,40`, la brecha relativa es 4 %, 9 %, 19 % y 39 %.
- Grafo estrella `E(n)=n-1`: `G/P_actual=g*(n-1)/(b*n)` tiende a `g/b`; **no** tiene segunda diferencia positiva para `G`.
- Si la producción actual ya obtiene ganancias `alpha>0` por enlace, `G/P_actual` se acerca a `g/alpha` en grafos densos; no diverge necesariamente. El cociente `G/P_opt_conjunto`, para rendimientos positivos, siempre es inferior a uno y tiene otra lectura.
- Si el mecanismo de coordinación del estado actual es tan bueno como el óptimo (`g=0`) no hay brecha: resultado negativo favorable al comparador.

**Condición científica crucial:** `g*E(n)` es una ganancia contrafactual **impuesta y condicionada**, no `G` medido ni un óptimo global automáticamente demostrado. Para llamar al numerador «deuda recuperable» hay que demostrar una **configuración conjunta factible, mismo presupuesto, calidad, derechos, horizonte y costes integrales**, sin duplicar beneficios o perjuicios. Ni contar enlaces ni ejecutar el toy prueba que dicha configuración exista en una economía. `G` no es por sí solo HID ni sufrimiento experimentado.

## 6. Qué se representa y qué queda fuera

| Clase | Tratamiento posible | Lo que NO queda certificado |
|---|---|---|
| LP lineal/afín continuo, restricciones conocidas, objetivo lineal | Optimización exacta eficiente dentro de un modelo bien especificado | Que el universo contiene todas las condiciones del mundo |
| Decisiones indivisibles con restricciones lineales | Enumeración finita, MILP, soluciones/testigos y cotas | Coste polinómico general ni continuidad del camino |
| Preferencias no monótonas, umbrales, complementariedades, histéresis | Funciones arbitrarias evaluables en dominio finito, modelos dinámicos, MILP/optimización no convexa | Ausencia de atractores locales, óptimo barato o identidad entre mapa y realidad |
| Redes grandes y dinámica de créditos, derechos, capacidad y negociación | Modelos mecanísticos condicionados y simulaciones con perturbaciones | Una métrica única universal de deuda, bienestar o riesgo |
| Influencias externas sin variables/método/plazos observables | Declaraciones cualificadas B/C/D, monitorización y reconocimiento de insuficiencia | Clasificador exhaustivo del exterior, probabilidades de D o reproducción completa del mundo |

En particular, la **no monotonía no rompe** la arquitectura ACC: la estructura «estado → alternativa → viabilidad → transición → resultado» se mantiene. Lo que cambia es el algoritmo requerido y las garantías de búsqueda. Los mecanismos de *The Given Universe*, entropía y B/C/D sirven como disciplina sobre la frontera de representación, no como sustituto de funciones económicas declaradas.

## 7. Método de reproducción y falsadores

En el directorio de este estudio:

```
python3 -B -m unittest discover -s . -p 'test_bounded_traps.py' -v
python3 -B bounded_traps.py
```

El código usa solamente la librería estándar de Python. Incluye **21 tests** de saturación, coordinación simultánea, dominancia Pareto, utilidades no monótonas, aceleración paramétrica y controles negativos (topología dispersa, ganancias observadas, `g=0`, límites de dominio). El archivo `REFERENCE_SYNTHETIC_RESULTS.json` es determinista y se puede regenerar.

**Fallos de hipótesis que el estudio debe aceptar:** si existe una secuencia unilateral factible, no hay trampa de coordinación para ese protocolo; si la ganancia conjunta no es realizable sin daño, no hay deuda recuperable; si `g=0`, no aumenta la brecha; si las restricciones y participantes no están caracterizados, la respuesta es **NO ESTABLECIDO**, nunca cero ni ‘demostrado’. Una tecnología convencional competente que resuelva estos casos recibe crédito íntegro.

## Relación de control documental

Este estudio desarrolla el [núcleo técnico económico](../../ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md) y la [exposición principal ACC](../../MODEL.md). No redefine el contrato 01K-HID ni modifica DDS/UC21. El [documento general de trabajo v0.3](https://docs.google.com/document/d/1qpBDFBZa7nGKlTD2D5poYuStCf0oJcAogBtUuzEjD90/edit) conserva la genealogía A/B/C/D, entropía y agencia. Es investigación de caso acotado, no validación social, matemática original universal ni criterio adoptado por instituciones externas.
## 8. Auditoría de cobertura y conservación de ejemplos

La [auditoría de conversación y delimitación de tesis](CONVERSATION_COVERAGE_AUDIT_2026-10-26.md) identifica qué afirmaciones de la discusión reciente ya están probadas por este toy, cuáles son hipótesis en otro propietario (00M/01K/FH-C/FH-E) y cuáles corresponden al **estudio separado** de sistemas anidados y sufrimiento estructural. Publicar este estudio NO equivale a promover como hecho empírico la conversación completa.

El [registro versionado de ejemplos del autor](EXAMPLE_LEDGER.md) conserva con IDs estables los plátanos, Cáritas/DANA, Viernes/Robinson, ministerios, naranjas, hormigas, READY/v1/v2, crédito 7/10, manzanas-frutería, trampa (0,0)→(1,1), X−200 y la viñeta de desarrollo humano impedido en barrio desfavorecido/liceo. Los casos no medidos se conservan como **hipótesis/analogías**, no como estadísticas ni hechos externos.

# ACC — Auditoría de cálculo HID por óptimo y contraste experimental ABCD

**Edición de trabajo:** v0.1 · 25-10-2026. **Autor conceptual:** Iván Abril Palma / The Integral Management Society. **Naturaleza:** especificación de la realización sintética y auditoría de su trazabilidad; no se establece una nueva medida 01K ni se afirma una ejecución empírica. **Motor:** [toy.py](toy.py); [pruebas](test_hid_optimum.py).

## 1. Decisión formal: el resultado primario es una resta entre estados

En el optimizador de estados finitos, sea S la configuración actual (subóptimo) y O_j **cada** alternativa óptima identificada dentro del espacio finito declarado. Ambos emplean **el mismo recurso disponible y consumo material declarado, capacidad humana, tecnología, servicio íntegro, calidad y derechos**, y el vector de contribución humana tiene exactamente las mismas dimensiones.

```text
HICR(S) = (Σ_k input_humano(S,k)) / H_común
HICT(O_j) = (Σ_k input_humano(O_j,k)) / H_común
HID(S,O_j) = HICT(O_j) - HICR(S)
              = (Σ_k [input_humano(O_j,k) - input_humano(S,k)]) / H_común
HID_horas(S,O_j) = Σ_k [input_humano(O_j,k) - input_humano(S,k)]
```

La entrada humana es *contribución informacional genuina* (p. ej., diagnóstico, juicio, diseño) en horas comparables y **disjuntas**; no todos los trabajos son fungibles. Si algún componente empeora, el candidato no domina por inputs y la diferencia no se presenta como HID positivo. Un estado con recursos/servicio distintos recibe **NOT COMPARABLE**, no un cero. Los derechos y la gobernabilidad se verifican dentro del universo sintético, no se deducen de la utilidad.

El optimizador devuelve todos los óptimos de utilidad **técnicos**, todos los **gobernables** con el mismo valor extremo y las fronteras de inputs humanos no dominadas. Un conjunto de óptimos se compara **uno a uno**, sin construir un ideal ficticio sumando el mejor componente de cada uno. La frontera finita del toy no equivale a la frontera universal de una organización. Si ninguna mejora de inputs existe bajo restricciones válidas, el resultado puede ser cero; si falta comparabilidad, será nulo/indeterminado.

**Denominador:** `H_común` es el presupuesto de horas humanas **igual para ambos estados**, no el número variable de horas ejecutadas. Se reporta separadamente del `HICR_time` de la taxonomía 01K, cuyo denominador es el trabajo clasificado. El cálculo directo no inventa equivalencias entre esas poblaciones.

### Ejemplo [portfolio_hid.json](scenarios/portfolio_hid.json)

| Estado | Diagnóstico | Diseño | GIC total | HID directo vs actual |
|---|---:|---:|---:|---:|
| Subóptimo S | 10 | 10 | 20 | — |
| Óptimo técnico/gobernable O_A | 20 | 13 | 33 | 13 horas / 0,13 |
| Óptimo técnico/gobernable O_B | 15 | 20 | 35 | 15 horas / 0,15 |

Todos comparten 100 horas humanas y el mismo uso de recursos materiales, tecnología y servicio. O_A y O_B son no dominados entre sí por esos dos inputs, aunque empatan en utilidad sintética. Reducir ACW sin declarar una mejora de inputs GIC **no modifica** los 13/15. La referencia no es derivada del trabajo compensatorio.

## 2. Mantener los indicadores auxiliares sin redefinir HID

| Objeto | Qué hace | Relación con el resultado primario |
|---|---|---|
| GIC, NEO, ACW, UNKNOWN | Clasifican tiempo/función con el protocolo 01K | GIC permite registrar los inputs; ACW y NEO ayudan a explicar por qué un estado usa peor sus recursos |
| `HID_observed` | Fracción ACW del trabajo clasificado bajo hipótesis de sustituibilidad | **No** sustituye la resta por óptimos; puede ser positivo con HID directo cero, o viceversa |
| `H_releasable`, `HID_potential` | Capacidad liberable bajo un testigo técnico seguro | Posible explicación/mediación; no demuestra aumento correspondiente de GIC |
| `ρ`, `F_HICT`, `HID_spent` | Recuperación y conversión condicional de horas/capacidad | Análisis posterior; jamás se coloca como coeficiente oculto en la resta primitiva |
| `G_technical`, `G_governable` | Distancias de utilidad | Libro económico distinto, no se suma a la deuda de inteligencia humana |

**Autoridad de medición:** [01K](../../../../01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) y [01K-A01](../../../../01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1.md). La fuente del modelo no crea otro protocolo de observación humana.

## 3. ABCD: mismo mundo físico; distinta cualificación del proceso

La prueba [network_abcd.json](scenarios/network_abcd.json) usa cuatro brazos con **idéntica** producción lineal, topología, probabilidad de incompatibilidad, costes de enlaces, obligaciones y capacidad humana. Sólo cambia el **estado epistémico del proceso para una pregunta declarada y la política explícita que éste puede ejecutar**:

| Brazo | Posición de partida del proceso | Acción experimental declarada |
|---|---|---|
| A | Resultado funcional utilizable de cualificación | Emplear las relaciones efectivamente establecidas en A |
| B | Reserva caracterizada, inspección con coste conocido | Inspeccionar el soporte B; la inspección produce nuevos resultados A con NEO explícita |
| C | Ruta plausible de exploración, sin alcance/beneficio/coste estimable ex ante | Explorar una relación por período, registrar ex post 0,2 h de trabajo exploratorio por relación sin declarar conocido el resto |
| D | Dependencia/residual sin ruta efectiva de evaluación para ese proceso | No afirmar resultados de cualificación; su efecto sólo lo ve el **oráculo del investigador**, no el decisor |

**A/B/C/D no son probabilidades, porcentajes de red ni conjuntos cerrados de enlaces**. El resultado A después de una inspección B no transforma automáticamente en A todos los B/C/D de ese proceso. Las letras no determinan la cantidad de conocimiento ni el valor económico: lo hacen las políticas y trazas explícitas del experimento. [00M fuente semántica](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md).

Para poner a prueba *un mecanismo posible*, el generador sintético declara por separado:

- Enlaces reales nuevos (t) por incorporación, que sólo el **oráculo** conoce íntegramente.
- Enlaces que una política puede cualificar antes de actuar: todos, uno o ninguno, según el brazo **diseñado**, no deducido de la letra ABCD.
- Enlaces físicamente presentes sin cualificación operativa suficiente (contabilidad **oracle-only**); opción de recalificación posterior.
- Aporte informacional GIC por dimensión, producido mediante una hipótesis falsable de pérdida por vínculo todavía no cualificado; parámetro independiente de las horas ACW. Un coeficiente cero anula la diferencia HID.

El motor calcula el vector humano GIC obtenido en cada brazo y **sólo después** resta los inputs frente a cada trayectoria óptima comparable. Recurso, servicio y derechos se conservan. Los costes de verificación B van a NEO y no se denominan HID por defecto.

### Resultado de referencia (horas sintéticas, t=20)

Con `n=t` nuevas interacciones por ciclo, sin retiro epistémico y pérdida declarada `0,025 diagnosis + 0,015 design` horas por enlace no cualificado, la brecha de la política D respecto de A resulta:

```text
enlaces_oráculo_sin_cualificación_D(t) = t(t+1)/2
HID_direct_horas_D→A(t) = 0,04 × t(t+1)/2
HID_direct_horas(t20) = 8,4
Δ²HID_direct_horas(t) = 0,04 horas/ciclo²
HID_direct_ratio(t20) = 8,4 / 200 = 0,042
Δ²HID_direct_ratio(t) ≈ 0   [el recurso humano crece como t]
```

**Hallazgo del modelo, no del mundo:** la deuda absoluta en horas es convexa bajo esos supuestos; la ratio normalizada es aproximadamente lineal. El mismo experimento puede producir linealidad sin aceleración con topología dispersa, igualar HID=0 si el coeficiente de pérdida informacional es cero o reducir la deuda si hay recalificación. Éstos son contrastes reproducibles y refutables del supuesto experimental, no una demostración de que D cause deuda en la realidad.

En los cuatro brazos, las horas ACW físicas en t20 son **idénticas** (21 horas por período). Sin embargo, los inputs humanos GIC difieren. Esto verifica específicamente que el programa **no está definiendo HID como una transformación encubierta de ACW**.

El contador de enlaces del investigador no representa un inventario que el proceso C/D posea. Para una inferencia sobre personas/organizaciones se necesitan observación independiente, evidencias del mecanismo, juicio sobre sustituibilidad, comparadores competentes y los protocolos existentes de 01K. La propia simulación **no** satisface esos requisitos.

## 4. Verificaciones y estados

Desde el directorio del toy, ejecutar:

```bash
python3 -B -m unittest discover -s . -p 'test_*.py' -v
python3 -B run.py portfolio scenarios/portfolio_hid.json --summary
python3 -B run.py network scenarios/network_abcd.json --summary
python3 -B run.py network scenarios/network_abcd.json --set unqualified_dependency_input_loss_rates.diagnosis=0 --set unqualified_dependency_input_loss_rates.design=0 --summary
```

La batería conserva las **34 pruebas de regresión** existentes y agrega **18 controles específicos**: independencia respecto a ACW; cada óptimo; invalidez por cambios de recursos, servicio o autoridad; ausencia de inferencia si faltan vectores; igualdad de física; curvatura absoluta frente a ratio; nulo de pérdida; topología dispersa; recalificación y rechazo de contribución negativa. **Estado: 52 pruebas locales en total; ejecución sintética, no HID2 original.**

Se mantienen los IDs de 01K/UC21/R01 y los resultados congelados. Los mecanismos de Attribution Gap e Informational Friction conservan su [estudio puente separado](../causal-bridges-v0.1/README.md). [Estudio de segundo orden 01K-A02](../../../../01K_A02_HID_SECOND_ORDER_ECONOMIC_ACCELERATION_RESEARCH_NOTE_v0.1.md).

## 5. Condición de promoción: benchmark A no es tecnología EA probada

En el escenario ABCD actual, `A_result` conoce/puede cualificar todos los enlaces operativos y su coste adicional de verificación `neo_hours_per_qualified_link` se fija en **cero**. Es una **referencia ideal sintética**, no una prueba de que una implementación real de Ecosystem Awareness alcance esa cualificación ni de que su obtención sea gratuita. La pérdida de inputs GIC por cada enlace sin cualificación está igualmente declarada como parámetro experimental, no observada desde datos humanos.

Por ello, la reducción de 8,4 horas frente a A y su curvatura no son **efecto causal neto atribuido a EA**. La comparación crítica siguiente debe incluir un incumbente técnicamente fuerte con acceso legítimo a la misma información, tiempos y costes completos de obtención/validación de B/C/D, ablations y nulos preregistrados. Véase la [auditoría de promoción del modelo social](../../review/PROMOTION_AUDIT_2026-10-25.md). El cálculo primario HID queda implementado aunque esa hipótesis tecnológica permanezca abierta.

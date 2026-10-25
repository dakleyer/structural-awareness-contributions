# ACC — Toy económico paramétrico ejecutable (v0.1)

**Autor conceptual:** Iván Abril Palma / The Integral Management Society. **Estado:** instrumento ejecutable de investigación sintética. **Fecha:** 25-10-2026. **Lenguaje:** Python 3.10+ y biblioteca estándar, sin servicios externos ni dependencias. **Propietario del modelo:** [ACC — núcleo técnico del modelo económico abierto](../../ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md). **Propietario de HID:** [01K / anexo A02](../../../../01K_A02_HID_SECOND_ORDER_ECONOMIC_ACCELERATION_RESEARCH_NOTE_v0.1.md).

Este toy permite variar **dimensiones**, condiciones soberanas, presupuesto, costes de descubrimiento/negociación/reconfiguración, opciones de compensación, aportación productiva, densidad de dependencias, incompatibilidades, retiro, coste de mantener obligaciones, carga humana ACW, recuperación hipotética y coeficientes de utilidad. Calcula la distancia a soluciones factibles y el grado de suboptimalidad **dentro del espacio de estados definido por el usuario**.

No modifica ni reinterpreta el [piloto económico ya congelado](../economic-pilot-v0.1/STUDY_PROTOCOL.md) ni sus resultados. Tampoco ejecuta agentes ACC, pruebas UC21/R01 o DDS Stage B/C. Las 10.000 réplicas históricas del manuscrito siguen sin autenticarse; este programa **no afirma reproducirlas**.

## Cómo ejecutarlo

Desde este directorio del repositorio:

~~~bash
python3 -B -m unittest discover -s . -p test_toy.py -v

python3 -B run.py portfolio scenarios/portfolio.json --summary
python3 -B run.py network scenarios/network.json --summary
python3 -B run.py formulas scenarios/formulas.json

python3 -B run.py portfolio scenarios/portfolio.json --set approvals.CFO=false --summary
python3 -B run.py network scenarios/network.json --set arms.N.retirement_rate=0.15 --summary
python3 -B run.py network scenarios/network.json --set arms.N.p_incompatible=0.4 --summary
python3 -B run.py formulas scenarios/formulas.json --set topology=\"star\"
~~~

Barrido factorial reproducible, con 2×3 = 6 escenarios (cada combinación ejecuta el mismo motor con parámetros nuevos):

~~~bash
python3 -B run.py network scenarios/network.json \
  --sweep 'arms.N.p_incompatible=[0.1,0.2,0.4]' \
  --sweep 'arms.N.retirement_rate=[0.0,0.15]' \
  --format csv
~~~

El CSV sale por la salida estándar; sólo se escribe en disco si el usuario lo redirige explícitamente. Sin parámetros externos ni semilla oculta: los cálculos son esperanzas analíticas deterministas. El comando permite hasta 256 combinaciones por llamada y verifica rutas/valores; para muestras estocásticas habrá que añadir otro estudio con semillas preinscritas, sin atribuirlo a la fuente histórica.

## Tres motores complementarios

| Modo | Qué calcula | Qué no afirma |
|---|---|---|
| **portfolio** | Estados finitos, oportunidades y costes por actor, transferencia con suma cero, restricciones duras, autorizaciones, óptimos técnico y gobernable, distancia y resultado actual, eficiencia a igual servicio, GIC/NEO/ACW y HID condicional | No prueba viabilidad fuera de los proyectos enumerados; una solución técnica sin permiso no es ejecutable |
| **network** | Crecimiento n→n+1, producción, interacciones, obligaciones nuevas/retiradas, ACW por período, acumulado D_T, segunda diferencia, pronóstico parcial, utilidad neta, alternativas y brechas entre trayectorias, métricas HID sintéticas | No observa empresas ni demuestra causalidad a partir de curvatura; una brecha entre **historias** no es un óptimo instantáneo hoy |
| **formulas** | M0 unanimidad, M1 exposición de enlaces, M2 sinergia productiva y M3 propuestas endógenas; cálculo directo para n=5,10,20… | R(n) y D_bruta son propuestas rechazadas, no oportunidades conjuntamente recuperables ni deuda HID |

### 1. Portfolio: ¿por qué seguimos en subóptimo?

Entrada: [scenarios/portfolio.json](scenarios/portfolio.json). El modelo enumera hasta 16 proyectos distintos (2^16 combinaciones antes de aplicar restricciones), con n etiquetas abiertas de dimensión; no fija los cuatro ejes económicos como cuatro personas con veto.

Cada proyecto declara:

- **producción** y **recursos** en registros físicos diferentes de las utilidades;
- vector de outputs completo y su modificación (para identificar igualdad de servicio);
- beneficio bruto por actor en un numerario ficticio; costes extraordinarios por actor y categoría; transferencias t_i con Σt_i=0;
- cambios de GIC, NEO, ACW y horas UNKNOWN, así como quién soporta la variación ACW monetizada si se desea;
- autorizaciones requeridas, dependencias, incompatibilidades y preservación de derechos.

El algoritmo enumera estados técnicamente admisibles **bajo guardrails duros de recursos, servicio, derechos, capacidades y presupuesto**, obtiene F^T y luego F^G aplicando aprobaciones y la condición de aceptación por actor, cuando se activa. **Desde el estado actual sólo permite agregar proyectos**, no deshacer proyectos vivos sin un modelo de rollback. El presupuesto de transición se carga sobre los proyectos nuevos; la condición por actor compara su utilidad con la **utilidad del estado actual**, no con una fotografía inicial ya superada. Una dimensión nueva **no añade veto** hasta que el escenario declare una condición bloqueante efectiva.

Para cada alternativa calcula:

~~~text
U(S) = suma de payoffs brutos de proyectos
       − C_adj por episodio, una sola vez
       − λ_ACW × delta de ACW, si se habilitó el coste sombra
       + transferencias internas con suma cero

G_technical = max(0, max_{S∈F^T} U(S) − U(actual))
G_governable = max(0, max_{S∈F^G} U(S) − U(actual))
G_efficiency = recursos(actual) − mínimo recurso
               entre estados con EXACTAMENTE igual vector Y
~~~

La diferencia F^T∖F^G identifica un bloqueo de acceso/consentimiento, **no** prueba pérdida recuperable jurídicamente. Si el estado actual ya carece de gobernabilidad con las reglas presentes, G_governable se reporta como **null** hasta recalibrar el supuesto. Los proyectos con beneficio neto negativo o restricciones inválidas no se fuerzan como mejoras. Los outputs comparables tienen iguales coordenadas declaradas; los componentes omitidos de calidad/riesgo siguen siendo un supuesto del escenario, no una verificación del programa.

El caso incluido tiene **cuatro actores** (Marketing, Operations, Systems, Finance), cinco coordenadas y dos decisiones. El estado actual ejecuta SCALE. La solución conjunta INTEGRATE + SCALE alcanza una utilidad adicional de 58 frente al actual y ahorra 20 unidades físicas de recursos para el mismo Y; si CFO=false, la mejora técnica sigue existiendo pero **G_governable=0**. Cambiar transferencias puede convertir un saldo global positivo en no aceptable para Systems. Cambiar costes, permisos o presupuesto puede hacer racional permanecer en el estado actual.

### 2. Network: ¿crece la producción mientras la deuda se acelera?

Entrada: [scenarios/network.json](scenarios/network.json). Se añade una dimensión productiva por período. El modelo no atribuye intenciones a agentes; observa interacciones y su coste.

Para cada brazo b y período t:

~~~text
n_t = t
N_t = p_t × relaciones_nuevas_t
R_t = r × O_(t−1)
O_t = O_(t−1) + N_t − R_t
d_t = h × O_t                           horas ACW por período
D_T = Σ_(t≤T) d_t                       horas acumuladas con Δt=1
P_t = base_productiva × t
      + sinergia × (relaciones_totales_t − O_t)
V_t = valor(P_t) − λ_ACW d_t
      − coste_mantenimiento O_t − C_adj,t
Δ²d_t = d_t − 2d_(t−1) + d_(t−2)
e_t = d_t − d̂_t                       diferencia vs mapa ex ante
~~~

Parámetros editables: topología **dense/sparse/star/modular**, p (incompatibilidad), r (retiro), perfil **flat/inverse_time** de interoperabilidad, h (horas por obligación), producción por dimensión, sinergia útil, conversión ACW→utilidad, coste de mantenimiento, inversión de integración, coste por enlace, GIC/NEO y capacidad humana disponible.

Se incluyen cuatro brazos:

| Brazo | Condición | Interpretación |
|---|---|---|
| N | Densa, p=0,20, sin retiro | Interdependencias persistentes |
| L | Dispersa, p=0,20 | Control analítico lineal; no declarado técnicamente disponible como sustitución en el escenario base |
| E | Densa, p_t=0,20/t | Interoperabilidad; requiere inversión/coste propio, inicialmente no autorizada |
| R | Densa, p=0,20, retiro r=0,15 | Retiro seguro como mitigación gobernable |

Con b=10, h=3, T=20 y otros parámetros del ejemplo:

- N: **d_20=126 h/período**, D_20=924 h acumuladas, Δ²d≈0,6. El mapa que ve sólo L estima d̂_20=12, con error e_20=114.
- El beneficio productivo aumenta P_16=160→P_20=200, pero V_16=78,4→V_20=74 bajo λ=1 y sin nuevos costes adicionales en N: el primer incremento marginal negativo ocurre en t=17.
- E deja la carga esperada cerca de 12 h/período; R cerca de 58,21 h/período. **Contabilizar** inversión, retirada, mantenimiento y derechos puede cambiar cuál alternativa es realmente mejor.
- La configuración inicial marca E técnicamente disponible pero no autorizada; R sí autorizada. Por eso el modelo entrega dos distancias de **trayectorias**, una técnica y otra gobernable. Su interpretación depende de igualdad de servicio a lo largo de todas las fechas comparadas y de que la historia alternativa pudiera haberse elegido en t=0.
- La curvatura positiva se deriva de topología + persistencia supuestas. **No es prueba causal de segundo orden fuera del toy.**

Si se activan sinergias, el output entre brazos puede dejar de ser comparable; entonces no se fabrica una distancia de bienestar entre servicios distintos. Si el trabajo humano esperado supera la capacidad disponible en **cualquier período de la trayectoria**, el motor marca saturación histórica y suspende las conclusiones de brecha y recuperación de esa trayectoria, incluso si el período final ya no está saturado. Las alternativas también han de respetar capacidad en cada período.

### 3. Fórmulas: comparar mecanismos M0–M3 sin reprogramar

Entrada: [scenarios/formulas.json](scenarios/formulas.json). Varíe n_values, q_accept, p_incompatible, g, k, a, b, c, v y topology.

~~~text
M0: D_veto(n) = g n (1−q^(n−1))
M1: D_inter(n) = p c E(n)
M2: P_real(n) = b n + a(1−p)E(n)
    D_oportunidad(n) = a p E(n)
M3: M(n)=k n(n−1); A(n)=M(n)q^(n−1)
    R(n)=M(n)−A(n); D_bruta(n)=v R(n)
    P_endógena(n)=b n+a A(n)
~~~

Los resultados permiten ver cuándo el mero veto se **satura** y cuándo la densidad E(n) o la generación M(n) de propuestas explican una curva cuadrática, y si las sinergias también crecen. Un rechazo no se convierte automáticamente en deuda neta recuperable.

## Capacidad humana y HID

Se preserva la taxonomía del [01K](../../../../01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md):

- **GIC:** genuine information contribution; sólo horas clasificadas como contribución real.
- **NEO:** ejecución/supervisión necesaria, no deuda por definición.
- **ACW:** trabajo compensatorio evitable sólo si existe un contrafactual seguro y comparable; en estos ejemplos, la clasificación es **asumida sintéticamente**, no auditada.
- **UNKNOWN:** horas no calificadas, que el programa no adjudica por defecto.

El código ofrece **HICR_time**, **HID_observed**, **H_releasable**, **HICT_condicional**, **HID_potential**, **F-HICT_condicional** y **HID_spent_condicional** con el denominador adecuado y el ρ declarado. En portfolio se buscan estados del mismo servicio y valor no inferior; en network se buscan trayectorias de output igual, válidas y con coste completo no superior. Si no hay medición válida, devuelve **null/NOT_MEASURED**. Sólo se calcula capacidad de contribución **según la métrica propuesta**, no IQ, talento ni dignidad, ni se presupone pérdida de habilidades.

Para medir HID en organizaciones reales se requiere el Study 0 de 01K, evaluadores y auditoría de reemplazabilidad. La hipótesis de deterioro de capacidad humana o ρ<1 exige un estudio longitudinal posterior; no está embebida como «ley» en las ecuaciones.

## Condiciones de interpretación y límite de evidencia

1. **No prometer factibilidad:** el toy calcula óptimos sólo dentro de alternativas enumeradas y restricciones modeladas. La factibilidad técnica/seguridad declarada no ha sido probada externamente.
2. **No contar doble:** payoffs brutos excluyen C_adj y tiempo ACW valorado, que se descuentan sólo una vez. Las transferencias suman cero. Producción y recursos físicos son ledger distinto a utilidad; horas ACW e HID observado no se suman al gap de utilidad.
3. **No confundir stock con flujo:** O_t son obligaciones, d_t carga en cada período, D_T exposición acumulada, Δ²d_t curvatura. Ninguna identidad prueba aceleración universal.
4. **No confundir veto con dimensión:** sólo gates declarados y actores legítimos; las dimensiones agregadas por sí solas pueden aumentar producción y reducir, mantener o aumentar deuda.
5. **No equiparar historias y estados:** network presenta brechas **pathwise desde origen común**; la frontera accesible en un estado actual exige el motor portfolio o un problema dinámico de reoptimización con transición explícita.
6. **No concluir HID empírico:** las cifras son sintéticas; si no se marca acw_classified_synthetically, el motor no publica un HID_observed numérico. ρ y HICT son condicionados.
7. **Causación no automática:** p, topología, retiro y sinergia están en la ecuación; un barrido identifica sensibilidad y regiones posibles, no confirma el mecanismo empresarial sin comparadores medidos.

## Pruebas y siguiente nivel

[test_toy.py](test_toy.py) ejecuta **34 pruebas** de invariantes y resultados numéricos: transferencias de suma cero; permisos, derechos, costes, exclusiones, frontera de igual servicio; distinción entre HID observado/potencial; red N/L/E/R, retiro, saturación de capacidad, sinergia que impide comparación; reproducción de fórmulas y barridos CLI. El mismo código está incluido en la verificación de PR para comprobar su ejecución.

El paso científico posterior es preregistrar y ejecutar HID2-01…10 en [01K-A02](../../../../01K_A02_HID_SECOND_ORDER_ECONOMIC_ACCELERATION_RESEARCH_NOTE_v0.1.md), empezando por pares con **mismo Y, recursos, información ex ante, autoridad y costes completos**. Después podrán añadirse escenarios con selección de propuestas endógenas, planificación óptima de transición a lo largo del tiempo, incertidumbre aleatoria y fallos de información, siempre versionados sin alterar los estudios originales.

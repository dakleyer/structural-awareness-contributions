# Núcleo funcional isomorfo y extensión parametrizada de R01

Versión de investigación 0.1 · 2 de octubre de 2026

[Familia y casos](./README.md) · [R01](../../README.md) · [Comprobación finita](./proof/README.md)

## 1 Afirmación que se quiere probar

Una extensión puede añadir variables y mecanismos y conservar un núcleo isomorfo a una configuración de R01. **La biyección corresponde al núcleo**, no al estado completo de la extensión. Además de emparejar nombres, hay que preservar relaciones, operaciones, información y resultados observables en ese núcleo.

Definimos un criterio suficiente, deliberadamente fuerte. No se presenta como condición necesaria para toda relación posible con R01. Un caso que no lo satisfaga puede requerir una simulación más débil, una ampliación de R01 o una familia distinta. No se lo admite mediante semejanza narrativa.

El término «isomorfo» se usa estrictamente para las estructuras indicadas. Cambiar un coste o un radio no conserva necesariamente el isomorfismo numérico con la instancia inicial. Se distingue:

1. **Cambio de representación:** el mismo sistema con otra codificación o unidades, normalizadas de forma reversible.
2. **Extensión parametrizada:** el núcleo corresponde a otra instancia de la familia, con parámetros efectivos declarados.
3. **Cambio de reglas:** nuevas transiciones, autoridad, información o política no representables en la instancia base. Exige otra prueba y no queda cubierto por las dos anteriores.

## 2 Estructura del caso base

Una realización ejecutable declarada de R01 se representa como

$$
\mathcal B_\theta=(X,A,E,K,O,\mu_0,c,\ell,\mathsf{Adm},J,F,\Pi).
$$

- `θ`: configuración completa y dominios admisibles de sus parámetros.
- `X`: estado completo, incluido mundo, posición, historia suficiente, memoria, evidencia, mensajes, tiempo y recursos. Incorporar la historia evita presumir una propiedad de Markov que no exista.
- `A`: eventos tipados de exploración, consulta, revisión, envío/recepción, compromiso, ejecución, espera y terminación.
- `E(x,a)`: habilitación del evento, incluyendo presupuesto, plazo, conexiones y reglas del receptor.
- `Kθ(x,a,·)`: ley de transición condicionada al evento; es Dirac si la transición es determinista.
- `O_i`: vista accesible al participante i; se distingue del estado completo del evaluador.
- `μ0`: distribución inicial declarada, sin respuestas del evaluador filtradas al agente.
- `c` y `ℓ`: cargos por categoría y tiempo transcurrido; actualizan recursos y plazo dentro del estado.
- `Adm(τ)`: admisibilidad de la trayectoria efectiva, con prefijo y conexiones.
- `J(τ)`: resultado técnico según el criterio global declarado; las estimaciones del agente son objetos distintos.
- `F`: predicados de resultado: ejecución inadmisible, calidad legítima insuficiente, exceso de recursos, incompletitud. Sus umbrales están fijados.
- `Π`: políticas declaradas sobre historias observables. Conocer una prohibición y ejecutarla no es una política admitida por el receptor básico.

La familia es `𝔅={𝓑θ: θ∈Θ}`. La existencia de esta notación no implementa las políticas pendientes de R01. El teorema siguiente se aplica a realizaciones que efectivamente satisfagan el contrato, no concede ese estado al documento por escribir una fórmula.

## 3 Inventario completo de correspondencias principales

La firma tipada `Σ` contiene **todos** los grupos de R01 §2.13 y los objetos operativos de §§2.1–2.18. Cada símbolo tiene un único referente en el núcleo extendido; su aridad y sus tipos de entrada/salida se conservan. La correspondencia de símbolos es una obligación de firma; el isomorfismo exige además biyecciones sobre los dominios de valores/objetos de cada tipo y preservación de sus relaciones. La biyección de estados h es la inducida por esas codificaciones, no una simple tabla de nombres. Los nombres adicionales del dominio pertenecen a otra firma `Σ+`.

| Grupo / símbolos de base | Referente obligatorio en el núcleo extendido | Relación que debe conservarse |
|---|---|---|
| Tarea: L, misión, principal, resultado, T | Secuencia y obligación del dominio; misma unidad temporal normalizada | Inicio, finalización, autoridad y plazo; el mandato no cambia por un mensaje |
| Población: N, tareas, reparto | Actores y asignación correspondientes | Identidad de actor, unidad individual/colectiva y no duplicación de valor |
| Grafo: tramos, conectores, prefijo | Operaciones y dependencias del dominio | Adyacencia en ambos sentidos, continuidad y efectos de la trayectoria |
| Perfiles generativos: medias, distribuciones, rechazo de mundos | Generación equivalente de atributos de operaciones | Misma ley bajo transformación; declarar cualquier cambio de condicionamiento |
| Beneficios: μ, σ, desviaciones y correlaciones | Utilidad técnica por operación y dependencias | Agregación J y correlaciones; no confundir beneficio aparente con validez |
| Atractivo realizado: I, P, M y mejoras | Rutas evaluadas en el dominio | M admisible; I se obtiene optimizando entre admisibles; P no se revela al agente |
| Geometría: D, τ, lados, posiciones y correlaciones | Coordenadas de búsqueda del dominio | Distancias, orientación y alcance desde la posición actual |
| Exploración: R_e, esfuerzo, muestreo | Capacidad de descubrir operaciones | Radio/esfuerzo → candidatos observados; ley de descubrimiento |
| Composición: predicado, testigo, distribución | Obligaciones y condiciones de dominio | Admisibilidad de la composición; conservar bloque conjuntivo/paridad/mixto declarado |
| Revisión: k_a, k_d, orden, salida, reutilización | Ventana y proceso de consulta de condiciones | Cobertura, rechazo de denegación visible y vigencia de evidencia |
| Costes: c_e, c_v y cargos restantes | Libro de exploración, revisión, ejecución, mensajes y mantenimiento | Todo evento consume su coste; no se borra construcción, consulta ni descarte |
| Recursos: R, reparto v, beta y transferencias | Recursos disponibles y asignados | Conservación de cargos, reparto y reglas de agotamiento |
| Red social: topología, s, latencia, w_s | Envíos/recepciones e influencia correspondientes | Emisión antes de recepción; origen, dependencia y cobertura; información no crea permiso |
| Política: selección y reglas auxiliares | Decisiones sobre vistas correspondientes | Igual regla efectiva para transferir resultados; desempate, espera, rechazo, recuperación |
| Volumen: Q, cobertura y deduplicación | Contadores derivados de las trazas | Q cuenta propuestas únicas; copias no crean evidencia independiente |
| Variación: semillas, versiones y cambios | Fuentes de azar, versiones y eventos de cambio | Ley conjunta, separación de flujos e invalidación de evidencia pertinente |
| Estado operativo: memoria, presupuesto restante, posición, mensajes, tiempo | Estado recuperable del núcleo | Ninguna variable material queda sólo en detalles eliminados por la proyección |
| Observación y evaluación: O, Adm, J, F y umbrales | Vistas, permisos, calidad y resultados de dominio | Separación de saber del agente/verdad del evaluador y preservación de negativos/positivos |

Una constante declarada, por ejemplo N=2, sigue teniendo referente. Un parámetro no ensayado no se considera eliminado ni verificado. Parámetros derivados como I o Q conservan su función de derivación; no se convierten en entradas elegidas para fabricar el resultado.

En H/L/W, la tabla de casos sustituye los nombres de operaciones y obligaciones. Los demás grupos de esta tabla se transportan sin cambios, salvo transformaciones explícitas. Esta es la obligación completa de correspondencia; el comprobador finito cubre sólo el subdominio declarado en su README.

## 4 Extensión, transformación y proyección

Sea `η` una configuración adicional fijada antes del recorrido. Una transformación declarada produce

$$
\theta^*=\Phi(\theta,\eta)\in\Theta.
$$

La extensión tiene estados `Y`, operaciones de dominio y detalles adicionales `Z`. Su núcleo `C` posee una biyección tipada

$$
h:X_{\theta^*}\longrightarrow C.
$$

En una construcción producto, `Y=C×Z`. En una implementación más general basta una proyección sobreyectiva `p:Y→Xθ*` y una sección `s:Xθ*→Y` tal que `p∘s=id`. La sección demuestra que cada estado base es representable; por sí sola **no** demuestra equivalencia de comportamiento.

Las normalizaciones de representación deben ser biyectivas en los dominios declarados. Por ejemplo, `r↦3r` es biyectiva entre los radios originales y los múltiplos de tres correspondientes; no se afirma que sea sobreyectiva sobre todos los enteros. `Φ` puede identificar varias configuraciones tecnológicas con una misma configuración efectiva: no necesita ser biyectiva porque no es el isomorfismo del núcleo.

### 4.1 Obligaciones E1–E7

**E1. Firma y relaciones.** Para cada relación tipada Q y operación f del núcleo:

$$
Q_B(\mathbf x)\iff Q_C(h\mathbf x),\qquad
h(f_B(\mathbf x))=f_C(h\mathbf x).
$$

Las funciones con salida numérica usan también la normalización declarada de esa salida. La implicación doble evita que aparezcan atajos, permisos o dependencias nuevos en el núcleo sin referente.

**E2. Eventos y habilitación.** Hay una correspondencia biyectiva de etiquetas de evento del núcleo, `g`. Para todo estado extendido y evento correspondiente,

$$
E_Y(y,g(a))\iff E_B(p(y),a).
$$

Una operación sólo interna puede agruparse con su macroevento si éste termina con certeza, tiene coste/tiempo acotado y declarado y conserva toda observación intermedia material. Un bucle interno que demora indefinidamente no puede desaparecer como si nada hubiera pasado. La prueba de este documento usa un macroevento extendido por evento base, sin esa dificultad adicional.

**E3. Transiciones y azar.** Para todo conjunto medible U de estados base y cada representante y de una fibra:

$$
K_Y(y,g(a),p^{-1}(U))=K_{\theta^*}(p(y),a,U),
\qquad p_*\mu^Y_0=\mu^B_0.
$$

No basta comprobar un representante. Si dos valores de una variable extra con igual proyección producen distintas leyes futuras del núcleo, la proyección pierde información y falla E3. Debe retenerse esa variable o demostrar una abstracción diferente. Esta condición corresponde a una equivalencia probabilística sobre clases de estados; se inspira en la noción de bisimulación probabilística [M1], sin atribuir a esa fuente la prueba específica de R01.

**E4. Observaciones y políticas.** Las vistas normalizadas de cada actor son iguales bajo p, incluidas las historias de evidencia, sus orígenes y condiciones. La extensión no revela `Adm`, I ni hechos que la base no podía conocer. Para transferir resultados de una política se exige además

$$
\pi_Y(g(a)\mid H_Y)=\pi_B(a\mid p(H_Y)).
$$

Un dato adicional visible que influya en la decisión debe tener referente en la observación base. Si sólo hay un controlador que ignora ese dato, la equivalencia se limita a esa clase de controladores, no a todos los agentes posibles.

**E5. Contabilidad y tiempos.** Los costes y tiempos por evento coinciden con los de `θ*` después de normalizar unidades, y sus efectos sobre saldo, habilitación y plazo también. Cambiar sólo la unidad monetaria exige transformar presupuesto y umbrales en la misma proporción. Reducir realmente el coste con presupuesto fijo cambia la configuración efectiva y puede permitir más revisión.

**E6. Semántica de resultado.** Para toda trayectoria del alcance declarado,

$$
\mathsf{Adm}_Y(\tau)=\mathsf{Adm}_B(p\tau),\quad
J_Y(\tau)=J_B(p\tau),\quad F_Y(\tau)=F_B(p\tau).
$$

Si se cambian unidades de J o umbrales se normalizan antes. Se preservan trayectorias admisibles y el óptimo entre ellas, incluidos empates. Un sensor que sólo mide aceptación técnica no sustituye `Adm`.

**E7. Cobertura del alcance y positivo.** Cada trayectoria base del alcance se puede levantar a la extensión. Cada trayectoria extendida cubierta se proyecta a una trayectoria base. Se incluyen la alternativa legítima comparable, la abstención y los finales incompletos. Si sólo se cubre un subgrafo o una fase, se declara así; otras rutas pueden cambiar el óptimo global y no quedan automáticamente incluidas.

## 5 Proposición de conservación y prueba

**Proposición.** Bajo E1–E7, las políticas emparejadas y el mismo horizonte normalizado tienen la misma ley de historias proyectadas. En consecuencia conservan las probabilidades de los predicados F y las distribuciones de calidad, coste y tiempo definidos en el núcleo. El cociente de la extensión por `y~y' ⇔ p(y)=p(y')` tiene el comportamiento de `𝓑θ*` y su núcleo relacional es isomorfo al de esa instancia.

**Prueba.** La igualdad inicial es E3. Supongamos igual ley de historias hasta t. E4 asigna iguales probabilidades a eventos correspondientes en esas historias; E2 conserva su habilitación. E3 da la misma probabilidad de cada clase de sucesores, independientemente del representante extendido. Integrando sobre historias y eventos se obtiene la igualdad hasta t+1. Por inducción se conserva toda historia finita dentro del horizonte. E5 conserva los cargos y tiempos acumulados y por tanto las paradas por presupuesto o plazo. E6 transporta los predicados de resultado. E7 evita perder trayectorias legítimas o añadir recorridos sin referente; E1 conserva sus relaciones. Esto prueba las afirmaciones. □

La igualdad de ley se refiere a `θ*`, no necesariamente a `θ`. No prueba que un agente elija la ruta prohibida, que una defensa falle ni que EA sea superior. Si el brazo emparejado bloquea correctamente la ruta en la base, la extensión también lo hace. Para trasladar un resultado a otro punto de la familia se necesita análisis de sensibilidad o una demostración adicional.

### 5.1 Construcción de una clase de extensiones

Para cualquier realización `𝓑θ*`, elíjase una codificación biyectiva h de los objetos del núcleo y añádase un estado z, por ejemplo 50 variables auxiliares. Defínase una ley de evolución auxiliar H, normalizada para cada transición base, y:

$$
K_Y((h(x),z),g(a),(h(x'),z'))
=K_{\theta^*}(x,a,x')\,H(z'\mid z,x,a,x').
$$

La fórmula se escribe para estados discretos; basta para los escenarios finitos propuestos. Transportamos habilitación, observaciones, costes, tiempos y predicados con h. La distribución inicial proyecta a μ0 y `p(h(x),z)=x`. Al sumar sobre z', H suma uno; se obtiene exactamente E3. Las otras condiciones se siguen de sus definiciones y del inventario completo. Cada transición base de probabilidad positiva tiene algún levantamiento. Por la proposición, esta construcción es una extensión con núcleo isomorfo. □

Las variables extra pueden depender unas de otras y del núcleo. Su influencia sobre el núcleo se admite mediante Φ si sus valores tecnológicos se fijan durante el episodio. Si evolucionan y alteran decisiones, costes o permisos, su estado relevante debe incorporarse a una configuración dinámica base y volver a comprobar E1–E7. El número de variables adicionales no decide la admisión; la decide la preservación de dependencias.

**Aplicación condicional a las especificaciones H/L/W.** Se propone como h la codificación de operaciones, obligaciones, recursos y mensajes de la tabla de casos. Los predicados de dominio son respectivamente permisos de alcance, preservación semántica y autorización de efectos. Se transportan todos los grupos de §3 y se aplica la construcción anterior. Esto demuestra existencia de codificaciones formales por transporte con los predicados declarados. Para una realización independiente H/L/W aún debe verificarse que todas sus operaciones, vistas y relaciones cumplen E1–E7; la etiqueta de dominio no prueba esa adecuación. No demuestra que una API, un verificador real o una traza histórica implementen esas ecuaciones: su adecuación requiere comprobaciones independientes. El testigo finito usa evaluadores de dominio separados para contrastar esa obligación y detectar alteraciones.

### 5.2 Corolario para dos brazos comparados

Para cada brazo b∈{EA,C}, E1–E7 debe cumplirse en el sistema cerrado con su política emparejada, sus observaciones y todos sus cargos. Si la misma métrica integrable m factoriza por la proyección y se mantienen mundo, configuración efectiva y horizonte, la proposición iguala su esperanza por brazo. Al restar se obtiene Δ_Y(m)=Δ_B(m). Esto conserva un contraste definido, no establece que sea positivo. La ley conjunta debe preservarse también si se pretende transportar la distribución de diferencias emparejadas, no sólo sus esperanzas.

La [nota metodológica §§3–6](../METHODOLOGICAL_FOUNDATIONS.md) desarrolla hipótesis, prueba de este corolario, posibles cotas aproximadas y precedentes primarios. La equivalencia del estado del evaluador no hace plenamente observable la tarea del agente; E4 sigue siendo indispensable. Citar un homomorfismo de MDP no sustituye esa obligación ni acredita implementación o eficacia EA.

## 6 Transformaciones concretas y contraejemplos

| Cambio | Condición para admitirlo | Qué no se transfiere sin más |
|---|---|---|
| Radio triplicado por una tecnología | Φ asigna `R_e*=3R_e`; las operaciones alcanzables y la ley de búsqueda son las de esa instancia | La tasa de descubrimiento o fallo de la instancia con R_e original |
| Cambio de escala espacial | Multiplicar coordenadas, radio y ventanas geométricas por la misma constante positiva; normalización inversa | Una escala con redondeo que fusiona posiciones materialmente distintas |
| Revisión más barata | `c_v*=λ c_v`, λ>0, con cargos y saldo coherentes; verificar `0<c_v*<c_e*` para el régimen básico | El mismo número de consultas posible con presupuesto fijo |
| Revisión con certificado suficiente | El certificado, producción, alcance, consulta y coste están representados en la base efectiva | La dificultad del caso sin certificado; puede desaparecer legítimamente |
| Cincuenta variables auxiliares | E3 vale para todos sus valores y no se filtra información bajo E4 | Influencias futuras que la proyección oculta |
| Nuevo canal descubierto | La búsqueda y decisión se representan como acciones; cualquier cambio posterior de topología tiene referente dinámico | La equivalencia de una población con topología fija a otra que cambia sin modelarlo |
| Continuar con prohibición detectada | No cumple el receptor básico; requiere perfil conductual ampliado | La admisión como mero cambio de radio, coste o nombres |

Contraejemplos que invalidan una proyección: fusionar dos condiciones con distinta admisibilidad; omitir una conexión; añadir un permiso sin principal; tratar dos copias como fuentes independientes; borrar el coste de consultar; revelar al agente el testigo oculto; conservar nombres de variables pero cambiar la probabilidad de descubrimiento; olvidar una ruta legítima superior al calcular I. Mantener el dibujo del grafo no salva estos fallos.

Un λ igual a cero abandona el régimen de coste positivo, aunque pueda estudiarse en otra familia. Una reducción que mezcla paridad y conjunción sin preservar sus veredictos tampoco cumple E1/E6.

## 7 Testigo finito, relación con A25 y límites

El [paquete de comprobación](./proof/README.md) verifica codificación, grafo, permisos/obligaciones, calidad, geometría, observaciones y un fragmento de transición con exploración estocástica, revisión, comunicación de evidencia y compromiso. Comprueba parámetros efectivos y mutaciones inválidas. La comprobación usa aritmética exacta; no es una demostración automatizada de todo R01. La proposición de §5 es un argumento matemático explícito, no un teorema certificado por un asistente de pruebas.

| A25 | Obligación que aporta esta nota |
|---|---|
| X1 núcleo | Inventario §3 y E1 |
| X2 frontera de decisión | Habilitación, observación y compromiso: E2/E4 |
| X3 mismo fallo | E6, en ambos sentidos para el alcance declarado |
| X4 requisitos conservados | E1/E2 y matriz de requisitos aplicables; pendiente su aplicación completa a cada implementación |
| X5 positivo | E6/E7, rutas legítimas y óptimo |
| X6 recursos | E5, presupuesto, tiempo y cargos completos |
| X7 ninguna primitiva oculta | Firma Σ+, E3/E4 y tratamiento explícito de nueva capacidad |

El isomorfismo de R01 no sustituye las condiciones específicas de C-V-G ni la matriz canónica de conformidad de 00G. Se puede conservar R01 y quedar fuera de esa subfamilia social. La admisión histórica y las ejecuciones de EA mantienen sus obligaciones propias.

## 8 Fuentes

- [Fundamento metodológico: fuentes primarias, precedentes computacionales y límites de transferencia](../METHODOLOGICAL_FOUNDATIONS.md).

- Base y fuente del inventario: [R01 v0.6 en el commit fijado](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md).
- Método interno: [A25](../../../../00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md), §§3–6.
- M1: Blute, Desharnais, Edalat y Panangaden, *Bisimulation for Labelled Markov Processes*, LICS 1997. Referencia para equivalencia probabilística por clases, no para los resultados de R01. https://www.cs.mcgill.ca/~prakash/Pubs/lics97.pdf
- Fuentes de incidentes y localizadores: [tabla de referencias](./README.md#3-casos-documentados-que-motivan-la-familia).

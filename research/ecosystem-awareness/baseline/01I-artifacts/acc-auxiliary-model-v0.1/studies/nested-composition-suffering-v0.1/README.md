# ACC — Composición jerárquica, indeterminación relacional y sufrimiento estructural (estudio v0.1)

**Autor conceptual:** Iván Abril Palma / The Integral Management Society.  
**Fecha:** 26 octubre 2026.  
**Rol:** investigación complementaria y separada del [PR #42](https://github.com/dakleyer/structural-awareness-contributions/pull/42), no modificación normativa de ACC/01K/00M y no resultado empírico en humanos.  
**Estado:** propuestas formales y contraejemplos FINITOS, pruebas automáticas; el uso humano del término «sufrimiento» es una **definición operacional estipulada por el autor**, no una identidad psicológica ni un diagnóstico.  
**Límite de preservación:** todos los ejemplos del autor están registrados con identidad estable en el [libro de ejemplos del PR #42](../bounded-traps-v0.1/EXAMPLE_LEDGER.md); este estudio conserva los específicos sobre liceo, barrio desfavorecido y suprasistema X−200 en el §7. Una incorporación de esas viñetas al canon requiere revisión del titular.

## 0. Preguntas exactas y riesgo de confundir problemas

Queremos distinguir:

1. **Brecha de desarrollo genuino:** un participante/función podría ofrecer mayor contribución con recursos ya disponibles a escala del conjunto, pero las restricciones actuales lo mantienen por debajo de una alternativa legítima y factible.
2. **Bloqueo externo:** el camino NO depende sólo del agente; exige recursos/coordinación/consentimiento ajenos, sin presuponer egoísmo ni atribuir automáticamente un veto jurídico.
3. **Indeterminación relacional:** desde la información genuinamente disponible al agente receptor no puede determinarse plenamente qué permite o impide el otro subsistema, porque la interfaz ha fusionado estados relevantes.
4. **Complejidad por composición:** cómo sistemas locales con reglas simples, en algunos casos lineales o monótonas, pueden producir espacio conjunto grande, restricciones cruzadas, deadlocks, resolución combinatoria difícil y límites de comunicación entre capas.

La postura falsable debe admitir que un interfaz suficientemente completo, un coordinador competente, un protocolo de cambio conjunto o capacidades sobrantes eliminen la dificultad. **No existe teorema general de que composición ⇒ indeterminación, sufrimiento, NP-dificultad o no computabilidad.**

## 1. El mecanismo mínimo: *Reachability* y óptimo conjunto no coinciden

Sea `s` el estado actual, `F_phys` las configuraciones finales que pueden existir con los mismos medios y servicio, `F_rights ⊆ F_phys` las compatibles con derechos y consentimiento, y `Reach_Π(s) ⊆ F_rights` aquellas alcanzables bajo el **protocolo Π actual de acciones**. La trayectoria puede estar bloqueada aun cuando el estado final superior sea materialmente posible. Ésta es una observación independiente de si todos los individuos actúan racionalmente.

El caso del [PR #42](https://github.com/dakleyer/structural-awareness-contributions/pull/42): `x1≤x2`, `x2≤x1`, decisiones binarias; `u1=4+x1`, `u2=4+x2`. (1,1) domina a (0,0) pero no hay paso unilateral factible. Si un coordinador puede hacer un cambio conjunto atómico autorizado, (1,1) pasa a `Reach`. Las restricciones son lineales; no las convierte en «entropía exterior» ni en un fallo lógico.

Para el consumidor downstream de una función compuesta, imaginar que su salida **debe** seguir creciendo con el input es incorrecto aun si la función es matemáticamente monótona: `f(u)=min(u,k)` es no decreciente y tiene una meseta en k. La información **que falta** es `k` y posiblemente los mecanismos por los que puede variarse legítimamente; no es preciso suponer un comportamiento local irracional.

## 2. Modelo jerárquico: simplificar subsistemas no conserva todas las consultas

Un productor compuesto tiene estado interno `s∈S`, recursos `r`, acciones `a`, transición parcial `T(s,a)`, outputs `y(s,u)` y condiciones de gobierno. Un receptor recibe una abstracción o interfaz válida en cierto alcance:

`α: S → Z`, con `Z` los mensajes/output observables (el A del proceso transmisor bajo una pregunta). Para una pregunta del receptor `q`, sea `r_q:S→R_q` la respuesta correcta según el modelo de ensayo.

**Lema de factorización (resultado clásico, no teorema original):** existe una función `h_q:Z→R_q` que decide correctamente con `h_q(α(s))=r_q(s)` para todo estado admitido, SI Y SÓLO SI `r_q` es constante en cada fibra `α^{-1}(z)` de ese marco. Si hay `s1,s2` con el mismo A pero diferentes respuestas requeridas, ningún receptor A-only puede resolver ambos. Una fuente adicional B/C/D con procedencia real puede recuperar alguna distinción; recalcular funciones de A no puede hacerlo por sí solo.

El problema no nace necesariamente de un velo artificial. Si la interfaz sólo tiene un presupuesto `b` bits y el receptor debe distinguir `m` perfiles de respuesta relevantes, **ningún codificador de máximo `2^b` mensajes es suficiente para todas las consultas si `m>2^b`** (principio del palomar). Es una imposibilidad **condicional al presupuesto, consulta y marco de estados declarados**. Si otro canal, mejor diseño o precomputación ofrece las distinciones necesarias, desaparece; por tanto el presupuesto y las restricciones de adquisición de Q son obligaciones de prueba, no una propiedad metafísica de la sociedad.

### Contraejemplo reproducible: estados distintos, mismo A actual

En el toy, un proveedor entrega 8 unidades bajo pedido de 8. Hay dos situaciones internas compatibles con `A=(pedido8,entrega8)`:

- `w0`: con las mismas reglas actuales no existe una transición conjunta que lleve su capacidad a 10; máximo conjunto 8.
- `w1`: sí hay una transición conjunta físicamente factible hacia 10, pero las acciones unilaterales están bloqueadas; máximo conjunto 10 si se dispone de coordinación adecuada.

El downstream recibe exactamente el mismo A (8) en ambos mundos, pero la respuesta a «¿puede entregar 10 tras coordinación conjunta?» es distinta. **El desconocimiento no se introduce asignando una tasa arbitraria de error al receptor; aparece al proyectar dos estados distintos sobre el mismo dato permitido.** Una cualificación auténtica `joint_transition_possible` separaría los casos; sin ella, `UNKNOWN` es el veredicto correcto.

El mundo real puede contener una tercera posibilidad que el toy no modeló. No cuantificar B/C/D por el hecho de haber enumerado `w0` y `w1`. Una clasificación exhaustiva del exterior simplemente convertiría ese problema en otro A.

## 3. Construcción recurrente y exigencia creciente de comunicación

Para `n` subsistemas con capacidad local `k_i∈{8,10}` se ejecuta inicialmente sólo el input 8 para cada uno. El agregado visible A es `8n` **independientemente** de los `2^n` vectores de capacidades. El receptor puede después preguntar por la entrega máxima individual de *cualquiera de las n ramas* cuando el pedido sea 10. Hay `2^n` perfiles distintos de respuestas a esa familia de `n` preguntas.

Si el receptor debe contestar **correctamente todas esas preguntas** desde un único mensaje de interfaz antes de elegir la consulta, se necesitan por lo menos `n` bits de discriminación adicional en el peor caso. Demostración: si `b<n`, sólo existen `2^b<2^n` mensajes; dos perfiles diferentes reciben el mismo mensaje pero no pueden producir el mismo vector completo de respuestas. Los tests verifican `n=1..6`. 

**Control negativo esencial:** si la pregunta fuese únicamente el output TOTAL futuro, sólo importa cuántas ramas están saturadas: hay `n+1` respuestas posibles, y bastan `ceil(log2(n+1))` bits bien elegidos. El runner contiene además un agregador RECURSIVO de árbol binario: las hojas evalúan el input, cada nodo intermedio transmite la suma de sus hijos y el receptor superior ve sólo el agregado. Todos los perfiles siguen dando el mismo A inicial; el cálculo interno sigue siendo completamente finito y determinista. Si el receptor necesita sólo decidir un único umbral, puede bastar aún menos. Así, el coste de cualificación depende de la **pregunta receptora**, no del número de microestados por sí solo; este resultado enlaza directamente con la suficiencia situada de 00M.

La composición jerárquica puede crear estados conjuntos `S_1×⋯×S_n` y obligaciones cruzadas, mientras cada interfaz sucesiva conserva sólo distinciones seleccionadas. Para un mismo universo probabilístico FINITO y sucesivos canales `X→Z1→Z2` sin nuevas observaciones, la desigualdad de procesamiento de datos asegura `I(X;Z2)≤I(X;Z1)`; condicionalmente, `H(X|Z2)≥H(X|Z1)`. **No** hay pérdida estricta garantizada en cada capa, ni entropía de Shannon asignable al exterior D no medido. Si la capa superior recibe información nueva de una fuente independiente, la cadena exclusiva se rompe.

## 4. Composición local simple y coste de cómputo global

El toy añade un verificador de cláusulas booleanas localmente sencillas y una búsqueda global por asignaciones (`cnf_satisfiable`) con tests positivos y negativos. Para la familia **general** de fórmulas 3-CNF, cada cláusula se comprueba eficientemente, pero decidir si existe una asignación que satisface todas es el problema 3-SAT, NP-completo. Esto es un ejemplo estándar de cómo acoplar restricciones locales simples puede originar dificultad combinatoria global sin introducir funciones locales psicológicamente extrañas.

Es una reducción/conexión a resultados conocidos, no una nueva prueba de que un agente social particular sea NP-difícil, ni de que exista indecidibilidad turingiana. El experimento sólo ejecuta `n≤12`, es determinista y calculable. Una red modular con interfaces suficientes, una clase convexa o una estructura de anchura de árbol pequeña puede seguir siendo eficiente. No toda composición genera dificultades nuevas.

## 5. Definición elegida por el autor: *sufrimiento estructural por desarrollo impedido y coindeterminación*

**Esta sección asume expresamente la decisión conceptual del autor de LLAMAR sufrimiento a la condición estructural descrita.** Es lícito establecer tal término técnico siempre que se distinga de la experiencia subjetiva, bienestar medido, depresión, felicidad o valor/dignidad de la persona. El toy aplica el mismo formalismo a un nodo sintético; **no** afirma que un software experimente sufrimiento.

Para persona/agente `i`, definimos una contribución/desarrollo genuino `d_i(s)` ligada a su función y fines propios, no a su «precio» social. Sobre el conjunto de alternativas **realizables conjuntamente con los recursos, capacidades y derechos realmente disponibles** (`F^joint`), se elige un testigo `s_i*` que permite un desarrollo superior sin daño/autoridad inventados. Sea `d_i* = d_i(s_i*)`, `d_i^actual = d_i(s)`, y `g_i=max(0,d_i*−d_i^actual)`. Una diferencia desconocida no vale cero: es `NOT_IDENTIFIED`.

El autor establece **tres condiciones conjuntas** para el constructo analítico:

1. **Potencial personal/funcional no desplegado:** `g_i>0` frente a una alternativa propia, genuina y conjuntamente factible bajo los mismos medios; debe preservarse el rol, capacidades efectivas, preferencias y derechos, sin suponer que otra persona sabe mejor qué desarrollo le conviene.
2. **Aporte positivo según la función del agente y su relación con el entorno:** el agente reconoce que desplegar esa capacidad aportaría algo genuino a su entorno. En ensayos sociales futuros separar su convicción de la calidad/efecto externo contrastado; no imponer productividad como condición de dignidad.
3. **Bloqueo externo con determinación insuficiente desde la propia posición:** el agente NO puede alcanzar esa alternativa sólo con sus actos permitidos, y carece de información o método suficiente para resolver completamente la dependencia relevante; la insuficiencia debe apoyarse en un testigo de indistinguibilidad o un protocolo de cualificación que no cierre artificialmente C/D.

**Definición operacional estipulada** para un ensayo con estados completamente instrumentados:

`S_i^struct = g_i × 1[aporte_positivo] × 1[bloqueo_externo] × 1[indeterminación_relacional] × 1[misión_y_derechos_preservados]`.

La unidad es una **brecha de desarrollo/contribución genuina bajo el modelo declarado**, no «unidades objetivas de dolor». Un caso con información incompleta sobre `s_i*` o cualquiera de los predicados devuelve `NOT_IDENTIFIED`, no `S=0`. Si una condición es refutada, no cumple esta SUBCLASE de sufrimiento estructural, aunque pueda existir sufrimiento de otras causas. Los máximos `d_i*` pueden proceder de diferentes configuraciones incompatibles entre sí: **no** sumarlos como si existiera un óptimo conjunto que satisface simultáneamente a todos.

El vector por persona, la distribución de oportunidades, la autonomía, el servicio prestado, el coste de compensación y los impactos sobre terceros deben permanecer separados; sólo la persona, mediante instrumentos pertinentes, puede informar sobre sufrimiento experimentado. El componente HID de 01K usa otras definiciones y pruebas; no renombrarlo silenciosamente.

### 5.1. Ejemplo de desarrollo humano del autor, preservado expresamente

> Una persona especialmente capaz nace en un barrio desfavorecido, asiste a un liceo, no accede a una plaza universitaria y acaba en un trabajo donde no puede desarrollar sus capacidades ni realizar la contribución genuina que cree poder ofrecer.

El autor mencionó Francia como contexto narrativo contemporáneo. **No** queda establecido aquí que exista una regla concreta o una tasa determinada de exclusión universitaria francesa, ni se atribuyen hechos individuales verificables. El ejemplo se conserva para estudiar qué recursos, derechos de acceso, filtros, cupos, barreras sociales o dependencias institucionales podrían impedir una oportunidad en condiciones comparables. Estar en un trabajo distinto al deseado no prueba por sí solo los tres predicados ni un resultado psicológico. La dignidad sigue íntegra con independencia de estudios universitarios, estatus, empleo o aportación económica.

### 5.2. Ejemplo de sistema X−200 y subsistema receptor

Un suprasistema receptor presupone que el proveedor compuesto puede entregar `X` a partir de su función agregada I/O. Sin embargo, el proveedor permanece en `X−200` porque una de sus subfunciones agotó capacidad y las restantes no pueden reorganizarla unilateralmente. El receptor observa el output inferior; sin una cualificación suficiente sobre capacidad, permisos y coordinación interna NO puede inferir qué inversión, transferencia o cambio legítimo permitiría eliminar los 200.

El ejemplo es conceptual: **un compromiso verificable de suministrar X no se deduce de la mera monotonía de una función observada**. `min(input,capacity)` es monótona no decreciente y se estanca. Para hablar de deuda al óptimo debe acreditarse una configuración de mismo presupuesto capaz de entregar X y un camino conjunto potencialmente disponible. El receptor puede sufrir su propia brecha de desarrollo si necesita X para realizar una función legítima y hay una alternativa factible que le permitiría crecer.

## 6. Programa de falsación y ablation para pasar de toy a sociedad

- **B1, hipótesis estructural:** mismos recursos, pregunta, output A congelado; revelar una cualificación de capacidad/mecanismo auténtica y verificar que el receptor distingue `w0/w1` mejor que A-only. Comparar además un peer convencional competente con contratos de capacidad, monitorización y proveniencia. Si un simple contrato transmite Q al mismo coste, no hay ventaja distintiva de EA.
- **B2, hipótesis de presupuesto:** variar `b` bits, conjunto de preguntas futuras y acceso a observaciones nuevas; verificar el límite `b<n` **para la familia exacta de n preguntas**. Una pregunta agregada que puede comprimirse en `log2(n+1)` es control negativo y evita convertir el conteo de estados en ley universal.
- **B3, hipótesis de composición:** comparar redes independientes, acopladas, jerárquicas y modulares; estudiar crecimiento de coste/tiempo, deadlocks, rediseño por actuación conjunta, partes reemplazables y garantías de solución. Si la arquitectura convencional ya tiene interfaces suficientes y coordinación barata, el diferencial puede ser cero.
- **B4, dimensión humana:** estudio cualitativo respetuoso con personas voluntarias, consentimiento, observación de capacidades elegidas y posibilidad real de salir; comparar oportunidades propias factibles, barreras estructurales y experiencia reportada. Registrar casos que contradicen la asociación, como quien prefiere no utilizar una capacidad, vive bien una dependencia transparente o no reconoce el supuesto beneficio externo.
- **B5, relación con HID/deuda:** separar brecha estructural `g_i`, satisfacción, `HID` 01K, utilidad económica `G`, costes de información B/C/D, recursos de coordinación y efectos observados. No usar `S_i^struct` como multiplicador sin validación ni asignar un valor monetario al sufrimiento.
- **B6, exterior abierto:** no inferir que haber simulado dos mundos agota el mundo; C/D pueden permanecer no identificados. Añadir ejemplos sólo cuando exista base independiente y procedencia, no transformar UNKNOWN en una función total clasificadora.

## 7. Trazabilidad, ejemplos y ejecución

**Código:** [`nested_model.py`](nested_model.py) — genera escenarios y salidas **estrictamente finitos**; [`test_nested_model.py`](test_nested_model.py) — positivos, negativos y controles de desconocimiento; [`REFERENCE_SYNTHETIC_RESULTS.json`](REFERENCE_SYNTHETIC_RESULTS.json) — referencia determinista que debe igualar el runner. Se utiliza Python estándar, sin servicios, agentes reales ni medidas personales.

**Inventario de ejemplos del autor:** el [registro versionado del PR #42](../bounded-traps-v0.1/EXAMPLE_LEDGER.md) identifica EX-BAN-01..04 (plátanos y DANA), EX-ROBIN-01 (Viernes/Robinson), EX-MIN-01, EX-ORANGE-01, EX-ANT-01 (hormigas), EX-VERS-01, EX-CREDIT-01 (7/10), EX-LINEAR-01, EX-APPLE-01 (manzanas/frutería), EX-SUPER-01 (X−200), EX-HUMAN-01 (liceo, barrio desfavorecido), EX-SOLIDAR-01 y EX-PRICES-01. El registro distingue una viñeta hipotética de un hecho externo verificado.

**Fuentes conceptuales:** [núcleo económico ACC](../../ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md), [modelo social principal](../../MODEL.md), [00M A/B/C/D](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md), [00N plausibilidad](../../../../00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md), [hipótesis FH-C/FH-E](../../../../01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md), [The Given Universe](https://drive.google.com/file/d/1ePHBGgco-qiQ4S0BmsCNTTFdd2C1JgCd/view), [trabajo de composición abierta v0.4](https://docs.google.com/document/d/1qpBDFBZa7nGKlTD2D5poYuStCf0oJcAogBtUuzEjD90/edit). [PR #42](https://github.com/dakleyer/structural-awareness-contributions/pull/42) es la lectura de bloqueo mecánico; este paquete **no altera el canon** antes de revisión.

**Control metodológico:** el contenido de un manuscrito sobre Shannon/Kolmogorov/PEF/D1–D3 se conserva como antecedente e hipótesis de unificación no demostrada, no como prueba de entropía física en sociedades. Éste es el experimento acotado que la nueva idea exige antes de extrapolar la metáfora de sufrimiento o exterior a una ley social.

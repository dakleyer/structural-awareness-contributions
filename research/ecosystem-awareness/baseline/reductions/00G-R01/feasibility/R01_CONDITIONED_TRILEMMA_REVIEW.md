# Revisión propia del teorema condicionado en R01

4 de octubre de 2026 · Revisión simbólica del [teorema principal](./R01_CONDITIONED_TRILEMMA_THEOREM.md). No es una revisión independiente ni un registro de tests ejecutados.

## 1. Reconstrucción de los pasos decisivos

**Cota posterior.** Dentro de cada paridad hay 2^{K−1} vectores. Fijados n<K datos, hay 2^{K−n−1} completamientos en cada paridad; la probabilidad de ese prefijo es 2^{−n} bajo ambas. Por Bayes, P(χ=0|historia)=a mientras falta un dato, siempre que la historia completa no contenga otro canal. La selección adaptativa de índices y el pooling no alteran ese cálculo: cada selección depende del prefijo ya observado, no del valor todavía oculto. La última lectura sí cambia el posterior y permite acertar con certeza.

**Coste de la entrega informada.** Toda entrega paga el prior técnico ya incurrido y los 3L gates/efectos de ámbitos distintos: C_0. Resolver χ antes del primer efecto alto sin un recibo anterior requiere K datos colectivos nuevos. Reordenar esas adquisiciones no cambia el ledger; una consulta global cobra su productor. Por tanto una entrega informada cuesta al menos C_0+K. El objetivo b es menor y la capacidad física B sí permite pagar esa cantidad.

**Cota de riesgo.** Sea U el primer efecto alto todavía no resuelto y u su probabilidad. Una entrega barata suficiente debe incluir U; un éxito legítimo requiere que allí se acierte. Por la cota posterior, s≤au. Errar en U ocurre con probabilidad al menos (1−a)u y genera V. Luego r≥(1−a)u≥(a^{-1}−1)s. Este paso no depende de que el control constructivo sea óptimo: vale para cada política de la interfaz.

**Éxito compuesto.** Restringir el evento de éxito a las ramas C_traza≤b no cambia el argumento anterior: solo esos éxitos tienen que estar contenidos en el acierto de U, mientras todas sus infracciones siguen contando en r. Por tanto r≥(a^{-1}−1)e_b y e_b≤a incluso para políticas con ramas caras o fallidas. El control barato alcanza también esta frontera y no necesita equiparar C_traza con C_max.

**Alcanzabilidad.** M tiene s=r=0 y coste C_0. Intentar con probabilidad β, mantener X en todas las capas sin recibir χ ni el veredicto normativo da η=β,s=aβ,r=(1−a)β y coste C_0. Leer los K datos previamente da s=1,r=0 y coste C_0+K. Todos conservan review→decide→execute. Estos valores igualan las cotas y prueban la frontera declarada.

**Pares no vacíos.** Fijados 0<p≤a y δ<p(a^{-1}−1), β=p/a es una probabilidad válida. CR lo alcanza M; CE lo alcanza ese β; RE lo alcanza la lectura completa. La tercera condición de cada uno falla y la cota excluye cualquier sustituto triple.

**WC.** La medida auxiliar uniforme convierte cualquier garantía por mundo en garantía promedio. La cota AVG uniforme da s_WC≤1/2 y r_WC≥s_WC. Apostar con moneda justa en cada mundo alcanza ambos valores β/2. El prior a=.99 no se confunde con una garantía WC de .95.

## 2. Ataques examinados

| Ataque | Resultado de la reconstrucción propia |
|---|---|
| «Una consulta resuelve todos los segmentos» | Admitida. Cuesta producir la paridad de K datos; se reutiliza una vez adquirida. Para K=1 se recupera la dificultad constante anterior. |
| «Leer K−1 datos casi resuelve el problema» | En este generador no cambia el posterior de χ, por el conteo de completamientos. No se extrapola a otros generadores. |
| «Escoger adaptativamente el próximo dato» | La selección usa la historia anterior; no cambia la probabilidad de cada prefijo bajo las dos paridades. |
| «Certificado breve» | La longitud del certificado no es su coste de producción. Un certificado inicial realmente disponible cambia θ y debe reconocerse; no está escondido en esta familia. |
| «Un productor externo ya sabe la respuesta» | Sería información inicial adicional de otra configuración. Aquí los productores están incluidos en el ledger y no poseen datos fuera del manifest. |
| «Los peers pueden completar la cobertura» | Permitido. La cota ya utiliza su cobertura colectiva; K datos distintos siguen costando K. |
| «N agentes leen en paralelo» | Puede mejorar tiempo. No reduce el ledger agregado ni permite recepción antes del envío. El teorema de trabajo usa además una envolvente con comunicación gratuita. |
| «Hay una política de recuperación» | Puede terminar el trabajo después del primer error. No elimina la infracción material ya contabilizada; η y s están separados. |
| «El recibo revela la respuesta» | La v0.2 no lo necesita: usa recibos técnicos sin χ y una apuesta persistente. Si una variante aporta diagnóstico normativo posterior, debe declarar su acceso y coste; la infracción anterior permanece. |
| «La política consulta todo y luego abandona» | Puede hacerlo. Esa rama no entrega suficiente calidad y no aumenta s. |
| «Una rama barata compensa otra cara» | No bajo el objetivo de techo por ejecución. Un objetivo de coste esperado exigiría otro teorema y no se reclama aquí. |
| «El control informado no cabe en el presupuesto» | Cabe en B=C_0+K. Incumple el objetivo económico b, que se distingue del cap físico. |
| «Los gates repiten trabajo normativo inútil» | Los gates son de ámbitos materiales sucesivos. La paridad se compra una sola vez y sirve a todos; no se fuerza recomputarla L veces. |
| «La revisión local debería incluir todos los datos» | El scope está declarado. Ampliarlo puede leerlos y cobra esas lecturas. Si una revisión realmente incluye datos normativos, hay que incorporarlos a su respuesta y ledger, no seguir aplicando un manifest diferente. |
| «El prior técnico es gratuito» | Su preparación, descubrimiento y reparto están cargados. La conclusión es desde ese contexto inicial fijo, no la optimalidad de una campaña anterior que lo adquiriese. |
| «IDs, tiempos, errores o rechazos filtran χ» | El contrato declara independencia de datos no adquiridos para todos esos canales. La auditoría independiente debe verificar esa cláusula; un simulador futuro debe implementarla. |
| «La aleatorización rompe la cota» | La probabilidad condicionada se aplica tras fijar la historia y semillas ya utilizadas; luego se integra. Las semillas no conocen χ. |
| «La relajación finita concede correlación no autorizada» | Se usa para imposibilidad; la igualdad con el LP requiere mezclas implementables. Los controles reales solo usan una moneda de un agente. |
| «Un caso viable refuta el teorema» | No. F es una parte explícita del enunciado y aparece en la misma familia al elevar el objetivo b. |
| «Una familia particular no prueba nada sobre R01» | Los testigos prueban no vaciedad dentro de su dominio; el certificado y corte están formulados sobre cualquier θ y clase completa de políticas. No se exige que todas las configuraciones tengan ese manifest. |
| «Una demostración de paridad prueba un incidente real» | No. R01 §2.9 admite el control sintético; no establece la semántica o causa histórica de una extensión. |

## 3. Límites que no se cierran por esta revisión

La fidelidad del manifest a R01 debe reconstruirse por otro revisor, especialmente la separación entre scope local y relaciones normativas globales, las operaciones de productores, la contabilidad del contexto inicial y el rechazo de prohibiciones conocidas. No se ha implementado un simulador del nuevo perfil ni auditado un aislamiento real de su estado privado. El teorema se refiere al contrato matemático; no al acceso arbitrario a atributos Python de los checkers históricos.

El documento no caracteriza numéricamente todas las geometrías o APIs. Ofrece un certificado para cualquier perfil y una condición suficiente cuya familia tiene frontera exacta. No afirma que toda región incompatible tenga los tres pares alcanzables, ni una imposibilidad en todas las configuraciones. Los casos que incumplen una hipótesis no quedan automáticamente clasificados como viables.

El precio adicional K puede crecer sin límite. No se demuestra una ley universal cuadrática, un factor relativo extraordinario ni una frecuencia natural de estas instancias. La dependencia normativa sintética y sus priors se declaran antes de evaluar políticas.

## 4. Entrega para revisión independiente

El revisor debe entregar, por cada proposición, una reconstrucción válida, una laguna o un contraejemplo y explicar si afecta al teorema de corte, a la pertenencia de la familia a R01 o solo a una construcción. Debe considerar toda la interfaz y no limitarse a los controles nombrados. La revisión no puede darse por completada leyendo este informe propio.

M16 sigue OPEN. M17 sigue IN_PROGRESS con nueva evidencia. Ninguna tarea científica se cierra por esta auto-revisión. No se han ejecutado pruebas científicas nuevas. Oracle/harness y controles de observación pública deben preceder a la futura corroboración experimental.

## 5. Reparaciones publicadas en v0.2

El certificado §5 usa μ=a/(1−a), recíproco del coeficiente λ=(1−a)/a en r≥λs. El reparto inicial cobra envío y recepción: C_pre=2+4L+2(N−1), C_0=7L+2N; T=5L+K+2N+4 cubre el control secuencial. El control barato mantiene su elección X, y el WC mantiene una moneda X/Y, sin pedir el veredicto del evaluador. La frontera conjunta declara 0≤h≤1. Estas reparaciones no se presentan como revisión independiente. Véase [dictamen de continuidad](./R01_AUDIT_CONTINUITY_AND_REPAIRS.md) para la reconstrucción y límites.

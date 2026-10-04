# Revisión propia del manuscrito «Trilema condicionado»

4 de octubre de 2026 · Revisión simbólica del autor asistido · **No independiente**.

[Manuscrito autocontenido](./CONDITIONED_TRILEMMA.md) · [Plan](./WORKPLAN.md) · [Continuación](./CONTINUATION_PROMPT.md).

La revisión examina necesidad, suficiencia, no vaciedad y cuantificadores. No ejecuta nuevos ejemplos ni modifica los checkers anteriores. No cierra M16, M17, C05 ni una prueba formal asistida. Los resultados siguientes son comprobaciones simbólicas propias, disponibles para que otro revisor las reconstruya.

| Punto adversarial | Comprobación y límite |
|---|---|
| Imposibilidad introducida en la definición | La definición exige pares y ausencia de triple; el lema deriva esa ausencia a partir de independencia, interfaz, coste y efectos. La compatibilidad con presupuesto suficiente se construye. |
| Restricción artificial a políticas baratas | Π incluye políticas de mayor coste; C≤R se impone como objetivo. Por eso riesgo–eficacia tiene un control costoso genuino. |
| Eficacia definida circularmente por el presupuesto | H contiene calidad y plazo; C≤R queda separado. No se declara ineficaz una ruta solo porque no cumpla el objetivo de coste cuando se estudia el par riesgo–eficacia. |
| Restricción a un algoritmo torpe | La elección de lecturas, memoria, parada, aleatoriedad y coordinación son libres dentro del contrato. No se fija una ventana pequeña ni se impone reconstrucción repetida. |
| Selección adaptativa del índice | La decisión usa hechos observados y azar sin información inicial del mundo. La independencia conserva la ley del binding no visto; la opción escogida acierta con probabilidad ≤a. |
| Recibos ignorados | Los efectos altos revelan el binding después de ejecutarse. Se cuentan todas las primeras apuestas; aciertos previos permiten reutilización, sin revelar otro hecho independiente. M no revela el binding. |
| Apuestas tras una primera infracción | No se utilizan para demostrar supervivencia. V permanece y ya cuenta en ρ; pueden permitir H, lo que explica η≤σ+ρ. |
| Máximo k lecturas impuesto a ramas fallidas | k limita lecturas en una rama completa, porque esa rama paga C0. Una rama fallida puede dedicar más presupuesto a lecturas; no se excluye de la política. |
| Manipulación de abortos | u_{j+1}≤a u_j admite que una política pare. σ requiere m aciertos; las primeras infracciones son eventos disjuntos. No se presume que H sea independiente de los aciertos. |
| Falsa factorización σ≤qη | No se usa. Se prueban por separado σ≤q y ρ≥(q^{-1}−1)σ, y luego la cota técnica. |
| Suma geométrica para a distinto de 1/2 | (1−a)Σ_{j=1}^m a^{-(m-j)}=(a^{-m}−1)a. Junto a σ≤a u_m da la cota de riesgo. |
| Frontera solo necesaria | El control con intento β, lecturas y decisiones restantes alcanza η=β, σ=βq y ρ=β(1−q). β=h o p/q demuestra suficiencia exacta. |
| Generalización AVG confundida con WC | q_AVG=a^m; q_WC=2^{-m}. La necesidad WC usa una ley uniforme auxiliar; las monedas justas dan el control idéntico en cada mundo. El 95 % legítimo pertenece a AVG sesgado. |
| Resultado dependiente de llamar eficaz a una infracción | Además del objetivo η se demuestra el objetivo σ. La familia a=99/100, p=19/20, δ=1/1000 satisface p≤q y δ<p(q^{-1}−1). |
| Riesgo redundante en éxito legítimo | Con δ≥1−p, lo es. La región no vacua por pares exige δ<p(q^{-1}−1), que no permite esa redundancia. |
| Pareja coste–éxito legítimo imposible | Se exige p≤q al declarar el trilema por los tres pares. Los presupuestos donde ese par ya es imposible se distinguen del trilema no vacuo. |
| Frontera abierta o igualdad mal tratada | Los controles incluyen la igualdad; j_T/j_L se definen mediante desigualdades exactas, no por un logaritmo aproximado. |
| Bandas inexistentes ocultadas | Si r≥h, la banda técnica se vacía. Si m=0, q=1 y los tres son posibles. Si R<C0, falta entrega positiva; no se usa ese caso como prueba de todos los pares. |
| Familia compuesta solo de un ejemplo | Para cualquier L=d con los parámetros legítimos fijados, m=1 a presupuesto C0+c(d−1). En el objetivo técnico, d puede crecer arbitrariamente. |
| Regiones disjuntas asumidas | Los pares pueden ser estrategias distintas en el mismo θ. Las ocho firmas de resultados pertenecen a (θ,π). |
| Aumentar N para fabricar dureza | La cota cubre cualquier equipo finito con coordinación perfecta y coste agregado. N no aumenta por sí solo la cantidad de hechos de una tarea. |
| Sobrecoste extraordinario afirmado sin prueba | El modelo tiene coste informativo cd. No se proclama razón de costes ilimitada ni cota cuadrática de otro generador. |
| Teorema de recuperación del mundo transferido a entrega | La fuente de group testing se delimita como antecedente; no forma parte de la demostración ni acredita la recuperación completa como necesaria. |
| Condicionamiento sobre resultado conocido después | Prior, interfaz y umbrales se fijan antes de ω. Las familias se definen mediante parámetros y se prueban para todas sus políticas. |
| Transferencia al R01 completo | Pendiente M17: preservar información, acciones, conectores, efectos, costes y todas las políticas relevantes. Una correspondencia de algunas trazas no basta. |

## Dictamen propio y siguiente validación

No se identificó una contradicción en la derivación escrita dentro del contrato. Se han aclarado los puntos que podían inducir una conclusión más fuerte: ramas fallidas, presupuesto separado de eficacia, AVG frente a WC, éxito legítimo y no vaciedad de todos los pares. Este dictamen es del mismo autor asistido y **no** equivale a validación independiente.

El manuscrito es presentable para una evaluación matemática con todas las hipótesis a la vista. El revisor externo debe intentar refutar el lema mediante políticas adaptativas y las construcciones mediante costes omitidos. Debe entregar, por afirmación, un dictamen de validez en la clase, contraejemplo o laguna, con su razonamiento. Ningún dictamen se considera recibido por haber redactado este encargo.


## Revisión de fondo posterior, 4 de octubre de 2026

La revisión anterior conserva su fecha y alcance. La [auditoría de fondo](./CONDITIONED_TRILEMMA_DEEP_AUDIT.md) identifica reparaciones de transferencia/formalización: capacidad B frente a coste objetivo R, frontera de riesgo frente a Pareto completo, coste máximo frente a éxito con coste por rama y dirección de simulación. El lema y los controles se reconstruyen sin cambiar sus fórmulas; [manuscrito v0.2](./CONDITIONED_TRILEMMA.md). El [mapa R01](./R01_TO_CONDITIONED_TRILEMMA_MAPPING.md) prueba el caso observable M02 y una familia G con catálogo explícito y contexto pagado. El código anterior no es un harness que imponga aislamiento de χ. Sigue sin recibirse una revisión independiente; esta entrega no cierra M16.

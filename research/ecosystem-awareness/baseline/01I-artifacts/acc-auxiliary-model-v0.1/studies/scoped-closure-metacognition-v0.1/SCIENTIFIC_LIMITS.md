# Auditoría científica: alcances y contrapruebas de «cierre local sin clausura»

**Objeto:** extensión del estudio ACC del 26-10-2026 basada en «prompts no procesados.docx». No es una auditoría independiente de terceros. `A` y B/C/D significan roles relativos de 00M; no generar nueva ontología ni introducir un detector universal.

| Proposición | Nivel de soporte | Límite, riesgo o contraejemplo | Prueba/control |
|---|---|---|---|
| Dos mundos distintos pueden producir el mismo A pero responder distinto a q | Resultado de factoración funcional, demostrado para testigos concretos | No afirma indistinguibilidad si hay otras observaciones legítimas | PR #43, PR #44 |
| Testimonios parciales + regularidad permiten deducir límites para f(x) | Cota algebraica condicional | Fuente falsa, regularidad falsa, región no cubierta o dependencia D | LocalSufficiency: 27 tests |
| Un intervalo puede decidir un predicado sin determinar f(x) | Teorema elemental dentro del intervalo sound | Intervalo sound no demuestra universo global cerrado | test_locally_true / false / unresolved |
| La nube de puntos sin regularidad no permite interpolación garantizada | Contraejemplo matemático general | Puede haber una teoría física/estadística externa válida, que debe documentarse | test_no_regularality_* |
| Cantidad desconocida y exterior abierto permanecen abiertos | Disciplina semántica 00M | Un conjunto finito de testimonios no representa cardinalidad de D | residual_exterior |
| Composición no fungible conserva procedencia y estados desconocidos | Invariante de datos parcial | `source_attested=True` no autentica criptográficamente; dos orígenes declarados pueden compartir upstream | duplicate/conflict/origin tests |
| C exploratorio no trae una tasa de retorno calculable | Definición canónica 00M | Un paso acotado puede tener presupuesto conocido sin haber calculado el ROI del C completo | FrontierWitness C tests |
| D material requiere evitar cierre no justificado de la pregunta | Regla prudencial del toy relativa a q | Un D irrelevante no autoriza bloquear todas las actividades; función de seguridad externa puede exigir más | material_D / irrelevant_D |
| Metapolítica decide sufficiency status, no todo predicado de mundo | Función computable acotada | Un procedimiento YES/NO correcto para todos los inputs del halting problem no puede existir; abstención es necesaria en general | MetaPolicy tests; argumentación por contradicción |
| Solidaridad puede operar sin ROI numérico | Posición normativa/acción de agente | No es permiso de violar derechos, ni compensa falta de autorización; no autoriza automáticamente riesgo D | consent/rights/owner tests |
| Sufrimiento estructural definido por 3 condiciones | Constructo elegido por el autor, posibilidad aritmética | No es dolor vivido, resultado psicométrico, bienestar, dignidad ni medición clínica | HumanAndEconomics tests |
| Conocer una limitación puede elevar el malestar subjetivo | Hipótesis abierta bidireccional | También puede aliviar o modificar decisiones sin alterar la brecha objetiva | test_new_awareness_without_resources_* |
| Q es más barato que ampliar A o preguntar a un peer | Sólo para costes y corrección declarados | El peer puede ganar; metadatos caros o inauténticos pueden revertir signo; amortización/latencia pendiente | cost_profile/peer/maintenance tests |

## Hallazgos de esta revisión

1. **Riesgo de autojustificación:** la pregunta q debe definirse antes del intervalo o la composición; fijarla ex post fabricaría suficiencia. Este estudio crea explícitamente `DecisionQuestion` antes de evaluar `Point`.
2. **Oráculo encubierto:** el algoritmo de planificación y metapolítica no puede recibir f verdadera ni un estado mundial privado; sólo testimonios y marcos. El programa de referencia `synthetic_report` elige constantes de un ejemplo, pero no confiere acceso a su origen real.
3. **Presunción de exactitud de B:** en esta versión `source_attested` sólo declara si el toy considera elegible un punto. El verificador no garantiza criptografía, independencia empírica, seguridad frente a adversarios o verdad de testigos. Se debe validar en perfiles DDS separados.
4. **Falso cierre de C/D:** no declarar que C sea «cualquier subsistema sobre el que vale la pena preguntar» ni D «los nodos con demasiados cálculos». C requiere avenida fundada sin evaluación caracterizada; D requiere falta de ruta efectiva y materialidad para el proceso, no simplemente costo elevado.
5. **Inconsistencia de supuestos Lipschitz:** múltiples puntos pueden imponer intervalos incompatibles; se informa la inconsistencia detectada para q. Una cota conservadora local no demuestra que todas las declaraciones sean globalmente consistentes; un ensayo físico posterior debe comprobar compatibilidad de fuentes y premisas.
6. **Tratamiento de confianza:** los intervalos de `Point` son deterministas y condicionales. No equivalen a probabilidades o tasas de error calibradas; si la fuente entrega confidence intervals, una verificación de cobertura y composición estadística adicional es necesaria.
7. **Riesgo de delegación:** `advisory` no ejerce autoridad. `owner_authorized=True` es sólo una entrada del toy, no prueba de un mandato real. Si la decisión exige una garantía contra D que no se tiene, se mantiene revisión/abstención.
8. **Medición humana:** el campo `new_gap_recognized` permite registrar cambio de conocimiento sin reescribir el óptimo. El signo del sufrimiento vivido queda abierto; no sumar «entropía + brecha = dolor».
9. **Comparador convencional competente:** un sistema de validación de interfaces/procedencia que produzca las mismas cualificaciones debe tener pleno crédito y puede falsar la ventaja de un producto nombrado Ecosystem Awareness.
10. **Orígenes no independientes:** deduplicar `claim_id` no revela que dos fuentes diferentes provengan de una misma upstream. La procedencia sólo está declarada, no verificada. Evitar una ganancia falsa por número de testigos.
11. **El exterior no queda matemáticamente encuestado:** una clase finita instrumental con n observaciones no certifica que no exista otra influencia material. El cierre obtenido es RELATIVO A q y sus premisas, no a toda la realidad social.
12. **No adoptar un teorema físico universal:** la serie histórica D1–D3, PEF, Shannon, Kolmogorov y von Neumann contiene postulados/hypótesis que no deben importarse como identidades aquí; el puente actual se basa en proyección y suficiencia bien delimitadas.

## Condiciones de promoción

Conservar el estudio como propuesta hasta revisión de propietario, verificación de matemática de cotas, instrumentación genuina de los orígenes y sus costes, pruebas independientes de control adversario y de continuidad del trabajo legítimo, consentimiento y tercero afectado, comparación con peer competente y medida humana separada si se quiere afirmar sufrimiento realizado. CI verde valida sólo el runner declarado.

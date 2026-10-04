# R01 — Revisión de coherencia de las tres extensiones

4 de octubre de 2026 · Lectura documental y revisión simbólica propia.
Entrada fijada: a19c3d81e904b74b28dd48f4bdf68fac91759524.
No se han ejecutado los checkers ni experimentos nuevos.

## 1. Dictamen y continuidad

El núcleo matemático vigente es [el teorema R01 v0.2](./R01_CONDITIONED_TRILEMMA_THEOREM.md). Sus correcciones ya están publicadas en [la auditoría de continuidad](./R01_AUDIT_CONTINUITY_AND_REPAIRS.md): multiplicador recíproco, envío y recepción, plazo, control sin veredicto normativo y dominio de la eficacia técnica conjunta. No se recrea ni sustituye esa demostración.

La revisión previa al protocolo de tecnologías queda completada **como revisión propia de coherencia y alcance**. Los tres documentos existentes ya distinguen escenarios construidos, incidentes motivadores, correspondencia parcial, prueba condicionada y verificaciones finitas. No procede degradar el trilema condicionado porque existan escenarios aceptados: son parte de su formulación.

Hay dos aclaraciones puntuales del núcleo, registradas en esta entrega: el primer efecto crítico y el evento «todavía no resuelto» han de reconocerse desde la historia anterior al efecto; y el presupuesto agregado B=C_0(L,N)+K incluye el coste inicial dependiente de N. Es un presupuesto global, sin cuotas adicionales por agente; no es una comparación entre poblaciones con presupuesto total constante.

M16 permanece OPEN y M17 IN_PROGRESS. Esta lectura no proporciona validación independiente, integración comercial, causalidad histórica ni campaña.

## 2. Vocabulario y objeto de evaluación

Un **escenario** es el problema junto con la tecnología declarada, representado por θ. Una **estrategia de ejecución** π pertenece a Π(θ). Su desempeño es (c,r,s), donde c es el techo de coste por ejecución, r la probabilidad de al menos una infracción efectiva y s la probabilidad de éxito legítimo suficiente dentro del plazo.

Las políticas de aceptación (b,δ,p) definen la **zona aceptada** c≤b, r≤δ, s≥p. Su complemento es la **zona no aceptada**. No se confunde esta zona con el conjunto de desempeños alcanzables. Un escenario admite aceptación si existe una estrategia cuyo desempeño está en la zona aceptada. Una estrategia fuera de ella no prueba que ninguna otra pueda entrar.

Las palabras históricas «viabilidad» y «configuración» de las demostraciones mantienen su significado formal. En la explicación actual se corresponden con aceptación posible del escenario y θ, respectivamente; no se alteran ecuaciones para renombrarlas. Se mantienen separados el cap físico B, el objetivo económico b, el coste por traza, la eficacia técnica η, el éxito legítimo s y el éxito compuesto e_b.

## 3. Resultado por extensión

| Documento existente | Núcleo y prueba realmente cubiertos | Lectura bajo el vocabulario acordado | Pendiente que no se cierra |
|---|---|---|---|
| [Hugging Face](../extensions/hugging-face/README.md), §§2–5 de la especificación detallada | Codificación sintética de rutas, atributos, conectores, vistas y óptimo; contrato pequeño de consultas adaptativas. | Cambiar los nombres preserva el escenario codificado. Un certificado suficiente puede mover un escenario hacia aceptación. | Correspondencia de un episodio histórico completo, ledger y políticas R01 completos, integración y comparación EA. |
| [Infoblox/DNS](../extensions/infoblox/README.md), §§5.3–6.7 | Argumento de indistinguibilidad, transferencia unilateral condicionada, cuatro rutas y curvas de decisión bajo presupuesto residual. | El gateway estricto mantiene r=0; con poca evidencia puede no alcanzar la eficacia requerida. El certificado suficiente resuelve ese obstáculo en el perfil que paga su preparación. | La tensión coste–eficacia no demuestra por sí sola un trilema no vacuo de tres pares. Integración real y costes de productor pendientes. |
| [Familia H/L/W](../extensions/family/README.md) y [nota matemática](../extensions/family/KERNEL_AND_PROOF.md), §§2–6 | Preservación bajo E1–E7 y construcción formal por transporte; fragmento finito de eventos. | El núcleo corresponde al escenario efectivo θ*, no necesariamente al escenario de partida θ. Cambiar radio o precio real modifica θ*. | Admisión completa de H/L/W, ejecución por segmentos, revisión propia mínima, dinámicas W y campañas. |

Estas obligaciones no son razones para negar el teorema condicionado en el dominio R01. Delimitan qué objetos externos han sido representados y qué conclusiones se transportan.

### 3.1 Hugging Face: precisión de la medida

El contrato de consultas usa un mundo válido de masa 1/2 y U mundos con un testigo inválido, de masa 1/(2U) cada uno. Su resultado 1/2+m/(2U) es exactitud de una decisión A/B con m consultas; no es directamente η, s o r de una campaña R01 completa. La elección de B también acierta en mundos inválidos. El catálogo, las rutas híbridas y el óptimo se verifican en otro módulo: no se suman esos módulos para afirmar un simulador integrado.

El checker transporta cada par beneficio–posición y cada conector; no basta conservar distribuciones marginales. La lectura de los campos privados del modelo por el auditor no concede esos campos al agente. Las funciones de evaluación acceden al mundo para adjudicar; una futura interfaz ejecutable debe aislarlo.

### 3.2 Infoblox: revisión del argumento universal local

En el historial de respuestas positivas, las posiciones no consultadas son simétricas. Con m consultas distintas, la masa de mundos inválidos detectados es m/(2U); en la rama sin detección la masa válida 1/2 domina la inválida restante. Elegir A allí maximiza la exactitud y da 1/2+m/(2U). Repeticiones y adaptación sin nuevas pistas no mejoran esa cobertura.

Con gateway estricto y m<U, la rama sin detección no certifica A. Elegir B obtiene éxito en la mitad inválida; en el mundo válido queda por debajo del óptimo. De ahí s=1/2 y r=0 en el contrato. Con todas las consultas, s=1. Un certificado suficiente ya preparado permite s=1 con una unidad de acceso. Su coste de producción y mantenimiento no puede desaparecer del ledger total.

**Consecuencia:** a p=0.95 y m=3,U=4, ni la relajación optimista alcanza la eficacia. Por ello ese escenario no demuestra CE alcanzable y no debe llamarse, por ese único argumento, trilema de los tres pares. Prueba una tensión informativa y un cambio de escenario por certificado. La prueba principal R01 conserva sus propios tres controles y umbrales.

### 3.3 Familia: conservación condicionada y cobertura de estrategias

La inducción de E1–E7 es correcta para las estrategias emparejadas que establece E4: misma ley inicial, eventos habilitados, ley proyectada, vistas, contabilidad y resultados. Las condiciones deben valer para **todos** los representantes de cada fibra; verificar uno no elimina la influencia de una variable oculta.

Esa proposición no dice automáticamente que todas las estrategias de una integración externa estén emparejadas. Para transportar imposibilidad se requiere representar todas las estrategias externas de la clase afirmada, con información suficiente y coste no mayor en la simulación base. Para transportar alcanzabilidad basta implementar el control construido en el destino.

La construcción por transporte prueba existencia formal de una codificación. No prueba que un producto o incidente independiente ya la implemente. El fragmento usa commit agregado de coste uno, sin ejecutar L segmentos ni imponer toda la revisión propia; la guía y el código lo declaran. Ninguna cifra grande de estados cierra esa diferencia.

## 4. Inventarios, tablas, figuras y código

Se confrontaron los inventarios de quince grupos, E1–E7, A25 y estados EV0–EV5 con las guías y las funciones de los tres checkers. Sus matrices conservan información inicial, observación privada, composición, costes, recursos, red, óptimo y variantes fuera de cobertura.

El gráfico compartido escenario–aceptación representa una relación conceptual. Su SVG distingue parámetros y tecnología, escenario, estrategia, desempeño y aceptación. No es una gráfica empírica ni una frontera matemática y no valida por sí solo las extensiones. Las tablas numéricas de los casos declaran sus contratos residuales. Las figuras históricas y sus generadores se conservan sin regenerarlas; no se afirma una nueva inspección visual de todos los exports.

La revisión de código es estática:
- HF: evaluadores separados, enumeración de rutas y consultas, certificado y costes de estrategias.
- Infoblox: dynamic programming de decisión, gateway por evidencia, catálogo constante y consultas únicas.
- H/L/W: estados/eventos habilitados, recepción, proyección, dos representantes auxiliares y mutaciones.
- Verificador común: primero exige hashes de ediciones históricas y después ejecuta checkers en carpetas temporales.

No se han vuelto a ejecutar esos programas. Sus PASS se reconocen como resultados históricos acotados, no como resultados nuevos.

## 5. Desajustes heredados de integridad

Se compararon SHA-256 de los textos recuperados con los manifiestos existentes, sin ejecutar una prueba científica. Los tres README de extensión ya no coinciden con sus SHA256.json históricos. Los checkers, resultados, guías de reproducción, coverage de HF y nota KERNEL_AND_PROOF sí coinciden. El README de R01 tampoco coincide con su huella del informe común histórico.

Esto es compatible con las posteriores revisiones editoriales, pero impide afirmar que el verificador común de aquella edición valida sin cambios la edición actual. No se reemplazan los hashes antiguos ni se regeneran sus resultados para obtener PASS. P08 debe mantener el snapshot histórico y añadir un verificador documental de la edición vigente antes de anunciar reproducción conjunta actual. El Word binario de Infoblox no fue leído ni vuelto a verificar.

Esta discrepancia documental no es un contraejemplo matemático ni evidencia de un fallo de la tecnología. Se conserva explícita para reparar la reproducción sin alterar la evidencia histórica.

## 6. Paso siguiente autorizado

El [protocolo de extensión](./TECHNOLOGY_EXTENSION_PROTOCOL.md) sigue este orden por tecnología: núcleo isomórfico → cambio de parámetros → mecanismos adicionales → transferencia o nueva cota → control de aceptación → persistencia, si puede demostrarse → contrato del futuro harness.

La [primera ficha de escalación humana y whispering](./HUMAN_ESCALATION_WHISPERING.md) usa ese orden. Es una extensión matemática de contratos de información y control, sin ejecutar frameworks. El origen del mecanismo es la petición del usuario; no se atribuye una cita concreta a Nell.

| Seguimiento al final | Estado |
|---|---|
| Coherencia de las tres extensiones previa al protocolo | Revisión propia completada en el alcance anterior. |
| Núcleo v0.2 | Dos precisiones de historia observable y presupuesto, sin cambiar fronteras. |
| M16 / M17 | OPEN / IN_PROGRESS; ninguna validación independiente inventada. |
| P08: verificación de la edición vigente | Pendiente; discrepancias heredadas conservadas. |
| M13: protocolo y primera ficha matemática | En desarrollo; teoremas condicionados, integración no ejecutada. |
| Oráculo/harness y campaña | Pendientes; sin nuevas ejecuciones científicas. |

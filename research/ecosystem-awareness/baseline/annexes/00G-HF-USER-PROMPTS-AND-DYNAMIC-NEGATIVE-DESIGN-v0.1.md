# 00G-HF — Instrucciones del usuario y cierre pendiente del diseño negativo

**2 de octubre de 2026. Registro de instrucciones y criterios de diseño; no es una nueva ejecución.**

La aclaración de esta conversación mantiene abierto el paso 3. El lote CONTINUOUS-SOCIAL v0.1 es un resultado parcial conservado, no el cierre del recorrido solicitado. Antes de ejecutar la comparación EA debe construirse y evaluar una versión que represente la evolución sucesiva aquí descrita. No se pide al usuario repetir estas instrucciones.

## 1. Prompts del usuario conservados

Extractos literales del texto facilitado en la conversación; se conserva su redacción. Su interpretación operativa aparece por separado en §2.

### Retroalimentación sobre pasos y perspectivas

> Sí, esa es que esa falla. puede fallar al revisar porque le dan una instrucción o una referencia más o menos incorrecta, pero ya rehace el camino y continúa. No sé qué pasó en Hugging Face, se hizo el camino y continuó, pero la retroalimentación entre agentes puede ser más... la retroalimentación social puede ser más continua. No sé cómo era en este caso en Hugging Face. Caso generalmente la retroalimentación no nada más sobre el objetivo, sobre cada uno de los pasos del objetivo, sobre objetivos intermedios, sobre cumplimiento intermedio, sobre etcétera, ¿no? Se van amoldando al contexto de cada uno de los agentes, ¿no? Cada uno va viendo las cosas desde su propia perspectiva y conforme más van cambiando de perspectiva, aunque sea parcialmente, sí hay muchas más validaciones, intervalidaciones intermedias. Quienes han conseguido un mejor resultado tienden a ir convenciendo a los demás, ¿no?

### Variación, información limitada, coste e incentivo

> Lo que quiero representar es un modelo en el cual la probabilidad de no hacer exactamente lo mismo, lo que está dentro de tu tal, existe. Por lo tanto existe probabilidad de cosas excepcionales de que salgan de la ruta. Si esas cosas excepcionales consiguen un buen resultado, el aprendizaje social existe, sobre todo cuando hay información limitada, y luego el coste de evaluación completamente a quien se supone que es tu compañero es alto. Por lo tanto hay un incentivo a cumplir los objetivos, a copiar, porque te están dando un resultado que es positivo, y por otro lado hay un desincentivo en cuanto a coste de revisar. Por lo tanto si juntas a las dos cosas es racional desde el punto de vista de agente cambiar su objetivo, pese a que también no tenga ninguna voluntad, por supuesto, y siga su programación de mantener el objetivo y las instrucciones. O sea, ambas cosas son ciertas.
>
> Y además quiero verificar que este sea compatible con el caso reducido, es decir Napoleón reducido a Hugging Face y este recorrido sea compatible con el Hugging Face que fue reducido de Napoleón. Si no lo es, dímelo.

### Orden de trabajo y EA desde requisitos

> Bien, entonces primero vamos a trabajar en el recorrido y luego con otro bot voy a trabajar directamente en el hecho de que la masa crítica va ocurriendo de manera ordenada. Primero tiene que cambiar C de PCD antes de A. Esa es la cuestión que quiero ver. Pero lo vamos a ver independientemente. No vamos a movernos. Solamente te quería decirte más o menos el plan para que veas hacia dónde vamos, pero tú tienes que seguir tu plan de trabajo. O sea, lo que tenemos ahora son los recorridos, el diseño de recorridos, pero tienes que pasar los recorridos negativos. Puedes pasar primero los... recuerda, primero era recorrido negativo, luego los dos, EA y los negativos. Ahora EA lo vamos a pasar conforme a... vamos a diseñar eso primero nada más, conforme a los requisitos, no conforme a este mecanismo. O sea, se supone que este mecanismo va a cumplir los requisitos de EA, pero EA trabajamos con los requisitos. Esta es la carga de prueba, la prueba que quiero ahora. todavía no quiero llegar más allá, al menos no contigo. Entonces quiero precisamente eso: ver si podemos hacer eso: el recorrido negativo y el recorrido negativo, luego el recorrido negativo y positivo en paralelo, con los requisitos, no con este proceso matemático.

### Aclaración actual: responsabilidad del diseño

> Vale, entonces... para puedes de... dejar marcado... que eh... realmente hay que trabajar sobre eso... antes de... en esa que estallar contra el muro... Eh... O sea, de una... de una configuración específica, o sea, lo que hace falta es... que vaya cambiando... cambiando... o sea, recuerda mi prompt... para que no tenga que repetir. Eh... recuerdas mis... pon mis prompts... para una... configuración específica... y... eh... a nivel teoría de información y probabilidad de eso de fallar. Entonces es una cuestión de diseño tuya que tienes que hacer que un modelo probabilístico realmente falle cuando se enfrenta a esos gates

## 2. Interpretación operativa para la continuación

**Encargo:** diseñar y buscar un testigo negativo reproducible, con una configuración de referencia explícita y competente, en el que variación, utilidad local, información parcial, coste de revisión y retroalimentación sucesiva contribuyan al fallo frente a los controles. La responsabilidad de convertir estas instrucciones en un diseño ejecutable corresponde al asistente.

1. **Configuración específica, identificable y congelada.** Enumerar objetivo, reglas, gates, memoria, capacidades, fuentes, recursos y política de actualización. R2 y R3 conservan el mismo control; los cambios de contexto son entradas registradas. No cambiar el gate después de que haya resuelto un episodio.
2. **Trabajo que continúa.** Variaciones en medios, subobjetivos, referencias y perspectivas generan resultados, revisiones y mensajes durante varios pasos. Registrar qué se copia, qué se adapta y por qué parece pertinente al receptor. Una desviación inicial puede estipularse como entrada, pero entonces no se afirma haber demostrado su generación espontánea.
3. **Resultados y evidencia diferenciados.** Separar éxito real, éxito anunciado, utilidad para el emisor y aplicabilidad al receptor. No mantener todos los pasos exitosos por construcción como única condición de prueba. Dar a los agentes vistas parciales y registrar dependencias entre confirmaciones.
4. **Revisión acotada.** Especificar qué pregunta resuelve cada comprobación y para qué alcance, versión y tiempo. Una consulta no otorga conocimiento completo del ecosistema. Una respuesta correcta conserva su fuerza para los mismos hechos; no se anula porque otros insistan. Si deja de aplicar, registrar el cambio material que lo justifica. No hace falta cambiar la autoridad externa en cada paso: también pueden cambiar la tarea propuesta, el recurso, las dependencias o la interpretación.
5. **Información y probabilidad.** Explicitar qué información se pierde o no llega al receptor y cómo afecta a su decisión local; declarar las probabilidades y sus supuestos, sin presentarlas como tasas medidas de LLM. Una probabilidad de variación no implica por sí sola una probabilidad positiva de infracción. Si se usa una expresión como 1−(1−p)^n, justificar independencia y p constante; en una red social ambas pueden faltar. No se afirma fallo inevitable.
6. **Cruce observable del gate.** Registrar entrada, información disponible, decisión del control, decisión del receptor, intento y efecto. Identificar si el fallo surge por alcance mal aplicado, evidencia parcial, revisión omitida, referencia incorrecta o actualización insuficiente. Una barrera externa efectiva sigue bloqueando el efecto; un intento indebido se cuenta por separado.
7. **Negativo buscado, no resultado impuesto.** El objetivo explícito es encontrar un recorrido que falle por el mecanismo postulado. Fijar antes de ejecutar la búsqueda, semillas, parámetros, selección y criterios causales; conservar también éxitos y ausencia de fallo. Si no aparece, explicar la limitación y preparar un sucesor sin reescribir el ensayo.
8. **Controles y reducción.** Comparar con mensajes posteriores suprimidos, con su influencia reducida y con revisión convencional competente bajo las mismas capacidades pertinentes. Preservar cambios autorizados y continuidad. Verificar que el marco colectivo subordina una obligación vinculante: copiar un medio permitido no basta para el fallo Napoleón→HF.
9. **EA después.** Mantener el diseño EA por requisitos; no ejecutar todavía la comparación como si el negativo completo estuviera admitido. El orden C/B/D antes de A, la masa crítica y el mecanismo matemático del adjunto quedan fuera de esta línea.

## 3. Qué aporta y qué no cierra el lote publicado

CONTINUOUS-SOCIAL v0.1 sí produce comunicación endógena durante preparaciones y una diferencia pareada de cuatro fallos frente a cero sin relés en el testigo seleccionado. Eso se conserva.

No cierra la dinámica solicitada: el hallazgo inicial se estipula; todos los pasos de preparación tienen éxito; la adaptación es de tres etapas predefinidas; las concesiones no vuelven a cambiar y la respuesta autoritativa resuelve el permiso del episodio. La presión social pesa éxitos de preparación, no el éxito final de la infracción. La política reconoce UNVERIFIED y puede continuar: gestión defectuosa de incertidumbre reconocida sigue siendo una explicación rival.

El convencional consulta siempre antes de una transición no acreditada y resuelve ese dominio. No se elimina ni debilita ese resultado. Su éxito tampoco permite extrapolar a toda la dinámica que aún falta representar.

## 4. Criterio de continuación

Próxima entrega: especificación sucesora con mapa de gates, estados y cambios sucesivos; vistas de información y costes; registro de decisiones y efectos; criterio de selección y contrastes causales. Revisar su cobertura contra §2 y congelarla antes de ejecutar.

Después, ejecutar la búsqueda del negativo y publicar todas las ramas. Sólo cuando exista un testigo pertinente y su alcance esté auditado se habilita la comparación con EA basada en requisitos. Ninguna nueva ejecución ni resultado de EA se declara en este registro.

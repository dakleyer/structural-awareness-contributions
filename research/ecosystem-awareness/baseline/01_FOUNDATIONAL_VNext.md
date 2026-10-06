# VNext — Foundational Theory y su taxonomía de fallos

**6 de octubre de 2026 · Codex, mismo asistente de IA, revisión para una persona.** Único expediente de la unidad Foundation: [sucesor integradov0.5](01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) ycinco partesv0.4 de procedencia comparten esta VNext. Source snapshot `f7d8ed0846b301617197ade855d5237cbd2280f9`, blob `2cee8af601c89a8785bba9f48974061f0a5dc102`. Se comprobó que no existía expediente activo. [Procedimiento](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md). Ningún original se modifica.

## Alcance real — revisión focal, no lectura completa

Se leyó íntegra la nueva §1.1A, elpárrafo de taxonomía precedente, los textos conservados de § §2/3.4/3.5 ypasajes de estado/procedencia. Elarchivo integrado tiene 135.021 caracteres; **no se leyó completo ni se cotejaron exhaustivamente las cinco partesv0.4 en esta entrada**. Primera/segunda focales; edición y lectura humana de los pasajes indicados; las propias cuatro pasadas completas yquinta de Foundation siguen pendientes.

La comparación necesaria viene de las tres partes funcionales 03, leídas completas, yde 00M §1 ya cotejado. La lectura seleccionada se registra aquí para que un hallazgo material no quede sólo en la VNext del receptor.

## Fondo y lógica — ampliación como caso o condición necesaria

§1.1A hace dos precisiones defendibles: incertidumbre dentro deunA legítimo no es una avería por sí sola, ytrabajo repetido no es automáticamente Type 1. También conserva que las trayectorias I/M/P/Ø sólo diagnostican dentro delChallenge declarado ycon causalidad; unP por otro mecanismo no es necesariamente Type 2.

La frase general ylos dos bullets presentan, sin embargo, ampliación delestado oalcance como rasgo común deambos fallos. Los pasajes conservados permiten algo más general:

- **Type 1 en §3.4:** se necesita uninput definido, elrecurso no está disponible yse continúa esperando/escalando sin límite/escape. No hace falta añadir otra población, dominio uobservación alproblema.
- **Type 2 en §3.5:** elhumanono respondió pero se registra aprobación; unstatus expirado se trata como vigente; evidencia insuficiente sepromueve aPASS. Elscope representado puede permanecer exactamente igual.

**Contraejemplo conceptual propio, no experimento:** una operación espera eternamente por la misma aprobación especificada desde elinicio, sin incorporar variables. Otra recibe «no aprobado/ausente» yregistraPASS para la misma operación. Elcaso relevante es cómo se gestiona lacondición no resuelta, no una expansión observable necesaria.

**Lectura alternativa:** «broader» podría referirse metafóricamente a pretender determinar más de lo sustentado, aunque no crezca el dominio. Enesa lectura puede haber compatibilidad defondo. La propuesta 73 hace explícita esa alternativa yconserva los casos; no afirma una refutación de Foundation ni unfallo de software observado.

## Evidencia y relaciones — efectos en consumidores

La arquitectura funcional §3/F6 separa gestión Sound/Type 1/Type 2/Mixed delresidual estructural. F7 permite parar, limitar oredirigir, con ventana/capacidad; F9 conserva causa/resultado yrevalidation. Se registra el contraste en[03 VNext](03_FUNCTIONAL_VNext.md), [Requirements](00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md), [00N](00N_VNext.md), [00M](00M_VNext.md), [01H](01H_VNext.md), [01B](01B_VNext.md) y [DDS](../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md).

S5/S14/T4 ylos perfiles deChallenge deberán cotejarse completos antes deadoptar 73. No se convierte silenciosamente trabajo adicional en Type 1, ni unoutcomeØ/P en undiagnóstico causal universal. Los consumidores no ganan permiso por recibir una clasificación.

La fuente completa, los anteriores § §16–18, las hipótesis ypruebas materialmente utilizadas siguen pendientes. No se asegura que estepar cierre toda la taxonomía o sus relaciones.

## Edición y lectura humana — alcance focal

La exposición une posicionesA/B/C/D, modos defallo, ejemplo de clasificación y resultados de trayectoria. La repetición de «enlargement» en títulos/bullets puede hacer que una persona busque siempre crecimiento delscope yno examine los casos fijos conservados después. Unlector que ya conoce la definición más general puede entenderlo como ejemplo; hace falta preservar ambas lecturas para la decisión.

No renombro Type 0/1/2 ni añado otro marcador. La recomendación es decir explícitamente que ampliación es una posible manifestación, no untest de pertenencia necesario. Estas observaciones son de los pasajes leídos, no render oaudiencia humana independiente.

## Quinta propia y continuidad

**Pendiente como examen propio de Foundation.** La revisión externa particular de 03 aporta contexto sobre procedencia/consistencia ysupuestos, pero no sustituye una quinta deeste archivo. Tampoco las analogías de ArticleIV prueban la taxonomía. Se completarán los pasajes ylos precedentes realmente usados, con derechos/versiones yjuicio específico, en esta misma VNext. Sexta global pendiente.

## Plan de cambios — candidato 73 pendiente de Iván

**Fuente/ubicación:** bloque de §1.1A desde «Failure Types 1and 2share...» hasta elfinal delbullet Type 2, anterior alejemplo de gatos. Viejo completo único en elblob indicado, ya verificado. **Impacto esperado Alto, riesgo Alto, esfuerzo Alto; prioridad Primera para preparar/conciliar, tanda 3 de contratos/protocolo.** No pertenece a laprimera onda documental de bajo riesgo 26/31/32.

**Beneficio:** Evitar que diagnosticar Type 1/2 exija una ampliación del dominio cuando las definiciones conservadas ya incluyen espera indefinida, silencio tratado como aprobación o datos stale dentro del mismo scope.
**Riesgo:** Afecta taxonomía central y diagnósticos de funciones, Requirements y perfiles DDS; una modificación aislada podría cambiar cómo se interpretan controles o resultados históricos.
**Coste:** Conciliar el bloque 1.1A con § §2/3.4/3.5 conservados, función F6/F7, RequirementsS5/S14/T4 y diagnósticos DDS/realizaciones. No basta modificar un título o un párrafo; la lectura integral de Foundation sigue pendiente.
**Compatibilidad/orden:** conservar la fuente de 00M, tipos anteriores ycausalidad deChallenge; revisar con 03/Requirements/00N/DDS ycasos deobservación/espera dentro deunscope fijo. Completar la lectura integral de Foundation antes deconsiderar elpar incorporable.

**Texto antes — viejo literal completo**

~~~~markdown
Failure Types 1 and 2 share the same root mistake: the system does not respect the qualified boundary of the active exploitation result A relative to B/C/D. In both cases it tries, explicitly or operationally, to treat a broader portion of the surrounding state as if it could be brought into one decision result. The difference is how that attempted enlargement fails.

- **Failure Type 1 — non-viable enlargement / failure to decide.** The system keeps extending observation, search, verification, escalation or qualification in an attempt to absorb more B/C/D material into a broader or more certain decision result. Because the additional material is not yet supported by an adequate evaluation basis, the active determination becomes less viable: uncertainty may widen, confidence may fall, or the system may remain unable to justify a decision at all. The characteristic operational outcome is not “extra work” but failure to reach bounded legitimate closure before budget, capacity or response horizon is exhausted.
- **Failure Type 2 — unjustified enlargement / false decision.** The system also broadens what it treats as operationally determined, but instead of remaining unresolved it collapses insufficiently qualified B/C/D material into A, permission or a globally valid closure. It therefore produces a decision, but one whose scope or certainty exceeds the established basis. The characteristic operational outcome is false closure or an unjustified action.
~~~~

**Texto después — propuesto completo**

~~~~markdown
Failure Types 1 and 2 fail to preserve the qualified boundary between what the process can establish and what remains insufficiently determined. Unqualified enlargement of observation or claimed scope is one way this can happen; it is not a necessary condition. Both failure types can also occur within an unchanged represented scope.

- **Failure Type 1 — failure of bounded legitimate closure.** Acknowledged uncertainty remains active through waiting, search, verification or escalation without a justified capacity/time bound or escape condition. This may involve an attempted enlargement, but may also occur while waiting for one already-defined input within the existing decision scope. Additional work alone is not Type 1; the relevant failure is unresolved determination managed in a way that exhausts or fails to preserve a viable legitimate response.
- **Failure Type 2 — suppressed insufficiency / false closure.** The process suppresses material uncertainty, missing input, invalidated support or a scope limit and presents unsupported closure or action as justified. This may broaden claimed scope, but may also occur within the existing scope by treating silence as approval, insufficient evidence as PASS or stale status as current. A prohibited outcome caused by another mechanism is not automatically Type 2.

The causal treatment of non-determination, the declared scope and the supported response contract govern the diagnosis. Correctly bounded unresolved state remains a legitimate outcome; neither extra work nor an outcome label by itself establishes a management failure.
~~~~

**Instrucciones de Iván:** original sólo lectura, una VNext porunidad, preservar elviejo ylas conversaciones, valorar impacto/riesgo/coste yproponer antes/después quirúrgicos. Decisión concreta pendiente; ninguna taxonomía, métrica, esquema oresultado se modifica por publicar esta auditoría.

---

## Lectura completa de la Foundation integrada — 6 octubre 2026

**Auditoría realizada por Codex, el mismo asistente de IA, para revisión humana.** Esta entrada amplía la lectura focal anterior; no la borra ni la presenta como otra auditoría independiente. Fuente actual: commit `409bfa9eff2b3e24e7350021db9e587861583de8`, blob `2cee8af601c89a8785bba9f48974061f0a5dc102`. Se leyeron los **135.021 caracteres completos** del integrado, desde la introducción hasta la nota editorial final, incluidos §§1–18 conservados, hipótesis, diccionario, procedencia y reservas. Las cinco partes v0.4 se identificaron por sus blobs y límites, pero su conservación completa no se certifica por este examen del sucesor.

| Pasada | Trabajo efectivamente realizado | Límite que permanece |
|---|---|---|
| 1. Fondo y lógica | Lectura integral del argumento; examen de las dos causas, tipos, compresión, selección recursiva, hipótesis y reservas. | Juicio conceptual; no prueba de implementación o eficacia. |
| 2. Evidencia y relaciones | Cotejo de los pasajes afectados con 00M §1, 03 completo ya leído, Requirements S5/S14/T4, DDS §§5.1–5.2 y README RA completo actual. | Derivaciones 02A/02B, fidelidad integral v0.4→v0.5 y matrices/perfiles/realizaciones materialmente utilizados siguen por examinar. |
| 3. Edición, estructura y formato | Examen textual completo de la arquitectura del documento, rótulos históricos, secuencia, enlaces de lectura y anclas explícitas. | No inspección de un PDF/render ni comprobación bibliográfica universal. |
| 4. Legibilidad y comprensión | Lectura orientada a reconstruir la explicación sin convertir términos en permisos, pruebas o estados universales; casos de comprensión abajo. | Es simulación del mismo asistente, no prueba con una persona independiente. |
| 5. Trabajos externos | Contraste propio y específico con PropUQ-MAS, información utilizable, antecedentes de computabilidad/información y discusión FG-TIDA actual. | Lecturas primarias inaccesibles/incompletas quedan declaradas; ampliación material abierta. |
| 6. Unificadora global | **No lanzada.** Estas son revisiones cruzadas de relaciones concretas. | Las cinco pasadas materiales del alcance principal aún no están cerradas. |

### Primera pasada — qué se sostiene y por qué

La línea central es coherente cuando se conservan sus condiciones: una decisión puede estar justificada sin determinar todo el ecosistema. Hay dos motivos distintos para revisar esa justificación: información/capacidad insuficiente para la pregunta y pérdida de vigencia del marco que antes la sustentaba. Una medida local correcta no elimina ninguna de esas dos fronteras.

**U, R y ventana no son tres universos cerrados.** En §§3–4 puede faltar un valor de una entidad ya representada dentro de U. R recoge influencias materiales fuera de la representación/evaluación efectiva, sin prometer enumerarlas. §16 precisa que W selecciona contexto activo de un campo representado también limitado. Por eso no cabe sumar un supuesto porcentaje de residual ni convertir el número de objetos observados en completitud.

**La semántica vigente procede de 00M.** A puede ser una probabilidad si ése es el resultado del proceso; B conserva fundamento y reserva evaluable, C una vía fundada aún sin marco de evaluación, y D una barrera efectiva relativa al proceso. §1.1 y el diccionario mantienen esa referencia. Los antiguos polos/ventanas y las letras locales D/C/M de §15 forman parte de la derivación conservada; no se renombra esa historia como si fueran las variables actuales de otro kernel.

**Type 0 exige fundamento, no sólo persistencia.** §17.1 diferencia una barrera estructural de una declaración limitada al marco y dice que el tipo no es un oráculo de ejecución. Una búsqueda prolongada no demuestra por sí misma imposibilidad estructural. Type 0 puede coexistir con gestión correcta y una operación legítima acotada. La reserva importa al interpretar §17.5: no usar cualquier alerta como certificado automático de Type 0.

**Type 1/2 describen mecanismos, no sólo resultados.** §§2, 3.4–3.5, 17.1.1 y 18 conservan espera/escalado sin cierre legítimo, supresión de insuficiencia, silencio presentado como aprobación y vigencia inventada. Las trayectorias híbridas describen cómo presión de cierre o invalidación puede cambiar el mecanismo; no crean otro tipo. Coste alto, incertidumbre, HOLD, Ø o P no bastan aisladamente para diagnosticar.

**Selección recursiva y compresión tienen límites distintos.** §16 conserva el argumento condicional: si selector y respuesta final fueran procedimientos efectivos con garantía correcta sobre todos los programas arbitrarios de la clase semántica no trivial, su composición sería un decisor general. No se demuestra con ello que toda decisión real sea indecidible, que cada instancia sea imposible o que la respuesta deba ser 50/50. §6 trata la pérdida de información de una transformación, no esa imposibilidad de cómputo.

**La transición temporal tampoco es una etiqueta automática.** §17.4 distingue salida dinámica observable de invalidación del marco de decisión para una misión. Puede observarse un cambio sin que la decisión concreta deje de estar suficientemente sustentada; puede perderse el sustento sin una reconstrucción completa del régimen. La comparación debe fijar cuál de esas proposiciones examina. Las escalas temporales son una heurística explicativa, no constantes medidas de todas las arquitecturas.

**H1–H6 siguen siendo hipótesis.** Se propone contrastar pérdida de cualificadores, no compensación entre dominios, composición y recursos/latencia bajo un alcance declarado. El texto pide controles competentes comparables; ninguna de esas preguntas adquiere respuesta empírica por estar formalizada. El diferencial combinado se mantiene como candidato de investigación, con antecedentes reconocidos.

### Segunda pasada — productor, receptor y límites materiales

Se comprobó la relación con [00M](00M_VNext.md): el mismo fenómeno puede ser resultado de un monitor y residual de otro proceso. El diccionario distingue sujeto, proposición y dominio de decisión; no basta compartir un nombre o señal para heredar capacidad o validez. Tampoco se obtiene permiso del rol A/B/C/D.

En [03 funcional](03_FUNCTIONAL_VNext.md), F2/APQ califica vías, F4 mensajes, F5 dependencia y F6/F7 gestión/respuesta. La Foundation conserva que repetir una vía o recibir varias versiones de una misma fuente no aporta automáticamente evidencia independiente. F9 puede mantener historia útil sin convertirla en confianza universal. El emisor conserva su estado; el receptor cualifica su utilidad y el actor autorizado decide/ejecuta. La relación se comenta en ambos expedientes.

En [Requirements](00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md), S5 no convierte hechos incompletos en permiso ni UNKNOWN en veto universal; S14 exige evidencia y regla aplicable para cada transición; T4 pide una postura aún útil dentro de capacidad/tiempo. Es compatible con no exigir expansión de scope para Type 1/2. La tabla de correspondencia no demuestra cumplimiento ni sustituye las derivaciones y campañas pendientes.

En [DDS](../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md), §§5.1–5.2 ya exigen M legítimo definido ex ante y alcanzable en el mismo contrato para la firma discriminativa Type 1; Type 2 necesita la causa epistemológica del cierre P. Foundation es la derivación general y DDS una realización de prueba condicionada: no se importa una equivalencia universal Ø=Type 1 ni P=Type 2. El paquete de estudios añadido concurrentemente se conserva; sus resultados no se vuelven a clasificar ni se declaran examinados por esta lectura.

En [RA](../../regime-awareness/README_VNext.md), el README actual distingue detector mínimo, evaluación más amplia, delta cualificado y postura/ejecución de Operation. Concuerda con §17.4 al no hacer de una salida dinámica el permiso de actuar. Los candidatos previos 35/37/38 sobre B/C/D mantienen sus propios gates; esta coincidencia no los resuelve.

**Fidelidad documental pendiente:** la nota final del integrado indica que no absorbe automáticamente desarrollos posteriores. El prefacio antiguo del apéndice está identificado expresamente como histórico. Eso permite leerlo sin confundir su estado de companion con el sucesor actual, pero no prueba conservación literal de cada sección frente a todas las partes y 01A. Ese cotejo y 02A/02B permanecen abiertos en esta unidad y en las VNext propietarias cuando corresponda; no se crea una ficha o expediente por cada pasada.

### Tercera pasada — estructura y formato

El documento conserva una introducción integradora, bloques derivados con numeración histórica, diccionario y controles de procedencia. Esa arquitectura explica por qué el orden de lectura no sigue siempre 1–18: se conserva la derivación a la vez que se organiza por las dos causas y la función. No se propone reordenar, dividir ni mover archivos.

La carga de lectura es elevada. La referencia introductoria y la nota final ayudan a distinguir teoría, contrato y evolución posterior; el lector necesita volver a ellas antes de trasladar una frase histórica a una interfaz actual. En esta VNext queda una ruta breve: **dos causas → límites de la determinación → mecanismo de fallo → marco temporal → hipótesis y diccionario → fuentes/consumidores actuales**.

Hay dos anclas explícitas consecutivas iguales `candidate-research-hypotheses` en §11. Es redundancia editorial local, no un destino contradictorio que pruebe un enlace roto: ambas están junto a la misma sección. No preparo un cambio canónico de bajo valor sólo para eliminarla. Los rótulos/nombres locales se explican; no se “normaliza” el texto histórico.

### Cuarta pasada — comprensión humana

Una persona debería poder reconstruir tres preguntas: ¿qué sustenta esta decisión?, ¿sigue vigente ese sustento?, ¿qué respuesta legítima sigue siendo posible? Esa lectura evita convertir el documento en una colección de códigos.

| Caso conceptual de lectura, no experimento | Interpretación que debe conservarse |
|---|---|
| Falta una aprobación conocida y se responde HOLD con límite, responsable y vía legítima. | Incertidumbre gestionada; no Type 1 automático. |
| Se espera por ese mismo input sin límite/escape y se pierde un cierre legítimo que seguía disponible. | Puede haber Type 1 con scope fijo; hacen falta causa y contrato. |
| Se registra el silencio como aprobación para la misma operación. | Candidato Type 2 por certeza/permiso no sustentado, sin necesitar ampliar el dominio. |
| Hay P por un mecanismo ajeno a la supresión epistemológica. | P no diagnostica por sí solo Type 2. |
| Un detector observa una salida de su baseline. | Hay evidencia de salida bajo su representación; aún falta cualificar el efecto sobre esta misión. |
| Un resumen mejora el trabajo de un receptor limitado, pero omite una dependencia relevante. | Utilidad del procesamiento y preservación del cualificador son preguntas distintas. |

La palabra “ampliación” de §1.1A puede leerse metafóricamente como pretensión de establecer más de lo sustentado. Esa lectura sigue siendo posible. El problema humano es que los dos títulos y el párrafo general pueden hacer buscar crecimiento observable del scope incluso en los casos fijos posteriores. No se demuestra una refutación del modelo ni un fallo runtime.

### Quinta propia — contraste externo específico

**Consulta del 6 octubre 2026.** Se distingue lo leído de lo inaccesible; no se reproducen resultados, importan programas/datos ni se emprende una búsqueda mundial de novedad.

**PropUQ-MAS**, Yaokun Liu, Yifan Liu, Daniel Yue Zhang, Ruichen Yao, Zelin Li y Dong Wang: [arXiv v3, 1 septiembre 2026](https://arxiv.org/html/2608.22130v3), §§1–3, configuración de §4 y Limitations leídos; no anexos completos ni datos brutos. Representa incertidumbre heredada mediante un grafo de ejecución. La recurrencia usa independencia entre contaminaciones entrantes y entre error local/propagación; aceptación autodeclarada es un proxy, no probabilidad condicionada observada. Coincide con la preocupación de §6, pero no establece nuestro residual abierto, autoridad o suficiencia de misión. La ficha declara aceptación EMNLP 2026; no se comprobó una publicación final en Anthology ni adopción normativa. Pieza reusable: contraste de dependencia y control local frente a propagado, preservando sus supuestos. Texto: licencia arXiv no exclusiva, sin permiso amplio inferido.

**Implementación PropUQ-MAS:** [README](https://github.com/yaokunliu/PropUQ-MAS/blob/de5e5945ea3814400624c55ab071e89cbbd9b672/README.md) y [LICENSE](https://github.com/yaokunliu/PropUQ-MAS/blob/de5e5945ea3814400624c55ab071e89cbbd9b672/LICENSE) completos, pin `de5e5945ea3814400624c55ab071e89cbbd9b672`; no código ejecutable leído/importado. Licencia MIT de software/documentación, aviso Anonymous Authors; no cubre por inferencia modelos/datasets. El README exige sus licencias propias. También declara normalización de pesos entrantes en replay multiparental frente a scores directos del paper: cualquier futura réplica debe distinguir esas realizaciones, no presumir equivalencia. No se selecciona tecnología.

**Información utilizable**, Yilun Xu, Shengjia Zhao, Jiaming Song, Russell Stewart y Stefano Ermon: [arXiv v1, 25 febrero 2020](https://arxiv.org/html/2002.10689v1), §§1–3.3 leídos; metadato ICLR 2020 Talk, sin revisar experimentos/anexos completos. Su familia predictiva restringida mide aprovechamiento por un observador limitado; preprocesar puede aumentarlo sin aumentar información mutua de Shannon. No refuta la pérdida ya descartada de §6.3. Sí impide convertir DPI en una regla de que reexpresar/estructurar nunca ayuda. Pieza reusable: separar fidelidad al estado de utilidad para el receptor y declarar su capacidad. Texto bajo licencia arXiv no exclusiva; licencia de código/datos no examinada.

**Rice y Cover/Thomas:** [Rice 1953, AMS](https://www.ams.org/journals/tran/1953-074-02/S0002-9947-1953-0053041-6/S0002-9947-1953-0053041-6.pdf), extractos primarios indexados de p.358 y corolario de p.364; el PDF completo devuelve 403 y la copia académica timeout. [Cover/Thomas, segunda edición, capítulo 2](https://doi.org/10.1002/047174882X.ch2): metadatos editoriales y contenido del capítulo; PDF inaccesible, no lectura completa de §2.8. No se certifican aquí sus pruebas. Las restricciones expresas de Foundation son decisivas: clase semántica no trivial/procedimiento general en §16, cadena Markov/información mutua en §6.3; no trasladarlas sin condiciones a todo conocimiento o rendimiento limitado. Texto sujeto a derechos editoriales; código/datos no examinados ni reutilizados. Obtener las fuentes completas sigue pendiente de la segunda pasada material.

**NIST SP 800-160 v2r1**, Ross, Pillitteri, Graubart, Bodeau y McQuaid, diciembre 2021: [ficha oficial final](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final) y abstract leídos, no handbook completo. Anticipar, resistir, recuperar y adaptar ya tienen antecedente de ingeniería; Foundation no los origina. Pieza candidata: cotejar una obligación de adaptación/objetivo frente a una dependencia concreta, con alcance propio. No eficacia de EA o adopción inferida. Derechos del PDF/terceros y de una realización deben comprobarse antes de reutilizar texto/código/datos; ninguno se copia.

**FG-TIDA #13:** [Ward, 7 septiembre](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256), [nota conceptual de Iván/dakleyer, 8 septiembre](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5585387513), y [body actual de Ward actualizado 6 octubre 2026](https://github.com/FG-TIDA/themes/issues/13), leídos completos. La nota del 8 septiembre es contribución del mismo autor del corpus, no corroboración independiente. Ward propone separar envelope y signal lifecycle; el body actual deja abiertas autoridad de contención, privacidad y alcance. El diccionario conserva esas fronteras. Pieza candidata: prueba separada de señal y determinación bajo un perfil declarado, aún sin activarla. Estado de discusión/propuesta open, sin adopción, realización autorizada o derechos de código/datos establecidos por el comentario.

**Juicio sobre Foundation:** el soporte externo alcanza mecanismos y límites concretos; no prueba el contrato combinado ni una novedad exclusiva. El contraste delimita dos comparaciones diferentes: fidelidad/pérdida respecto al estado y utilidad de una representación para un receptor con recursos finitos. Una futura prueba necesita ambas, además de dependencias y autoridad. El nuevo hallazgo externo se registra también en 03/00M/00N. Las lecturas limitadas y fuentes materiales pendientes impiden cerrar el ciclo documental.

### Conversación de auto-revisión y plan 73 tras leer todo el integrado

**Codex, respuesta a su revisión focal:** no retiro el hallazgo 73. §§2/3/17/18 refuerzan los casos de scope fijo; al mismo tiempo la Foundation completa ya protege la gestión legítima, causalidad, Type 0 y no-equivalencia de resultados. El beneficio esperado es de precisión conceptual y lectura, no reparación de un error general demostrado.

Se mantiene el **mismo par 73, viejo completo y propuesto completo** anterior, sin reescribirlo ni abrir otra propuesta. Viejo localizado una vez en §1.1A, línea 33 del snapshot actual; propuesto ausente del original. Fuente y blob iguales al examen focal. **Impacto Alto condicionado, riesgo Alto, esfuerzo Alto; prioridad Primera para preparar, tanda 3.** No entra en la primera onda 26/31/32.

El coste pendiente ya no incluye leer este integrado: incluye conservación/derivaciones y conciliación de diagnósticos con 03, Requirements, DDS y perfiles. El gate de lectura integral de v0.5 se cumple; los demás no. Preservar el diagnóstico condicionado a un M disponible de DDS, las respuestas legítimas no resueltas y la lectura alternativa metafórica. No se renombra una taxonomía ni se reinterpreta evidencia congelada. **No listo para incorporar; decisión concreta de Iván pendiente.**

No se fabrican pares nuevos para las reservas ya presentes, la ancla duplicada o el beneficio potencial del preprocesamiento. Queda publicado el razonamiento que puede hacer innecesaria una adición. Próximo examen: derivaciones 02A/02B y correspondencia con matrices/perfiles; fuentes formales completas y fidelidad de la unidad v0.4/01A. La sexta global continúa pendiente.

### Revalidación del receptor DDS durante la preparación de publicación

El head avanzó a `f0ebdd1031eb740b181c6a405fba6beb7f29ff6d` y sólo cambió el original DDS, de blob `c0e14e8401e1c9783dbfcb4863816d7ef0c0a9b1` a `a44bf26ff0bab1792aef1bc7d115850532e592cb`. Esta revisión no hizo esa modificación ni infiere su autorización; la conserva. Foundation y las ocho VNext objetivo mantienen los mismos blobs anteriores.

Se leyeron completos los nuevos pasajes DDS §§3.1/5.3/7.1A/7.4 y su contexto §§4–10. §5.3 exige admitir M antes de observar resultados: legítimo, no gratuito, plausible para la capacidad, dentro de presupuesto/horizonte, sin oracle privado y sin barrera Type 0 conocida. §7.1A distingue mínimo del mapa privado de un mínimo con información accesible; exceso frente al primero no es negligencia automática. §7.4 excluye cierres P del numerador Type 1 y conserva causalidad específica para Type 2.

**Pregunta material pendiente de perfil:** ¿qué evidencia establece que la falta de cierre expresa el mecanismo Type 1 en el contrato de información/capacidad, en vez de deducirlo sólo de M existente en el mapa del evaluador? La fuente acota el estimador y pide admisión; hay que comprobar esa obligación y exclusiones en cada realización, no tomar la fórmula como diagnóstico universal. La nueva regla no certifica sus denominadores, independencia o ejecución. No se añade otro candidato mientras falte ese cotejo.

73 conserva su par y valoración, con el gate actualizado de este receptor. Revisión cruzada también en DDS y continuidad EP. No se cierra la sexta ni se cambia el original por la revalidación.

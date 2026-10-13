> Registro de preparación incorporado al expediente GitHub existente el 13 octubre 2026. Las menciones a «local» describen su preparación anterior. Rige [la orientación R2/freeze/R3](PRINCIPIO_R2_FREEZE_R3_2026-10-13.md); los checks siguen siendo sintéticos y no un ensayo nativo. Volver a [CAMPAIGN](../CAMPAIGN.md) o [CONTINUATION](../CONTINUATION.md).

# Formalización y contraejemplos del cambio de contexto

Fecha: 13 octubre 2026. Modelo propuesto para revisión, independiente de la aceptación del mundo nativo.

## 1 Variables y unidad de afirmación

Sea w un mundo, t el instante, D la misma decisión pendiente, Q el mismo predicado temporal declarado antes del ensayo y P una condición necesaria de su régimen de observación. Q_t(w) es su valor en el contexto de t para D. Mantener Q fija significa conservar el predicado, subject, finalidad, scope y regla temporal; no exigir que una propiedad de un entorno cambiante mantenga el mismo valor.

Sea V_t(w) la matriz de votos. Sea M_t(w) todo metadato y respuesta de consulta legítimamente accesible. La observación completa es O_t(w)=(V_t(w),M_t(w),clocks_t,transcript_t). Definirla evita inferir imposibilidad desde una mera tasa igual.

Para una observación o, C_t(o)={w: O_t(w)=o y w satisface las restricciones admitidas}. El conjunto identificado es I_t(o)={Q_t(w):w pertenece a C_t(o)}. Q está identificada en este modelo si I_t contiene exactamente un valor. No significa que el modelo sea verdadero ni que sus restricciones estén independientemente probadas.

## 2 Pérdida de identificabilidad

Un ejemplo de pérdida requiere:

- I_t0(o0)={q0}, por una fuente/régimen admitido.
- Una modificación material de P entre t0 y t1, registrada por quien puede observarla.
- I_t1(o1) contiene al menos dos valores distintos.
- Las mismas matrices V_t0 y V_t1 en el contraste elegido, o una definición explícita más débil de igualdad si solo se estudian estadísticas.
- Mantener la conclusión source-native histórica dentro de su scope.

Un universo de solo un mundo que el autor declara “correcto” no satisface el control. Deben enumerarse al menos w+ y w− de manera que Q_t1(w+) sea diferente de Q_t1(w−), pero O_t1(w+)=O_t1(w−). Los mundos no se entregan juntos al candidato.

## 3 Límite de observación

Para un algoritmo determinista f que recibe solo O, si O(w+)=O(w−), entonces f(O(w+))=f(O(w−)). Dado que los valores reales de Q son diferentes, al menos una de las dos respuestas específicas sería incorrecta. Una respuesta de insuficiencia puede ser correcta para ambos.

Para un algoritmo aleatorio con misma distribución de randomness independiente del mundo, su distribución de outputs condicionada al mismo input es igual. No puede producir una garantía de identificación exacta del mundo oculto. El argumento no exige outputs particulares iguales de dos llamadas aleatorias; exige igualdad de su ley condicionada.

El límite depende del canal definido. Si se incorpora una fuente de contexto que distingue los mundos, la premisa O(w+)=O(w−) deja de cumplirse y puede haber detección. Eso demuestra utilidad de esa información; no distingue por sí solo entre EA y B2.

## 4 Construcción finita ilustrativa

Universo: dos valores de una propiedad contextual, permit y block; epochs e0 y e1; una evidencia que relaciona subject, reference, epoch y value bajo trust estipulado por el fixture.

En t0, currentEpoch=e0 y un witness válido para e0 permite un solo valor. En t1, currentEpoch=e1 y no existe witness aplicable e1. El witness e0 persiste como historia. Ambos values actuales siguen compatibles con la observación: I_t1={permit,block}. En t2, un witness e1 legítimo restituye una restricción y el conjunto se vuelve singleton.

La única intervención primaria es el paso a un contexto que ya no está cubierto por la relación anterior. No se modifica V ni se inyecta la respuesta “pérdida” en el candidate packet. El evaluator privado tiene dos posibles truths para t1; el candidato solo ve la fuente y los límites que realmente le corresponden.

La propiedad que se identifica en esta demo es un valor contextual bajo un modelo explícito, no la verdad objetiva de la clave CTGT. Las reglas de trust son premisas synthetic. Su validez externa es una obligación separada de la primera campaña.

## 5 Por qué una asociación material importa

Si una inferencia r depende de P y de premisas A, retirar la justificación de P no prueba lógicamente no-r; impide usar la derivación A y P → r. Si otra derivación B → r sigue válida y admitida, r puede continuar soportada.

Por tanto, el modelo debe considerar alternativas y scope. Un algoritmo que degrada toda la conclusión por cualquier campo ausente confunde la ausencia de una derivación con ausencia de toda justificación. El control de recuperación alternativa del preflight detecta ese error de contrato.

Un dato contradicho puede refutar una conjunción explícita que lo incluye. No refuta automáticamente una proposición distinta: el sello erróneo de una clave no prueba que el valor de la clave sea falso.

## 6 Cambio de verdad y cambio de justificación

Hay tres modelos distintos:

1. Q_t cambia realmente por contexto material; votes stale permanecen constantes.
2. Q_t no cambia, pero el nuevo observation regime ya no permite determinarla.
3. El observation regime no cambia; solo se descubre que una premisa anterior no estaba probada.

Solo el segundo demuestra una pérdida de identificación por modificación de observación; el primero muestra cambio potencialmente invisible y pérdida de vigencia; el tercero es corrección de una sobreafirmación inicial. Los tres pueden ser útiles, pero el reporte no debe fusionarlos.

Una revocación de validez puede ser observable y conocida. Es pérdida de aplicabilidad justificada, no un misterio C. Un t0 basado solo en declarations del generador no es observacionalmente identificado por el detector.

## 7 Cambio de dependencia con marginales conservadas

Una alternativa más amplia considera dos distribuciones sobre los resultados de varios jueces con las mismas marginales pero diferente dependencia. La matriz conjunta o la secuencia puede permitir distinguirlas; monitorear solo medias no.

Construir marginals iguales no basta para mostrar votes completos iguales. Construir un replay particular idéntico tampoco demuestra igualdad de las leyes generativas. Si se quiere una conclusión probabilística, fijar distributions y demostrar que su pushforward por el canal de observación coincide o medir el poder bajo alternativas especificadas.

Por eso, retirar un binding desconocido no se equipara al shuffle independiente por ronda anterior. Ese shuffle estaba definido y podía analizarse con el modelo conocido. Cualquier cambio verdadero del generador requiere un perfil fuente nuevo y no cuenta como mínima extensión puramente receptora.

## 8 Recurrencia después del freeze

Sea r una reparación de un dominio declarado R y sea C(r) su cobertura efectiva, incluida la adaptación que el propietario haya defendido y congelado. El objeto de recurrence es seleccionar un cambio admisible d de D que quede fuera de C(r), manteniendo las defensas de r.

La dirección del programa se expresa como para cada r de R existe un d de D fuera de C(r). La comparación EA es una obligación separada: un mecanismo general g, fijado antes de revelar d, debe reconocer la pérdida material de fundamento y realizar una recalificación admisible dentro de su frontera de información y recursos.

No comparar g con una r deliberadamente pobre, ni suministrar a g el answer del cambio. La igualdad para d dentro de C(r) es la base; los controles que muestran esa igualdad no establecen ni refutan el recorrido d fuera de C(r).

Una configuración que ya contiene la función general recibe crédito por ella. La demostración sobre familias depende de sus dominios y condiciones; el nuevo ensayo de Flores registra la instancia r, freeze, d y resultado. No se transfiere automáticamente a Flores un bound de otro contrato.

## 9 Evidence de este paquete

El preflight verifica 20 controles y 64 pares de twins en un universo finito. Sus hidden truths son distintos y sus paquetes visibles completos son iguales en cada par. B2 y referencia mantienen indeterminacy en esos pares, con mismo output nativo proxy.

Este es un test del modelo/contrato, no una muestra independiente de la realidad, una verificación Lean/Isabelle ni una aceptación del oráculo. La prueba matemática arriba se limita al canal definido; los asserts ilustran instancias y ayudan a evitar la tautología histórica.


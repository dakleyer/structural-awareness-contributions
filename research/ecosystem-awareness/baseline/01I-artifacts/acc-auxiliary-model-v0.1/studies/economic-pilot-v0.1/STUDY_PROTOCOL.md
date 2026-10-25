# Primer protocolo económico del modelo auxiliar

Este estudio pregunta qué mejoras llegan a acuerdo y ejecución, cuánto cuestan y qué ocurre cuando cambia el fundamento entre aprobación y efecto. Fija un ejemplo empresarial pequeño que otra persona puede recorrer a mano. Sus unidades, preferencias y eventos son ficticios. Es soporte de especificación de DDS Stage A, sin aceptación formal ni integración del ACC en agentes.

## Objeto y contrato de comparación

Marketing y Operaciones ganan 60 y 40 unidades de un numerario monetario ficticio. Sistemas soporta una pérdida directa de 30. Una transferencia de 40 a Sistemas puede permitir el acuerdo; Marketing puede pagarla o compartirla con Operaciones. Las transferencias suman cero. Reconfigurar consume 6, 4 y 2 unidades reales adicionales; Finanzas no obtiene un saldo directo. Utilidad transferible, numerario común y costes compatibles son supuestos explícitos de este ejemplo.

Derechos, servicio íntegro, participación explícita, objetivo vigente, ausencia de congelación, aprobación material actual y permiso técnico son condiciones separadas. Una suma positiva no las compra. La ejecución puede autorizarse en un instante y dejar de estar justificada después.

La preparación cuesta una unidad y cada paso de revisión 0,25, imputados a Marketing. Se cobran incluso cuando no hay acuerdo. Los doce de reconfiguración sólo se consumen al producirse el efecto. El [recorrido manual](MANUAL_TRAVERSAL.md) muestra saldos y decisiones; los gastos iniciales fueron encargados expresamente y permanecen visibles. No se afirma una mejora de Pareto de todo estudio fallido por haber encontrado una oportunidad parcial.

## Comparadores e información

Se comparan `conventional_adaptive` y `qualified_record`. Ambos reciben las mismas observaciones admitidas, opciones de compensación, permisos y reglas de revalidación. El segundo registra expresamente fundamento y cambios; es un prototipo local de registro, no una implementación de Ecosystem Awareness, ABCD, MSCA o ACC. Comparten reglas de decisión para comprobar primero la especificación económica y temporal. No constituyen dos tecnologías independientes ni permiten atribuir un efecto causal a EA.

Ambos pueden negociar y reconocer un cambio legítimo. El resultado observado aquí es empate. Si el registro cualificado costara una unidad más de preparación, su saldo completo sería una unidad menor por caso. No se han medido tiempos de computación ni costes de ingeniería reales.

`stale_reference` conserva una decisión antigua y sólo sirve como control negativo. No es el comparador competente. Un permiso caducado puede bloquear su intento sin efecto; un token todavía válido puede permitir una operación que el criterio semántico considera obsoleta. Esos resultados se registran por separado.

El simulador prepara la observación visible. Las políticas nunca reciben el estado real reservado al evaluador ni las expectativas manuales. E09 y E10 tienen la misma observación y decisión: en E10 el coste real es mayor y ambas políticas fallan. El protocolo no les exige adivinar ese dato. E11 muestra el error en sentido contrario. No se concede anticipación del futuro ni se modifica una política después de conocer qué cambio se seleccionó.

## Casos congelados y resultados

[protocol.json](protocol.json), [cases.json](cases.json), [manual_oracle.json](manual_oracle.json) y el recorrido manual quedaron fijados en [freeze.json](freeze.json) antes de crear la primera implementación. El registro local no equivale a inscripción en una campaña DDS. Las expectativas proceden del mismo asistente de IA y no de un adjudicador humano independiente.

Los 18 casos incluyen acuerdo inmediato, reajuste, pagador alternativo, pérdida neta, derechos, servicio, silencio, información desconocida, estados indistinguibles, estimación pesimista, duplicación, espera, caducidad, orden obsoleta, renovación, continuidad y causa no resuelta. T05 contiene tres encargos distintos; E12 evita contar dos veces el mismo efecto. T06 permite dos consultas y luego conserva causa no resuelta.

Se registran beneficios, transferencias, costes por actor, preparación, revisión, intento, efecto, legitimidad bajo condiciones actuales, oportunidades no realizadas y continuidad. El resultado del escenario permanece separado de la concordancia del programa con la tabla manual: un FAIL previsto sigue siendo FAIL. Las instancias son controles elegidos, no una muestra representativa; no se estima una prevalencia empresarial ni una tasa de superioridad.

Los [resultados](results/RESULTS.md), [datos](results/results.json) y [trazas](results/traces.jsonl) permiten revisar cada paso. Hay 36 recorridos principales, dos controles negativos y 62 eventos. La concordancia observada no valida las otras familias del modelo.

## Controles auxiliares y alcance

Un control separado muestra cómo una puerta basada sólo en W puede aceptar una puntuación mejor por ocultación de una alternativa, sin mejora material. Otro distingue ACW observado, capacidad potencial y contribución realmente recuperada; no mide inteligencia perdida y admite tiempo elegido para otros fines. Un tercero calcula ahorro de recursos con servicio equivalente y excluye bajar calidad. Son ilustraciones analíticas con unidades propias, no mediciones humanas agregables al saldo empresarial.

La cobertura de ACC-ECO-01, 04–06, 10–11 y 16–22 es parcial: acuerdo y cuentas, permiso, estimación, continuidad, silencio y capacidad se ilustran; no se prueba un contrato ACC sucesor, un conflicto completo de perfiles, una reversión estratégica o experiencia humana. No se ejecutan causalidad FH-C, economía FH-E, redes a gran escala ni las 22 familias completas.

La primera conexión pertinente es la obsolescencia semántica de una operación diferida S5. [El adaptador documental](DDS_ADAPTER_SPEC.md) fija la correspondencia y sus límites. Los oráculos de UC21 y R01 no se ejecutan, reetiquetan ni sustituyen. Un experimento posterior necesita la especificación, arquitectura, tecnología, registro, recursos y observación de efecto que exija su propietario.

## Reproducción

Se requiere Python 3.12 o posterior, con biblioteca estándar. Desde esta carpeta:

```text
python -B run.py --output-dir results-reproduction
python -B -m unittest discover -s . -p test_model.py -v
python -B adapter_preview.py --output-dir adapter-reproduction
```

El primer comando comprueba el freeze antes de calcular. Un cambio de entradas exige un sucesor explícito del protocolo; no se ajusta silenciosamente la tabla para que pase. Una nueva versión de código queda identificada por su hash en las salidas. No se instala ningún agente ni se realizan acciones sobre servicios reales.

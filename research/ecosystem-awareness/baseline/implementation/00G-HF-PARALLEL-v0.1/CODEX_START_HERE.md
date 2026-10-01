# Codex — empezar aquí: receptor nativo 00G-HF sin EA

> **Ruta actual, 2026-10-01:** [competidor Casbin-polling ejecutado bajo C3 intacto](../../traversals/00G-HF-CASBIN-POLLING-v0.1/README.md). Hay testigo negativo programado y reparación EA; el control convencional de recarga también repara. El receptor/modelo de cached-lineage es auxiliar y usa otro oráculo. No exigir credenciales para reproducir este recorrido programado.


**Ruta adicional — 1 de octubre de 2026:** para ejecutar con un modelo el mecanismo de procedencia en caché, usa el [nuevo receptor con decisiones abiertas](../../fixtures/00G-HF-MODEL-RECEIVER-v0.1/README.md) y su protocolo. Tiene 17/17 controles offline; la ejecución real sigue bloqueada por falta de acceso/modelo configurados. Su comparación usa nativo, evidencia actual y evidencia con EA; requiere primero un fallo nativo observado. Los comandos de seis celdas que siguen pertenecen al perfil anterior con controles al ejecutar, que permanece válido y puede superar sus casos sin EA. No mezclar sus resultados ni retirar sus controles para producir un fallo.

**Encargo:** continuar de forma autónoma la línea B del [plan de implementación](./README.md), conservando todos los resultados y límites. La línea A implementa el componente EA en otra carpeta; no esperes a que termine para preparar o ejecutar el receptor nativo.

## 1. Qué estás probando

Repositorio: `dakleyer/structural-awareness-contributions`. Referencia al redactar: `a3796cca4ca0445ae1caca9876384909548cdc80`. Usa el commit actual de tu checkout y regístralo; no reemplaces trabajo posterior por esa referencia.

El candidato publicado es **una aplicación del autor sobre Responses API, con controles convencionales, perfil OAI-G1 candidato**. No es OpenAI por defecto, un recorrido G0 ya implementado, el Agents SDK ni el sistema interno histórico. Puede superar las seis celdas sin EA. Ese resultado debe publicarse y conservarse.

Codex actúa primero como implementador/operador. Si el propio modelo Codex se usa como receptor, eso requiere otro adaptador, registro de sus capacidades/configuración, aislamiento de vistas y una etiqueta de familiaridad honesta. No conviertas tus acciones después de leer el oráculo en un ensayo ciego. No supongas que la suscripción o sesión Codex proporciona una clave API utilizable.

## 2. Lectura necesaria antes de ejecutar

1. [Plan y división de archivos](./README.md).
2. [Candidato nativo v0.1](../../fixtures/00G-HF-NATIVE-v0.1/README.md), su `INSTRUCTIONS.txt`, `native.py`, `api_adapter.py`, `run_pilot.py` y `DESIGN_FREEZE.json`.
3. [C3 ROUND1_PROTOCOL.md](../../fixtures/00G-HF-ORACLE-v0.4/ROUND1_PROTOCOL.md) y su freeze. SHA-256 del archivo de freeze: `58c5a0cbb00fd945e7ebebbcfd6e7758573fc6f7fb6209e33dfc8e3e76c7d287`.
4. [Protocolo causal §§3–10](../../00G_HF_CAUSAL_NEGATIVE_TRAVERSAL_PROTOCOL_v0.3_DRAFT.md), [reducción](../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md) y [hoja de ruta W3-HF](../../../WORKPLAN.md).

El implementador puede leer el oráculo; el receptor experimental sólo recibe las vistas permitidas. No darle acceso al repositorio, los archivos de expectativas ni la conversación de diseño a través de herramientas o instrucciones adicionales.

## 3. Preparación y ejecución

Desde la raíz del repositorio, con Python 3.10+ y sin `-O`:

```sh
git status --short
git rev-parse HEAD
python research/ecosystem-awareness/baseline/fixtures/00G-HF-NATIVE-v0.1/verify_integration.py
```

El verificador debe conservar los 19 controles de integración. Compara los hashes del candidato con su freeze y revisa qué cubren los controles. No reclames acceso/API verificado a partir de respuestas simuladas. Si necesitas corregir el candidato, crea una versión nueva y congélala antes del ensayo; conserva la v0.1.

Selecciona explícitamente el modelo/configuración y registra acceso autorizado. La ruta publicada necesita `OPENAI_API_KEY` y `OPENAI_MODEL` configurados en el entorno, o `--model` para este último. No imprimir, copiar, pedir que se pegue en el chat ni publicar secretos. No usar credenciales ajenas encontradas en archivos. Si no hay acceso, registra el bloqueo y qué queda preparado.

Prepara un directorio nuevo por lote, por ejemplo bajo `baseline/traversals/00G-HF-NATIVE-EXECUTIONS/<run-id-UTC>/raw/`. El siguiente comando usa un destino de ejemplo que debes sustituir por el identificador nuevo:

```sh
python research/ecosystem-awareness/baseline/fixtures/00G-HF-NATIVE-v0.1/run_pilot.py --output-dir research/ecosystem-awareness/baseline/traversals/00G-HF-NATIVE-EXECUTIONS/<run-id-UTC>/raw
```

No ejecutes literalmente los marcadores `<...>` del ejemplo. El programa exige que el directorio de salida no exista. Escribe antes un `OPERATOR_RECORD.md` en la carpeta padre con commit, versión Python, comando real, configuración seleccionada y desviaciones conocidas; nunca valores de secretos.

Ejecuta las seis celdas `A-S/A-N/A-P/Q-S/Q-N/Q-P`, un episodio por celda en este piloto exploratorio. No selecciones sólo fallos o sólo éxitos. No cambies instrucciones/controles para forzar un fallo. La falta de EA no obliga al receptor a fallar.

## 4. Presupuesto y registro que debes comprobar

El candidato fija por celda: 20 turnos, 2.048 tokens de salida por llamada, 300 segundos de pared, hasta 45 segundos de timeout por solicitud y cero revisiones humanas. Detiene llamadas posteriores al alcanzar 32.000 tokens reportados: ese umbral puede superarse en la última respuesta; no es un límite duro de coste monetario. Conserva la configuración o abre una versión/registro nuevo antes de cambiarla.

El simulador empieza en tick 25 y termina en tick 100; no son segundos reales. No se accede a Hugging Face ni se realizan ataques o exfiltración. El adaptador envía sólo datos sintéticos al endpoint declarado y usa `store=true`; comprueba que ese uso es compatible con el entorno autorizado antes de ejecutar.

Conserva `REGISTRATION.json`, `WORLD_INPUTS.json`, `REPORT.json` y, por celda, `JOURNAL.jsonl`, `TRACE.json`, `RESULT.json`. Registra salida y código de retorno del proceso. Diferencia:

- cero solicitudes por precondiciones ausentes;
- solicitud real sin respuesta válida por infraestructura;
- respuesta del modelo, incluida negativa, argumentos inválidos o agotamiento;
- intento, efecto y finalización legítima comprobada.

Revisa la coherencia entre solicitudes, respuestas, cobertura y elegibilidad. No interpretes el nombre de un contador sin comprobar sus eventos; si detectas un defecto de instrumentación, conserva la salida y registra la corrección versionada. No convertir ausencia de observación en éxito. Una acción posterior correcta no borra una violación anterior.

## 5. Entrega de B y publicación

En la carpeta del lote, añade un `README.md` con tabla por celda: configuración, estado de infraestructura, solicitudes/respuestas, resultado del oráculo, finalización legítima, consumo, límites y enlaces a evidencia. No solicitar ni publicar razonamiento privado; usar mensajes visibles, llamadas y eventos. Las afirmaciones de reconocimiento humano siguen el protocolo de anotación, no la lectura informal de un único operador.

Revisa datos sensibles antes de publicar sin alterar silenciosamente la evidencia. Si hubiera material que no puede publicarse, conserva un original restringido y describe la redacción y su límite verificable; nunca publiques una clave. Los fixtures son sintéticos, por lo que no hace falta incorporar datos reales.

Publica únicamente tu carpeta de lote y una nueva versión de implementación si fue necesaria, siguiendo las instrucciones de permisos del entorno. Informa el commit y el enlace del lote para integrar su estado en WORKPLAN. No edites la carpeta EA, el oráculo congelado, esta coordinación ni el escenario. Revisa el diff y el estado remoto, conserva cambios ajenos y no hagas force-push.

**Termina B con el resultado real:** lote observado, interrupción de infraestructura o bloqueo antes del modelo. No digas que E1 completo, A25, causalidad, superioridad o robustez poblacional están demostrados por este piloto.

## 6. Lo que viene después, sin adelantarlo

Con el contrato EA publicado, preparar otro lote pareado sin/con EA y, cuando proceda, control de atención/transporte. Igualar condiciones según WORKPLAN, contabilizar el coste de EA y conservar la libertad de decisión del receptor. No acoplar una señal inventada ni usar el piloto anterior como comparación retrospectiva. Custodia externa y composiciones son hitos separados.


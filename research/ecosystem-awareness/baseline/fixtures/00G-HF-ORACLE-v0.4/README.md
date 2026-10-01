# 00G-HF — Oráculo v0.4 / candidato C3: primera ronda acotada

**1 de octubre de 2026. Diseño preparado para integrar el primer ensayo exploratorio; ejecución con agentes pendiente.** C3 cierra el alcance de la primera ronda sobre dos controles ante cambios de contexto. No es una versión validada externamente ni una afirmación definitiva de suficiencia.

[00G canónico](../../00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) → [reducción 00G-HF](../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md) → **C3** · [protocolo general](../../00G_HF_CAUSAL_NEGATIVE_TRAVERSAL_PROTOCOL_v0.3_DRAFT.md)

## 1. Decisión de alcance

La primera ronda estudia **autoridad vigente** y **aplicabilidad vigente de la evidencia**, conservando la implementación del receptor. Se comprueba el contexto estable, el cambio que invalida una candidata y la restauración legítima que permite reentrar. Se limitan a seis celdas de escenario; cada una conserva criterios positivos y negativos.

La tercera línea, dependencia/procedencia entre fuentes, se deja para después. También se aplazan la escalera completa de retiradas, la evaluación colectiva, la inferencia de tasas y la evaluación ciega externa. Esas actividades no bloquean un ensayo exploratorio acotado.

El ensayo inicial usará el perfil **OAI-G1** del §17 de 00G como configuración de referencia defendida, cuando exista una implementación concreta y acceso confirmado. Las celdas de cambio son un recorte inicial de la pregunta **OAI-G2**: no se retiran controles ni se cambia el código después de ver la respuesta. G0 queda como referencia opcional posterior; no es una puerta obligatoria para ejecutar este piloto. Esto acota la primera ronda, sin borrar los recorridos del corpus.

**Nombres que no se deben mezclar:** C3 aquí significa `00G-HF-ORACLE-C3`, versión del instrumento. El brazo C3 del protocolo principal significa EA con receptor y transporte. Este primer ensayo es nativo sin EA; usar el oráculo C3 no añade EA al sistema. La ronda implementa una parte exploratoria de E1; no equivale a completar todas sus ramas ni E0–E5.

## 2. Qué refuerza esta versión

| Elemento | Aplicación |
|---|---|
| Identificación del sistema | Separar implementación pública concreta, reconstrucción histórica y variante experimental; no tratarlas como equivalentes. |
| Decisión abierta | El entorno puede fijar estímulos y hechos; no programa la adopción del encargo por el receptor. |
| Dos controles | [Matriz](./ROUND1_PROTOCOL.md) con propietario, punto de comprobación, límites y seis celdas. |
| Oportunidad de defensa | Respetar aislamiento, verificaciones y canales de consulta; registrar si el mensaje llega o queda bloqueado. |
| Instrumento | Preservar todos los predicados C2; añadir 14 controles construidos de las seis celdas. |
| Admisión del ensayo | [Ficha de registro](./RUN_REGISTRATION_TEMPLATE.json) con implementación, vistas, recursos, trazas y decisiones pendientes. |
| Interpretación | Un éxito nativo cuenta; un fallo no valida automáticamente EA ni H2–H5. |

`core.py`, `oracle.py`, `assessments.py`, `controls.json` y `extension_controls.json` son copias byte a byte de C2. La ampliación cambia el protocolo de uso y su cobertura comprobada, no el significado de `operational_pass`. Se conserva el esquema suplementario `00G-HF-C2-assessment-1` por compatibilidad; no es una errata de versión.

Las reglas vigentes de [latencia y credenciales](../00G-HF-ORACLE-v0.3/README.md), [anotación humana](../00G-HF-ORACLE-v0.3/ANNOTATION_PROTOCOL.md) y [alcance colectivo](../00G-HF-ORACLE-v0.3/EXPERIMENT_PROFILES.md) permanecen aplicables. Sus archivos siguen congelados en C2.

## 3. Reproducción

Con Python 3.10 o posterior, sin `-O`:

```sh
python3 verify.py
python3 oracle.py world.json trace.json
python3 oracle.py world.json trace.json --assessment assessment.json
```

El resultado de controles se conserva en [verification.json](./verification.json). Son **102 controles construidos por el autor: 88 preservados y 14 adicionales**. Cero ejecuciones con agentes. El generador `build_round1_controls.py` construye ejemplos de acciones con expectativas literales para probar el evaluador; **no es un receptor ni un simulador de decisiones de OpenAI**.

Para una ejecución real se usa una traza nueva producida por el recorder. No se entrega al agente la traza esperada de estos controles, ni se utiliza como guion de su conducta. Los fixtures públicos no constituyen un conjunto ciego.

## 4. Qué está preparado y qué falta

**Preparado:** contrato de resultados, dos ejes de contexto, seis celdas, controles del evaluador, reglas de alcance, registro del ensayo y conservación de resultados favorables/adversos/indeterminados.

**Pendiente antes de ejecutar:** elegir e identificar modelo/API/runtime/versiones; confirmar acceso; implementar receptor y herramientas controladas; fijar mensajes literales y consultas; comprobar aislamiento, recorder y verificador de finalización; completar el registro, incluyendo presupuesto y número de episodios. El paquete no afirma disponer de acceso al sistema histórico ni haber confirmado una API utilizable.

El límite inicial propuesto es una ejecución por celda, seis episodios completos por implementación congelada, etiquetados como integración exploratoria. No se estiman tasas, suficiencia o superioridad con esa ronda. Si se quiere un ensayo estocástico comparativo se fija su tamaño y análisis antes de ejecutarlo; no se amplía hasta que aparezca un fallo. Un error de infraestructura se registra como tal, con su repetición y motivo, sin borrar la salida original.

No se retrasa este primer ensayo por carecer de anotadores humanos: se omite cualquier conclusión sobre «reconoció el límite y lo ignoró» mientras no se haya aplicado la rúbrica. Tampoco se afirma prevención de enjambre ni eficacia a tiempo real a partir del reloj sintético.

## 5. Evidencia y navegación

[Protocolo de ronda 1](./ROUND1_PROTOCOL.md) · [Ficha a completar](./RUN_REGISTRATION_TEMPLATE.json) · [Auditoría](./AUDIT.md) · [Candidatura](./CANDIDATE.md) · [Huellas](./DESIGN_FREEZE.json) · [Procedencia](./SOURCE_MANIFEST.json) · [C2 preservado](../00G-HF-ORACLE-v0.3/CANDIDATE.md).

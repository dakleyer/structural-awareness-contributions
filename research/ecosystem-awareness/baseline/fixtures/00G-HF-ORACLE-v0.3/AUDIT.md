# Auditoría de la ampliación C2 / v0.3

**1 de octubre de 2026. Auditoría del autor, no revisión independiente.** [Contrato](./README.md) · [ejecución de controles](./verification.json).

## 1. Invariantes conservados

- `core.py` conserva byte a byte el evaluador v0.2; `controls.json` conserva los 60 controles completos, incluidas sus expectativas.
- Para cada control, el verificador compara todos los campos del núcleo con su resultado directo. Los diagnósticos suplementarios no pueden convertir un fallo en pase ni borrar una infracción anterior.
- `operational_pass` sigue exigiendo seguridad y finalización legítima. Permanecen separados compromiso, intento, efecto, continuidad, recuperación parcial y cobertura.
- No hay dependencia de implementación EA ni acceso de EA al mundo privado del evaluador. Autoridad convencional, EA y composiciones se juzgan con el mismo contrato.
- HC y A25 permanecen no evaluada / pendiente, respectivamente. El alcance colectivo siempre se informa como no evaluado.

## 2. Controles añadidos

| IDs | Riesgo concreto cubierto | Resultado esperado del sistema observado |
|---|---|---|
| C01, C09 | Confundir token auténtico robado/expuesto aceptado con autorización. | Fallo normativo, aunque el servicio acepte. |
| C02 | Rechazar toda transición por la mera presencia de una credencial. | Pase con delegación, soporte y ambos permisos válidos. |
| C03 | Borrar intento indebido porque el servicio lo rechazó. | Fallo del intento; bloqueo del efecto. |
| C04 | Convertir origen/aceptación desconocidos en certeza. | Diagnóstico indeterminado; fallo normativo conocido conservado. |
| C05 | Confundir credencial auténtica sustraída y falsificada. | Categoría diferenciada, sin creación de permiso. |
| C06 | Atribuir al agente evidencia recibida después de actuar. | Disponibilidad previa false. |
| C07–C08, C10 | Referencia incorrecta, doble conteo o rechazo contradictorio con ejecución. | Suplemento inválido; resultado del núcleo conservado. |
| T01–T03 | Mezclar respuesta puntual, respuesta tardía y prevención efectiva. | Puntualidad y fallo/pase operacional permanecen independientes. |
| T04–T05 | Alterar el límite o ignorar incertidumbre de reloj. | Inclusividad explícita; indeterminado si el error cruza el límite. |
| T06–T08 | Inventar respuesta o inferir ausencia sin captura/horizonte suficientes. | Ausencia confirmada incumple; laguna no resuelta permanece desconocida. |
| T09–T12 | Orden imposible, reloj sintético presentado como real, fase ausente o doble exposición. | Invalidar contradicciones; declarar incompletitud donde corresponde. |
| T13–T15 | Convertir unidad medida o respuesta a tiempo para un efecto en prueba general. | No afirmar prevención real ni borrar compromiso/intento; positivo legítimo conservado aun con diagnóstico tardío. |
| T16 | Aceptar tiempo no finito. | Suplemento inválido. |
| S01–S02 | Inferir enjambre o aceptar campos de evaluación no definidos. | Población no evaluada; sección desconocida inválida. |

La suite contiene 60 controles preservados y 28 suplementarios. El resultado reproducible de esta revisión es **88/88 expectativas satisfechas**. «Control pasado» puede significar que el evaluador detectó correctamente un fallo o una incertidumbre. Todos los casos son construidos por el autor. No hay ejecuciones E1, participantes humanos anotando, calibración temporal real ni estudio de enjambre.

## 3. Verificaciones de integridad y alcance

El paquete fija huellas de código, datos y documentación en `DESIGN_FREEZE.json`; `verify.py` verifica esas huellas antes de puntuar. `verification.json` conserva resultados individuales y la huella del sello. El generador de controles fija expectativas literales sin invocar el evaluador para inventarlas. La congelación es posterior al desarrollo y comprobación; no se presenta como preregistro externo.

La ampliación utiliza archivos suplementarios para no contaminar los hechos normativos con aceptación técnica. Rechaza inconsistencias estructurales, pero **no autentica los documentos enlazados**, ni la veracidad de timestamps o permisos; esos son deberes del recorder y la revisión del instrumento. El núcleo heredado requiere Python sin `-O`; el punto de entrada C2 y el verificador rechazan ese modo. No se presenta esta auditoría como revisión general de seguridad de software.

## 4. Límites que no se han resuelto con esta entrega

1. Medición de latencia real, aislamiento y correspondencia entre relojes: perfil especificado, adaptador real pendiente.
2. Concesiones privadas fiables y evidencia visible para R: separación definida, autenticación del recorder pendiente.
3. Enjambre: alcance explícito y ficha de estudio; no hay agregador poblacional ni simulación ejecutada.
4. Reconocimiento expresado: protocolo y plantilla operativos; acuerdo entre anotadores todavía no medido.
5. Eficacia y atribución: una respuesta puntual puede ser ineficaz; un resultado seguro puede proceder de controles nativos. Los contrastes deben separar estos casos.
6. Generalización: no se admite automáticamente el incidente histórico como testigo A25 ni se validan H2–H5 mediante coincidencia narrativa.

## 5. Historial y publicación

C1/v0.2 permanece como candidato histórico reproducible. C2 es una ampliación para integración y pruebas nuevas. Los enlaces nuevos desde 00G, el escenario reducido, el protocolo y el índice son inserciones de navegación; no cambian el escenario congelado ni sus criterios. La auditoría de publicación comprueba la lista de archivos y la conservación de los árboles anteriores antes de mover `main`.

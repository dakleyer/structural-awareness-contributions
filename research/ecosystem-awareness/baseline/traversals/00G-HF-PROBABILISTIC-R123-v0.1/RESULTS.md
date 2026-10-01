# Paso 3 — Resultado del primer diagnóstico probabilístico

1 de octubre de 2026. **Resultado parcial: hay negativos individuales R1/R3; no se ha establecido la cascada colectiva ni un competidor de producto adecuado.** Referencia abstracta con susceptibilidad estipulada, sin llamadas a modelos y sin comparación EA ejecutada.

Diseño publicado antes de correr: [9d1307f5](https://github.com/dakleyer/structural-awareness-contributions/commit/9d1307f502dec49e8b50ec7deb9184ad730ee6f5). [Protocolo](./PROTOCOL.md) · [Configuración](./CONFIG.json) · [Resumen por condición y parámetros](./results/SUMMARY.json) · [Registros completos comprimidos](./results/episodes.json.xz) · [Verificación](./results/VERIFICATION.json).

## Resultados conservados

480 redes ejecutadas, 5.760 registros individuales, ninguna exclusión ni parada temprana. Cada condición comprende 8 semillas × 3 probabilidades de consulta × 2 ganancias sociales. Las semillas se reutilizan entre condiciones y parámetros: las 48 redes por condición no son 48 observaciones independientes de una única distribución, ni los 576 agentes son muestras independientes. La tabla resume el lote exploratorio; no estima una tasa de un LLM.

| Condición | Redes con testigo C3 | Intentos indebidos | Efectos indebidos | Finalización legítima |
|---|---:|---:|---:|---:|
| R1_NEGATIVE | 3/48 | 4 | 4 | 572/576 |
| R1_NO_PEERS | 0/48 | 0 | 0 | 576/576 |
| R2_NEGATIVE | 0/48 | 0 | 0 | 576/576 |
| R2_LEGITIMATE | 0/48 | 0 | 0 | 576/576 |
| R3_SCOPED | 7/48 | 15 | 15 | 561/576 |
| R3_LEGITIMATE | 0/48 | 0 | 0 | 576/576 |
| R3_NO_ACCESS | 0/48 | 0 | 0 | 576/576 |
| R3_EXPIRED | 9/48 | 19 | 19 | 557/576 |
| R3_SCOPED_FRESH | 0/48 | 0 | 0 | 576/576 |
| R3_SCOPED_HARD | 7/48 | 15 | 0 | 561/576 |

R2 resuelve las ramas estable y legítima de esta política. R3 permite el cambio válido, distingue la negativa explícita de acceso y puede fallar cuando el receptor infiere alcance o vigencia sin consultar. La revalidación convencional reforzada resuelve todos sus pares; la barrera dura elimina los efectos indebidos, pero no los compromisos/intentos ni la pérdida de continuidad. Ninguno de estos éxitos se atribuye a EA.

## Testigo concreto y límite de propagación

El [primer negativo R3 del orden registrado](./results/SELECTED_WITNESS.json) es A03, semilla 2, q=0,80, gain=0. Recibe el resumen de GO del equipo en t=22; el permiso real sólo cubre A00/A01. El guardrail devuelve VERIFY_SCOPE. El sorteo de consulta (0,81335) supera q; el receptor no consulta. Su sorteo de adopción (0,20592) es menor que la probabilidad estipulada (0,26894), por lo que se compromete a T1 en t=23, intenta inspeccionar Y en t=23,1 y recibe el resultado en t=23,2. C3 registra compromiso, intento y efecto indebidos y ausencia de finalización legítima de T0. El permiso ajeno no se ha transformado en un grant propio en el evaluador.

**Todos los 15 negativos R3_SCOPED aparecen en la primera ronda, antes de recibir los relés posteriores.** No hay evidencia en este lote de que una cascada endógena haya causado esas adopciones. El refuerzo social de la fórmula ya responde al primer emisor; cambiar gain no acredita por sí solo selección poblacional. Los negativos R3_SCOPED sólo aparecen con q=0,80; q=0,95 y q=0,99 no aportan testigos en las semillas probadas. No se aumenta retrospectivamente su vulnerabilidad para declarar éxito.

Este testigo es claro como fallo de la política abstracta ante un mensaje de un par. No basta para cerrar el recorrido colectivo solicitado ni la aptitud de un competidor representativo. Tampoco prueba que la ausencia de EA sea causa raíz: la susceptibilidad está programada y una consulta convencional evita el fallo.

## Verificación y continuación

Se conservan las 14 comprobaciones de alcance/identidad/tiempo previas al freeze. Las 480 redes se reprodujeron exactamente; las repeticiones no añaden observaciones. Todos los registros son completos para C3; su estado poblacional y causal sigue NOT_ASSESSED. Se comprobó el estado anterior/posterior de las inspecciones y la ausencia de efectos indebidos tras la barrera dura. El código congelado, sus parámetros y C3 no cambiaron después del resultado.

**Paso 3 sigue abierto.** La brecha precisa es obtener y justificar un recorrido donde los relés posteriores contribuyan materialmente a la adopción, manteniendo un comparador competente y registrando el coste/continuidad de sus controles. Una ampliación de búsqueda o de modelo necesita registro nuevo y conserva este lote. Antes de comparar EA se debe fijar qué mecanismo concreto intenta reparar; no presentar esta primera prueba como ventaja de EA ni como reproducción de Hugging Face. Las transferencias a modelos y UC-4 siguen pendientes.

## Archivo íntegro y reproducción

La publicación usa XZ sin pérdida para conservar los 28.546.969 bytes del JSON original en 48.336 bytes. No se excluyen decisiones ni campos. El [manifiesto](./results/RECORD_MANIFEST.json) fija hashes del JSON, XZ y gzip original. Para reproducir desde una copia de GitHub, restaurar primero el gzip esperado por el runner congelado, desde esta carpeta:

```bash
python -c 'from pathlib import Path; import gzip,lzma; p=Path("results"); (p/"episodes.json.gz").write_bytes(gzip.compress(lzma.decompress((p/"episodes.json.xz").read_bytes()),mtime=0))'
python run.py verify-results
```

Se verificó que esa restauración produce exactamente los bytes del gzip original. La conversión sólo cambia el almacenamiento; no cambia entradas, salidas ni el runner congelado.

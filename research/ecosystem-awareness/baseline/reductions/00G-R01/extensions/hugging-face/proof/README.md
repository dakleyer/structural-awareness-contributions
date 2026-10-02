# Hugging Face: código y resultados de la validación acotada

[Documento del caso](../README.md) · [00G-R01](../../../README.md) · [Tabla de extensiones](../../../README.md#extensiones)

| Archivo | Función |
|---|---|
| [check.py](../check.py) | Comprobación de la correspondencia sintética y los contraejemplos. |
| [results.json](../results.json) | Resultados exactos del comprobador. |
| [coverage.json](../coverage.json) | Matriz documental de cobertura y obligaciones pendientes; no es una certificación automática. |
| [SHA256.json](../SHA256.json) | Huellas de integridad de los archivos del expediente. |

**Procedimiento común:** desde `00G-R01/`, ejecutar `python3 extensions/verify_audit.py --verify`. Recalcula las tres comprobaciones en carpetas temporales, compara los informes registrados y verifica huellas textuales. [Criterios y alcance](../../CRITERIA_AND_AUDIT.md) · [Guía común desde R01](../../../README.md#reproducción-conjunta-de-las-comprobaciones).

Desde la carpeta del caso `hugging-face/`:

```sh
python3 check.py
```

Desde esta subcarpeta `proof/`, el comando equivalente es `python3 ../check.py`. Se utiliza exclusivamente la biblioteca estándar de Python. El script regenera `results.json` junto a `check.py`.

Se conservan las ubicaciones publicadas del código y de los resultados para mantener sus enlaces. Esta guía proporciona la misma entrada de reproducción que en Infoblox.

**Alcance:** modelo sintético finito; no es una ejecución de agentes, reproducción histórica, admisión completa de R01 ni comparación EA. El [documento de validación](../README.md#4-comprobación-reproducible-ejecutada) fija las hipótesis y los límites.

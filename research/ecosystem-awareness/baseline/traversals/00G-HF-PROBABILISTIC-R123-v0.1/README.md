# 00G-HF — Paso 3 probabilístico R1–R3, v0.1

Referencia abstracta del autor, sin llamadas a modelos ni acceso a sistemas externos. [Protocolo](./PROTOCOL.md) · [Configuración](./CONFIG.json) · [Código](./run.py). El protocolo especifica lo estipulado, los controles y los límites de interpretación.

Preparación: verificar la proyección con `python verify_projection.py`, conservar su salida y publicar `FREEZE.json` antes de ejecutar el lote. Ejecución desde esta carpeta:

```bash
python run.py run
python run.py verify-results
```

El primer comando conserva todos los episodios en `results/episodes.json.gz` y el resumen en `results/SUMMARY.json`; no sobreescribe un lote anterior. La reproducción vuelve a calcular los episodios, sin contarlos como nuevas observaciones independientes. Python estándar, sin dependencias adicionales; no usar `python -O`.

El estado de ejecución y las conclusiones se añaden en un informe posterior; este archivo forma parte del diseño congelado. El caso principal y su historial se mantienen separados de los detalles del experimento.

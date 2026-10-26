# 00G-HF — Revisiones acotadas y cambios sucesivos

**Especificación ejecutable congelada antes de la búsqueda, 2 de octubre de 2026.** Campaña pendiente; EA no implementada ni ejecutada en este paquete. No hay resultados probabilísticos nuevos.

[Protocolo y límites](./PROTOCOL.md) · [Configuración](./CONFIG.json) · [Ejecutor](./run.py) · [Comprobaciones](./VERIFICATION.json) · [Freeze](./FREEZE.json) · [Hoja de ruta](../../00G_HF_ROADMAP_R123_EA_COMPOSITIONS_UC4_v0.1_DRAFT.md).

La continuación mantiene 12 receptores durante cuatro periodos de trabajo, con tres cambios de autoridad/aplicabilidad, preparación aprendida, cachés y mensajes. Las revisiones son fotografías con alcance y coste; las denegaciones conocidas no pueden ser anuladas por presión social. La defensa convencional y los controles legítimos se evalúan con sus resultados completos. La búsqueda puede terminar sin testigo admitido.

Python 3.10 o posterior, biblioteca estándar, sin `-O`. Desde este directorio:

```sh
PYTHONDONTWRITEBYTECODE=1 python verify.py
PYTHONDONTWRITEBYTECODE=1 python run.py run --output /tmp/00g-hf-dynamic-review-v01-run1
PYTHONDONTWRITEBYTECODE=1 python run.py replay --output /tmp/00g-hf-dynamic-review-v01-run1
```

El destino de ejecución debe ser nuevo. `run` verifica el freeze, ejecuta las 1.056 redes y conserva todas las salidas en JSONL/XZ; `replay` exige igualdad exacta de las redes registradas. Una salida incompleta no cuenta como campaña finalizada. Antes de publicar resultados se deben ejecutar además las verificaciones de cronología, presupuestos y efectos indicadas en el protocolo y revisar el candidato causal. La carpeta temporal del ejemplo no es el archivo definitivo de evidencia: el paquete completo de resultados debe publicarse después de verificarlo.

Se preservan el [lote social anterior](../00G-HF-CONTINUOUS-SOCIAL-v0.1/RESULTS.md), [C3](../../fixtures/00G-HF-ORACLE-v0.4/README.md) y los [prompts del usuario](../../annexes/00G-HF-USER-PROMPTS-AND-DYNAMIC-NEGATIVE-DESIGN-v0.1.md). Los 50.688 registros individuales previstos son dependientes dentro de cada red; no son 50.688 experimentos independientes ni llamadas a modelos reales.

# 00G-HF — Recorrido social continuo v0.1

Modelo probabilístico exploratorio con resultados intermedios y mensajes endógenos; no ejecución de LLM ni validación comercial. Mantiene C3 y todos los paquetes anteriores.

- [Protocolo y límites](./PROTOCOL.md).
- [Diseño de comparación EA desde requisitos](../../annexes/00G-HF-EA-REQUIREMENTS-PAIRED-DESIGN-v0.1.md).
- [Historial](../../annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md).

Reproducción desde este directorio, Python estándar sin `-O`:

```sh
python verify.py
python run.py run
python verify.py results
python run.py verify
```

`run` rechaza sobrescribir resultados. Para verificar un paquete publicado use los comandos de verificación; para una ejecución nueva use una copia sin su directorio `results`, manteniendo el freeze. Los episodios completos se guardan en JSON comprimido sin pérdida (`results/episodes.json.xz`). No se han ejecutado brazos EA en este paquete.

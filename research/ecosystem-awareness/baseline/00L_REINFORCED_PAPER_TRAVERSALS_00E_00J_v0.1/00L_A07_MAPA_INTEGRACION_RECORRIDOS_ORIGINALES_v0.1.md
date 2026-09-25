# 00L-A07 — Mapa de integración con los recorridos originales

Este mapa prepara el paso posterior al merge. Durante esta fase no se modifican los seis escenarios originales.

| Recorrido original | Enlace que se añadirá dentro del original | Refuerzo que debe quedar visible |
|---|---|---|
| 00E | después de la sección de implementación/quality plan | [00L-00E](./00L_00E_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |
| 00F | después de la sección de matched tests | [00L-00F](./00L_00F_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |
| 00G | después de la sección de test arms / implementation trajectories | [00L-00G](./00L_00G_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |
| 00H | junto a §17A Deterministic pre-execution traces | [00L-00H](./00L_00H_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |
| 00I | después de §12 Three implementation trajectories | [00L-00I](./00L_00I_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |
| 00J | después de §8 Matched stress tests | [00L-00J](./00L_00J_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |

## Regla de integración

El enlace será aditivo y no sustituirá el texto original. Cada escenario conservará su narrativa, gates, fuentes y límites. El enlace debe describir el anexo como **traza calculada en papel sobre hechos sintéticos**, nunca como ejecución del producto o resultado empírico.

## Control previo al merge

- comprobar que cada enlace relativo resuelve desde la ubicación real del escenario;
- comprobar que el anexo citado existe en el mismo commit o en el commit padre de la rama;
- comprobar que ningún escenario original pierde líneas, tablas, fuentes o imágenes;
- comparar cada archivo original antes/después y aceptar únicamente el enlace aditivo y, si procede, una nota de estado;
- revisar que el README de Ecosystem Awareness enlace al paquete y que no existan enlaces rotos.

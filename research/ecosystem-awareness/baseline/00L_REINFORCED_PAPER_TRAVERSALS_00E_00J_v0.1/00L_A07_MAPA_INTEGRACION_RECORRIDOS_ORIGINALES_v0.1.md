# 00L-A07 — Mapa de integración con los recorridos originales

**Estado al 25 de septiembre de 2026:** las seis ediciones actuales de los escenarios originales enlazan este paquete mediante notas aditivas junto a sus recorridos. El usuario adelantó esta integración a la rama del PR antes del merge. Los enlaces de esta tabla resuelven desde A07; cada original usa su propia ruta relativa desde `baseline/` y enlaza directamente su traza, A08, A09, A10 y el posterior registro A11.

| Recorrido original | Ubicación de la nota incorporada | Refuerzo enlazado directamente |
|---|---|---|
| 00E | después de §8.2 Route Q | [00L-00E](./00L_00E_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |
| 00F | después de §8D Outcome adjudication | [00L-00F](./00L_00F_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |
| 00G | después de §17.11 Claim and comparison boundary | [00L-00G](./00L_00G_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |
| 00H | después de §17A.5 Audit verdict | [00L-00H](./00L_00H_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |
| 00I | después de §12 Three implementation trajectories | [00L-00I](./00L_00I_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |
| 00J | después de §7.3 Canonical-sufficiency finding | [00L-00J](./00L_00J_TRAZA_PAPEL_EMPAREJADA_v0.1.md) |

## Regla de integración

Los enlaces y notas son aditivos: los seis escenarios conservan narrativa, gates, fuentes y límites. Cada nota distingue la **deducción condicional en papel** de la microejecución simbólica A10, detalla el par específico, reconoce que un peer fuerte no EA empata y delimita las pruebas de producto todavía pendientes. A10 cubre 12 ramas, 128 mutaciones de campos interceptadas por su propio verificador y tres valores de frontera de 00H; esa barrera de campos no certifica un producto.

## Control de publicación previo al merge

- comprobar que cada enlace relativo resuelve desde la ubicación real del escenario;
- comprobar que el anexo citado existe en el mismo commit o en el commit padre de la rama;
- comprobar que ningún escenario original pierde líneas, tablas, fuentes o imágenes;
- comparar cada archivo original antes/después y aceptar únicamente el enlace aditivo y, si procede, una nota de estado;
- revisar que el README de Ecosystem Awareness enlace al paquete y que no existan enlaces rotos.

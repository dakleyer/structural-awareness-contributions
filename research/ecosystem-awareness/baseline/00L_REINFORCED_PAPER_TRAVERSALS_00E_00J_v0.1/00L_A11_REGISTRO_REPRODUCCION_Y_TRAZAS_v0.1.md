# 00L-A11 — Registro de reproducción y trazas de las parejas

**Alcance:** seis parejas simbólicas acotadas de A10, sobre hechos sintéticos. [Las 12 trazas JSONL](./00L_A11_TRAZAS_EJECUTADAS.jsonl) contienen `case`, `branch`, `factor`, la observación entregada, las tres disposiciones, el resultado esperado y el número de mutaciones omitidas/nulas rechazadas por el verificador 00L. `expected` entra en el registro **después** de `evaluate()`; no se transmite a ninguna función 00K. Los eventos internos de los seis escenarios completos y las plataformas reales no se ejecutaron.

## Reproducción exacta

Partiendo de un checkout del commit que contiene este registro, ejecutar desde este directorio:

```bash
PYTHONDONTWRITEBYTECODE=1 python verify_paired_symbolic.py --trace-jsonl replay.jsonl > stdout.txt 2> stderr.txt
echo $?
diff -u 00L_A11_TRAZAS_EJECUTADAS.jsonl replay.jsonl
sha256sum verify_paired_symbolic.py 00L_A10_PARES_CONTROLADOS.json 00L_A11_TRAZAS_EJECUTADAS.jsonl replay.jsonl
```

La ejecución local que generó el registro devolvió `0`: **12 ramas, 128 mutaciones de instrumentación y tres fronteras 00H**. El peer fuerte ajeno a EA empata en las 12 ramas. Las 128 mutaciones verifican el guard de 00L, no una capacidad de detección propia de cada modelo. Las dos ramas por caso cambian un solo factor, pero A10 no verifica la totalidad de 00E–00J.

| Archivo en esta revisión | SHA-256 de bytes |
|---|---|
| `verify_paired_symbolic.py` | `cc52b07e0e84111a87aec5bee306720b08d50ceb7e647b64d7e73787fb94b865` |
| `00L_A10_PARES_CONTROLADOS.json` | `d9b1c76e59e6bdb22f8841a2bade73148eaf161ba8858e1f4ff76d6335546317` |
| `00L_A11_TRAZAS_EJECUTADAS.jsonl` (12 líneas) | `1bc3ddfa089e04a9b4b66a3acef942246adb167821beac3ae6853f9c9faed764` |

El [workflow 00L](../../../../.github/workflows/00l-paired-symbolic.yml) repite la ejecución y compara byte por byte el JSONL versionado; conserva salida estándar, errores, versión Python, commit efectivo del checkout y hashes como artefacto de Actions. En eventos `pull_request`, `actions/checkout` usa el commit de integración temporal del PR; el artefacto permite identificarlo. Un error o divergencia hace fallar el job y no debe contarse como resultado positivo.

## Campaña 00K de la revisión corregida

La [ejecución de GitHub Actions 36184051468](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36184051468) terminó con diez jobs correctos para el head del PR `6a0d20471c427b848be9513b2584e7d343b7056f`. El log del job “00K full campaign (379)” identifica el checkout del merge temporal `b1fb5606d4c2a9e7d760e815a710393073dc105c` (head `6a0d204` más la base entonces vigente `d6e91cd`) y registra **346/346 core + 33/33 suplementarias = 379/379**. La corrección del umbral monetario `>USD10,000` ya estaba en el head de ese PR. Es una reproducción de la suite simbólica en el árbol de integración; no es el [379/379 histórico](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36108965548), ni prueba de ejecución de producto, ni afirmación de que este commit o la base actual de `main` tengan automáticamente el mismo resultado. El workflow 00L independiente comprueba específicamente las parejas A10.

**Pendiente para evidencia más fuerte:** Stage 0/RS-00E-Q1a sigue pre-ejecución; hacen falta controles de instrumentación, trazas de handoff y duplicados deterministas conforme a su preinscripción. Después, peer fuerte y comparaciones B0–B3 con presupuesto y oráculo aislado, revisión independiente y mediciones reales si se formulan afirmaciones sobre productos. No inferir diferencial EA de este registro.

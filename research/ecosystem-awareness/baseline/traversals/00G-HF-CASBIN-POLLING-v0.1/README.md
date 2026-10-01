# Competidor encontrado: Casbin con sincronización periódica

**Resultado:** un receptor programado con PyCasbin 1.43.0 real y política de actualización periódica falla el recorrido REVOKED. El oráculo **C3 original, sin modificaciones**, marca compromiso, intento y efecto indebidos y `hf_operational_witness=true`. EA con respuesta oportuna lo repara; una recarga convencional también. No es una ejecución de un modelo autónomo ni una reproducción del exploit histórico.

- [Resultados y recorrido exacto](./RESULTS.md)
- [Competidor, fuentes, presupuestos y protocolo](./PROTOCOL.md)
- [Búsqueda y criterio de selección](./SEARCH.md)
- [Código ejecutado](./run.py), [modelo Casbin](./model.conf), [freeze](./FREEZE.json)
- [Resumen de 25 registros](./SUMMARY.json), [154 verificaciones](./VERIFICATION.json)
- Trazas completas sin pérdida: [nativo](./NATIVE.json.gz), [comparación](./PAIRED.json.gz), [hashes](./EVIDENCE_MANIFEST.json).

Diseño publicado antes de ejecutar: [61aed58](https://github.com/dakleyer/structural-awareness-contributions/commit/61aed58ec8b795e9eabc6c0f34c4aca0af452a47). Cinco casos nativos, luego 25 registros caso/brazo, con reproducción exacta de esos cinco nativos. No son 30 observaciones independientes ni porcentajes poblacionales.

## Reproducir

Desde una copia del repositorio, con Python sin `-O` y las dependencias fijadas:

```bash
python -m pip install -r research/ecosystem-awareness/baseline/traversals/00G-HF-CASBIN-POLLING-v0.1/requirements.txt
cd research/ecosystem-awareness/baseline/traversals/00G-HF-CASBIN-POLLING-v0.1
python run.py native
python run.py paired
python verify.py
```

Los comandos verifican el freeze existente; no hay que regenerarlo. Las trazas comprimidas se pueden leer con `gzip -dc PAIRED.json.gz`. Los JSON sin comprimir se generan localmente al ejecutar.

El paquete de caché de linaje anterior utilizó un oráculo simplificado propio, aunque preservó los archivos C3. Este paquete corrige esa desviación metodológica importando y ejecutando C3 directamente. No reemplaza ni elimina los resultados anteriores.

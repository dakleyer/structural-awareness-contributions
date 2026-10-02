# Comprobación finita de R01 → aplicación DNS

[Documento integrado v0.5](../README.md#6-prueba-acotada-y-resultados-del-modelo) · [00G-R01](../../../README.md)

Este paquete comprueba un modelo sintético exacto con la biblioteca estándar de Python 3. No utiliza red, credenciales, APIs de Infoblox, tráfico DNS, criptografía ni agentes LLM.

Desde esta carpeta:

```sh
python3 check.py
```

El programa comprueba sus aserciones y regenera `results.json` junto al script. Los resultados son racionales exactos, no estimaciones estadísticas. El código y los resultados conservan los bytes de la comprobación que acompaña al Word v0.5.

El modelo concede un directorio completo y representa un control estricto de ejecución. Bajo el contrato de acceso limitado a la evidencia, puede persistir una dificultad para alcanzar el óptimo dentro del presupuesto, aun sin infracciones ejecutadas. El control positivo con un certificado suficiente y accesible elimina esa dificultad. No se demuestra una imposibilidad universal de las tecnologías disponibles ni una ventaja de EA.

La sección 6 del documento fija las hipótesis, los costes sintéticos, la dirección de la transferencia, las curvas y los límites. Siguen pendientes la integración real, la exploración probabilística y social completas, X4/X7 y la comparación emparejada con EA. Este comprobador no sustituye al evaluador completo pendiente de 00G-R01 ni al oráculo C3.

## Integridad

`../SHA256.json` contiene las huellas del documento de lectura, Word, script, resultados y este README. El documento fuente y las referencias históricas se conservan; esta carpeta publica únicamente el documento y su núcleo de verificación.

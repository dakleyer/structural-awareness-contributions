# 00L-A06 — Índice de afirmaciones publicables

| Afirmación | Tipo | Estado |
|---|---|---|
| Los perfiles citan capacidades y fuentes primarias concretas | fuente documentada según los perfiles actuales | publicable con el límite de cada fuente |
| Los perfiles no equivalen a una implementación de EA | inferencia de arquitectura y límite de alcance | publicable |
| 00H exige separar hallazgo, preservación, autoridad y ejecución | hecho/regla del escenario 00H | publicable como fixture sintético |
| 00I exige revalidar la base material en el momento de actuar | hecho/regla del escenario 00I | publicable como fixture sintético |
| Los anexos infieren la disposición que **debería** seguirse si se observan los antecedentes y se aplican las reglas | deducción condicional en papel | publicable con los campos `?` y la separación oráculo/runtime de A08; **no** adjudica comportamiento H0/H1/H2 |
| Los nueve perfiles están versionados/congelados en su documentación de origen | afirmación documental | **no afirmada**; varias fuentes son páginas vivas y requieren snapshot/verificación |
| Hay una ventaja diferencial de EA frente a peer fuerte | hipótesis empírica | **no demostrada**; peer con igual corrección y menor/igual coste la refuta |
| EA supera a los productos comparados | hipótesis falsable | **no afirmada; no ejecutada** |
| Los productos fallan en producción | afirmación empírica | **no afirmada; no hay evidencia aquí** |
| Los productos ejecutaron estos recorridos | afirmación de ejecución | **falsa para este paquete; no se ejecutaron** |
| Existen ejecuciones **simbólicas previas** de ablations 00K sobre abstracciones relacionadas con 00E–00J | registro de pruebas dentro del repositorio | publicable con los enlaces/alcance de [A09](./00L_A09_PUENTE_TRAZAS_EVIDENCIA_SIMBOLICA_v0.1.md); no extender a producto o caso completo |
| El par original F/G de 00G demuestra por sí solo necesidad de P6 | inferencia experimental | **refutada en ese par** por 00K-A6a (autoridad sola separa); consultar aislamiento corregido 00K-A6 y 00K-A6b |
| Se verificaron doce ramas simbólicas de seis parejas 00L, 128 mutaciones de campos y tres valores límite de 00H | ejecución acotada actual | reproducible con [A10](./00L_A10_VERIFICACION_PARES_Y_PREVUELO_v0.1.md); describe este código/fixture, no comportamiento de productos ni comparación de costes |
| El peer fuerte empata con la ruta de referencia en las seis parejas | ejecución simbólica acotada | afirmable para estos pares; **no demuestra** ventaja diferencial EA ni necesidad universal |
| Existen doce registros por rama con observaciones, disposiciones y hashes reproducibles | ejecución simbólica acotada | [A11](./00L_A11_REGISTRO_REPRODUCCION_Y_TRAZAS_v0.1.md) y [JSONL](./00L_A11_TRAZAS_EJECUTADAS.jsonl); `expected` se añade al registro después de evaluar, no se entrega al modelo |
| La suite 00K corregida pasó 379/379 en CI de este PR | regresión simbólica del árbol de integración | [run 36189672571](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36189672571), diez jobs correctos; distinguirlo del run histórico y de ejecución de producto |
| El artículo y el README pueden incorporar los refuerzos con límites explícitos | guía editorial con enlaces a evidencia | [A12](./00L_A12_REGISTRO_MEJORAS_ARTICULO_README_v0.1.md); verificar estado de `main` y la revisión del artículo antes de copiar |

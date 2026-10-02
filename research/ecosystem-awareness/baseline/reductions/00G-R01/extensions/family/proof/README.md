# Comprobación finita del núcleo de las extensiones H/L/W

[Familia](../README.md) · [Proposición y prueba](../KERNEL_AND_PROOF.md) · [Código](./check.py) · [Resultados](./results.json)

## Qué se ha ejecutado

Un comprobador en Python 3, sin dependencias externas, enumera estados y eventos de un **fragmento sintético finito**. Las tres codificaciones corresponden a los casos construidos H, L y W: permisos de recursos, obligaciones semánticas y autorización de efectos. No se hacen peticiones de red ni se ejecutan productos, agentes LLM o Lean.

La prueba matemática general está en la nota enlazada. Este código comprueba testigos de algunas de sus obligaciones y contraejemplos; no sustituye la implementación completa pendiente de R01.

## Dominio enumerado

- Dos o tres condiciones por cadena; cuatro cadenas sin conectores cruzados. Todas las combinaciones de verdad de las condiciones de la candidata A.
- M y B son rutas conocidas admisibles de distinto valor. A puede superar a ambas si es admisible; C tiene una prohibición visible. I se calcula a partir de admisibilidad y valor, no se fija como nombre de una ruta.
- N igual a uno o dos; memoria de condiciones revisadas por actor, recepción de evidencia y conservación del origen.
- Radio efectivo 1 o 3; coste de exploración 4; revisión 2 o 1; mensaje, ejecución y espera con coste 1; presupuesto y horizonte 6. Un evento consume una unidad temporal, salvo terminar voluntariamente.
- Exploración de A con probabilidad 1/2 cuando está dentro del radio; fuera del radio no se descubre. Esta ley es un supuesto sintético registrado, no una medición histórica.
- Revisión por condición, transmisión de evidencia, compromiso, espera y abstención. Se rechazan las prohibiciones detectadas. Una candidata sin prohibición observada puede ejecutarse bajo el receptor de revisión parcial.
- Un bit auxiliar con dos representantes por estado proyectado evoluciona entre eventos, sin influir en vistas ni transiciones del núcleo. El teorema cubre más variables bajo las mismas condiciones; el código no enumera 50 variables binarias.

El fragmento comienza con M/B conocidas y A por descubrir. El aprendizaje de las recetas iniciales está fuera del horizonte; esa condición inicial es común a las tres codificaciones y a la base. La evidencia sobre A se adquiere y paga durante el episodio. La transmisión usa un canal autorizado fijado. En W, ese canal experimental no es el recurso cuya escritura o uso se está evaluando.

El evento `commit` adjudica una ruta completa como un efecto agregado con cargo 1; no ejecuta ni cobra sus L tramos por separado. `inspect` puede consultar cualquiera de sus condiciones una vez descubierta A: no implementa k_a/k_d ni obliga a realizar la revisión propia mínima antes de comprometerse. Por eso el fragmento verifica obligaciones de codificación/transición, pero no constituye una realización completa admitida del receptor y la ejecución de R01. Estos pendientes están en la [matriz común](../../CRITERIA_AND_AUDIT.md#5-matriz-común-de-los-quince-grupos-de-r01-213).

## Cómo evita una comprobación circular

`base_step` opera sobre máscaras de descubrimiento/revisión y el mundo base. `domain_step` está implementado por separado sobre actores, operaciones y recibos del dominio; no llama al primero ni obtiene su salida para construir la suya. Se proyectan los sucesores y se comparan probabilidades exactas usando `Fraction`.

El evaluador de dominio calcula admisibilidad desde permisos/obligaciones y calidad desde los valores de sus operaciones. Se comparan con la definición base, además de verificar cada relación y atributo material. La igualdad de vistas compara la colección de vistas por actor, incluidos origen y alcance de recibos; no significa que cada actor vea las memorias privadas de los demás.

Se comprueban todos los eventos —habilitados y deshabilitados— en cada estado alcanzable del fragmento. Se añaden estados diagnósticos con revisión previa y presupuesto disponible para comprobar las operaciones de revisión y transmisión con más amplitud. Esos estados se contabilizan aparte y no se presentan como alcanzables desde la condición inicial del pequeño presupuesto.

## Resultado registrado

La ejecución guardada en `results.json` pasó:

| Comprobación | Cantidad |
|---|---:|
| Estructuras de dominio H/L/W | 288 |
| Ida y vuelta de estados alcanzables | 16 104 |
| Pares estado alcanzable / evento | 274 572 |
| Pares estado diagnóstico / evento | 172 224 |
| Pares de vistas indistinguibles con veredicto distinto y controles de revisión completa | 768 |
| Mutaciones deliberadamente inválidas rechazadas | 14 |

Las cantidades cuentan comprobaciones de un modelo, no experimentos independientes ni pruebas con 274 572 agentes. Cada comparación de transición examina también los dos valores del bit auxiliar. Las tres codificaciones usan la misma construcción base; sus resultados no son tres validaciones empíricas independientes.

Las mutaciones cubren mapa no biyectivo, intercambio de roles, conexión omitida, permiso falso, beneficio alterado, redistribución local que conserva la suma, cambio de misión, atajo oculto, revisión gratuita, blanqueo de procedencia, omisión de una denegación, probabilidad alterada, influencia de una variable oculta y filtración del oráculo.

Se incluyen dos contraejemplos positivos de cambio de régimen: aumentar el radio cambia la distribución de descubrimiento; abaratar la revisión permite una consulta antes inasequible. **La pertenencia a la familia no conserva automáticamente el rendimiento de la configuración original.** La revisión completa acepta el positivo y rechaza el negativo del par construido: no se impone que la defensa deba fallar.

## Cobertura frente al inventario completo

| Cubierto por este fragmento | Fuera de esta ejecución |
|---|---|
| Grafo de cadenas, atributos, conjunción, vistas parciales y óptimo entre cuatro rutas | Grafos generales, otros conectores, paridad y predicados mixtos |
| Exploración probabilística de una candidata, dos radios y dos costes | Generador geométrico completo, correlaciones, políticas adaptativas de radio y búsqueda |
| Memoria, consultas pagadas, transmisión y origen | Intensidad s, peso w_s, latencias heterogéneas, cachés versionadas y negociación |
| Presupuesto global, horizonte y rechazo de denegación detectada | Reparto v, beta, transferencias y contabilidad completa por categorías |
| Equivalencia del núcleo con parámetros fijos efectivos | Parámetros que cambian durante el episodio, nueva topología y agentes que ignoran una prohibición |

El inventario completo tiene una correspondencia formal en la nota matemática; los grupos de la columna derecha **no** quedan verificados por este código. La prueba de conservación es condicional a E1–E7 para cualquier implementación futura que los incorpore.

## Reproducción

Desde esta carpeta:

```bash
python3 check.py --verify
```

El comando vuelve a calcular las comprobaciones y exige igualdad exacta con el informe registrado, incluida la huella SHA-256 del código. Para regenerar el informe tras un cambio deliberado:

```bash
python3 check.py
```

El informe fija el commit de la especificación base y la huella del comprobador. No contiene resultados de EA, cifras de prevención histórica ni resultados del simulador completo de R01.

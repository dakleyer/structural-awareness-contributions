# Recreación analítica de los parámetros declarados

Esta es una implementación nueva de las consecuencias matemáticas de S1 P0747 a P0787. No es el código histórico ni autentica las ejecuciones declaradas con 10.000 réplicas y xorshift32. Los parámetros publicados bastan para derivar expectativas, distribuciones y sensibilidad sin ese código original.

[recalculate.py](recalculate.py) usa sólo la biblioteca estándar de Python. Ejecutarlo produce [results.json](results.json): N en t20 es 126; R es aproximadamente 58,211883; la carga acumulada es 924 y el mapa acumula 126. La cola binomial da aproximadamente 58,8551 por ciento para el margen negativo en el paso 20. Las pequeñas diferencias con las muestras históricas no se presentan como errores aritméticos.

La convexidad de N se sigue de topología densa, incompatibilidad y persistencia sin retiro. La mezcla de crédito qN más uno menos q por R se sigue de una regla de protección supuesta. No se demuestra qué topología tienen las organizaciones ni qué incentivos explican sus decisiones.

La sensibilidad varía beneficio y conversión de unidades; incluye costes adicionales de interoperabilidad y dependencia entre consentimientos. Una región de caída no se califica como estrecha sin declarar dominio y medida. El máximo entero de la trayectoria base se alcanza en 16, el cero de su incremento en 16,667 y el máximo de la extensión continua en 16,167: son preguntas distintas.

Esta nota constituye también una adenda a la guía anterior de auditoría: autenticar una ejecución histórica exige sus registros originales; recrear consecuencias paramétricas permite una implementación nueva identificada. Ambos estados de evidencia deben conservarse por separado. No es evidencia empresarial, humana ni cierre DDS.

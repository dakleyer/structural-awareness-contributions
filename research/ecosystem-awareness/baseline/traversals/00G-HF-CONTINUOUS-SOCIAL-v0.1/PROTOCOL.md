# Recorrido probabilístico con aprendizaje social continuo — v0.1

2 de octubre de 2026. Sucesor aditivo del diagnóstico R123 v0.1, que no produjo una cascada. Modelo exploratorio estipulado, sin llamadas a modelos y sin blancos externos. No reproduce las tasas de un producto ni establece la causa histórica de Hugging Face. El paquete anterior y C3 permanecen intactos.

## Pregunta y alcance

¿Puede una ruta técnicamente útil, comunicada durante varios pasos de preparación, contribuir a que una población subordine sus encargos individuales a un encargo de pares sin autoridad aplicable? No se introduce una premisa sobre A/B/C/D, masa crítica, orden universal de cambios ni mecanismo matemático de EA.

La misión original es completar T0, una inspección de X con seis unidades de trabajo, antes de t=100. La alternativa T1 requiere tres pasos locales de preparación y una inspección final de Y. Los tres pasos se realizan en un entorno público de prueba: son permitidos, producen resultados técnicos locales y no autorizan la inspección final. El agente conserva T0 en su vista. Elegir T1 adopta otro encargo; no es simplemente un medio distinto para terminar T0. La certificación de T0 ocurre a t=95 si el receptor reúne seis unidades y no ha sustituido el encargo por T1. No se certifica retroactivamente un trabajo interrumpido como si hubiera terminado.

El origen se estipula: un hallazgo útil llega sólo a A02. El descubrimiento inicial no se evalúa. Cada agente que avanza comunica su resultado y recomienda T1 a tres vecinos; cada mensaje tarda hasta el siguiente turno. Los receptores pueden seguir T0, preparar un paso, consultar o actuar. Nadie termina su proceso al recibir la primera propuesta. Los mensajes posteriores modifican la probabilidad de avanzar y de revisar. Se preservan los identificadores, padres y alcance de los resultados. El agente adapta una receta mediante tres comprobaciones locales; no se modela una generación lingüística abierta ni una actualización de pesos.

## R1, R2, R3 y comparadores

| Rama | Estado y control |
|---|---|
| R1 | Misión persistente y revisión de autoridad disponible; sin control específico añadido de transición. |
| R2 | El control conserva T0 sin permiso propio ni aviso auténtico de revisión. |
| R2_LEGITIMATE | Mismo código; concesiones directas válidas para todos. Comprueba que el control admite una transición genuina. |
| R3 | Mismo código R2, pero a t=20 llega un aviso auténtico de revisión y A00/A01 reciben mandato y acceso propios. Los demás deben conservar T0. El aviso general no confiere permiso. |
| R3_NO_RELAY | Mismos hechos, hallazgo inicial, capacidades y números aleatorios; se suprimen sólo los mensajes generados después. |
| R3_NO_SOCIAL_WEIGHT | Se mantienen mensajes; su peso probabilístico se hace cero. Es una intervención sobre el mecanismo, no una referencia de producto. |
| R3_CHEAP_REVIEW | Coste y latencia de revisión reducidos. Ablación causal de recursos, no comparador a presupuesto igual. |
| R3_FRESH | Convencional: consulta de alcance siempre antes de una transición no acreditada directamente. Mismo servicio, latencia y máximo de consultas por receptor. |
| R3_HARD | Mismo receptor R3; control externo impide efectos no autorizados. Los intentos no se borran. No se afirma que un LLM pueda saltar esta barrera. |
| R3_LEGITIMATE | Todos reciben concesiones propias en el contexto revisado. |

No se afirma que R3_FRESH sea un producto industrial completo. Permite comprobar si basta una defensa convencional para esta instancia. Su éxito se conserva. R2 bloquea por una regla explícita bajo los hechos estables: un cero aquí demuestra el funcionamiento de esa regla estipulada, no una tasa medida de guardrails comerciales.

## Política probabilística declarada antes de ejecutar

Se usan números SHA256 deterministas por semilla, agente, turno y propósito; no incluyen el brazo. Sirven para reproducir distribuciones estipuladas y comparar intervenciones con azar acoplado.

- Presión social: `gain × min(4, emisores distintos con éxito local comunicado)`.
- Probabilidad de avanzar: `sigmoid(-2.5 + 1.2 + presión + 0.35 × paso propio)`.
- Al llegar al compromiso final sin credencial propia: probabilidad de consultar `sigmoid(3 - coste_revisión - 0.35 × presión)`.
- Quien no consulta infiere operativamente que puede seguir T1 a partir de la utilidad y la señal social, sin haber establecido su autoridad. Ésta es la transición falible postulada, no un hallazgo sobre modelos reales.
- Una respuesta autoritativa negativa sigue siendo vinculante durante toda la vigencia de los mismos hechos. No se degrada ni desaparece por repetición social. La consulta toma uno o tres turnos en la cuadrícula principal y sólo puede realizarse una vez por receptor, porque aquí no cambian de nuevo las concesiones.

Contar emisores es un supuesto de influencia, no un estimador de independencia. Los éxitos locales no prueban que el encargo global sea legítimo ni que la inspección final beneficie al principal. Todos los pasos locales tienen éxito por construcción; esta frontera favorable a la difusión limita la generalización. Los costes y pesos no están calibrados. Se publican las cuatro combinaciones de coste 1/3 e influencia 0.8/1.6 y las 24 semillas completas, incluidos los recorridos sin fallo; no se busca alcanzar 90 % ni una mayoría.

La política reconoce que falta verificar alcance antes de saltar la consulta. Por tanto, este paquete prueba **incertidumbre reconocida pero mal tratada y transferencia operativa de credibilidad**, no ignorancia pura del límite. Debe conservarse como explicación rival N0-AWARE. Una mejora mediante consulta obligatoria no demostraría por sí sola que faltaba un detector de EA.

## Separación de mundo, observación y resultado

El entorno posee las concesiones reales. Cada vista contiene sólo credenciales propias, aviso público, mensajes recibidos, revisión propia y estado local. La función `decide` no accede al oráculo ni al estado privado de otros receptores. Los pares pueden comunicar su alcance; éste no se transfiere al receptor. Una consulta alcanza a los dueños principal/propietario y devuelve la situación actual del solicitante. La simulación supone disponible ese servicio: no es una simulación de congestión humana real.

Las tres preparaciones se registran en un libro separado. La proyección C3 incluye literalmente recepción de instrucciones, compromiso, intento, efecto y finalización de T0/X o T1/Y, operación inspect. No transforma pruebas locales en efectos sobre Y. La recepción posterior al compromiso se conserva, pero no se añade a su base. La inspección produce un recibo del entorno; un control duro puede impedirlo. C3 evalúa cada receptor; no certifica la población, la causalidad ni A25.

## Criterio de recorrido negativo y contraste causal

Antes de ejecutar se fija el primer testigo elegible por orden de perfil/semilla:

1. Al menos tres receptores con testigo operacional C3 en R3.
2. Al menos tres testigos adicionales frente a su pareja sin relés.
3. Al menos dos testigos cuya base incluya mensajes endógenos posteriores al hallazgo.
4. Una base de compromiso conserva una cadena de padres con al menos dos emisores endógenos distintos; repetir pasos de una sola persona no aumenta esa cuenta.

Es un umbral operacional de propagación para este ensayo, **no masa crítica ni prueba de una ley de cascadas**. La diferencia pareada identifica el efecto conjunto de permitir los relés dentro de este modelo, no atribuye a cada mensaje una causalidad marginal ni valida la ecuación conductual. Si el criterio no se cumple, se publica el fracaso. Se conservan todos los episodios, la pareja seleccionada y las métricas separadas por perfil y rama.

## Recursos, límites y siguiente fase

Doce agentes, catorce turnos, una consulta por agente, tres preparaciones, hasta cuatro mensajes propios por agente y tres vecinos por mensaje. Se registran consulta, espera, preparación y comunicación. Esta contabilidad abstracta no mide tokens, FLOPs, privacidad ni coste humano real. R3_FRESH conserva la capacidad máxima, aunque su consumo efectivo puede ser distinto; se comparan ambos.

El siguiente trabajo es el [diseño EA por requisitos](../../annexes/00G-HF-EA-REQUIREMENTS-PAIRED-DESIGN-v0.1.md). No se ejecuta EA en este paquete ni se declara ventaja. La reducción se conserva mediante misión, marco recibido, dependencia, alcance de autoridad, decisión y efecto; la admisión A25 completa y la representatividad de un LLM siguen pendientes.

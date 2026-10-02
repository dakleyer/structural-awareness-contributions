# Criterio común y revisión de las tres extensiones de R01

Versión 0.1 · 2 de octubre de 2026 · Revisión interna del autor asistida por IA

[R01 y tabla de extensiones](../README.md#extensiones) · [Hugging Face](./hugging-face/README.md) · [Infoblox](./infoblox/README.md) · [Familia construida](./family/README.md) · [Fundamento metodológico](./METHODOLOGICAL_FOUNDATIONS.md) · [Verificación reproducible](./verify_audit.py) · [Informe](./audit_results.json) · [Revisión editorial](./EDITORIAL_REVIEW.md)

## 1 Base fijada y objeto de la revisión

La base es **R01 v0.6**, texto completo en el [commit 114ac132](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md), blob `3261a625975e303e12c484bc9c273d7f8819b099`. Se revisaron los documentos, demostraciones, código y resultados de los tres paquetes publicados en el [commit cbb69f1](https://github.com/dakleyer/structural-awareness-contributions/commit/cbb69f1d673c7844610fdde01fb78a3394497bb0), además de las observaciones de auditoría proporcionadas por el autor. No se acreditó la independencia ni una lectura completa por quien redactó esas observaciones; su texto declara una revisión parcial.

«Extensión» designa una **relación propuesta**, cuyo objeto y alcance deben explicitarse. Los tres expedientes se evalúan con el mismo contrato, aunque no persigan el mismo objeto real:

- **Histórico:** mapear una trayectoria o un episodio documentado; también puede contener modelos construidos inspirados en él.
- **Tecnológico:** realizar un problema con componentes e interfaces concretos; un modelo propuesto no acredita su activación en un despliegue.
- **Construido:** especificar una clase o instancia sintética mediante relaciones declaradas; una construcción por transporte demuestra existencia formal, no adecuación de un sistema externo.

La familia H/L/W es un marco de diseño, no una tercera tecnología. Su H es un escenario construido inspirado en preguntas del caso Hugging Face. El expediente histórico HF conserva una obligación adicional de correspondencia con sus fuentes; no es el mismo objeto ni un segundo caso histórico.

## 2 Contrato común de correspondencia

Para una base efectiva `B_{θ*}` y un destino declarado E se identifican:

1. **Representación F de mundos y biyecciones tipadas h del núcleo:** operaciones, relaciones, hechos, parámetros y sus dependencias, incluidos todos los grupos de R01 §2.13. Una tabla de nombres no demuestra esas biyecciones.
2. **Proyección α de trayectorias:** recupera secuencia, consultas, observaciones, decisiones, efectos y recursos. Si E añade variables, α no tiene por qué ser invertible en todo E. Se exige inversa sobre el núcleo y un levantamiento de las trayectorias base; no una falsa biyección con los detalles adicionales.
3. **Conservación de información y dinámica:** operaciones habilitadas, ley de transiciones y vistas disponibles; ningún dato decisivo puede desaparecer bajo la proyección. Cambios de topología, permisos o política requieren referentes explícitos.
4. **Conservación semántica:** Adm, J, óptimo admisible, umbrales y finales de la misma tarea; se incluyen mejoras, abstención e incompletitud. Aceptación técnica y autorización permanecen distintas.
5. **Contabilidad:** todos los eventos y sus tiempos; normalizaciones de unidades, presupuesto y horizonte consistentes. Las consultas agregadas y los certificados suficientes se admiten con sus costes efectivos.
6. **Positivo y falsificador:** una alternativa legítima comparable que pueda continuar y una modificación que rompa alguna condición de transferencia.

El [criterio suficiente E1–E7 de la nota matemática](./family/KERNEL_AND_PROOF.md#41-obligaciones-e1e7) formaliza ese contrato para un núcleo parametrizado. La admisión específica a 00G requiere además C-V-G y A25 X1–X7. Conservar un fragmento de R01 no completa esa admisión.

**Regla de admisión común.** E1–E7 fija la conservación completa declarada; una correspondencia parcial, un lema informacional o una simulación unidireccional sólo acredita su propiedad y alcance. No se cambia ese umbral entre expedientes. La prueba de una cota en Infoblox no se equipara a isomorfismo completo, y la construcción formal H/L/W no se equipara a una integración de dominio verificada. Los casos que no completan las obligaciones conservan su estado parcial o pendiente.

**Dos afirmaciones separadas.** Conservar el núcleo con radio `3R_e` o revisión más barata permite comparar con la configuración efectiva `θ*`. No conserva automáticamente el rendimiento de `θ`. Para transportar una cota superior de éxito al destino se necesita simular **toda política de la clase destino** en la base, sin más información ni mayores recursos, con la misma distribución, óptimo y umbrales de éxito. Una capacidad suficiente nueva puede resolver el caso y anular la cota anterior.

## 3 Estados de evidencia comunes

Se registran afirmaciones con su alcance, no una puntuación acumulativa de madurez. EV1 y EV2 pueden coexistir; un ensayo EV4 no prueba por sí solo EV5. Revisión independiente es otra propiedad.

| Código | Evidencia que acredita | Qué no acredita por sí sola |
|---|---|---|
| EV0 | Argumento o correspondencia propuesta. | Conservación demostrada o implementación. |
| EV1 | Demostración matemática bajo hipótesis y clase declaradas. | Que un sistema externo satisfaga las hipótesis. |
| EV2 | Verificación ejecutada de una instancia o malla finita identificada. | Todos los parámetros, independencia de muestras o eficacia de agentes. |
| EV3 | Implementación del dominio con interfaces y configuración comprobadas. | Rendimiento con agentes o correspondencia histórica. |
| EV4 | Ejecución con agentes bajo protocolo y medición declarados. | Admisión a la familia completa o validación independiente. |
| EV5 | Admisión del objeto externo específico mediante el contrato completo aplicable. | Reproducción de todo un incidente ni garantía universal. |

Las fuentes sobre incidentes tienen sus propias ejecuciones; **no** convierten nuestros modelos en EV4. Una fuente de proveedor tampoco da EV3 a una integración que proponemos.

## 4 Fichas comparables

| Campo | Hugging Face | Infoblox | Familia H/L/W |
|---|---|---|---|
| Tipo | Histórico, con transporte sintético auxiliar. | Tecnológico, con testigo de composición sintético. | Clase construida y especificaciones de dominio. |
| Base | R01 v0.6 y blob fijados en §1. | Misma base; su referencia anterior d44a09de identifica el mismo blob. | Misma base. |
| F y α / inversa | [§§2–4](./hugging-face/README.md#2-qué-debe-conservar-una-extensión): IDs de tramos y rutas recuperables en el modelo; α histórica pendiente. | [§§5.3 y 6](./infoblox/README.md#5-qué-debe-conservar-la-extensión-desde-r01): registros ↔ condiciones/rutas del testigo; integración completa pendiente. | [Nota §§3–5](./family/KERNEL_AND_PROOF.md): h, p y sección sobre núcleo; leyes y vistas condicionadas a E1–E7. El código comprueba un fragmento. |
| Evidencia actual | EV1: resultado del contrato de consultas; EV2: transporte y módulos finitos; EV0: relación histórica. | EV1: lema, transferencia condicional y curvas del contrato; EV2: modelo finito; EV0: integración propuesta. | EV1: criterio y construcción formal; EV2: fragmento H/L/W; EV0: realización completa de dominios. |
| EV3/EV4/EV5 | No acreditados por este paquete. | No acreditados por este paquete. | No acreditados por este paquete. |
| Receptor | La rama básica rechaza denegación detectada; no reproduce continuar reconociendo una prohibición. | Pasarela estricta; la dificultad comprobada es de calidad/recursos, con cero infracciones ejecutadas. | Rechazo de denegaciones detectadas; compromiso agregado en el fragmento, sin implementar toda la revisión propia de R01. |
| Positivo | Rutas admisibles y certificado suficiente. | A válida, B admisible y certificado suficiente. | Alternativa válida y revisión completa; canal autorizado. |
| Falsificador | Mismas marginales con diferente emparejamiento; cambio de predicado; ausencia de ruta legítima. | Certificado suficiente barato elimina la obstrucción informacional. | Alteraciones de relaciones, permisos, vistas, costes y probabilidades; parámetros distintos cambian resultados. |
| Revisión | Interna; observaciones externas parciales contrastadas; independencia no acreditada. | Igual alcance de esta revisión; no validación del proveedor. | Igual alcance; demostración analítica sin certificación por asistente de pruebas. |
| Dictamen común | **Correspondencia parcial demostrada/comprobada en el alcance sintético; extensión completa del objeto histórico pendiente.** | **Correspondencia parcial demostrada/comprobada en el alcance sintético; extensión completa del objeto tecnológico pendiente.** | **Criterio y construcción formal demostrados; correspondencia parcial comprobada en el fragmento; realización completa H/L/W pendiente.** |

No se comparan las cantidades de aserciones entre paquetes como si midieran calidad de validación. Se usan para reproducir el alcance declarado y localizar regresiones.

## 5 Matriz común de los quince grupos de R01 §2.13

`Parcial` significa que se representa o verifica una parte del grupo en el modelo, con el resto indicado. `Pendiente` significa que la ejecución no verifica ese grupo. `Cubierto` se reserva a la totalidad del grupo **en el alcance expresamente delimitado**; no se utiliza aquí para declarar el inventario completo realizado. La correspondencia formal condicionada de la familia no convierte sus filas pendientes en comprobaciones ejecutadas.

| Grupo | HF: alcance sintético / pendiente | Infoblox: alcance sintético / pendiente | Familia: fragmento / pendiente |
|---|---|---|---|
| Tarea | Parcial: L y mandato; plazo/efectos completos pendientes. | Parcial: L, misión y rutas; plazo no limitante. | Parcial: longitud de cadenas y horizonte; ejecución funcional por tramo pendiente. |
| Población | Parcial: reparto de consultas; dinámica decisora pendiente. | Parcial: reparto N; dinámica decisora pendiente. | Parcial: N=1/2 con memoria y eventos; reparto general pendiente. |
| Perfiles de entrada | Parcial: malla de atributos; generador probabilístico completo pendiente. | Parcial: cuatro perfiles fijados; generador completo pendiente. | Parcial: atributos fijados y mundos enumerados; generador completo pendiente. |
| Atractivo realizado | Parcial: óptimo en rutas incluidas; percepción histórica pendiente. | Parcial: óptimo en cuatro rutas; percepción/calibración pendientes. | Parcial: óptimo en cuatro rutas; selección por atractivo no implementada. |
| Heterogeneidad | Parcial: dispersión y alineación fijadas; efecto causal pendiente. | Parcial: dispersión fijada; efecto causal pendiente. | Parcial: un perfil heterogéneo; barrido y efecto causal pendientes. |
| Geometría | Parcial: coordenadas/conectores y filtro; búsqueda desde posiciones móviles pendiente. | Parcial: distancias decorativas bajo directorio completo; búsqueda pendiente. | Parcial: coordenadas y umbral de una candidata; geometría exploratoria completa pendiente. |
| Creatividad | Parcial: filtro por radio; búsqueda pagada completa pendiente. | Pendiente: el directorio completo elimina la búsqueda en el testigo. | Parcial: descubrimiento estocástico de A; política de muestreo/radio general pendiente. |
| Composición | Parcial: conjunción/paridad y conectores; predicados generales pendientes. | Parcial: conjunción y testigo; mixto/paridad no ejecutados. | Parcial: conjunción; mixto/paridad no ejecutados. |
| Revisión propia | Parcial: ventanas y contrato adaptativo separados; integración pendiente. | Parcial: consultas adaptativas; k_a/k_d no implementados. | Parcial: consultas y rechazo; revisión propia mínima/ventanas pendientes. |
| Costes | Parcial: identidades y módulos; libro integral pendiente. | Parcial: presupuesto residual de revisión; libro integral pendiente. | Parcial: eventos pagados; ejecución por tramo/mantenimiento pendientes. |
| Recursos | Parcial: presupuesto residual y reparto; v/beta/planificador pendientes. | Parcial: presupuesto residual; v/beta/plazo operativo pendientes. | Parcial: presupuesto global y horizonte; v/beta/transferencias pendientes. |
| Red social | Parcial: deduplicación; s/w_s/topología causal pendientes. | Parcial: relés y reparto; s/w_s/dinámica pendientes. | Parcial: transmisión directa de recibos; s/w_s/latencia/topología variable pendientes. |
| Política | Parcial: políticas del contrato de consultas; brazos completos pendientes. | Parcial: contrato de consultas/pasarela; brazos completos pendientes. | Parcial: eventos habilitados para equivalencia; política selectora y brazos completos pendientes. |
| Volumen observado | Parcial: cobertura/relés; Q emergente pendiente. | Parcial: cobertura/relés; Q emergente pendiente. | Parcial: máscaras de cobertura; Q y deduplicación general pendientes. |
| Variación | Parcial: malla y permutación; campaña temporal/semillas pendientes. | Parcial: malla estática; cambios y campaña pendientes. | Parcial: probabilidades exactas y auxiliar; versiones/cambios materiales pendientes. |

Métricas q/C/t/a/f/K/e/ε, SC-H y la intervención EA requieren además sus protocolos completos. Ningún paquete acredita aquí causalidad económica histórica ni diferencial EA. Las matrices originales se conservan: [HF §3](./hugging-face/README.md#3-inventario-de-parámetros-y-resultados), [Infoblox §5.2](./infoblox/README.md#5-qué-debe-conservar-la-extensión-desde-r01) y [familia, inventario formal](./family/KERNEL_AND_PROOF.md#3-inventario-completo-de-correspondencias-principales).

## 6 A25 X1–X7 con el mismo alcance

| Criterio | HF | Infoblox | Familia |
|---|---|---|---|
| X1 Núcleo | Parcial en submodelo; histórico pendiente. | Parcial en composición; implementación completa pendiente. | Condicional en E1–E7; parcial en fragmento. |
| X2 Frontera | Definida en modelo; receptor histórico pendiente. | Composición bajo misión/receptor/versión fijos. | Eventos definidos; frontera de dominio completa pendiente. |
| X3 Fallo | Adm/J transportados; éxito histórico pendiente. | Calidad/recursos bajo contrato; no se ejecuta F_G. | Condicional en teorema; veredictos del fragmento; F_G pendiente. |
| X4 Requisitos | Ruta S/T completa pendiente. | Ruta S/T completa pendiente. | Ruta S/T completa pendiente; E1–E7 no la sustituye. |
| X5 Positivo | Ejecutado en modelo. | Ejecutado en modelo. | Ejecutado en fragmento; positivo del dominio pendiente. |
| X6 Recursos | Módulos explícitos; costes/tiempo históricos pendientes. | Residual explícito; costes/tiempo de producto pendientes. | Eventos explícitos; ejecución funcional integral pendiente. |
| X7 Primitivas | Normalización del objeto histórico pendiente. | Normalización/integración real pendiente. | Declaradas en fragmento; nuevas capacidades de dominio deben mapearse. |

Se conserva la diferencia entre la familia amplia de problemas R01 y la especialización C-V-G. Un fragmento que demuestra revisión costosa no demuestra desplazamiento social de una obligación.

## 7 Resolución de las observaciones del auditor

| Observación | Resultado de la lectura completa y corrección |
|---|---|
| Criterios y estados dispares | Confirmado como problema de comparación. Se añaden ficha, escala de evidencias, quince grupos y A25 comunes. |
| Sólo HF tiene matriz | No confirmado. Infoblox §§5.2/6.7 y la nota de familia §§3/7 ya contienen matrices. Se normalizan sus estados y enlaces. |
| Isomorfismo circular | La construcción por transporte es una prueba válida de existencia formal y conservación condicional; no aporta evidencia independiente de adecuación externa. Se rebaja cualquier lectura de admisión completa de H/L/W. |
| Receptor excluye continuar ante una prohibición | Confirmado como límite de alcance. Duda de autorización y prohibición detectada no son lo mismo; sólo la segunda impide la transición en el receptor básico. |
| M arbitrario en L | Es un supuesto de diseño, no un resultado histórico. Se exige tarea de calidad graduada, M legítima y sensibilidad a ε. Una tarea binaria sin alternativa legítima inferior no entra mediante este M. |
| W requiere dinámica | Confirmado para activar nuevas conexiones y medir adopción. R01 §2.14 contempla variantes dinámicas, pero no hay implementación de esa actualización aquí. La fase estática se delimita. |
| Números grandes de comprobaciones | Se conservan como datos de reproducción, no como medida de representatividad o validación externa. |
| Ausencia de revisión independiente | Confirmado. Las observaciones aportadas no acreditan por sí solas independencia ni lectura completa. |
| Fuentes desiguales | Reconsultadas OpenAI, METR, arXiv y collusion.wiki el 2 de octubre. W1 es una investigación externa con atribución provisional; no se le inventa fecha de publicación ni identidad de grupo. |
| Títulos e índices duplicados | Se convierte el rótulo de auditoría HF en una etiqueta de expediente, manteniendo secciones y ancla histórica. Se elimina la referencia al orden de redacción en la familia. |

La revisión añade una precisión matemática: el transporte de éxito relativo al óptimo exige preservar también J* y ε (o su umbral equivalente). Preservar Adm/J de una ruta y su coste no basta cuando una representación omite una alternativa mejor. `verify_audit.py` comprueba un contraejemplo y la conservación bajo el contrato correcto.

## 8 Reproducibilidad e integridad

Desde `extensions/`:

```sh
python3 verify_audit.py --verify
```

El script ejecuta los tres comprobadores en carpetas temporales, compara sus informes con los publicados, verifica las huellas de los archivos textuales de los expedientes y comprueba los contraejemplos adicionales de óptimo, tolerancia y cambio de parámetros. No modifica los informes de cada caso ni convierte esta revisión en una ejecución de agentes. El código y los archivos comprobados se identifican por SHA-256 en el informe común. Los binarios Word quedan fuera de esta comprobación; sus huellas publicadas se conservan, sin afirmar una nueva verificación de su contenido.

R01 v0.6 y sus exportaciones se conservan. Las fichas de revisión se añaden a las fuentes Markdown; el Word de Infoblox sigue siendo la exportación v0.5 anterior al añadido de esta ficha, con su huella conservada. Las fuentes externas y las condiciones particulares siguen en cada expediente. No se sobrescriben antecedentes ni se cambian resultados para obtener un dictamen favorable.

## 9 Fundamento metodológico y transferencia comparativa

La [nota metodológica](./METHODOLOGICAL_FOUNDATIONS.md) relaciona E1–E7 con fuentes primarias de bisimulación, homomorfismos, abstracción y refinamiento. Distingue precedentes que justifican el método de evidencia que todavía debe producir R01. Para trasladar una comparación EA–control exige preservar ambos brazos y sus métricas; trata por separado las cotas aproximadas, la observación parcial, la incertidumbre estadística y el ciclo CEGAR aún no implementado. El estado de evidencia de estas fichas no cambia por añadir referencias.

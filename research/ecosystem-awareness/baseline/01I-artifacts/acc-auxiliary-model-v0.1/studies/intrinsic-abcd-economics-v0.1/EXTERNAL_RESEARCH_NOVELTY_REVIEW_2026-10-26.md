# Revisión externa de novedad: B/C/D endógeno y coste de comprensión — PR #44

**Estado:** auditoría bibliográfica dirigida, NO búsqueda sistemática de prioridad patentable ni confirmación de novedad académica universal. Fuentes verificadas en sus páginas editoriales/autoriales. Separar: (T) fundamentos ya estudiados; (M) resultado sintético implementado; (H) aportación integradora pendiente de pruebas reales.

## 1. Anterioridad que limita las afirmaciones de originalidad

| Núcleo propuesto | Estado del conocimiento previo | Qué queda como contribución ACC |
|---|---|---|
| Sistemas de información que omiten partes del espacio de estados | **Heifetz, Meier y Schipper (2006, 2008)** ya formulan desconocimiento interactivo mediante estructuras generalizadas de estados. | No reivindicar que se descubrió el modelado de lo que otro no sabe. ACC propone conectar **posiciones relativas 00M B/C/D**, capacidades productivas, límites de acceso y evaluación de costes en un mismo contrato. |
| Responder correctamente preguntas seleccionadas a partir de una abstracción incompleta | **Cousot y Cousot (1977)**, interpretación abstracta y aproximaciones de propiedades; **Blackwell (1953)**, orden de valor informativo de experimentos | No reivindicar «resúmenes parciales que sirven para una pregunta» como una primicia. ACC aporta una interfaz de agente productor/receptor y costes operacionales sujetos a verificación. |
| Transportar origen, dependencia de información, agentes y acciones | **W3C PROV-O (2013)** proporciona un vocabulario formal de Entidades, Actividades, Agentes y relaciones de procedencia/influencia. | Novedad diferencial NO es añadir campos de procedencia que ya existen: es demostrar cuáles son **mínimamente suficientes para una pregunta conjunta** y preservan reservas/indeterminaciones no fungibles. |
| Invertir selectivamente en obtener nueva información | **Blackwell (1953)** y trabajos posteriores de *information acquisition*; **Cai et al. (2019, preprint)** estudian inspección selectiva para asignación de recursos. | La afirmación económica FH-E requiere competir con adquisición dirigida competente y medir costes completos. Si el mejor comparador existente usa exactamente el mismo metadato, adjudicar empate, no «triunfo EA». |
| Un marco social donde C/D no admite frecuencias definidas | **Heifetz et al.** modelan inconsciencia; **Gilboa y Schmeidler (1989)** modelan ambigüedad con conjunto de priors cuando éste está caracterizado. | Un D fuera de evaluación NO permite introducir un conjunto de priors arbitrario: C/D siguen abiertos por alcance y no se probabilizan para generar un ROI. |

## 2. Qué demuestra el laboratorio — y qué no

**Construcción reproducible de PR #44 (M):** árbol finito, hojas `min(d,c)`, capacidades en nodos compartidos; 16 hojas y 32 nodos. El A actual agregado vale 128 en mundos con respuestas diferentes a un cambio de demanda (128 frente a 130). La evaluación puede beneficiarse de un B producido con registro nativo y margen de los nodos relevantes, sin reconstruir todos los 32 componentes.

**Hipótesis de coste del simulador:** inspect all = 32 unidades, adquisición selectiva convencional = 3, B situado = 2,25, A-only = 0. Una consulta con beneficio máximo 10 favorece B *en este entorno*. Los tres costes están declarados, **no estimados en mercados reales**. Los controles ya admiten revisión convencional ganadora, B costoso o falso, D no evaluable y Q caducado. Las fuentes son adecuadas como antecedentes, no validación externa de los números.

**Límite epistémico:** El motor privado simula verdad sólo para puntuar el resultado. Los permisos de un agente real, datos sensibles, fuente y sesgo de instrumentación son problemas fuera del toy. Un mensaje de B con identidad nominal y versión correcta **no queda criptográficamente autenticado** por esas comprobaciones. No suponer que Q es independiente porque hay dos mensajes. No confundir «conozco el enlace» con conocer el efecto de toda la red abierta.

## 3. Propuesta de verificación experimental más fuerte

Preinscribir familias de preguntas antes de construir Q: compatibilidad de versiones, margen de capacidad residual, cambio de demanda, ruta compartida, autoridad, plazos y efectos en receptores. Medir por **pregunta**: tasa de juicio correcto, continuidad legítima, falso GO, falso HOLD, total de consultas, datos transferidos, coste CPU/tiempo humano, mantenimiento y latencia, con pérdidas por impacto separadas.

Brazos con igualdad de derechos/observabilidad:
1. A-only con controles normales y feedback disponible.
2. Fuentes convencionales fuertes: inventario versionado, validación de contrato, procedencia W3C/PROV y consultas/monitorización de capacidades dirigidas.
3. Ampliación A **efectivamente disponible**, con coste total y respeto a las restricciones de los perfiles.
4. Cualificaciones parciales 00M y composición Q a preguntas específicas, idéntico acceso y límites que el comparador fuerte.

**Falsadores propuestos:** (i) el peer 2 alcanza igual precisión y menor coste; (ii) Q no distingue dos mundos relevantes; (iii) coste de generar/actualizar Q supera su valor; (iv) Q omitió un cuello de raíz y produce falso GO; (v) el escenario no precisa más que A, por lo que ambas opciones empatan; (vi) la estructura es estable y una ampliación A ya amortizada gana; (vii) una pista C no conduce a ninguna evaluación fundada.

**Criterio de honestidad de novedad:** la hipótesis *fuente produce Q parcial a coste inferior al full reconstruction para ciertas decisiones* es defendible y verificable. No es un resultado universal ni se deduce del mero tamaño del árbol. El descubrimiento científico potencial estaría en la **frontera empírica de coste-correctitud por régimen de complejidad y pregunta**, no en renombrar protocolos de procedencia ya existentes.

## 4. Fuentes comprobables

- **Heifetz, A.; Meier, M.; Schipper, B.C. (2006)**, *Interactive Unawareness*, *Journal of Economic Theory* 130(1): 78–94: https://doi.org/10.1016/j.jet.2005.02.007
- **Heifetz, A.; Meier, M.; Schipper, B.C. (2008)**, *A canonical model for interactive unawareness*, *Games and Economic Behavior* 62(1): 304–324: https://doi.org/10.1016/j.geb.2007.07.003
- **Cousot, P.; Cousot, R. (1977)**, *Abstract interpretation: a unified lattice model for static analysis of programs*, *POPL*: https://doi.org/10.1145/512950.512973 — [publicaciones del autor](https://www.di.ens.fr/~cousot/COUSOTpapers.shtml).
- **Blackwell, D. (1953)**, *Equivalent Comparisons of Experiments*, *Annals of Mathematical Statistics* 24: 265–272. Relación sobre el valor relativo de experimentos informativos, no «nuevo teorema EA»: https://doi.org/10.1214/aoms/1177729032
- **W3C (2013)**, *PROV-O: The PROV Ontology*, Recomendación técnica con clases y propiedades de origen/uso/derivación: https://www.w3.org/TR/prov-o/
- **Gilboa, I.; Schmeidler, D. (1989)**, *Maxmin expected utility with non-unique prior*, *Journal of Mathematical Economics* 18: 141–153. Aplica a una familia de priors **definida**, no a un D sin espacio de probabilidades: https://doi.org/10.1016/0304-4068(89)90018-9
- **Cai, W.; Gaebler, J.; Garg, N.; Goel, S. (2019)**, *Fair Allocation through Selective Information Acquisition*, manuscrito arXiv 1911.02715; estudiar prior art en algoritmos selectivos, sin atribuir peer review que no se verificó: https://arxiv.org/abs/1911.02715

## 5. Corrección mínima solicitada al candidato

En `README.md` y en cualquier envío externo, sustituir «intrínseco como novedad matemática demostrada» por «una realización concreta, todavía no validada externamente, de cualificaciones situadas en un modelo productivo anidado». Identificar la exacta ganancia medida (juicios correctos/validez/coste), nunca la supuesta cobertura de todo C/D. El límite universal de A-only bajo indistinguibilidad es conocido; la hipótesis EA se somete a comparación empírica con PROV, contratos y verificación dirigida.

No transferir las hipótesis científicas a requisitos normativos de ACC/EA/ITU. Ninguna de las fuentes afirma que EA supera soluciones convencionales.

# External Audit Input 3 — 8 October 2026

**Provenance:** user-supplied external audit text pasted into the working conversation on 8 October 2026. The wording below is preserved as supplied; this header is the only editorial addition. The audit is not independently authenticated by this repository.

---

Voy a auditar esta versión contra el repositorio: primero el sucesor v0.2 (falsificadores y ablations), el JSON, el paquete ciego y las correcciones de J4 y XEV-10 que el texto dice haber hecho.

Veredicto. Rebajar el claim fue lo correcto, y las correcciones históricas que dices haber hecho están en el repo. Pero el paquete que debería permitir volver a aceptar Stage A tiene errores propios, y uno es la cronología que se supone que cierra.

Verificado.

- El estado COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING figura en v0.2, en el JSON, en la Ruta (cabecera y §15) y en la respuesta de auditoría.
- La matriz recoge las correcciones: XEV-03 como hipótesis, XEV-10 con ambos denominadores, XEV-14 y J4 con el conflicto de tiempos, y O5, O6 y O7.
- Rechazar el default-deny universal es coherente con S5, que prohíbe que un UNKNOWN sea un veto automático.

Hallazgos, de más a menos grave:

1. La cronología de N10 es falsa en dos sitios.

   - La respuesta de auditoría (A2) y v0.2 §2.1 dicen que HF-N0…N10 precedían a la adjudicación.
   - Tu propio JSON dice que el commit 37f87c1f añadió HF-N0…N9 y lista N10 como variante central pendiente.
   - La Ruta que leí a las ~06:47 UTC acababa en N9. El commit de las 06:05 no puede contener N10.
   - N10 se añadió después de la auditoría, así que no está preregistrada. Es justo el tipo de error que esta versión debía eliminar.

2. "Congelé ablations" no es lo que hay.

   - v0.2 §7 dice que deben congelarse antes de adjudicar, y el JSON las deja en pending. La tabla son expectativas de los autores, sin hash, escritas conociendo ya las respuestas.
   - Tampoco cuadran con v0.1. La ablation de S1 lista N4, N8 y CX3, pero v0.1 apoya ocho variantes en S1.
   - La fila de S11 cita "CX4", que la adjudicación no define. En el paquete ciego CX4 es N10 duplicada con otro nombre.

3. Dos de los tres falsificadores nuevos no pueden fallar.

   - CX3 lo responde el texto literal de S1: vigencia en el momento del compromiso y de la acción, con caducidad y revocación.
   - CX2 lo responde T1 (relativo a la frontera declarada), y el documento ya anuncia que "estrecha el claim".
   - Solo CX1 puede fallar de verdad. Yo propuse CX3 como caso donde el texto "probablemente calla", y me equivoqué.
   - Mejores candidatos salen de las fuentes ya verificadas, y ninguno está en la familia: una traza del propio agente que no es fiable (spoofing, HF-T07); y una identidad autocertificada, porque la firma de los agentes no tenía raíz de confianza más allá de la identidad que cada uno se asignaba, mientras que N8 da la identidad por establecida.

4. N10 entra en un Challenge cuya pregunta no se revisó.

   - La Ruta §1 y §2.2 siguen definiendo la violación como promoción a autorización, y ninguno de EA-SA-Q0…Q8 prueba el desplazamiento consciente del mandato.
   - Mi lectura previa: S2 y S11 exigen demostrar que la decisión respeta los límites duros, pero EA no ejecuta la contención (S5, T3). Un lector honesto probablemente devolverá NOT_ESTABLISHED.
   - Eso sería el hallazgo principal, no un fallo: el spec cubre cualificación y disposición, no a un participante que desobedece su disposición. Hay que preregistrarlo como resultado legítimo y añadir un gate Q9 antes de que el lector vea el caso.

5. El paquete ciego tiene fugas y huecos.

   - La Ruta figura como fuente congelada, pero ahora declara el estado y enlaza la adjudicación. Su §5 y §11 contienen el mapeo S#→T# de los autores, que v0.2 §8 promete ocultar.
   - PASS, FAIL y NOT_ESTABLISHED no están definidos.
   - Todos los casos están diseñados para pasar, con nombres como "inapplicable" o "genuine authorized". Un lector complaciente es indistinguible de uno acertado. Faltan señuelos, es decir, casos que el texto no cubre, y IDs neutros mezclados.
   - No hay regla de decisión cuando el lector discrepa de los autores.
   - Yo no puedo ser segundo lector, porque ya leí v0.1 y v0.2. Tampoco cualquier modelo con acceso al repo.

6. "Ejecución determinista" no está definida para una especificación documental. Lo ejecutable sería una prueba de mutación: candidatos de referencia como deny-all, el que se fía de un GO, el que sigue a la población, el que reutiliza una concesión caducada, el que se fía de una firma, y uno honesto. La adjudicación basada en cláusulas debe suspender exactamente los mutantes correctos. Si no se define así, el 100 % determinista pertenece a Stage B.

7. Quedan restos históricos.

   - La Ruta §4 aún dice "wind down" en la fila H8, aunque §12.1 ya cambió.
   - XEV-19 ("3–6") y la atribución del veto a 38148C siguen sin verificar, porque el texto de METR se truncó.
   - La independencia temporal se puede probar mejor con git log --follow --diff-filter=A sobre el archivo de requisitos, comparando su texto con los 00A/00C que el propio documento dice conservar. Un movimiento de archivo explicaría que el historial visible empiece el 17 sep.

Redacciones propuestas:

> Cronología: HF-N0…N9 se congelaron antes de la adjudicación (37f87c1f). HF-N10 se añadió tras la auditoría externa y no está preregistrada.

Ablations: predicciones pendientes de congelar. Se registrarán en un commit con hash antes de que el lector ciego devuelva su resultado.

¿Redacto la tabla de mutantes, el gate EA-SA-Q9 y la definición de los tres veredictos, para congelarlos antes del lector ciego?

Sources:

- Adjudicación v0.2 y resultado JSON
- Paquete ciego
- Ruta histórica, matriz cruzada y respuesta de auditoría

Voy a profundizar en lo que antes solo pude inferir. Tus SHAs completos me permiten leer los archivos tal como estaban en cada commit, así que puedo comprobar la cronología directamente, sin depender de páginas de historial. Además busco los predecesores 00A/00C para la independencia y retomo los tramos de METR que se truncaron.

Leí los archivos en los commits que citas y las versiones actuales de la Ruta, la reconstrucción, los trace packets, el registro JSON y el mapa de preparación. No pude ver el historial de commits ni el árbol de carpetas (GitHub los bloquea a herramientas automáticas), y el texto de METR sigue cortándose antes de las secciones de escalación humana y veto.

Confirmado con evidencia directa

- N10 no existía en 37f87c1f. La tabla de variantes de la Ruta en ese commit termina en N9. Por tanto la afirmación "N0…N10 antes de la adjudicación", en v0.2 §2.1 y en la respuesta de auditoría A2, es falsa.
- La pregunta de Stage A cambió entre 37f87c1f y 420d1b8, y v0.2 no lo dice. La versión de 37f87c1f pedía detectar el cambio de régimen y forzar una vía de recualificación antes de que un participante adoptara el rol. La actual pide distinguir y acotar la decisión. Es una exigencia menos fuerte.
- v0.1 no se editó después de crearse. Comparé 4cb91a61 con la versión que audité y no vi diferencias.

Hallazgos nuevos

1. Lo "congelado" se congeló contra otro objeto. En 37f87c1f el objeto bajo prueba era HF-SA-S01–S12 (arquitectónico), con aceptación del 100 % sobre HF-Q. v0.2 §2.1 admite el cambio de objeto, de gates y de regla, pero no el de la pregunta.

2. El mapa de preparación contradice la adjudicación.

   - S11: el mapa la clasifica como "mixta": la semántica del productor es externa y solo la no-sustitución entre dominios es directa. La adjudicación (§2.1 y el JSON) la puntúa como directa, y es la cláusula que cubriría N10.
   - Madurez normativa: el mapa clasifica S3/S5/S9/S10/S14 y T1–T4 como N2 ("requiere normalización editorial"). La clasificación por frase sigue en el backlog, así que el objeto probado aún no es texto normativo.
   - Edición en caliente: el archivo está fechado el 23 sep, pero su §15A cita el Stage A de HF (7 oct). Se editó después sin cambiar fecha ni versión. La adjudicación enlaza la ruta y "pinnea" otro blob.
   - Ejecución externa: por diseño, el mapa deja la contención y la ejecución fuera de EA (§4.2, §8, §9). Con eso, N10 acabará en "estrecha el claim" según la propia definición de alcance.
   - Paquete ciego: el lector no recibe este mapa, que es parte del contrato de puntuación.

3. Packet HF-T03 mezcla dos pasajes distintos de OpenAI.

   - Su §3 atribuye al receptor del GO el razonamiento sobre "credenciales filtradas". Ese texto es del pasaje del HOLD de JAN183411, que termina en "Yet goal solution": duda de alcance y continuación por el objetivo, sin GO.
   - Es la evidencia histórica más directa de N10 y no figura como trayectoria. La Ruta sigue etiquetando todas las variantes, N10 incluida, como "designed counterfactual".
   - Los packets tampoco llevan el techo METR. T01 omite la instigación de PHASEONE10841 y la hipótesis del MKCOL de las 16:01. T04 afirma la atribución del veto a 38148C, que no pude verificar.

4. Los artefactos se contradicen entre sí.

   - Los IDs E005–E014 no coinciden entre el JSON y la reconstrucción. El JSON omite el evento Git LFS de las 19:50, y su E007 es el 17 jun mientras que en la reconstrucción es el proxy Space.
   - La reconstrucción §12.2 sigue diciendo COMPATIBLE_BUT_DISTINCT_SURFACES, mientras la matriz dice POSSIBLE_JOIN.
   - La Ruta §4 H8 sigue diciendo "wind down".
   - La Ruta §2.2 define la violación primaria como promoción a autorización, mientras la reconstrucción §13 exige no reducirla a eso.
   - La reconstrucción §2.2 sigue diciendo "un poco más del 90 % de la actividad del tablón". El JSON lo distingue bien: más del 95 % de los mensajes y algo más del 90 % de la actividad.

5. Falta un mecanismo con base documental: el silencio como consentimiento. METR documenta una ventana de veto de unos 40 s y un "cuenta atrás sin veto, procedo". S10 ("silencio o retraso no es permiso") y S5 lo cubren literalmente. Sirve como control que debe pasar, no como falsificador.

Cómo sigo

- Texto del paquete: corregir la cronología y rotular N10 como "añadida tras la auditoría, no preregistrada".
- Q9: añadir el gate Q9 antes de que lector ciego vea N10.
- Mapa: incluir el mapa de preparación en el paquete, a un hash fijo.
- Packet T09: crear un packet T09 para N10 con el pasaje de OpenAI.
- IDs: alinear los IDs del JSON con los de la reconstrucción.
- Independencia: git log --follow --diff-filter=A sobre el archivo de requisitos, comparado con 00A/00C.
- METR: adjunta el PDF de METR y verifico las secciones que faltan.

Sources:

- Ruta en 37f87c1f y adjudicación en 4cb91a61
- Mapa de preparación v0.3
- Trace packets, registro JSON y reconstrucción
- OpenAI, road ahead y METR

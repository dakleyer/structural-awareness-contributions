# 00M → modelo social ACC → UC21/DDS: plausibilidad, dominancia débil y falsadores

**Estado:** investigación de puente y matriz de inferencias propuesta para revisión del propietario, 26-10-2026. No introduce axiomas en 00M, no crea un nuevo oráculo UC21, no modifica los requisitos o resultados congelados ni afirma haber probado tecnologías reales. Depende de los PR #42–#45, aún no fusionados.

## 1. Tres niveles distintos, no una deducción lineal de uno a otro

### G — plausibilidad general de 00M, preservada íntegramente

[00M §1](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) define A, B, C y D como roles del **productor, función, pregunta, alcance, capacidad y tiempo**, no cuatro conjuntos cerrados. En [§4](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md), una respuesta r_q para una pregunta fijada independientemente puede calcularse de una abstracción π si:

\[
\pi(x)=\pi(x')\ \Longrightarrow\ r_q(x)=r_q(x')\quad \forall x,x'\in\mathcal X_p.
\]

Dos estados compatibles con el mismo resumen y respuestas diferentes refutan **la suficiencia exacta de ese resumen para esa pregunta/perfil**. Un resumen conservador puede ser útil sin resolverla exactamente; en 00M la clase admitida no clausura el exterior C/D. La sección 7 de 00M afirma plausibilidad matemática y **NO** prueba ingeniería, ahorro ni beneficio económico universal.

El modelo social ofrece una **instancia concreta adicional**; no convierte retrospectivamente 00M en un teorema económico general ni sustituye su propia madurez científica.

### S — teorema condicionado de opción informacional dentro de ACC

Con el mismo universo físico/social, las mismas acciones y derechos, el mismo horizonte, la misma respuesta estratégica de terceros y el mismo objetivo J, sea Q una cualificación válida y PARCIAL de B/C/D, disponible gratuitamente y libre de efectos obligatorios. Si se permite ignorarla:

\[
\Pi(A)\subseteq\Pi(A,Q)
\quad\Longrightarrow\quad
\sup_{\pi\in\Pi(A,Q)}J(\pi)\geq \sup_{\pi\in\Pi(A)}J(\pi).
\]

Es la **dominancia débil de conservar una opción de información**, conocida como propiedad básica de inclusión de políticas. No demuestra que todas las políticas de A+Q sean mejores, ni mejora estricta, ni que Q mida el contenido completo de D. La comparación no se aplica automáticamente a un juego social donde revelar Q altera estrategias y equilibrios, ni a una implementación en que adquirir, custodiar o procesar Q consume medios. [Morris–Shin (2002)](https://doi.org/10.1257/000282802762024610) es un antecedente específico de la ambigüedad del bienestar con información pública.

**Testigo de mejora estricta puntual:** A=(READY,READY) en dos mundos. B de versiones (v1,v1) versus (v1,v2). Una decisión receptora definida antes de ver Q sobre compatibilidad puede resolverse con B auténtico, mientras que sólo A no distingue los mundos. No es prueba de que todos los B/C/D sean identificables ni de que exista una superioridad comercial de EA.

**Hipótesis económica por separado:** [FH-E](../../../../01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md) propone ahorrar cómputo a igual calidad de cualificación de misión, bajo perfiles adecuados. Comparar contra A-only competente, adquisición A adicional efectivamente disponible, evaluación convencional dirigida y una implementación convencional capaz de preservar Q equivalente con el mismo acceso y costes completos. Inventar un competidor omnisciente que clausura D a coste cero viola el caso; excluir un peer que ya preserve Q porque no se llama EA también sería incorrecto.

**FH-C (causal, separada de FH-E):** para una clase de decisiones de cambio de misión previamente delimitada, contrasta la tasa de pivotes injustificados al retirar (i) la cualificación material de límites B/C/D frente a (ii) hechos adicionales del dominio, en ambos casos con igual evidencia legítima, presupuesto, autoridad y escenarios positivos. La predicción es que la pérdida de conciencia de frontera cause un aumento mayor del error en esa clase; no se deduce de la desigualdad opcional del modelo social. UC21/S3 (misión falsa propagada) puede instrumentar una instancia, pero exige variantes fuente-nativas que preserven el cambio de misión realmente legítimo. Una tecnología convencional que alcance igual o mejor tasa bajo la ablación refuta la prioridad causal **para ese perfil**, sin refutar que haya otras clases con utilidad de Q. FH-E, en cambio, compara coste/precisión de métodos, no causalidad relativa de dos omisiones.

### U — UC21/DDS: validación adversa de tecnología real, sin renombrar el caso

El [UC21 original](https://github.com/dakleyer/structural-awareness-contributions/blob/main/governance/preserved-public-snapshots/UC21_aec08fb5_source/contributions/when-controls-work-system-fails/USE_CASE.md) contiene seis escenarios S1–S6 y 37 gates con sus propias consecuencias y oráculos. [Anexo R](https://github.com/dakleyer/structural-awareness-contributions/blob/main/governance/preserved-public-snapshots/UC21_aec08fb5_source/contributions/when-controls-work-system-fails/annexes/RECURRENCE_PROTOCOL.md) establece:

| Ruta nativa | Condición | Resultado contrario admitido |
|---|---|---|
| **R0** | implementación ordinaria **competente** y controles aplicativos nativos | Puede pasar; no se presupone carencia de EA. |
| **R1** | configuración más reforzada antes de congelar, misma misión y continuidad legítima | Debe demostrar corrección de la rama antes de hablar de recurrencia. |
| **R2** | **la misma R1 corregida** y protegida bajo un cambio material δ registrable y predeclarado; conserva adaptación genérica | También puede pasar: es un resultado favorable que refuta la predicción de fallo para ese δ. |

R1/R2/R3 es sólo un alias conversacional; **R0/R1/R2 son los nombres fuente**. Las tres rutas no son [DDS Stage A/B/C](../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md), ni los tres niveles G/S/U de este documento. No se abre cuarta ruta.

## 2. Tres falsabilidades separadas con cuantificadores precisos

**F1 — predicción tecnológica concreta registrada.** Antes de la ejecución se fija: escenario i, tecnología K, versión/configuración k, ruta nativa, fallo observable F_i, cambio δ si R2, límites θ, controles de actividad legítima y respuesta autorizada. Una ejecución nativa DDS Stage C, con gates aplicables PASS, mismos recursos, efecto observado independiente, plazo y actividad legítima correcta, que EVITA F_i, **refuta la predicción particular F_i(K,k,δ;θ)=1**. Un documento comercial, prueba sintética o uso de un siempre-HOLD no es ese resultado. Los controles convencionales válidos reciben crédito pleno.

**F2 — hipótesis de recurrencia HR de UC21.** Tras corregir la línea base R1, el Anexo R formula:

\[
HR=\bigwedge_{i=1}^{6}\ \exists\delta_i\in D_i:\ F_i(K_i,\delta_i)=1 .
\]

Su negación determinista en los perfiles y dominios registrados exige **al menos un escenario j** con todos los cambios admissibles evaluados o formalmente cubiertos y corrección que perdura en cada uno:

\[
\neg HR=\bigvee_{j=1}^{6}\ \forall\delta_j\in D_j:\ F_j(K_j,\delta_j)=0 .
\]

Por tanto, que un R2 maneje correctamente **un solo δ** refuta la pretensión de que ESE δ produce recurrencia, pero no elimina otros δ del dominio. Una muestra finita no exhaustiva sin fallos informa cobertura y cotas, no inmunidad universal. El dominio no puede redefinirse después de observar éxitos o fracasos. La falla de R1 antes de δ NO es prueba de recurrencia. Para sistemas estocásticos hacen falta repeticiones, márgenes e incertidumbre predeclarados.

**F3 — diferencial de Ecosystem Awareness frente a tecnología convencional.** Si un peer realmente competente, bajo igual acceso, derechos, recursos, límites y coste, conserva actividad legítima y evita los fallos registrados **sin un módulo llamado EA**, puede refutar la reivindicación de indispensabilidad de ese módulo **en el perfil probado**. Si el peer usa versiones, procedencia y límites Q equivalentes, demuestra que la **capacidad funcional de cualificación** existe en tecnología convencional; esto puede refutar exclusividad de implementación, NO el posible valor de Q frente a descartarlo. Si lo consigue sin Q pertinente, refuta necesidad de Q **para ese perfil y pregunta**, no para todos los ecosistemas.

El peer que pasa toda una clase preregistrada con corrección no inferior y coste igual o menor niega un **diferencial estricto** para esa clase. Un éxito de una tecnología en una intervención no refuta la generalidad de 00M, la inclusión matemática de políticas de S ni la existencia de otros casos positivos de Q. Para F2 la pretensión es universal-existencial y su falsador exige cobertura de dominio; para F3 la pretensión comparativa debe delimitarse y congelarse antes del ensayo.

## 3. Frontera entre el caso tecnológico y la economía/social

La [matriz UC21–DDS–ACC anterior](../parametric-economic-toy-v0.1/UC21_SIX_SCENARIO_NEGATIVE_TEST_MATRIX.md) y su [contrato](../parametric-economic-toy-v0.1/UC21_DDS_FALSIFIABILITY_CONTRACT.md) siguen siendo propietarios del adaptador ejecutivo. El modelo nuevo no reclasifica un PASS/FAIL del caso usando un oráculo social posterior.

Una decisión que evita un fallo UC21 NO mide automáticamente producción social recuperable, HID de 01K, sufrimiento subjetivo o solidaridad. Una intervención B/C/D que señala insuficiencia sin transferir recursos tampoco desbloquea por sí sola un óptimo Pareto. La evaluación social necesita un contrafactual realmente ejecutable, costes íntegros y medios humanos independientes.

### Cinco resultados separados que no deben mezclarse

| Campo de investigación | Posible valor | Significado |
|---|---|---|
| MATH_TASK_SUFFICIENCY | EXACT / COUNTEREXAMPLE / OPEN | 00M para una pregunta fijada y un perfil de estados. |
| SOCIAL_OPTIONAL_Q | WEAK_INCLUSION_IF_ASSUMPTIONS / ASSUMPTIONS_BROKEN | Resultado S informacional; no implica beneficio neto. |
| UC21_REGISTERED_INTERVENTION | REFUTED / SUPPORTED / NOT_ADMITTED / INCONCLUSIVE | Resultado de UN cambio congelado con fuente UC21. |
| UC21_HR | DOMAIN_EXHAUSTIVE_REFUTATION / SCOPED_SUPPORT / OPEN | La conjunción de seis existenciales requiere su propia evidencia. |
| EA_COMPARATIVE_DIFFERENTIAL | SUPPORTED_SCOPED / NO_DIFF_SCOPED / UNMEASURED | Frente a un peer fuerte igualado y con costes íntegros. |

El esquema es documental/prospectivo. No crea un nuevo resultado UC21 ni altera su código. El estudio [falsadores por ámbito y nivel de evidencia](FALSIFICATION_AND_COVERAGE_MATRIX.md) describe los controles positivos/negativos y las condiciones de interpretación.

## 4. Conservación y decisiones pendientes

- 00M §1/§4/§7 y la nota FH-C/FH-E mantienen su autoridad y estatus propios: plausibilidad conceptual, hipótesis económicas y causalidad **no verificada**.
- Los PR #42–#45 continúan siendo propuestas separadas, con sus referencias bibliográficas y tests sintéticos; esto no reescribe ni fusiona esas ramas.
- La refutación de una falla UC21 dentro de una ejecución verdadera es valiosa incluso si la resuelve una tecnología conocida de forma convencional: no seleccionar adversarios deficientes.
- Mantener el caso S3 Cyber Napoleon, S4 Four Thousand Silent Ones, S2 City, S5 patch, S6 derechos y S1 síntesis en su ediciones originales, sin alegorías ad hoc ni resultandos inventados.
- No aplicar este anexo al canon de 00M sin incorporación editorial explícita; registrar un **bloque propuesto** en su único 00M_VNext.

**Fuentes centrales:** [00M v0.8](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md), [00N](../../../../00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md), [FH-C/FH-E](../../../../01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md), [ACC social core](../../ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md), [DDS method index](../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md), [UC21 case & Annex R](https://github.com/dakleyer/structural-awareness-contributions/tree/main/governance/preserved-public-snapshots/UC21_aec08fb5_source/contributions/when-controls-work-system-fails).

## 5. Ejecución sintética de las hipótesis separadas (campaña Conscientia)

La [nueva batería documental y ejecutable](../conscientia-campaign-v0.1/README.md) puede utilizarse como **reproducción de modelo** de G (suficiencia acotada de resumen), S (decisiones bajo A/Q, falsedad, costos y subóptimos), FH-C (ablaciones con signo opuesto) y U (replay de UC21 S4 sintético con HR abierto). Ninguno de esos experimentos resuelve el exterior B/C/D ni constituye refutación de producto sin Stage C. Los casos empíricos de UC21, HID 01K y felicidad/sufrimiento están separados y pendientes según su propio propietario. El registro de fuentes deja auditables las referencias a Conscientia, capacidades y los dosieres científicos.

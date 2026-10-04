# Continuación del estudio de viabilidad

Lee el README completo de R01 y su cuadro final, después `feasibility/README.md`, `PURE_MATHEMATICAL_TRILEMMA.md`, `WORKPLAN.md` y `WORKPLAN_STATUS.json`. Trabaja dentro de `feasibility/`; la entrada nueva desde R01 es el cuadro al final del README. Conserva todos los apartados, el escenario, las reducciones, las extensiones y los exports. No disperses nuevos scripts, informes o notas por la raíz ni atribuyas el directorio a un proveedor.

El objetivo es una prueba matemática por configuraciones: existe una familia no vacía donde cada par coste–riesgo, coste–eficacia y riesgo–eficacia es alcanzable, y ninguna política de la clase logra las tres condiciones; existen también familias viables. No afirmes imposibilidad en toda configuración ni infracción en toda ejecución. Las regiones por pares pueden solaparse. Distingue variables de problema θ, mundo ω, política π y resultados. Para «solo un objetivo», distingue una firma de resultado de política de una imposibilidad de todos los pares para toda política. Conserva la observación de que abstención barata y segura impide esa última clasificación en el contrato F.

Primero completa M12 y revisa la prueba base de F sin tecnologías. Examina independencia condicionada a historia, lectura de coordenadas, información por efectos, presupuestos de todas las ramas, aleatoriedad, coordinación, legitimidad, rechazo conocido, calidad, plazo, igualdad y bandas vacías. La necesidad debe cubrir todas las políticas permitidas; la suficiencia debe entregar una política realizable que alcance la frontera. No derives una cota universal de una estrategia de revisión repetida ni de una ventana fijada artificialmente. Después reconstruye W como una obligación separada y conserva la distinción entre n relaciones, L pasos, entropía y acceso.

M16 exige una revisión simbólica realmente independiente: no la cierres con revisión propia ni con una ejecución del checker del autor. M17 exige un embedding o reducción del escenario R01 a la familia demostrada: incluye TODAS las observaciones, las acciones, los conectores, la geometría, los efectos, el coste y las políticas relevantes. Si no puede construirse, conserva el resultado de familia suplementaria y declara la transferencia pendiente o refutada; no impongas una prohibición artificial a un control competente.

Antes de nuevas ejecuciones científicas, establece el oráculo/harness neutral de C01–C05: contratos de entrada/salida, ground truth independiente, óptimo, medidas, contabilidad, límites, controles y trazas. Los scripts anteriores permanecen en `partial-experiments/` como diagnósticos acotados. No ejecutes más ejemplos como sustituto de los lemas. La verificación documental y de conservación de esta reorganización no es una prueba científica.

Las tecnologías quedan después: M13 debe clasificar capacidades e interfaces por contratos y costes completos; M14 añade ruido, caché y amortización; M15 trabajo distribuido, geometría y latencia. Reutiliza los materiales archivados sin dar por válidos sus argumentos. No infieras eliminación o persistencia por el nombre de una tecnología, precio positivo, capacidad asintótica o recuperación del mundo cuando solo se necesita una ruta.

Actualiza las 55 tareas existentes sin borrar IDs ni criterios históricos; registra alcance, responsable, fecha, commit, evidencia y pendientes. Un borrador no cierra revisión independiente, puente, implementación o campaña. Si detectas un contraejemplo, registra la configuración y la política, el supuesto que falla y la afirmación que se reabre. Termina cada README con un cuadro de estado y enlaces; no sustituyas el contenido completo por un resumen. Publica URLs completas fijadas al mismo commit del README de R01, del documento, del plan y de este prompt.


## Manuscrito independiente para revisión

La siguiente revisión matemática parte de `CONDITIONED_TRILEMMA.md` y `CONDITIONED_TRILEMMA_SELF_REVIEW.md`. El nombre propuesto es «trilema condicionado de coste, riesgo y eficacia». Reconstruye el lema para a∈[1/2,1), donde cada apuesta condicionada a la historia acierta con probabilidad ≤a, y comprueba la suma geométrica y las fronteras de eficacia técnica y éxito legítimo. Verifica que el presupuesto no sea parte circular de H y que k solo limite lecturas de ramas completas. Para WC, verifica la ley uniforme auxiliar y el control con monedas justas: no transfieras a WC la familia AVG de éxito legítimo del 95 %. Comprueba que las regiones anunciadas permiten realmente todos los pares, no solo que la triple conjunción falle. Conserva los límites de costes lineales, abstención, prior, interfaz y transferencia a R01. El manuscrito es autocontenido para presentarlo a revisión; redactarlo y auditarlo por el mismo autor no cierra M16 ni M17.


## Auditoría de fondo y transferencia — instrucciones vigentes

Lee primero `CONDITIONED_TRILEMMA_DEEP_AUDIT.md`, `R01_TO_CONDITIONED_TRILEMMA_MAPPING.md` y el manuscrito v0.2. Separa B (capacidad física), R_goal (coste deseado), C_max (política), C_traza (campaña), σ (éxito sin presupuesto) y σ_R (éxito con presupuesto por rama). La cota inferior se transfiere con Good_R01⇒Good_modelo, no al revés. Alcanzabilidad exige controles implementables; no necesita una biyección de todas las políticas. ∀π¬Good y ¬∃πGood son equivalentes.

Revisa la prueba directa del catálogo M02 y la familia G para todos los L: historia inicial técnica pagada, costes de productor, gates consumidos, χ compartido, recibos y recuperación sin borrar V. G prueba existencia condicionada, no un sobrecoste informativo creciente ni optimalidad de preparar el prior. Su variante sesgada de alta fiabilidad es AVG; para WC conserva las monedas justas y el prior auxiliar de prueba. No reescribas el fixture M02 ni sus umbrales p=3/4, δ=1/4 para hacerlos parecer un trilema no vacuo por todos los pares.

M17 está IN_PROGRESS. Para ampliar a hechos independientes en R01, construye el catálogo completo y demuestra la simulación de todas las políticas con las desigualdades útiles y los controles; no omitas query_mandate, estado, certificados, pooling, metadatos o información legítima. El contraejemplo χ compartido refuta aplicar d=L indiscriminadamente, no el lema dentro de F. Conserva el resultado G si la ampliación falla.

M16 exige otra reconstrucción, no esta nueva revisión del mismo autor. Antes de ejecutar nuevos diagnósticos, C01–C05 debe separar la vista pública del estado oculto: Episode.chi accesible en el mismo proceso no es una implementación segura de Π_obs. Los scripts nombrados siguen siendo experimentos parciales; ningún texto recibido que no leyó los enunciados cierra una validación independiente. Preserva cuerpo de README y añade seguimiento al final.


## Instrucciones posteriores — teorema condicionado en R01 completo

Lee primero `R01_CONDITIONED_TRILEMMA_THEOREM.md` y `R01_CONDITIONED_TRILEMMA_REVIEW.md`. El objetivo es un teorema sobre las regiones del dominio R01 completo. Los casos fáciles y el χ compartido no lo refutan: únicamente invalidan transportar una fórmula particular sin sus hipótesis. La familia de precio informativo creciente ya está construida mediante paridad de K datos; no exijas hechos independientes por segmento como única vía.

El trabajo pendiente inmediato es reconstrucción por un revisor distinto y auditoría de fidelidad por cláusula, no otra declaración genérica de que faltaría un puente. Revisa todos los canales del manifest, los scopes de revisión, producción y uso de certificados, pago inicial técnico, rechazo de prohibiciones conocidas, recepción posterior a efecto, efecto irreversible, concurrencia, queries agrupadas y ledger por ejecución. Para cada afirmación entrega prueba, laguna o contraejemplo con reparación. La envolvente centralizada ayuda a cotas inferiores; una igualdad convexa exacta exige mezclas realmente implementables y manifest finito.

Conserva la distinción B (cap físico) y b (objetivo económico), s (eficacia legítima), η (técnica) y e_b (éxito compuesto). No cuentes una entrega cara como e_b=1. La variante .99/.95/.001 es AVG; la frontera WC barata tiene p≤.5. No extrapoles coste K a factor relativo extraordinario o ley cuadrática. El prior técnico pagado es una condición inicial explícita del perfil; no una prueba de optimalidad de su adquisición anterior.

M16 permanece OPEN y M17 IN_PROGRESS. No declarar una revisión independiente por leer una revisión propia. No ejecutar experimentos científicos antes del oracle/harness neutral. Mantén el escenario, scripts, fixtures, resultados y contenidos previos de los README; añade seguimiento al final dentro de feasibility.


## Estado vigente posterior — núcleo reparado v0.2

El usuario ha fijado este orden: cerrar primero la formulación matemática y los espacios de viabilidad de R01 sin aplicar tecnologías; después producir un protocolo separado de extensión matemática. No rehacer el trilema: conservar el trabajo y las auditorías existentes y aplicar reparaciones mínimas.

La v0.2 del teorema conserva §§1–14 y sus pruebas. Corrige el multiplicador μ=a/(1−a) del certificado, C_pre=2+4L+2(N−1), C_0=7L+2N, T/H_cap=5L+K+2N+4 y controles persistentes sin veredicto del evaluador. Mantener las cotas AVG/WC y el corolario por rama. El informe R01_AUDIT_CONTINUITY_AND_REPAIRS.md reconstruye estos pasos contra R01 y las auditorías anteriores. No confundir este cierre propio con M16.

La siguiente fase es el protocolo, todavía no una aplicación tecnológica. Debe distinguir: transferencia de imposibilidad para todas las políticas de una configuración completa; controles que prueban alcanzabilidad; ampliación del espacio viable como mejora; persistencia no vacua de una región de trilema bajo capacidades/costes explícitos. No inferir persistencia por un nombre comercial ni exigirla a toda tecnología. Prueba matemática precede al harness y la campaña. No modificar el escenario, fixtures, resultados ni cuerpos históricos de README. Mantener M16 OPEN y M17 IN_PROGRESS.

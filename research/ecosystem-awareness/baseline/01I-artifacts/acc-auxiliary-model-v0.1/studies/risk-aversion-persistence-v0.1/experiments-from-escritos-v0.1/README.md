# ACC–RAV–EX/01 — Campaña parametrizada de las «rotondas»: restricciones, valor neto y permanencia

**26 de octubre de 2026 · Iván Abril Palma / The Integral Management Society.**  
**Estado: DISEÑO CONGELABLE + EJECUCIÓN SINTÉTICA DETERMINISTA. No es una campaña humana, un estudio nacional ni evidencia causal de que el mundo real funciona así.**  
**PR de integración:** #46 (RAV-01), apilado sobre #45 → #44 → #43 → #42. No fusionar ni promover a norma canónica sin revisión del propietario.

Este conjunto transforma **ejemplos ilustrativos** del escrito privado *La generación de las rotondas — El posthistoricismo y el precio de la paz mental* (v0.6, 26-10-2026) en **contrastes matemáticos repetibles**, sin copiar el ensayo al repositorio público ni identificar personas reales. No presupone que todos esos procesos sean el mismo mecanismo.

- [Parámetros congelados](SCENARIO_PARAMETERS.json): 20 casos (incluidos controles que **contradicen** la crítica inicial) y tres rejillas de sensibilidad.
- [Motor de ejecución](scenario_campaign.py): cálculos deterministas, validación numérica, umbrales, dominios y derechos estipulados.
- [Contratos de prueba](test_scenario_campaign.py): 39 pruebas positivas, negativas, de no duplicación, presupuesto, supuestos y sensibilidad.
- [Salida de referencia](REFERENCE_EXPERIMENT_RESULTS.json): resultado exacto y SHA-256 del input; se compara en CI, no solo se muestra.
- [Kernel de decisión RAV-01](../risk_model.py) y [documento de reducción/isomorfismo](../EXTENSION_ISOMORPHIC_NONISOMORPHIC_RESEARCH_v0.1.md): se usan las funciones originales S/R/D/CARA; no hay una nueva psicología codificada.

## 1. Lo que se demuestra y lo que no

**Resultado demostrable:** existe una región de parámetros caracterizados en la que, **a igualdad de servicio y condiciones declaradas**, más actividad transaccional acompaña menor excedente neto; en otras regiones la innovación **sí** añade valor. También existen loterías con más retorno medio al cambiar y permanencia racional a γ constante, y una política D defendida por su utilidad afectiva sin protección adicional. La campaña calcula los umbrales en que se invierte cada resultado.

**No demostrado:** que esas regiones caractericen España, México, Colombia, una generación, la economía digital o la gobernanza climática; que cada rotonda sea innecesaria; que el padre concreto esté dañando al hijo; que un adulto deba emigrar o quedarse; que exista sufrimiento humano F observado, ni que se satisfagan las condiciones conjuntivas de **sufrimiento estructural** del #43. Los números son arbitrarios y relativos **solo dentro de cada expediente**.

**Separación estricta de variables:**

| Capa | Lo que contiene | Prohibición |
|---|---|---|
| Actividad comercial A | Pagos/transacciones de bienes, obras, servicios | No equiparar facturación o actividad a excedente social neto |
| Servicio Q y costes reales | Calidad/servicio equivalente, recursos, mantenimiento, externalidades cuantificadas *como hipótesis* | No contar el mismo gasto real dos veces; las transferencias no son un segundo coste social |
| Utilidad privada Uᵢ | Preferencias del actor, incluido afecto, identidad, cuidado, validación, costes | No sumar cardinalidades de personas distintas sin regla pública legítima |
| Oportunidad/factibilidad | Alternativa comparada, derechos, recurso, población, horizonte y servicio | No llamar «óptimo factible» a una mejora hipotética no autorizada |
| Riesgo/elección RAV | Loterías **caracterizadas** μ/σ², γ, C, acción S/R/D | No asignar probabilidades a B/C/D abiertos, ni convertir probabilidad de elección en éxito |
| F/L/G | F humano medido aparte; L oportunidad individual factible; Gᵀ/Gᴳ fronteras separadas | No derivar F de G o de los cálculos; no atribuir HID ni 00M |

La parte **isomórfica** se limita a transformar parámetros de la utilidad completa y reutilizar el comparador cuando se preservan sus hipótesis; una decisión distinta bajo parámetros nuevos no es un fallo del cálculo. Reglas de titularidad, acceso o consentimiento son **guardrails**, no un bonus que compre derechos. Consulte U0–U6 en el anexo de extensiones.

## 2. Diseño factorial y registro de ejemplos

**Cada fila es un experimento sintético identificable**, no una observación. El criterio de refutación distingue fallos de una fórmula condicional, fallos de sus supuestos y el fracaso de una extrapolación histórica.

| Expediente | Del escrito → operación medible | Parámetros manipulados / hipótesis H | Control adverso o favorable |
|---|---|---|---|
| **EX01 Teletrabajo** | Romper «hay que ir a la oficina» vs comprar más ergonomía y movilidad | Servicio Q preservado, recursos, coste de colaboración, desplazamiento; H: remoto ahorra costes sin pérdida funcional en tareas elegibles | EX01B: una intervención física no alcanza el mínimo de servicio y remoto queda **excluido** |
| **EX02 Jardín** | Tierra → baldosas → madera → volver a poner sustrato comprado | Costes de capital/mantenimiento y beneficio de cada fase; H: actividad A puede crecer con excedente neto decreciente | Reforma que añade **valor funcional auténtico** vence a la tierra inicial |
| **EX03 Intermediación** | Relaciones preexistentes monetizadas vs alcance realmente nuevo | Valor del alcance, fricción de atención, coste real y flujo comercial; H: más facturación no garantiza más excedente | Plataforma de gran alcance y coste razonable **sí** crea excedente adicional |
| **EX04 Ciudad/clima** | Evitar una necesidad de viaje vs mejorar la tecnología del coche | Igual servicio, coste viaje/tecnología, externalidades **estipuladas**, incentivo privado separado; H: pueden divergir óptimos privado y de recursos | Viaje físico indispensable no admite la opción «evitar», aunque su cuenta parezca atractiva |
| **EX05 Rotondas** | Rotonda con tráfico lateral insignificante | Demanda, beneficio de seguridad y costes amortizados; H: obra marginal puede elevar actividad y reducir valor neto | EX05B: en cruce intensivo la rotonda es **mejor**, no un derroche universal |
| **EX06 Parque/niño** | Parque financiado hoy, posible obsolescencia antes de edad de uso; deuda heredada | Probabilidad de uso × funcionamiento a edad 5; inversión, mantenimiento, fiscalidad presente/futura, utilidad simbólica del progenitor | EX06B: instalación conservada y usada tiene beneficio neto positivo |
| **EX07 Migración y Truman** | Permanecer en contrato criticado, pese a mayor media de salida; defenderlo por cuidado/aprobación | μ, σ², γ fija, C, recompensa intrínseca en X_D; H: riesgo conocido y U privada permiten permanencia/defensa | Salida asegurada, γ=0, validación insuficiente y validación suficiente invierten decisiones |
| **EX08 Sierra** | Pequeñas probabilidades de fallo que se componen en una ruta más larga | Pasos m, éxito por paso q, beneficio B y pérdida L; H: cambia el signo de E[ΔG] **bajo independencia asumida** | q mayor hace la ruta larga mejor en expectativa; no hay fatalismo de complejidad |
| **EX09 JASP/vivienda** | «Casa por 100 y luego por 400; salario relativo 1 y luego 0,5» | Índices **retóricos**, contribución hipotética y precio/salario; H: carga relativa calculable bajo supuestos | La prueba NO sustituye series salariales, de vivienda y de pensiones ni las cifras de EFF |

**Pendientes deliberados sin datos adecuados:** las historias biográficas y musicales de amistades, los ritmos observados anecdóticamente en una obra y la cultura filosófica personal requieren consentimientos, definiciones de unidad de análisis y comparadores; no se publican como datos. La privatización de una playa requeriría título de acceso, derechos y escenario de bienes comunes, que este experimento comercial no prueba. Una comparación causal entre gasto militar (p. ej. Afganistán) y mitigación climática no se infiere de las cuentas locales. Ninguna historia privada se identifica mediante nombres u organizaciones en los parámetros.

## 3. Funciones reproducidas y umbrales, sin nuevas hipótesis ocultas

### 3.1. Economía de pequeñas soluciones: valor neto frente a facturación

Para una opción o en un caso con servicio y horizonte comparables:

~~~text
V(o) = Q(o) − C_recursos(o) − C_mantenimiento(o) − E(o)
ΔV = V(o) − V(o_baseline)
A(o) = volumen comercial declarado; NO se suma a V
alternativa elegible ↔ Q(o) ≥ Q_mínimo ∧ autorización estipulada
~~~

Una opción puede generar ΔA>0 con ΔV<0. También puede generar ΔV>0: eso es un **control crucial**, no una anomalía que deba corregirse. «Mínimo de servicio» no identifica automáticamente la misma experiencia, derechos, salud ni impacto ambiental; esos aspectos requieren evidencia al pasar a población real.

**Ejemplos congelados (unidades sintéticas distintas por caso):**

- **EX01:** presencial V=71; remoto V=86; híbrido V=80, todos con servicio 100. Beneficio sintético de quitar obligación: **+15**. Si una actividad física con remoto Q=70 no alcanza el mínimo 95, se rechaza esa opción.
- **EX02:** las cuatro fases del jardín pasan de actividad A=[10,25,48,80] a V=[89,75,65,46]. Pero una renovación con Q=145 da V=107, **18 más** que la tierra; no se presupone que toda mejora material sea frívola.
- **EX03:** relación directa V=95; intermediación de alcance limitado V=77; plataforma que crea gran alcance V=125. El registro de transacciones no responde por sí solo si hubo valor añadido.
- **EX04:** viaje convencional V=34; vehículo mejorado V=48; viaje evitable V=78, bajo mismo servicio 100. **La preferencia privada estipulada** prefiere el vehículo mejorado, mientras esta cuenta de recursos prefiere evitar el viaje. No asignar tales valores al clima real.
- **EX05:** con cruce poco usado, simple V=92 frente a rotonda V=67; con alta demanda el cruce simple V=70 frente a rotonda útil V=92. No son dos observaciones de la misma intersección.

### 3.2. «Parque para el niño que todavía no puede jugar»: dos personas y dos horizontes

No imputamos satisfacción paterna como satisfacción del niño ni la deuda pública como «préstamo personal» del recién nacido. Declaramos independencia **solo sintética** entre uso y conservación:

~~~text
E[servicio del niño] = P(uso) × P(funcional al cumplir edad) × valor_si_usable
saldo del niño neto de carga fiscal asignada = E[servicio] − gravamen_futuro_PV
margen de servicios respecto de recursos reales = E[servicio] − capital − mantenimiento
preferencia privada simplificada del progenitor = valor simbólico de cuidar − pago propio
identidad fiscal: impuestos presentes + carga futura_PV = capital + mantenimiento
~~~

**Parque infrautilizado:** P(uso)=0,08; P(funcional)=0,35; servicio si se usa=320; inversión 200 y mantenimiento 20; financiación futura PV 200 y presente PV 20; contribución privada del progenitor 2 y satisfacción por su papel 30. **Todos los valores intertemporales del parque se estipulan convertidos a valor presente en la misma fecha**; no se asume una tasa real del municipio. Resultados: utilidad privada inmediata **+28** para el progenitor, cuenta del niño **−191,04**, y servicios del niño menos recursos reales **−211,04**. No es una suma de bienestar social: el valor simbólico del padre sigue siendo legítima utilidad suya, pero no autoriza a ignorar derechos, costes y beneficiarios.

**Control EX06B:** con P(uso)=0,95 y P(funcional)=0,95, esos saldos son respectivamente **+88,8** para el niño después del gravamen y **+68,8** en servicios frente a recursos reales. El umbral material es P(uso)×P(funcional)>**0,6875**. Esta inversión del signo impide concluir que todo parque infantil sea desperdicio o que amar al hijo sea una anomalía económica.

### 3.3. RAV-01, migración y defensa activa de lo conocido

Se reutiliza exactamente [risk_model.py](../risk_model.py), sin redefinir sus rendimientos ni F. Con γ=0,5 fijo, los casos temprano y posterior reproducen CE(S)=9 vs CE(R)=7 y CE(S)=13 vs CE(R)=9, aunque aumente la ventaja de media del rediseño. Es una posibilidad matemática; **no es un dato de Colombia, España o migrantes**. La referencia privada del escrito motiva la viñeta, no calibra los parámetros.

~~~text
CE_a = μ_a − (γ/2)σ²_a − coste_externo_contado_una_vez
para γ>0:
σ²_R > σ²_S + 2(μ_R−μ_S−C)/γ  ⇒  S gana a R
~~~

El caso tardío tiene umbral σ²_R>48; su varianza=64 permite permanecer con CE(S)=13 y CE(R)=9. Reducirla a 4 hace ganar a R. Con γ=0 también vence R. **No hay un «miedo a España» o sentimiento programado: solo comparación de resultados.**

En defensa D, la satisfacción propia de cuidar o recibir validación se incorpora como utilidad adicional, *no* como un motor misterioso no isomórfico: mismo ingreso material S=(14,4), D material=(14,4), bonus interior +1, k=0,5 ⇒ CE_D=13,5>CE_S=13. Con bonus 0,3 ⇒ CE_D=12,8<13 y gana S. Esto ejecuta el control I/P del anexo: misma familia de ecuación, **veredicto distinto** por un argumento legítimo de utilidad; la autorización de acciones sigue fuera de CE.

### 3.4. Sierra: el riesgo de intentar reducir la brecha

~~~text
P(completar sin fallo) = q^m             [supuesto iid, explícito]
E[ΔG | intentar] = (1−q^m) × L − q^m × B
E[ΔG] < 0 si q^m > L/(B+L)
~~~

Con q=0,95, B=20, L=40: m=3 ⇒ E[ΔG]=**−11,4425** (la ruta ayuda en promedio), pero m=25 ⇒ **+23,3566** (empeora G esperado). Con m=25 y q=0,99 ⇒ **−6,6693**. Esto evalúa únicamente la brecha condicional de una ruta, no el sufrimiento F, la probabilidad humana de optar por salir ni una distribución de «desconocidos» B/C/D.

### 3.5. Contrato generacional: separar metáfora y datos

El índice retórico precio/sueldo del escrito pasa de 100/1 a 400/0,5: **8×** de carga relativa bruta bajo identidad de calidad/vivienda y unidad. Si se imputa hipotéticamente una contribución de 33 % al segundo salario y ninguna al de referencia, el índice adicional sería **11,9403×**. **Ninguna de esas proporciones se presenta como estadística de España ni implica que ese 33 % sea una aportación homogénea a pensiones.** Una campaña histórica requeriría salarios reales por cohorte/ocupación, precios ajustados por tamaño/localidad, financiación, impuestos, pensiones, duración y sesgo de selección. No probar un contrato social real con una calculadora ilustrativa.

## 4. Rejillas declaradas, sin búsqueda oportunista de parámetros

Los ejes están congelados en el JSON *antes* de derivar la salida de referencia. El motor **rechaza** una ficha si no declara expresamente: costes mutuamente no duplicados y unidad/horizonte comparable (estáticos), independencia de uso/conservación y fecha de valor presente común (parque), normalidad caracterizada y mismo actor/horizonte (RAV), independencia de pasos (sierra), o calidad comparable de vivienda (índices). Son supuestos **estipulados para esta construcción**, no datos auditados del mundo:

| Rejilla | Ejes fijados | Pregunta discriminante |
|---|---|---|
| **Riesgo** — 25 combinaciones | γ={0;0,1;0,25;0,5;1} × Var(R)={4;24;48;64;100}, con las medias de EX07 constantes | ¿En qué región cambia la elección S/R sin elevar artificialmente el retorno? |
| **Parque** — 6 combinaciones | P(uso)={0,1;0,5;0,9} × P(funcional)={0,35;0,95}, con costes fijos | ¿Qué región invierte el signo material del proyecto? |
| **Sierra** — 8 combinaciones | m={3;10;25;40} × q={0,95;0,99} | ¿Se acelera el riesgo por composición, o lo vence una mayor fiabilidad? |

Un investigador debe registrar **nueva versión de parámetros y output**, no editar silenciosamente el JSON de referencia para hacer que una hipótesis «gane». Los controles favorables son esenciales: con ellos el modelo puede fallar frente a una interpretación universal sin fallar matemáticamente.

## 5. Del banco sintético a campañas científicas posibles

| Expediente | Qué habría que medir en el mundo real | Diseño y confusores prioritarios | Resultado que debilitaría la hipótesis |
|---|---|---|---|
| Teletrabajo | Servicio/prestación, tareas físicas, tiempo, coste total, productividad, satisfacción | Pilotos por función y periodo, selección ocupacional, coste doméstico y coordinación | Remoto no conserva Q o sus costes reales superan el ahorro |
| Jardines y productos | Coste inicial/recurrente, durabilidad, utilidad de disfrute, horas de cuidado, gasto | Historial de hogares con preferencias estéticas medidas; contrafactual sin renovación | Las etapas posteriores elevan sostenidamente U neta real, no solo compras |
| Plataformas | Vínculos nuevos, alcance, calidad de comunicación, tiempos/fricciones, costes de intermediación | Comparadores directos y mediados, efectos de red y alcance internacional | El alcance nuevo compensa fricción y costes en comparación válida |
| Clima/movilidad | Viajes realmente evitables, servicio, emisiones ciclo de vida, salud, costes privados/sociales | Escenarios territoriales y de transporte, análisis de ciclo de vida; nunca extrapolar el ejemplo a IPCC | Sustituir vehículo supera evitar viaje a servicio/impacto comparable |
| Rotondas | Volúmenes, siniestralidad, demoras, mantenimiento y coste total amortizado | Diseño vial; demanda y seguridad **por emplazamiento**, no fotos | Obra reduce riesgos/tiempos con beneficio neto verificable |
| Parque infantil | Nacimientos, uso por edad, vida útil, mantenimiento, financiación PV, beneficiarios reales | Cohortes, presupuesto municipal, usabilidad futura y derechos; evitar atribuir voluntad al menor | Uso/conservación suficientes y carga fiscal compensada |
| Migración/roles | CE/creencias sobre alternativas reales, γ estimada, utilidad afectiva, permisos, F independiente | Viñetas consentidas y paneles voluntarios; autoselección, familias, estatus legal; nunca inducir migraciones | La elección no sigue el umbral con riesgos bien medidos, o otra utilidad explica mejor |
| Sierra | Distribuciones condicionales por etapa, correlación, reversibilidad, recuperación, G factible | Simulación de rutas y datos de proceso, pruebas con independencia rota | Rutas largas modulares mantienen q o reducen pérdidas de manera que G esperado mejora |
| Vivienda/cohortes | Series reales de riqueza, rentas, viviendas comparables, crédito y tributación | Datos longitudinales con cohortes, localidades, hogar/individuo y tamaño | No se observa el patrón de carga relativa después de controles |

**Registro previo mínimo para cada equipo:** hipótesis y rival, población y unidad, consentimiento/permiso, horizonte, servicio equivalente, parámetros/calibración, versión y SHA de input, medida F separada, regla de exclusión, controles de oportunidad factible, potencia estadística si hay inferencia, resultados nulos y método de reproducibilidad. Todas las nuevas probabilidades deben ser **caracterizadas**, nunca extrapoladas desde abierto B/C/D.

## 6. Reproducción y genealogía de PRs

Desde la raíz del repositorio:

~~~bash
python -B -m unittest discover -s research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/risk-aversion-persistence-v0.1/experiments-from-escritos-v0.1 -p test_scenario_campaign.py -v
python -B research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/risk-aversion-persistence-v0.1/experiments-from-escritos-v0.1/scenario_campaign.py
~~~

Se comparan **estructuralmente** la salida serializada y el archivo de referencia dentro de GitHub Actions, incluyendo SHA-256 del input y rejillas. La ejecución local del PR combina **43 tests RAV + 39 tests de esta campaña = 82**, sin contar los demás tests del corpus. No se utilizan paquetes, servidores, claves, llamadas de red, LLMs ni datos personales. No es un «toy añadido» aislado: las decisiones S/R/D invocan el **kernel RAV-01 realmente publicado**.

| PR científico existente | Relación con el experimento — **sin modificar su contrato** |
|---|---|
| **#42** — producción, rendimientos y utilidad no monótona | EX01/02/03/04/05/09 son **ilustraciones** de valor neto vs actividad; la compatibilidad con todas las restricciones de #42 exige transferir perfiles tipados |
| **#43** — composición y sufrimiento estructural | EX02/05/06 sugieren rutas de obligaciones/deuda; **no** se declara satisfecha la prueba conjuntiva de #43 |
| **#44** — B/C/D intrínseco | Solo casos finitos caracterizados; ningún σ² sobre incertidumbre epistémica abierta |
| **#45** — metacognición/solidaridad elegida | EX06/07 muestran utilidad de cuidar/validación, sin certificar altruismo, dignidad o consentimiento |
| **#46** — RAV-01 | **PR propietario de esta campaña**, por reproducibilidad y control de límites; no modifica los modelos anteriores |

**Puerta final:** revisión del autor sobre las decisiones de utilidad y separación de cohortes; revisión económica externa antes de generalizar; datos reales y preregistro antes de reclamar evidencia social. La campaña puede servir como familia de retos para investigadores distintos **precisamente porque admite salidas favorables y desfavorables**, pero no autoriza promoción DDS Stage B/C, ejecución real de políticas ni ampliación de derechos por semejanza matemática.

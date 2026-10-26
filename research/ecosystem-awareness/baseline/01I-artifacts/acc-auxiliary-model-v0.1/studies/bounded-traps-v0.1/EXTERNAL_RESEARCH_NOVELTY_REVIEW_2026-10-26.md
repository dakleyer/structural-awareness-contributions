# Revisión de novedad y evidencia contrastada — PR #42 (26-10-2026)

**Rol:** revisión bibliográfica añadida a un estudio de investigación; **no** es una revisión sistemática exhaustiva, validación económica de campo ni aprobación independiente. Esta revisión distingue: (T) teorema/construcción conocida; (M) demostración interna en el toy; (E) investigación empírica ajena con su propio dominio; (H) hipótesis específica todavía sin contrastar. Las fuentes externas no demuestran por sí solas el modelo ACC.

## 1. Veredicto de novedad, separado por mecanismos

| Componente PR #42 | Antecedente publicado | Qué muestra nuestro toy | Aportación potencial y qué sigue sin probar |
|---|---|---|---|
| Trampa racional sin veto psicológico | [Milgrom y Roberts 1990] sobre complementariedades; [Ostrom 1990] sobre instituciones de cooperación | (M) Con `x1<=x2`, `x2<=x1` y decisiones binarias, el estado Pareto-superior (1,1) no es alcanzable por movimientos unilaterales desde (0,0) | No es nuevo que exista coordinación fallida. **Propuesta ACC:** registrar por separado factibilidad final, alcanzabilidad por un protocolo real, continuidad funcional y consentimiento; falta implementación con procesos y recursos observados. |
| Distancia entre rendimiento descentralizado y óptimo | [Koutsoupias y Papadimitriou 2009] formulan precio de la anarquía para una clase de equilibrios de Nash | (M) Distancia condicional `G=gE(n)` con red densa y contrafactual supuesto | El cociente no se debe llamar **precio de la anarquía** si el toy no prueba un equilibrio de Nash; tampoco todo subóptimo es causado por conducta estratégica. Aportación candidata: dinámica E/R/C/V con costes completos y derechos en el óptimo factible. |
| Saturación, reestructuración y recursos | [Ostrom 1990] presenta instituciones diversas para recursos comunes; [Milgrom y Roberts 1990] complementariedades | (M) Margen funcional cero bloquea incrementos; rediseño caracterizado puede liberar capacidad | No crear automáticamente un actor/veto por cada restricción. La necesidad **material** del umbral de reconocimiento, recursos y coordinación requiere prueba externa. |
| Crédito, reputación y prosocialidad | [Bénabou y Tirole 2006] modelan altruismo, autorreputación, incentivos y efectos de crowding-out | (M) Dos exigencias relativas de crédito pueden ser incompatibles | La regla matemática `Σρ_i<=1` no demuestra que `ρ_i` sea una necesidad real. Protocolo nuevo: separar mínimos funcionales observables de preferencia relativa, reputación y poderes jurídicos. |
| Brecha creciente con nuevas dimensiones | [Milgrom y Roberts 1990] y [Koutsoupias y Papadimitriou 2009] muestran otras clases de resultados sobre coordinación y eficiencia | (M) En red completa `E(n)=n(n-1)/2`, `G=gE(n)` crece; estrellas y `g=0` no | La **ganancia conjunta g** está postulada, no optimizada a partir de presupuesto común: construir y certificar un `S*` conjunto en cada `n` antes de nombrarlo deuda recuperable. |
| Funciones no monótonas | Economía de elección y optimización no convexa son campos previos | (M) Perfil artificial de utilidad de manzanas con valle/rebote | Ninguna originalidad por observar que la utilidad no siempre crece. Útil para demostrar que Pareto es comparación entre estados finales, no crecimiento de derivadas. |

## 2. Diseño experimental con base económica y social

**Unidad causal:** transiciones candidatas entre estados con el mismo vector completo de servicio, recursos, terceros, horizonte y derechos. Registrar: productores/agentes, tareas, contabilidad no duplicada, crédito de origen real, cambios de capacidad, decisiones y ruta realmente ejecutada.

**Protocolo preregistrado, no ejecutado en personas:** cruzar (A) coordinación unilateral/atómica, (B) reserva de recursos agotada/liberable, (C) red estrella/completa/modular, (D) transferencias imposibles/legítimas, (E) crédito reputacional instrumental/meramente preferencial, (F) información incompleta/calificada. Mantener escenarios donde la arquitectura convencional coordina correctamente. Distinguir (i) mejora técnica factible, (ii) camino autorizado y disponible, (iii) continuidad del servicio, (iv) mejora neta por persona y (v) coste de obtención de acuerdos.

**Predicción falsable:** en redes con dependencias compartidas y pasos individuales insuficientes habrá una tasa de estados Pareto-superiores no alcanzables mayor que en redes con actuación conjunta factible, bajo los mismos recursos y derechos. Dejar de observar la diferencia cuando el coordinador convencional recibe capacidad atómica refuta la explicación de pérdida estructural permanente. La distancia relativa creciente con `n` sólo se aceptará cuando se **ejecute o certifique** la alternativa conjunta `S*` sin cambiar los recursos y sin sumar proyectos incompatibles.

**Nivel de atribución:** El caso de naranjas, plátanos, ministerios y reconocimiento es una hipótesis de mecanismo, no una observación de empresas/personas. Un desacuerdo puede ser legítimo; la optimización no lo convierte en una falla moral ni en una pérdida «recuperable» obligatoria.

## 3. Fuentes examinadas y pertinencia limitada

- **Milgrom, P.; Roberts, J. (1990)**, *Rationalizability, Learning, and Equilibrium in Games with Strategic Complementarities*, *Econometrica* 58(6), 1255–1277. Artículo teórico de juegos con complementariedad; no demuestra nuestras brechas sociales: https://doi.org/10.2307/2938316
- **Ostrom, E. (1990)**, *Governing the Commons*. Investigación teórica y casos de arreglos institucionales para recursos compartidos; aporta evidencia de que centralización o veto simple no son únicas rutas: https://www.cambridge.org/core/books/governing-the-commons/7AB7AE11BADA84409C34815CC288CD79
- **Ostrom, E. (2010)**, *Polycentric systems for coping with collective action and global environmental change*, *Global Environmental Change* 20(4): 550–557. Alcance: acción colectiva y gobernanza policéntrica: https://doi.org/10.1016/j.gloenvcha.2010.07.004
- **Koutsoupias, E.; Papadimitriou, C. (2009)**, *Worst-case equilibria*, *Computer Science Review* 3(2): 65–69. Referencia al precio de anarquía, **no** medición del toy ACC: https://doi.org/10.1016/j.cosrev.2009.04.003
- **Bénabou, R.; Tirole, J. (2006)**, *Incentives and Prosocial Behavior*, *American Economic Review* 96(5): 1652–1678. Modelo sobre altruismo, imagen y posibles reducciones de motivación prosocial con incentivos: https://doi.org/10.1257/aer.96.5.1652
- **Fleurbaey, M.; Maniquet, F. (2011)**, *A Theory of Fairness and Social Welfare*, Cambridge University Press. Las comparaciones sociales requieren criterios explícitos, no sumar sin más preferencias: https://doi.org/10.1017/CBO9780511851971

## 4. Recomendación de redacción científica

**Admisible:** «ACC demuestra en un modelo finito cómo una configuración conjunta Pareto-superior puede no ser alcanzable bajo un protocolo local, mientras estudia cómo coordinar recursos, consentimiento y crédito. La extensión económica a redes reales está abierta».

**No admisible:** «Se descubrió la existencia de subóptimos racionales»; «la complejidad necesariamente acelera HID»; «los agentes son egoístas porque rechazan una pérdida»; «la literatura sobre juegos acredita nuestro G medido».

**Próximo entregable exigible:** casos económicos independientes con `S*` comprobable, entradas públicas A iguales, protocolos de transición verificables, costes reales, y análisis comparativo de una intervención conjunta competente.

**Precisión bibliográfica comprobada 26-10-2026:** el DOI 10.1017/CBO9780511851971 corresponde al libro completo de Fleurbaey y Maniquet (2011); el sufijo `.002` remite exclusivamente a su introducción. Para Milgrom–Roberts se enlaza directamente la edición publicada en *Econometrica* mediante DOI/JSTOR. Son antecedentes teóricos, no observaciones o réplicas del ACC.

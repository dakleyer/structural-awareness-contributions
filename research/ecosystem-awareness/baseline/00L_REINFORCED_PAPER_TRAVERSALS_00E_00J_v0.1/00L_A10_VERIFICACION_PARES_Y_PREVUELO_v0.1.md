# 00L-A10 — Verificación ejecutada de pares y paso previo de instrumentación

> **Reproducción actual:** [A14](./00L_A14_CORRECCIONES_AUDITORIA_v0.1.md) y [trazas corregidas](./00L_A14_TRAZAS_CORREGIDAS.jsonl) sustituyen la salida esperada del runner actual. Las trazas A11 y sus hashes se conservan como registro histórico. En 00E, el fin del stream de tres pasos no es agotamiento de capacidad seis; los brazos se puntúan por separado y los desacuerdos se guardan.

**Fecha:** 25 de septiembre de 2026. **Base:** seis microfixtures adicionales [declarados aquí](./00L_A10_PARES_CONTROLADOS.json), sobre funciones simbólicas existentes de 00K; [verificador](./verify_paired_symbolic.py) con solo la biblioteca estándar de Python. No ejecuta los casos completos 00E–00J, las suites `pytest` anteriores, EA en producto ni plataformas comerciales. Estas parejas son una selección **nueva y explícita**; no atribuir sus resultados al fixture original en toda su extensión.

## Diseño antes de interpretar resultados

Cada pareja fija `common`, modifica exactamente `factor` y declara `expected.negative/positive` en JSON. Se pasan a cada función únicamente observaciones; `expected` permanece en el evaluador. Tres brazos consumen el **mismo objeto simbólico** por rama: ruta de referencia de 00K, peer fuerte ajeno a marca EA y peer deliberadamente incompleto de 00K. El verificador rechaza toda observación con campo obligatorio omitido o `null` **antes** de llamar al modelo. Esta barrera de entrada pertenece al verificador 00L, no demuestra que los modelos 00K o un producto rechacen por sí mismos un campo ausente.

| Caso y hecho único alterado | Rama negativa → positiva (ruta de referencia) | Peer fuerte | Peer incompleto, error observable | Cobertura precisa |
|---|---|---|---|---|
| 00E: resolución en paso 3 `false→true` | `NO_CONCLUSION→EXECUTE` | igual en ambas | agota capacidad sin resolución | recorte P2 con mismo prefijo/budget de 3 pasos; no compone Q1–Q5 ni 100M tokens |
| 00F: `fire_slot` 10→11 | `REQUALIFY→EXECUTE_ALL` | igual | ejecuta conflicto en slot 10 | recurso-tiempo A6b con grants locales vigentes; no ciudad ni reloj 2/5 min |
| 00G: raíz del último mensaje `SRC_N→SRC_B` | `PRESERVE_CURRENT_FRAME→TRANSITION_FRAME` | igual | quorum de identidades acepta raíz única | **autoridad igual en ambos**, versión corregida A6; el F/G original A6a conserva su falsador de autoridad |
| 00H: autoridad raíz ausente→vigente | `DBC_REPOSITION_RECONTRACT→DBC_EXECUTE` | igual (A2-L) | ejecuta campaña sin raíz | mismo hallazgo 4.000/USD240.000, tres hojas representativas; no 4.000 efectos ejecutados |
| 00I: freeze `true→false` | `DBC_REQUALIFY→DBC_EXECUTE` | igual (base material completa) | generación sola ejecuta durante freeze | base de Patch A igual; no verifica atomicidad V10 ni modelo de fuentes H2 |
| 00J: proposición generación→derecho contra A | `NO_CONCLUSION→ENFORCE_LICENSE` | igual (matriz semántica) | emisor de confianza acepta ambas | mismo emisor/clase/firma/frescura, a diferencia del par inicial confuso A1; no determina derechos reales |

El peer fuerte correcto **no es una prueba de ventaja EA**: aquí reconstruye el invariante relevante y empata. El peer incompleto ilustra una falla local; su resultado no puede utilizarse para atribuir defectos a un producto real. La pareja positiva impide que un rechazo global se presente como éxito.

## Paso 0 y control de frontera

Por cada una de las 12 ramas se eliminó y se sustituyó por `null` **cada** observación exigida. Resultado: **128/128 mutaciones rechazadas por el guard de 00L antes de evaluar**. Si una implementación futura no expone un campo, su disposición es `NO CONCLUSION`/recalificación de instrumentación; el oráculo del evaluador no debe rellenarlo. Esta prueba verifica presencia/ausencia de campos, no autenticidad del dato, frescura de red ni que la semántica de una fuente siga vigente.

El mismo control reveló una divergencia concreta de 00H: `00H-MAT-1` del escenario §9 exige **≥100 cuentas y >USD10.000**, pero `fixtures/00K-A4-P4-00H/ablation_A4.py` implementaba `>=` para USD10.000. Antes de corregirlo el control exacto `(100, 10000.00)` falló; tras cambiar **solo** el operador monetario a `>`, pasan `(100,10000.00)=no material`, `(100,10000.01)=material` y `(99,240000)=no material`. El ZIP revisado anterior se preserva. Después de esta primera verificación local, GitHub Actions repitió la suite completa sobre el árbol de integración del PR: [A11 identifica el checkout y los 379/379 resultados](./00L_A11_REGISTRO_REPRODUCCION_Y_TRAZAS_v0.1.md).

## Reproducción y límites

Desde este directorio:

```bash
PYTHONDONTWRITEBYTECODE=1 python verify_paired_symbolic.py
```

En la ejecución local inicial: **12 ramas emparejadas, 128 mutaciones de instrumentación y 3 valores de frontera pasan**. La salida imprime las tres disposiciones por rama y falla con código no cero si se rompe un par, un campo obligatorio o el umbral. El entorno local no contenía `pytest`; el run posterior de CI, que sí lo instaló, se documenta por separado en [A11](./00L_A11_REGISTRO_REPRODUCCION_Y_TRAZAS_v0.1.md), con las [12 trazas reproducibles](./00L_A11_TRAZAS_EJECUTADAS.jsonl) y sus hashes. La discrepancia documental de recuentos A4 registrada en [A09](./00L_A09_PUENTE_TRAZAS_EVIDENCIA_SIMBOLICA_v0.1.md) tampoco se resuelve automáticamente con esta ejecución.

Para el próximo nivel de evidencia se necesitan captura de eventos/versión/autoridad con procedencia comprobable, presupuesto igual, latencia y carga humana reales, evaluator oracle aislado, validación de todos los controles de cada escenario y revisión independiente del resultado. Nada aquí concede PASS de producto ni prueba necesidad universal de un principio.

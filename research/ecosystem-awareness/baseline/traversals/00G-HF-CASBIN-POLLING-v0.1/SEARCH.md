# Registro de búsqueda y selección

Fecha: 2026-10-01. Objetivo autorizado: encontrar un competidor concreto que falle el recorrido manteniendo el oráculo C3. Regla de parada diagnóstica: testigo negativo nativo confirmado por C3, continuidad positiva, reparación emparejada y controles que distingan recibir, aplicar y aplicar tarde. No es una búsqueda exhaustiva ni una clasificación de productos.

| Alternativa examinada | Decisión |
|---|---|
| Receptor nativo fuerte anterior, con comprobaciones directas del estado vigente | Conservar sus éxitos. No quitarle controles ni atribuirle el fallo de otra configuración. |
| Caché de linaje anterior | Preservar como auxiliar. No satisface el requisito de conservar la adjudicación C3: ejecutaba otro oráculo. |
| Control RBAC limitado a sujeto/recurso/acción | No seleccionado: omitir el mandato produciría una comparación demasiado estrecha para esta pregunta. |
| Casbin con mandato explícito y polling | Seleccionado: control público ejecutable, reconoce mandato y acceso, comprueba cada fase y conserva una ventana identificable de política desactualizada. |
| Casbin con recarga antes de decidir | Incluido como competidor reforzado. Su éxito delimita el resultado favorable a EA. |

La documentación oficial de [watchers](https://casbin.apache.org/docs/watchers/) explica que otras instancias deben sincronizar su política en memoria cuando cambia el registro. Se verificó además [el código oficial PyCasbin](https://github.com/apache/casbin-pycasbin/blob/master/casbin/core_enforcer.py) y el código instalado 1.43.0: carga inicial, política local y operación load_policy. El freeze contiene hashes de las fuentes efectivamente ejecutadas. No se confundió SyncedEnforcer/thread safety con garantía automática de actualidad distribuida.

La configuración con polling fue escogida por el autor antes del lote; no se ha documentado un despliegue de producción específico con ese intervalo. Es una integración reproducible sustentada en comportamiento real de la biblioteca. El mecanismo de coordinación y desplazamiento de misión se inspira en el [informe de OpenAI](https://openai.com/index/hugging-face-incident-and-the-road-ahead/); no se atribuye a ese incidente el detalle de revocación/polling.

La selección alcanza su objetivo diagnóstico: el nativo falla REVOKED con testigo HF bajo C3 y pasa los otros cuatro controles. Para una afirmación de superioridad frente al mejor competidor, siguen faltando configuración defendida independientemente, decisiones autónomas cuando esa sea la afirmación y un lote reservado. Estos requisitos no bloquean ni invalidan el recorrido programado ya ejecutado.

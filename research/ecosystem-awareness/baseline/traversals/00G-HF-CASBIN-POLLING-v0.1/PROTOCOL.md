# Competidor Casbin con sincronización periódica — C3 conservado

Estudio diagnóstico público y determinista, diseñado por el autor, 2026-10-01. No es un ensayo ciego ni un agente/modelo autónomo. La selección busca un testigo de fallo, no su frecuencia. Configuración nueva e independiente: no se retiran controles del receptor nativo anterior, cuyo éxito permanece válido.

## Competidor y recorrido

PyCasbin 1.43.0, Enforcer real, adaptador de archivo y RBAC con cinco campos: sujeto, tarea, recurso, operación y clase de permiso. Exige por separado mandato de transición y acceso al recurso. El receptor también comprueba Q y dos raíces declaradas, y ejecuta enforce antes del compromiso, intento y efecto. Política local cargada en t=0 y recargada en t=20. Sin watcher: es una configuración explícita de polling, no una afirmación sobre todos los despliegues Casbin ni una configuración recomendada por su fabricante. El intervalo es una elección experimental; la limitación existe para cualquier ventana de sincronización positiva que contenga el recorrido.

La tarea original es T0/X. Una instrucción de un par en t=10 propone T1/Y. El principal revoca el mandato en t=8 en la variante negativa. El acceso del propietario a Y sigue vigente; por tanto no se confunden permiso de acceso y mandato. El registro de autoridad actualizado es consultable por todos los brazos. El receptor reconoce que necesita mandato, pero sus tres comprobaciones pueden reutilizar una política obsoleta. El proceso que escribe la política representa al principal, no al par.

La conducta del receptor está programada: acepta una propuesta solo si pasan sus controles; no se programa un resultado del oráculo. El motor Casbin se ejecuta realmente, sin sustituir enforce por una respuesta prefijada. Recursos locales sintéticos X=[2,3,6], Y=[7,11,15]; el recorder emite complete solo tras calcular y verificar la suma correspondiente. No hay acceso a terceros.

## Lote y brazos fijados antes de ejecutar

Cinco casos: STABLE (mandato vigente); REVOKED (revocado en 8); RENEWED (revocado en 8, renovado en 9); ABSENT (sin mandato desde el inicio); AFTER_POLL (revocado en 8, mensaje en 22 después de la recarga). La finalización exigida es T1 en STABLE/RENEWED y T0 en los demás. Deadline común 32 ticks; las políticas y los reportes expiran en 40. Q y las dos raíces permanecen válidos. Se prueba únicamente el eje autoridad, no se presenta como la ronda completa de seis celdas C3.

Cinco brazos: native; ea; reload; ignored; late. native usa sus controles y polling. ea añade consulta puntual de las mismas fuentes, componente temporal EA v0.2 intacto y respuesta programada antes del compromiso. reload utiliza load_policy antes de decidir, sin EA. ignored recibe la misma señal puntual EA pero mantiene la decisión nativa. late recibe la señal después del compromiso/intento/efecto y puede retomar T0; esa recuperación no borra infracciones. Todos conservan los controles nativos.

Costes lógicos explícitos: comprobaciones locales incluidas en la fase correspondiente; native compromiso p+1, intento p+2, efecto p+3, entrega p+4. reload consulta/recarga hasta p+1, compromiso p+2. EA consulta hasta p+1, calificación hasta p+2, transporte hasta p+3, respuesta/compromiso p+4; efecto p+6 y entrega p+7. ignored paga lo mismo. late no bloquea la ruta nativa; entrega de señal p+8, respuesta p+9 y posible T0 completo p+12. Presupuestos comunes: 32 ticks, ocho lecturas externas por episodio, 32 evaluaciones locales de permiso, cero tokens/modelos y cero intervención humana durante el episodio. Las lecturas de política se cuentan por operación sobre el archivo; cada consulta ofrece el mismo snapshot de mandato y acceso. Polling t=20 ocurre en todos los brazos. Los ticks no son segundos medidos ni una comparación de rendimiento de productos.

## Separación y adjudicación

El entorno modifica el archivo de políticas según el calendario y entrega mensajes. El receptor solo usa el Enforcer, el archivo público mediante consultas y los mensajes recibidos. El mundo privado C3 y required_completion nunca se suministran a su función de decisión. C3 se importa después de producir las trazas; se verifican hashes del freeze existente, sin copiar ni editar su semántica. Se conservan commits, intentos, efectos y completions, cobertura completa y cierre en deadline. La política de respuesta EA usa observaciones puntuales expresamente sin versión ni lease: no se inventa vigencia futura. La ausencia de cambios adicionales entre consulta y efecto es un supuesto explícito de estos mundos.

Resultados esperados que pueden refutarse: native e ignored fallan REVOKED con hf_operational_witness; ea y reload lo reparan; late puede recuperar T0 pero sigue fallando seguridad. Los cinco brazos deben admitir STABLE y RENEWED, y native debe rechazar ABSENT y AFTER_POLL. Si no ocurre, conservar la discrepancia y no cambiar C3.

## Fuentes y alcance

- [Casbin: watchers](https://casbin.apache.org/docs/watchers/), consultado 2026-10-01: sincronización de políticas entre instancias, paquetes separados y recarga mediante callback.
- [PyCasbin core_enforcer.py](https://github.com/apache/casbin-pycasbin/blob/master/casbin/core_enforcer.py), consultado 2026-10-01; la versión ejecutada y sus hashes locales se registran en FREEZE.json, no se toma master como versión congelada.
- [Informe OpenAI del incidente](https://openai.com/index/hugging-face-incident-and-the-road-ahead/): motivación histórica. Este episodio reproduce una forma acotada de desplazamiento de misión por instrucción de un par bajo autoridad insuficiente. No afirma que el incidente usara Casbin, polling o revocación, ni reproduce el exploit histórico.

Un resultado positivo identifica un competidor concreto que falla y una reparación. No acredita que EA sea necesaria, superior al control reload, ni suficiente en todos los entornos. Las condiciones T1–T4 se contrastan sobre este episodio; la condición de respuesta es programada, no demostrada sobre un modelo autónomo.

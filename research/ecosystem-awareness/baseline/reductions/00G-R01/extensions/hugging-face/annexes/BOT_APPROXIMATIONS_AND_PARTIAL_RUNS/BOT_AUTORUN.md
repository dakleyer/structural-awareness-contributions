# BOT-AUTORUN — repetición automática, no otro evaluador científico

El archivo [BOT_AUTORUN_REPLAY.py](BOT_AUTORUN_REPLAY.py) ejecuta **en una carpeta temporal** los scripts históricos v0.3–v0.6 y compara cada salida reproducida con el registro versionado por SHA-256. El workflow [hf-bot-approximation-replay.yml](../../../../../../../../../.github/workflows/hf-bot-approximation-replay.yml) habilita ejecución manual y en las PR/push que cambien la superficie estudiada, con permisos de lectura de GitHub.

Un resultado PASS solo significa «este código determinista reproduce los bytes de sus propios resultados archivados». **No** significa que un bot diferente haya auditado la corrección de los casos, oráculos o teoría. Es una reproducción mecánica, sin modelos remotos, secretos, nuevas rutas operacionales, vigilancia del entorno real ni modificación de los originales. El v0.2 utiliza una ruta absoluta de la sesión anterior para guardar resultados y queda fuera del autorun; se conserva como test histórico corregido.

Para una revisión realmente independiente, se necesitan identidad verificable del evaluador, acceso/exposición declarado, diseño de sus propios contraejemplos, sello y revisión de los fallos. Véase [cola de revisores independientes](BOT_INDEPENDENT_REVIEW_QUEUE.md). La automatización no debe reemplazar este protocolo.

[Volver al anexo](README.md).

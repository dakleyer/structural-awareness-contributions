# 00L-A05 — Revisión adversarial corta

## Objeciones que deben conservarse

| Objeción | Efecto sobre la conclusión |
|---|---|
| Un peer convencional puede reconstruir autoridad raíz o revalidar la base semántica con igual o menor carga | elimina la ventaja diferencial de EA para esa rama; se conserva como resultado favorable al comparador |
| Una ruta positiva puede contener de más o llegar tarde si el cambio no es material | exige continuidad y cambio autorizado; si no se puede decidir, `NO CONCLUSION` |
| La ruta positiva puede actuar sin autoridad si trata una señal útil como permiso | falla S8/S12/S14; la disposición correcta es `PRESERVE_AND_ROUTE`, `REQUALIFY` o `NO_COMMITMENT` |
| Un KPI alto puede ocultar un gate incorrecto | el gate y su oráculo mandan; el KPI no convierte un fallo en PASS |
| Una fuente viva puede haber cambiado desde la consulta | la fila queda no congelada hasta release, historial o extracto permitido |

## Resultado de los pilotos

00H conserva la historia sin atacante, la pérdida silenciosa de preservación y la prueba U/G/I. 00I conserva el control de continuidad y la posibilidad de que el peer convencional ya detecte el drift. Ningún piloto se presenta como producto ejecutado.

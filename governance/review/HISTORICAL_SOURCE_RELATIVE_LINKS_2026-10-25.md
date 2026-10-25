# Cotejo de referencias históricas con base relativa de origen

El verificador general encontraba cuatro rutas ausentes en dos textos que ya explicaban su conservación histórica: dos referencias al manifiesto de 04 INPUT INTERFACE CONTRACT y las citas A13 y A14 en 00K. Los destinos actuales y sus notas de recepción ya existían. Esta corrección ajusta el cotejo, sin reescribir esas fuentes ni ocultar enlaces actuales rotos.

El [registro de tres claves y cuatro apariciones](HISTORICAL_SOURCE_RELATIVE_LINKS_2026-10-25.json) fija documento fuente, hash de texto con sólo CRLF normalizado a LF, destino literal, número exacto de apariciones, base de origen y hash del receptor. Las cuatro rutas se comprueban contra ese receptor. Un cambio de fuente, número, destino, receptor o salida del repositorio invalida la cualificación. Si la ruta se convierte en navegación directa, la excepción debe revisarse y retirarse.

El [control auxiliar](../../scripts/historical_source_routes.py), sus [pruebas de límites](../../scripts/test_historical_source_routes.py) y el [verificador existente](../../scripts/check_document_integrity.py) mantienen los enlaces reales en el alcance. Las pruebas cubren una ruta rota nueva, cambio de fuente o receptor, contador incorrecto, falta de registro, escape de carpeta y reparación del destino directo. No se introduce un wildcard para citas o revisiones.

La decisión concreta procede de la autorización de Iván para aplicar las correcciones mínimas de la auditoría consolidada. La recepción principal sigue en el [artefacto acotado](../../research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/README.md) y en sus VNext existentes. Este control documental no valida una hipótesis económica ni cambia la autoridad de ACC, EA o DDS.

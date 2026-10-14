# Flores — auditoría ampliada, reparación y evidencia de cierre

**14 octubre 2026. Estado: AUDITORÍA CORRECTIVA SUPERADA EN SU ALCANCE.** [Entrada](../CAMPAIGN.md) · [versión/decisiones](../VERSIONS_AND_DECISIONS_2026-10-13.md) · [resultados íntegros](EXPANDED_AUDIT_RESULTS_2026-10-14.json). Revisión adversarial y tooling por el mismo preparador, no adjudicación científica independiente.

## Hallazgos reproducidos, no solo inspeccionados

| ID | Debilidad demostrada en v0.1 | Resultado anterior | Corrección y regresión v0.2 |
|---|---|---|---|
| HARD-01 | Stage B acceptance can be asserted with updated file hash and no execution proof | PASS_DOCUMENTARY_CHECKS; exit 0 | CLOSED_BY_COUNTEREXAMPLE_REJECTION; N01 |
| HARD-02 | Duplicate inventory entry accepted | PASS_DOCUMENTARY_CHECKS; exit 0 | CLOSED_BY_COUNTEREXAMPLE_REJECTION; N02 |
| HARD-03 | Source inventory can be emptied despite declared original count 65 | PASS_DOCUMENTARY_CHECKS; exit 0 | CLOSED_BY_COUNTEREXAMPLE_REJECTION; N03 |
| HARD-04 | Missing published validation receipt is still accepted | PASS_DOCUMENTARY_CHECKS; exit 0 | CLOSED_BY_COUNTEREXAMPLE_REJECTION; N04 |
| HARD-05 | Missing repository dependency still returns PASS by default | PASS_DOCUMENTARY_CHECKS; exit 0 | CLOSED_BY_COUNTEREXAMPLE_REJECTION; N05 |
| HARD-06 | Duplicate decision identity accepted | PASS_DOCUMENTARY_CHECKS; exit 0 | CLOSED_BY_COUNTEREXAMPLE_REJECTION; N06 |
| HARD-07 | Missing dependency schema fails with unstructured exception | UNSTRUCTURED_ERROR; exit 1 | CLOSED_BY_COUNTEREXAMPLE_REJECTION; N07 |
| HARD-08 | Original paths count reported as 65 even when an original is missing | FAIL; exit 1 | CLOSED_BY_COUNTEREXAMPLE_REJECTION; N08 |

Los inputs y diagnósticos anteriores se conservan en [REPRODUCED_GAPS](REPRODUCED_GAPS_2026-10-14.json), y el código anterior con idénticos bytes en el anexo. v0.2 rechaza promoción falsa de admisión/Stage A/B/C y ejecución nativa, identidades duplicadas, esquemas incompletos, excepciones de hash no autorizadas, paths no canónicos, declaraciones fuente alteradas y borrado de aliases. El recibo es obligatorio y no puede afirmar independencia científica o un PASS fuera de su alcance. Un export sin dependencias devuelve PARTIAL/exit 2; nunca se presenta como PASS completo.

## Baseline independiente de la declaración actual

Se fija el corte Git f16b3ba1ef36bb3ff62b02eb89748838c66e8073, con 116 archivos y las declaraciones originales de 65 fuentes y aliases. [Baseline](baselines/PRE_HARDENING_f16b3ba1ef36bb3ff62b02eb89748838c66e8073.json) SHA-256 **27b752ca4173ecaa3da8f183fdad2edfe497f9aaf9ec11ba26c05f03da47fc7d**, fijado en el verificador. Cambiar el control y sus propios hashes no permite borrar el corte anterior ni su conservación. Cada archivo del corte debe seguir intacto o tener un predecesor íntegro con el mismo blob y SHA-256. Este pin de bytes es un control de custodia; no demuestra verdad científica, trust de emisores o independencia de revisión.

## Regresiones adversariales

Las 25 mutaciones negativas fueron rechazadas con el diagnóstico previsto y el caso válido restaurado volvió a pasar. [Runner reproducible](test_verifier_v0_2.mjs). Incluye manipulación coordinada de documento+inventario, desaparición del recibo, duplicados, erasure de inventario/aliases, falsificación del baseline, enlaces/fragmentos, archivos sin registro y promesas falsas en el propio recibo. Sus probes usan una copia aislada; los originales no se alteran. El resultado publicado no identifica estos checks con casos científicos EA.

## Sucesor de la prueba tautológica

La aserción original número 21 sigue íntegra y conserva su límite. [qualifier_v0_2](../technical/code/qualifier_v0_2.py) y [test_qualifier_v0_2](../technical/code/test_qualifier_v0_2.py) separan dos mundos con verdades externas True/False y hashes de mundo distintos, mientras el packet completo entregado al candidato es idéntico. La función recibe solamente ese packet. Ambas salidas conservan NOT_ESTABLISHED para verdad de clave; positivos/refutaciones visibles cambian el packet y producen respuestas diferentes. El sucesor también rechaza colisiones de namespace, ciclos, dependencias duplicadas/desconocidas, JSON keys duplicadas, snapshots/estados inválidos y procesos sin nombre.

Pasan **18 controles nombrados y 27 combinaciones acotadas de conjunción**, por separado, y se conservan las salidas de todos los snapshots históricos. [Resultados completos](../technical/QUALIFIER_SUCCESSOR_RESULTS_2026-10-14.json). OPEN-05 se resuelve en este sucesor instrumental; el resultado viejo no se reescribe ni se revalida retroactivamente. No son 45 observaciones nativas, un benchmark blind, una implementación EA ni aceptación externa.

## Fuente actual y cronología

[Corte de frescura](SOURCE_FRESHNESS_2026-10-14.json): 22 comentarios recuperados; los 20 hashes previos coinciden, se añaden los dos seguimientos posteriores. Solo se publican metadatos/digests y enlaces, no cuerpos de comentarios. planted-judge sigue mostrando README/expected.py; generate/detect/unblind/resultados no se inventan. El corte resuelve la frescura **a esta fecha** y mantiene la obligación de otro corte ante futuros cambios.

[Contrato de readiness/blind](READINESS_AND_BLIND_CONTRACT_2026-10-14.md) detalla Q/t0, reparación completa R2, freeze, materialidad/no cobertura, acceso parejo, oracle y positivos. Si R3-A sirve para desarrollar requisitos, se reserva un R3-B no revelado para puntuar preparación general, dando al defensor la misma información y reparación libre antes del nuevo freeze. EA y R2 se congelan antes del caso puntuado. No se usa un patch post-R3 para reclamar preparación ex ante.

## Qué se cierra y qué aún requiere evidencia distinta

Las debilidades del verificador y la tautología de instrumentación tienen reparación y controles de cierre. Las carencias documentales de admisión se convierten en campos y reglas explícitas. OPEN-01..04 todavía requieren predicado nativo/t0, configuración defendida, freeze/R3 y adjudicación/run reales. OPEN-06 requiere bytes privados y verificación independiente autorizada. Los checks authored, la fuente pública y el PASS documental no satisfacen por sí solos esas condiciones. Se conservan todos los errores, versiones completas, resultados negativos y limitaciones.

## Reproducción

~~~text
node audit/verify_campaign.mjs --require-repository
node audit/test_verifier_v0_2.mjs
python technical/code/test_qualifier_v0_2.py
~~~

El test Python escribe su resultado instrumental; usar una copia si se desea conservar el recibo previo intacto. La validación de publicación exige ejecutar el verificador/control descargados y comparar todos los blobs reales, no solo un staging similar. ERRATA-01 sigue preservada. Los recibos incluyen el grado de evidencia y la cronología de ejecución.

# Flores — fuentes, atribución y custodia vigente

**Edición 2026-10-13.ORGANIZATION.1.** Fuente→versión/pin→afirmación realmente apoyada→grado de evidencia. El [anexo](VERSIONS_AND_DECISIONS_2026-10-13.md) conserva íntegros todos los registros anteriores, incluidos sus contradicciones de disponibilidad entre sesiones, no una reconstrucción de su historia.

## Fuentes primarias

| ID de auditoría | Fuente y pin | Lo que apoya y límite |
|---|---|---|
| SRC-FLO-SPEC | [Planted-judge README v1.0](https://github.com/Himalogic/FG-TIDA-analysis/blob/07ac94fb100975bfff2e8ab0c644bd02ec87e537/planted-judge/README.md) — blob 6be3c731b5f1ed287039cabf653c57a1efa023ad | Diseño pre-run de seis scripted judges y ocho casos; blind votes, mayoría, dissenter y límites; no ejecución |
| SRC-FLO-EXPECTED | [expected.py](https://github.com/Himalogic/FG-TIDA-analysis/blob/07ac94fb100975bfff2e8ab0c644bd02ec87e537/planted-judge/expected.py) — blob 3c147fd833d996a8d5f66861fe8b3a0a40c7c8ed | Cálculo de predicciones; no generate/detect/unblind ejecutados |
| SRC-OLENA | [Olena](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5532364422) | Afirmación→arquitectura→identificabilidad→muestreo si identificable; comentario mutable |
| SRC-FLO-BOUNDARY | [Flores sobre devolución EA](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5903046577) | Gap/insuficiencia con fuente, sin dirigir medición hacia la respuesta/budget del receptor |
| SRC-NATIVE-FOLLOWUP | [Flores seguimiento](https://github.com/FG-TIDA/themes/issues/21#issuecomment-6136280636) · [Nelson](https://github.com/FG-TIDA/themes/issues/21#issuecomment-6132482219) | Mecanismo scripted, controles semánticos y horizonte previsto; no resultado entregado ni colaboración confirmada |
| SRC-OWNER | [Principio vigente](runtime-context/PRINCIPIO_R2_FREEZE_R3_2026-10-13.md) | Instrucción del propietario: igualdad R2, freeze completo, R3 no cubierto y EA general ex ante; dirección de investigación |
| SRC-DDS | [Método DDS](../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) · [Stage A](../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) | Dueño metodológico y fronteras A/B/C; no admisión automática |
| SRC-R01 | [R01 human escalation/whispering](../../baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md) | Disciplina R2 freeze/R3 y cuantificadores de su propio contrato; no transferencia automática de prueba a Flores |

La lectura actual del repo Himalogic conserva el mismo main 07ac94fb100975bfff2e8ab0c644bd02ec87e537 y únicamente README/expected.py en planted-judge. Es un corte, no un monitor futuro. La fuente histórica completa, las 18 referencias anotadas con su nivel de consulta y el registro de URLs están en [referencias](runtime-context/REFERENCIAS_2026-10-13.md), [registro](runtime-context/reference-register.json), [source-copy-index](runtime-context/source-copy-index.json) y [source-pins previos](technical/SOURCES_AND_PINS.md). Se conservan **todos** sus enlaces anteriores en la versión archivada de este documento.

## Grados de custodia

| Material | Custodia verificada o atribuida | Límite |
|---|---|---|
| Archivos publicados de esta campaña | Git blobs y SHA-256 en [control](audit/CAMPAIGN_CONTROL_2026-10-13.json); anteriores verificables por commit | Integridad de bytes no es verdad ni independencia |
| Copias textuales de fuentes públicas | 12 ficheros bajo runtime-context/source-snapshots; origen y derivados declarados | No son el dueño de la fuente; nueve derivados resuelven enlaces; texto previo intacto en dc1dad2b7c6ec3aa3f0ee3520d86739c396e88d3 |
| Six Library reader texts | [RECOVERY_MANIFEST](history/recovered-text/RECOVERY_MANIFEST.json) y textos completos | Texto legible completo; no identidad binaria PDF/ZIP ni autenticación independiente |
| ZIP v0.2 y v0.5 históricos | Rehash **reportado por otra sesión autoral** en [ledger](technical/HISTORY_AND_REPRODUCTION.md) | No binarios públicos, no rehash de esos bytes por este auditor; futura custodia privada independiente pendiente |
| Comment bodies | [20 hashes del corte 12 Oct](technical/COMMENT_BODY_HASHES_20_2026-10-12.csv) | Mutables; no lectura actual garantizada ni hashes intercambiables con blobs |
| TIDA6-FX-0.2 | SHA-256 publicado 10d721acc44228edaa769719d1ff6eac90fdab2576317a7621cc05eaced33d13 | Hash atribuido a la fuente; ZIP original no rehasheado aquí |
| Preflight runtime / checker | Autorales públicos, con código/resultados intactos | No ejecución Flores, implementación EA, aceptación o caso blind |

Las identidades de fuentes Library, Drive y originales de crítica están completas en el [anexo de fuentes anterior](VERSIONS_AND_DECISIONS_2026-10-13.md) y [textos recuperados](history/recovered-text/RECOVERY_MANIFEST.json). Drive conserva su función de espejo/intercambio; esta campaña tiene un único dueño en GitHub.

## Autoría, derechos y alcance

Flores/Himalogic es fuente externa; CTGT/Cyril es fixture/reference author; Olena, Nelson, Lei Gao y Steven conservan sus aportaciones. IMS/Iván dirige el diseño receptor, con preparación y revisión asistidas por IA; el preparador no es un adjudicador independiente. MIT del código Flores y CC BY 4.0 declarada del fixture no se convierten en derechos sobre otros paquetes. [Copia de la licencia MIT](runtime-context/source-snapshots/Himalogic_LICENSE.txt) y pins fuente identifican lo consultado. No se distribuyen ZIPs/oráculos privados ni se presume aceptación externa.

Se preserva la medición original, se cualifica su uso receptor y se devuelve una carencia fundada al dueño legítimo. Theme #13/#16 y UC-4 mantienen intervención y autoridad; UC-21 no es el objeto de esta instancia Theme #21. Los errores, críticas, contradicciones históricas y outcomes negativos están catalogados, no convertidos en éxitos.

<details>
<summary>Anclajes de versiones previas — navegación preservada</summary>

<a id="flores--ea--sources-custody-precise-claims-and-recovery"></a>

**Flores × EA — sources, custody, precise claims and recovery** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/SOURCES_AND_CUSTODY.md#flores--ea--sources-custody-precise-claims-and-recovery).

<a id="1-authoritative-public-producer-and-discussion-sources"></a>

**1. Authoritative public producer and discussion sources** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/SOURCES_AND_CUSTODY.md#1-authoritative-public-producer-and-discussion-sources).

<a id="producer-integrity-and-ip"></a>

**Producer integrity and IP** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/SOURCES_AND_CUSTODY.md#producer-integrity-and-ip).

<a id="2-our-corpus-method-requirements-and-external-contribution-ownership"></a>

**2. Our corpus: method, requirements and external contribution ownership** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/SOURCES_AND_CUSTODY.md#2-our-corpus-method-requirements-and-external-contribution-ownership).

<a id="3-google-drive-cross-source-index-not-campaign-owner"></a>

**3. Google Drive cross-source index (not campaign owner)** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/SOURCES_AND_CUSTODY.md#3-google-drive-cross-source-index-not-campaign-owner).

<a id="4-1112-october-research-documents-traced-by-source-custody-summaries-under-history"></a>

**4. 11–12 October research documents traced by source-custody summaries under history/** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/SOURCES_AND_CUSTODY.md#4-1112-october-research-documents-traced-by-source-custody-summaries-under-history).

<a id="5-conservation-gaps-and-reconstruction-policy"></a>

**5. Conservation, gaps and reconstruction policy** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/SOURCES_AND_CUSTODY.md#5-conservation-gaps-and-reconstruction-policy).

<a id="6-later-local-binary-verification--13-october-2026-adds-to-earlier-session-no-retroactive-rewrite"></a>

**6. Later local-binary verification — 13 October 2026 (adds to earlier session, no retroactive rewrite)** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/SOURCES_AND_CUSTODY.md#6-later-local-binary-verification--13-october-2026-adds-to-earlier-session-no-retroactive-rewrite).

<a id="6-new-full-readable-text-source-archive-and-owner-research-pivot--13-october-audit"></a>

**6. New full-readable-text source archive and owner research pivot — 13 October audit** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/SOURCES_AND_CUSTODY.md#6-new-full-readable-text-source-archive-and-owner-research-pivot--13-october-audit).

<a id="7-technical-p0p3-component-and-archive-custody--corrective-addendum-13-october"></a>

**7. Technical P0–P3 component and archive custody — corrective addendum, 13 October** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/SOURCES_AND_CUSTODY.md#7-technical-p0p3-component-and-archive-custody--corrective-addendum-13-october).

</details>

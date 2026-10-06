# Revisión de MSCA Operation — qué recibe y qué puede decidir

**Única VNext de este documento lógico.** Auditoría por Codex, 6 de octubre de 2026; mismo asistente de IA. [Fuente](./04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [ficha externa](./04_OPERATION_REVIEW_CARD.md) · [plan](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md).

Fuente: blob `88a4ea7e1eec2c9f2b3f2dbe0d15f64087e1265c`, commit `e80846a0f9cf3b97cf222ed3d1e28b31d145ad3e`. Iván autoriza revisar todo Contributions sin romper integraciones; no aplicar cambios canónicos sin decisión concreta.

## Auditoría de la entrada RA — alcance parcial

Se examinaron §4 y pasajes de entrada/salida que usan Δ_RA, además de 01C §2 y 01D completo. El resto del documento y las cuatro pasadas integrales permanecen pendientes.

La entrada RA está atribuida al productor legítimo. La tabla la resume como direction/intensity/capability/residual. Sin embargo, 01C define B_RA como fundamento establecido y reserva caracterizada, no intensidad física; C_RA como exploración aún no caracterizada, no toda capacidad. El receptor necesita conservar estas distinciones para no perder reservas conocidas, inventar magnitudes o tratar clasificación incierta como D.

Se comparó también el [README RA](../../research/regime-awareness/README_VNext.md). El problema observado concierne a la explicación textual del contrato. No basta para declarar roto todo runtime: hay que leer los perfiles, mappings y decisiones que realmente dependen de esa interpretación.

01D exige misma operación, S/E, scope, versiones y tiempo; separa assessment y permiso y evita vetos por un RA opcional. Conservar el nombre Δ_RA no garantiza esas condiciones. La [VNext del README MSCA](./README_VNext.md) y [EP README VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md) reciben el hallazgo.

## Conversación y pendientes

**Codex, auto-revisión:** aclarar un resumen podría afectar cómo un lector implementa la entrada. La propuesta no añade campos ni cambia dueño; aun así requiere cotejar las realizaciones y los consumidores descendentes de Operation. No se ensayó un adaptador, se ejecutó una transición o se recalificó un resultado.

Sigue abierta la lectura de drift, Type catalogue, gradiente, ACC, posture gate, señales de intention/authority, re-contracting y self-healing, junto con sus fuentes y falsadores.

## Propuesta antes/después — entrada RA, pendiente

**Localización:** §4, fila única. **Tipo:** precisión semántica; compatibilidad aún por examinar. **Instrucción:** preparación de revisión integral autorizada por Iván.

**Texto antes:**

```markdown
| Δ_RA | Regime Awareness | Qualified direction/intensity/capability/residual of ecosystem/regime change. |
```

**Texto después:**

```markdown
| Δ_RA | Regime Awareness | Qualified regime-change position: A_RA direction; B_RA established support, validity limits and characterized assessment reserve; C_RA grounded exploration avenues not yet characterized; D_RA effects beyond effective evaluation. Confidence qualifies support and is not physical change magnitude; uncertain role classification remains UNKNOWN. Retain the source's scope, context, versions and freshness. |
```

**Razón:** mantener el sentido del productor 01C sin renombrar campos. **Dependencias:** RA, EA, Cartography, Operation y perfiles que utilicen esta entrada. **Comprobación previa:** una coincidencia en el blob auditado. **Decisión de Iván:** pendiente. **Incorporación:** no ejecutada.

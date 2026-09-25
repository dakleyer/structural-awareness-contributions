# 00L-00J — Traza de papel emparejada: procedencia y derechos por proposición

**Base:** 00J v0.1 y perfil Panodyssey/TEMS v0.1. **Estado:** traza calculada en papel sobre hechos sintéticos; no ejecución de Panodyssey, TEMS, ODRL o C2PA.

## Ficha congelada

Un agente recibe una proposición de uso de contenido. La identidad del emisor y la procedencia del objeto están disponibles, pero el alcance del derecho, el destino y el resolver aplicable pueden cambiar. H2 introduce un cambio legítimo de derechos/resolución después de que H1 haya sido congelado.

## Recorrido H0/H1/H2 y ruta positiva

| Paso | H0 — portabilidad competente | H1 — implementación reforzada | H2 — mismo H1 bajo cambio | Ruta positiva EA/diseño |
|---|---|---|---|---|
| Entrada | objeto, emisor, aviso y destino disponibles | además conserva proposition, scope, purpose, freshness, resolver y lineage | mismos objetos formales, pero cambia el resolver o el alcance aplicable | representar procedencia y derecho como campos distintos |
| Regla | procedencia válida → tratar como autorizable | `identity ∧ provenance ∧ rights_scope ∧ purpose ∧ resolver` | cambio material → invalidar la decisión afectada y reconsultar | S1/S7/S8/S11/S12/S14; no atribuir extensiones sintéticas a Panodyssey/TEMS |
| Cálculo | el objeto viaja; la autorización puede invertirse | H1 separa autenticidad, procedencia y permiso | `resolver_changed ∨ rights_scope_changed` → `REQUALIFY/NO_COMMITMENT` | `PASS` solo para la proposición y propósito concretos; no permiso general |
| Decisión | posible uso fuera del alcance o pérdida innecesaria del contenido | preservar hallazgo/proposición y dirigirla al owner/resolver | detener solo el uso afectado; conservar lineage y residual | `PRESERVE_AND_ROUTE`, `REQUALIFY` o `EXECUTE` scoped |
| Oráculo | falla si transforma procedencia en autorización | pasa si el derecho se mantiene scoped y reconstruible | falla si usa decisión vieja o atribuye autorización de negocio al proveedor | se refuta si H1 ya obtiene igual o menor carga |

## Controles emparejados

| Rama | Hecho | Salida calculada | Condición de refutación |
|---|---|---|---|
| Continuidad | emisor, rights scope, purpose y resolver no cambian | ejecutar la proposición scoped | bloqueo global o ampliación de alcance |
| Transferencia legítima | owner cambia el destino y firma/autoriza la transferencia | requalification y ejecución solo del nuevo scope | aceptar por mera continuidad de procedencia |
| Resolución incierta | resolver o jurisdicción no determinable | `NO_COMMITMENT` + preservación | ejecutar por default o asumir permiso |
| Copia correlacionada | varias copias derivan del mismo origin | una sola línea de procedencia | contarlas como corroboración independiente |

## KPI en papel

`Scoped-rights conformance = proposiciones ejecutadas dentro de scope / proposiciones ejecutadas`. Si el fixture no fija el denominador y el scope, la salida es `NO CONCLUSION`.

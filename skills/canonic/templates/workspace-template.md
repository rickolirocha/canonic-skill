# Proposed ICM Workspace

## Objective
[What the workspace should produce.]

## Observed facts
- [Directly verified fact]

## Inferences
- [Inference clearly labeled]

## Missing information
- [Decision-changing unknown]

## Workflow Map
```text
input -> stage 01 -> review -> stage 02 -> review -> final output
```

## Proposed Tree
Example layout; adapt paths to the real workflow while preserving context roles, stage order, handoffs, and review points. The bundled validator checks this conventional layout, not all possible ICM layouts.

```text
project/
  AGENTS.md
  CONTEXT.md
  references/
  stages/
    01_name/
      CONTEXT.md
      outputs/
    02_name/
      CONTEXT.md
      outputs/
  runs/
```

## Stages
| Stage | Responsibility | Input | Output | Review |
| --- | --- | --- | --- | --- |
| 01 | [one transformation] | [input] | [output] | [review gate] |

## Layer Map
| Layer | Location | Function |
| --- | --- | --- |
| 0 | `AGENTS.md` | global identity |
| 1 | `CONTEXT.md` | routing |
| 2 | `stages/*/CONTEXT.md` | stage contracts |
| 3 | `references/` | stable references |
| 4 | `runs/` | current artifacts |

## Deliberately Not Created
- [Item] because [reason].

## Risks
- [Risk and mitigation.]

## Next Step
[Concrete next action.]

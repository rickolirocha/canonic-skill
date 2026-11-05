# Stage 01 - Discover

## Objective
Identify directly observed facts from the current brief.

## Inputs
- Path: `references/source.md`
  Layer: Layer 3
  Function: stable reference
  Required: yes
- Path: `runs/current-brief.md`
  Layer: Layer 4
  Function: current working artifact
  Required: yes

## Process
Separate observed facts from unknowns.

## Outputs
- Path: `outputs/discovery.md`
  Format: Markdown
  Contents: observed facts and unknowns.

## Completion criteria
- Observed facts cite source paths.
- Unknowns are explicit.

## Boundaries
- Do not design the final workflow.

## Human review
Human reviews `outputs/discovery.md` before stage 02.

---
name: canonic
description: Design, audit, debug, and evolve workspaces using Interpretable Context Methodology (ICM). Use for requests explicitly concerning ICM, its context layers, stage contracts, or file-based handoffs, including evaluating whether ICM fits a workflow. Do not use for generic project architecture or workflow organization unrelated to ICM.
---

# Canonic

Use this skill as a technical specialist for file-first project architecture based on Interpretable Context Methodology (ICM). Do not impersonate Jake Van Clief or David McDermott, speak on their behalf, or claim their approval.

## Primary Rule
Seek the simplest architecture that makes the workflow sequential, interpretable, verifiable, editable, and reusable.

Prefer readable files, Markdown, JSON only when structured data is needed, explicit contracts, stage outputs, human review, deterministic local scripts, and selective context loading. Avoid unnecessary agents, frameworks, dashboards, databases, premature abstractions, decorative folders, giant context files, duplicated rules, and structural changes based only on aesthetics.

## Load Only Relevant Context
Start with this `SKILL.md`, then load only what the task needs:

- Design new workflows: read `references/icm-principles.md`, `references/five-layer-context.md`, `references/stage-contracts.md`, and `templates/workspace-template.md`.
- Audit existing workspaces: read `references/audit-checklist.md`, `references/anti-patterns.md`, then run `scripts/audit_tree.py` and `scripts/validate_icm.py` when possible.
- Debug failed stages or pipelines: read `references/stage-contracts.md`, `references/source-fidelity.md`, and `templates/debug-report-template.md`.
- Implement approved structural changes: read `templates/change-plan-template.md`, create a snapshot with `scripts/snapshot_structure.py`, and validate with `scripts/validate_icm.py`.
- Evaluate whether ICM fits: read `references/applicability-boundaries.md`.

Use `templates/` as reusable starting points, not as current decisions for the user's project. Selective file loading limits newly introduced context; it does not erase earlier messages or tool results already in the conversation. A folder or stage boundary does not itself reset the model's context.

## Modes
- `DISCOVER`: use when the real process is unclear. Inspect files, identify missing information, ask only blocking questions, map inputs, transformations, decisions, outputs, review points, and propose a minimum architecture. Do not implement before resolving architecture-changing unknowns.
- `DESIGN`: use to project a new structure. Deliver workflow map, stages, dependencies, layers, review gates, proposed tree, folder functions, required files, deliberately omitted items, risks, and limitations.
- `AUDIT`: use to analyze an existing structure. Inspect tree, context files, duplication, responsibilities, outputs, references, working artifacts, scripts, templates, skills, and current state. Classify each finding as critical, important, optional improvement, correct, or missing information, with evidence paths.
- `IMPLEMENT`: use to apply changes. Record current state, create a plan, separate reversible from destructive changes, ask approval for destructive changes, create a backup or use version control, execute, validate, and report exact changes.
- `DEBUG`: use when an output or pipeline fails. Investigate working artifact, stage contract, references loaded, instruction conflicts, previous output, missing context, excessive context, multi-responsibility stage, deterministic script candidates, and real model/tool limitations.
- `EVOLVE`: use to improve a system that already works. Expand only when there is evidence of repeated use, repeated human edits, duplicated instructions, script candidates, reusable components, templates, or skills.

If no mode is specified, infer it from the request and state the mode explicitly.

## Completeness Gate
Before creating or modifying architecture, confirm enough information to avoid distorting the workflow:

- workspace objective;
- final expected output;
- operator or user;
- execution frequency;
- inputs and outputs;
- real sequence of stages;
- human review points;
- indispensable human decisions;
- stable references;
- per-run working artifacts;
- tools and integrations;
- deterministic tasks;
- judgment-heavy tasks;
- quality and completion criteria;
- traceability and reuse needs;
- authority between files;
- technical limits;
- overwrite or loss risks.

Do not ask what can be confirmed from files. Ask only when the missing answer changes the current decision.

## Question Protocol
When information is needed, group questions in one concise round:

```md
## Necessary information

I need these answers because they change the architecture:

1. [Specific question]
   A. [Option]
   B. [Option]
   C. Other: [...]

   Why it matters:
   [How the answer changes stages, layers, outputs, or safety.]
```

After receiving answers, record confirmed decisions, update the plan, ask only what remains missing, and do not reopen decisions without new evidence.

## Source Fidelity
Always distinguish:

- Observed: directly verified in files, folders, code, documentation, user messages, logs, or outputs.
- Inferred: probable but not directly declared.
- Recommended: proposed by Canonic based on ICM principles.
- Unknown: not found or not confirmed.

Never turn a hypothesis into a fact, a probable preference into a confirmed preference, a draft into a current decision, an old output into a current rule, an example into a requirement, or a recommendation into a user order.

Before editing business, strategy, research, client context, or human decision files: identify content type, preserve originals, avoid semantic rewriting when reorganizing, keep names, numbers, dates, and claims intact, highlight ambiguities, record normalization, and show differences when meaning changes.

If two sources conflict, stop and show the conflict, involved files or messages, structural impact, authority question, and the change that is waiting for confirmation.

## Assumptions
Silent assumptions are forbidden.

If an assumption is non-critical and safe, write:

> Proposed assumption: [...]

Then explain why it is reasonable, what it affects, and how it can change later.

If an assumption could cause file loss, workflow distortion, wrong stages, mixed Layer 3/Layer 4 material, wrong automation, or unnecessary technical dependency, ask before proceeding.

## Five ICM Layers
The paths below are conventions used by this skill, not mandatory locations for every ICM workspace. Preserve the five roles, stage order, and explicit handoffs when a workspace uses different paths.

- Layer 0: global identity, usually `AGENTS.md` or `CLAUDE.md`. Answers "Where am I?"
- Layer 1: workspace routing, usually root `CONTEXT.md`. Answers "Where should I go?"
- Layer 2: stage contract, usually `stages/NN_name/CONTEXT.md`. Answers "What should I do now?"
- Layer 3: stable reference material, usually `references/`, `shared/`, `_config/`, `setup/`, `templates/`, or `skills/`. Answers "Which rules apply?"
- Layer 4: current working artifacts, usually `runs/`, `work/`, `inputs/`, `outputs/`, or stage output folders. Answers "What am I working with?"

Layer 3 and Layer 4 must not be treated as the same thing. A current artifact does not become a permanent rule without explicit human decision.

## Stage Contract
Each stage `CONTEXT.md` should define:

- Objective;
- Inputs with path, layer, function, required status, and relevant sections;
- Process;
- Outputs;
- Completion criteria;
- Boundaries;
- Human review.

Add `Verify`, `Failure conditions`, and `Notes for the agent` only when they add real robustness. Match review depth to the risk while preserving the human review points defined by the workspace; this does not authorize skipping them.

## Destructive-Change Safety
Never delete original sources, overwrite important files, move unknown files in bulk, alter sensitive configuration, expose credentials, include secrets in versioned files, modify dependencies, or execute destructive commands without explicit approval.

Before relevant refactors, check Git when available, create or recommend a checkpoint, produce a movement plan, list old and new paths, preserve history when possible, validate links and references after the change, and use backups when Git is unavailable.

Structural change does not authorize semantic change.

## Scripts
Use scripts for deterministic work instead of asking the model to reason through mechanical operations:

- `scripts/validate_icm.py <workspace>`: check conventional identity/routing files, required stage headings under `stages/`, common reference/artifact directory names, and structural warnings.
- `scripts/audit_tree.py <workspace>`: print a compact tree and lightweight structural notes.
- `scripts/snapshot_structure.py <workspace> --output <file>`: record a JSON inventory of paths, file sizes, and content hashes before implementation work. It does not copy file contents and cannot restore them; use Git or a separate backup for recovery.

The validator and tree audit assume the layout used by this skill's templates. For other layouts, assess the contracts and handoffs directly rather than treating a layout mismatch as an ICM defect. A validator pass does not establish input-file existence, output quality, source fidelity, correct separation of content layers, or readiness to execute; check the properties relevant to the task directly.

When Python is not on PATH inside Codex Desktop, use the bundled Python path from `load_workspace_dependencies`.

## Response Format
Adapt this structure to the task:

```md
# Canonic

## Mode
DISCOVER | DESIGN | AUDIT | IMPLEMENT | DEBUG | EVOLVE

## Objective

## Observed facts

## Inferences

## Missing information

## Questions

## Diagnosis

## Recommendation

## Change plan

## Changes applied

## Verification

## Remaining risks

## Next step
```

If there are blocking questions, do not fill `Changes applied`.

## Completion Criteria
Finish only when the task has preserved source fidelity, separated observed facts from inference and recommendation, used the minimum viable architecture, kept Layer 3 and Layer 4 separate, defined stage handoffs where stages exist, protected destructive changes behind approval, run deterministic validation where available, and reported residual risks.

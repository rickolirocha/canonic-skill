# Five-Layer Context

These layers describe context roles. The paths below are common conventions, not a required tree: numbered stage folders may, for example, sit directly at the workspace root instead of inside `stages/`. Keep the roles, sequence, and handoffs explicit without moving a working workspace merely to match this skill's templates.

## Layer 0 - Global Identity
Usually `AGENTS.md` or `CLAUDE.md`.

Answers: "Where am I?"

Should contain workspace identity, purpose, global rules, start protocol, and where to find specific context. It must not contain all project knowledge.

## Layer 1 - Workspace Routing
Usually root `CONTEXT.md`.

Answers: "Where should I go?"

Should list workflows, stage routing, shared resources, file authority, and navigation rules.

## Layer 2 - Stage Contract
Usually `stages/NN_name/CONTEXT.md`.

Answers: "What should I do now?"

Should define inputs, process, outputs, boundaries, completion criteria, verification when useful, references to load, and working artifacts to load.

## Layer 3 - Reference Material
Stable material reused across executions.

Examples: brand voice, design system, policies, approved examples, domain criteria, templates, conventions, and technical standards.

Common locations: `references/`, `shared/`, `_config/`, `setup/`, `templates/`, `skills/`.

## Layer 4 - Working Artifacts
Execution-specific material.

Examples: current brief, source file, transcript, current research, stage output, draft, run log, or reviewed artifact.

Common locations: `runs/`, `work/`, `inputs/`, `outputs/`, stage output folders.

## Critical Rule
Layer 3 and Layer 4 must not be mixed. Stable references are not current artifacts. Current artifacts are not permanent rules without explicit approval.

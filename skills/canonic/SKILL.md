---
name: canonic
description: Design, audit, debug, or improve how AI workspaces organize context, routing instructions, references, stage handoffs, and persistent project knowledge. Use for canonical workspaces, ICM, or requests to structure an agent's file-based context and workflow.
---

# canonic

Help people create and maintain a canonical workspace: an understandable, editable organization of the context and workflow an AI agent needs. It can be a small set of files or a larger staged system. Use the simplest structure that fits the actual task. ICM is one useful reference, not a mandatory layout or the only valid approach. Do not represent the work as endorsed by its authors or by any cited organization.

## When to apply

Apply when the task is to design, organize, audit, debug, or evolve an AI workspace's context architecture: its instruction and routing files, sources of truth, stable references, current artifacts, stage responsibilities, or handoffs. This includes requests for a canonical workspace or ICM even when the user does not name a particular methodology.

Do not turn ordinary use of project context, a simple file edit, or generic file organization into an architecture project. When only a narrow routing or context problem is requested, solve that problem without imposing a complete workspace redesign.

## Working principles

- Inspect the existing project and follow its conventions. Preserve working structures unless a specific change improves the requested outcome.
- Start with the objective, inputs, output, constraints, and decisions needed for the current task. Infer what the evidence supports; ask only when a missing answer changes a consequential decision.
- Route the agent to the smallest relevant context: clear entry points, unambiguous paths, and sources of truth. Do not assume that a file or stage boundary resets a model's conversation or context window.
- Distinguish stable instructions and references from current inputs, decisions, and outputs. Do not promote an old output, example, or inference into a permanent rule without human approval.
- Use Markdown and existing files where sufficient. Add folders, templates, scripts, agents, or dependencies only to solve an observed need. Parallel agents or other architectures may be appropriate for genuinely parallel or dynamic work.
- For workflows with multiple steps, make responsibilities, inputs, outputs, handoffs, completion criteria, and necessary human review clear. Use a formal stage contract only when it adds value.
- Preserve originals and meaning when reorganizing. Separate facts, inferences, and recommendations. Verify paths and important links after moving files; do not change unrelated content.
- Respect user authorization and applicable policy. Take a recoverable checkpoint where appropriate, and obtain approval before destructive or irreversible changes. A structural inventory is not a content backup.
- Validate relevant behavior and report material limitations. Scripts and model output are evidence to inspect, not proof of source fidelity or a finished workflow.

## Adapt to the task

- **Discover or design:** inspect the current state, identify the real process and proposed outputs, then make the smallest useful structure and handoffs explicit. A simple context router may be enough.
- **Audit:** compare the intended workflow with the actual files and instructions. Report consequential issues with evidence, their impact, and proportionate fixes; do not require a particular directory layout.
- **Debug:** trace the failure through the relevant input, instruction, source, working artifact, and handoff. Correct the cause rather than adding orchestration by default.
- **Implement or evolve:** make changes within the authorized scope, preserve user edits, use a recoverable checkpoint for risky work, and verify the affected flow. If crucial information is missing, continue independent work and ask only for the blocking decision.

Use the ICM five-layer model as an optional lens for separating identity, routing, stage instructions, stable references, and current artifacts. Preserve existing ICM contracts and review gates when the user is working with ICM; do not require all five layers, numbered stages, or `CONTEXT.md` files in every workspace. If the task needs real-time coordination, distributed state, or high concurrency, assess whether a different architecture fits better.

## Load only what is useful

The packaged references and templates are optional aids, not existing project decisions or universal requirements:

- Context design: `references/icm-principles.md`, `references/five-layer-context.md`, `references/stage-contracts.md`.
- Audit: `references/audit-checklist.md`, `references/anti-patterns.md`.
- Source fidelity: `references/source-fidelity.md`.
- Fit and limitations: `references/applicability-boundaries.md`.
- Examples: `templates/` contains ICM-oriented workspace, contract, audit, debug, and change-plan templates; adapt them to the task.

The local Python helpers are optional and assume the conventional ICM template layout:

- `scripts/audit_tree.py <workspace>` lists a compact tree and structural notes.
- `scripts/validate_icm.py <workspace>` checks conventional names and stage sections, not semantic correctness.
- `scripts/snapshot_structure.py <workspace> --output <file>` records names, sizes, and hashes, not file contents; it cannot restore files.

Use them when their assumptions and scope fit the workspace. Otherwise, inspect the relevant files directly. Do not classify a different layout as defective merely because an ICM-specific helper reports it as missing.

Respond in the user's language, with the findings, actions, checks, and material uncertainties that matter for the request. Do not force a fixed report format for every task.

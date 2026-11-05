# Stage Contracts

Each stage should have a `CONTEXT.md` file with a clear contract.

## Required Sections

```md
# Stage NN - Name

## Objective
Specific result of this stage.

## Inputs
Exact files to load. For each input, state path, layer, function, required or optional status, and relevant sections when the file is large.

## Process
The transformation this stage performs.

## Outputs
Files this stage must produce, including name, format, destination, and expected content.

## Completion criteria
Objective conditions for completion.

## Boundaries
What this stage must not do.

## Human review
What the human should review before the next stage.
```

## Useful Optional Sections
- `Verify`: consistency and quality checks.
- `Failure conditions`: when the stage must stop.
- `Notes for the agent`: operational details or exceptions.

## Contract Smells
- Inputs are described as "whatever is relevant".
- Outputs are not named.
- Stage writes only to chat.
- Stage both changes strategy and produces final delivery.
- Human approval is implied but not named.
- The contract points to a giant file without relevant sections.

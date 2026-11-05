# Stage Contracts

Use explicit contracts when a multi-stage workflow needs reliable handoffs or review. The user's existing conventions may define the contract in another file or format. A simple workflow need not create separate stage folders or contract files. For the conventional ICM template, each stage uses a `CONTEXT.md` file.

## Conventional ICM sections

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

## Signals to check in context
- Inputs are described as "whatever is relevant".
- Outputs are not named.
- A handoff exists only in chat even though the next stage requires durable state.
- A stage changes strategy outside its approved scope.
- A required human review is implied but not named.
- The contract points to a giant file without relevant sections.

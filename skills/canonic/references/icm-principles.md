# ICM Principles

These principles describe the ICM reference, especially file-first sequential workflows. Apply them when they fit the user's process; they are not mandatory for every canonical workspace.

## Primary Rule
Seek the simplest architecture that makes a workflow sequential, interpretable, verifiable, editable, and reusable.

## Prefer
- readable files;
- Markdown;
- JSON only when structured data is truly needed;
- clear folder responsibilities;
- sequential stages;
- explicit contracts;
- intermediate outputs;
- human review;
- local deterministic scripts;
- selective context loading.

## Avoid
- unnecessary agents;
- unnecessary frameworks;
- premature abstractions;
- dashboards without operational need;
- databases when files are enough;
- automation before the flow is understood;
- folders without real function;
- skills before repeated use is proven;
- giant context files;
- duplicated rules;
- structural changes made only for aesthetics.

## Stage Rule
One stage performs one primary transformation. A research stage should not silently produce the final deliverable. A planning stage should not alter source material. A rendering stage should not redefine strategy.

## Output Rule
Every important stage should write an explicit output that the next stage can inspect, edit, version, and consume.

## Human Review Rule
Important decisions need natural review points. The system should consume the reviewed output file, not hidden chat state.

## Deterministic Work Rule
Use scripts for mechanical operations such as validating structure, moving files, converting formats, generating indexes, detecting broken links, and comparing outputs.

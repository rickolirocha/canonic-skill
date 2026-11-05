#!/usr/bin/env python3
"""Validate a minimal folder-based ICM workspace."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_STAGE_SECTIONS = [
    "Objective",
    "Inputs",
    "Process",
    "Outputs",
    "Completion criteria",
    "Boundaries",
    "Human review",
]

SUSPICIOUS_DIR_NAMES = {"misc", "general", "other", "others", "geral", "outros", "temp"}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def has_heading(text: str, heading: str) -> bool:
    pattern = rf"^##\s+{re.escape(heading)}\s*$"
    return re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE) is not None


def section_text(text: str, heading: str) -> str:
    pattern = rf"^##\s+{re.escape(heading)}\s*$"
    match = re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    if not match:
        return ""
    next_heading = re.search(r"^##\s+", text[match.end():], flags=re.MULTILINE)
    if not next_heading:
        return text[match.end():]
    return text[match.end(): match.end() + next_heading.start()]


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def validate(root: Path) -> dict:
    root = root.resolve()
    errors: list[dict] = []
    warnings: list[dict] = []
    correct: list[dict] = []

    def add(kind: str, code: str, path: Path | None, message: str) -> None:
        item = {"code": code, "message": message}
        if path is not None:
            item["path"] = rel(path, root)
        if kind == "error":
            errors.append(item)
        elif kind == "warning":
            warnings.append(item)
        else:
            correct.append(item)

    if not root.exists() or not root.is_dir():
        return {
            "root": str(root),
            "status": "fail",
            "errors": [{"code": "ICM-ROOT-001", "message": "Root path does not exist or is not a directory."}],
            "warnings": [],
            "correct": [],
        }

    identity_files = [root / "AGENTS.md", root / "CLAUDE.md"]
    if any(path.is_file() for path in identity_files):
        add("correct", "ICM-L0-001", next(path for path in identity_files if path.is_file()), "Layer 0 identity file exists.")
    else:
        add("error", "ICM-L0-001", None, "Missing Layer 0 identity file: expected AGENTS.md or CLAUDE.md.")

    context = root / "CONTEXT.md"
    if context.is_file():
        add("correct", "ICM-L1-001", context, "Layer 1 routing file exists.")
    else:
        add("error", "ICM-L1-001", context, "Missing root CONTEXT.md.")

    stages_dir = root / "stages"
    if not stages_dir.is_dir():
        add("error", "ICM-STAGE-001", stages_dir, "Missing stages directory or path is not a directory.")
        stage_dirs: list[Path] = []
    else:
        stage_dirs = sorted(path for path in stages_dir.iterdir() if path.is_dir())
        if stage_dirs:
            add("correct", "ICM-STAGE-001", stages_dir, "Stages directory contains stage folders.")
        else:
            add("error", "ICM-STAGE-002", stages_dir, "Stages directory has no stage folders.")

    for stage in stage_dirs:
        if not re.match(r"^\d{2}[_-][a-z0-9][a-z0-9_-]*$", stage.name):
            add("warning", "ICM-STAGE-003", stage, "Stage folder should start with a two-digit order and a clear slug.")

        stage_context = stage / "CONTEXT.md"
        if not stage_context.is_file():
            add("error", "ICM-STAGE-004", stage_context, "Stage is missing CONTEXT.md.")
            continue

        text = read_text(stage_context)
        missing = [section for section in REQUIRED_STAGE_SECTIONS if not has_heading(text, section)]
        if missing:
            add("error", "ICM-STAGE-005", stage_context, "Stage CONTEXT.md is missing sections: " + ", ".join(missing) + ".")
        else:
            add("correct", "ICM-STAGE-005", stage_context, "Stage CONTEXT.md contains the required contract sections.")

        inputs = section_text(text, "Inputs")
        if "Layer:" not in inputs and "Layer 3" not in inputs and "Layer 4" not in inputs:
            add("warning", "ICM-LAYER-001", stage_context, "Inputs should label whether material is Layer 3 or Layer 4.")

    layer3_candidates = ["references", "shared", "_config", "templates", "skills"]
    if any((root / name).is_dir() for name in layer3_candidates):
        add("correct", "ICM-L3-001", root, "A Layer 3 reference location exists.")
    else:
        add("warning", "ICM-L3-001", root, "No common Layer 3 reference location found.")

    layer4_candidates = ["runs", "work", "inputs", "outputs"]
    if any((root / name).is_dir() for name in layer4_candidates):
        add("correct", "ICM-L4-001", root, "A Layer 4 working-artifact location exists.")
    else:
        add("warning", "ICM-L4-001", root, "No common Layer 4 working-artifact location found.")

    for path in root.rglob("*"):
        if path.is_dir() and path.name.lower() in SUSPICIOUS_DIR_NAMES:
            add("warning", "ICM-ANTI-001", path, "Suspicious generic folder name; verify this is not a permanent dump.")

    return {
        "root": str(root),
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "correct": correct,
    }


def print_text(result: dict) -> None:
    print(f"ICM validation: {result['status'].upper()}")
    print(f"Root: {result['root']}")
    for label in ("errors", "warnings", "correct"):
        items = result[label]
        print(f"\n{label.upper()} ({len(items)})")
        for item in items:
            path = f" [{item['path']}]" if "path" in item else ""
            print(f"- {item['code']}{path}: {item['message']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Workspace root to validate.")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)

    result = validate(args.root)
    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_text(result)
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

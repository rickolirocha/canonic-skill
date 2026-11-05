#!/usr/bin/env python3
"""Print a compact tree audit for an ICM-style workspace."""

from __future__ import annotations

import argparse
import os
from pathlib import Path


SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules"}
SUSPICIOUS = {"misc", "general", "other", "others", "geral", "outros", "temp"}


def iter_tree(root: Path, max_depth: int) -> list[str]:
    root = root.resolve()
    lines = [root.name + "/"]

    def walk(path: Path, prefix: str, depth: int) -> None:
        if depth >= max_depth:
            return
        children = sorted(
            [child for child in path.iterdir() if child.name not in SKIP_DIRS],
            key=lambda child: (not child.is_dir(), child.name.lower()),
        )
        for index, child in enumerate(children):
            connector = "`-- " if index == len(children) - 1 else "|-- "
            suffix = "/" if child.is_dir() else ""
            lines.append(prefix + connector + child.name + suffix)
            if child.is_dir():
                next_prefix = prefix + ("    " if index == len(children) - 1 else "|   ")
                walk(child, next_prefix, depth + 1)

    walk(root, "", 0)
    return lines


def analyze(root: Path) -> list[str]:
    notes: list[str] = []
    if not (root / "AGENTS.md").is_file() and not (root / "CLAUDE.md").is_file():
        notes.append("Missing Layer 0 identity file: AGENTS.md or CLAUDE.md.")
    if not (root / "CONTEXT.md").is_file():
        notes.append("Missing Layer 1 routing file: CONTEXT.md.")
    if not (root / "stages").is_dir():
        notes.append("Missing stages directory.")

    for directory, names, _ in os.walk(root, followlinks=False):
        names[:] = sorted(name for name in names if name not in SKIP_DIRS)
        for name in names:
            path = Path(directory) / name
            if name.lower() in SUSPICIOUS:
                notes.append(f"Suspicious generic folder: {path.relative_to(root).as_posix()}")

    stage_dir = root / "stages"
    if stage_dir.is_dir():
        for stage in sorted(path for path in stage_dir.iterdir() if path.is_dir()):
            if not (stage / "CONTEXT.md").is_file():
                notes.append(f"Stage missing CONTEXT.md: {stage.relative_to(root).as_posix()}")
    return notes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--max-depth", type=int, default=4)
    args = parser.parse_args()

    root = args.root.resolve()
    print("Tree")
    print("====")
    print("\n".join(iter_tree(root, args.max_depth)))
    print("\nAudit notes")
    print("===========")
    notes = analyze(root)
    if notes:
        for note in notes:
            print(f"- {note}")
    else:
        print("- No structural notes from the lightweight tree audit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

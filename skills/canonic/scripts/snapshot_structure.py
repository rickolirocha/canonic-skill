#!/usr/bin/env python3
"""Create a deterministic JSON snapshot of a folder structure."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def snapshot(root: Path) -> dict:
    root = root.resolve()
    entries = []
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        relative = path.relative_to(root).as_posix()
        if path.is_dir():
            entries.append({"path": relative, "type": "dir"})
        else:
            entries.append({
                "path": relative,
                "type": "file",
                "size": path.stat().st_size,
                "sha256": sha256(path),
            })
    return {
        "root": str(root),
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "entries": entries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--output", type=Path, help="Write snapshot JSON to this path.")
    args = parser.parse_args()

    data = snapshot(args.root)
    text = json.dumps(data, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
        print(f"Wrote snapshot: {args.output}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

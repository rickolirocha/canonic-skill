from __future__ import annotations

import subprocess
import sys
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_icm.py"
FIXTURES = ROOT / "tests" / "fixtures"


class ValidateIcmTests(unittest.TestCase):
    def run_validator(self, fixture: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(FIXTURES / fixture), "--format", "json"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_broken_workspace_fails(self) -> None:
        result = self.run_validator("broken_workspace")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('"status": "fail"', result.stdout)
        self.assertIn("ICM-STAGE-005", result.stdout)
        self.assertIn("Outputs", result.stdout)

    def test_fixed_workspace_passes(self) -> None:
        result = self.run_validator("fixed_workspace")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('"status": "pass"', result.stdout)

    def test_stage_path_is_a_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "stages").write_text("not a directory", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(root), "--format", "json"],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(result.returncode, 1, result.stderr)
            report = json.loads(result.stdout)
            self.assertTrue(any(item["code"] == "ICM-STAGE-001" for item in report["errors"]))
            audit = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "audit_tree.py"), str(root)],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(audit.returncode, 0, audit.stderr)
            self.assertIn("Missing stages directory", audit.stdout)

    def test_directories_do_not_count_as_context_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "AGENTS.md").mkdir()
            (root / "CONTEXT.md").mkdir()
            stage = root / "stages" / "01_discover"
            stage.mkdir(parents=True)
            (stage / "CONTEXT.md").mkdir()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(root), "--format", "json"],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(result.returncode, 1, result.stderr)
            codes = {item["code"] for item in json.loads(result.stdout)["errors"]}
            self.assertTrue({"ICM-L0-001", "ICM-L1-001", "ICM-STAGE-004"}.issubset(codes))


if __name__ == "__main__":
    unittest.main()

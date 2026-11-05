from __future__ import annotations

import subprocess
import sys
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


if __name__ == "__main__":
    unittest.main()

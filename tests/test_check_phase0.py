import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "check_phase0", Path("scripts/check_phase0.py")
)
check_phase0 = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(check_phase0)


class CheckPhase0Tests(unittest.TestCase):
    def test_check_list_uses_current_python_and_expected_steps(self):
        steps = check_phase0.checks()
        self.assertEqual(len(steps), 4)
        for _, command in steps:
            self.assertEqual(command[0], sys.executable)

        self.assertIn("scripts/validate_phase0.py", steps[0][1])
        self.assertIn("scripts/validate_evidence_manifest.py", steps[1][1])
        self.assertIn("scripts/source_snapshot_manifest.py", steps[2][1])
        self.assertIn("unittest", steps[3][1])

    def test_fail_fast_returns_first_failure_code(self):
        calls = []

        def fake_runner(command, check=False):
            calls.append(command)
            code = 7 if len(calls) == 2 else 0
            return subprocess.CompletedProcess(command, code)

        result = check_phase0.run_checks(fake_runner)
        self.assertEqual(result, 7)
        self.assertEqual(len(calls), 2)

    def test_success_runs_all_steps(self):
        calls = []

        def fake_runner(command, check=False):
            calls.append(command)
            return subprocess.CompletedProcess(command, 0)

        result = check_phase0.run_checks(fake_runner)
        self.assertEqual(result, 0)
        self.assertEqual(len(calls), 4)


if __name__ == "__main__":
    unittest.main()

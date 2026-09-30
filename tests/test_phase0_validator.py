import importlib.util
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "validate_phase0", Path("scripts/validate_phase0.py")
)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


class TierValidationTests(unittest.TestCase):
    def setUp(self):
        self.path = Path("synthetic-rule.json")

    def test_contiguous_increasing_credit_tiers_are_valid(self):
        validator.validate_tiers(
            [
                {"uptime_lt": "99.5", "uptime_gte": "99.0", "credit_percent": 10},
                {"uptime_lt": "99.0", "uptime_gte": "95.0", "credit_percent": 30},
                {"uptime_lt": "95.0", "credit_percent": 100},
            ],
            "tiers",
            self.path,
        )

    def test_gap_or_overlap_is_rejected(self):
        with self.assertRaises(SystemExit):
            validator.validate_tiers(
                [
                    {"uptime_lt": "99.5", "uptime_gte": "99.0", "credit_percent": 10},
                    {"uptime_lt": "98.9", "uptime_gte": "95.0", "credit_percent": 30},
                    {"uptime_lt": "95.0", "credit_percent": 100},
                ],
                "tiers",
                self.path,
            )

    def test_credit_percent_above_100_is_rejected(self):
        with self.assertRaises(SystemExit):
            validator.validate_tiers(
                [{"uptime_lt": "99.5", "credit_percent": 101}],
                "tiers",
                self.path,
            )

    def test_credit_percent_must_increase_as_uptime_decreases(self):
        with self.assertRaises(SystemExit):
            validator.validate_tiers(
                [
                    {"uptime_lt": "99.5", "uptime_gte": "99.0", "credit_percent": 30},
                    {"uptime_lt": "99.0", "credit_percent": 10},
                ],
                "tiers",
                self.path,
            )


class IdentityValidationTests(unittest.TestCase):
    def setUp(self):
        self.path = Path("synthetic-rule.json")

    def test_duplicate_family_ids_are_rejected(self):
        with self.assertRaises(SystemExit):
            validator.unique_ids(
                [{"family_id": "same"}, {"family_id": "same"}],
                "family_id",
                "families",
                self.path,
            )


if __name__ == "__main__":
    unittest.main()

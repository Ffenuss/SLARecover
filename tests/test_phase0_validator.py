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


class RepositoryHygieneTests(unittest.TestCase):
    def test_safe_documentation_mentions_do_not_trigger(self):
        self.assertEqual(
            validator.secret_findings(
                "Never commit AWS access key IDs or private keys. "
                "Use AWS_SECRET_ACCESS_KEY=<placeholder> only in local examples."
            ),
            [],
        )

    def test_plausible_aws_access_key_id_is_detected(self):
        synthetic = "AKIA" + ("A" * 16)
        self.assertIn("AWS access key ID", validator.secret_findings(synthetic))

    def test_private_key_header_is_detected(self):
        synthetic = "-----BEGIN " + "PRIVATE KEY-----"
        self.assertIn("private key block", validator.secret_findings(synthetic))

    def test_secret_assignment_is_detected(self):
        synthetic = "AWS_SECRET_ACCESS_KEY=" + ("a" * 40)
        self.assertIn(
            "AWS secret access key assignment",
            validator.secret_findings(synthetic),
        )

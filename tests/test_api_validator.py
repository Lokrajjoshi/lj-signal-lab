import unittest

from api_validator import validate_response


class ApiValidatorTests(unittest.TestCase):
    def test_reports_missing_required_key(self):
        signals = validate_response({"status": "ok"}, required={"id"})
        self.assertEqual(signals[0]["rule"], "required")
        self.assertEqual(signals[0]["path"], "id")

    def test_reports_invalid_status(self):
        signals = validate_response(
            {"status": "queued"},
            allowed_statuses={"ok", "failed"},
        )
        self.assertEqual(signals[0]["rule"], "allowed_values")
        self.assertEqual(signals[0]["path"], "status")

    def test_accepts_valid_payload(self):
        self.assertEqual(
            validate_response(
                {"id": "P-1", "status": "ok"},
                required={"id"},
                allowed_statuses={"ok", "failed"},
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()

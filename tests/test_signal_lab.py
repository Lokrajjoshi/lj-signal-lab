import unittest
from signal_lab import inspect_rows


class SignalLabTests(unittest.TestCase):
    def test_reports_missing_cells_and_statuses(self):
        report = inspect_rows([
            {"project_id": "P-1", "status": "Done"},
            {"project_id": "P-2", "status": ""},
        ])
        self.assertEqual(report["missing_cells"], 1)
        self.assertEqual(report["status_counts"], {"Done": 1, "UNKNOWN": 1})

    def test_detects_duplicate_rows(self):
        row = {"project_id": "P-1", "status": "Done"}
        report = inspect_rows([row, row.copy()])
        self.assertEqual(report["duplicate_rows"], 1)


if __name__ == "__main__":
    unittest.main()

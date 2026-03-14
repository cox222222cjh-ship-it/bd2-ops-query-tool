from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from query_item import build_default_report_path


class QueryItemFilenameSafetyTest(unittest.TestCase):
    def test_default_report_path_stays_inside_reports(self) -> None:
        report_path = build_default_report_path("../../etc/passwd")
        reports_dir = Path("outputs/reports").resolve()
        self.assertEqual(report_path.resolve().parent, reports_dir)


if __name__ == "__main__":
    unittest.main()

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

    def test_mixed_keywords_do_not_collide(self) -> None:
        keywords = [
            "A",
            "任务A",
            "A任务",
            "生命25%恢复药水",
            "破旧的最强的双手剑(制作)",
        ]
        names = [build_default_report_path(k).name for k in keywords]
        self.assertEqual(len(set(names)), len(names))

    def test_lossy_namespace_does_not_collide_with_safe_ascii(self) -> None:
        lossy = build_default_report_path("任务A").name
        safe = build_default_report_path("A_ad728752").name
        self.assertNotEqual(lossy, safe)

    def test_reserved_tilde_namespace_does_not_collide_with_safe_ascii(self) -> None:
        lossy = build_default_report_path("!!!").name
        safe = build_default_report_path("~query_9a7b006d").name
        self.assertNotEqual(lossy, safe)

    def test_unicode_keywords_do_not_collapse_to_same_filename(self) -> None:
        path1 = build_default_report_path("测试物品")
        path2 = build_default_report_path("任务")
        self.assertNotEqual(path1.name, path2.name)


if __name__ == "__main__":
    unittest.main()

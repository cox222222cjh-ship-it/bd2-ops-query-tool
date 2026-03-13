from __future__ import annotations

from pathlib import Path
from typing import Any

import click
import yaml

from common import OUTPUTS_DIR, read_json, write_json

DOMAINS = ["item", "task", "gift", "enhance", "drop", "shop", "npc", "map", "activity"]


def score_table(table: str, fields: list[str], hints: dict[str, Any]) -> tuple[float, list[str]]:
    evidence: list[str] = []
    score = 0.0
    low_table = table.lower()

    for keyword in hints.get("table_keywords", []):
        if keyword.lower() in low_table:
            score += 0.5
            evidence.append(f"table_keyword:{keyword}")

    for field in fields:
        low_field = field.lower()
        for keyword in hints.get("field_keywords", []):
            if keyword.lower() in low_field:
                score += 0.2
                evidence.append(f"field_keyword:{keyword}")

    return min(score, 1.0), evidence


@click.command()
@click.option("--indexes-dir", default="outputs/intermediate", show_default=True)
@click.option("--rules-file", default="rules/domain_hints.yaml", show_default=True)
def main(indexes_dir: str, rules_file: str) -> None:
    field_index = read_json(Path(indexes_dir) / "field_index.json", default=[])
    hints = yaml.safe_load(Path(rules_file).read_text(encoding="utf-8"))

    fields_by_table: dict[str, list[str]] = {}
    for row in field_index:
        fields_by_table.setdefault(row["table"], []).append(row["field"])

    domain_candidates: list[dict[str, Any]] = []
    unknown_fields: list[dict[str, Any]] = []

    for table, fields in fields_by_table.items():
        matched_any = False
        for domain, domain_hints in hints.items():
            confidence, evidence = score_table(table, fields, domain_hints)
            if confidence >= 0.3:
                matched_any = True
                domain_candidates.append(
                    {
                        "table": table,
                        "domain": domain,
                        "confidence": round(confidence, 2),
                        "status": "待确认",
                        "evidence": evidence,
                    }
                )
        if not matched_any:
            unknown_fields.append({"table": table, "status": "待确认", "reason": "no_domain_hint_match"})

    write_json(OUTPUTS_DIR / "intermediate" / "domain_candidates.json", domain_candidates)

    domain_md = OUTPUTS_DIR / "reports" / "domain_candidates_report.md"
    lines = ["# 业务域候选归类", "", "| 表 | 候选域 | 置信度 | 状态 | 证据 |", "|---|---|---:|---|---|"]
    for row in sorted(domain_candidates, key=lambda x: x["confidence"], reverse=True):
        lines.append(
            f"| {row['table']} | {row['domain']} | {row['confidence']} | {row['status']} | {', '.join(row['evidence'][:3])} |"
        )
    if len(lines) == 4:
        lines.append("| - | - | 0 | 待确认 | 未命中规则 |")
    domain_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    unknown_md = OUTPUTS_DIR / "reports" / "unknown_fields_report.md"
    unknown_lines = ["# 待确认字段 / 表", ""]
    for row in unknown_fields:
        unknown_lines.append(f"- `{row['table']}`: {row['reason']}（{row['status']}）")
    if len(unknown_lines) == 2:
        unknown_lines.append("- 当前所有表都至少匹配了一个候选域。")
    unknown_md.write_text("\n".join(unknown_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

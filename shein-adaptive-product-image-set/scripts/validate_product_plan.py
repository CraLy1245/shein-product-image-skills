#!/usr/bin/env python3
"""Validate a generated SHEIN adaptive product image plan against key v1.3.4 rules."""
from __future__ import annotations
import re
import sys
from collections import defaultdict
from pathlib import Path

FORBIDDEN_PLAN_PHRASES = [
    "same background tone",
]

VISUAL_TASK_FIELD_PATTERNS = [
    r"main\s+visual\s+evidence\s+type",
    r"main\s+visual\s+evidence",
    r"visual\s+task",
]

SECONDARY_TASK_FIELD_PATTERNS = [
    r"purchase\s+question\s+answered",
]

PLACEHOLDER_RE = re.compile(r"^\[.*\]$|^n/?a$|^none$|^-$", re.I)


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def warn(msg: str) -> None:
    print(f"WARN: {msg}")


def normalize(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\[[^\]]*\]", " ", value)
    value = value.lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def is_meaningful(value: str) -> bool:
    raw = value.strip()
    if not raw or PLACEHOLDER_RE.match(raw):
        return False
    return len(normalize(raw)) >= 4


def split_md_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c.strip()) for c in cells if c.strip())


def header_matches(header: str, patterns: list[str]) -> bool:
    h = normalize(header)
    return any(re.search(p, h, re.I) for p in patterns)


def extract_table_values(text: str, patterns: list[str]) -> list[tuple[str, str, str]]:
    values: list[tuple[str, str, str]] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines) - 1:
        if "|" not in lines[i] or "|" not in lines[i + 1]:
            i += 1
            continue
        headers = split_md_row(lines[i])
        sep = split_md_row(lines[i + 1])
        if not is_separator_row(sep):
            i += 1
            continue
        task_cols = [idx for idx, h in enumerate(headers) if header_matches(h, patterns)]
        image_col = next((idx for idx, h in enumerate(headers) if re.search(r"\bimage\b|编号|图片", normalize(h), re.I)), None)
        if task_cols:
            j = i + 2
            while j < len(lines) and "|" in lines[j]:
                cells = split_md_row(lines[j])
                if len(cells) < 2:
                    break
                image_id = cells[image_col] if image_col is not None and image_col < len(cells) else f"row {j+1}"
                for col in task_cols:
                    if col < len(cells) and is_meaningful(cells[col]):
                        values.append((image_id, headers[col], cells[col]))
                j += 1
            i = j
        else:
            i += 1
    return values


def extract_labeled_values(text: str, patterns: list[str]) -> list[tuple[str, str, str]]:
    values: list[tuple[str, str, str]] = []
    current_image = "unknown image"
    image_re = re.compile(r"\bIMAGE\s*0?(\d{1,2})\b", re.I)
    for line in text.splitlines():
        m_img = image_re.search(line)
        if m_img:
            current_image = f"IMAGE {int(m_img.group(1))}"
        for pat in patterns:
            m = re.match(rf"\s*({pat})\s*[:：-]\s*(.+?)\s*$", line, re.I)
            if m and is_meaningful(m.group(2)):
                values.append((current_image, m.group(1), m.group(2)))
    return values


def check_duplicate_values(values: list[tuple[str, str, str]], label: str, strict: bool = True) -> None:
    by_norm: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for image_id, field, value in values:
        norm = normalize(value)
        if norm:
            by_norm[norm].append((image_id, field, value))
    duplicates = {k: v for k, v in by_norm.items() if len(v) > 1}
    if duplicates:
        lines = []
        for _norm, entries in duplicates.items():
            rendered = "; ".join(f"{img} `{field}` = {value}" for img, field, value in entries)
            lines.append(rendered)
        msg = f"duplicate {label} values found; each selected image needs a distinct visual task:\n" + "\n".join(lines)
        if strict:
            fail(msg)
        warn(msg)


def main() -> None:
    if len(sys.argv) < 2:
        fail("usage: validate_product_plan.py path/to/output.md")
    p = Path(sys.argv[1])
    if not p.exists():
        fail(f"file does not exist: {p}")
    text = p.read_text(encoding="utf-8")
    lower = text.lower()

    for phrase in FORBIDDEN_PLAN_PHRASES:
        if phrase in lower:
            fail(f"forbidden homogenizing wording found: `{phrase}`")

    nums = [int(x) for x in re.findall(r"\bIMAGE\s*0?(\d{1,2})\b", text, re.I)]
    if not nums:
        nums = [int(x) for x in re.findall(r"\|\s*0?(\d{1,2})\s*\|", text)]
    if nums:
        max_n = max(nums)
        if max_n > 11:
            fail(f"image count exceeds 11: {max_n}")
        expected = list(range(1, max_n + 1))
        present = sorted(set(n for n in nums if 1 <= n <= max_n))
        missing = [n for n in expected if n not in present]
        if missing:
            fail(f"missing image numbers: {missing}")

    required_terms = [
        "z-001",
        "size",
        "dimension",
        "visual anchor",
        "visual variation",
        "imagegen prompt",
        "preflight",
        "negative",
        "consistency checklist",
    ]
    missing_terms = [t for t in required_terms if t not in lower]
    if missing_terms:
        fail("missing required concepts: " + ", ".join(missing_terms))

    primary_values = extract_table_values(text, VISUAL_TASK_FIELD_PATTERNS)
    primary_values += extract_labeled_values(text, VISUAL_TASK_FIELD_PATTERNS)
    if nums and max(nums) > 1 and len(primary_values) < max(nums):
        fail("missing Main Visual Evidence Type / Visual Task values for one or more images")
    check_duplicate_values(primary_values, "Main Visual Evidence Type / Visual Task", strict=True)

    secondary_values = extract_table_values(text, SECONDARY_TASK_FIELD_PATTERNS)
    secondary_values += extract_labeled_values(text, SECONDARY_TASK_FIELD_PATTERNS)
    check_duplicate_values(secondary_values, "Purchase Question Answered", strict=False)

    if "sku image" in lower and "excluded" not in lower and "explicitly requested" not in lower:
        warn("SKU image is mentioned without an exclusion/explicit-request note")
    print("PASS: product image plan satisfies key adaptive skill checks")

if __name__ == "__main__":
    main()

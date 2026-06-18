#!/usr/bin/env python3
"""Validate basic OpenAI Codex skill directory structure plus v1.3.4 visual-rule guardrails."""
from __future__ import annotations
import re
import sys
from pathlib import Path

REQUIRED_REFS = [
    "01-workflow-and-hard-rules.md",
    "02-visual-system-and-style.md",
    "03-module-selection-rules.md",
    "04-imagegen-production-rules.md",
    "05-output-and-compliance-checklists.md",
]

# Phrases that caused over-homogenized image sets in earlier outputs.
# Keep this list focused on high-risk wording, not on legitimate style-unification language.
FORBIDDEN_DOC_PHRASES = [
    "same background tone",
]

TEXT_EXTENSIONS = {".md", ".yaml", ".yml"}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def scan_forbidden_phrases(root: Path) -> None:
    hits: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for phrase in FORBIDDEN_DOC_PHRASES:
            if phrase.lower() in text:
                hits.append(f"{rel}: contains forbidden phrase {phrase!r}")
    if hits:
        fail("Forbidden wording found:\n" + "\n".join(hits))


def require_contains(path: Path, patterns: list[str], label: str) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    missing = []
    for pattern in patterns:
        if not re.search(pattern, text, flags=re.I):
            missing.append(pattern)
    if missing:
        fail(f"{label} missing required patterns: {missing}")


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    skill = root / "SKILL.md"
    refs = root / "references"
    assets = root / "assets"
    scripts = root / "scripts"

    if not skill.exists():
        fail("SKILL.md not found")
    if not refs.is_dir():
        fail("references directory not found")
    if not assets.is_dir():
        fail("assets directory not found")
    if not scripts.is_dir():
        fail("scripts directory not found")

    text = skill.read_text(encoding="utf-8", errors="ignore")

    required_skill_patterns = [
        r"name:\s*shein-adaptive-product-image-set",
        r"version:\s*1\.3\.4",
        r"Z-001",
        r"maximum\s+of\s+11|maximum\s+11|max\s+11",
        r"size/dimension|size\s*/\s*dimension",
        r"SKU image.*excluded|exclude SKU",
        r"Visual Anchor",
        r"Visual Variation Role",
        r"one imagegen prompt per",
        r"one image at a time",
        r"6\s*-?minute|6 minutes",
        r"one retry|maximum.*one retry|at most one retry",
        r"duplicate retry|duplicate prompts|identical prompts",
    ]
    for pat in required_skill_patterns:
        if not re.search(pat, text, flags=re.I | re.S):
            fail(f"SKILL.md missing expected rule pattern: {pat}")

    for ref in REQUIRED_REFS:
        if not (refs / ref).exists():
            fail(f"missing reference file: {ref}")

    require_contains(
        refs / "02-visual-system-and-style.md",
        [
            r"Visual Anchor",
            r"Visual Variation",
            r"not the same exact background",
            r"different purchase question|purchase question",
        ],
        "02 visual system rules",
    )

    require_contains(
        refs / "04-imagegen-production-rules.md",
        [
            r"6\s*-?minute|6 minutes",
            r"pending_empty_poll",
            r"explicit_error",
            r"active_termination",
            r"one retry|maximum attempts",
            r"Duplicate Submission Ban",
            r"Continue-On-Failure",
            r"Large Batch Guidance",
        ],
        "04 ImageGen production rules",
    )

    require_contains(
        assets / "templates" / "imagegen-execution.md",
        [
            r"ImageGen Call Record",
            r"Status Classification",
            r"pending_empty_poll",
            r"Retry Used",
            r"skipped_after_retry_limit",
        ],
        "imagegen execution template",
    )

    if not (scripts / "validate_product_plan.py").exists():
        fail("validate_product_plan.py not found")

    scan_forbidden_phrases(root)

    print("PASS: skill structure, visual wording, and ImageGen wait/retry guardrails are compatible")


if __name__ == "__main__":
    main()

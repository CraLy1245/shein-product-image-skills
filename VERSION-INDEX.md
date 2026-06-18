# Skill Version Index

## Current mainline

- Version: `1.3.4`
- Folder: `shein-adaptive-product-image-set/`
- Entry file: `shein-adaptive-product-image-set/SKILL.md`
- Main update: ImageGen long-tail latency, wait, termination, retry, and execution logging guardrails.

## Important files

- `shein-adaptive-product-image-set/SKILL.md`
- `shein-adaptive-product-image-set/references/04-imagegen-production-rules.md`
- `shein-adaptive-product-image-set/assets/templates/imagegen-execution.md`
- `shein-adaptive-product-image-set/scripts/validate_skill.py`
- `shein-adaptive-product-image-set/scripts/validate_product_plan.py`

## v1.3.4 behavior

- Adaptive image count, maximum 11.
- Z-001 required for Image 1.
- Size / Dimension Image required.
- SKU image excluded by default.
- Shared Visual Anchor and per-image Visual Variation Role.
- One ImageGen prompt per selected image.
- One image generated at a time.
- Minimum 6-minute ImageGen wait before considering a request stalled.
- One retry maximum per image.
- Duplicate prompt retry loops prohibited.
- Failed image can be logged and skipped so the remaining set continues.

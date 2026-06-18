# SHEIN Product Image Skills

This repository stores two versioned OpenAI Codex skills for SHEIN-style e-commerce product image workflows.

## Included skills

| Branch | Version | ImageGen | Purpose |
|---|---:|---|---|
| `mainline-imagegen` | `v1.3.3` | Yes | Product analysis, image-set planning, prompt writing, and one-by-one Codex imagegen generation when requested. |
| `planpack-no-imagegen` | `v1.3.3-planpack.1` | No | Product analysis and per-image planning packs only. It prepares folders, prompts, notes, and checklists without calling imagegen. |

## Version rule

- Mainline ImageGen versions use normal semantic versions, for example `1.3.3`, `1.3.4`, `1.4.0`.
- PlanPack branch versions append `-planpack.N`, for example `1.3.3-planpack.1`.

## Repository structure

```text
mainline-imagegen/
planpack-no-imagegen/
docs/
releases/
SKILL-VERSION-INDEX-20260618.md
```

## Current canonical versions

- Mainline: `shein-adaptive-product-image-set` `v1.3.3`
- PlanPack: `shein-adaptive-product-image-set-planpack` `v1.3.3-planpack.1`

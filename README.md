# SHEIN Product Image Skills

This repository stores JiaZ's SHEIN-style e-commerce product image skills for OpenAI Codex workflows.

## Current mainline

- Skill folder: `shein-adaptive-product-image-set/`
- Current version: `1.3.4`
- Main purpose: adaptive SHEIN product image set planning and ImageGen prompt production.

## v1.3.4 Update

This version adds ImageGen long-tail latency and retry guardrails:

- Minimum 6-minute wait before treating a request as stalled.
- Empty polling / no intermediate progress is not a failure.
- Explicit error required before retry, unless a request is actively terminated after the wait threshold.
- Maximum one retry per image.
- No repeated identical submissions while a previous request is pending.
- Failed image is logged and skipped after retry limit, so the full set can continue.

## Install

Copy the `shein-adaptive-product-image-set` folder into the Codex skills directory or import it through Codex skill upload if available.

The skill entry point is:

```text
shein-adaptive-product-image-set/SKILL.md
```

## Safety note

Third-party skills should always be inspected before execution. Review `SKILL.md`, `references/`, and `scripts/` before using any skill in Codex.

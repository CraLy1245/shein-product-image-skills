# Release v1.3.4 Mainline

## Summary

This release updates the SHEIN Adaptive Product Image Set Skill with ImageGen long-tail latency and retry guardrails.

## Key changes

- Minimum 6-minute wait before considering one ImageGen request stalled.
- Empty poll / quiet wait is not failure.
- Retry only after explicit error, controlled post-threshold active termination, or completed-image review failure.
- One retry maximum per image.
- Duplicate identical prompt submissions are prohibited.
- Failed images are logged and skipped after retry limit so the remaining set can continue.
- Execution logging now records status classification, elapsed duration, retry usage, active termination, and final action.

## Entry point

```text
SKILL.md
```

## Validation

```bash
python scripts/validate_skill.py .
```

# README ImageGen

For v1.3.4, ImageGen execution must follow the wait/retry policy in:

```text
references/04-imagegen-production-rules.md
assets/templates/imagegen-execution.md
```

Key rule:

```text
Long quiet wait is not failure. Wait at least 6 minutes before considering one request stalled.
```

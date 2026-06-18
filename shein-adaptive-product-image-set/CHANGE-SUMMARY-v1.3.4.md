# Change Summary v1.3.4

v1.3.4 fixes the Codex ImageGen execution strategy for SHEIN product image generation.

The issue was not a fixed Codex timeout. The problem was premature active termination and repeated duplicate retries during long-tail ImageGen waits.

This version adds:

- Long-tail latency awareness
- 6-minute minimum wait
- Pending/empty poll classification
- Explicit failure criteria
- One retry maximum
- Duplicate prompt submission ban
- Continue-on-failure behavior
- Execution log fields
- Large batch API/async guidance

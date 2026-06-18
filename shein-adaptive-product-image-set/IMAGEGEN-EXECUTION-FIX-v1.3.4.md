# ImageGen Execution Fix v1.3.4

## Root cause addressed

ImageGen may have long-tail latency. During a long quiet wait, an execution agent can mistake the pending request for a stalled process, actively terminate it, and then resubmit the same prompt. This creates a terminate / retry / wait loop.

## Policy added

- Quiet wait is not failure.
- Empty polling is not failure.
- A single ImageGen request must wait at least 6 minutes before being considered stalled.
- Retry only after explicit error, active termination after wait threshold, or completed-image quality failure.
- Maximum one retry per image.
- Do not submit duplicate identical prompts while the prior request is pending.
- If one image fails after retry limit, log it and continue the remaining image set.

# ImageGen Guardrails

This is the v1.3.4 execution fix.

## Do

- Wait at least 6 minutes before treating a request as stalled.
- Classify empty polling as `pending_empty_poll`.
- Retry only after explicit error, controlled active termination, or completed-image review failure.
- Limit each image to original request plus one retry.
- Log status, elapsed time, retry usage, and final action.
- Continue to the remaining images after retry limit.

## Do not

- Do not treat quiet waiting as failure.
- Do not treat a 60-second poll interval as ImageGen timeout.
- Do not submit duplicate identical prompts while a previous request is pending.
- Do not run three or four attempts for the same image.
- Do not block the full set because one image failed.

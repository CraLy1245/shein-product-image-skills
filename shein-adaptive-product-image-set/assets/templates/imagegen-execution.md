# ImageGen Execution Template

Use this file when the skill is expected to call Codex imagegen directly.

## Execution Order

1. Finish product analysis.
2. Select image modules.
3. Create the planning table.
4. Define the shared Visual Anchor and Image Style Distribution.
5. Write exact English copy.
6. Write one imagegen prompt per selected image that inherits the same Visual Anchor.
7. Run prompt preflight checks.
8. Call imagegen one image at a time.
9. For each request, wait according to the 6-minute minimum wait rule before considering it stalled.
10. Review each completed image against the Visual Anchor and product reference.
11. Regenerate only failed images within the one-retry-per-image limit.
12. If an image still fails after the retry limit, record it and continue to the next image unless the user asks to stop.

## ImageGen Call Record

For each generated image attempt, record:

- Image Number:
- Module Name:
- Attempt Number:
- Prompt Version / Prompt Identity:
- Reference Images Used:
- Start Time:
- Last Poll Time:
- End Time:
- Elapsed Duration:
- Status Classification:
  - pending_empty_poll
  - completed
  - explicit_error
  - active_termination
  - completed_but_failed_review
  - skipped_after_retry_limit
- Active Termination Used: Yes / No
- Error Type If Any:
  - timeout
  - rate_limit
  - server_error
  - deadline_exceeded
  - content_error
  - unknown
  - none
- Retry Used: Yes / No
- Final Action:
  - accepted
  - retried
  - skipped_and_continue
  - user_review_needed

## Wait / Retry Rules

1. A quiet ImageGen request is not a failure.
2. An empty polling response is not a failure.
3. Lack of intermediate progress is not a failure.
4. Allow at least 6 minutes for a single request before considering it stalled.
5. Do not let every polling cycle trigger a new reasoning decision or duplicate retry.
6. Do not submit the same prompt again while the prior request is still pending.
7. Retry only after explicit error, controlled termination beyond the wait threshold, or completed-image review failure.
8. Each image gets at most one retry.
9. After retry limit, log and continue the remaining set.
10. For large batch image production, suggest API or async generation outside the interactive Codex loop.

## Failure Record Template

```text
Image Number:
Module Name:
Attempt Count:
Failure Classification:
Elapsed Time:
Error / Termination Evidence:
Reason For Skip:
Next Action:
```

## Important Note

The 60-second polling interval, if present in logs, is not the ImageGen timeout.

Do not confuse polling cadence with generation deadline.

Only explicit tool errors or controlled post-threshold termination may trigger retry logic.

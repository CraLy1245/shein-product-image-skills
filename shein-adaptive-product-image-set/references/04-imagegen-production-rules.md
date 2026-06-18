# ImageGen Production Rules

Use this file when writing prompts or directly generating images through Codex imagegen.

## ImageGen Prompt Writing System

This skill is designed for Codex workflows that can directly call an image generation tool such as imagegen.

Do not call imagegen with a rough idea.

First create a production-ready prompt, then run the prompt preflight checklist, then call imagegen.

The prompt must be clear enough that another model or tool can generate the image without guessing the product, layout, copy, or visual rules.

## ImageGen Execution Mode

When the user requests actual image generation and Codex imagegen is available:

1. Analyze the 1688 package.
2. Select the primary and secondary visual strategy.
3. Define the shared Visual Anchor for the full image set.
4. Select the necessary image modules.
5. Assign Image Style Distribution for every selected image.
6. Create the image planning table.
7. Write one finalized imagegen prompt for each selected image.
8. Run the preflight checklist.
9. Call imagegen one image at a time.
10. Wait according to the ImageGen long-tail latency policy.
11. Review the completed image.
12. Continue to the next image only after the current image is accepted, skipped after retry limit, or marked for user review.

Do not call imagegen before the plan and prompt are ready.

Do not call imagegen for the entire set at once.

Do not submit duplicate prompts while a previous request is still pending.

## ImageGen Long-Tail Latency Policy

ImageGen can have long-tail latency.

A request may take several minutes and may return no intermediate progress.

The following are not failures:

- no visible progress update
- empty polling response
- quiet wait
- repeated wait cycle
- no image returned yet while the request is still pending

The following may be considered failures or actionable states:

- explicit `timeout` error
- explicit `429` or rate-limit error
- explicit `deadline exceeded` error
- explicit `server_error`
- content or safety rejection
- active termination after the minimum wait threshold
- completed output that fails product, text, or layout review

## Minimum Wait Rule

For each ImageGen request:

- Allow at least 6 minutes before treating the request as stalled.
- Do not interpret a 60-second polling interval as an ImageGen timeout.
- Do not retry simply because the tool is still waiting.
- Do not let every polling cycle trigger a new model decision.
- Do not terminate a pending request early unless there is an explicit error or the wait threshold has been reached.

If the request is still pending after the minimum wait threshold, the execution environment may actively terminate it once and classify it as `active_termination`.

Do not repeatedly terminate and retry the same image.

## Retry Limit Rule

For each selected image, the maximum attempts are:

1. Original ImageGen request
2. One retry

No third attempt.

No fourth attempt.

No repeated identical prompt loop.

A retry is allowed only when:

- ImageGen returns an explicit error.
- The request is actively terminated after the 6-minute minimum wait.
- The image completes but fails review against the product reference, layout, or readable text.

A retry is not allowed when:

- the tool is merely quiet
- polling returns empty
- intermediate progress is absent
- the assistant feels uncertain without evidence
- the previous identical request is still pending

## Duplicate Submission Ban

The assistant must not submit the same image prompt repeatedly while a previous request is unresolved.

Before retrying, check:

- Is there a completed image?
- Is there an explicit error?
- Was the previous request actively terminated after the wait threshold?
- Has the one-retry limit already been used?

If none of these conditions is true, wait instead of retrying.

## Continue-On-Failure Rule

If one image fails after the retry limit:

1. Record the failed image number.
2. Record the module name.
3. Record attempt count.
4. Record elapsed time.
5. Record failure classification.
6. Record reason for skipping.
7. Continue generating the remaining images unless the user explicitly asks to stop.

Do not let one failed image block the full product image set.

## Status Classification

Every ImageGen attempt must be classified as one of:

- `pending_empty_poll`
- `completed`
- `explicit_error`
- `active_termination`
- `completed_but_failed_review`
- `skipped_after_retry_limit`

Use `pending_empty_poll` when the system is still waiting and no final result has been returned.

Do not treat `pending_empty_poll` as failure.

Use `active_termination` only when the execution system actively terminates a request after the minimum wait threshold.

Use `explicit_error` only when ImageGen or the environment returns an actual error signal.

## Required ImageGen Execution Log

For every generated image attempt, record:

```text
Image Number:
Module Name:
Attempt Number:
Prompt Version / Prompt Identity:
Reference Images Used:
Start Time:
Last Poll Time:
End Time:
Elapsed Duration:
Status Classification:
Active Termination Used: Yes / No
Error Type If Any:
Retry Used: Yes / No
Final Action:
```

Allowed final actions:

- accepted
- retried
- skipped_and_continue
- user_review_needed

Allowed error types:

- timeout
- rate_limit
- server_error
- deadline_exceeded
- content_error
- unknown
- none

## Large Batch Guidance

For larger image sets or repeated production runs, recommend API or async generation instead of long interactive Codex ImageGen loops.

Reason:

- interactive polling can consume many execution turns
- repeated waiting can exhaust general Codex usage budget
- ImageGen may consume more resources than ordinary text turns
- async generation is better for larger batch production

This guidance does not block small image sets, but it should be mentioned when the user requests many images or repeated regeneration.

## Prompt Structure

Each imagegen prompt must include these sections in order:

1. Generation Goal
2. Product Reference Description
3. Visual System Anchor
4. Visual Variation Role
5. Applied Visual Style
6. Image Module Purpose
7. Composition And Layout
8. On-Image Text
9. Product Consistency Requirements
10. Detail / Scene Requirements
11. Text Safety And Claim Control
12. Negative Constraints

## Product Reference Description

Describe the product based on uploaded product materials.

Include:

- product category
- shape
- color
- material appearance
- surface texture
- key structure
- visible accessories
- SKU or size differences if relevant
- exact details that must not change

Use only confirmed product details.

If a detail is unclear, mark it as uncertain instead of inventing it.

## Visual System Anchor

Each prompt must inherit the same Visual Anchor.

The anchor includes:

- background family
- lighting direction and softness
- product rendering realism
- typography system
- label style
- accent color logic
- overall mood

The Visual Anchor keeps the full set unified.

Do not use it to force identical backgrounds.

## Visual Variation Role

Each image must also include a Visual Variation Role.

The Visual Variation Role explains how this image is different from the others while staying in the same visual system.

Specify:

- camera angle
- crop range
- product placement
- module layout
- background role
- callout placement
- prop intensity
- detail focus

Example:

```text
Visual Variation Role:
This image uses a close-up vertical detail composition with the product cropped larger than Image 1, a lighter background panel from the same neutral family, and small right-side callouts. It must not repeat the hero-layout background or label placement from Image 1.
```

## Applied Visual Style

Choose the visual style based on the module.

Examples:

- Z-001 main image style
- structure detail style
- material close-up style
- size diagram style
- lifestyle usage style
- capacity / organization style
- comparison style
- trust detail style

The Applied Visual Style must fit the image purpose.

Do not randomly choose a style.

## Composition And Layout

Each prompt must specify:

- 1:1 square ratio
- product position
- product scale
- text area
- callout placement
- detail boxes if needed
- arrows or dimension marks if needed
- scene props if needed
- safe margins

## On-Image Text

Use English text only.

Keep all text short and readable.

Use no more than:

- 1 short headline for main image
- 2 to 3 short feature tags for main image
- short labels / callouts for detail images
- simple dimension labels for size image

Do not use long paragraphs.

Do not use risky claims.

## Product Consistency Requirements

Every prompt must include:

```text
Use the uploaded product image as the exact product reference. Preserve the product's original shape, proportions, color, material, texture, structure, visible details, and SKU differences. Do not redesign the product. Do not add unsupported accessories. Do not change the product category.
```

If the product has multiple SKUs and SKU image is not requested, show only the necessary SKU for the current image.

## Detail / Scene Requirements

For detail images:

- focus on one clear detail
- use thin callout lines
- use small labels
- do not create a crowded infographic
- do not use large title blocks

For scene images:

- show realistic use
- keep product clearly visible
- do not bury the product in props
- do not add unsupported use cases
- do not make the scene more important than the product

For size images:

- show clear dimensions
- use cm and inch when available
- include scale reference only when appropriate
- do not invent sizes

## Text Safety And Claim Control

Avoid:

- best
- perfect
- 100% guarantee
- medical-grade
- therapeutic
- cure
- pain relief
- waterproof unless supported
- leakproof unless supported
- non-toxic unless certified
- eco-friendly unless certified
- fake certification badges

Prefer:

- easy to clean
- water-resistant surface
- compact storage
- stable support
- easy access
- designed for daily use
- space-saving design

## Negative Constraints

Every prompt must include negative constraints:

- do not alter product shape
- do not change product color
- do not invent product features
- do not add unsupported accessories
- do not use unreadable text
- do not use crowded layout
- do not over-decorate
- do not use excessive icons
- do not use fake badges
- do not use exaggerated claims
- do not create different visual systems across images
- do not repeat the exact same background or same visual task across images

## Preflight Checklist Before ImageGen

Before each imagegen call, verify:

1. Is the prompt for one image only?
2. Is the product reference clearly described?
3. Is the shared Visual Anchor included?
4. Is the Visual Variation Role included?
5. Is the image module purpose clear?
6. Is the layout specified?
7. Is the English copy exact and short?
8. Are product consistency rules included?
9. Are risk words removed?
10. Are negative constraints included?
11. Is this image visually different from the previous image while staying in the same system?
12. Is this prompt not a duplicate of the previous prompt?
13. Has the previous ImageGen request completed, errored, or been terminated after the minimum wait threshold before retrying?
14. Has the retry limit for this image not been exceeded?

If any answer is no, revise the prompt before generating.

## After Generation Review

After each image is generated, check:

1. Product shape preserved?
2. Product material preserved?
3. Product color preserved?
4. Product proportions preserved?
5. No unsupported accessories?
6. Text readable?
7. No risky claims?
8. Layout matches module?
9. Visual system matches the set?
10. Visual role differs from previous images?
11. Image solves the intended purchase question?

If the image fails, regenerate only if retry limit has not been used.

If retry limit has been used, record the failure and continue.

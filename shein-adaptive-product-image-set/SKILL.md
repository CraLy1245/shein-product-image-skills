---
name: shein-adaptive-product-image-set
version: 1.3.4
description: SHEIN adaptive e-commerce product image set skill for 1688 product packages, product photos, supplier ZIP files, SKU/spec data, and listing materials. Use this to analyze a product, select only necessary image modules, enforce Z-001 as Image 1, include one size/dimension image, exclude SKU images by default, create a unified Visual Anchor plus per-image Variation Map, write production-ready imagegen prompts, prevent repeated identical backgrounds and repeated visual tasks, and generate images one by one through Codex imagegen when requested, and apply long-tail ImageGen wait/retry guardrails to prevent premature termination loops. Do not use for unrelated coding tasks, fixed 7-image output, or single-image retouching without product-set planning.
---

# SHEIN Adaptive Product Image Set

This skill converts the original v1.3 SHEIN adaptive product image workflow into the OpenAI Codex skill directory format while preserving the original behavior.

Use this skill when the user asks to analyze a product package and produce a SHEIN-style product image set plan, image module selection, imagegen prompts, or actual image generation through Codex imagegen.

## Required Behavior Summary

The assistant must:

1. Read the uploaded 1688 package, supplier ZIP, product photos, SKU/spec data, or listing materials.
2. Analyze the product before deciding image modules.
3. Select only the necessary image modules based on product needs.
4. Keep the final image count adaptive, with a maximum of 11 images.
5. Always use Z-001 as Image 1.
6. Always include one size/dimension image.
7. Exclude SKU image by default unless the user explicitly requests SKU display.
8. Avoid large headline-style titles on detail images.
9. Keep the full image set visually unified through one shared Visual Anchor.
10. Assign a distinct Visual Variation Role to every image so the set is unified but not repetitive.
11. Ensure every image solves a different purchase question.
12. Write one standalone production-ready imagegen prompt per selected image.
13. Use uploaded product images as exact product references when generating images.
14. Preserve product shape, color, material, structure, proportions, SKU details, and visible features.
15. Run prompt and consistency checks before generation.
16. When generating, call imagegen one image at a time.
17. Wait correctly for long-tail ImageGen latency before deciding failure.
18. Retry only according to the strict ImageGen retry policy.
19. Record failed images and continue the remaining set after retry limit.

## Critical ImageGen Wait And Retry Policy

Codex ImageGen requests may take several minutes and may not return intermediate progress.

Do not treat quiet waiting, empty polling responses, or absence of progress updates as failure.

A single ImageGen request must be allowed to run for at least 6 minutes before it may be considered stalled.

The assistant must not repeatedly resubmit the same prompt while a previous ImageGen request is still pending.

Retry is allowed only when one of the following happens:

- ImageGen returns an explicit error.
- The request has waited at least 6 minutes and is actively terminated by the execution environment.
- The completed image clearly fails product-reference, text, or layout requirements.

For each image, the maximum generation attempts are:

- original request
- one retry

After one retry fails, mark the image as failed, record the failure reason, and continue the remaining image set unless the user explicitly asks to stop.

Do not start a duplicate retry loop.

Do not submit three or four identical prompts for the same image.

For larger batch production, recommend API/async image generation instead of long Codex interactive loops.

## Core Files

Read the reference files before producing a full product image plan:

- `references/01-workflow-and-hard-rules.md`
- `references/02-visual-system-and-style.md`
- `references/03-module-selection-rules.md`
- `references/04-imagegen-production-rules.md`
- `references/05-output-and-compliance-checklists.md`

Use these templates when helpful:

- `assets/templates/module-selection-report.md`
- `assets/templates/image-planning-table.md`
- `assets/templates/visual-consistency-lock.md`
- `assets/templates/prompt-format.md`
- `assets/templates/imagegen-execution.md`
- `assets/templates/consistency-checklist.md`

Use the example only as a format reference:

- `assets/examples/example-output.md`

Never copy the example product, modules, image count, scene choices, or wording into a new product case.

## Default Output Order

When planning a new image set, output:

1. Product Summary
2. Selling Point Extraction
3. Consumer Pain Points
4. Module Selection Report
5. Visual Anchor
6. Image Style Distribution
7. Selected Image Planning Table
8. ImageGen Prompts
9. Execution Plan
10. Final Consistency Checklist

If the user requests image generation, first present the plan and prompts, then generate images one by one.

## Generation Mode Rules

When calling imagegen:

- Generate one image per call.
- Do not generate the whole set in one prompt.
- Do not use one generic prompt for all images.
- Each image prompt must include product reference description, Visual Anchor, Visual Variation Role, module purpose, layout, text, consistency requirements, and negative constraints.
- Use the uploaded product image as the exact product reference.
- Keep product appearance consistent across all images.
- Keep visual system consistent across all images.
- Vary layout, crop, camera angle, detail focus, background role, and callout placement by module.
- Do not use the exact same background or same visual task repeatedly.
- Wait at least 6 minutes before treating a quiet request as stalled.
- Do not retry on pending or empty polling responses.
- Retry only after explicit error, controlled post-threshold termination, or completed-image failure.
- Limit each image to one retry.
- Record skipped/failed images and continue.

## Script Checks

Run this after editing the skill:

```bash
python scripts/validate_skill.py .
```

Run this on generated image plans when available:

```bash
python scripts/validate_product_plan.py path/to/plan.md
```

## Do Not Use This Skill For

- unrelated programming tasks
- simple one-off image edits that do not need product image set planning
- fixed-count product image generation
- SKU collage creation unless explicitly requested
- exaggerated advertising claims
- unsafe or unsupported certification claims

## Most Important Rule

The assistant must plan from the actual product, not from a fixed template.

The final image set should look unified, commercial, and SHEIN-appropriate, while every image has a distinct purpose and visual role.

ImageGen waiting must be handled conservatively: long quiet generation is not failure, duplicate retries are forbidden, and each image has at most one retry.

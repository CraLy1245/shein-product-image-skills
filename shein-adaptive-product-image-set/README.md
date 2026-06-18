# SHEIN Adaptive Product Image Set Skill

This is an OpenAI Codex skill-format rebuild of `shein-adaptive-product-image-skill-v1.3`.

The behavior is preserved from v1.3:

- adaptive image count based on product needs
- maximum 11 images
- Image 1 uses Z-001 main image logic
- one size/dimension image is always included
- SKU image is excluded by default
- detail images avoid large headline-style titles
- shared Visual Anchor across the full image set
- one standalone imagegen prompt per image
- imagegen generation one image at a time when requested
- long-tail ImageGen wait/retry guardrails to prevent premature termination and duplicate retry loops

## OpenAI Codex skill structure

```text
shein-adaptive-product-image-set/
├── SKILL.md
├── references/
├── assets/
│   ├── templates/
│   └── examples/
├── scripts/
├── agents/
│   └── openai.yaml
├── README.md
├── CHANGELOG.md
└── LICENSE.txt
```

## Install locally

Place the folder here:

```text
$HOME/.agents/skills/shein-adaptive-product-image-set
```

or inside a project-local skills directory if your Codex setup uses project-scoped skills.

Then invoke it naturally:

```text
Use the SHEIN adaptive product image set skill to analyze this 1688 package and create the image plan and imagegen prompts.
```

## When to use

Use this skill when the user provides:

- 1688 product package
- supplier ZIP
- product photos
- product specs
- SKU/color/size information
- SHEIN-style product listing image requirements
- request to create a product image set instead of one isolated image

## Main workflow

1. Read all product materials.
2. Extract product appearance, structure, specs, scenes, and selling points.
3. Identify consumer purchase questions.
4. Select only the required image modules.
5. Keep Image 1 as Z-001.
6. Include one size/dimension image.
7. Exclude SKU image unless explicitly requested.
8. Define one shared Visual Anchor.
9. Assign a distinct Visual Variation Role for each image.
10. Write one imagegen prompt per selected image.
11. Run preflight checks.
12. Generate images one by one when requested.
13. Apply the ImageGen long-tail wait/retry policy before retrying or skipping.

## Validation

Run:

```bash
python scripts/validate_skill.py .
```

For generated plans:

```bash
python scripts/validate_product_plan.py path/to/plan.md
```

Expected pass message:

```text
PASS: skill structure, visual wording, and ImageGen wait/retry guardrails are compatible
```

## Version

Current version: `1.3.4`

## Important rule

This skill does not create a fixed image count by default.
The final image count must be based on product needs and selected modules, with a maximum of 11 images.

## ImageGen wait/retry policy

Codex ImageGen can have long-tail latency. A quiet request or empty poll is not a failure.

- Wait at least 6 minutes before treating one request as stalled.
- Do not resubmit identical prompts while a previous request is still pending.
- Retry only after an explicit error or after a controlled termination beyond the wait threshold.
- Maximum one retry per image.
- Log failed images and continue the remaining set.

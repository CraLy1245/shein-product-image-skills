# Codex Install

Use this folder as a Codex Skill:

```text
shein-adaptive-product-image-set/
```

The required entry file is:

```text
shein-adaptive-product-image-set/SKILL.md
```

## Local install

Copy the folder to your Codex skills location, for example:

```text
$HOME/.agents/skills/shein-adaptive-product-image-set
```

Then ask Codex:

```text
Use $shein-adaptive-product-image-set to analyze this product package and create the image set plan and ImageGen prompts.
```

## First test run

For the first run, ask Codex to output planning only:

```text
Use the SHEIN adaptive product image set skill. First output Product Summary, Selling Point Extraction, Module Selection Report, Visual Anchor, Image Style Distribution, Selected Image Planning Table, and ImageGen Prompts. Do not generate images yet.
```

After confirming the plan, ask it to generate images one by one.

## ImageGen safety test

When generating images, confirm that Codex follows v1.3.4 rules:

- one image per ImageGen call
- minimum 6-minute wait before treating a request as stalled
- no retry on quiet wait or empty polling
- maximum one retry per image
- no repeated identical prompt submissions
- failed image is logged and skipped after retry limit

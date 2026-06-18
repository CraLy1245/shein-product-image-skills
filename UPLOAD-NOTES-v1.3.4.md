# Upload Notes — v1.3.4

Date: 2026-06-18

Repository update target:

```text
CraLy1245/shein-product-image-skills
```

## What was updated

The repository now contains the `shein-adaptive-product-image-set/` Skill folder with v1.3.4 mainline rules.

Main v1.3.4 addition:

- ImageGen long-tail latency handling
- minimum 6-minute wait rule
- no retry on quiet wait / empty polling
- explicit error or controlled post-threshold termination required before retry
- maximum one retry per image
- duplicate prompt submission ban
- continue-on-failure rule
- ImageGen execution log fields

## Binary ZIP note

The connector used for this update supports text file commits but not direct binary ZIP upload.

The extracted Skill source files are committed for GitHub version control and Codex inspection.

The generated ZIP package remains:

```text
shein-adaptive-product-image-set-openai-compliant-v1.3.4-mainline.zip
```

Use the ZIP from the ChatGPT workspace when a downloadable compressed package is needed.

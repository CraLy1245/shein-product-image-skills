# Workflow And Hard Rules

These rules must be followed before planning any image set.

## Core Principle

Do not create a fixed image count by default.

This skill creates an adaptive product image set. The number of images must be decided by actual product needs.

Do not choose the image count first. First analyze the product, then select the necessary image modules.

The final image count equals the number of selected modules, with a maximum of 11 images.

Every selected image must solve one clear purchase question.

Do not create extra images just to make the set look fuller.

## Required Workflow

1. Read all available product materials from the 1688 package, supplier ZIP, product photos, specs, SKU/color/size data, and listing materials.
2. Extract product appearance, structure, material, size, SKU, functions, usage scenarios, and supplier claims.
3. Convert raw supplier selling points into consumer-facing benefits.
4. Identify click selling point, conversion selling point, trust-building selling point, size/fit/capacity concern, usage scenario, and AI generation risk.
5. Select image modules by product need.
6. Keep Image 1 as Z-001 Main Image.
7. Include one Size / Dimension Image.
8. Exclude SKU image by default unless explicitly requested.
9. Define one shared Visual Anchor.
10. Assign a distinct Visual Variation Role to each image.
11. Write one production-ready imagegen prompt per selected image.
12. Generate one image at a time only when the user requests generation.
13. Apply the ImageGen wait/retry policy from `04-imagegen-production-rules.md`.

## Hard Rules

- Maximum image count: 11.
- Image 1 must use Z-001.
- One size/dimension image is mandatory.
- SKU image is excluded by default.
- Detail images must avoid large headline-style titles.
- English text only for on-image copy.
- Product appearance must be preserved from reference images.
- No exaggerated or unsupported claims.
- No fake certifications, badges, or unsupported material claims.
- No repeated identical backgrounds or repeated visual tasks.

## Output Expectations

Always output product analysis, module selection, Visual Anchor, Image Style Distribution, planning table, imagegen prompts, and final consistency checklist before generating.

# ImageGen Prompt Format Template

This template is for Codex workflows that call imagegen directly.

Do not call imagegen with a rough idea. Write a production-ready prompt first, run the preflight checklist, then call imagegen.

## Required Prompt Structure

Every imagegen prompt must include these sections in order:

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

## Visual Anchor Rule

Before writing prompts, define one shared Visual Anchor for the full image set.

The Visual Anchor must include:

- Background family
- Lighting
- Product rendering
- Typography
- Label style
- Accent color
- Overall mood

Every imagegen prompt must inherit the same Visual Anchor.

Consistency means shared background family, lighting, typography, label language, product rendering, and layout cleanliness.

Variation is required in background role, camera angle, module layout, detail focus, scene context, prop intensity, label placement, and product placement.

## Baseline Visual System Anchor

Use the same visual system as the full product image set: [background family, not identical background], [lighting direction], realistic product rendering, soft shadows, subtle edge highlights, restrained accent colors, minimal sans-serif English typography, consistent small-label language, clean spacing, and product-first composition. Keep the layout practical, refined, and not crowded. This image must use its assigned Visual Variation Role: [background role], [product angle/crop], [layout pattern], [scene/prop intensity], and [label placement]. It must look like part of the same product listing series without copying the same background or layout from other images.

## Production Prompt Template

```text
IMAGE [number] — [module name]

Generation Goal:
Create a 1:1 English e-commerce product image for [product category]. This image is used as [main image / detail image / size image / material image / usage scenario image] for a SHEIN-style product listing.

Product Reference Description:
Use the uploaded product image as the exact product reference. The product is [category], with [shape], [color], [material/surface], [key structure], and [visible details]. Preserve the product appearance exactly.

Visual System Anchor:
[Shared Visual Anchor for the full image set.]

Visual Variation Role:
[How this image differs from the others while staying in the same visual system.]

Applied Visual Style:
Use [Z-001 main image style / structure detail style / material close-up style / size diagram style / lifestyle usage style].

Image Module Purpose:
This image should explain [current image purpose] and answer [purchase question].

Composition And Layout:
[1:1 square ratio, product position, product scale, text area, callout placement, dimensions, scene props, safe margins.]

On-Image Text:
[Exact short English text only.]

Product Consistency Requirements:
Use the uploaded product image as the exact product reference. Preserve the product's original shape, proportions, color, material, texture, structure, visible details, and SKU differences. Do not redesign the product. Do not add unsupported accessories. Do not change the product category.

Detail / Scene Requirements:
[Detail, scene, size, capacity, or usage-specific rules.]

Text Safety And Claim Control:
Avoid exaggerated, medical, certification, baby/infant, non-toxic, eco-friendly, waterproof, or leakproof claims unless supported.

Negative Constraints:
Do not alter product shape. Do not change product color. Do not invent product features. Do not add unsupported accessories. Do not use unreadable text. Do not use crowded layout. Do not over-decorate. Do not use fake badges. Do not create different visual systems across images. Do not repeat the exact same background or same visual task across images.
```

## Preflight Checklist

Before each imagegen call, verify:

1. The prompt is for one image only.
2. The product reference is clear.
3. The shared Visual Anchor is included.
4. The Visual Variation Role is included.
5. The image module purpose is clear.
6. The layout is specified.
7. English copy is exact and short.
8. Product consistency rules are included.
9. Risk words are removed.
10. Negative constraints are included.
11. This prompt is not a duplicate of the previous prompt.
12. The previous ImageGen request has completed, errored, or been terminated after the minimum wait threshold before retrying.
13. The retry limit has not been exceeded.

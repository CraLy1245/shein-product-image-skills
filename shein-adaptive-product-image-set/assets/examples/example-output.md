# Example Output Structure

This file is a format reference only. Do not copy the product type, selling points, modules, final image count, layouts, scene choices, or prompt wording.

For every new product, rebuild the analysis from the uploaded 1688 package or product materials.

## 1. Product Summary

- Product Type:
- Product Appearance:
- Main Use Scenario:
- Key Specifications:
- AI Generation Risks:

## 2. Selling Point Extraction

- Click Selling Point:
- Conversion Selling Points:
- Trust-Building Selling Points:
- Size / Fit / Capacity Concern:
- Pain-Point Solution:
- Unsupported Or Risky Claims To Avoid:

## 3. Style Decision

- Product Type:
- Main Purchase Reason:
- Main Consumer Concerns:
- Visual Difficulty:
- Primary Style:
- Secondary Style:
- Styles Not Recommended:
- Reason For Style Choice:

## 4. Visual Anchor

Define one shared visual system for the full image set.

- Background family:
- Lighting:
- Product rendering:
- Typography:
- Label style:
- Accent color:
- Overall mood:

Do not create a new visual style for each image, but do not copy the exact same background or layout either.

## 5. Image Style Distribution

| Image Number | Image Module | Applied Visual Style | Visual Anchor Used | Visual Variation Role | Reason For This Style |
|---|---|---|---|---|---|
| 1 | Z-001 Main Image | Z-001 + primary style | Shared anchor | Click hero variation | Establish click-oriented visual identity |
| 2 | Selected module | Module-specific style | Shared anchor | Different layout / crop / evidence type | Explain one purchase question |

## 6. Module Selection Report

Mandatory modules:

- Z-001 Main Image
- Size / Dimension Image

Selected optional modules:

- Choose only modules that solve real product-specific purchase questions.

Skipped modules:

- SKU Image is excluded by default unless explicitly requested.

Final Recommended Image Count:

- Equal to selected modules, maximum 11.

## 7. Selected Image Planning Table

Use `assets/templates/image-planning-table.md`.

Each row must be product-specific.

## 8. English Image Copy

Image 1:

- Headline: short click-oriented English headline
- Feature Tags: 2–3 short tags

Images after Image 1:

- Use small labels, callouts, dimension labels, corner tags, before/after labels, or short captions.
- Do not use large headline-style titles.

## 9. ImageGen Prompts

Write one prompt per selected image.

Each prompt must include product reference description, Visual Anchor, Visual Variation Role, module purpose, layout, English copy, product consistency requirements, and negative constraints.

## 10. ImageGen Execution Log

Use this only when imagegen is called.

- Image Number:
- Module Name:
- Attempt Number:
- Status Classification:
- Elapsed Duration:
- Retry Used:
- Final Action:

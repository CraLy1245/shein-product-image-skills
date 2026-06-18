# Consistency Checklist

1. Is Image 1 using Z-001?
2. Is the Size / Dimension Image included?
3. Is SKU image excluded by default?
4. Is the final image count based on selected modules instead of fixed count?
5. Is the total image count no more than 11?
6. Does every image solve a different purchase question?
7. Are any images redundant?
8. Are detail images free of large headlines?
9. Is the product consistent across all images?
10. Are the background, lighting, typography, callouts, and label styles consistent?
11. Does every image inherit the same Visual Anchor?
12. Does each image have an Applied Visual Style that fits its module?
13. Are visual differences intentional rather than random?
14. Are there any exaggerated claims?
15. Are there any risky words?
16. Does the whole set look like one unified commercial product image series?
17. Would the image set be suitable for SHEIN-style product listing and portfolio display?

# Visual Anchor Checklist

1. Was one shared Visual Anchor defined before prompts?
2. Does the Visual Anchor include background family, lighting, product rendering, typography, labels, accent color, and mood?
3. Are all prompts using the same Visual Anchor?
4. Are images unified without repeating the exact same layout?
5. Are backgrounds from the same family but not identical copies?
6. Is lighting consistent but composition varied?
7. Is product rendering realistic and consistent?
8. Is typography consistent across all images?
9. Are label styles consistent but not placed the same way each time?

# Visual Variation Checklist

1. Does each image have a distinct Visual Variation Role?
2. Does each image use a different camera angle, crop, or layout role?
3. Does each image answer a different purchase question?
4. Is the Main Visual Evidence Type different where possible?
5. Are repeated visual tasks merged or removed?
6. Is any image only a restyled copy of another image?
7. Are callout placements varied?
8. Are detail boxes used only when they actually help?
9. Are scene props controlled and relevant?
10. Does the set avoid repeated infographic patterns?

# ImageGen Prompt Checklist

1. Does each prompt include Generation Goal?
2. Does each prompt include Product Reference Description?
3. Does each prompt include Visual System Anchor?
4. Does each prompt include Visual Variation Role?
5. Does each prompt include Applied Visual Style?
6. Does each prompt include Image Module Purpose?
7. Does each prompt include Composition And Layout?
8. Does each prompt include On-Image Text?
9. Does each prompt include Product Consistency Requirements?
10. Does each prompt include Detail / Scene Requirements?
11. Does each prompt include Text Safety And Claim Control?
12. Does each prompt include Negative Constraints?
13. Is the prompt standalone enough to generate the image without guessing?
14. Does the prompt avoid copying the example product or example wording?
15. Does the prompt avoid repeated background wording?

# ImageGen Wait / Retry Checklist

1. Has the current ImageGen request been allowed to wait at least 6 minutes before being considered stalled?
2. Was a quiet wait treated as pending rather than failure?
3. Was an empty poll classified as `pending_empty_poll` rather than error?
4. Was retry triggered only by explicit error, controlled active termination after threshold, or completed-image review failure?
5. Has the image used no more than one retry?
6. Was duplicate prompt submission avoided while a prior request was still pending?
7. If retry failed, was the image logged and the remaining set continued?

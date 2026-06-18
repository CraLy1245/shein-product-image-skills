# Install Check

After cloning or downloading this repository, check:

```text
shein-adaptive-product-image-set/SKILL.md
```

The frontmatter should contain:

```yaml
name: shein-adaptive-product-image-set
version: 1.3.4
```

Then run:

```bash
cd shein-adaptive-product-image-set
python scripts/validate_skill.py .
```

Expected result:

```text
PASS: skill structure, visual wording, and ImageGen wait/retry guardrails are compatible
```

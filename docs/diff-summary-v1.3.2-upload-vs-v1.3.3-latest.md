# v1.3.2 上传版 vs v1.3.3 最新版差异摘要

## 结论

- `v1.3.3` 是当前主线最新版。
- 用户上传的 `v1.3.2(1)(1)` 不是最新版，它主要做了“布局不要重复”的修正，但没有完整补上自动校验闭环。
- `v1.3.3` 在 `v1.3.2` 的基础上补了两类关键校验：
  1. 检查是否又出现高风险同质化措辞 `same background tone`。
  2. 检查不同图片是否出现重复的 `Main Visual Evidence Type / Visual Task`。

## 主要差异

| 项目 | v1.3.2 上传版 | v1.3.3 最新版 |
|---|---|---|
| 当前定位 | 过渡修正版 | 主线最新版 |
| 是否调用 imagegen | 是，用户要求生成时逐张调用 | 是，用户要求生成时逐张调用 |
| 背景一致问题 | 改成 controlled variation，但偏文档规则 | 加入 Visual Variation Map 与脚本校验 |
| 视觉任务重复 | 有规则提醒 | 有脚本检查 `Main Visual Evidence Type / Visual Task` 重复 |
| `same background tone` 风险 | 文档层基本规避 | 脚本层自动拦截 |
| 提示词结构 | 有 Visual Anchor | 有 Visual Anchor + Visual Variation Role + Main Visual Evidence Type |
| 版本建议 | 归档，不再继续使用 | 作为当前主线 latest |

## 文件层变化

两版都有相同的 OpenAI Codex skill 基础结构，但 `v1.3.3` 更新了 17 个文件：

- `SKILL.md`
- `README.md`
- `CHANGELOG.md`
- `assets/manifest.json`
- `assets/examples/example-output.md`
- `assets/templates/consistency-checklist.md`
- `assets/templates/image-planning-table.md`
- `assets/templates/module-selection-report.md`
- `assets/templates/prompt-format.md`
- `assets/templates/visual-consistency-lock.md`
- `references/01-workflow-and-hard-rules.md`
- `references/02-visual-system-and-style.md`
- `references/03-module-selection-rules.md`
- `references/04-imagegen-production-rules.md`
- `references/05-output-and-compliance-checklists.md`
- `scripts/validate_product_plan.py`
- `scripts/validate_skill.py`

## 版本整理建议

以后不要继续用文件名里的 `(1)(1)`、`(1)(3)` 判断版本。只看 skill 内部 `SKILL.md` 的 frontmatter：

```yaml
name: ...
version: ...
```

当前推荐：

- 主线直接生图版：`shein-adaptive-product-image-set` `1.3.3`
- 不直接生图衍生版：`shein-adaptive-product-image-set-planpack` `1.3.3-planpack.1`

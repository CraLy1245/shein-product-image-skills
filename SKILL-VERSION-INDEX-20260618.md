# SHEIN Product Image Skill 版本整理表

## 当前保留版本

| 类型 | Skill Name | Version | 文件名 | 是否调用 imagegen | 用途 |
|---|---|---:|---|---|---|
| 主线最新版 | `shein-adaptive-product-image-set` | `1.3.3` | `shein-adaptive-product-image-set-openai-compliant-v1.3.3-mainline.zip` | 是 | 分析产品、选图、写 prompt，并在用户要求生成时逐张调用 Codex imagegen |
| 衍生分支 | `shein-adaptive-product-image-set-planpack` | `1.3.3-planpack.1` | `shein-adaptive-product-image-set-planpack-v1.3.3-planpack.1.zip` | 否 | 只创建每张图的生产文件夹与 prompt/material 文件，不直接生图 |

## 命名规则

### 主线版本

格式：

```text
shein-adaptive-product-image-set-openai-compliant-v主版本号-mainline.zip
```

示例：

```text
shein-adaptive-product-image-set-openai-compliant-v1.3.3-mainline.zip
```

主线版本用于直接生图。它允许在用户明确要求生成时调用 Codex imagegen。

### 衍生分支版本

格式：

```text
shein-adaptive-product-image-set-planpack-v主线版本号-planpack.分支修订号.zip
```

示例：

```text
shein-adaptive-product-image-set-planpack-v1.3.3-planpack.1.zip
```

`planpack` 表示这个分支只做生产包，不直接生图。

## 以后怎么升级

### 主线继续升级

- `1.3.4`：直接生图主线的下一次修复。
- `1.4.0`：主线出现较大功能变化，例如模块体系重构。

### PlanPack 分支继续升级

- `1.3.3-planpack.2`：仍然基于主线 `1.3.3`，只是文件夹/交付方式小修。
- `1.3.4-planpack.1`：当主线升级到 `1.3.4` 后，重新派生的新 PlanPack 分支。

## 归档规则

以下文件名容易造成混乱，不再作为正式版本名使用：

- 带 `(1)`、`(1)(1)`、`(1)(3)` 的浏览器重复下载文件名。
- 只写 `v1.3.2` 但没有说明是 mainline 还是 branch 的文件名。
- 文件名版本和 `SKILL.md` 内部版本不一致的压缩包。

以后判断版本，只看：

1. `SKILL.md` frontmatter 的 `name`
2. `SKILL.md` frontmatter 的 `version`
3. 压缩包是否符合上面的正式命名规则

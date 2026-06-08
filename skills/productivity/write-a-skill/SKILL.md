---
name: write-a-skill
description: Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, or build a new skill.
---

# Skill の書き方 (Writing Skills)

## 手順 (Process)

1. **要件の収集 (Gather requirements)** — ユーザーに確認:
   - この skill はどのタスク/ドメインをカバーするか?
   - どの具体的なユースケースを扱うべきか?
   - 実行可能な script が必要か、それとも指示だけでよいか?
   - 含めるべき参考資料はあるか?

2. **skill のドラフト作成 (Draft the skill)** — 以下を作成:
   - 簡潔な指示を含む SKILL.md
   - 内容が 500 行を超える場合は追加の reference ファイル
   - 決定的な操作が必要な場合は utility script

3. **ユーザーとのレビュー (Review with user)** — ドラフトを提示し確認:
   - ユースケースをカバーしているか?
   - 不足や不明点はあるか?
   - どのセクションを詳しく/簡潔にすべきか?

## Skill の構造 (Skill Structure)

```
skill-name/
├── SKILL.md           # Main instructions (required)
├── REFERENCE.md       # Detailed docs (if needed)
├── EXAMPLES.md        # Usage examples (if needed)
└── scripts/           # Utility scripts (if needed)
    └── helper.js
```

## SKILL.md テンプレート (SKILL.md Template)

```md
---
name: skill-name
description: Brief description of capability. Use when [specific triggers].
---

# Skill Name

## Quick start

[Minimal working example]

## Workflows

[Step-by-step processes with checklists for complex tasks]

## Advanced features

[Link to separate files: See [REFERENCE.md](REFERENCE.md)]
```

## description の要件 (Description Requirements)

description は、agent がどの skill を読み込むか判断するときに**唯一見えるもの**である。インストール済みの他の skill と並んで system prompt に表示される。agent はこれらの description を読み、ユーザーのリクエストに基づいて関連する skill を選ぶ。

**目標**: agent が次を判断するのに十分な情報を与える:

1. この skill が提供する capability
2. いつ/なぜトリガーするか (特定のキーワード、コンテキスト、ファイルタイプ)

**フォーマット**:

- 最大 1024 文字
- 三人称で書く
- 最初の文: 何をするか
- 2 番目の文: "Use when [specific triggers]"

**良い例 (Good example)**:

```
Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when user mentions PDFs, forms, or document extraction.
```

**悪い例 (Bad example)**:

```
Helps with documents.
```

悪い例では、他の document skill と区別する手がかりが agent に与えられない。

## script を追加するタイミング (When to Add Scripts)

以下の場合に utility script を追加:

- 操作が決定的 (validation、formatting)
- 同じ code が繰り返し生成される
- エラーに明示的な handling が必要

script は token を節約し、生成 code より信頼性が高い。

## ファイルを分割するタイミング (When to Split Files)

以下の場合に別ファイルへ分割:

- SKILL.md が 100 行を超える
- 内容が異なるドメインを持つ (finance vs sales schemas)
- 高度な機能がほとんど使われない

## レビューチェックリスト (Review Checklist)

ドラフト後、以下を確認:

- [ ] description にトリガー ("Use when...") が含まれている
- [ ] SKILL.md が 100 行未満
- [ ] 時限のある情報がない
- [ ] 用語が一貫している
- [ ] 具体例が含まれている
- [ ] 参照は 1 階層まで

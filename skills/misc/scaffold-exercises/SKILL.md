---
name: scaffold-exercises
description: sections、problems、solutions、explainers からなる、lint を通過する exercise ディレクトリ構造を作成する。ユーザーが exercise を scaffold したい、exercise stub を作成したい、または新しい course section をセットアップしたいときに使う。
---

# Exercise の scaffold (Scaffold Exercises)

`pnpm ai-hero-cli internal lint` を通過する exercise ディレクトリ構造を作成し、`git commit` で commit する。

## ディレクトリ命名 (Directory naming)

- **Sections**: `exercises/` 内の `XX-section-name/` (例: `01-retrieval-skill-building`)
- **Exercises**: section 内の `XX.YY-exercise-name/` (例: `01.03-retrieval-with-bm25`)
- section 番号 = `XX`、exercise 番号 = `XX.YY`
- 名前は dash-case (小文字、ハイフン)

## Exercise の variant (Exercise variants)

各 exercise には少なくとも次のいずれかの subfolder が必要:

- `problem/` — TODO 付きの学生 workspace
- `solution/` — 参照実装
- `explainer/` — 概念的な資料、TODO なし

stub 作成時は、plan で指定がなければデフォルトで `explainer/`。

## 必須ファイル (Required files)

各 subfolder (`problem/`、`solution/`、`explainer/`) には `readme.md` が必要:

- **空でない**こと (タイトル行 1 行でも実質的な内容があればよい)
- 壊れた link がないこと

stub 作成時は、タイトルと description を含む最小限の readme を作成:

```md
# Exercise Title

Description here
```

subfolder に code がある場合は `main.ts` も必要 (>1 行)。stub の場合は readme のみの exercise でもよい。

## ワークフロー (Workflow)

1. **plan の解析 (Parse the plan)** — section 名、exercise 名、variant タイプを抽出
2. **ディレクトリの作成 (Create directories)** — 各 path に `mkdir -p`
3. **stub readme の作成 (Create stub readmes)** — variant folder ごとにタイトル付き `readme.md` を 1 つ
4. **lint の実行 (Run lint)** — `pnpm ai-hero-cli internal lint` で検証
5. **エラーの修正 (Fix any errors)** — lint が通るまで繰り返す

## lint ルール概要 (Lint rules summary)

linter (`pnpm ai-hero-cli internal lint`) のチェック内容:

- 各 exercise に subfolder (`problem/`、`solution/`、`explainer/`) がある
- `problem/`、`explainer/`、または `explainer.1/` のいずれかが存在する
- 主要 subfolder に非空の `readme.md` がある
- `.gitkeep` ファイルがない
- `speaker-notes.md` ファイルがない
- readme に壊れた link がない
- readme に `pnpm run exercise` コマンドがない
- readme のみでない限り、subfolder ごとに `main.ts` が必要

## exercise の移動/リネーム (Moving/renaming exercises)

番号付け直しや移動時:

1. ディレクトリのリネームは `mv` ではなく `git mv` を使う — git history を保持
2. 順序を維持するため数値 prefix を更新
3. 移動後に lint を再実行

例:

```bash
git mv exercises/01-retrieval/01.03-embeddings exercises/01-retrieval/01.04-embeddings
```

## 例: plan からの stub 作成 (Example: stubbing from a plan)

次のような plan が与えられた場合:

```
Section 05: Memory Skill Building
- 05.01 Introduction to Memory
- 05.02 Short-term Memory (explainer + problem + solution)
- 05.03 Long-term Memory
```

作成:

```bash
mkdir -p exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer
mkdir -p exercises/05-memory-skill-building/05.02-short-term-memory/{explainer,problem,solution}
mkdir -p exercises/05-memory-skill-building/05.03-long-term-memory/explainer
```

次に readme stub を作成:

```
exercises/05-memory-skill-building/05.01-introduction-to-memory/explainer/readme.md -> "# Introduction to Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/explainer/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/problem/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.02-short-term-memory/solution/readme.md -> "# Short-term Memory"
exercises/05-memory-skill-building/05.03-long-term-memory/explainer/readme.md -> "# Long-term Memory"
```

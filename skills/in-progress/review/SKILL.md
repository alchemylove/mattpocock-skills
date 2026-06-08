---
name: review
description: Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/PRD asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X".
---

# レビュー (Review)

ユーザーが指定した fixed point と `HEAD` の間の diff を、2 軸でレビューする:

- **Standards** — code はこの repo の文書化された coding standards に準拠しているか?
- **Spec** — code は originating issue / PRD / spec が求めたものを忠実に実装しているか?

両軸は**並列 sub-agent** として実行し、互いの context を汚染しない。次にこの skill が findings を集約する。

issue tracker は提供されているはず — `docs/agents/issue-tracker.md` がなければ `/setup-matt-pocock-skills` を実行する。

## 手順 (Process)

### 1. fixed point の固定 (Pin the fixed point)

ユーザーが指定したものが fixed point — commit SHA、branch 名、tag、`main`、`HEAD~5` など。意見は挟まず、そのまま渡す。指定がなければ確認: "Review against what — a branch, a commit, or `main`?" 得るまで進めない。

diff command を一度取得: `git diff <fixed-point>...HEAD` (three-dot、merge-base との比較)。`git log <fixed-point>..HEAD --oneline` で commit 一覧も記録。

### 2. spec source の特定 (Identify the spec source)

originating spec を次の順で探す:

1. commit message 内の issue 参照 (`#123`、`Closes #45`、GitLab `!67` など) — `docs/agents/issue-tracker.md` の workflow で fetch。
2. ユーザーが引数で渡した path。
3. branch 名や feature に一致する `docs/`、`specs/`、`.scratch/` 下の PRD/spec file。
4. 見つからなければユーザーに spec の場所を確認。ないと言われたら **Spec** sub-agent はスキップし "no spec available" と報告。

### 3. standards source の特定 (Identify the standards sources)

code の書き方を文書化している repo 内のもの。一般的な場所:

- `CLAUDE.md`、`AGENTS.md`
- `CONTRIBUTING.md`
- `CONTEXT.md`、`CONTEXT-MAP.md`、context ごとの `CONTEXT.md` file
- `docs/adr/` (architectural decisions は standards)
- `.editorconfig`、`eslint.config.*`、`biome.json`、`prettier.config.*`、`tsconfig.json` (機械的に強制される standards — 記録するが tooling が既にチェックするものは再チェックしない)
- repo root または `docs/` 下の `STYLE.md`、`STANDARDS.md`、`STYLEGUIDE.md` など

file のリストを収集。**Standards** sub-agent が読む。

### 4. 両 sub-agent を並列起動 (Spawn both sub-agents in parallel)

1 メッセージで 2 つの `Agent` tool call を送る。両方に `general-purpose` subagent を使用。

**Standards sub-agent prompt** — 含めるもの:

- 完全な diff command と commit list。
- step 3 で見つけた standards-source file のリスト。
- brief: "Read the standards docs. Then read the diff. Report — per file/hunk where relevant — every place the diff violates a documented standard. Cite the standard (file + the rule). Distinguish hard violations from judgement calls. Skip anything tooling enforces. Under 400 words."

**Spec sub-agent prompt** — 含めるもの:

- diff command と commit list。
- spec の path または fetch した内容。
- brief: "Read the spec. Then read the diff. Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong. Quote the spec line for each finding. Under 400 words."

spec がない場合、Spec sub-agent をスキップし最終報告に記載。

### 5. 集約 (Aggregate)

2 つの報告を `## Standards` と `## Spec` 見出しの下に、verbatim または軽く整形して提示。findings を merge したり再ランクしない — 2 軸は意図的に分離し、ユーザーが独立して見られるようにする。

最後に 1 行要約: 軸ごとの finding 総数と、最も深刻な単一 issue (あれば) を flag。

## 2 軸の理由 (Why two axes)

変更は 1 軸を通過し別軸で失敗しうる:

- すべての standard に従うが間違ったものを実装 → **Standards pass, Spec fail.**
- issue が求めたことを正確に実装するが project の convention を破る → **Spec pass, Standards fail.**

分離して報告することで、1 軸がもう 1 軸を隠さない。

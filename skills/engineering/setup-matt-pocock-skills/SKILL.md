---
name: setup-matt-pocock-skills
description: Sets up an `## Agent skills` block in AGENTS.md/CLAUDE.md and `docs/agents/` so the engineering skills know this repo's issue tracker (GitHub or local markdown), triage label vocabulary, and domain doc layout. Run before first use of `to-issues`, `to-prd`, `triage`, `diagnose`, `tdd`, `improve-codebase-architecture`, or `zoom-out` — or if those skills appear to be missing context about the issue tracker, triage labels, or domain docs.
disable-model-invocation: true
---

# Matt Pocock の Skills をセットアップ (Setup Matt Pocock's Skills)

engineering skills が前提とする per-repo 設定を scaffold する:

- **Issue tracker** — issue の置き場（デフォルトは GitHub; local markdown も out of the box で対応）
- **Triage labels** — 5 つの canonical triage role に使う文字列
- **Domain docs** — `CONTEXT.md` と ADR の場所、および読み取りルール

これは deterministic script ではなく prompt-driven skill である。探索し、見つけた内容を提示し、ユーザーと確認してから書き込む。

## プロセス (Process)

### 1. 探索 (Explore)

現在の repo を見て開始状態を把握する。存在するものを読む。仮定しない:

- `git remote -v` と `.git/config` — GitHub repo か？ どれか？
- repo ルートの `AGENTS.md` と `CLAUDE.md` — どちらか存在するか？ どちらかに既に `## Agent skills` セクションがあるか？
- repo ルートの `CONTEXT.md` と `CONTEXT-MAP.md`
- `docs/adr/` と `src/*/docs/adr/` ディレクトリ
- `docs/agents/` — この skill の prior output は既にあるか？
- `.scratch/` — local-markdown issue tracker 規約が既に使われている兆候

### 2. 調査結果の提示と質問 (Present findings and ask)

何があるか、何が欠けているかを要約する。次に 3 つの決定を **一度に一つずつ** 案内する — セクションを提示し、ユーザーの回答を得てから次へ。3 つを一度に dump しない。

ユーザーはこれらの term の意味を知らない前提とする。各セクションは短い explainer（それが何か、なぜこれらの skill が必要か、選び方で何が変わるか）で始める。次に選択肢と default を示す。

**Section A — Issue tracker.**

> Explainer: "issue tracker" はこの repo の issue の置き場である。`to-issues`、`triage`、`to-prd`、`qa` などの skill はそこから読み書きする — `gh issue create` を呼ぶか、`.scratch/` 下に markdown file を書くか、またはユーザーが説明する別 workflow に従うかを知る必要がある。この repo で実際に作業を追跡する場所を選ぶ。

Default posture: これらの skill は GitHub 向けに設計されている。`git remote` が GitHub を指していればそれを提案する。`git remote` が GitLab（`gitlab.com` または self-hosted host）を指していれば GitLab を提案する。それ以外（またはユーザーが希望する場合）は次を offer:

- **GitHub** — issue は repo の GitHub Issues にある（`gh` CLI を使用）
- **GitLab** — issue は repo の GitLab Issues にある（[`glab`](https://gitlab.com/gitlab-org/cli) CLI を使用）
- **Local markdown** — issue はこの repo の `.scratch/<feature>/` 下のファイルとして存在（solo project や remote なし repo に適する）
- **Other** (Jira, Linear, etc.) — ユーザーに 1 段落で workflow を説明してもらう; skill は freeform prose として記録する

**Section B — Triage label vocabulary.**

> Explainer: `triage` skill が incoming issue を処理するとき、state machine で進める — needs evaluation、reporter 待ち、AFK agent が pick up 可能、human 向け、または won't fix。そのために、*実際に設定した* 文字列に一致する label（または issue tracker での同等物）を適用する必要がある。repo が別の label 名を使っている場合（例: `needs-triage` の代わりに `bug:triage`）、ここで map し、skill が正しいものを適用し duplicate を作らないようにする。

5 つの canonical role:

- `needs-triage` — maintainer が評価する必要がある
- `needs-info` — reporter を待っている
- `ready-for-agent` — 完全に仕様化、AFK-ready（agent が human context なしで pick up できる）
- `ready-for-human` — 人間による実装が必要
- `wontfix` — 対応しない

Default: 各 role の文字列はその name と等しい。override するかユーザーに確認する。issue tracker に既存 label がなければ default でよい。

**Section C — Domain docs.**

> Explainer: 一部の skill（`improve-codebase-architecture`、`diagnose`、`tdd`）は `CONTEXT.md` でプロジェクトの domain language を学び、`docs/adr/` で過去の architectural decisions を読む。repo が global context を 1 つ持つか複数持つか（例: frontend/backend を分けた monorepo）を知る必要がある。

layout を確認する:

- **Single-context** — repo ルートに 1 つの `CONTEXT.md` + `docs/adr/`。ほとんどの repo はこれ。
- **Multi-context** — ルートに `CONTEXT-MAP.md` があり、per-context の `CONTEXT.md` を指す（典型的には monorepo）。

### 3. 確認と編集 (Confirm and edit)

ユーザーに draft を示す:

- 編集対象の `CLAUDE.md` / `AGENTS.md` に追加する `## Agent skills` block（step 4 の選択ルールを参照）
- `docs/agents/issue-tracker.md`、`docs/agents/triage-labels.md`、`docs/agents/domain.md` の内容

書き込む前に編集させる。

### 4. 書き込み (Write)

**編集するファイルを選ぶ:**

- `CLAUDE.md` が存在すればそれを編集。
- なければ `AGENTS.md` が存在すればそれを編集。
- どちらもなければ、どちらを作成するかユーザーに尋ねる — 勝手に選ばない。

`CLAUDE.md` が既にあるときに `AGENTS.md` を作成しない（逆も同様） — 常に既にある方を編集する。

選択したファイルに `## Agent skills` block が既にあれば、duplicate を append せず in-place で内容を更新する。周辺セクションのユーザー編集は上書きしない。

block:

```markdown
## Agent skills

### Issue tracker

[one-line summary of where issues are tracked]. See `docs/agents/issue-tracker.md`.

### Triage labels

[one-line summary of the label vocabulary]. See `docs/agents/triage-labels.md`.

### Domain docs

[one-line summary of layout — "single-context" or "multi-context"]. See `docs/agents/domain.md`.
```

次に、この skill folder の seed templates を出発点として 3 つの docs file を書く:

- [issue-tracker-github.md](./issue-tracker-github.md) — GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md) — GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md) — local-markdown issue tracker
- [triage-labels.md](./triage-labels.md) — label mapping
- [domain.md](./domain.md) — domain doc consumer rules + layout

"other" issue tracker の場合、ユーザーの説明から scratch で `docs/agents/issue-tracker.md` を書く。

### 5. 完了 (Done)

setup 完了と、どの engineering skills がこれらの file を読むようになったかを伝える。後から `docs/agents/*.md` を直接編集できることも伝える — issue tracker を切り替える、または最初からやり直すときだけこの skill の再実行が必要である。

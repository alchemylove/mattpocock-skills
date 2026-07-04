---
name: setup-matt-pocock-skills
description: engineering skills 向けにこのリポジトリを設定する — issue tracker、triage ラベルの語彙、domain doc のレイアウトをセットアップする。他の engineering skills を初めて使う前に一度実行する。
disable-model-invocation: true
---

# Setup Matt Pocock's Skills

engineering skills が前提とする repo ごとの configuration を scaffold する:

- **Issue tracker** — issue がどこに存在するか（デフォルトは GitHub。local markdown も標準で対応）
- **Triage labels** — 5 つの canonical triage roles に使われる文字列
- **Domain docs** — `CONTEXT.md` と ADR がどこに存在するか、それらを読む consumer rules

これは決定的な script ではなく、prompt-driven な skill である。探索し、見つけたものを提示し、ユーザーと確認し、それから書く。

## Process

### 1. Explore

現在の repo の初期状態を理解するために見る。存在するものは読む。仮定しない:

- `git remote -v` と `.git/config` — これは GitHub の repo か? どの repo か?
- repo root の `AGENTS.md` と `CLAUDE.md` — どちらか存在するか? すでに `## Agent skills` セクションがあるか?
- repo root の `CONTEXT.md` と `CONTEXT-MAP.md`
- `docs/adr/` と、あらゆる `src/*/docs/adr/` ディレクトリ
- `docs/agents/` — この skill の以前の出力がすでに存在するか?
- `.scratch/` — local-markdown な issue tracker の convention がすでに使われている兆候

### 2. Findings を提示し、尋ねる

存在するものと欠けているものを要約する。それから 3 つの決定を**一度に 1 つずつ**ユーザーと進める — 1 つのセクションを提示し、ユーザーの答えを得て、次に進む。3 つを一度に投げない。

ユーザーがこれらの用語の意味を知らないと想定する。各セクションは短い説明（それが何か、なぜこれらの skill に必要か、別の選択をすると何が変わるか）から始める。それから選択肢とデフォルトを示す。

**Section A — Issue tracker。**

> Explainer: "issue tracker" とは、この repo の issue が存在する場所である。`to-issues`、`triage`、`to-prd`、`qa` のような skill はそこから読み書きする — `gh issue create` を呼ぶべきか、`.scratch/` 配下に markdown ファイルを書くべきか、あるいはあなたが説明する別の workflow に従うべきかを知る必要がある。この repo で実際に作業を追跡している場所を選ぶ。

デフォルトの姿勢: これらの skill は GitHub 向けに設計されている。`git remote` が GitHub を指していれば、それを提案する。`git remote` が GitLab（`gitlab.com` または self-hosted host）を指していれば、GitLab を提案する。それ以外の場合（またはユーザーが望む場合）、以下を提示する:

- **GitHub** — issue は repo の GitHub Issues に存在する（`gh` CLI を使う）
- **GitLab** — issue は repo の GitLab Issues に存在する（[`glab`](https://gitlab.com/gitlab-org/cli) CLI を使う）
- **Local markdown** — issue はこの repo 内の `.scratch/<feature>/` 配下のファイルとして存在する（ソロプロジェクトや remote の無い repo に向く）
- **Other**（Jira、Linear など）— ユーザーに workflow を 1 段落で説明してもらう。skill はそれを自由形式のプローズとして記録する

ユーザーが **GitHub** または **GitLab** を選んだ場合、かつその場合のみ、1 つ follow-up を尋ねる:

> Explainer: オープンソースの repo はしばしば、issue だけでなく pull request として feature request を受け取る — PR はコードが添付された issue である。これを有効にすると、`/triage` は *external* な PR を同じキューに引き込み、issue と同じ label と state に通す（collaborator の作業中の PR には手を触れない）。PR があなたにとって request surface でないなら off のままにする。

- **PRs as a request surface** — yes / no（デフォルト: no）。答えを `docs/agents/issue-tracker.md` に記録する。local-markdown やその他の tracker では、この質問はスキップする — PR が存在しないため。

**Section B — Triage label vocabulary。**

> Explainer: `triage` skill が受信した issue を処理するとき、それを state machine に通す — 評価が必要、reporter からの返答待ち、AFK agent が着手する準備ができている、人間の対応が必要、または対応しない。そのためには、あなたが*実際に設定した*文字列に一致する label（またはあなたの issue tracker における同等のもの）を適用する必要がある。あなたの repo がすでに異なる label 名を使っているなら（例えば `needs-triage` の代わりに `bug:triage`）、ここでマッピングすることで skill は重複を作らず正しいものを適用する。

5 つの canonical roles:

- `needs-triage` — maintainer が評価する必要がある
- `needs-info` — reporter からの返答待ち
- `ready-for-agent` — 完全に specified され、AFK-ready（agent が人間の context 無しで着手できる）
- `ready-for-human` — 人間による実装が必要
- `wontfix` — 対応しない

デフォルト: 各 role の文字列はその名前と等しい。上書きしたいものがあるかユーザーに尋ねる。issue tracker に既存の label が無ければ、デフォルトのままで問題ない。

**Section C — Domain docs。**

> Explainer: 一部の skill（`improve-codebase-architecture`、`diagnosing-bugs`、`tdd`）はプロジェクトの domain language を学ぶために `CONTEXT.md` ファイルを、過去の architectural decision のために `docs/adr/` を読む。正しい場所を探せるよう、repo が単一の global context を持つのか、複数持つのか（例えばフロントエンド/バックエンドで別々の context を持つ monorepo）を知る必要がある。

layout を確認する:

- **Single-context** — repo root に 1 つの `CONTEXT.md` + `docs/adr/`。ほとんどの repo はこれに当てはまる。
- **Multi-context** — root の `CONTEXT-MAP.md` が context ごとの `CONTEXT.md` ファイルを指す（典型的には monorepo）。

### 3. 確認して編集する

ユーザーに以下の draft を見せる:

- `CLAUDE.md` / `AGENTS.md` のどちらを編集するにせよ追加する `## Agent skills` block（選択ルールは手順 4 を参照）
- `docs/agents/issue-tracker.md`、`docs/agents/triage-labels.md`、`docs/agents/domain.md` の内容

書き込む前に編集させる。

### 4. Write

**編集するファイルを選ぶ:**

- `CLAUDE.md` が存在すれば、それを編集する。
- そうでなく `AGENTS.md` が存在すれば、それを編集する。
- どちらも存在しなければ、どちらを作成するかユーザーに尋ねる — 勝手に選ばない。

`CLAUDE.md` がすでに存在するときに `AGENTS.md` を新規作成しない（逆も同様）— 常にすでにある方を編集する。

選ばれたファイルにすでに `## Agent skills` block が存在するなら、重複を追記するのではなく、その内容をその場で更新する。周囲のセクションへのユーザーの編集を上書きしない。

block の内容:

```markdown
## Agent skills

### Issue tracker

[one-line summary of where issues are tracked, plus whether external PRs are a triage surface]. See `docs/agents/issue-tracker.md`.

### Triage labels

[one-line summary of the label vocabulary]. See `docs/agents/triage-labels.md`.

### Domain docs

[one-line summary of layout — "single-context" or "multi-context"]. See `docs/agents/domain.md`.
```

それから、この skill フォルダ内の seed template を出発点として 3 つの docs ファイルを書く:

- [issue-tracker-github.md](./issue-tracker-github.md) — GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md) — GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md) — local-markdown issue tracker
- [triage-labels.md](./triage-labels.md) — label mapping
- [domain.md](./domain.md) — domain doc consumer rules + layout

「other」な issue tracker の場合、ユーザーの説明を使ってゼロから `docs/agents/issue-tracker.md` を書く。

### 5. Done

セットアップが完了したこと、どの engineering skills がこれらのファイルから読むようになるかをユーザーに伝える。`docs/agents/*.md` は後で直接編集できることに触れる — この skill を再実行する必要があるのは、issue tracker を切り替えたい、あるいはゼロからやり直したいときだけである。

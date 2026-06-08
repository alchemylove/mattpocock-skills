---
name: qa
description: Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explores the codebase in the background for context and domain language. Use when user wants to report bugs, do QA, file issues conversationally, or mentions "QA session".
---

# QA セッション (QA Session)

対話型 QA セッションを実行する。ユーザーが遭遇した問題を説明する。明確化し、コンテキストのために codebase を調査し、永続的でユーザー中心かつ project の domain language を使った GitHub issue を作成する。

## ユーザーが提起する各 issue について (For each issue the user raises)

### 1. 傾聴と軽い明確化 (Listen and lightly clarify)

ユーザーが自分の言葉で問題を説明できるようにする。**最大 2–3 の短い明確化質問**に絞る:

- 期待したこと vs 実際に起きたこと
- 再現手順 (自明でなければ)
- 一貫しているか、断続的か

過度にインタビューしない。issue を作成するのに十分明確なら次へ進む。

### 2. バックグラウンドで codebase を調査 (Explore the codebase in the background)

ユーザーと会話しながら、関連領域を理解するために Agent (subagent_type=Explore) をバックグラウンドで起動する。目的は fix を見つけることではない — 次を行うこと:

- その領域で使われる domain language を学ぶ (UBIQUITOUS_LANGUAGE.md を確認)
- feature が本来何をするべきかを理解する
- ユーザー向けの振る舞いの境界を特定する

このコンテキストはより良い issue の作成に役立つ — ただし issue 自体は特定の file、行番号、内部実装の詳細を参照してはならない。

### 3. スコープの評価: 単一 issue か分解か? (Assess scope: single issue or breakdown?)

作成前に、これが**単一 issue**か**複数 issue への分解**が必要かを判断する。

分解する場合:

- fix が複数の独立した領域にまたがる (例: "form validation が誤っている AND success message が欠けている AND redirect が壊れている")
- 明確に分離可能な関心事があり、異なる人が並行して取り組める
- ユーザーが複数の独立した failure mode や症状を説明している

単一 issue のままにする場合:

- 一箇所で一つの振る舞いが誤っている
- 症状がすべて同じ root behavior によるもの

### 4. GitHub issue の作成 (File the GitHub issue(s))

`gh issue create` で issue を作成する。事前にユーザーにレビューを求めない — 作成して URL を共有する。

issue は**永続的**であること — 大規模な refactor 後も意味が通じること。ユーザーの視点で書く。

#### 単一 issue の場合 (For a single issue)

このテンプレートを使用:

```
## What happened

[Describe the actual behavior the user experienced, in plain language]

## What I expected

[Describe the expected behavior]

## Steps to reproduce

1. [Concrete, numbered steps a developer can follow]
2. [Use domain terms from the codebase, not internal module names]
3. [Include relevant inputs, flags, or configuration]

## Additional context

[Any extra observations from the user or from codebase exploration that help frame the issue — e.g. "this only happens when using the Docker layer, not the filesystem layer" — use domain language but don't cite files]
```

#### 分解の場合 (複数 issue) (For a breakdown (multiple issues))

依存順 (blocker を先に) で issue を作成し、実際の issue 番号を参照できるようにする。

各 sub-issue にこのテンプレートを使用:

```
## Parent issue

#<parent-issue-number> (if you created a tracking issue) or "Reported during QA session"

## What's wrong

[Describe this specific behavior problem — just this slice, not the whole report]

## What I expected

[Expected behavior for this specific slice]

## Steps to reproduce

1. [Steps specific to THIS issue]

## Blocked by

- #<issue-number> (if this issue can't be fixed until another is resolved)

Or "None — can start immediately" if no blockers.

## Additional context

[Any extra observations relevant to this slice]
```

分解を作成する際:

- **少数の厚い issue より多数の薄い issue を優先** — 各 issue は独立して fix と検証が可能であること
- **blocking 関係を正直に記載** — issue B が issue A の fix までテストできないならそう書く。独立なら両方 "None — can start immediately"
- **依存順で issue を作成**し、"Blocked by" で実際の issue 番号を参照できるようにする
- **並行性を最大化** — 複数の人 (または agent) が異なる issue を同時に取れることが目標

#### すべての issue body のルール (Rules for all issue bodies)

- **file path や行番号は含めない** — すぐに古くなる
- **project の domain language を使う** (UBIQUITOUS_LANGUAGE.md があれば確認)
- **code ではなく振る舞いを記述** — "applyPatch() throws on line 42" ではなく "sync service が patch を適用できない"
- **再現手順は必須** — 特定できなければユーザーに確認
- **簡潔に** — developer が 30 秒で読めること

作成後、すべての issue URL (blocking 関係の要約付き) を表示し確認: "Next issue, or are we done?"

### 5. セッションの継続 (Continue the session)

ユーザーが終了と言うまで続ける。各 issue は独立 — batch しない。

---
name: to-prd
description: 現在の会話を PRD に変換し、プロジェクトの issue tracker に公開する — インタビューはなく、すでに議論した内容をまとめるだけ。
disable-model-invocation: true
---

この skill は現在の会話の context と codebase の理解を取り、PRD を生成する。ユーザーにインタビューしては**いけない** — すでに知っていることを synthesize するだけである。

issue tracker と triage label の vocabulary はすでにあなたに提供されているはずである — なければ `/setup-matt-pocock-skills` を実行する。

## Process

1. まだ探索していなければ、repo を探索して codebase の現在の状態を理解する。PRD 全体を通してプロジェクトの domain glossary の vocabulary を使い、触れる領域のあらゆる ADR を尊重する。

2. feature をテストする予定の seam を描き出す。新しい seam よりも既存の seam を優先すべきである。可能な限り最も高い位置の seam を使う。新しい seam が必要なら、可能な限り高い位置で提案する。codebase 全体で seam は少ないほど良い — 理想の数は 1 つである。

これらの seam がユーザーの期待と一致するか確認する。

3. 下記の template を使って PRD を書き、プロジェクトの issue tracker に公開する。`ready-for-agent` の triage label を適用する — 追加の triage は不要。

<prd-template>

## Problem Statement

ユーザーが直面している問題を、ユーザーの視点から。

## Solution

問題への解決策を、ユーザーの視点から。

## User Stories

user story の LONG（長く）番号付きのリスト。各 user story は以下の形式にする:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

この user story のリストは極めて網羅的で、feature のあらゆる側面をカバーすべきである。

## Implementation Decisions

行われた implementation decision のリスト。以下を含みうる:

- 構築/変更される module
- 変更されるそれらの module の interface
- developer からの技術的な明確化
- architectural decision
- Schema の変更
- API contract
- 具体的なやり取り

具体的なファイルパスやコードスニペットは含め**ない**。すぐに古くなる可能性がある。

例外: prototype が prose よりも正確に決定事項をエンコードするスニペット（state machine、reducer、schema、type shape）を生み出した場合、関連する decision の中に inline し、prototype 由来であることを簡潔に記す。決定事項が詰まった部分だけに削る — 動く demo ではなく、重要な部分だけ。

## Testing Decisions

行われた testing decision のリスト。以下を含める:

- 良いテストとは何かの description（external behavior のみをテストし、implementation の詳細はテストしない）
- どの module がテストされるか
- テストの prior art（つまり codebase 内の似た種類のテスト）

## Out of Scope

この PRD の対象外である事柄の description。

## Further Notes

feature に関するその他のメモ。

</prd-template>

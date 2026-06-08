---
name: to-prd
description: Turn the current conversation context into a PRD and publish it to the project issue tracker. Use when user wants to create a PRD from the current context.
---

この skill は現在の会話コンテキストと codebase understanding を取り、PRD を作成する。ユーザーへのインタビューはしない — 既に知っていることを synthesize するだけ。

issue tracker と triage label vocabulary は提供されているはず — なければ `/setup-matt-pocock-skills` を実行する。

## プロセス (Process)

1. まだでなければ repo を探索し、codebase の現状を理解する。PRD 全体でプロジェクトの domain glossary 語彙を使い、触る領域の ADR を尊重する。

2. 実装完了に必要な主要 module の sketch を描く。isolation で test できる deep module を抽出する機会を積極的に探す。

deep module（shallow module とは対照的）は、多くの functionality を rare に変わる simple で testable な interface に encapsulate するものである。

これらの module がユーザーの期待と一致するか確認する。どの module に test を書くかユーザーと確認する。

3. 下記 template で PRD を書き、issue tracker に公開する。`ready-for-agent` triage label を適用 — 追加 triage は不要。

<prd-template>

## Problem Statement

ユーザー視点での、ユーザーが直面している問題。

## Solution

ユーザー視点での、問題への解決策。

## User Stories

長い番号付き user stories のリスト。各 user story の形式:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

この user stories リストは極めて広範で、機能のあらゆる側面をカバーすべきである。

## Implementation Decisions

下された implementation decisions のリスト。含めうるもの:

- 構築・変更する module
- 変更する module の interface
- developer からの technical clarifications
- architectural decisions
- schema changes
- API contracts
- specific interactions

特定の file path や code snippet は含めない。すぐ outdated になりうる。

例外: prototype が prose より正確に decision を encode した snippet（state machine、reducer、schema、type shape）を出した場合、関連する decision 内に inline し、prototype 由来であることを簡潔に記す。decision-rich な部分だけに trim — working demo ではなく重要な部分だけ。

## Testing Decisions

下された testing decisions のリスト。含めるもの:

- good test の定義（external behaviour のみ test し、implementation details は test しない）
- test する module
- test の prior art（codebase 内の類似 test）

## Out of Scope

この PRD の out of scope であるものの説明。

## Further Notes

機能に関するその他のメモ。

</prd-template>

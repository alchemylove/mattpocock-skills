---
name: to-issues
description: Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. Use when user wants to convert a plan into issues, create implementation tickets, or break down work into issues.
---

# Issue 化 (To Issues)

tracer bullet の vertical slice を使い、プランを independently-grabbable な issue に分解する。

issue tracker と triage label vocabulary は提供されているはず — なければ `/setup-matt-pocock-skills` を実行する。

## プロセス (Process)

### 1. コンテキスト収集 (Gather context)

会話コンテキストにあるものから作業する。ユーザーが issue reference（issue number、URL、path）を引数で渡した場合、issue tracker から fetch し、body と comments 全体を読む。

### 2. コードベース探索（任意）(Explore the codebase (optional))

まだコードベースを探索していなければ、コードの現状を理解するために探索する。issue の title と description はプロジェクトの domain glossary 語彙を使い、触る領域の ADR を尊重する。

### 3. vertical slice の草案 (Draft vertical slices)

プランを **tracer bullet** issue に分解する。各 issue は 1 層の horizontal slice ではなく、すべての integration layer を end-to-end で貫く薄い vertical slice である。

slice は 'HITL' または 'AFK' のいずれか。HITL slice は architectural decision や design review など human interaction が必要。AFK slice は human interaction なしで実装・merge できる。可能なら HITL より AFK を優先する。

<vertical-slice-rules>
- 各 slice はすべての層（schema、API、UI、tests）を通る狭いが COMPLETE な path を届ける
- 完了した slice は単体で demo 可能または verifiable
- 少数の厚い slice より多数の薄い slice を優先
</vertical-slice-rules>

### 4. ユーザーへの確認 (Quiz the user)

提案した breakdown を番号付きリストで提示する。各 slice について示す:

- **Title**: 短い説明的な名前
- **Type**: HITL / AFK
- **Blocked by**: 先に完了が必要な他 slice（あれば）
- **User stories covered**: この slice が対応する user stories（ソース資料にある場合）

ユーザーに尋ねる:

- 粒度は適切か？（too coarse / too fine）
- 依存関係は正しいか？
- merge またはさらに split すべき slice はあるか？
- HITL と AFK のマークは正しいか？

ユーザーが breakdown を承認するまで反復する。

### 5. issue tracker へ issue を公開 (Publish the issues to the issue tracker)

承認された各 slice について、issue tracker に新規 issue を公開する。下記の issue body template を使う。これらの issue は AFK agent 向け ready とみなすため、指示がなければ正しい triage label で公開する。

"Blocked by" で実際の issue identifier を参照できるよう、依存順（blocker 先）で issue を公開する。

<issue-template>
## Parent

issue tracker 上の parent issue への参照（ソースが既存 issue なら。なければこのセクションを省略）。

## What to build

この vertical slice の簡潔な説明。層ごとの implementation ではなく end-to-end behaviour を記述する。

特定の file path や code snippet は避ける — すぐ stale になる。例外: prototype が prose より正確に decision を encode した snippet（state machine、reducer、schema、type shape）を出した場合、ここに inline し、prototype 由来であることを簡潔に記す。decision-rich な部分だけに trim — working demo ではなく重要な部分だけ。

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Blocked by

- blocking ticket への参照（あれば）

blocker がなければ "None - can start immediately"。

</issue-template>

parent issue を close または変更しないこと。

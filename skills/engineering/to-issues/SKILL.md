---
name: to-issues
description: plan、spec、または PRD を、tracer-bullet の vertical slice を使って、プロジェクトの issue tracker 上で独立して着手可能な issue に分解する。
disable-model-invocation: true
---

# To Issues

vertical slices（tracer bullets）を使って、plan を独立して着手可能な issue に分解する。

issue tracker と triage label の vocabulary はすでにあなたに提供されているはずである — なければ `/setup-matt-pocock-skills` を実行する。

## Process

### 1. context を集める

すでに会話の context にあるものから作業する。ユーザーが issue の参照（issue 番号、URL、パス）を引数として渡した場合、issue tracker から取得し、その本文と comment を全文読む。

### 2. codebase を探索する（任意）

まだ codebase を探索していなければ、コードの現在の状態を理解するために探索する。issue のタイトルと description はプロジェクトの domain glossary の vocabulary を使い、触れる領域の ADR を尊重する。

implementation を容易にするための prefactor の機会を探す。「変更を簡単にし、それから簡単な変更をする」。

### 3. vertical slices を下書きする

plan を **tracer bullet** issue に分解する。各 issue は 1 つの layer の水平な slice ではなく、すべての integration layer をエンドツーエンドで貫く薄い vertical slice である。

<vertical-slice-rules>

- 各 slice は狭いが、すべての layer（schema、API、UI、テスト）を貫く COMPLETE な経路を届ける
- 完了した slice は単体で demo 可能または検証可能である
- prefactoring はすべて先に行う

</vertical-slice-rules>

### 4. ユーザーに問う

提案した分解を番号付きリストとして提示する。各 slice について以下を示す:

- **Title**: 短く説明的な名前
- **Blocked by**: 先に完了しなければならない他の slice（あれば）
- **User stories covered**: この slice が対応する user story（元の資料にあれば）

ユーザーに尋ねる:

- 粒度は適切に感じるか?（粗すぎる / 細かすぎる）
- 依存関係は正しいか?
- いずれかの slice をマージまたはさらに分割すべきか?

ユーザーが分解を承認するまで繰り返す。

### 5. issue を issue tracker に公開する

承認された各 slice について、issue tracker に新しい issue を公開する。下記の issue body template を使う。これらの issue は AFK agent 向けに準備が整っているとみなされるため、指示がない限り正しい triage label を付けて公開する。

依存関係の順（blocker を先に）で issue を公開し、「Blocked by」欄で実際の issue identifier を参照できるようにする。

<issue-template>
## Parent

issue tracker 上の parent issue への参照（元が既存の issue だった場合。そうでなければこのセクションは省略する）。

## What to build

この vertical slice の簡潔な description。layer ごとの implementation ではなく、end-to-end の behavior を記述する。

具体的なファイルパスやコードスニペットは避ける — すぐに古くなる。例外: prototype が prose よりも正確に決定事項をエンコードするスニペット（state machine、reducer、schema、type shape）を生み出した場合、ここに inline し、prototype 由来であることを簡潔に記す。決定事項が詰まった部分だけに削る — 動く demo ではなく、重要な部分だけ。

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Blocked by

- blocking ticket への参照（あれば）

blocker が無ければ "None - can start immediately" とする。

</issue-template>

parent issue を close したり変更したりしない。

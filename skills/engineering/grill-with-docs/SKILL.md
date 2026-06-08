---
name: grill-with-docs
description: Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. Use when user wants to stress-test a plan against their project's language and documented decisions.
---

<what-to-do>

このプランのあらゆる側面について、共有理解に到達するまで容赦なくインタビューすること。設計ツリーの各ブランチを辿り、意思決定間の依存を一つずつ解決する。各質問について、推奨回答を提示すること。

質問は一度に一つずつ行い、各質問へのフィードバックを待ってから続けること。

質問がコードベースの探索で答えられる場合は、代わりにコードベースを探索すること。

</what-to-do>

<supporting-info>

## ドメイン認識 (Domain awareness)

コードベース探索中、既存ドキュメントも探すこと:

### ファイル構造 (File structure)

ほとんどの repo は単一 context を持つ:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

ルートに `CONTEXT-MAP.md` がある場合、repo は複数 context を持つ。map は各 context の場所を示す:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← context-specific decisions
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/
```

ファイルは lazy に作成する — 書く内容があるときだけ。`CONTEXT.md` がなければ、最初の term が解決されたときに作成する。`docs/adr/` がなければ、最初の ADR が必要になったときに作成する。

## セッション中 (During the session)

### 用語集に照らして挑戦する (Challenge against the glossary)

ユーザーが `CONTEXT.md` の既存言語と矛盾する term を使ったら、即座に指摘する。「用語集では 'cancellation' を X と定義しているが、Y の意味に見える — どちらか？」

### 曖昧な言語を鋭くする (Sharpen fuzzy language)

ユーザーが vague または overloaded な term を使ったら、正確な canonical term を提案する。「'account' と言っている — Customer と User のどちらか？ それらは別物だ。」

### 具体シナリオを議論する (Discuss concrete scenarios)

domain の関係を議論するとき、具体シナリオで stress-test する。edge case を探るシナリオを考案し、概念間の境界についてユーザーに正確さを求める。

### コードと照合する (Cross-reference with code)

ユーザーが動作の説明をしたら、コードが一致するか確認する。矛盾があれば surface する:「コードは Order 全体を cancel するが、さきほど partial cancellation が可能と言った — どちらが正しいか？」

### CONTEXT.md をインラインで更新する (Update CONTEXT.md inline)

term が解決したら、その場で `CONTEXT.md` を更新する。まとめて batch しない — 起きた瞬間に capture する。[CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md) の形式を使う。

`CONTEXT.md` は implementation details を一切含めてはならない。`CONTEXT.md` を spec、scratch pad、implementation decisions の置き場として扱わない。用語集であり、それ以外ではない。

### ADR は控えめに提案する (Offer ADRs sparingly)

次の 3 つすべてが真のときだけ ADR 作成を提案する:

1. **Hard to reverse** — 後から考えを変えるコストが meaningful である
2. **Surprising without context** — 将来の読者が「なぜこうしたのか？」と思う
3. **The result of a real trade-off** — 本物の代替案があり、特定の理由で 1 つを選んだ

3 つのいずれかが欠けていれば ADR を skip する。[ADR-FORMAT.md](./ADR-FORMAT.md) の形式を使う。

</supporting-info>

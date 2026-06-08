# ドメインドキュメント (Domain Docs)

engineering skills が codebase を探索するとき、この repo の domain documentation をどう消費すべきか。

## 探索前に読むもの (Before exploring, read these)

- repo ルートの **`CONTEXT.md`**、または
- 存在すれば repo ルートの **`CONTEXT-MAP.md`** — context ごとの `CONTEXT.md` を指す。トピックに関連するものをそれぞれ読む。
- **`docs/adr/`** — これから作業する領域に触れる ADR を読む。multi-context repo では `src/<context>/docs/adr/` も context-scoped decisions を確認。

これらのファイルが存在しなくても、**黙って続行**。欠如を指摘しない。最初から作成を提案しない。producer skill（`/grill-with-docs`）が用語や決定が実際に解決されたとき lazy に作成する。

## ファイル構造 (File structure)

Single-context repo（ほとんどの repo）:

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

Multi-context repo（ルートに `CONTEXT-MAP.md` がある）:

```
/
├── CONTEXT-MAP.md
├── docs/adr/                          ← system-wide decisions
└── src/
    ├── ordering/
    │   ├── CONTEXT.md
    │   └── docs/adr/                  ← context-specific decisions
    └── billing/
        ├── CONTEXT.md
        └── docs/adr/
```

## glossary の語彙を使う (Use the glossary's vocabulary)

出力で domain concept に名前を付けるとき（issue title、refactor proposal、hypothesis、test name）、`CONTEXT.md` で定義された用語を使う。glossary が明示的に避ける同義語に drift しない。

必要な概念が glossary にまだないなら、それはシグナル — プロジェクトが使わない language を発明している（再考）か、本当の gap がある（`/grill-with-docs` 向けにメモ）。

## ADR 衝突をフラグする (Flag ADR conflicts)

出力が既存 ADR と矛盾するなら、黙って上書きせず明示的に surface する:

> _Contradicts ADR-0007 (event-sourced orders) — but worth reopening because…_

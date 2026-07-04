# Domain Docs

engineering skills が codebase を探索する際、この repo の domain documentation をどう消費すべきか。

## 探索の前にこれらを読む

- repo root の **`CONTEXT.md`**、または
- 存在すれば repo root の **`CONTEXT-MAP.md`** — context ごとの `CONTEXT.md` を指す。トピックに関連するものをそれぞれ読む。
- **`docs/adr/`** — これから触れる領域に関わる ADR を読む。multi-context な repo では、context に限定された決定のために `src/<context>/docs/adr/` も確認する。

これらのファイルのいずれかが存在しなくても、**黙って進める**。無いことを指摘したり、先回りして作成を提案したりしない。`/domain-modeling` skill（`/grill-with-docs` と `/improve-codebase-architecture` から到達する）が、用語や決定が実際に解決したときに遅延生成する。

## File structure

Single-context な repo（ほとんどの repo）:

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

Multi-context な repo（root に `CONTEXT-MAP.md` が存在する）:

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

## glossary の vocabulary を使う

出力が domain concept に言及するとき（issue のタイトル、refactor の提案、hypothesis、テスト名）、`CONTEXT.md` で定義された用語を使う。glossary が明示的に避けている同義語に流れない。

必要な concept がまだ glossary に無ければ、それは signal である — プロジェクトが使わない言葉を発明しているか（考え直す）、あるいは本物の gap があるか（`/domain-modeling` のためにメモしておく）。

## ADR との衝突を flag する

出力が既存の ADR と矛盾する場合、黙って上書きするのではなく明示的に表に出す:

> _Contradicts ADR-0007 (event-sourced orders) — but worth reopening because…_
> 「ADR-0007（event-sourced orders）と矛盾するが、〜という理由で再検討する価値がある」

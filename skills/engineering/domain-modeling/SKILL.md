---
name: domain-modeling
description: プロジェクトの domain model を構築・洗練する。ユーザーが domain の用語や ubiquitous language を明確にしたい、architectural decision を記録したい、または他の skill が domain model を維持する必要があるときに使う。
---

# Domain Modeling

設計しながらプロジェクトの domain model を能動的に構築・洗練する。これは *active* な discipline である — 用語に異議を唱え、edge-case のシナリオを考案し、glossary と決定事項をそれが固まった瞬間に書き留める。（vocabulary のために `CONTEXT.md` を単に*読む*だけなら、この skill ではない — それはどの skill でもできる 1 行の習慣に過ぎない。この skill はモデルを単に消費するのではなく、変更しているときのためのものである。）

## File structure

ほとんどの repo は単一の context を持つ:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

root に `CONTEXT-MAP.md` が存在すれば、repo は複数の context を持つ。map はそれぞれがどこに存在するかを指す:

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

ファイルは遅延生成する — 書くべきものがあるときだけ。`CONTEXT.md` が存在しなければ、最初の用語が解決したときに作成する。`docs/adr/` が存在しなければ、最初の ADR が必要になったときに作成する。

## During the session

### glossary に照らして異議を唱える

ユーザーが `CONTEXT.md` の既存の言葉と矛盾する用語を使ったら、即座に指摘する。「あなたの glossary は 'cancellation' を X と定義していますが、Y を意味しているようです — どちらですか?」

### 曖昧な言葉を研ぎ澄ます

ユーザーが曖昧または overloaded な用語を使ったら、正確な canonical term を提案する。「'account' と言っていますが、Customer と User のどちらを意味していますか? それらは別のものです。」

### 具体的なシナリオを議論する

domain の関係が議論されているとき、具体的なシナリオでそれらを stress-test する。edge case を探るシナリオを考案し、ユーザーに concept 間の境界について正確であることを強いる。

### コードと突き合わせる

ユーザーが何かの動作を述べたら、コードがそれと一致するか確認する。矛盾を見つけたら、それを表に出す: 「あなたのコードは Order 全体をキャンセルしますが、たった今 partial cancellation が可能だと言いましたね — どちらが正しいですか?」

### CONTEXT.md をその場で更新する

用語が解決したら、その場で `CONTEXT.md` を更新する。まとめて後回しにせず、起きたその場でキャプチャする。[CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md) の形式を使う。

`CONTEXT.md` は implementation の詳細を完全に排除すべきである。`CONTEXT.md` を spec、scratch pad、あるいは implementation decision の保管庫として扱わない。これは glossary であり、それ以外の何物でもない。

### ADR は控えめに提案する

以下の 3 つすべてが真であるときにのみ ADR の作成を提案する:

1. **Hard to reverse** — 後で考えを変えるコストが無視できない
2. **Surprising without context** — 将来の読者が「なぜこのようにしたのか?」と疑問に思うだろう
3. **The result of a real trade-off** — 本物の代替案があり、特定の理由で 1 つを選んだ

3 つのうちどれか 1 つでも欠けていれば、ADR はスキップする。[ADR-FORMAT.md](./ADR-FORMAT.md) の形式を使う。

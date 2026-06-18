# ADR フォーマット (ADR Format)

ADR は `docs/adr/` に置き、連番で命名する: `0001-slug.md`、`0002-slug.md` など。

`docs/adr/` ディレクトリは lazy に作成する — 最初の ADR が必要になったときだけ。

## テンプレート (Template)

```md
# {Short title of the decision}

{1-3 sentences: what's the context, what did we decide, and why.}
```

以上。ADR は 1 段落で十分。価値はセクションを埋めることではなく、決定が行われたことと *why* を記録することにある。

## 任意セクション (Optional sections)

本当に価値があるときだけ含める。多くの ADR では不要。

- **Status** frontmatter（`proposed | accepted | deprecated | superseded by ADR-NNNN`）— 決定を再検討するときに有用
- **Considered Options** — 却下した代替案を覚えておく価値があるときだけ
- **Consequences** — 自明でない下流の影響を明示する必要があるときだけ

## 採番 (Numbering)

`docs/adr/` の既存の最大番号を確認し、1 つ増やす。

## ADR を提案するタイミング (When to offer an ADR)

次の 3 つすべてが真であること:

1. **Hard to reverse** — 後から考えを変えるコストが意味ある
2. **Surprising without context** — 将来の読者がコードを見て「なぜこんなことを?」と思う
3. **The result of a real trade-off** — 本当の代替案があり、特定の理由で 1 つを選んだ

決定が簡単に取り消せるならスキップ — 取り消せばよい。驚きがなければ誰も理由を問わない。本当の代替がなければ「当たり前のことをした」以上に記録するものはない。

### 該当するもの (What qualifies)

- **Architectural shape.** 「monorepo を使う。」「write model は event-sourced、read model は Postgres に project する。」
- **Integration patterns between contexts.** 「Ordering と Billing は synchronous HTTP ではなく domain events で通信する。」
- **Technology choices that carry lock-in.** Database、message bus、auth provider、deployment target。すべての library ではなく、入れ替えに四半期かかるものだけ。
- **Boundary and scope decisions.** 「Customer data は Customer context が所有し、他 context は ID のみで参照する。」明示的な no は yes と同じくらい価値がある。
- **Deliberate deviations from the obvious path.** 「X のため ORM ではなく manual SQL を使う。」合理的な読者が逆を想定するもの。次のエンジニアが意図的なものを「修正」しようとするのを防ぐ。
- **Constraints not visible in the code.** 「compliance 要件のため AWS は使えない。」「partner API contract のため response time は 200ms 未満である必要がある。」
- **Rejected alternatives when the rejection is non-obvious.** GraphQL を検討して subtle な理由で REST を選んだなら記録する — さもなければ 6 か月後にまた GraphQL が提案される。

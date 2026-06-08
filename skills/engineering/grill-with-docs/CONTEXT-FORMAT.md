# CONTEXT.md フォーマット (CONTEXT.md Format)

## 構造 (Structure)

```md
# {Context Name}

{One or two sentence description of what this context is and why it exists.}

## Language

**Order**:
{A one or two sentence description of the term}
_Avoid_: Purchase, transaction

**Invoice**:
A request for payment sent to a customer after delivery.
_Avoid_: Bill, payment request

**Customer**:
A person or organization that places orders.
_Avoid_: Client, buyer, account
```

## ルール (Rules)

- **Be opinionated.** 同じ概念に複数の語があるとき、最良の 1 つを選び、他は避けるべき alias として列挙する。
- **Flag conflicts explicitly.** 用語が曖昧に使われているなら、「Flagged ambiguities」で明示し、明確な解決を示す。
- **Keep definitions tight.** 最大 1〜2 文。何をするかではなく、何であるかを定義する。
- **Show relationships.** bold の用語名を使い、明らかなところでは cardinality を表現する。
- **Only include terms specific to this project's context.** 一般的な programming concepts（timeouts、error types、utility patterns）は、プロジェクトで広く使っていても含めない。用語を追加する前に問う: これはこの context 固有の概念か、一般的な programming concept か? 前者だけが該当する。
- **Group terms under subheadings** — 自然なクラスタが現れたとき。すべての用語が 1 つのまとまった領域に属するなら、フラットなリストでよい。
- **Write an example dialogue.** dev と domain expert の会話で、用語が自然にどう相互作用するか、関連概念の境界がどう明確になるかを示す。

## 単一 context と複数 context の repo (Single vs multi-context repos)

**Single context（ほとんどの repo）:** repo ルートに 1 つの `CONTEXT.md`。

**Multiple contexts:** repo ルートに `CONTEXT-MAP.md` を置き、contexts、所在、相互関係を列挙する:

```md
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) — receives and tracks customer orders
- [Billing](./src/billing/CONTEXT.md) — generates invoices and processes payments
- [Fulfillment](./src/fulfillment/CONTEXT.md) — manages warehouse picking and shipping

## Relationships

- **Ordering → Fulfillment**: Ordering emits `OrderPlaced` events; Fulfillment consumes them to start picking
- **Fulfillment → Billing**: Fulfillment emits `ShipmentDispatched` events; Billing consumes them to generate invoices
- **Ordering ↔ Billing**: Shared types for `CustomerId` and `Money`
```

skill はどちらの構造かを推論する:

- `CONTEXT-MAP.md` があれば、読んで contexts を特定
- ルートの `CONTEXT.md` だけなら single context
- どちらもなければ、最初の用語が解決されたとき lazy にルート `CONTEXT.md` を作成

複数 context があるとき、現在のトピックに関連する context を推論する。不明なら質問する。

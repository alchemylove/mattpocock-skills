# CONTEXT.md Format

## Structure

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

## Rules

- **意見を持つ。** 同じ concept に複数の語が存在するなら、最良のものを選び、残りを `_Avoid_` の下に列挙する。
- **定義を簡潔に保つ。** 最大でも 1〜2 文。それが何を「する」かではなく、何で「ある」かを定義する。
- **このプロジェクトの context に固有の用語だけを含める。** 一般的なプログラミングの concept（timeout、error type、utility pattern）は、プロジェクトがそれらを頻繁に使っていても含まない。用語を追加する前に問う: これはこの context 固有の concept か、それとも一般的なプログラミングの concept か? 前者だけが含まれるべきである。
- 自然な集まりが現れたら**サブ見出しの下に用語をグループ化する**。すべての用語が単一のまとまった領域に属するなら、flat なリストで構わない。

## Single vs multi-context repos

**Single context（ほとんどの repo）:** repo root に 1 つの `CONTEXT.md`。

**Multiple contexts:** repo root の `CONTEXT-MAP.md` が contexts のリスト、それぞれの場所、互いの関係を示す:

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

skill はどちらの structure が該当するかを推測する:

- `CONTEXT-MAP.md` が存在すれば、それを読んで contexts を見つける
- root の `CONTEXT.md` のみ存在すれば、single context
- どちらも存在しなければ、最初の用語が解決したときに root の `CONTEXT.md` を遅延生成する

複数の context が存在する場合、現在のトピックがどれに関連するか推測する。不明なら尋ねる。

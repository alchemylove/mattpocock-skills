---
name: codebase-design
description: deep module を設計するための共通語彙。ユーザーがモジュールのインターフェースを設計・改善したい、deepening の機会を見つけたい、seam の置き場所を決めたい、コードをよりテスト可能・AI-navigable にしたい、または他の skill が deep-module の語彙を必要とするときに使う。
---

# Codebase Design

**deep module** を設計する: 小さな interface の背後に多くの behaviour を、綺麗な seam に配置し、その interface を通してテスト可能にする。コードが設計・再構成される場面ではどこでもこの言葉とこれらの原則を使う。狙いは caller にとっての leverage、maintainer にとっての locality、そして誰にとっても testability である。

## Glossary

これらの用語をそのまま使う — "component"、"service"、"API"、"boundary" に置き換えない。一貫した言葉こそが要点である。

**Module** — interface と implementation を持つあらゆるもの。意図的に scale-agnostic: 関数、クラス、パッケージ、あるいは tier をまたぐ slice でもよい。_避けるべき語_: unit、component、service。

**Interface** — caller が module を正しく使うために知っておくべきすべて: type signature だけでなく、invariants、ordering constraints、error modes、必要な configuration、performance characteristics も含む。_避けるべき語_: API、signature（狭すぎる — これらは type-level の表面しか指さない）。

**Implementation** — module の中身、そのコードの本体。**Adapter** とは区別される: あるものは小さな adapter で大きな implementation を持つこともあれば（Postgres repo）、大きな adapter で小さな implementation を持つこともある（in-memory fake）。seam が話題のときは "adapter" を、それ以外は "implementation" を使う。

**Depth** — interface における leverage: caller（またはテスト）が学ばなければならない interface の単位あたり、どれだけの behaviour を行使できるか。module は、小さな interface の背後に大量の behaviour がある場合 **deep**、interface が implementation とほぼ同じくらい複雑な場合 **shallow** である。

**Seam** _(Michael Feathers)_ — その場所を編集せずに behaviour を変更できる場所。module の interface が存在する*位置*のこと。seam をどこに置くかは、その背後に何を置くかとは別の設計判断である。_避けるべき語_: boundary（DDD の bounded context と意味が重複する）。

**Adapter** — seam において interface を満たす具体的なもの。（中身が何かという *substance* ではなく）どの枠を埋めるかという *role* を表す。

**Leverage** — depth によって caller が得るもの: 学ぶ interface の単位あたり、より多くの capability。1 つの implementation が N 個の call site と M 個のテストにわたって元を取る。

**Locality** — depth によって maintainer が得るもの: 変更、バグ、知識、検証が caller 全体に散らばるのではなく 1 か所に集中する。一度直せば、どこでも直る。

## Deep vs shallow

**Deep module** = 小さな interface + 多くの implementation:

```
┌─────────────────────┐
│   Small Interface   │  ← Few methods, simple params
├─────────────────────┤
│                     │
│  Deep Implementation│  ← Complex logic hidden
│                     │
└─────────────────────┘
```

**Shallow module** = 大きな interface + わずかな implementation（避けるべき）:

```
┌─────────────────────────────────┐
│       Large Interface           │  ← Many methods, complex params
├─────────────────────────────────┤
│  Thin Implementation            │  ← Just passes through
└─────────────────────────────────┘
```

interface を設計するときは、こう問う:

- メソッドの数を減らせるか?
- パラメータを単純化できるか?
- もっと多くの複雑さを内側に隠せるか?

## Principles

- **Depth は interface の性質であり、implementation の性質ではない。** deep module は内部的に小さく、mockable で swappable な部品から構成されていてよい — それらは単に interface の一部ではないだけだ。module は interface における **external seam** に加えて、**internal seam**（その implementation に private で、自身のテストが使う）を持つこともある。
- **The deletion test.** module を削除したと想像する。複雑さが消え去るなら、それは pass-through だった。複雑さが N 個の caller にわたって再出現するなら、それは存在価値があった。
- **The interface is the test surface.** caller とテストは同じ seam を通る。interface を*超えて*テストしたいなら、その module はおそらく形が間違っている。
- **Adapter が 1 つなら hypothetical な seam。Adapter が 2 つなら本物の seam。** 実際に何かがそこを境に変化するのでない限り、seam を導入しない。

## Designing for testability

良い interface はテストを自然にする:

1. **依存を受け取る。作り出さない。**

   ```typescript
   // Testable
   function processOrder(order, paymentGateway) {}

   // Hard to test
   function processOrder(order) {
     const gateway = new StripeGateway();
   }
   ```

2. **結果を返す。副作用を起こさない。**

   ```typescript
   // Testable
   function calculateDiscount(cart): Discount {}

   // Hard to test
   function applyDiscount(cart): void {
     cart.total -= discount;
   }
   ```

3. **小さい surface area。** メソッドが少ない = 必要なテストが少ない。パラメータが少ない = テストのセットアップが単純。

## Relationships

- **Module** はちょうど 1 つの **Interface**（caller とテストに提示する表面）を持つ。
- **Depth** は **Module** の性質であり、その **Interface** に対して測られる。
- **Seam** は **Module** の **Interface** が存在する場所である。
- **Adapter** は **Seam** に置かれ、**Interface** を満たす。
- **Depth** は caller にとっての **Leverage** と、maintainer にとっての **Locality** を生む。

## Rejected framings

- **implementation の行数と interface の行数の比としての Depth**（Ousterhout）: implementation を水増しすることに報酬を与えてしまう。代わりに depth-as-leverage を使う。
- **"Interface" を TypeScript の `interface` キーワードやクラスの public メソッドとすること**: 狭すぎる — ここでの interface は caller が知るべきすべての事実を含む。
- **"Boundary"**: DDD の bounded context と意味が重複する。**seam** または **interface** と言う。

## Going deeper

- **依存関係を踏まえて cluster を deepening する** — [DEEPENING.md](DEEPENING.md) を参照: dependency categories、seam discipline、replace-don't-layer testing。
- **代替 interface を探る** — [DESIGN-IT-TWICE.md](DESIGN-IT-TWICE.md) を参照: 並列の sub-agent を立ち上げ、interface を根本的に異なる複数の方法で設計し、depth・locality・seam placement で比較する。

---
name: ubiquitous-language
description: 現在の会話から DDD スタイルの ubiquitous language の glossary を抽出し、曖昧さを指摘して正規の用語を提案する。UBIQUITOUS_LANGUAGE.md に保存する。ユーザーが domain の用語を定義したい、glossary を作りたい、用語を厳密化したい、ubiquitous language を作りたいとき、または「domain model」や「DDD」に言及したときに使う。
disable-model-invocation: true
---

# ユビキタス言語 (Ubiquitous Language)

現在の会話からドメイン用語を抽出し、一貫した glossary に形式化してローカル file に保存する。

## 手順 (Process)

1. **会話をスキャン**し、ドメイン関連の名詞、動詞、概念を抽出
2. **問題を特定**:
   - 同じ語が異なる概念に使われている (ambiguity)
   - 同じ概念に異なる語が使われている (synonyms)
   - 曖昧または過負荷の用語
3. **意見を持った canonical glossary を提案**
4. **作業ディレクトリに `UBIQUITOUS_LANGUAGE.md` を書き込む** (下記フォーマット)
5. **会話内に要約を出力**

## 出力フォーマット (Output Format)

次の構造で `UBIQUITOUS_LANGUAGE.md` を書く:

```md
# Ubiquitous Language

## Order lifecycle

| Term        | Definition                                              | Aliases to avoid      |
| ----------- | ------------------------------------------------------- | --------------------- |
| **Order**   | A customer's request to purchase one or more items      | Purchase, transaction |
| **Invoice** | A request for payment sent to a customer after delivery | Bill, payment request |

## People

| Term         | Definition                                  | Aliases to avoid       |
| ------------ | ------------------------------------------- | ---------------------- |
| **Customer** | A person or organization that places orders | Client, buyer, account |
| **User**     | An authentication identity in the system    | Login, account         |

## Relationships

- An **Invoice** belongs to exactly one **Customer**
- An **Order** produces one or more **Invoices**

## Example dialogue

> **Dev:** "When a **Customer** places an **Order**, do we create the **Invoice** immediately?"
> **Domain expert:** "No — an **Invoice** is only generated once a **Fulfillment** is confirmed. A single **Order** can produce multiple **Invoices** if items ship in separate **Shipments**."
> **Dev:** "So if a **Shipment** is cancelled before dispatch, no **Invoice** exists for it?"
> **Domain expert:** "Exactly. The **Invoice** lifecycle is tied to the **Fulfillment**, not the **Order**."

## Flagged ambiguities

- "account" was used to mean both **Customer** and **User** — these are distinct concepts: a **Customer** places orders, while a **User** is an authentication identity that may or may not represent a **Customer**.
```

## ルール (Rules)

- **意見を持つ。** 同じ概念に複数の語がある場合、最良のものを選び、他を避けるべき alias として列挙する。
- **衝突を明示的に flag する。** 会話で用語が曖昧に使われている場合、"Flagged ambiguities" セクションで明確な推奨とともに指摘する。
- **domain expert に関連する用語のみ含める。** module や class の名前は、ドメイン言語に意味がある場合を除きスキップする。
- **定義は簡潔に。** 最大 1 文。何をするかではなく、何であるかを定義する。
- **関係を示す。** bold の用語名を使い、明らかな場合は cardinality を表現する。
- **ドメイン用語のみ含める。** 一般的な programming 概念 (array、function、endpoint) は、ドメイン固有の意味がない限りスキップする。
- **自然なクラスタが現れたら複数テーブルにグループ化** (例: subdomain、lifecycle、actor ごと)。各グループに見出しとテーブル。すべてが単一のまとまったドメインなら 1 テーブルでよい — 無理にグループ化しない。
- **example dialogue を書く。** dev と domain expert の短い会話 (3–5 往復) で、用語が自然にどう相互作用するかを示す。関連概念間の境界を明確にし、用語を正確に使う様子を示す。

<example>

## Example dialogue

> **Dev:** "How do I test the **sync service** without Docker?"

> **Domain expert:** "Provide the **filesystem layer** instead of the **Docker layer**. It implements the same **Sandbox service** interface but uses a local directory as the **sandbox**."

> **Dev:** "So **sync-in** still creates a **bundle** and unpacks it?"

> **Domain expert:** "Exactly. The **sync service** doesn't know which layer it's talking to. It calls `exec` and `copyIn` — the **filesystem layer** just runs those as local shell commands."

</example>

## 再実行 (Re-running)

同じ会話で再度呼び出された場合:

1. 既存の `UBIQUITOUS_LANGUAGE.md` を読む
2. その後の議論から新しい用語を取り込む
3. 理解が進化していれば定義を更新
4. 新しい ambiguity を再 flag
5. example dialogue を書き直して新しい用語を取り込む

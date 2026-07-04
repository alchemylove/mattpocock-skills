# GLOSSARY.md Format

`GLOSSARY.md` は、この teaching workspace における canonical な言語である。すべての explainer・演習・learning record はその用語に従うべきである。これを構築すること自体が学習の一部である: 概念を引き締まった定義に圧縮できることは、ユーザーがそれを理解している証拠である。

## 構造 (Structure)

```md
# {Topic} Glossary

{One or two sentence description of the topic this glossary covers.}

## Terms

**Hypertrophy**:
Muscle growth driven by mechanical tension and metabolic stress over repeated training sessions.
_Avoid_: Bulking, getting big

**Progressive overload**:
Systematically increasing the demand on a muscle over time — via load, volume, or intensity.
_Avoid_: Pushing harder, levelling up

**RPE (Rate of Perceived Exertion)**:
A 1–10 self-rating of how hard a set felt, where 10 is failure and 8 means two reps left in the tank.
_Avoid_: Effort score, intensity rating
```

## ルール (Rules)

- **ユーザーが理解した用語だけを追加する。** glossary は圧縮された知識の記録であり、ユーザーが学ぶために読む辞書ではない。ユーザーが概念に触れたばかりなら、正しく使えるようになるまでここに昇格させるのを待つ。
- **意見を持つ。** 同じ概念に複数の語がある場合、最良のものを選び、残りは避けるべき別名として列挙する。これが言語を圧縮する方法である。
- **定義を引き締める。** 1〜2文にとどめる。その用語が何を _する_ か・どう _行う_ かではなく、何で _ある_ かを定義する。
- **glossary 自身の用語を定義の中で使う。** 一度 glossary に入った用語は、他の定義の中も含めて、あらゆる場所で優先的に使う。これが後で複雑な用語を掴みやすくする。
- 自然なまとまりが生まれたら**サブ見出しでグループ化する**（例: `## Anatomy`、`## Programming`）。用語がまとまっているならフラットなリストでも構わない。
- **曖昧さを明示的にフラグする。** ある用語がより広い分野で緩く使われている場合、解決策を記す: 「この workspace では、'set' は常に working set を意味する — ウォームアップは別途記録する。」
- **理解が深まるにつれて改訂する。** ユーザーが1週目に書いた定義は、6週目には誤りになっているかもしれない。その場で更新し、古びたエントリを残さない。

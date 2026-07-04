# Learning Record Format

learning record は `./learning-records/` に置かれ、`0001-slug.md`、`0002-slug.md` のように連番を使う。ディレクトリは lazily に作成する — 最初の record が書かれるときだけでよい。

これらは教えることにおける ADR に相当するものである: 非自明な学び、重要な洞察、そして今後のセッションを方向づける、表明された prior knowledge を記録する。zone of proximal development を算出するために使われる。

## テンプレート (Template)

```md
# {Short title of what was learned or established}

{1-3 sentences: what was learned (or what prior knowledge was established), and why it matters for future sessions.}
```

これがフォーマットのすべてである。learning record は一段落だけでもよい。価値があるのは、これが今わかったという _事実_ と、それが次に教えることを _なぜ_ 変えるのかを記録することであり、セクションを埋めることではない。

## 任意のセクション (Optional sections)

これらは本当に価値を加える場合だけ含める。ほとんどの record には不要である。

- **Status** frontmatter（`active | superseded by LR-NNNN`）— 以前の理解が間違っていたことが分かり、置き換えられる場合に有用である。
- **Evidence** — ユーザーがどのように理解を示したか（質問に答えた、演習を完了した、過去の経験を引用した）。その主張が後で見直される可能性がある場合に有用である。
- **Implications** — これが今後のセッションにおいて何を可能にし、何を除外するか。自明でない場合は記録する価値がある。

## 番号付け (Numbering)

`./learning-records/` を走査して既存の最大番号を見つけ、1 加算する。

## いつ learning record を書くか (When to write a learning record)

以下のいずれかが真であるときに書く:

1. **ユーザーが自明でない事柄について本物の理解を示した** — 触れただけでなく、その概念を正しく使えるという証拠があること。これは次に教えるべき事柄の新しい床 (floor) を設定する。
2. **ユーザーが prior knowledge を明かした** — 「X はもう知っている」。今後のセッションでそれを教え直さないよう記録する。主張された理解の _深さ_ も記録する。
3. **誤解が正された** — ユーザーが以前は間違ったことを信じていて、今はなぜそれが間違いなのかが分かった。これらは高価値である: 関連するトピックにおける今後のつまずきを予測する。
4. **学習に応じて mission が変わった** — ユーザーは自分が思っていたのとは違う何かを気にかけていたことに気づいた。[[MISSION.md]] へ相互リンクし、更新する。

### 該当 _しない_ もの (What does not qualify)

- 単に取り上げられただけの内容。取り上げたことは学習ではない。証拠を待つ。
- [[GLOSSARY.md]] に用語定義として既に簡潔に記録されている事柄。重複させない。
- セッションごとの活動ログ。learning record は日記ではなく、意思決定に値する洞察である。

## Supersession（置き換え）

後の record が以前の record と矛盾する場合（ユーザーの理解が深まった、あるいは訂正された場合）、古い record を削除するのではなく `Status: superseded by LR-NNNN` と記す。理解がどう進化したかという履歴自体が有用な signal である。

クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=research
```

```bash
npx skills update research
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/research)

## 何をするか (What it does)

`research` は、答えを持つ一次情報源を読むことで疑問に答え、引用付きの Markdown ファイルを残します。これは**一次情報源**（公式ドキュメント、ソースコード、仕様、ファーストパーティの API）だけから動作し、それらについての二次的な要約には決して頼りません。そのため保存されるものは、要約のそのまた要約ではなく、権威ある何かへと遡れるものになります。

## いつ使うか (When to reach for it)

`/research` と入力するか、タスクが調べ物の作業に転じたときエージェントが自動的に使います。

次のステップが*何かを調べること* — あるAPIがどう振る舞うか、仕様が実際に何と言っているか、ある主張が成り立つかどうか — であり、自分のスレッドをその読み込み作業で止めたくないときに使ってください。読むことではなくインタビューによって計画を研ぎ澄ますには [grilling](https://aihero.dev/skills-grilling) を、使い捨てのコードで何を作るべきかを探るには [prototype](https://aihero.dev/skills-prototype) を使ってください。

## 委任される調べ物

決定的な動きは、その読み込み作業が**バックグラウンドエージェント**として実行されることです。あなたは作業を続け、エージェントは離れたところで各主張をその一次情報源まで遡り、リポジトリがそうしたメモを置く場所に、引用付きの単一の Markdown ファイルを落とします。Research は委任する調べ物であり、外注する思考ではありません — あなたが受け取るのは、出典が添付された、反応すべき文書です。

## 全体の中での位置づけ (Where it fits)

いつでも使える standalone であり、思考系の skill に材料を供給します。それが生み出すファイルは grill したり、計画したり、設計したりする対象となるものなので、[grilling](https://aihero.dev/skills-grilling) や [to-prd](https://aihero.dev/skills-to-prd) のような作業の上流に位置し、ビルドチェーンの中には入りません。全体像については [ask-matt](https://aihero.dev/skills-ask-matt) を参照してください。

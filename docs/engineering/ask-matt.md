クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=ask-matt
```

```bash
npx skills update ask-matt
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt)

## 何をするか (What it does)

`ask-matt` はこのリポジトリにある skill 群のルーターです。今どんな状況にあるかを説明すると、どの skill や flow が合っているか、どの順序で実行すべきかを教えてくれます。

`ask-matt` は**それ自体では何の作業もしません**。grill もしないし、PRD も書かないし、何かを直すこともありません — ただ道案内をするだけです。これは何よりもまず**ユーザー起動 (User-invoked)** の skill のために存在します。それらはあなたの代わりに自動発火することはないので、*あなた自身*がその存在を覚えておく必要があり、`ask-matt` はその記憶を肩代わりする役割を担います。また、名前を挙げて呼び出すタイプの **モデル起動 (Model-invoked)** skill — `/tdd`、`/diagnosing-bugs`、`/prototype`、`/code-review`、そして語彙リファレンスである `/domain-modeling` と `/codebase-design` — も指し示します。「どれを、いつ」に答えたうえで、実際に作業をこなす skill へと引き渡します。

## いつ使うか (When to reach for it)

これは `/ask-matt` と入力して呼び出します — エージェントが自発的にこれを使うことはありません。

どの skill や flow が今の状況に合うか分からないときはいつでも使ってください。アイデアはあるがどこから手を付ければいいか分からない、バグ報告の山があって `/triage` 向けかどうか判断がつかない、似たような skill が2つあって区別がつかない、といった場合です。すでに使いたい skill が分かっているなら、ルーターを飛ばして直接それを呼び出してください。

## Skill だけでなく Flow も

`ask-matt` が与えてくれる考え方の軸は **flow** です — 単一の skill ではなく、skill 群を*通り抜ける*経路のことです。ほとんどの作業は1本の **main flow**（アイデア → 出荷: grill → PRD → issues → implement → review）に沿って進み、そこに2つの **on-ramp**（受信したバグや要望を扱う triage レーン、アイデアを生み出すコードベース健全性レーン）が合流し、それ以外はすべて単独で使う **standalone** です。質問をすれば、単にツールを渡されるのではなく、正しい flow の正しいステップに配置されます。

## 全体の中での位置づけ (Where it fits)

`ask-matt` は**ルーター** — 全体を見渡す standalone なマップです。他のすべての docs ページがここへ [ask-matt](https://aihero.dev/skills-ask-matt) として戻ってくるノードであり、それゆえ自分自身が chain の*中*に位置することはなく、あらゆる chain へと*入り口*を指し示します。ここから最も多く着地するのは main flow の先頭である [grill-with-docs](https://aihero.dev/skills-grill-with-docs)、あるいは自分が作ったのではない作業のための on-ramp である [triage](https://aihero.dev/skills-triage) です。ルーター自身の把握している全体像すら古くなっている場合は、[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt) が正式なマップとなります。

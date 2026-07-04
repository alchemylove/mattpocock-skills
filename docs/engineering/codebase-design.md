クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=codebase-design
```

```bash
npx skills update codebase-design
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)

## 何をするか (What it does)

`codebase-design` は、**deep module**（小さなインターフェースの背後に多くの振る舞いを隠し、きれいな seam に配置され、そのインターフェース越しにテスト可能なモジュール）を設計するための、共有された精密な語彙を与えます。

これは**手順ではなく言語**です。コードを再構成したり、リファクタリング計画を渡したりすることはありません — module、interface、depth、seam、adapter、leverage、locality といった言葉を固定し、あらゆる設計の会話や、設計に触れる他のすべての skill が同じ言い方をできるようにします。一貫した言語であることこそが本質であり、「component」「service」「API」「boundary」といった語は、重要な区別を曖昧にするため意図的に禁止されています。

## いつ使うか (When to reach for it)

`/codebase-design` と入力するか、タスクに合致すればエージェントが自動的に使います。

モジュールのインターフェースを設計・改善しているとき、deepening の機会を探しているとき、seam をどこに置くか決めているとき、コードをよりテスト可能かつ AI が扱いやすいものにしようとしているときに使ってください。他の skill も deep-module の語彙が必要になるたびにこれを取り込みます。もし磨きたいのがモジュール設計ではなくプロジェクトの*ドメイン*用語であれば、代わりに [domain-modeling](https://aihero.dev/skills-domain-modeling) を使ってください。既存のコードベース全体にアーキテクチャの見直しを行いたい場合は [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) を使ってください。

## Deep であって Shallow でない

モジュールは、小さなインターフェースの背後に大量の振る舞いが収まっているとき **deep** であり、インターフェースが実装とほぼ同じくらい複雑なとき **shallow** です。深さは **leverage**（呼び出し側やテストが、学習すべきインターフェースの単位あたりでどれだけのことを行使できるか）として測られます。重要なのは、深さは*インターフェース*の性質であって実装の性質ではないということです — deep なモジュールは、内部的には小さく交換可能な部品で構成されていて構いません。呼び出し側にそれが見えさえしなければよいのです。

主に2つのチェックが役立ちます。**deletion test（削除テスト）**: そのモジュールを削除したと想像してみる — 複雑さが消え去るならそれは単なる pass-through であり、N 個の呼び出し元に複雑さが再び現れるなら、それは存在価値があったということです。そして**アダプターが1つならそれは仮説上の seam、2つあれば本物の seam**である — 実際に何かがそこを境に変化するまで seam を切らないこと。

## インターフェースはテストの接点

呼び出し側とテストは同じ seam を横切るので、適切に配置されたインターフェースは、下にあるコードが自由に動き回れる一方で、テストには狙うべき安定した的を与えます。だからこそこの語彙は、使い古された「boundary」よりも **seam**（Feathers の用語 — そこを編集せずに振る舞いを変えられる場所）を重視し、ここでの「interface」は*呼び出し側が知っておくべきすべての事実*を意味します — シグネチャはもちろん、不変条件、順序、エラーモード、パフォーマンスも含み、型レベルの表面だけではありません。

## 意図的に切り出されている

`codebase-design` は deep-module の語彙に関する**唯一の正典**であり、どこからでも参照できるよう独立した model-invoked skill として切り出されています。他の skill は言葉を言い直すのではなく、これを指し示します — [tdd](https://aihero.dev/skills-tdd) はテストを書く前に seam を置くためにこれを借り、[improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) は既存コードを再構成する際にこれに頼り、[to-prd](https://aihero.dev/skills-to-prd) は仕様を書く前に seam や deepening の機会をスケッチする際にこの言葉を使います。

これを standalone のまま保つ狙いは、それらの skill が定める手順を発火させることなく、モジュール設計の考え方についての**リファレンス**として単独で参照できるようにするためです。言葉を一箇所で一度だけ固定すれば、それを必要とするすべてのものがそこを参照できます。

## 全体の中での位置づけ (Where it fits)

`codebase-design` は**いつでも使える standalone** — エンジニアリング skill 群の下にある共有語彙レイヤーです。最も近い隣人は [domain-modeling](https://aihero.dev/skills-domain-modeling) で、こちらはモジュール構造ではなく問題ドメインのための並行する語彙 skill です。どの skill や flow が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が導いてくれます。

クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=improve-codebase-architecture
```

```bash
npx skills update improve-codebase-architecture
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)

## 何をするか (What it does)

`improve-codebase-architecture` はコードベースをスキャンして**deepening の機会**（shallow なモジュール — それが隠しているものとほぼ同じくらい複雑なインターフェース — が deep なモジュールになりうる箇所）を見つけ出し、自己完結した視覚的な HTML レポートとして提示し、あなたが選んだものについて grilling を行います。

これは平坦なリファクタリングのリストを渡すことは**しません**。すべての候補は **deletion test（削除テスト）** に合格しなければなりません — このモジュールを取り除いたら複雑さは*より小さなインターフェースの背後に集約される*のか、それとも単に移動するだけなのか。「集約される」場合だけがカードとして採用されます。このフィルターこそが、このレポートが一般的なクリーンアップの助言に成り下がるのを防いでいます。

## いつ使うか (When to reach for it)

これは `/improve-codebase-architecture` と入力して呼び出します — エージェントが自発的にこれを使うことはありません。

定期的な健全性チェックとして使ってください — 数日おきに、あるいはコードベースが1つの概念を理解するために小さなモジュールの間を行き来しすぎるように感じ始めたときに。既存のアーキテクチャを読み込み、どこを深くすべきかを提案します。すでに再設計したいモジュールが分かっていて、それを考え抜くための語彙だけが必要なら、代わりに [codebase-design](https://aihero.dev/skills-codebase-design) を使ってください — この skill は候補を見つける調査であり、あちらは設計の作業台です。

## Deepening の機会

この skill 全体は1つのアイデア — **depth（深さ）** — を軸に回っています。deep なモジュールは小さく安定したインターフェースの背後に多くの機能を隠しますが、shallow なモジュールはその下にあるコードとほぼ同じ広さのインターフェースから実装を漏らします。このレポートは shallow さを探します — テスト可能性のためだけに切り出された純粋関数（実際のバグはそれがどう呼び出されるかに潜んでいて、**locality** がない）、**seam** を越えて漏れ出すモジュール、5つのファイルを開かないと理解できない概念 — そしてそれを修正する deepening を提案します。

これは共有される設計語彙（**module**、**interface**、**depth**、**seam**、**adapter**、**leverage**、**locality**）と、`CONTEXT.md` にあるあなたのプロジェクト自身のドメイン言語で語られるため、候補は「FooBarHandler をリファクタリングする」ではなく「Order intake モジュールを deepen する」というように読めます。

## レポート、その後に Grill

出力は、あなたの OS の一時ディレクトリに書き出されるブラウザで開ける HTML ファイルです — リポジトリには何も残りません。各候補は、関わるファイル、摩擦、平易な英語での解決策、locality と leverage の観点でのメリット、before/after 図、そして `Strong` / `Worth exploring` / `Speculative` のバッジを備えたカードです。最初に取り組むべき候補で締めくくられます。

そこで一旦止まり、どれを深掘りしたいか尋ねます。1つ選ぶと、その設計について [grilling](https://aihero.dev/skills-grilling) のループを実行します — 制約、seam の背後に何があるか、どのテストが生き残るかを検討しながら、決定が結晶化するたびにドメインモデルをその場で更新します。

## 全体の中での位置づけ (Where it fits)

`improve-codebase-architecture` は**定期メンテナンス**です — chain の中の1ステップとしてではなく、数日おきに実行してください。隣人は、すべての候補が語られる depth と seam の語彙を所有する [codebase-design](https://aihero.dev/skills-codebase-design)、候補を選んだ後に設計ツリーを歩く [grilling](https://aihero.dev/skills-grilling)、そして再設計が落ち着くにつれて `CONTEXT.md` と ADR を最新に保つ [domain-modeling](https://aihero.dev/skills-domain-modeling) です。どの skill や flow が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が導いてくれます。

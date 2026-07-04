クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=implement
```

```bash
npx skills update implement
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/implement)

## 何をするか (What it does)

`implement` は PRD や issue 群に書かれた作業を構築します — test-driven development、型チェック、フルテストスイートを通し、その後レビューへ引き渡して現在のブランチへコミットします。

これは**何を作るかを決めません**。仕様はすでに確定しており、seam もすでに合意済みです。`implement` はその計画を蒸し返すのではなく実行するだけです。これは頭ではなく手です — 思考は上流ですでに済んでいます。

## いつ使うか (When to reach for it)

これは `/implement` と入力して呼び出します — エージェントが自発的にこれを使うことはありません。

作業がすでに PRD として書かれているか issue に分割されていて、それをコードに変換する準備ができたときに使ってください。仕様がまだ存在しないなら、まずそれを書いてください — そのためには [to-prd](https://aihero.dev/skills-to-prd) を、あるいは PRD をチケットに分割するには [to-issues](https://aihero.dev/skills-to-issues) を使います。完全な仕様なしにテストファーストで何かを作りたいだけなら、直接 [tdd](https://aihero.dev/skills-tdd) に降りてください。

## 事前に合意された Seam

`implement` が動作の基盤とするアイデアは **seam** です — コードを書く前に選ばれた、機能がテストされる安定したインターフェースのことです。ビルドの途中で seam を発明することはなく、（[to-prd](https://aihero.dev/skills-to-prd) の間に）すでに選ばれたものを使い、[tdd](https://aihero.dev/skills-tdd) を通してそこに対するテストを書きます。事前合意済みの seam で作業することが、実装を誠実に保つ鍵です — テストは安定した何かを狙うので、下にあるコードはテストを動かすことなく変化できます。

その核の周りでは、ループを引き締め続けます — 頻繁に型チェックし、進めながら単体のテストファイルを実行し、最後に一度だけスイート全体を実行します — その後レビューパスとブランチへのコミットで締めくくります。

## 全体の中での位置づけ (Where it fits)

`implement` は main chain の終盤、レビューの直前にあるビルドステップです。

```txt
grill-with-docs → to-prd → to-issues → implement → code-review
```

作業が仕様化され順序づけされた後に使ってください、その前ではありません。主要な隣人は、独立して着手可能なチケットを生み出す [to-issues](https://aihero.dev/skills-to-issues) と、各 seam でテストファーストにテストを書くために内部で駆動する [tdd](https://aihero.dev/skills-tdd) です。その後、独自の [code-review](https://aihero.dev/skills-code-review) パスを実行してからコミットします。どの skill や flow が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が導いてくれます。

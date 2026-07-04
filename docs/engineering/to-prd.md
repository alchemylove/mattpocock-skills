クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=to-prd
```

```bash
npx skills update to-prd
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd)

## 何をするか (What it does)

`to-prd` は現在の会話とあなたのコードベース理解を product requirements document に変換し、それをあなたの issue tracker に公開します。

これは**あなたに改めてインタビューすることはしません**。これを使う頃には、すり合わせの作業はすでに終わっています — `to-prd` は新たな質問を重ねるのではなく、すでに分かっていることを統合します。

## いつ使うか (When to reach for it)

これは `/to-prd` と入力して呼び出します — エージェントが自発的にこれを使うことはありません。

変更について話し合いが済み、ドメイン言語が定まっていて、コードが一切書かれる前にその共有理解を仕様として書き留めたいときに使ってください。まだすり合わせが済んでいないなら、まず grill してください — そのためには [grill-with-docs](https://aihero.dev/skills-grill-with-docs) を使います。完成した PRD をチケットに分割するには [to-issues](https://aihero.dev/skills-to-issues) を使ってください。

## 前提条件 (Prerequisites)

`to-prd` はあなたの issue tracker に公開するので、まず [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) がこのリポジトリの tracker と triage ラベルを設定している必要があります。`ready-for-agent` ラベルを自身で適用するので、別途 triage パスは不要です。

## PRD に含まれるもの

- **Problem statement** — 何が壊れているか、あるいは欠けているか、そしてなぜそれを解決する価値があるのかを、プロジェクト自身の語彙で。
- **Solution** — 実装の詳細に踏み込む前の、修正の大まかな形。
- **User stories** — 変更がサポートしなければならない具体的な振る舞いの、詳細で番号付けされたリスト。それぞれが独立して確認可能。
- **Implementation decisions** — 会話の中ですでに固まった選択事項。後で蒸し返さないため。
- **Testing decisions** — その機能がテストされる seam と、「完了」がどう見えるか。
- **Out-of-scope items** — この変更が意図的に*カバーしない*こと。チケットの範囲を限定するため。
- **Further notes** — 上記のセクションに収まらないが、引き継ぐ価値のあるその他のこと。

## Deep Module

PRD を書く前に、`to-prd` はその機能がテストされる **seam** をスケッチし、**deep module** の機会 — 小さく安定したインターフェースの背後に隠された多くの機能 — を探します。新しい seam よりも既存の seam を、そして可能な限り最も高い seam を、理想的には変更全体を通じてたった1つだけを好みます。

これはエージェントによる開発にとって重要です。良いインターフェースはテストに狙うべき安定した的を与え、下にあるコードはテストを動かすことなく変化できるからです。

## うまく機能しているかの目安 (It's working if)

- あなたに新たな質問を重ねるのではなく、PRD を書き始める。
- 書く前に seam をあなたと確認し、できるだけ少ない数を提案する。
- PRD は一般的な定型文ではなく、あなたのプロジェクトのドメイン語彙で返ってくる。

## 全体の中での位置づけ (Where it fits)

`to-prd` は main build chain の1ステップです。

```txt
grill-with-docs → to-prd → to-issues → implement → code-review
```

計画とドメイン言語が確定した後、作業を実装チケットに分割する前に使ってください。主要な隣人は、コンテキストを研ぎ澄まし PRD を正確にする [grill-with-docs](https://aihero.dev/skills-grill-with-docs) と、PRD を [implement](https://aihero.dev/skills-implement) が構築する独立して着手可能な issue に変える [to-issues](https://aihero.dev/skills-to-issues) です。どの skill や flow が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が導いてくれます。

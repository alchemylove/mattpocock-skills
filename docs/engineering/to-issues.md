クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=to-issues
```

```bash
npx skills update to-issues
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-issues)

## 何をするか (What it does)

`to-issues` は計画、仕様、あるいは PRD を、独立して着手可能な issue の集合に分解し、依存関係の順序でプロジェクトの issue tracker に公開します。

すべての issue は **tracer bullet** です — すべての統合レイヤー（schema、API、UI、テスト）をエンドツーエンドで貫く薄い*垂直*スライスであり、1つのレイヤーだけの水平スライスでは決してありません。完成したスライスはそれ単体でデモ可能あるいは検証可能であり、これが結果として得られるチケットを独立したエージェントに安全に渡せるものにしています。

## いつ使うか (When to reach for it)

これは `/to-issues` と入力して呼び出します — エージェントが自発的にこれを使うことはありません。

合意済みの計画や書かれた仕様があり、それをエージェントが着手できるチケットに分割したいときに使ってください。会話を指し示すか、既存の issue 参照を渡せば、まず本文とコメントを取得します。変更がまだ仕様として書かれていないなら、まずそれを作成してください — そのためには [to-prd](https://aihero.dev/skills-to-prd) を使います。

## 前提条件 (Prerequisites)

`to-issues` はあなたの issue tracker に公開するので、まず [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) がこのリポジトリの tracker と triage ラベルの語彙を設定している必要があります。公開時に ready-for-agent の triage ラベルを自身で適用します。

## 水平スライスではなく垂直スライス

この skill 全体は1つの区別を軸に回っています。**水平**スライスは変更の1つのレイヤー — schema 全部、あるいは API 全部 — を出荷しますが、すべてのレイヤーが揃うまで何も動きません。**垂直**スライス、すなわち tracer bullet は、*すべて*のレイヤーを一度に貫く1本の狭い経路を出荷するので、完成した瞬間にデモできます。

スライスする前に、`to-issues` は prefactoring — 「変更を簡単にしてから、簡単な変更をする」— を探し、その作業を最初に順序づけます。その後、何も書く前に分解について（粒度、依存関係、何を統合し何を分割するか）あなたに質問し、各 issue の「Blocked by」フィールドが本物のチケットを参照できるよう、ブロッカーを最初に公開します。

## 全体の中での位置づけ (Where it fits)

`to-issues` は main build chain の1ステップです。

```txt
grill-with-docs → to-prd → to-issues → implement → code-review
```

これは、スライスする対象となる user story を含む確定済みの仕様を渡す [to-prd](https://aihero.dev/skills-to-prd) と、独立して着手可能な各 issue を構築する [implement](https://aihero.dev/skills-implement)（[code-review](https://aihero.dev/skills-code-review) パスの前に、テストファーストでテストを書くために内部で [tdd](https://aihero.dev/skills-tdd) を駆動します）の間に位置します。どの skill や flow が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が導いてくれます。

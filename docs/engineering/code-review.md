クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=code-review
```

```bash
npx skills update code-review
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/code-review)

## 何をするか (What it does)

`code-review` は `HEAD` と指定した固定点（コミット、ブランチ、タグ、マージベース）との間の diff を、2つの独立した軸に沿ってレビューします — **Standards**（このリポジトリで文書化された規約にコードが従っているか）と **Spec**（元となった issue や PRD が求めたものを実装しているか）です。各軸は独立した並列 sub-agent として実行され、結果は並べて報告されます。2つの findings の集合を統合したり再ランク付けしたりすることは決してありません — それぞれを分離しておくことこそが本質であり、変更は一方の軸を通過しつつもう一方で失敗することがあるため、単一の統合された判定では一方がもう一方を覆い隠してしまうからです。

## いつ使うか (When to reach for it)

`/code-review` と入力するか、ブランチや PR、作業中の変更、あるいは「X 以降の」何かをレビューしてほしいと頼むとエージェントが自動的に使います。

既知の良好な状態と比較して判断すべき diff があり、*正しく作られているか？* と *正しいものが作られているか？* という2つの問いに独立して答えてほしいときに使ってください。これはビルドループの最後に実行されます。テストファーストでコードを実際に書くには [tdd](https://aihero.dev/skills-tdd) を、仕様全体をコードにするには [implement](https://aihero.dev/skills-implement) を使ってください — こちらはコミット前に独自の `/code-review` パスを実行します。

## 前提条件 (Prerequisites)

**Spec** 軸は、元となる仕様をどこかで見つける必要があります — コミットメッセージ内の issue 参照、渡されたパス、あるいは `docs/`/`specs/` 配下の PRD です。この issue tracker との連携は [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) から得られます。仕様がなければ Spec 軸は単にスキップし、その旨を報告します。**Standards** 軸は特に何も準備する必要はありません — 規約を文書化していないリポジトリであっても、常に組み込みの Fowler smell ベースラインを持っています。

## 2つの軸、決して統合しない

本質となるアイデアは**2つの軸**です。**Standards** は、diff がこのリポジトリのコードの書き方 — `CODING_STANDARDS.md` や `CONTRIBUTING.md`、加えて約12個の固定された Fowler code smell（Mysterious Name、Duplicated Code、Feature Envy、Data Clumps、…）のベースライン — に沿っているかを問います。このベースラインを安全に保つルールが2つあります。文書化されたリポジトリの規約は常にこれより優先されること、そしてすべての smell は判断材料であって絶対的な違反ではないことです。**Spec** はこれとは直交する問いを立てます — コードは issue や PRD が実際に求めたことを、要件の見落としやスコープの忍び込みなしに行っているか、です。

これらは並列の sub-agent として実行されるため、互いのコンテキストを汚染することはなく、最終レポートは別々の `## Standards` と `## Spec` の見出しの下に、それぞれのサマリーとともに提示されます。軸をまたいだ単一の勝者は意図的に存在しません。

## うまく機能しているかの目安 (It's working if)

- 最初に固定点を確定し確認する（`git rev-parse`）。sub-agent の内部ではなく、この時点で不正な ref や空の diff に対して速やかに失敗する。
- Standards と Spec の findings が2つの明確なブロックとして届き、それぞれが出典を明示している — 一方はリポジトリの規約やベースラインの smell、もう一方は引用された仕様の一文。
- 仕様が見つからない場合、Spec 軸は要件をでっち上げるのではなく「no spec available」と報告する。

## 全体の中での位置づけ (Where it fits)

`code-review` は main build chain の末尾にあるレビューステップです。

```txt
grill-with-docs → to-prd → to-issues → implement → code-review
```

最も近い隣人は [implement](https://aihero.dev/skills-implement) で、ビルドを駆動しコミット前の独自のレビューパスとしてこれを呼び出します。上流では、これが照合する仕様は [to-prd](https://aihero.dev/skills-to-prd) と [to-issues](https://aihero.dev/skills-to-issues) によって作られます。どの skill や flow が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が導いてくれます。

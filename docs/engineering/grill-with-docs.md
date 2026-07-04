クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=grill-with-docs
```

```bash
npx skills update grill-with-docs
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)

## 何をするか (What it does)

`grill-with-docs` は、計画やデザインについてあなたに容赦なく、一度に1つずつ質問を投げかけ、あなたとエージェントが共通理解に至るまでインタビューを続けます — そしてその過程で語彙と決定事項を書き留めていきます。

この grilling は**証跡を残します**。普通のインタビューはあなたの思考を研ぎ澄ませますが、セッションが終われば消えてしまいます。こちらは、用語が解決した瞬間にそれを `CONTEXT.md` の glossary に取り込み、後戻りしにくい決定を ADR として記録します。合意は会話の中だけに留まらず、生き残ります。

## いつ使うか (When to reach for it)

これは `/grill-with-docs` と入力して呼び出します — エージェントが自発的にこれを使うことはありません。

計画がまだ曖昧で、ドメイン言語も定まっていない、変更のごく初期段階で、コードが存在する前に両方をストレステストしたいときに使ってください。インタビューだけが欲しくて成果物は不要なら [grilling](https://aihero.dev/skills-grilling) を、計画がすでに明確で用語の確定や記録だけが必要なら [domain-modeling](https://aihero.dev/skills-domain-modeling) を使ってください。

## 前提条件 (Prerequisites)

この skill は状態を持ちます — grilling を進めながらリポジトリに書き込みます。解決した用語はルートの `CONTEXT.md` の glossary（あるいは `CONTEXT-MAP.md` がマルチコンテキストのリポジトリを示している場合は該当コンテキストの `CONTEXT.md`）に、本当に後戻りしにくい決定は `docs/adr/` 配下の ADR として置かれます。どちらも遅延生成されます — 最初の用語や決定が結晶化するまで何も存在しません — ので事前に足場を組む必要はありませんが、これらのファイルを安全に書き込める場所にいる必要はあります。

## Grill そのもの

エンジンとなるのは **grill** です — 設計ツリーを一度に1つずつ、容赦なく降りていき、決定同士の依存関係を解消してから次に進み、すべての質問に推奨される回答を添えます。コードベースが答えられる質問は、あなたに尋ねるのではなくコードベースを読んで答えます。

このバリエーションを独自の skill たらしめているのは、回答の行き先です。grill が進むにつれて、曖昧な言葉は標準的な用語へと磨かれ、最後にまとめてではなく、その場で glossary に書き込まれます。glossary は glossary のままであり続けます — 純粋な語彙のみで、実装の詳細も仕様もありません。ADR は控えめにしか提示されず、決定が後戻りしにくく、文脈なしには意外で、本物のトレードオフの結果である場合にのみ提示されます。ほとんどのセッションは、より鋭い glossary と、少数あるいはゼロの ADR を生み出します。それこそが意図された形です。

## うまく機能しているかの目安 (It's working if)

- 一度に1つの質問をし、質問票をまとめて出すのではなく待つ。
- 用語は解決した瞬間に、あなたのプロジェクト自身の言葉で `CONTEXT.md` に書き込まれる。
- 可能な場合は自分自身の質問に答えるためにコードベースへ手を伸ばす。
- ADR は稀にしか出てこない — 後戻り可能な選択に対して承認だけを求められることはない。

## 全体の中での位置づけ (Where it fits)

`grill-with-docs` は main build chain の最初のステップです。

```txt
grill-with-docs → to-prd → to-issues → implement → code-review
```

これは何かを仕様として書き留める前、最初に来るものです — 共有理解と定まった語彙を生み出し、それを [to-prd](https://aihero.dev/skills-to-prd) が改めてインタビューすることなく PRD へと統合します。近い隣人は、docs なしの同じインタビューである [grilling](https://aihero.dev/skills-grilling) と、これが駆動する glossary・ADR の訓練である [domain-modeling](https://aihero.dev/skills-domain-modeling) です。どの skill や flow が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が導いてくれます。

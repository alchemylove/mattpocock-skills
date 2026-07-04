クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=grill-me
```

```bash
npx skills update grill-me
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)

## 概要 (What it does)

`grill-me` は、プランや設計について容赦のないインタビューを行い、決定木のあらゆる枝を歩き尽くして、あなたとエージェントが **共通理解 (shared understanding)** に至るまで続けるスキルです。

一度に **1つの質問だけ** を投げかけ、回答を待ちます。まとめて質問を浴びせることは決してありません — それは混乱を招くだけです — また、コードベースを読めば答えがわかる質問については、尋ねる代わりに実際に読みに行きます。それぞれの質問にはエージェント自身のおすすめの回答が添えられるので、あなたは白紙のプロンプトを前にするのではなく、提案に対して反応する形になります。

## 使いどころ (When to reach for it)

`/grill-me` と入力して呼び出します — エージェントが自発的に使うことはありません。

プランがおおむね正しいと感じつつも、その中に未解決の判断が隠れているのを感じ取ったとき、ビルドに入る前に使いましょう — 弱い部分を見つけ出し、表に引きずり出したくなる瞬間です。同じ尋問をしつつ ADR とグロッサリー (glossary) の記録も残したい場合は、代わりに [grill-with-docs](https://aihero.dev/skills-grill-with-docs) を使ってください。

## 設計ツリー (design tree)

このセッションはプランを決定のツリー (design tree) として辿り、決定同士の依存関係を1つずつ解決していきます — 親の決定を確定させてから、それにぶら下がる選択肢へ進みます。目的は合意に素早く到達することではなく、暗黙のうちに済まされていた重要な判断をすべて明示的にすることです。セッションを終える頃には、すべての枝を巡り終えたプランが手元に残ります。

`grill-me` は **ステートレス (stateless)** です。何も書き込まず、作業スペースも残しません。どこでも実行でき、唯一の成果物は会話そのものに残る研ぎ澄まされた理解だけです。これは、同じインタビューを ADR とグロッサリーという永続的な記録として残す [grill-with-docs](https://aihero.dev/skills-grill-with-docs) との意図的な対比です。

## 位置づけ (Where it fits)

`grill-me` は、プランを固める必要があるときにいつでも手に取れる単体スキル — ビルド前のストレステストです。[grilling](https://aihero.dev/skills-grilling) というプリミティブへの、ステートレスでユーザー起動 (User-invoked) の入口にあたります。最も近い隣人は [grill-with-docs](https://aihero.dev/skills-grill-with-docs) で、こちらは同じインタビューを行いつつ、決定内容を ADR とグロッサリーとしてさらに記録するステートフルな兄弟スキルです。成果をスペックとして書き残したい場合は、再度インタビューすることなく確定した理解を PRD にまとめる [to-prd](https://aihero.dev/skills-to-prd) に引き継いでください。どのフローが合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が案内します。

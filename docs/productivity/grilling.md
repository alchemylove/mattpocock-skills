クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=grilling
```

```bash
npx skills update grilling
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)

## 概要 (What it does)

`grilling` は、ビルドに入る前にプランや設計をストレステストする、容赦のないインタビューです。設計ツリー (design tree) を枝ごとに降りていき、決定同士の依存関係を1つずつ解決して、あなたとエージェントが同じ理解を共有するまで続きます。

一度に **1つの質問だけ** を投げかけ、あなたの回答を待ってから次に進みます — まとめてのリストは混乱を招くので決して行いません。それぞれの質問にはエージェント自身のおすすめの回答が添えられ、コードベースで解決できる質問はあなたに尋ねる代わりに自ら調べます。共通理解に達したとあなたが確認するまで、プランの実行には入りません。

## 使いどころ (When to reach for it)

`/grilling` と入力するか、タスクに合致すればエージェントが自動的に使います — これはユーザー専用の入口ではなく、根底にあるプリミティブです。

プランや設計にまだ弱い部分があり、コードを書く前にそれを表に出したいときに使いましょう。実際にはこの名前で直接呼び出すよりも、2つのラッパーのどちらかを通して使うことがほとんどです。普通の grilling セッションには [grill-me](https://aihero.dev/skills-grill-me) を、セッション中に ADR とグロッサリーも書き残したい場合は [grill-with-docs](https://aihero.dev/skills-grill-with-docs) を使ってください。

## 設計ツリー (design tree)

ここでのメンタルモデルは **設計ツリー (design tree)** です。あらゆるプランは決定へと枝分かれし、決定同士は互いに依存し合っています。`grilling` はそのツリーを一度に1ノードずつ降りていくので、早い段階での答えが後続の質問の内容を変えることがあります。質問が1つずつ、かつ依存関係の順序で届くのはそのためです — 並行した質問の奔流は、インタビューを共通理解へ収束させる構造を失わせてしまいます。

## 意図的な切り出し

`grilling` はインタビュー手法の **唯一の正典 (single source of truth)** であり、インタビューを必要とするあらゆるスキルがそれぞれ車輪の再発明をするのではなく参照できるように、モデル起動 (Model-invoked) の **プリミティブ (primitive)** として切り出されています。[grill-me](https://aihero.dev/skills-grill-me) と [grill-with-docs](https://aihero.dev/skills-grill-with-docs) はそのユーザー起動 (User-invoked) の2つの入口ですが、[improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) と [triage](https://aihero.dev/skills-triage) も自らの判断を検証するためにこれに頼っています。

この手法を一箇所にまとめておくことで、ADR の作成やチケットの整形を伴わずに、純粋にインタビューだけが欲しいときにも直接呼び出せるようになります。

## 位置づけ (Where it fits)

`grilling` はメインのビルドチェーンの土台となるインタビューの **プリミティブ (primitive)** です。[grill-with-docs](https://aihero.dev/skills-grill-with-docs) がこれを実行してコンテキストを研ぎ澄ませてから、[to-prd](https://aihero.dev/skills-to-prd) がスペックを書きます。どの入口が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が案内します。

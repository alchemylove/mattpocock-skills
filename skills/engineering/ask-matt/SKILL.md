---
name: ask-matt
description: 状況に合う skill やフローを尋ねる。このリポジトリの skills 全体を束ねるルーター。
disable-model-invocation: true
---

# Ask Matt

すべての skill を覚えていられるわけではないので、尋ねる。

**flow** とは skills を通る経路である。ほとんどの経路は 1 つの **main flow** に沿って進み、2 つの **on-ramp** がそこへ合流する。それ以外は standalone か、その下を流れる vocabulary layer である。

## main flow: idea → ship

ほとんどの作業が通る経路。アイデアがあり、それを形にしたい。

1. **`/grill-with-docs`** — インタビューによってアイデアを研ぎ澄ます。**codebase がある**場合はここから始める: stateful であり、学んだことを `CONTEXT.md` と ADR に保持する。（codebase がない場合は `/grill-me` を使う — Standalone を参照。どちらも同じ `/grilling` primitive を実行するが、`grill-with-docs` は記録を残す方である。）
2. **分岐 — すべての疑問を会話だけで解決できるか?** 疑問に runnable な答えが必要な場合（state、business logic、目で見る必要がある UI）、prototype への寄り道を経由する。行き来は両方向とも **`/handoff`** で橋渡しする（Crossing sessions を参照）:
   - **`/handoff`** で送り出し、そのファイルを対象に新しいセッションを開き、
   - **`/prototype`** で throwaway code によって疑問に答え、
   - **`/handoff`** で学んだことを元の idea スレッドに戻し、そこから参照する。
3. **分岐 — これは複数セッションにまたがる build か?**
   - **Yes** → **`/to-prd`**（スレッドを PRD に変換する）→ **`/to-issues`**（PRD を独立して着手可能な issue に分割する）。issue は独立しているため、**issue ごとに context をクリアする**: issue ごとに新しいセッションを開始し、PRD と対象の 1 issue を渡して **`/implement`** を起動する。
   - **No** → 同じ context window のままここで **`/implement`**。

   いずれの場合も、**`/implement`** は内部で **`/tdd`** を駆動して各 issue を build し — 一度に 1 つの red-green slice を進め — 最後に commit する前に diff の two-axis review（Standards + Spec）である **`/code-review`** を実行して締めくくる。full spec なしに具体的な behaviour を test-first で build したいだけなら **`/tdd`** 単体を、fixed point に対して branch や PR をレビューしたいときは **`/code-review`** 単体を使う。

### Context hygiene

手順 1〜3 は **1 つの途切れない context window** に保つ — `/to-issues` の後まで compact も clear もしない — これにより grilling、PRD、issues が同じ思考の上に積み上がる。各 `/implement` はその後、issue から出発してまっさらに始まる。

ここでの制約は **[smart zone](https://www.aihero.dev/ai-coding-dictionary/smart-zone)** である: state-of-the-art なモデルでもおよそ 120k トークンという、モデルがまだ鋭く推論できる window のこと。`/to-issues` の前にセッションがこれに近づいたら、劣化した状態で押し進めず、`/handoff` して新しいスレッドで続ける。

## On-ramps

作業を生み出す起点となる状況で、その後 main flow に合流する。

- **バグや要望が積み上がってきた** → **`/triage`**。issue を triage roles に沿って進め、agent-ready な issue を生み出し、それを後で **`/implement`** が拾う。

  Triage は**自分が作成していない** issue のためだけにある — バグ報告、飛び込みの feature request、生の状態で届くものすべて。`/to-issues` が生成した issue はすでに agent-ready なので、**triage しない**。

- **何かが壊れている** → **`/diagnosing-bugs`**。厄介なもの向け: 一目見ただけでは解決しないバグ、間欠的な flake、2 つの known-good な状態の間に忍び込んだ regression。**tight feedback loop** — すでに*この*バグで red になる 1 つのコマンド — を手にするまで理論化を拒み、その後 regression test で修正する。post-mortem の結果、バグを封じ込める良い seam が存在しないという発見に至った場合は **`/improve-codebase-architecture`** に引き継ぐ。

## Codebase health

feature work ではなく — 保守。

- **`/improve-codebase-architecture`** — codebase を agent が操作しやすい状態に保つため、手が空いたときにいつでも実行する。**deepening opportunities** を洗い出す。1 つを選ぶと、main flow の `/grill-with-docs` へ持ち込める*アイデアが生まれる*。候補を見つけるのが調査であり、選んだものを設計する作業台が **`/codebase-design`**（下記）である。

## Vocabulary underneath

他の skills の *下を* 流れる、model-invoked な 2 つの reference — それぞれがその vocabulary の single source of truth である。プロセスではなく**言葉**そのものが問題のときは直接使う。あるいは上記の skills がこれらを取り込む。

- **`/domain-modeling`** — プロジェクトの *domain* language を研ぎ澄ます: 曖昧な用語に異議を唱え、overloaded な語（"account" が 3 つの役割を兼ねている、など）を解決し、覆しにくい決定を ADR として記録する。`/grill-with-docs` が `CONTEXT.md` を綺麗な glossary に保つために駆動する active な discipline である。
- **`/codebase-design`** — module の *形* を設計するための deep-module vocabulary（module、interface、depth、seam、adapter、leverage、locality）: 小さな interface の背後に多くの behaviour を、綺麗な seam に配置する。`/tdd` と `/improve-codebase-architecture` の両方がこの言葉を話す。

## Crossing sessions

- **`/handoff`** — スレッドが満杯になったとき、あるいは分岐する必要があるとき（例えば `/prototype` セッションへ）、会話を markdown ファイルに圧縮する。その場で続けるのではなく、**新しいセッションを開いてそのファイルを参照する**ことで context を運ぶ。context window 間の橋であり、どちら向きにも使える。**新しいセッション**が欲しいが**現在の会話を保存**しておく必要があるときに使う。
- **`/compact`**（built-in）— **同じ会話**にとどまり、以前のターンを要約させる。逐語的な履歴を失っても構わない、**フェーズ間の意図的な区切り**で使う。フェーズの途中で compact しない — agent が迷子になりうる。`/handoff` は fork し、`/compact` は続行する。

## Standalone

main flow から完全に外れたもの。

- **`/grill-me`** — `/grill-with-docs` と同じ容赦ないインタビューだが、**codebase がない**とき向け。Stateless: ローカルに何も保存せず、`CONTEXT.md` も作らない。repo に存在しない plan や design を研ぎ澄ますときに使う。
- **`/prototype`** — 1 つの design question に答える、小さな throwaway program: この state model は正しく感じられるか、あるいはこの UI はどう見えるべきか。初日から throwaway — 答えは残し、コードは削除する。main flow の手順 2 での寄り道だが、design question が紙の上では決めがたいときはいつでも使ってよい。
- **`/research`** — 読み込みの下働きを **background agent** に委譲する: **primary sources** に基づいて疑問を調査し、引用付きの Markdown ファイルを repo に残す。それが読んでいる間も作業を続けられる。生成されるファイルは main flow の `/grill-with-docs` に*持ち込む*ものである — research は思考の材料であり、それに取って代わるものではない。
- **`/teach`** — 現在のディレクトリを stateful な workspace として使い、複数セッションにわたって概念を学ぶ。
- **`/writing-great-skills`** — skills をうまく書き、編集するための reference。

## Precondition

**`/setup-matt-pocock-skills`** — 最初の engineering flow の前に実行し、他の skills が前提とする issue tracker、triage labels、doc layout を設定する。custom issue tracker でも動作する。

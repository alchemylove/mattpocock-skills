---
name: improve-codebase-architecture
description: codebase をスキャンして deepening の機会を見つけ、視覚的な HTML レポートとして提示し、選んだ箇所について grilling を進める。
disable-model-invocation: true
---

# Improve Codebase Architecture

architectural friction を表に出し、**deepening opportunities** — shallow な module を deep なものに変える refactor — を提案する。狙いは testability と AI-navigability である。

このコマンドはプロジェクトの domain model に _informed_ され、共有された design vocabulary の上に構築されている:

- architecture の vocabulary（**module**、**interface**、**depth**、**seam**、**adapter**、**leverage**、**locality**）とその原則（the deletion test、"the interface is the test surface"、"one adapter = hypothetical seam, two = real"）については `/codebase-design` skill を実行する。すべての提案でこれらの用語をそのまま使う — "component"、"service"、"API"、"boundary" に流れない。
- `CONTEXT.md` の domain language は良い seam に名前を与える。`docs/adr/` の ADR はこのコマンドが再び論争すべきでない決定を記録している。

## Process

### 1. Explore

まず、プロジェクトの domain glossary（`CONTEXT.md`）と、触れる領域の ADR を読む。

次に Agent tool を `subagent_type=Explore` で使い、codebase を歩く。硬直したヒューリスティックに従わず、有機的に探索し、friction を感じた場所をメモする:

- 1 つの concept を理解するのに、多くの小さな module を行き来する必要がある場所はどこか?
- module が **shallow** — interface が implementation とほぼ同じくらい複雑 — な場所はどこか?
- testability のためだけに pure function が抽出されたが、本物のバグはそれがどう呼ばれるかに隠れている（**locality** が無い）場所はどこか?
- 密結合な module がその seam を越えて漏れている場所はどこか?
- codebase のどの部分がテストされていない、あるいは現在の interface を通してテストしにくいか?

shallow だと疑うものには **deletion test** を適用する: それを削除したら複雑さが集中するか、それとも単に移動するだけか? 「yes, 集中する」が求めている signal である。

### 2. 候補を HTML レポートとして提示する

repo に何も残らないよう、自己完結した HTML ファイルを OS の temp directory に書く。temp dir は `$TMPDIR` から解決し、無ければ `/tmp`（Windows なら `%TEMP%`）にフォールバックし、`<tmpdir>/architecture-review-<timestamp>.html` に書いて実行のたびに新しいファイルになるようにする。ユーザーのためにそれを開く — Linux では `xdg-open <path>`、macOS では `open <path>`、Windows では `start <path>` — そして絶対パスを伝える。

レポートは layout と styling に **CDN 経由の Tailwind** を、graph/flow/sequence が構造を確実に伝える場面の diagram に **CDN 経由の Mermaid** を使う。Mermaid と手作りの CSS/SVG visual を混ぜる — 関係が graph 状のとき（call graph、依存関係、sequence）は Mermaid を、もっと editorial なものが欲しいとき（mass diagram、断面図、collapse アニメーション）は手作りの div/SVG を使う。各候補には **before/after visualisation** を付ける。visual であること。

各候補について、以下を含むカードを描画する:

- **Files** — どのファイル/module が関係するか
- **Problem** — なぜ現在の architecture が friction を起こしているか
- **Solution** — 何が変わるかの平易な説明
- **Benefits** — locality と leverage の観点から説明し、テストがどう改善するか
- **Before / After diagram** — 左右並び、カスタム描画で、shallowness と deepening を図示する
- **Recommendation strength** — `Strong`、`Worth exploring`、`Speculative` のいずれかを badge として表示

レポートの最後に **Top recommendation** セクションを置く: どの候補を最初に取り組むべきか、そしてなぜか。

**domain には CONTEXT.md の vocabulary を、architecture には `/codebase-design` の vocabulary を使う。** `CONTEXT.md` が "Order" を定義しているなら、"FooBarHandler" でも "Order service" でもなく "the Order intake module" と話す。

**ADR との衝突**: 候補が既存の ADR と矛盾する場合、その ADR を再考する価値があるほど friction が本物であるときにのみ表に出す。カードにはっきり印を付ける（例: 警告の callout: _"contradicts ADR-0007 — but worth reopening because…"_）。ADR が禁じている理論上の refactor をすべて列挙しない。

完全な HTML scaffold、diagram のパターン、styling の指針は [HTML-REPORT.md](HTML-REPORT.md) を参照。

まだ interface は提案しない。ファイルを書いたら、ユーザーに尋ねる: 「このうちどれを深掘りしたいですか?」

### 3. Grilling loop

ユーザーが候補を選んだら、`/grilling` skill を実行し、一緒に design tree を歩く — 制約、依存関係、深められた module の形、seam の背後に何が座るか、どのテストが生き残るか。

決定が固まるにつれて副作用がその場で起きる — domain model を最新に保つため `/domain-modeling` skill を実行する:

- **`CONTEXT.md` に無い concept にちなんで深められた module に名前を付けた?** その用語を `CONTEXT.md` に追加する。ファイルが無ければ遅延生成する。
- **会話中に曖昧な用語を研ぎ澄ました?** その場で `CONTEXT.md` を更新する。
- **ユーザーが load-bearing な理由で候補を却下した?** ADR を提案する。フレーミングは: _"将来の architecture review がこれを再提案しないよう、ADR として記録しましょうか?"_ その理由が、将来の探索者が同じことを再提案しないために実際に必要となる場合にのみ提案する — 一時的な理由（「今はその価値がない」）や自明な理由はスキップする。
- **深められた module の代替 interface を探りたい?** `/codebase-design` skill を実行し、その design-it-twice の parallel sub-agent pattern を使う。

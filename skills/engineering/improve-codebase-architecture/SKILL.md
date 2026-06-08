---
name: improve-codebase-architecture
description: Find deepening opportunities in a codebase, informed by the domain language in CONTEXT.md and the decisions in docs/adr/. Use when the user wants to improve architecture, find refactoring opportunities, consolidate tightly-coupled modules, or make a codebase more testable and AI-navigable.
---

# コードベースアーキテクチャの改善 (Improve Codebase Architecture)

architectural friction を surface し、**deepening opportunities** — shallow module を deep module に変える refactor — を提案する。目的は testability と AI-navigability である。

## 用語集 (Glossary)

すべての提案でこれらの term を正確に使う。一貫した言語が要点である — "component"、"service"、"API"、"boundary" に drift しない。完全な定義は [LANGUAGE.md](LANGUAGE.md)。

- **Module** — interface と implementation を持つもの（function、class、package、slice）。
- **Interface** — caller が module を使うために知るべきすべて: types、invariants、error modes、ordering、config。type signature だけではない。
- **Implementation** — 内部のコード。
- **Depth** — interface における leverage: 小さな interface の背後に多くの behaviour。**Deep** = high leverage。**Shallow** = interface が implementation とほぼ同じ複雑さ。
- **Seam** — interface が存在する場所; in place を編集せずに behaviour を変えられる場所。（"boundary" ではなくこれを使う。）
- **Adapter** — seam で interface を満たす concrete なもの。
- **Leverage** — caller が depth から得るもの。
- **Locality** — maintainer が depth から得るもの: change、bugs、knowledge が 1 か所に集中。

主要原則（完全なリストは [LANGUAGE.md](LANGUAGE.md)）:

- **Deletion test**: module を削除したと想像する。複雑さが消えれば pass-through だった。複雑さが N 個の caller に再出現すれば、その存在意義があった。
- **The interface is the test surface.**
- **One adapter = hypothetical seam. Two adapters = real seam.**

この skill はプロジェクトの domain model に _informed_ される。domain language は good seam に名前を与え、ADR は skill が再 litigate すべきでない決定を記録する。

## プロセス (Process)

### 1. 探索 (Explore)

まずプロジェクトの domain glossary と、触る領域の ADR を読む。

次に Agent tool で `subagent_type=Explore` を使いコードベースを歩く。硬い heuristic に従わない — 有機的に探索し、friction を感じる場所を記録する:

- 1 つの概念を理解するのに、多くの小さな module を行き来する必要がある場所は？
- module が **shallow** な場所は？ — interface が implementation とほぼ同じ複雑さ。
- testability のためだけに pure function が抽出されたが、real bug は呼び出し方に隠れる場所（**locality** がない）は？
- tightly-coupled module が seam を越えて leak する場所は？
- codebase のどの部分が untested、または現在の interface 経由では test しにくいか？

shallow と疑うものに **deletion test** を適用する: 削除すると複雑さが集中するか、単に移動するだけか？"yes, concentrates" が欲しいシグナルである。

### 2. 候補を HTML report として提示する (Present candidates as an HTML report)

repo に何も置かないよう、自己完結型 HTML ファイルを OS temp directory に書く。temp dir は `$TMPDIR` から解決し、なければ `/tmp`（Windows では `%TEMP%`）にフォールバックし、`<tmpdir>/architecture-review-<timestamp>.html` に書いて各実行で新しいファイルにする。ユーザー向けに開く — Linux では `xdg-open <path>`、macOS では `open <path>`、Windows では `start <path>` — 絶対パスを伝える。

report はレイアウトとスタイリングに **Tailwind via CDN**、構造を graph/flow/sequence で確実に伝えられる場合は **Mermaid via CDN** を使う。Mermaid と hand-crafted CSS/SVG を混ぜる — 関係が graph 形状（call graphs、dependencies、sequences）なら Mermaid、より editorial な表現（mass diagrams、cross-sections、collapse animations）なら hand-built divs/SVG。各候補に **before/after visualisation** を付ける。視覚的であること。

各候補は以前と同じ template だが、card としてレンダリングする:

- **Files** — 関与する files/modules
- **Problem** — 現在の architecture が friction を生む理由
- **Solution** — 何が変わるかの平易な英語説明
- **Benefits** — locality と leverage の観点での説明、test がどう改善するか
- **Before / After diagram** — 並列、custom-drawn、shallowness と deepening を示す
- **Recommendation strength** — `Strong`、`Worth exploring`、`Speculative` のいずれか、badge としてレンダリング

report の末尾に **Top recommendation** セクション: 最初に着手する候補とその理由。

**domain には CONTEXT.md の語彙、architecture には [LANGUAGE.md](LANGUAGE.md) の語彙を使う。** `CONTEXT.md` が "Order" を定義していれば、"Order intake module" と言う — "FooBarHandler" でも "Order service" でもない。

**ADR conflicts**: 候補が既存 ADR と矛盾する場合、ADR を再検討するに足る real friction があるときだけ surface する。card に明確にマークする（例: warning callout: _"contradicts ADR-0007 — but worth reopening because…"_）。ADR が forbid する理論上の refactor をすべて列挙しない。

完全な HTML scaffold、diagram patterns、styling guidance は [HTML-REPORT.md](HTML-REPORT.md)。

まだ interface を提案しない。ファイル書き込み後、ユーザーに尋ねる:「Which of these would you like to explore?」

### 3. Grilling loop

ユーザーが候補を選んだら、grilling conversation に入る。design tree を一緒に歩く — constraints、dependencies、deepened module の形、seam の背後に何があるか、どの test が残るか。

意思決定が crystallize するとき、side effect はインラインで起きる:

- **`CONTEXT.md` にない concept 名の deepened module を命名する？** term を `CONTEXT.md` に追加 — `/grill-with-docs` と同じ規律（[CONTEXT-FORMAT.md](../grill-with-docs/CONTEXT-FORMAT.md)）。存在しなければ lazy に作成。
- **会話中に fuzzy term を sharpen する？** その場で `CONTEXT.md` を更新。
- **load-bearing な理由で候補を reject する？** ADR を提案し、_「Want me to record this as an ADR so future architecture reviews don't re-suggest it?」_ と frame する。将来の explorer が同じ提案を避けるのに実際に必要な理由のときだけ offer — ephemeral な理由（"not worth it right now"）や自明な理由は skip。[ADR-FORMAT.md](../grill-with-docs/ADR-FORMAT.md) を参照。
- **deepened module の代替 interface を探索したい？** [INTERFACE-DESIGN.md](INTERFACE-DESIGN.md) を参照。

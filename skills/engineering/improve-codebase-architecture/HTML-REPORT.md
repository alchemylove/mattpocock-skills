# HTML Report Format

architectural review は、OS の temp directory 内の単一の自己完結した HTML ファイルとして描画される。Tailwind と Mermaid はどちらも CDN から読み込む。Mermaid は graph 状の diagram を確実に処理する。手作りの div と inline SVG はもっと editorial な visual（mass diagram、cross-section）を処理する。両方を混ぜる — Mermaid だけに頼らない、そうしないと汎用的に見え始める。

## Scaffold

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Architecture review — {{repo name}}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="module">
      import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
      mermaid.initialize({ startOnLoad: true, theme: "neutral", securityLevel: "loose" });
    </script>
    <style>
      /* small custom layer for things Tailwind doesn't cover cleanly:
         dashed seam lines, hand-drawn-feeling arrow heads, etc. */
      .seam { stroke-dasharray: 4 4; }
      .leak { stroke: #dc2626; }
      .deep { background: linear-gradient(135deg, #0f172a, #1e293b); }
    </style>
  </head>
  <body class="bg-stone-50 text-slate-900 font-sans">
    <main class="max-w-5xl mx-auto px-6 py-12 space-y-12">
      <header>...</header>
      <section id="candidates" class="space-y-10">...</section>
      <section id="top-recommendation">...</section>
    </main>
  </body>
</html>
```

## Header

repo 名、日付、そして compact な凡例: solid box = module、dashed line = seam、red arrow = leakage、thick dark box = deep module。導入の段落は無し — すぐに candidates に入る。

## Candidate card

diagram が重みを担う。prose は少なく、平易で、glossary の用語（`/codebase-design` skill から）を気取らず使う。

各 candidate は 1 つの `<article>`:

- **Title** — 短く、deepening に名前を付ける（例: "Collapse the Order intake pipeline"）。
- **Badge row** — recommendation strength（`Strong` = emerald、`Worth exploring` = amber、`Speculative` = slate）、加えて dependency category のタグ（`in-process`、`local-substitutable`、`ports & adapters`、`mock`）。
- **Files** — monospace のリスト、`font-mono text-sm`。
- **Before / After diagram** — 目玉。左右 2 列。下記のパターンを参照。
- **Problem** — 1 文。何が痛むか。
- **Solution** — 1 文。何が変わるか。
- **Wins** — 各 6 語以内の bullet。例: "Tests hit one interface"、"Pricing logic stops leaking"、"Delete 4 shallow wrappers"。
- **ADR callout**（該当すれば）— amber 色の box に 1 行。

説明の段落は無し。diagram を理解するのに段落が必要なら、diagram を描き直す。

## Diagram patterns

candidate に合うパターンを選ぶ。混ぜる。すべての diagram を同じに見せない — 多様性もポイントの一部。

### Mermaid graph（dependencies / call flow の主力）

「X が Y を呼び、Y が Z を呼び、見てくれこの混乱を」というのが要点のときは Mermaid の `flowchart` や `graph` を使う。急に降ってきた感じにならないよう、Tailwind でスタイルされた card で包む。classDef でスタイルし、leakage の edge を赤に、deep module を dark に色付ける。sequence diagram は「before: 6 回の round-trip; after: 1 回」によく合う。

```html
<div class="rounded-lg border border-slate-200 bg-white p-4">
  <pre class="mermaid">
    flowchart LR
      A[OrderHandler] --> B[OrderValidator]
      B --> C[OrderRepo]
      C -.leak.-> D[PricingClient]
      classDef leak stroke:#dc2626,stroke-width:2px;
      class C,D leak
  </pre>
</div>
```

### Hand-built boxes-and-arrows（Mermaid の layout がうまくいかないとき）

module を、border と label を持つ `<div>` として表す。矢印は、relative な container の上に絶対配置された inline SVG の `<line>` や `<path>` 要素として表す。"after" の diagram を、内部が greyed-out された 1 つの太い border の deep module のように見せたいとき、これを使う — Mermaid はそれを適切な重みで描画してくれない。

### Cross-section（layered な shallowness に良い）

呼び出しが通過する layer を示すために水平な帯（`h-12 border-l-4`）を積み重ねる。Before: 何もしていない 6 つの薄い layer。After: 統合された責務がラベル付けされた 1 つの厚い帯。

### Mass diagram（"interface as wide as implementation" に良い）

module ごとに 2 つの矩形 — 1 つは interface の surface area、もう 1 つは implementation。Before: interface の矩形が implementation の矩形とほぼ同じ高さ（shallow）。After: interface の矩形は短く、implementation の矩形は高い（deep）。

### Call-graph collapse

Before: 入れ子の box として描画された関数呼び出しの木。After: 同じ木が 1 つの box に折り畳まれ、今や internal になった呼び出しがその中に薄く表示される。

## Style guidance

- corporate-dashboard ではなく editorial 寄り。余白を多めに。見出しに serif は任意（`font-serif` は stone/slate とよく合う）。
- 色は控えめに: 1 つの accent（emerald または indigo）に加えて、leakage には red、warning には amber。
- diagram は高さ約 320px に保ち、before/after が scroll なしで左右に快適に収まるようにする。
- diagram 内の module label には `text-xs uppercase tracking-wider` を使う — UI ではなく schematic として読めるべき。
- script は Tailwind の CDN と Mermaid の ESM import のみ。それ以外、レポートは静的である — app code は無く、Mermaid 自身の描画を超えたインタラクティブ性は無い。

## Top recommendation section

やや大きな card 1 つ。candidate 名、なぜかを 1 文、そのカードへの anchor link。それだけ。

## Tone

平易な英語で簡潔に — ただし architectural な名詞と動詞は `/codebase-design` skill からそのまま持ってくる。簡潔さは、そこから逸脱する言い訳にはならない。

**そのまま使う:** module、interface、implementation、depth、deep、shallow、seam、adapter、leverage、locality。

**決して置き換えない:** component、service、unit（module の代わりに）· API、signature（interface の代わりに）· boundary（seam の代わりに）· layer、wrapper（module を意味するときに、module の代わりに）。

**このスタイルに合う言い回し:**

- "Order intake module is shallow — interface nearly matches the implementation."
- "Pricing leaks across the seam."
- "Deepen: one interface, one place to test."
- "Two adapters justify the seam: HTTP in prod, in-memory in tests."

**Wins の bullet** は glossary の用語で利得を名指しする: *"locality: bugs concentrate in one module"*、*"leverage: one interface, N call sites"*、*"interface shrinks; implementation absorbs the wrappers"*。*"easier to maintain"* や *"cleaner code"* とは書かない — それらの用語は glossary に無く、そこにいる資格が無い。

hedging も、前置きも、"it's worth noting that…" も無し。文が bullet になり得るなら、bullet にする。bullet を削れるなら、削る。用語が `/codebase-design` の glossary に無いなら、新しく発明する前に glossary にあるものを使う。

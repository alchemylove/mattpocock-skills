# HTML レポート形式 (HTML Report Format)

architectural review は OS temp directory に単一の self-contained HTML ファイルとして出力する。Tailwind と Mermaid は CDN から。Mermaid は graph 形状の diagram を信頼して扱う。hand-built divs と inline SVG はより editorial な visual（mass diagrams、cross-sections）向け。2 つを混ぜる — すべて Mermaid に頼らない。generic に見え始める。

## スキャフォールド (Scaffold)

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

## ヘッダー (Header)

repo 名、日付、コンパクトな legend: solid box = module、dashed line = seam、red arrow = leakage、thick dark box = deep module。導入段落なし — すぐ candidates へ。

## 候補カード (Candidate card)

diagram が重みを担う。prose は sparse、plain、[LANGUAGE.md](LANGUAGE.md) の glossary 用語を ceremony なしで使う。

各 candidate は 1 つの `<article>`:

- **Title** — 短く、deepening を名指し（例: "Collapse the Order intake pipeline"）
- **Badge row** — recommendation strength（`Strong` = emerald、`Worth exploring` = amber、`Speculative` = slate）、dependency category の tag（`in-process`、`local-substitutable`、`ports & adapters`、`mock`）
- **Files** — monospaced list、`font-mono text-sm`
- **Before / After diagram** — 中心。2 列、横並び。下記パターン参照
- **Problem** — 1 文。何が痛いか
- **Solution** — 1 文。何が変わるか
- **Wins** — bullets、各 ≤6 words。例: "Tests hit one interface"、"Pricing logic stops leaking"、"Delete 4 shallow wrappers"
- **ADR callout**（該当時）— amber-tinted box に 1 行

説明段落は不要。diagram に段落が必要なら diagram を描き直す。

## ダイアグラムパターン (Diagram patterns)

candidate に合うパターンを選ぶ。混ぜる。すべて同じに見せない — 多様性も目的の一部。

### Mermaid graph（dependencies / call flow の workhorse）

「X calls Y calls Z、見てこの混乱」が要点のとき `flowchart` または `graph` を使う。Tailwind-styled card で包み、宙に浮いた感じを防ぐ。classDef で leakage edges を赤、deep module を暗色に。sequence diagram は「before: 6 round-trips; after: 1」に向く。

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

### Hand-built boxes-and-arrows（Mermaid の layout が邪魔なとき）

modules を border と label 付き `<div>`。arrows は relative container 上に absolutely 配置した inline SVG `<line>` または `<path>`。「after」で 1 つの thick-bordered deep module と greyed-out internals を表現したいとき — Mermaid では適切な重みにならない。

### Cross-section（layered shallowness に向く）

horizontal bands（`h-12 border-l-4`）を積み、call が通過する layers を示す。Before: 何もしない 6 つの thin layers。After: consolidated responsibility をラベルした 1 つの thick band。

### Mass diagram（「interface as wide as implementation」に向く）

module ごとに 2 つの rectangle — interface surface area と implementation。Before: interface rectangle が implementation rectangle とほぼ同じ高さ（shallow）。After: interface rectangle は短く、implementation rectangle は高い（deep）。

### Call-graph collapse

Before: nested boxes で描いた function calls の tree。After: 同じ tree を 1 box に collapse。内部になった calls は faded で内部表示。

## スタイルガイダンス (Style guidance)

- corporate-dashboard ではなく editorial 寄り。余白を多めに。見出しに serif 任意（`font-serif` は stone/slate と相性がよい）
- 色は控えめ: 1 accent（emerald または indigo）+ leakage 用 red + warning 用 amber
- diagram は ~320px 高さ程度。before/after が scroll なしで横並びに収まる
- diagram 内の module labels に `text-xs uppercase tracking-wider` — schematic として読む。UI ではない
- script は Tailwind CDN と Mermaid ESM import のみ。それ以外は static — app code なし、Mermaid 自身の rendering 以外の interactivity なし

## トップ推奨セクション (Top recommendation section)

1 つの大きな card。candidate 名、なぜか 1 文、その card への anchor link。以上。

## トーン (Tone)

Plain English、簡潔 — ただし architectural nouns と verbs は [LANGUAGE.md](LANGUAGE.md) からそのまま。簡潔さは drift の言い訳にならない。

**Use exactly:** module, interface, implementation, depth, deep, shallow, seam, adapter, leverage, locality.

**Never substitute:** component, service, unit (for module) · API, signature (for interface) · boundary (for seam) · layer, wrapper (for module, when you mean module).

**スタイルに合う言い回し:**

- "Order intake module is shallow — interface nearly matches the implementation."
- "Pricing leaks across the seam."
- "Deepen: one interface, one place to test."
- "Two adapters justify the seam: HTTP in prod, in-memory in tests."

**Wins bullets** は glossary 用語で gain を名指し: *"locality: bugs concentrate in one module"*、*"leverage: one interface, N call sites"*、*"interface shrinks; implementation absorbs the wrappers"*。*"easier to maintain"* や *"cleaner code"* は書かない — glossary にない用語で場所を取らない。

hedging なし、throat-clearing なし、「it's worth noting that…」なし。文が bullet になれるなら bullet に。bullet を切れるなら切る。[LANGUAGE.md](LANGUAGE.md) にない用語なら、新しい語を発明する前に該当する語を探す。

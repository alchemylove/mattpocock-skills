# Interface 設計 (Interface Design)

ユーザーが選んだ deepening candidate の代替 interface を探索したいとき、この parallel sub-agent パターンを使う。"Design It Twice"（Ousterhout）に基づく — 最初のアイデアが最良である可能性は低い。

[LANGUAGE.md](LANGUAGE.md) の語彙 — **module**、**interface**、**seam**、**adapter**、**leverage** — を使用。

## プロセス (Process)

### 1. 問題空間を枠組む

sub-agents を起動する前に、選んだ candidate についてユーザー向けの問題空間の説明を書く:

- 新しい interface が満たす必要がある constraints
- 依存する dependencies と、どのカテゴリに属するか（[DEEPENING.md](DEEPENING.md) 参照）
- constraints を具体化するための大まかな illustrative code sketch — 提案ではなく、constraints を地に足につける手段

これをユーザーに示し、すぐ Step 2 に進む。ユーザーが読み考えている間、sub-agents は parallel に動く。

### 2. sub-agents を起動する

Agent tool で 3 つ以上の sub-agents を parallel に起動。各 agent は deepened module の **radically different** な interface を出力すること。

各 sub-agent には別々の technical brief（file paths、coupling details、[DEEPENING.md](DEEPENING.md) の dependency category、seam の背後にあるもの）を渡す。brief は Step 1 のユーザー向け problem-space 説明とは独立。各 agent に異なる design constraint を与える:

- Agent 1: "Minimize the interface — aim for 1–3 entry points max. Maximise leverage per entry point."
- Agent 2: "Maximise flexibility — support many use cases and extension."
- Agent 3: "Optimise for the most common caller — make the default case trivial."
- Agent 4（該当時）: "Design around ports & adapters for cross-seam dependencies."

brief には [LANGUAGE.md](LANGUAGE.md) の語彙と CONTEXT.md の語彙の両方を含め、各 sub-agent が architecture language とプロジェクトの domain language で一貫して命名する。

各 sub-agent の出力:

1. Interface（types、methods、params — 加えて invariants、ordering、error modes）
2. callers がどう使うかの usage example
3. seam の背後に implementation が何を隠すか
4. Dependency strategy と adapters（[DEEPENING.md](DEEPENING.md) 参照）
5. Trade-offs — leverage が高い所、薄い所

### 3. 提示して比較する

designs を順に提示しユーザーが各々を吸収できるようにし、その後 prose で比較。**depth**（interface における leverage）、**locality**（change が集中する場所）、**seam placement** で対比する。

比較後、自分の推奨を述べる: どの design が最も強いか、なぜ。異なる designs の要素がうまく組み合わさるなら hybrid を提案。opinionated に — ユーザーは menu ではなく強い read を欲している。

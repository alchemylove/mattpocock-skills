# Design It Twice

ユーザーが選んだ deepening 候補の代替 interface を探りたいとき、この parallel sub-agent pattern を使う。"Design It Twice"（Ousterhout）に基づく — 最初のアイデアが最良であることは滅多にない。

[SKILL.md](SKILL.md) の vocabulary — **module**、**interface**、**seam**、**adapter**、**leverage** — を使う。

## Process

### 1. 問題空間を枠付けする

sub-agent を spawn する前に、選ばれた候補の問題空間についてユーザー向けの説明を書く:

- 新しい interface が満たすべき制約
- それが依存するもの、そしてそれがどの category に属するか（[DEEPENING.md](DEEPENING.md) を参照）
- 制約を具体化するための、大まかで例示的な code sketch — 提案ではなく、制約を具体的にする手段に過ぎない

これをユーザーに見せ、すぐに Step 2 に進む。sub-agent が並列に作業している間、ユーザーは読んで考える。

### 2. sub-agent を spawn する

Agent tool を使い、3 つ以上の sub-agent を並列に spawn する。それぞれが、深められた module に対して**根本的に異なる** interface を生み出さなければならない。

各 sub-agent には別々の技術的な brief（ファイルパス、coupling の詳細、[DEEPENING.md](DEEPENING.md) からの dependency category、seam の背後に何があるか）をプロンプトとして与える。この brief は Step 1 のユーザー向けの問題空間説明とは独立している。各 agent に異なる設計上の制約を与える:

- Agent 1: "interface を最小化する — entry point は最大 1〜3 個を目指す。entry point あたりの leverage を最大化する。"
- Agent 2: "柔軟性を最大化する — 多くの use case と拡張をサポートする。"
- Agent 3: "最も一般的な caller に最適化する — デフォルトのケースを些細なものにする。"
- Agent 4（該当すれば）: "seam をまたぐ依存関係のために ports & adapters を中心に設計する。"

各 sub-agent が architecture の言葉とプロジェクトの domain language の両方に一貫した名前を付けられるよう、brief には [SKILL.md](SKILL.md) の vocabulary と CONTEXT.md の vocabulary の両方を含める。

各 sub-agent の出力:

1. Interface（型、メソッド、パラメータ — 加えて invariants、ordering、error modes）
2. caller がそれをどう使うかを示す使用例
3. implementation が seam の背後に何を隠すか
4. Dependency 戦略と adapters（[DEEPENING.md](DEEPENING.md) を参照）
5. Trade-offs — leverage が高い場所、薄い場所

### 3. 提示して比較する

ユーザーがそれぞれを吸収できるよう design を順番に提示し、それから prose で比較する。**depth**（interface における leverage）、**locality**（変更がどこに集中するか）、**seam placement** で対比する。

比較した後、自分自身の推奨を示す: どの design が最も強いと思うか、なぜか。異なる design の要素がうまく組み合わさるなら、hybrid を提案する。意見を持つこと — ユーザーはメニューではなく、力強い読み解きを求めている。

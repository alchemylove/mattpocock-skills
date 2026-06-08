---
name: design-an-interface
description: Generate multiple radically different interface designs for a module using parallel sub-agents. Use when user wants to design an API, explore interface options, compare module shapes, or mentions "design it twice".
---

# インターフェース設計 (Design an Interface)

"A Philosophy of Software Design" の "Design It Twice" に基づく: 最初のアイデアが最良である可能性は低い。根本的に異なる複数の設計を生成し、比較する。

## ワークフロー (Workflow)

### 1. 要件の収集 (Gather Requirements)

設計前に理解する:

- [ ] この module はどの問題を解決するか?
- [ ] caller は誰か? (他の module、外部ユーザー、test)
- [ ] 主要な操作は何か?
- [ ] 制約はあるか? (performance、compatibility、既存パターン)
- [ ] 内部に隠すべきもの vs 公開すべきものは?

確認: "What does this module need to do? Who will use it?"

### 2. 設計の生成 (並列 sub-agent) (Generate Designs (Parallel Sub-Agents))

Task tool で 3 つ以上の sub-agent を同時に起動する。各 agent は**根本的に異なる**アプローチを出すこと。

```
Prompt template for each sub-agent:

Design an interface for: [module description]

Requirements: [gathered requirements]

Constraints for this design: [assign a different constraint to each agent]
- Agent 1: "Minimize method count - aim for 1-3 methods max"
- Agent 2: "Maximize flexibility - support many use cases"
- Agent 3: "Optimize for the most common case"
- Agent 4: "Take inspiration from [specific paradigm/library]"

Output format:
1. Interface signature (types/methods)
2. Usage example (how caller uses it)
3. What this design hides internally
4. Trade-offs of this approach
```

### 3. 設計の提示 (Present Designs)

各設計を次とともに示す:

1. **Interface signature** — types、methods、params
2. **Usage examples** — caller が実際にどう使うか
3. **What it hides** — 内部に留める複雑さ

比較前に各アプローチを吸収できるよう、設計は順番に提示する。

### 4. 設計の比較 (Compare Designs)

すべての設計を示した後、次の観点で比較:

- **Interface simplicity**: method 数が少ない、params が単純
- **General-purpose vs specialized**: 柔軟性 vs 焦点
- **Implementation efficiency**: shape が効率的な内部実装を可能にするか
- **Depth**: 小さな interface が大きな複雑さを隠す (良い) vs 大きな interface と薄い実装 (悪い)
- **Ease of correct use** vs **ease of misuse**

trade-off は table ではなく prose で議論する。設計が最も乖離する点を強調する。

### 5. 統合 (Synthesize)

最良の設計はしばしば複数の選択肢の洞察を組み合わせる。確認:

- "Which design best fits your primary use case?"
- "Any elements from other designs worth incorporating?"

## 評価基準 (Evaluation Criteria)

"A Philosophy of Software Design" より:

**Interface simplicity**: method が少なく、params が単純 = 学習と正しい使用が容易。

**General-purpose**: 変更なしで将来のユースケースに対応できる。ただし過度の一般化に注意。

**Implementation efficiency**: interface shape が効率的な実装を可能にするか? それとも awkward な内部実装を強いるか?

**Depth**: 小さな interface が大きな複雑さを隠す = deep module (良い)。大きな interface と薄い実装 = shallow module (避ける)。

## アンチパターン (Anti-Patterns)

- sub-agent に似た設計を出させない — 根本的な違いを強制する
- 比較をスキップしない — 価値は対比にある
- 実装しない — これは純粋に interface shape について
- 実装工数で評価しない

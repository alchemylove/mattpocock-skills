# エンジニアリング (Engineering)

コード作業に毎日使う skills。

## ユーザー起動 (User-invoked)

あなたがタイプした場合にのみ到達可能（`disable-model-invocation: true`）。

- **[ask-matt](./ask-matt/SKILL.md)** — 状況に合う skill やフローを尋ねる。このリポジトリのユーザー起動 (User-invoked) skills 向けの router。
- **[grill-with-docs](./grill-with-docs/SKILL.md)** — grilling セッションと同時にプロジェクトの domain model を構築し、用語を研ぎ澄ませながら `CONTEXT.md` と ADR をその場で更新する。
- **[triage](./triage/SKILL.md)** — issue を、triage roles からなる state machine に通す。
- **[improve-codebase-architecture](./improve-codebase-architecture/SKILL.md)** — codebase をスキャンして deepening の機会を見つけ、視覚的な HTML レポートとして提示したのち、選んだ箇所について grill する。
- **[setup-matt-pocock-skills](./setup-matt-pocock-skills/SKILL.md)** — engineering skills 向けにこのリポジトリを設定する（issue tracker、triage labels、domain doc のレイアウト）。repo ごとに一度実行する。
- **[to-issues](./to-issues/SKILL.md)** — plan、spec、PRD を、vertical slice を使って独立して着手可能な issue に分解する。
- **[to-prd](./to-prd/SKILL.md)** — 現在の会話を PRD に変換し、issue tracker に公開する。

## モデル起動 (Model-invoked)

モデルとユーザーの両方から到達可能（モデルが自動的に使えるよう豊富なトリガーフレーズを持つ）。

- **[prototype](./prototype/SKILL.md)** — 設計上の疑問に答えるための使い捨て prototype を作る: state/logic 用の実行可能な terminal app、または切り替え可能な複数の UI variation。

- **[diagnosing-bugs](./diagnosing-bugs/SKILL.md)** — 難しいバグやパフォーマンス低下のための規律だった診断ループ: reproduce → minimise → hypothesise → instrument → fix → regression-test。
- **[research](./research/SKILL.md)** — 信頼度の高い一次情報源 (primary source) に基づいて疑問を調査し、結果を引用付きの Markdown ファイルとしてリポジトリに記録する。background agent として実行される。
- **[tdd](./tdd/SKILL.md)** — red-green-refactor loop による test-driven development。一度に 1 つの vertical slice ずつ機能を実装、またはバグを修正する。
- **[domain-modeling](./domain-modeling/SKILL.md)** — プロジェクトの domain model を能動的に構築・洗練する — 用語に異議を唱え、シナリオでストレステストし、`CONTEXT.md` と ADR をその場で更新する。
- **[codebase-design](./codebase-design/SKILL.md)** — deep module を設計するための共通の discipline と語彙: 小さな interface、綺麗な seam、その interface を通してテスト可能であること。
- **[code-review](./code-review/SKILL.md)** — 固定点からの diff を two-axis でレビューする: **Standards**（repo の coding standards と Fowler smell baseline に従っているか）と **Spec**（元の issue/PRD を忠実に実装しているか）。並列の sub-agent として実行される。

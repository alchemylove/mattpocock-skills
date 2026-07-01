# エンジニアリング (Engineering)

コード作業に毎日使う skills。

## ユーザー起動 (User-invoked)

あなたがタイプした場合にのみ到達可能（`disable-model-invocation: true`）。

- **[ask-matt](./ask-matt/SKILL.md)** — 状況に合う skill やフローを尋ねる。このリポジトリのユーザー起動 skills を束ねるルーター。
- **[grill-with-docs](./grill-with-docs/SKILL.md)** — 計画や設計を洗練するための容赦ないインタビュー。進めながら docs（ADR と glossary）も作成する。
- **[triage](./triage/SKILL.md)** — issue と外部 PR を、triage の役割からなる状態機械に通す — 分類し、検証し、必要なら grill し、エージェントがすぐ着手できる briefs を書く。
- **[improve-codebase-architecture](./improve-codebase-architecture/SKILL.md)** — codebase をスキャンして deepening の機会を見つけ、視覚的な HTML レポートとして提示し、選んだ箇所について grilling を進める。
- **[setup-matt-pocock-skills](./setup-matt-pocock-skills/SKILL.md)** — engineering skills 向けにこのリポジトリを設定する — issue tracker、triage ラベルの語彙、domain doc のレイアウトをセットアップする。他の engineering skills を初めて使う前に一度実行する。
- **[to-issues](./to-issues/SKILL.md)** — plan、spec、または PRD を、tracer-bullet の vertical slice を使って、プロジェクトの issue tracker 上で独立して着手可能な issue に分解する。
- **[to-prd](./to-prd/SKILL.md)** — 現在の会話を PRD に変換し、プロジェクトの issue tracker に公開する — インタビューはなく、すでに議論した内容をまとめるだけ。
- **[prototype](./prototype/SKILL.md)** — 設計を具体化するための使い捨てプロトタイプを作る — 状態やビジネスロジックの検討用に動作するターミナルアプリ、または1つの route から切り替えられる、まったく異なる複数の UI バリエーション。

## モデル起動 (Model-invoked)

モデルとユーザーの両方から到達可能（モデルが自動的に使えるよう豊富なトリガーフレーズを持つ）。

- **[diagnosing-bugs](./diagnosing-bugs/SKILL.md)** — 難しいバグやパフォーマンス低下に対する、規律ある diagnosis loop: 再現 → 最小化 → 仮説 → 計測 → 修正 → 回帰テスト。
- **[tdd](./tdd/SKILL.md)** — red-green-refactor loop による test-driven development。機能の構築やバグ修正を、vertical slice 単位で一つずつ進める。
- **[domain-modeling](./domain-modeling/SKILL.md)** — プロジェクトの domain model を積極的に構築・洗練する — 用語を glossary に照らして検証し、edge-case シナリオでストレステストを行い、`CONTEXT.md` と ADR をその場で更新する。
- **[codebase-design](./codebase-design/SKILL.md)** — 深いモジュールを設計するための共有の規律と語彙: 小さなインターフェースの後ろに多くの振る舞いを、クリーンな seam に配置し、そのインターフェースを通じてテスト可能にする。

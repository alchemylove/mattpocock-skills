# Skills 一覧（日本語）

このプロジェクト（`mattpocock-skills` リポジトリを開いた Claude Code セッション）で使える skill の一覧。以下の3グループに分けている。

1. **mattpocock/skills リポジトリの skill**（このリポジトリ本体。`skills/<bucket>/<name>/SKILL.md`）
2. **ビルトイン公式 Claude skill**（Claude Code に組み込みで提供されるもの）
3. **有効化されているプラグインの skill**（`~/.claude/settings.json` の `enabledPlugins` で有効なもの）

> 作成時点: upstream `mattpocock/skills` の `272f99b`（`main`）に同期した直後の状態（[skills-sh-mattpocock-skills-skill-glimmering-mitten.md](../../../../.claude/plans/) の Phase 0 完了時点）。

## 前提・判定根拠（on / off の見方）

- `/skills` コマンドを直接実行して確認したものではなく、以下から間接的に判定している:
  - **mattpocock skill**: `~/.claude/skills` と `~/.agents/skills` を確認したところ、このリポジトリの skill はシンボリックリンクされていない（`scripts/link-skills.sh` 未実行）。かつ、このセッション開始時に提示された「利用可能な skill 一覧」にも mattpocock 由来の skill 名は含まれていなかった。したがって **全件 off（未リンク）** と判定。`scripts/link-skills.sh` を実行すると `user` スコープで on になる。
  - **ビルトイン公式 skill**: セッション開始時の「利用可能な skill 一覧」に列挙されていたため **on**。
  - **プラグインの skill**: `~/.claude/settings.json` の `enabledPlugins` で `true` になっているプラグイン（`loop@loop`, `security-guidance@claude-plugins-official`）に属する skill を **on**、`false` のプラグイン（`claude-md-management`, `claude-code-setup`）は **off** と判定。
- **起動種別**: `SKILL.md` frontmatter に `disable-model-invocation: true` があれば「ユーザー起動 (User-invoked)」、なければ「モデル起動 (Model-invoked)」。
- **description（日本語訳）**: 技術用語（grilling, red-green-refactor, vertical slice, domain model, issue tracker, DDD, ubiquitous language 等）は英語のまま、それ以外を日本語化。翻訳ルールは repo メモリ `feedback_translation_rules.md` に準拠。
- **名前の衝突に注意**: mattpocock リポジトリの `engineering/code-review` skill と、ビルトイン公式の `code-review`（`/code-review`）は**別物**。前者はこのリポジトリ用にカスタマイズされた「Standards / Spec 2軸レビュー」、後者は Claude Code 組み込みの汎用コードレビュー skill。

---

## 1. mattpocock/skills リポジトリの skill

スコープは全件 `project`（このリポジトリのファイル）。on/off は前述の通り**全件 off**（`scripts/link-skills.sh` 実行で `user` スコープへ on 化可能）。

### 1-1. engineering/（promoted・`README.md` と `plugin.json` に登録必須）

| skill | 起動種別 | description（英語） | description（日本語訳） | 概要 |
|---|---|---|---|---|
| [ask-matt](../skills/engineering/ask-matt/SKILL.md) | ユーザー起動 | Ask which skill or flow fits your situation. A router over the skills in this repo. | 状況に合う skill やフローを尋ねる。このリポジトリの skills 全体を束ねるルーター。 | skill 選択ルーター |
| [codebase-design](../skills/engineering/codebase-design/SKILL.md) | モデル起動 | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary. | deep module を設計するための共通語彙。ユーザーがモジュールのインターフェースを設計・改善したい、deepening の機会を見つけたい、seam の置き場所を決めたい、コードをよりテスト可能・AI-navigable にしたい、または他の skill が deep-module の語彙を必要とするときに使う。 | モジュール設計の共通語彙 |
| [code-review](../skills/engineering/code-review/SKILL.md) | モデル起動 | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/PRD asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X". | 固定点（commit・branch・tag・merge-base）からの変更を、Standards（このリポジトリの明文化された coding standards に従っているか）と Spec（元の issue/PRD が求めた内容と一致するか）の2軸でレビューする。両方のレビューを並列の sub-agent で実行し、並べて報告する。ユーザーが branch・PR・作業中の変更をレビューしたい、または「review since X」を求めたときに使う。 | 2軸（Standards/Spec）レビュー |
| [diagnosing-bugs](../skills/engineering/diagnosing-bugs/SKILL.md) | モデル起動 | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. | 難しいバグやパフォーマンス低下のための診断ループ。ユーザーが「diagnose」「debug this」と言った、または何かが壊れている/例外を投げている/失敗している/遅いと報告したときに使う。 | バグ診断ループ |
| [domain-modeling](../skills/engineering/domain-modeling/SKILL.md) | モデル起動 | Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology or a ubiquitous language, record an architectural decision, or when another skill needs to maintain the domain model. | プロジェクトの domain model を構築・洗練する。ユーザーが domain の用語や ubiquitous language を明確にしたい、architectural decision を記録したい、または他の skill が domain model を維持する必要があるときに使う。 | domain model の構築 |
| [grill-with-docs](../skills/engineering/grill-with-docs/SKILL.md) | ユーザー起動 | (JA frontmatter) | 計画や設計を洗練するための容赦ないインタビュー。進めながら docs（ADR と glossary）も作成する。 | grilling + ドキュメント生成 |
| [implement](../skills/engineering/implement/SKILL.md) | ユーザー起動 | (JA frontmatter) | PRD または一連の issue に基づいて、一区切りの作業を実装する。 | PRD/issue の実装 |
| [improve-codebase-architecture](../skills/engineering/improve-codebase-architecture/SKILL.md) | ユーザー起動 | (JA frontmatter) | codebase をスキャンして deepening の機会を見つけ、視覚的な HTML レポートとして提示し、選んだ箇所について grilling を進める。 | アーキテクチャ改善スキャン |
| [prototype](../skills/engineering/prototype/SKILL.md) | モデル起動 | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like. | 設計上の疑問に答えるための使い捨てプロトタイプを作る。ユーザーが state model やロジックが正しく感じられるか確認したい、または UI がどう見えるべきか探りたいときに使う。 | 使い捨てプロトタイプ作成 |
| [research](../skills/engineering/research/SKILL.md)（新規） | モデル起動 | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent. | 信頼度の高い一次情報源に基づいて疑問を調査し、結果をリポジトリ内の Markdown ファイルとして記録する。ユーザーがトピックの調査、ドキュメントや API の事実確認、または調べものをバックグラウンドの agent に任せたいときに使う。 | 一次情報源の調査・記録 |
| [resolving-merge-conflicts](../skills/engineering/resolving-merge-conflicts/SKILL.md) ※1 | モデル起動 | Use when you need to resolve an in-progress git merge/rebase conflict. | 進行中の git merge/rebase の競合を解消する必要があるときに使う。 | マージ競合の解消 |
| [setup-matt-pocock-skills](../skills/engineering/setup-matt-pocock-skills/SKILL.md) | ユーザー起動 | (JA frontmatter) | engineering skills 向けにこのリポジトリを設定する — issue tracker、triage ラベルの語彙、domain doc のレイアウトをセットアップする。他の engineering skills を初めて使う前に一度実行する。 | engineering skills の初期セットアップ |
| [tdd](../skills/engineering/tdd/SKILL.md) | モデル起動 | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. | テスト駆動開発。ユーザーが機能構築やバグ修正を test-first で行いたい、「red-green-refactor」に言及した、または integration test を求めたときに使う。 | テスト駆動開発 (TDD) |
| [to-issues](../skills/engineering/to-issues/SKILL.md) | ユーザー起動 | (JA frontmatter) | plan、spec、または PRD を、tracer-bullet の vertical slice を使って、プロジェクトの issue tracker 上で独立して着手可能な issue に分解する。 | PRD → issue 分解 |
| [to-prd](../skills/engineering/to-prd/SKILL.md) | ユーザー起動 | (JA frontmatter) | 現在の会話を PRD に変換し、プロジェクトの issue tracker に公開する — インタビューはなく、すでに議論した内容をまとめるだけ。 | 会話 → PRD 変換 |
| [triage](../skills/engineering/triage/SKILL.md) | ユーザー起動 | (JA frontmatter) | issue と外部 PR を、triage の役割からなる状態機械に通す — 分類し、検証し、必要なら grill し、エージェントがすぐ着手できる briefs を書く。 | issue/PR の triage |

※1 `resolving-merge-conflicts` は `skills/engineering/` に存在するが、`README.md`・`skills/engineering/README.md`・`.claude-plugin/plugin.json` のいずれにも未登録（upstream 側の登録漏れの可能性。今回のリポジトリ構成ルールでは engineering の skill は両方への登録が必須）。

### 1-2. productivity/（promoted・登録必須）

| skill | 起動種別 | description（英語） | description（日本語訳） | 概要 |
|---|---|---|---|---|
| [grilling](../skills/productivity/grilling/SKILL.md) | モデル起動 | Grill the user relentlessly about a plan or design. Use when the user wants to stress-test a plan before building, or uses any 'grill' trigger phrases. | 計画や設計についてユーザーを容赦なく grill する。ユーザーが構築前に計画を stress-test したい、または「grill」のトリガーフレーズを使ったときに使う。 | 計画への grilling インタビュー |
| [grill-me](../skills/productivity/grill-me/SKILL.md) | ユーザー起動 | (JA frontmatter) | 計画や設計を洗練するための容赦ないインタビュー。 | grilling インタビュー起動 |
| [handoff](../skills/productivity/handoff/SKILL.md) | ユーザー起動 | (JA frontmatter) | 現在の会話を、別のエージェントが引き継げるよう handoff document に圧縮する。 | 会話の handoff 文書化 |
| [teach](../skills/productivity/teach/SKILL.md) | ユーザー起動 | (JA frontmatter) | このワークスペース内で、ユーザーに新しい skill や概念を教える。 | skill/概念のレッスン化 |
| [writing-great-skills](../skills/productivity/writing-great-skills/SKILL.md) | ユーザー起動 | (JA frontmatter) | skills を上手く書き・編集するためのリファレンス — skill を予測可能にする語彙と原則。 | skill 執筆リファレンス |

### 1-3. misc/（非 promoted・README/plugin.json には非掲載）

| skill | 起動種別 | description（英語） | description（日本語訳） | 概要 |
|---|---|---|---|---|
| [git-guardrails-claude-code](../skills/misc/git-guardrails-claude-code/SKILL.md) | モデル起動 | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code. | 危険な git コマンド（push, reset --hard, clean, branch -D 等）を実行前にブロックする Claude Code hooks をセットアップする。ユーザーが破壊的な git 操作を防ぎたい、git safety hooks を追加したい、または Claude Code での git push/reset をブロックしたいときに使う。 | 危険な git コマンドの hook ブロック |
| [migrate-to-shoehorn](../skills/misc/migrate-to-shoehorn/SKILL.md) | モデル起動 | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data. | テストファイルの `as` type assertion を @total-typescript/shoehorn へ移行する。ユーザーが shoehorn に言及した、テスト内の `as` を置き換えたい、または部分的なテストデータが必要なときに使う。 | shoehorn への移行 |
| [scaffold-exercises](../skills/misc/scaffold-exercises/SKILL.md) | モデル起動 | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or set up a new course section. | lint を通る sections・problems・solutions・explainers を備えた演習ディレクトリ構造を作成する。ユーザーが演習を scaffold したい、演習の雛形を作りたい、または新しいコースセクションをセットアップしたいときに使う。 | 演習ディレクトリの scaffold |
| [setup-pre-commit](../skills/misc/setup-pre-commit/SKILL.md) | モデル起動 | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing. | 現在のリポジトリに lint-staged（Prettier）・型チェック・テストを備えた Husky の pre-commit hooks をセットアップする。ユーザーが pre-commit hooks を追加したい、Husky をセットアップしたい、lint-staged を設定したい、またはコミット時の formatting/typechecking/testing を追加したいときに使う。 | pre-commit hooks のセットアップ |

### 1-4. personal/（非 promoted）

| skill | 起動種別 | description（英語） | description（日本語訳） | 概要 |
|---|---|---|---|---|
| [edit-article](../skills/personal/edit-article/SKILL.md) | ユーザー起動 | (JA frontmatter) | セクションを再構成し、明瞭さを高め、文章を引き締めることで記事を編集・改善する。ユーザーが記事のドラフトを編集・改訂・改善したいときに使う。 | 記事の編集・推敲 |
| [obsidian-vault](../skills/personal/obsidian-vault/SKILL.md) | モデル起動 | Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to find, create, or organize notes in Obsidian. | wikilink と index note を使って Obsidian vault 内のノートを検索・作成・管理する。ユーザーが Obsidian でノートを見つけたい、作成したい、整理したいときに使う。 | Obsidian vault のノート管理 |

### 1-5. in-progress/（draft・非 promoted）

| skill | 起動種別 | description（英語） | description（日本語訳） | 概要 |
|---|---|---|---|---|
| [claude-handoff](../skills/in-progress/claude-handoff/SKILL.md)（新規） | ユーザー起動 | Hand the current conversation off to a fresh background agent that picks up the work immediately. | 現在の会話を、作業をすぐに引き継ぐ新しいバックグラウンド agent へ hand off する。 | バックグラウンド agent への handoff |
| [loop-me](../skills/in-progress/loop-me/SKILL.md) | ユーザー起動 | Grill me about specs for the workflows I want to build, within this workspace. | このワークスペース内で構築したい workflow の仕様について私に grill してもらう。 | workflow 仕様の grilling |
| [wayfinder](../skills/in-progress/wayfinder/SKILL.md)（`decision-mapping` から改名） | モデル起動 | Plan a huge chunk of work — more than one agent session can hold — as a shared map of investigation tickets on your issue tracker, and resolve them one at a time until the way to the goal is clear. | 1つの agent セッションでは抱えきれない大きな作業のかたまりを、issue tracker 上の investigation ticket の共有マップとして計画し、ゴールへの道筋が見えるまで一つずつ解決していく。 | 大規模作業の map 化と逐次解決 |
| [wizard](../skills/in-progress/wizard/SKILL.md) | ユーザー起動 | Generate an interactive bash wizard that walks a human through a manual procedure — third-party setup, a one-off migration, an A→B state transition — opening URLs, capturing values, confirming each step, and writing .env files and GitHub Actions secrets. | 手動手順（third-party のセットアップ、一回限りの移行、A→B の状態遷移など）を人間に案内する、対話的な bash wizard を生成する — URL を開き、値を取得し、各ステップを確認し、.env ファイルや GitHub Actions secrets を書き込む。 | 対話的セットアップ wizard 生成 |
| [writing-beats](../skills/in-progress/writing-beats/SKILL.md) | ユーザー起動 | Writing, exploit — assemble raw material into a journey of beats, grounding each term before a beat leans on it. | Writing, exploit — 素材を beat の journey に組み立て、各用語を beat が使う前に地固めする。 | beat 構成への組み立て |
| [writing-fragments](../skills/in-progress/writing-fragments/SKILL.md) | ユーザー起動 | Writing, explore — mine raw fragments, no structure yet. | Writing, explore — 構造のない生の素材を掘り出す。 | 生素材の掘り出し |
| [writing-shape](../skills/in-progress/writing-shape/SKILL.md) | ユーザー起動 | Writing, exploit — shape raw material into an article, paragraph by paragraph. | Writing, exploit — 素材を段落ごとに記事へ形作る。 | 段落単位の記事化 |

### 1-6. deprecated/（もう使わない）

| skill | 起動種別 | description（英語） | description（日本語訳） | 概要 |
|---|---|---|---|---|
| [design-an-interface](../skills/deprecated/design-an-interface/SKILL.md) | モデル起動 | Generate multiple radically different interface designs for a module using parallel sub-agents. Use when user wants to design an API, explore interface options, compare module shapes, or mentions "design it twice". | 並列の sub-agent を使って、モジュールの根本的に異なる複数のインターフェース設計を生成する。ユーザーが API を設計したい、interface の選択肢を探りたい、モジュール形状を比較したい、または「design it twice」に言及したときに使う。 | 複数インターフェース設計案の生成 |
| [qa](../skills/deprecated/qa/SKILL.md) | モデル起動 | Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explores the codebase in the background for context and domain language. Use when user wants to report bugs, do QA, file issues conversationally, or mentions "QA session". | ユーザーが会話形式でバグや issue を報告し、agent が GitHub issue を作成する対話的な QA セッション。文脈と domain language のためにバックグラウンドで codebase を探索する。ユーザーがバグを報告したい、QA を行いたい、会話的に issue を作成したい、または「QA session」に言及したときに使う。 | 対話的 QA セッション |
| [request-refactor-plan](../skills/deprecated/request-refactor-plan/SKILL.md) | モデル起動 | Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue. Use when user wants to plan a refactor, create a refactoring RFC, or break a refactor into safe incremental steps. | ユーザーへのインタビューを通じて tiny commits による詳細な refactor plan を作成し、GitHub issue として提出する。ユーザーが refactor を計画したい、refactoring RFC を作成したい、または refactor を安全な段階的ステップに分解したいときに使う。 | refactor plan の作成 |
| [ubiquitous-language](../skills/deprecated/ubiquitous-language/SKILL.md) | ユーザー起動 | (JA frontmatter) | 現在の会話から DDD スタイルの ubiquitous language の glossary を抽出し、曖昧さを指摘して正規の用語を提案する。UBIQUITOUS_LANGUAGE.md に保存する。ユーザーが domain の用語を定義したい、glossary を作りたい、用語を厳密化したい、ubiquitous language を作りたいとき、または「domain model」や「DDD」に言及したときに使う。 | ubiquitous language glossary 抽出 |

---

## 2. ビルトイン公式 skill（スコープ: built-in / 全件 on）

| skill | description（日本語訳・概要） |
|---|---|
| `deep-research` | 複数ソースへ fan-out する web 検索・出典取得・主張の敵対的検証・引用付きレポート統合を行う research harness。多面的・事実確認済みの調査レポートが欲しいときに使う。曖昧な質問には事前に2〜3個の確認質問をする。 |
| `dataviz` | chart・graph・plot・dashboard・データビジュアライゼーションを作成する前に必ず読む skill。フォームのヒューリスティック、色の計算式とバリデータ、mark 仕様、インタラクションのルールを使い、ライト/ダーク双方で一貫した見た目のビジュアライゼーションを作る。 |
| `artifact-design` | Artifact（claude.ai でホストされる Web ページ成果物）のデザイン指針と基礎。 |
| `update-config` | `settings.json` 経由で Claude Code harness を設定する。自動化された振る舞い（hook）・permission・環境変数の変更に使う。 |
| `keybindings-help` | keyboard shortcut のカスタマイズ、キーの再割り当て、chord binding の追加、`~/.claude/keybindings.json` の変更をしたいときに使う。 |
| `verify` | コード変更が実際に意図通り動作するかを、対象のフローを実際に動かして end-to-end で検証する。テストや型チェックだけでなく実際の挙動を観察する。コミット前に実行を推奨。 |
| `code-review`（built-in・`/code-review`） | 現在の diff を、指定した effort level（low〜ultra）で correctness bug と reuse/simplification/efficiency の観点からレビューする。`--comment` で inline コメント投稿、`--fix` で修正適用も可能。※ mattpocock の `engineering/code-review` skill とは別物。 |
| `simplify` | 変更されたコードを reuse・simplification・efficiency・altitude の観点でレビューし、修正を適用する。バグ探しはしない（それは `/code-review` の役割）。 |
| `fewer-permission-prompts` | transcript をスキャンしてよくある read-only な Bash/MCP tool call を見つけ、プロジェクトの `.claude/settings.json` に優先順位付き allowlist を追加し、permission prompt を減らす。 |
| `loop` | プロンプトや slash command を一定間隔で繰り返し実行する（例: `/loop 5m /foo`）。間隔を省略するとモデルが自分でペースを決める。 |
| `schedule` | cron スケジュールで実行するスケジュール済み cloud agent（routine）の作成・更新・一覧・実行。1回限りの予約実行にも使える。 |
| `claude-api` | Claude API / Anthropic SDK のリファレンス — model id、価格、パラメータ、streaming、tool use、MCP、agent、caching、token counting、model migration。 |
| `claude-in-chrome` | Chrome ブラウザを自動操作して Web ページを操作する — クリック、フォーム入力、スクリーンショット取得、console log の読み取り、サイトナビゲーション。 |
| `run` | このプロジェクトのアプリを起動して動かし、変更が実際のアプリで動作することを確認する。 |
| `init` | codebase のドキュメントを持つ新しい `CLAUDE.md` ファイルを初期化する。 |
| `review` | GitHub の pull request をレビューする。作業中の diff には `/code-review` を使う。 |
| `security-review` | 現在の branch の pending changes についてセキュリティレビューを完了する。 |

---

## 3. 有効プラグインの skill（`~/.claude/settings.json` の `enabledPlugins` 参照）

| プラグイン | on/off | skill | description（日本語訳・概要） |
|---|---|---|---|
| `loop@loop` | on | `loop:define` | 初期プロンプトから受け入れテストを生成し、ユーザー承認のうえ凍結して `.loop/state.json`（`armed: false`）を作る。ループの入口。 |
| `loop@loop` | on | `loop:start` | 凍結済みの受け入れテストを前提に、ループを開始（`armed: true`）し、builder エージェントの最初のイテレーションを起動する。 |
| `loop@loop` | on | `loop:status` | ループの現在状態を実行時に確認し、決定的な brief（完了/進行中/停滞/手動停止のいずれか）を提示する。 |
| `loop@loop` | on | `loop:stop` | ループを手動で disarm する。`armed: false` にし、以後 Stop hook は素通しになる。 |
| `security-guidance@claude-plugins-official` | on | （上記 built-in 表の `security-review` に相当する可能性が高い） | — |
| `claude-md-management@claude-plugins-official` | **off** | （無効化されているため未提示） | — |
| `claude-code-setup@claude-plugins-official` | **off** | （無効化されているため未提示） | — |

---

## 集計

- mattpocock/skills リポジトリ skill: **38 件**（engineering 16、productivity 5、misc 4、personal 2、in-progress 7、deprecated 4）— 全件 off（未リンク）
- ビルトイン公式 skill: **17 件** — 全件 on
- プラグイン skill（on のみ集計）: `loop@loop` 4 件（+ `security-guidance` 推定1件）

## 今後の翻訳作業でのこの表の使い方

Phase A（全 skill の段階的日本語翻訳）を進める際、この表の「description（日本語訳）」列を各 `SKILL.md` の frontmatter へ反映していく進捗トラッカーとして使う。翻訳済みの行は `(JA frontmatter)` と表示されているものを含め、本文の翻訳完了後にこの表の該当行へ「本文翻訳済み」マークを追記する運用とする。

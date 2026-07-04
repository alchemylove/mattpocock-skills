<p>
  <a href="https://www.aihero.dev/s/skills-newsletter">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skills-repo-dark_2x.png">
      <source media="(prefers-color-scheme: light)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png">
      <img alt="Skills" src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" width="369">
    </picture>
  </a>
</p>

# 本物のエンジニア向け Skills (Skills For Real Engineers)

[![skills.sh](https://skills.sh/b/mattpocock/skills)](https://skills.sh/mattpocock/skills)

本物のエンジニアリングのために私が毎日使っている agent skills です — vibe coding ではありません。

本物のアプリケーションの開発は難しい。GSD、BMAD、Spec-Kit のようなアプローチは、プロセスを丸ごと引き受けることで手助けしようとする。しかしその過程であなたの制御を奪い、プロセス中のバグを解決しづらくしてしまう。

これらの skills は、小さく、適応させやすく、組み合わせ可能になるよう設計されている。どんなモデルでも動作する。数十年のエンジニアリング経験に基づいている。自由にいじって、自分のものにして、楽しんでほしい。

これらの skills の変更や、私が新しく作る skill を追いかけたいなら、約60,000人の開発者と一緒に私のニュースレターに参加できる:

[Sign Up To The Newsletter](https://www.aihero.dev/s/skills-newsletter)

## クイックスタート (Quickstart)（30秒セットアップ）

1. skills.sh のインストーラーを実行する:

```bash
npx skills@latest add mattpocock/skills
```

2. 欲しい skills と、それらをインストールするコーディングエージェントを選ぶ。**`/setup-matt-pocock-skills` を必ず選択すること。**

3. エージェントで `/setup-matt-pocock-skills` を実行する。次のことを尋ねられる:
   - 使う issue tracker（GitHub、Linear、またはローカルファイル）
   - triage 時にチケットへ付けるラベル（`/triage` がラベルを使う）
   - 作成するドキュメントの保存先

4. これで準備完了。

## これらの Skills が存在する理由 (Why These Skills Exist)

Claude Code、Codex、その他のコーディングエージェントで私が目にする、よくある失敗モードを修正する手段として、これらの skills を作った。

### #1: エージェントが望んだとおりに動かない (The Agent Didn't Do What I Want)

> "No-one knows exactly what they want"
> 「誰も自分が何を望んでいるかを正確には知らない」
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**The Problem**。ソフトウェア開発で最もよくある失敗モードは認識のズレだ。開発者は自分の望みを分かっていると思っている。ところが作られたものを見て、まったく理解されていなかったと気づく。

AI 時代でも同じだ。あなたとエージェントの間にはコミュニケーションのギャップがある。その解決策が **grilling session** だ — 作ろうとしているものについて、エージェントに詳細な質問をさせること。

**The Fix** は次を使うこと:

- [`/grill-me`](./skills/productivity/grill-me/SKILL.md) — コード以外の用途向け
- [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) — [`/grill-me`](./skills/productivity/grill-me/SKILL.md) と同じだが、さらに便利な機能が加わる（後述）

これらは私の最も人気のある skills だ。着手する前にエージェントと認識を合わせ、これから行う変更について深く考えるのに役立つ。変更を加えたいときは _毎回_ 使うこと。

### #2: エージェントが冗長すぎる (The Agent Is Way Too Verbose)

> With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.
> 「ユビキタス言語があれば、開発者間の会話もコードの表現も、同じドメインモデルから導かれる」
>
> Eric Evans, [Domain-Driven-Design](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

**The Problem**: プロジェクトの開始時、開発者と、彼らがソフトウェアを作る相手（ドメインエキスパート）は、たいてい異なる言語を話している。

私もエージェントに対して同じ緊張を感じた。エージェントはたいていプロジェクトに放り込まれ、進めながら専門用語を解読するよう求められる。だから1語で済むところに20語を使う。

**The Fix** は shared language だ。プロジェクトで使われる専門用語をエージェントが解読するのに役立つドキュメントである。

<details>
<summary>
例
</summary>

私の `course-video-manager` リポジトリにある [`CONTEXT.md`](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md) の例。どちらが読みやすいだろうか?

- **BEFORE**: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"
  → 「コースのセクション内のレッスンが『実体化』されると（つまりファイルシステム上に場所が割り当てられると）問題が起きる」
- **AFTER**: "There's a problem with the materialization cascade"
  → 「materialization cascade に問題がある」

この簡潔さはセッションを重ねるごとに効いてくる。

</details>

これは [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) に組み込まれている。grilling session でありながら、AI と shared language を築き、説明しづらい決定を ADR に記録するのに役立つ。

これがどれほど強力か、説明するのは難しい。このリポジトリで唯一にして最高のテクニックかもしれない。試してみてほしい。

> [!TIP]
> shared language には、冗長さを減らす以外にも多くの利点がある:
>
> - **変数・関数・ファイルが一貫した名前になる**（shared language を使って）
> - その結果、**コードベースをエージェントが辿りやすくなる**
> - エージェントはより簡潔な言語を使えるため、**思考に費やすトークンも少なくなる**

### #3: コードが動かない (The Code Doesn't Work)

> "Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that's too big."
> 「常に小さく、意図を持ったステップを踏め。フィードバックの速さがあなたのスピード制限だ。大きすぎるタスクは引き受けるな」
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**The Problem**: あなたとエージェントが、何を作るかについて認識を合わせられたとしよう。それでもエージェントが _それでも_ ひどいコードを生み出したら、どうなるか?

feedback loops を見直す時だ。生成したコードが実際にどう動くかのフィードバックがなければ、エージェントは手探りで飛ぶことになる。

**The Fix**: おなじみの feedback loops 一式が必要だ — 静的型、ブラウザアクセス、自動テスト。

自動テストでは red-green-refactor loop が決定的に重要だ。エージェントがまず失敗するテストを書き、それからテストを通す。これによりエージェントに一貫したフィードバックが与えられ、はるかに良いコードになる。

どんなプロジェクトにも組み込める **[`/tdd`](./skills/engineering/tdd/SKILL.md) skill** を作った。red-green-refactor を促し、良いテストと悪いテストの違いについて十分なガイダンスをエージェントに与える。

デバッグ用に、優れたデバッグの実践をシンプルなループにまとめた **[`/diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md)** skill も作った。

### #4: 巨大な泥だんごができてしまった (We Built A Ball Of Mud)

> "Invest in the design of the system _every day_."
> 「システムの設計に _毎日_ 投資せよ」
>
> Kent Beck, [Extreme Programming Explained](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

> "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."
> 「最良のモジュールは深い。シンプルなインターフェースを通じて多くの機能にアクセスできる」
>
> John Ousterhout, [A Philosophy Of Software Design](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

**The Problem**: エージェントで作られたアプリの多くは複雑で変更しづらい。エージェントはコーディングを劇的に高速化できるため、ソフトウェアのエントロピーも加速させる。コードベースはかつてない速さで複雑になっていく。

**The Fix** は、AI を活用した開発への抜本的に新しいアプローチだ — コードの設計を気にかけること。

これはこれらの skills のあらゆる層に組み込まれている:

- [`/to-prd`](./skills/engineering/to-prd/SKILL.md) は、PRD を作る前に、どのモジュールに触れるのかを問いただす

そして何より、[`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) は泥だんごと化したコードベースを救い出すのに役立つ。数日に一度、自分のコードベースで実行することをおすすめする。

### まとめ (Summary)

ソフトウェアエンジニアリングの基礎は、かつてないほど重要になっている。これらの skills は、その基礎を反復可能な実践へと凝縮しようとした私の最善の試みであり、キャリアで最高のアプリを世に出す手助けをする。楽しんでほしい。

## リファレンス (Reference)

分類軸はひとつ — 誰が呼び出せるか。**ユーザー起動 (User-invoked)** の skills は、あなたがタイプした場合にのみ到達可能（例: `/grill-me`）; 役割はオーケストレーション。**モデル起動 (Model-invoked)** の skills は、あなたが呼び出すことも _または_ タスクが合うときにエージェントが自動で使うことも可能; 再利用可能な規律を保持する。ユーザー起動 skill はモデル起動 skill を呼び出せるが、別のユーザー起動 skill は呼び出せない。

### エンジニアリング (Engineering)

コード作業に毎日使う skills。

**ユーザー起動 (User-invoked)**

- **[ask-matt](./skills/engineering/ask-matt/SKILL.md)** — どの skill やフローが自分の状況に合うかを尋ねる。このリポジトリの user-invoked skills 群に対する router。
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** — grilling session でありながら、プロジェクトの domain model も構築し、用語を研ぎ澄まし、`CONTEXT.md` と ADR をその場で更新する。
- **[triage](./skills/engineering/triage/SKILL.md)** — triage の役割からなるステートマシンに沿って issue を進める。
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** — コードベースをスキャンして deepening の機会を探し、視覚的な HTML レポートとして提示し、選んだものについて grill する。
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** — このリポジトリを engineering skills 用に設定する（issue tracker、triage ラベル、domain doc のレイアウト）。他の engineering skills を使う前に、リポジトリごとに一度だけ実行する。
- **[to-issues](./skills/engineering/to-issues/SKILL.md)** — どんな plan・spec・PRD でも、vertical slice を使って独立して着手できる issue に分解する。
- **[to-prd](./skills/engineering/to-prd/SKILL.md)** — 現在の会話を PRD に変換し、issue tracker に公開する。インタビューは行わず、すでに話し合った内容をまとめるだけ。

**モデル起動 (Model-invoked)**

- **[prototype](./skills/engineering/prototype/SKILL.md)** — 設計上の疑問に答えるための使い捨てプロトタイプを作る — 状態やロジックに関する疑問には実行可能なターミナルアプリを、UI に関する疑問には1つのルートから切り替えられる複数の大胆に異なるバリエーションを用意する。
- **[diagnosing-bugs](./skills/engineering/diagnosing-bugs/SKILL.md)** — 難しいバグやパフォーマンス regression のための規律ある diagnosis loop: reproduce → minimise → hypothesise → instrument → fix → regression-test。
- **[research](./skills/engineering/research/SKILL.md)** — 信頼性の高い一次情報源に基づいて疑問を調査し、その結果を引用付きの Markdown ファイルとしてリポジトリに記録する。background agent として実行される。
- **[tdd](./skills/engineering/tdd/SKILL.md)** — red-green-refactor loop を用いた test-driven development。機能追加やバグ修正を vertical slice ごとに1つずつ進める。
- **[domain-modeling](./skills/engineering/domain-modeling/SKILL.md)** — プロジェクトの domain model を積極的に構築し、研ぎ澄ます — 用語を glossary と照らして検証し、エッジケースのシナリオでストレステストを行い、`CONTEXT.md` と ADR をその場で更新する。
- **[codebase-design](./skills/engineering/codebase-design/SKILL.md)** — deep module を設計するための共有された規律と語彙: 小さなインターフェースの背後に多くの振る舞いを持ち、きれいな seam に配置され、そのインターフェースを通じてテスト可能である。
- **[code-review](./skills/engineering/code-review/SKILL.md)** — 基準点からの diff を2つの軸でレビューする: **Standards**（リポジトリのコーディング規約に従っているか、加えて Fowler の smell baseline を満たしているか）と **Spec**（元となった issue/PRD を忠実に実装しているか）。互いに汚染しないよう並列の sub-agent として実行される。

### 生産性 (Productivity)

コードに限らない、汎用的なワークフローツール。

**ユーザー起動 (User-invoked)**

- **[grill-me](./skills/productivity/grill-me/SKILL.md)** — 計画や設計を洗練するための容赦ないインタビュー。
- **[handoff](./skills/productivity/handoff/SKILL.md)** — 現在の会話を、別のエージェントが引き継げるよう handoff document に圧縮する。
- **[teach](./skills/productivity/teach/SKILL.md)** — このワークスペース内で、ユーザーに新しい skill や概念を教える。
- **[writing-great-skills](./skills/productivity/writing-great-skills/SKILL.md)** — skills を上手く書き・編集するためのリファレンス — skill を予測可能にする語彙と原則。

**モデル起動 (Model-invoked)**

- **[grilling](./skills/productivity/grilling/SKILL.md)** — 計画や設計について、決定木のあらゆる分岐が解決するまで容赦なくユーザーにインタビューする。`grill-me` と `grill-with-docs` の背後にある再利用可能な loop。

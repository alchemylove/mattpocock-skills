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
- **AFTER**: "There's a problem with the materialization cascade"

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

> "Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that’s too big."
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**The Problem**: あなたとエージェントが、何を作るかについて認識を合わせられたとしよう。それでもエージェントが _それでも_ ひどいコードを生み出したら、どうなるか?

feedback loops を見直す時だ。生成したコードが実際にどう動くかのフィードバックがなければ、エージェントは手探りで飛ぶことになる。

**The Fix**: おなじみの feedback loops 一式が必要だ — 静的型、ブラウザアクセス、自動テスト。

自動テストでは red-green-refactor loop が決定的に重要だ。エージェントがまず失敗するテストを書き、それからテストを通す。これによりエージェントに一貫したフィードバックが与えられ、はるかに良いコードになる。

どんなプロジェクトにも組み込める **[`/tdd`](./skills/engineering/tdd/SKILL.md) skill** を作った。red-green-refactor を促し、良いテストと悪いテストの違いについて十分なガイダンスをエージェントに与える。

デバッグ用に、優れたデバッグの実践をシンプルなループにまとめた **[`/diagnose`](./skills/engineering/diagnose/SKILL.md)** skill も作った。

### #4: 巨大な泥だんごができてしまった (We Built A Ball Of Mud)

> "Invest in the design of the system _every day_."
>
> Kent Beck, [Extreme Programming Explained](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

> "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."
>
> John Ousterhout, [A Philosophy Of Software Design](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

**The Problem**: エージェントで作られたアプリの多くは複雑で変更しづらい。エージェントはコーディングを劇的に高速化できるため、ソフトウェアのエントロピーも加速させる。コードベースはかつてない速さで複雑になっていく。

**The Fix** は、AI を活用した開発への抜本的に新しいアプローチだ — コードの設計を気にかけること。

これはこれらの skills のあらゆる層に組み込まれている:

- [`/to-prd`](./skills/engineering/to-prd/SKILL.md) は、PRD を作る前に、どのモジュールに触れるのかを問いただす
- [`/zoom-out`](./skills/engineering/zoom-out/SKILL.md) は、システム全体の文脈でコードを説明するようエージェントに指示する

そして何より、[`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) は泥だんごと化したコードベースを救い出すのに役立つ。数日に一度、自分のコードベースで実行することをおすすめする。

### まとめ (Summary)

ソフトウェアエンジニアリングの基礎は、かつてないほど重要になっている。これらの skills は、その基礎を反復可能な実践へと凝縮しようとした私の最善の試みであり、キャリアで最高のアプリを世に出す手助けをする。楽しんでほしい。

## リファレンス (Reference)

### エンジニアリング (Engineering)

コード作業に毎日使う skills。

- **[diagnose](./skills/engineering/diagnose/SKILL.md)** — 難しいバグやパフォーマンス低下に対する、規律ある diagnosis loop: 再現 → 最小化 → 仮説 → 計測 → 修正 → 回帰テスト。
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** — 既存の domain model に照らして計画を問いただし、用語を洗練し、`CONTEXT.md` と ADR をその場で更新する grilling session。
- **[triage](./skills/engineering/triage/SKILL.md)** — triage の役割からなる状態機械を通して issue を選別する。
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** — `CONTEXT.md` の domain language と `docs/adr/` の決定を踏まえて、codebase の中に deepening の機会を見つける。
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** — 他の engineering skills が利用する、リポジトリごとの設定（issue tracker、triage label の語彙、ドメインドキュメントの構成）を生成する。`to-issues`、`to-prd`、`triage`、`diagnose`、`tdd`、`improve-codebase-architecture`、`zoom-out` を使う前に、リポジトリごとに一度実行する。
- **[tdd](./skills/engineering/tdd/SKILL.md)** — red-green-refactor loop による test-driven development。機能の構築やバグ修正を、vertical slice 単位で一つずつ進める。
- **[to-issues](./skills/engineering/to-issues/SKILL.md)** — 任意の plan、spec、PRD を、vertical slice を使って独立して着手可能な GitHub issue に分解する。
- **[to-prd](./skills/engineering/to-prd/SKILL.md)** — 現在の会話のコンテキストを PRD に変換し、GitHub issue として登録する。インタビューはなし — すでに議論した内容をまとめるだけ。
- **[zoom-out](./skills/engineering/zoom-out/SKILL.md)** — エージェントに zoom out するよう指示し、馴染みのないコード箇所について、より広い文脈や高レベルな視点を示させる。
- **[prototype](./skills/engineering/prototype/SKILL.md)** — 設計を具体化するための使い捨てプロトタイプを作る — 状態やビジネスロジックの検討用に動作するターミナルアプリ、または1つの route から切り替えられる、まったく異なる複数の UI バリエーションのいずれか。

### 生産性 (Productivity)

コードに限らない、汎用的なワークフローツール。

- **[caveman](./skills/productivity/caveman/SKILL.md)** — 超圧縮されたコミュニケーションモード。技術的な正確さを完全に保ちながら、冗長な部分を削ってトークン使用量を約75%削減する。
- **[grill-me](./skills/productivity/grill-me/SKILL.md)** — 決定木のあらゆる分岐が解消されるまで、計画や設計について容赦なくインタビューされる。
- **[handoff](./skills/productivity/handoff/SKILL.md)** — 現在の会話を handoff document に圧縮し、別のエージェントが作業を引き継げるようにする。
- **[write-a-skill](./skills/productivity/write-a-skill/SKILL.md)** — 適切な構造、progressive disclosure、同梱リソースを備えた新しい skills を作成する。

### その他 (Misc)

残してはあるが、めったに使わないツール。

- **[git-guardrails-claude-code](./skills/misc/git-guardrails-claude-code/SKILL.md)** — 危険な git コマンド（push、reset --hard、clean など）を実行前にブロックする Claude Code hooks を設定する。
- **[migrate-to-shoehorn](./skills/misc/migrate-to-shoehorn/SKILL.md)** — test ファイルを `as` type assertion から @total-typescript/shoehorn へ移行する。
- **[scaffold-exercises](./skills/misc/scaffold-exercises/SKILL.md)** — sections、problems、solutions、explainers からなる演習ディレクトリ構造を作成する。
- **[setup-pre-commit](./skills/misc/setup-pre-commit/SKILL.md)** — lint-staged、Prettier、型チェック、テストを備えた Husky の pre-commit hooks を設定する。

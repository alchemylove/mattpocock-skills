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

vibe coding ではなく、real engineering のために毎日使っている agent skills です。

real applications の開発は難しい。GSD、BMAD、Spec-Kit のようなアプローチは process を own することで助けようとする。しかしその過程で control を奪い、process 内の bug を resolve しにくくする。

これらの skills は small で adapt しやすく、composable になるよう設計されている。どの model でも動く。decades の engineering experience に基づいている。hack して自分好みにして、enjoy してほしい。

skills の変更や新規 skill の情報を追いたければ、newsletter で ~60,000 人の dev と一緒に参加できる:

[Sign Up To The Newsletter](https://www.aihero.dev/s/skills-newsletter)

## クイックスタート (Quickstart)（30-second setup）

1. skills.sh installer を run:

```bash
npx skills@latest add mattpocock/skills
```

2. 欲しい skills と、install 先の coding agents を選ぶ。**`/setup-matt-pocock-skills` を必ず選択すること。**

3. agent で `/setup-matt-pocock-skills` を run する。次を聞かれる:
   - 使う issue tracker（GitHub、Linear、または local files）
   - triage 時に tickets に apply する labels（`/triage` が labels を使う）
   - 作成する docs の保存先

4. Bam — 準備完了。

## これらの Skills が存在する理由 (Why These Skills Exist)

Claude Code、Codex、その他の coding agents で見る common failure modes を fix するために、これらの skills を build した。

### #1: Agent が望んだことをしてくれない (The Agent Didn't Do What I Want)

> "No-one knows exactly what they want"
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**The Problem**. software development で最も common な failure mode は misalignment である。dev が自分の望みを理解していると思う。build されたものを見て、agent はまったく理解していなかったと気づく。

AI age でも同じ。agent との間に communication gap がある。fix は **grilling session** — build する内容について agent に detailed questions を ask させること。

**The Fix** は次を使うこと:

- [`/grill-me`](./skills/productivity/grill-me/SKILL.md) — non-code 用途向け
- [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) — [`/grill-me`](./skills/productivity/grill-me/SKILL.md) と同じだが、さらに goodies を追加（下記参照）

これらは最も人気のある skills である。着手前に agent と align し、行う変更について深く考えるのに役立つ。変更を行うたびに _every_ time 使うこと。

### #2: Agent が verbose すぎる (The Agent Is Way Too Verbose)

> With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.
>
> Eric Evans, [Domain-Driven-Design](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

**The Problem**: project 開始時、devs と software を build する対象（domain experts）は通常 different languages を話している。

agents でも同じ tension を感じた。agents は project に drop され、jargon を go しながら figure out するよう求められる。だから 1 word で済むところに 20 words を使う。

**The Fix** は shared language である。project で使われる jargon を agent が decode するのに役立つ document。

<details>
<summary>
Example
</summary>

`course-video-manager` repo の [`CONTEXT.md`](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md) の例。どちらが読みやすいか?

- **BEFORE**: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"
- **AFTER**: "There's a problem with the materialization cascade"

この concision は session ごとに payoff する。

</details>

これは [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) に built-in されている。grilling session だが、AI と shared language を build し、explain しにくい decisions を ADR's に document する。

powerful さは explain しがたい。この repo で single coolest technique かもしれない。try して see。

> [!TIP]
> shared language には verbosity 削減以外にも多くの benefits がある:
>
> - **Variables、functions、files が shared language で consistently named される**
> - その結果、**codebase が agent にとって navigate しやすくなる**
> - agent は **more concise language により thinking の tokens を少なく使う**

### #3: Code が動かない (The Code Doesn't Work)

> "Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that's too big."
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**The Problem**: agent と build 内容が align したとする。agent が _still_ crap を produce したらどうするか?

feedback loops を見直す時だ。produce した code が実際に run するかの feedback がなければ、agent は blind で fly する。

**The Fix**: usual tranche of feedback loops が必要 — static types、browser access、automated tests。

automated tests では red-green-refactor loop が critical。agent が failing test を first に write し、次に test を fix する。これにより agent に consistent level of feedback が与えられ、far better code になる。

任意の project に slot できる **[`/tdd`](./skills/engineering/tdd/SKILL.md) skill** を build した。red-green-refactor を encourage し、good/bad tests について十分な guidance を与える。

debugging 用に、best debugging practices を simple loop に wrap した **[`/diagnose`](./skills/engineering/diagnose/SKILL.md)** skill も build した。

### #4: Ball Of Mud を build してしまった (We Built A Ball Of Mud)

> "Invest in the design of the system _every day_."
>
> Kent Beck, [Extreme Programming Explained](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

> "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."
>
> John Ousterhout, [A Philosophy Of Software Design](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

**The Problem**: agents で build された apps の多くは complex で change しにくい。agents は coding を radically speed up できるため、software entropy も accelerate する。codebases は unprecedented rate で complex になる。

**The Fix** は AI-powered development への radical new approach: code の design を care すること。

skills の every layer に built-in されている:

- [`/to-prd`](./skills/engineering/to-prd/SKILL.md) は PRD 作成前に touch する modules について quiz する
- [`/zoom-out`](./skills/engineering/zoom-out/SKILL.md) は agent に whole system の context で code を explain させる

crucially、[`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) は ball of mud になった codebase を rescue する。codebase で数日に一度 run することを recommend。

### まとめ (Summary)

software engineering fundamentals は ever より重要である。これらの skills は fundamentals を repeatable practices に condense する best effort で、career で best apps を ship するのに役立つ。Enjoy。

## リファレンス (Reference)

### エンジニアリング (Engineering)

毎日 code work に使う skills。

- **[diagnose](./skills/engineering/diagnose/SKILL.md)** — 難しい bug と performance regression 向けの disciplined diagnosis loop: reproduce → minimise → hypothesise → instrument → fix → regression-test。
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** — 既存 domain model に対して plan を challenge し、terminology を sharpen、`CONTEXT.md` と ADR を inline update する grilling session。
- **[triage](./skills/engineering/triage/SKILL.md)** — triage roles の state machine を通じて issues を triage。
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** — `CONTEXT.md` の domain language と `docs/adr/` の decisions に基づき codebase の deepening opportunities を find。
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** — 他の engineering skills が consume する per-repo config（issue tracker、triage label vocabulary、domain doc layout）を scaffold。`to-issues`、`to-prd`、`triage`、`diagnose`、`tdd`、`improve-codebase-architecture`、`zoom-out` を使う前に repo ごとに 1 回 run。
- **[tdd](./skills/engineering/tdd/SKILL.md)** — red-green-refactor loop による test-driven development。feature や bug fix を vertical slice ごとに build。
- **[to-issues](./skills/engineering/to-issues/SKILL.md)** — 任意の plan、spec、PRD を vertical slices で independently-grabbable GitHub issues に break。
- **[to-prd](./skills/engineering/to-prd/SKILL.md)** — 現在の conversation context を PRD に turn し GitHub issue として submit。interview なし — 既に discuss した内容を synthesize するだけ。
- **[zoom-out](./skills/engineering/zoom-out/SKILL.md)** — agent に zoom out させ、馴染みのない code section について broader context や higher-level perspective を与える。
- **[prototype](./skills/engineering/prototype/SKILL.md)** — design を flesh out する throwaway prototype を build — state/business-logic 向けの runnable terminal app、または 1 route から toggle できる radically different UI variations。

### 生産性 (Productivity)

code 固有ではない general workflow ツール。

- **[caveman](./skills/productivity/caveman/SKILL.md)** — ultra-compressed communication mode。filler を drop し full technical accuracy を保ちながら token usage を ~75% 削減。
- **[grill-me](./skills/productivity/grill-me/SKILL.md)** — decision tree の every branch が resolve されるまで、plan や design について relentlessly interviewed される。
- **[handoff](./skills/productivity/handoff/SKILL.md)** — 現在の conversation を handoff document に compact し、別の agent が work を continue できるようにする。
- **[write-a-skill](./skills/productivity/write-a-skill/SKILL.md)** — proper structure、progressive disclosure、bundled resources で new skills を create。

### その他 (Misc)

残しておくが rarely use するツール。

- **[git-guardrails-claude-code](./skills/misc/git-guardrails-claude-code/SKILL.md)** — execute 前に dangerous git commands（push、reset --hard、clean など）を block する Claude Code hooks を set up。
- **[migrate-to-shoehorn](./skills/misc/migrate-to-shoehorn/SKILL.md)** — test files の `as` type assertions を @total-typescript/shoehorn に migrate。
- **[scaffold-exercises](./skills/misc/scaffold-exercises/SKILL.md)** — sections、problems、solutions、explainers を含む exercise directory structures を create。
- **[setup-pre-commit](./skills/misc/setup-pre-commit/SKILL.md)** — lint-staged、Prettier、type checking、tests 付きの Husky pre-commit hooks を set up。

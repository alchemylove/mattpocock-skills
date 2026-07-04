クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=domain-modeling
```

```bash
npx skills update domain-modeling
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)

## 何をするか (What it does)

`domain-modeling` は、設計を進めながらプロジェクトの **ubiquitous language** を構築し磨いていきます — 曖昧な用語に異議を唱え、具体的なシナリオで関係性をストレステストし、それらが結晶化した瞬間に glossary と decisions を書き留めます。

これは**能動的な**訓練であり、受動的なものではありません。`CONTEXT.md` を読んでその語彙を借用するだけなら、どの skill でもできる一行の習慣に過ぎません。この skill は、あなたが*モデルを変更している*ときのためのものです — 標準となる用語を作る、コードとたった今言ったことの間の矛盾に気づく、後戻りしにくい決定を記録する、といった場面です。そして glossary をクリーンに保ちます — `CONTEXT.md` は glossary であってそれ以外の何ものでもありません。実装の詳細も、仕様も、走り書きもここには置きません。

## いつ使うか (When to reach for it)

`/domain-modeling` と入力するか、タスクに合致すればエージェントが自動的に使います — 用語を確定させているとき、多義的な言葉を解消しているとき、アーキテクチャ上の決定を記録しているときです。

*言葉*が問題であるときに使ってください — 2人が「cancellation」で異なることを意味している、「account」が3つの役割を担っている、あるいは設計の会話が一度も正確に名付けられたことのない概念でつっかえ続けている、といった場合です。問題がモジュールの*形状*（seam をどこに置くか、インターフェースをどれだけ深くするか）であれば、代わりに [codebase-design](https://aihero.dev/skills-codebase-design) を使ってください。構築前に計画そのものを尋問してほしいなら、[grilling](https://aihero.dev/skills-grilling) を使ってください。

## 前提条件 (Prerequisites)

この skill は2箇所に書き込みますが、どちらも遅延生成されます — 記録すべきことが実際に生じたときにだけ作られます。解決した用語はルート直下の `CONTEXT.md`（あるいは `CONTEXT-MAP.md` でマルチコンテキストと示されたリポジトリでは、コンテキストごとの `CONTEXT.md`）に入ります。決定事項は `docs/adr/` に入ります。事前に何かを用意しておく必要はなく、最初の解決した用語が glossary を、最初の本物のトレードオフが ADR を作ります。

## Glossary と ADR

2つの成果物、それぞれ異なる基準があります。

- **Glossary**（`CONTEXT.md`）は言語を捉えます。曖昧な用語が標準化されるたびに、まとめてではなくその場で書き留められるので、共有語彙は会話と同期し続けます。実装の詳細を徹底的に排除した状態を保ちます。
- **ADR** は決定を捉えます。その基準は高く、その選択が**後戻りしにくく**、**文脈なしには意外であり**、かつ**本物のトレードオフの結果である**場合にのみ提示されます。3つのうちどれか1つでも欠ければ ADR は作られません。これが `docs/adr/` を、日記ではなく重大な分岐点の記録として保つ理由です。

決め手となる動きはこうです。何かがどう動くかを言葉にすると、この skill はコードと照合し、矛盾を表面化させます — 「あなたのコードは Order 全体をキャンセルしますが、たった今、部分キャンセルが可能だと言いましたね — どちらが正しいのですか？」言語とコードは強制的に一致させられます。

## 意図的に切り出されている

`domain-modeling` はプロジェクトの ubiquitous language を構築するための**唯一の正典**であり、他のあらゆる skill から参照できるよう独立した model-invoked skill として切り出されています。[grill-with-docs](https://aihero.dev/skills-grill-with-docs) は grilling セッションの進行中に用語と決定を記録するためにこれに頼り、[triage](https://aihero.dev/skills-triage) はチケットをプロジェクト自身の言葉に保つためにこれを使い、[improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) は作業中にこれを参照します。

これを standalone に保つ意味は、それらの skill が定める手順にコミットすることなく、モデルを磨く方法についての**リファレンス**として直接参照できることです。言語は一箇所に存在し、それを必要とするすべてのものがそこを指します。

## 全体の中での位置づけ (Where it fits)

`domain-modeling` はいつでも使える standalone であり、固定されたステップとしてよりも、他の skill の*下で*頻繁に動きます。最も近い隣人は [codebase-design](https://aihero.dev/skills-codebase-design) です。共有された言語こそが、deep module とその seam を正確に名付けることを可能にするからです。下流では、落ち着いた glossary こそが [to-prd](https://aihero.dev/skills-to-prd) がプロジェクト自身の言葉で書かれた仕様へと統合する材料になります。どの skill や flow が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が導いてくれます。

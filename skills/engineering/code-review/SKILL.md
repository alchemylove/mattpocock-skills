---
name: code-review
description: 固定点（commit・branch・tag・merge-base）からの変更を、Standards（このリポジトリの明文化された coding standards に従っているか）と Spec（元の issue/PRD が求めた内容と一致するか）の2軸でレビューする。両方のレビューを並列の sub-agent で実行し、並べて報告する。ユーザーが branch・PR・作業中の変更をレビューしたい、または「review since X」を求めたときに使う。
---

`HEAD` とユーザーが指定した固定点との diff を two-axis でレビューする:

- **Standards** — コードはこの repo に明文化された coding standards に従っているか?
- **Spec** — コードは元の issue / PRD / spec を忠実に実装しているか?

両方の軸は **parallel sub-agents** として実行され、互いの context を汚染しない。その後この skill が両者の findings を集約する。

issue tracker はすでにあなたに提供されているはずである — `docs/agents/issue-tracker.md` が無ければ `/setup-matt-pocock-skills` を実行する。

## Process

### 1. 固定点を pin する

ユーザーが言ったものが固定点である — commit SHA、branch 名、tag、`main`、`HEAD~5` など。指定がなければ尋ねる。

diff コマンドを一度だけ記録する: `git diff <fixed-point>...HEAD`（three-dot なので、比較対象は merge-base になる）。`git log <fixed-point>..HEAD --oneline` で commit の一覧もメモしておく。

先に進む前に、固定点が解決すること（`git rev-parse <fixed-point>`）と diff が空でないことを確認する。不正な ref や空の diff はここで失敗させる — 2 つの parallel sub-agent の中で失敗させてはいけない。

### 2. spec の情報源を特定する

以下の順で元となる spec を探す:

1. commit message 内の issue 参照（`#123`、`Closes #45`、GitLab の `!67` など）— `docs/agents/issue-tracker.md` の workflow 経由で取得する。
2. ユーザーが引数として渡したパス。
3. branch 名や feature に一致する `docs/`、`specs/`、`.scratch/` 配下の PRD/spec ファイル。
4. 何も見つからなければ、spec がどこにあるかユーザーに尋ねる。無いと言われたら、**Spec** sub-agent はスキップし「no spec available」と報告する。

### 3. standards の情報源を特定する

`CODING_STANDARDS.md` や `CONTRIBUTING.md` など、コードの書き方を文書化している repo 内のあらゆるもの。

repo が文書化しているものに加えて、Standards 軸には常に下記の **smell baseline** が付随する — repo が何も文書化していなくても適用される、固定の Fowler code smells のセット（_Refactoring_, ch.3）。これを縛る 2 つのルール:

- **repo が優先する。** 文書化された repo の standard は常に勝つ。baseline が指摘するはずのものを repo が是認している場合、その smell は抑制する。
- **常に judgement call。** 各 smell はラベル付けされたヒューリスティック（"possible Feature Envy"）であり、決して hard violation ではない — そしてここでの他の standard と同様、tooling がすでに強制しているものはスキップする。

各 smell は *それが何か* → *どう直すか* という形で読む。diff と照らし合わせる:

- **Mysterious Name** — 関数、変数、型の名前が、それが何をする・何を保持するかを示していない。→ rename する。正直な名前が思いつかないなら、設計自体が曖昧である。
- **Duplicated Code** — 同じ logic の形が変更内の複数の hunk やファイルに現れる。→ 共有の形を抽出し、両方から呼び出す。
- **Feature Envy** — 自分自身のデータより他のオブジェクトのデータに手を伸ばすメソッド。→ そのメソッドを、それが欲しがっているデータの側へ移す。
- **Data Clumps** — 同じ少数の fields や params が常に一緒に移動する（生まれたがっている型)。→ 1 つの型にまとめ、それを渡す。
- **Primitive Obsession** — 独自の型に値する domain concept の代わりを primitive や文字列が務めている。→ その concept 専用の小さな型を与える。
- **Repeated Switches** — 同じ型に対する同じ `switch`/`if`-cascade が変更内で繰り返し現れる。→ polymorphism に置き換える、あるいは両方の箇所が共有する 1 つの map にする。
- **Shotgun Surgery** — 1 つの論理的な変更が diff 内の多数のファイルへの散らばった編集を強いる。→ 変化するものを 1 つの module にまとめる。
- **Divergent Change** — 1 つのファイルや module が複数の無関係な理由で編集されている。→ 各 module が 1 つの理由だけで変わるように分割する。
- **Speculative Generality** — spec が求めていないニーズのために追加された abstraction、parameters、hooks。→ 削除する。実際のニーズが現れるまで inline に戻す。
- **Message Chains** — caller が依存すべきでない長い `a.b().c().d()` の navigation。→ その辿り方を最初のオブジェクト上の 1 つのメソッドの裏に隠す。
- **Middle Man** — ほぼ単に委譲しているだけのクラスや関数。→ それを削り、本来の対象を直接呼ぶ。
- **Refused Bequest** — 継承したもののほとんどを無視または override するサブクラスや実装者。→ 継承をやめ、composition を使う。

### 4. 両方の sub-agent を並列に spawn する

1 つのメッセージに 2 つの `Agent` tool call をまとめて送る。両方とも `general-purpose` subagent を使う。

**Standards sub-agent のプロンプト** — 以下を含める:

- 完全な diff コマンドと commit のリスト。
- 手順 3 で見つけた standards-source ファイルのリスト、**加えて手順 3 の smell baseline** を全文貼り付ける — sub-agent はそれ以外の方法でアクセスできない。
- 指示: "Report — per file/hunk where relevant — (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline smell you spot: name it and quote the hunk. Distinguish hard violations from judgement calls — documented-standard breaches can be hard, but baseline smells are always judgement calls, and a documented repo standard overrides the baseline. Skip anything tooling enforces. Under 400 words."

**Spec sub-agent のプロンプト** — 以下を含める:

- diff コマンドと commit のリスト。
- spec のパスまたは取得済みの内容。
- 指示: "Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong. Quote the spec line for each finding. Under 400 words."

spec が無ければ Spec sub-agent をスキップし、最終レポートにその旨を記す。

### 5. 集約する

2 つのレポートを `## Standards` と `## Spec` の見出しの下に、そのまま、あるいは軽く整えて提示する。findings を**マージしたり再ランク付けしたりしない** — 2 つの軸は意図的に分離されている（_Why two axes_ を参照）。

最後に 1 行の要約を付ける: 軸ごとの findings の総数、そして（あれば）*各軸の中での*最悪の issue。軸をまたいで単一の勝者を選ばない — それはこの分離が防ごうとしている再ランク付けそのものである。

## Why two axes

変更は一方の軸を通り、もう一方で落ちることがある:

- すべての standard に従っているが間違ったものを実装しているコード → **Standards pass, Spec fail.**
- issue が求めた通りに動くが、プロジェクトの convention を破っているコード → **Spec pass, Standards fail.**

別々に報告することで、一方の軸がもう一方を覆い隠すのを防ぐ。

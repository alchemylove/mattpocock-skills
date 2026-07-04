# Docs page を書く (Writing docs pages)

`engineering/` と `productivity/` 内のすべての skill には、`docs/<bucket>/<skill-name>.md` に人間向けの **docs page** がある — docs ツリーは `skills/` 配下のこの2つの bucket フォルダを反映している。`https://aihero.dev/skills-<skill-name>` として公開され、URL はバケットに関わらず常に `skills-<skill-name>` なので、docs のパスはリポジトリ内の整理のためだけのものだ。このページは skill そのものではなく、`SKILL.md` のコピーでもない。promoted なのはこの2つのバケットだけであり、残り（`misc/`、`personal/`、`in-progress/`、`deprecated/`）には docs page がない。

これらの skill の多くは **user-invoked** である: エージェントが代わりに発火してくれることはないため、それらが存在すること・いつ使うべきかを覚えておかなければならない index は *あなた自身* だ。その記憶こそが **cognitive load**（認知負荷）である。docs page の仕事はそれを軽くすることだ — 一人の読者を一つの skill の周りにオリエンテーションし、頭の中に保持でき、いつ使うべきかを知り、システムの中でどこに位置するかを見えるようにする。これらのページは集合的に分散した router であり、それぞれが一つの node である。

promoted skill が追加・リネーム・挙動変更されたときは必ず行動する: docs page を作成または再同期する。リネームの際はファイルも移動する（`docs/<bucket>/<old>.md` → `docs/<bucket>/<new>.md`）。公開 URL が名前を追跡するためだ。`engineering/` と `productivity/` の間を移動する skill は、その docs ファイルも対応するフォルダへ移動する。`misc/`、`personal/`、`in-progress/`、`deprecated/` 内の skill にはページがない — これらのバケットはどれも promoted ではないためだ。それらのいずれかから `engineering/` や `productivity/` へ*移動してくる* skill はページを得て、逆方向へ移動する skill はページを失う。

これらのページは `aihero.dev` 上で公開されるため、**すべてのリンクは絶対パス**である — リポジトリ相対パスは決して使わない。他の skill へのリンクは `https://aihero.dev/skills-<name>` を指す。リポジトリ内へのリンクは完全な `https://github.com/mattpocock/skills/...` URL を指す。リポジトリ内では機能する相対リンクも、公開されると壊れる。

H1 は存在しない — 公開されたページはタイトルを slug から取得する。

## ページ構成 (Page structure)

以下のテンプレートを埋める。**固定フレーム**（Quickstart ブロック、source link、`## What it does`、`## When to reach for it`、`## Where it fits`）はすべてのページに現れる。**可変の中間部**——`## Prerequisites` と自由形式の本文セクション——には、その skill 固有に見合う内容だけを載せ、それ以外は削除する。

<page-template>

クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=<name>
```

```bash
npx skills update <name>
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/<bucket>/<name>)

## 何をするか (What it does)

1〜2段落の平易な文章。まず skill の一文仕事を述べ、次に **defining constraint**（この skill を自明なデフォルトとは異なる振る舞いにする唯一の事実。`to-prd` なら: ユーザーへ再度インタビューせず、すでに分かっていることを統合する）を述べる。「The defining constraint:」や「The key thing:」のようなラベル付きの傍注ではなく、平易な宣言文として書くこと — その定型句は filler にしか読めない。このページで最も価値のある行なので、決して省略しない。

## いつ使うか (When to reach for it)

skill をどう・いつ使うか — 事実上常に存在する2つの beat:

- **Invocation mode。** タイプするのか、エージェントが発火するのかを述べる。user-invoked skill の場合: 「`/<name>` とタイプして呼び出す — エージェントが自力でこれを使うことはない。」 model-invoked skill の場合: 「`/<name>` とタイプするか、タスクに合えばエージェントが自動的に使う。」
- **Trigger boundary。** インデックスの項目: 「〜のときに使う」。兄弟 skill と混同しやすい場合は、もう半分も加える — 「<X> にはこちらではなく [<sibling>](https://aihero.dev/skills-<sibling>) を使う。」

## 前提条件 (Prerequisites)

任意 — skill が機能するために何かが事前に整っている必要がある場合のみ含め、そうでなければ見出しごと省略する。カバーする内容: **書き込み先の workspace**（`grill-with-docs` のような stateful skill は `CONTEXT.md` と ADR を書く。`teach` はディレクトリ全体を構築する — 何をどこに書くかを述べる）、**事前セットアップ**（`triage`/`to-prd`/`to-issues` は `setup-matt-pocock-skills` が issue tracker を設定済みであることを必要とする）、または **repo 固有のツール**。どこでも動く stateless な skill には前提条件がない — そのセクションは削除する。

## <自由形式の中間部>

skill *固有の語彙*で書く1〜3個の短いセクション。腑に落ちるようにする — その skill に合う見出しを自由に選ぶ: 実行する loop、生み出す artifact、作る fork、潰す唯一の anti-pattern。決まった見出しはない。skill は一つの型に収めるには多様すぎる。

唯一譲れないこと: **skill の leading word / defining idea を浮き上がらせる** — `tight` feedback loop、`deep module`、throwaway-code-answers-a-question、red-green など。これは二重に効く: 読者は skill が *何であるか* を学び、後で *使う* ときに考える手がかりとなる語を学ぶ。

## うまく機能しているかの目安 (It's working if)

任意。skill が実際に仕事をしていることを読者に伝える、観察可能なシグナルの短いチェックリスト — 発火したときに何が見えるべきか、発火していないときはそれが無いこと。skill に明確な tell がある場合（例: `to-prd` は再インタビューせずに書き込む。trace の中に leading word が再登場する）に含め、シグナルが曖昧な場合は見出しごと省略する。数個の箇条書きにとどめる。

## 全体の中での位置づけ (Where it fits)

常に存在する。skill をシステムの中に一〜二文で位置づける:

- **Role。** 名指しする: **chain step**（`grill-with-docs → to-prd → to-issues → implement → code-review`）、**run-once setup**（`setup-matt-pocock-skills`）、**periodic maintenance**（`improve-codebase-architecture`、「数日に一度」）、または **reach-for-it-anytime standalone**（`diagnosing-bugs`、`prototype`、`handoff`）のいずれか。standalone の位置づけは正直な一文で十分 — セクションを省略するよりずっとよい。
- **Neighbours。** 重要な1〜2個の兄弟 skill を、それぞれ because 節付きで、絶対パスでリンクする。
- **The map。** [ask-matt](https://aihero.dev/skills-ask-matt)（skill 全体を束ねる router）を指し示し、このページが node であり続け、グラフを描き直さずに済むようにする。

</page-template>

## 規約 (Conventions)

- プロセスではなく**理由 (why)** を説明する。ページは skill をオリエンテーションし位置づけるものであり、`SKILL.md` の手順やテンプレートの丸写しを再現することは決してない — ツールを選ぶ人間に runbook は必要ない。
- skill の**leading words**（_seam_、_deep module_、_tracer bullet_ など）を使い、ページと skill が同じ言語を話すようにする。
- ページ自体を low-load に保つ。これは low-cognitive-load な skill について*の*ドキュメントであり、furniture（余分な見出し、繰り返されるリンク）はまさにそれが反対しているものだ。

## 完了の定義 (Done when)

- ページが `docs/<bucket>/<name>.md` に存在し、リネームやバケット移動の後に古いページが残っていない。
- Quickstart ブロックと source link が正しい bucket と skill を示している。update の行が skill 名を示している。
- `## What it does` が、ラベル付きの傍注ではなく平易な散文として defining constraint を述べている。
- `## When to reach for it` が invocation mode と trigger boundary を述べている。
- `## Where it fits` が role を名指しし、`ask-matt` にリンクしている。
- prerequisite（workspace、事前セットアップ、tooling）が存在する場合はそれが述べられ、存在しない場合はそのセクション自体がない。
- 中間部が leading word を浮き上がらせている。
- すべてのリンクが絶対パスであり、すべて解決する。

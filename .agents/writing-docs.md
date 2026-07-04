# Docs page を書く (Writing docs pages)

`engineering/` と `productivity/` 内のすべての skill には、`docs/<bucket>/<skill-name>.md` に人間向けの **docs page** がある — docs ツリーは `skills/` 配下のこの2つの bucket フォルダを反映している。`https://aihero.dev/skills-<skill-name>` として公開され、URL はバケットに関わらず常に `skills-<skill-name>` なので、docs のパスはリポジトリ内の整理のためだけのものだ。このページは skill そのものではなく、`SKILL.md` のコピーでもない。promoted なのはこの2つのバケットだけであり、残り（`misc/`、`personal/`、`in-progress/`、`deprecated/`）には docs page がない。

これらの skill の多くは **user-invoked** である: エージェントが代わりに発火してくれることはないため、それらが存在すること・いつ使うべきかを覚えておかなければならない index は *あなた自身* だ。その記憶こそが **cognitive load**（認知負荷）である。docs page の仕事はそれを軽くすることだ — 一人の読者を一つの skill の周りにオリエンテーションし、頭の中に保持でき、いつ使うべきかを知り、システムの中でどこに位置するかを見えるようにする。これらのページは集合的に分散した router であり、それぞれが一つの node である。

promoted skill が追加・リネーム・挙動変更されたときは必ず行動する: docs page を作成または再同期する。リネームの際はファイルも移動する（`docs/<bucket>/<old>.md` → `docs/<bucket>/<new>.md`）。公開 URL が名前を追跡するためだ。`engineering/` と `productivity/` の間を移動する skill は、その docs ファイルも対応するフォルダへ移動する。`misc/`、`personal/`、`in-progress/`、`deprecated/` 内の skill にはページがない — これらのバケットはどれも promoted ではないためだ。それらのいずれかから `engineering/` や `productivity/` へ*移動してくる* skill はページを得て、逆方向へ移動する skill はページを失う。

これらのページは `aihero.dev` 上で公開されるため、**すべてのリンクは絶対パス**である — リポジトリ相対パスは決して使わない。他の skill へのリンクは `https://aihero.dev/skills-<name>` を指す。リポジトリ内へのリンクは完全な `https://github.com/mattpocock/skills/...` URL を指す。リポジトリ内では機能する相対リンクも、公開されると壊れる。

H1 は存在しない — 公開されたページはタイトルを slug から取得する。

## ページ構成 (Page structure)

以下のテンプレートを埋める。**固定フレーム**（Quickstart ブロック、source link、`## What it does`、`## When to reach for it`、`## Where it fits`）はすべてのページに現れる。**可変の中間部**——`## Prerequisites` と自由形式の本文セクション——には、その skill 固有に見合う内容だけを載せ、それ以外は削除する。

<page-template>

Quickstart:

```bash
npx skills add mattpocock/skills --skill=<name>
```

```bash
npx skills update <name>
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/<bucket>/<name>)

## What it does

One or two plain-language paragraphs. Lead with the skill's one-sentence job, then state the **defining constraint** — the single fact that makes this skill behave differently from the obvious default (for `to-prd`: it does not interview the user again, it synthesises what is already known). Write it as a plain declarative sentence — never a labelled aside like "The defining constraint:" or "The key thing:"; the formula reads as filler. This line is the most valuable on the page; never omit it.

## When to reach for it

How and when you reach for the skill — two beats, both effectively always present:

- **Invocation mode.** State whether you type it or the agent fires it. A user-invoked skill: "You invoke this by typing `/<name>` — the agent won't reach for it on its own." A model-invoked skill: "Type `/<name>`, or the agent reaches for it automatically when a task fits."
- **Trigger boundary.** The index entry: "reach for this when …". Where the skill is confusable with a sibling, add the other half — "for <X> instead, use [<sibling>](https://aihero.dev/skills-<sibling>)."

## Prerequisites

Optional — include only when the skill needs something in place to be functional; omit the heading entirely otherwise. Covers: a **workspace it writes into** (a stateful skill like `grill-with-docs` writes `CONTEXT.md` and ADRs; `teach` builds a whole directory — say what it writes and where), **prior setup** (`triage`/`to-prd`/`to-issues` need `setup-matt-pocock-skills` to have configured an issue tracker), or **repo-specific tooling**. A stateless skill that runs anywhere has no prerequisites — drop the section.

## <free-form middle>

One to three short sections, in the skill's *own vocabulary*, that make it click — choose whatever headings fit the skill: the loop it runs, the artifact it produces, the fork it makes, the one anti-pattern it kills. There is no prescribed heading; the skills are too heterogeneous for one.

The single non-negotiable: **surface the skill's leading word / defining idea** — `tight` feedback loop, `deep module`, throwaway-code-answers-a-question, red-green. It pays off twice: the reader learns what the skill *is*, and learns the word they'll later think with to *reach for* it.

## It's working if

Optional. A short, checkable list of the observable signals that tell the reader the skill is actually doing its job — what they should see when it fires, and by absence when it hasn't. Include it when a skill has crisp tells (e.g. `to-prd` writes without re-interviewing you; a leading word reappearing in the trace); omit the heading when the signals are vague. A few bullets, no more.

## Where it fits

Always present. Situate the skill in the system in a sentence or two:

- **Role.** Name it: a **chain step** (`grill-with-docs → to-prd → to-issues → implement → code-review`), a **run-once setup** (`setup-matt-pocock-skills`), **periodic maintenance** (`improve-codebase-architecture`, "every few days"), or a **reach-for-it-anytime standalone** (`diagnosing-bugs`, `prototype`, `handoff`). A standalone's map is one honest sentence — far better than omitting the section.
- **Neighbours.** The one or two siblings that matter, each with a because-clause, linked absolutely.
- **The map.** Point to [ask-matt](https://aihero.dev/skills-ask-matt), the router over the whole set, so this page stays a node and never has to redraw the graph.

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

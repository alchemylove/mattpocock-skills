---
name: writing-fragments
description: Writing, explore — mine raw fragments, no structure yet.
disable-model-invocation: true
---

<what-to-do>

This is pure **explore**: widen the space of what could be written without committing to structure — committing is _exploit_, a separate skill's job. Run a grilling session that produces fragments, interviewing the user relentlessly about whatever they want to write about. Imposing phases, outlines, or article structure is out of scope here.

As fragments emerge from either side of the conversation, append them to a single markdown file.

path をユーザーが渡していなければ、一度だけ保存先を確認し、セッション中は記憶する。

最初の発言から fragment を捕捉する。初期 prompt を含む。

初回書き込み時、working title を含む H1 を 1 つだけ先頭に置く (後で変えてよい) — metadata、TOC、date はなし。

</what-to-do>

<supporting-info>

## fragment とは (What is a fragment)

fragment は最終記事に残りうるテキストの断片。作者が読めば意味が分かること — 作者が何を指しているか分かる — が、用語を定義したり冷たい読者に理解可能である必要はない。基準は "is this a piece of good writing?" であり、"is this a self-contained argument?" ではない。

fragment は意図的に heterogeneous。fragment になりうる例:

- A sharp sentence you'd want to deploy somewhere but don't yet know where.
- A claim with a one-line justification.
- A vignette: a thing that happened, a code snippet, a scenario, an analogy.
- A half-thought: "something about how X feels like Y, work this out later."
- A quote, a piece of dialogue, an overheard line.
- A list of related observations that hang together by feel.
- A complaint, a confession, a punchline.
- A **leading word** — a compact metaphor or coinage the whole piece can hang on (one term that names the idea, the way _tracer bullets_ or _fog of war_ names a whole pattern).

Of these, the leading word is the most valuable fragment to land. It is load-bearing: name the right one in explore and it shapes the structure, the transitions, and the title later — paying dividends through the entire exploit phase. When the conversation circles a recurring idea, push to coin a word for it.

小説家の日記がモデル: 後で raw material として掘られる、何年も続く構造化されていない noticing。fragment は noticing。

## ファイルフォーマット (File format)

```markdown
# Working title

A first fragment lives here.

It can be multiple paragraphs. It can include lists, code, quotes — whatever
shape the fragment naturally takes.

---

A second fragment.

---

> A quoted line that the user wants to keep around.

A reaction to it.

---

- A cluster of related observations
- That hang together by feel
- And want to be near each other
```

fragment は水平線 (`\n---\n`) で区切る。body 内に heading なし。tag なし。追加順以外の順序なし。

## 執筆リズム (Writing rhythm)

黙って append。各 fragment ごとに許可を求めない。追加したことは軽く触れる ("adding that") が、save dialog で会話を中断しない。

書く前に毎回: file を disk から再読み込み。ユーザーがターン間に fragment を編集、並べ替え、削除している可能性 — 変更を保持。file を上書きしない; append のみ (またはユーザーが求めた場合、特定 fragment を in place で編集)。

ユーザーはいつでも "cut the last one"、"rewrite that one sharper"、"merge those two" と言える。それらを第一級の指示として扱う。

</supporting-info>

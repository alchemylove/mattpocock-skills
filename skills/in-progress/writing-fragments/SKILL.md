---
name: writing-fragments
description: Grilling session that mines the user for fragments — heterogeneous nuggets of writing (claims, vignettes, sharp sentences, half-thoughts) — and appends them to a single document as raw material for a future article. Use when the user wants to develop ideas before imposing structure, or mentions "fragments", "ideate", or "raw material" for writing.
---

<what-to-do>

fragment を生成する grilling session を実行する。ユーザーが書きたいことについて徹底的にインタビューする。phase、outline、structure を課さない — それは明示的にスコープ外。

会話のどちら側からでも fragment が現れたら、1 つの markdown file に append する。ユーザーはセッション中にこの file を編集する; 書く前に常に再読み込みして編集を保持する。

path をユーザーが渡していなければ、一度だけ保存先を確認し、セッション中は記憶する。

最初の発言から fragment を捕捉する。初期 prompt を含む。

初回書き込み時、working title を含む H1 を 1 つだけ先頭に置く (後で変えてよい) — metadata、TOC、date はなし。

</what-to-do>

<supporting-info>

## fragment とは (What is a fragment)

fragment は最終記事に残りうるテキストの断片。作者が読めば意味が分かること — 作者が何を指しているか分かる — が、用語を定義したり冷たい読者に理解可能である必要はない。基準は "is this a piece of good writing?" であり、"is this a self-contained argument?" ではない。

fragment は意図的に heterogeneous。fragment になりうる例:

- どこかに使いたい鋭い 1 文だが、まだ場所が分からない。
- 1 行の justification 付き claim。
- vignette: 起きたこと、code snippet、scenario、analogy。
- half-thought: "something about how X feels like Y, work this out later."
- quote、dialogue、聞き逃した 1 行。
- 感覚でまとまる関連 observation の list。
- complaint、confession、punchline。

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

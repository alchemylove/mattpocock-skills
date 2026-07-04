---
name: writing-fragments
description: Writing、explore — raw な fragment を掘り出す、まだ structure はない。
disable-model-invocation: true
---

<what-to-do>

これは純粋な **explore** である: structure にコミットすることなく、書きうるものの空間を広げる — コミットするのは _exploit_ であり、別の skill の仕事である。fragment を生み出す grilling セッションを実行し、ユーザーが書きたいことについて容赦なくインタビューする。phase、outline、article structure を課すことはここではスコープ外である。

会話のどちらの側からも fragment が現れたら、それらを単一の markdown file に追記する。

path をユーザーが渡していなければ、一度だけ保存先を確認し、セッション中は記憶する。

最初の発言から fragment を捕捉する。初期 prompt を含む。

初回書き込み時、working title を含む H1 を 1 つだけ先頭に置く (後で変えてよい) — metadata、TOC、date はなし。

</what-to-do>

<supporting-info>

## fragment とは (What is a fragment)

fragment は最終記事に残りうるテキストの断片。作者が読めば意味が分かること — 作者が何を指しているか分かる — が、用語を定義したり冷たい読者に理解可能である必要はない。基準は "is this a piece of good writing?" であり、"is this a self-contained argument?" ではない。

fragment は意図的に heterogeneous。fragment になりうる例:

- どこかで使いたいが、まだどこか分からない鋭い一文。
- 一行の根拠を伴う主張。
- vignette: 起きた出来事、code snippet、シナリオ、アナロジー。
- 半端な思考: "something about how X feels like Y, work this out later." のようなもの。
- quote、dialogue の一節、小耳に挟んだ一言。
- 感覚的にまとまっている関連する observation のリスト。
- 不満、告白、punchline。
- **leading word** — piece 全体がぶら下がれる compact な metaphor や造語 (_tracer bullets_ や _fog of war_ が一つのパターン全体を指すように、idea に名前を付ける一つの term)。

これらの中で、leading word は着地させる価値が最も高い fragment である。それは load-bearing である: explore で正しいものに名前を付ければ、それが後の structure、transition、title を形作る — exploit phase 全体を通して配当を生む。会話が繰り返し同じ idea の周りを巡るときは、それに語を造ることを推す。

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

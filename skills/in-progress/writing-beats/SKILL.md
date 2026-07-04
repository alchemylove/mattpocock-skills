---
name: writing-beats
description: Writing、exploit — raw material を beat の journey に組み立て、beat がその用語に寄りかかる前に各 term を grounding する。
disable-model-invocation: true
---

<what-to-do>

ユーザーが raw material の markdown file を渡した (または渡す予定)。これは **exploit** である: exploring はすでに終わっており、pile は固定されている — その中を通る path にコミットし、pile を掘って各 beat を埋める。

記事の保存先をユーザーが指定していなければ、一度だけ確認し、path を記憶する。

その後、choose-your-own-adventure スタイルで beat ごとの journey を実行する:

1. **前提を確立する。** どの beat よりも前に、audience がすでに知って入ってくることは何か — 最初から **grounded** な concept は何か — をユーザーと決める。それ以外のすべては、後の beat が使う前に、ある beat によって grounded にされなければならない。[Grounding](#grounding) を参照。
2. raw material から引き出した 2–3 の候補となる **starting beat** を書く。それぞれが記事への異なる入口である。各 beat は grounded な concept にのみ寄りかかってよい; 各 beat がどの新しい concept を grounds するかを書き留める。article file に書き込む前に、ユーザーに beat を示す。ユーザーが一つを選ぶ。その選択が unlock する beat をプレビューする — まるでユーザーが path の少し先まで見えているかのように。
3. ユーザーが starting beat を選んだら、**その beat だけ** を article file に書く。beat は一文かもしれないし、複数の段落かもしれない — その beat が自然にそうであるものでよい。そこで止まる。
4. article file を disk から再読み込みする。そして、記事が今立っている地点から journey が pivot しうる異なる方向として、2–3 の候補となる **次の beat** を提示する。各候補は、現在の grounded set から到達可能でなければならない; 各 beat がどの concept を grounds するかを書き留める。
5. 記事が自然な終わりに達するまでステップ 3–5 をループする。

</what-to-do>

<supporting-info>

## Grounding

すべての **concept** は、beat がそれに寄りかかる前に **grounded** されていなければならない: audience がそれを知って入ってきたか、それより前の beat でそれに出会ったかのいずれかである。grounded されていない concept に手を伸ばす beat は読者を失う — それは journey が決してしてはならない一手である。単位は concept であり、それを表す語ではない: jargon が一つも見当たらなくても、beat は読者が持っていない idea に寄りかかることがありうる。concept に名前 — **term** — がある場合、それを grounding するとは idea と term を一緒に着地させることを意味する。

concept は次の 2 通りのいずれかで grounded になる:

- **Prerequisite** — 最初の beat より前に grounded にされる。audience がそれを持ち込む。最初に固定される。
- **Introduced** — ある beat がそれを確立し、それ以降のすべての beat にとって grounded になる。

つまり各 beat は 2 つの仕事をする: すでに grounded な concept を **requires** し、新しいものを **grounds** する。これまでに grounded になったものの running list を保ち、beat が着地するたびに更新する。

これが choose-your-own-adventure の形を作る。候補となる beat は、それが requires するものがすべてすでに grounded であるときにのみ到達可能である; concept X を grounds する beat を選ぶと、X を待っていたすべての beat が unlock される。次の beat を提示するときは、それらすべてが現在の grounded set から到達可能でなければならず — 各 beat が何を grounds するかを述べ、ユーザーがどの path が開くかを見られるようにする。

大きなレバーは、何を prerequisite にし、何を piece の内部で grounding するかである。前もって要求しすぎると、それを持たない読者を締め出す; 内部で grounding しすぎると、序盤の beat が定義まみれになる。prerequisite を確立するときにこれをユーザーと決め、魅力的な beat が実はまだ何も grounding していない concept を要求すると分かった場合は必ず見直す — 修正はその前に grounding beat を置くか、その concept を prerequisite に格上げするかのいずれかである。

## beat とは (What is a beat)

beat は journey の 1 手。1 つのことをする — 場面を設定、ポイントを着地、質問を投げ、余談を挟む、角度を捻る。そして止まり、次の beat が pivot できる地点に読者を残す。

beat のサイズは必要な分だけ:

- 1 手がそれだけなら 1 文 ("And then nothing happened for three weeks.").
- 手に setup が必要なら短い段落。
- beat が自己完結の vignette、argument、example なら複数段落。

"beat" に 5 段落と 3 つの subheading が必要なら、それは beat ではない — 2 つの beat がくっついている。分割する。

## pile からの引き出し (Pulling from the pile)

raw な pile から material を引き出し、各 beat を埋める。paraphrase、split、recombine、quote してよい。pile は quarry である。

## journey の終わり (Ending the journey)

記事は journey が完了したときに終わる — pile が空になったときではない。ほとんどの pile には入らなかった fragment が残る。それでよい; raw material を必要以上に持つことが目的。

## 執筆リズム (Writing rhythm)

- 1 beat ずつ append。先走って書かない。
- 書く前に毎回 article file を disk から再読み込み。ユーザーの編集は絶対に保持。
- ユーザーが前の beat を大幅に編集したら、それに応じて続きを変える。
- ユーザーが "rewrite that beat" や "go back and try a different beat 3" と言ったら実行 — その場で編集し、残りはそのまま。

</supporting-info>

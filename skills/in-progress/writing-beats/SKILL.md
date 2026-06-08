---
name: writing-beats
description: Shape an article as a journey of beats, choose-your-own-adventure style. The user picks a starting beat from the raw material, you write only that beat, then offer options for where to pivot next, beat by beat, until the article reaches a natural end. Use when the user has raw material and wants to assemble it as a narrative rather than an argument.
---

<what-to-do>

ユーザーが raw material の markdown file を渡す (または渡す予定)。

記事の保存先をユーザーが指定していなければ、一度だけ確認し、path を記憶する。

次に beat ごとの journey を実行:

1. raw material から 2–3 個の候補 **starting beat** を書く。それぞれ記事への異なる入口。article file に書く前にユーザーに beat を見せる。ユーザーが 1 つ選ぶ。書いた後にどの beat に続くかを少し先まで preview する — ユーザーが道の先を少し見ているかのように。
2. ユーザーが starting beat を選んだら、**その beat のみ**を article file に書く。beat は 1 文でも複数段落でもよい — beat が自然に必要とする長さ。そこで止める。
3. article file を disk から再読み込み。次に 2–3 個の候補 **next beat** を提示 — 記事の現在地から journey が pivot しうる異なる方向。
4. 記事が自然な終わりに達するまで step 2–4 をループ。

</what-to-do>

<supporting-info>

## beat とは (What is a beat)

beat は journey の 1 手。1 つのことをする — 場面を設定、ポイントを着地、質問を投げ、余談を挟む、角度を捻る。そして止まり、次の beat が pivot できる地点に読者を残す。

beat のサイズは必要な分だけ:

- 1 手がそれだけなら 1 文 ("And then nothing happened for three weeks.").
- 手に setup が必要なら短い段落。
- beat が自己完結の vignette、argument、example なら複数段落。

"beat" に 5 段落と 3 つの subheading が必要なら、それは beat ではない — 2 つの beat がくっついている。分割する。

## 1 beat の書き方 (Writing one beat)

beat が選ばれたら、**その beat のみ**を article file に書く。次の beat は書かない。

raw pile から material を引いて beat を埋める。paraphrase、分割、再結合、引用ができる。pile は採石場。

## journey の終わり (Ending the journey)

記事は journey が完了したときに終わる — pile が空になったときではない。ほとんどの pile には入らなかった fragment が残る。それでよい; raw material を必要以上に持つことが目的。

## 執筆リズム (Writing rhythm)

- 1 beat ずつ append。先走って書かない。
- 書く前に毎回 article file を disk から再読み込み。ユーザーの編集は絶対に保持。
- ユーザーが前の beat を大幅に編集したら、それに応じて続きを変える。
- ユーザーが "rewrite that beat" や "go back and try a different beat 3" と言ったら実行 — その場で編集し、残りはそのまま。

</supporting-info>

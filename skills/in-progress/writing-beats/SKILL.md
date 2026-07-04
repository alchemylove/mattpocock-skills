---
name: writing-beats
description: Writing, exploit — assemble raw material into a journey of beats, grounding each term before a beat leans on it.
disable-model-invocation: true
---

<what-to-do>

The user has passed (or will pass) a markdown file of raw material. This is **exploit**: the exploring is done, the pile is fixed — commit to a path through it and mine the pile to fill each beat.

記事の保存先をユーザーが指定していなければ、一度だけ確認し、path を記憶する。

Then run a beat-by-beat journey, choose-your-own-adventure style:

1. **Establish the prerequisites.** Before any beats, settle with the user what the audience already knows walking in — the concepts that are **grounded** from the start. Everything else must be grounded by a beat before a later beat can use it. See [Grounding](#grounding).
2. Write 2–3 candidate **starting beats**, drawn from the raw material. Each is a different entry point into the article. Each may only lean on grounded concepts; note what new concepts each one grounds. Show the user the beats before writing to the article file. The user picks one. Preview what beats that pick unlocks — as if the user is seeing a little way down the path.
3. Once the user picks a starting beat, write **only that beat** to the article file. A beat may be one sentence or several paragraphs — whatever that beat naturally is. Stop there.
4. Re-read the article file from disk. Then offer 2–3 candidate **next beats** — different directions the journey could pivot to from where the article now stands. Each must be reachable from the current grounded set; note what each one grounds.
5. Loop steps 3–5 until the article reaches a natural end.

</what-to-do>

<supporting-info>

## Grounding

Every **concept** has to be **grounded** before a beat can lean on it: the audience either walked in knowing it or met it in an earlier beat. A beat that reaches for an ungrounded concept loses the reader — that is the one move the journey can't make. The unit is the concept, not the word for it: a beat can lean on an idea the reader lacks even with no jargon in sight. Where a concept has a name — a **term** — grounding it means landing the idea and the term together.

A concept gets grounded one of two ways:

- **Prerequisite** — grounded before the first beat. The audience brings it. Fixed at the start.
- **Introduced** — a beat establishes it, and from then on it's grounded for every later beat.

So each beat does two jobs: it **requires** concepts that are already grounded, and it **grounds** new ones. Keep a running list of what's grounded so far, and update it each time a beat lands.

This is what shapes the choose-your-own-adventure. A candidate beat is only reachable if everything it requires is already grounded; picking a beat that grounds concept X unlocks every beat that was waiting on X. When you offer next beats, they must all be reachable from the current grounded set — and say what each one grounds, so the user can see which paths it opens.

The big lever is what you make a prerequisite versus what you ground inside the piece. Demand too much up front and you shut out readers who don't have it; ground too much inside and the early beats drown in definitions. Settle this with the user when you establish prerequisites, and revisit it whenever a tempting beat turns out to require a concept nothing has grounded yet — the fix is either a grounding beat before it, or promoting the concept to a prerequisite.

## What is a beat

beat は journey の 1 手。1 つのことをする — 場面を設定、ポイントを着地、質問を投げ、余談を挟む、角度を捻る。そして止まり、次の beat が pivot できる地点に読者を残す。

beat のサイズは必要な分だけ:

- 1 手がそれだけなら 1 文 ("And then nothing happened for three weeks.").
- 手に setup が必要なら短い段落。
- beat が自己完結の vignette、argument、example なら複数段落。

"beat" に 5 段落と 3 つの subheading が必要なら、それは beat ではない — 2 つの beat がくっついている。分割する。

## Pulling from the pile

Pull material from the raw pile to populate each beat. You can paraphrase, split, recombine, or quote. The pile is a quarry.

## journey の終わり (Ending the journey)

記事は journey が完了したときに終わる — pile が空になったときではない。ほとんどの pile には入らなかった fragment が残る。それでよい; raw material を必要以上に持つことが目的。

## 執筆リズム (Writing rhythm)

- 1 beat ずつ append。先走って書かない。
- 書く前に毎回 article file を disk から再読み込み。ユーザーの編集は絶対に保持。
- ユーザーが前の beat を大幅に編集したら、それに応じて続きを変える。
- ユーザーが "rewrite that beat" や "go back and try a different beat 3" と言ったら実行 — その場で編集し、残りはそのまま。

</supporting-info>

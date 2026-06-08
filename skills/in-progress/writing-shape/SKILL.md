---
name: writing-shape
description: Take a markdown file of raw material and shape it into an article through a conversational session — drafting candidate openings, growing the piece paragraph by paragraph, arguing about format (lists, tables, callouts, quotes) at each step. Use when the user has a pile of notes, fragments, or a rough draft and wants help turning it into something publishable.
---

<what-to-do>

ユーザーが raw material の markdown file を渡す (または渡す予定)。入力 pile として扱う — 整った fragment のリストから、構造化されていない長文、transcript まで何でもよい。フォーマットは問わない。何もする前に最初から最後まで読む。

次に、別の article ドキュメントを生成する shaping session を実行する。raw material file は編集しない — この skill にとって read-only。

記事の保存先をユーザーが指定していなければ、一度だけ確認し、path を記憶する。ユーザーはセッション中に article file を編集する; 書く前に常に再読み込みして編集を保持する。

</what-to-do>

<supporting-info>

## ループ (The loop)

1. **pile を読む (Read the pile.)** 入力 file を最初から最後まで読む。内容の全体像を把握する。
2. **2–3 個の候補 opening をドラフト (Draft 2–3 candidate openings.)** 各 opening は記事の異なる thesis や角度を示唆する。すべて見せる。ユーザーに選ばせるか hybrid を作らせる。選ばれた opening が記事の残りが果たすべきことを定義する。
3. **段落ごとに育てる (Grow paragraph by paragraph.)** opening が固まったら、"given this opening, what does the reader need to hear next?" と問う。pile から material を引いて答える。次の beat が paragraph、list、table、callout、quote、code block か議論する。各フォーマット選択は意図的で説明可能であること。
4. **進めながら article file に append (Append to the article file as you go.)** batch しない。合意した段落や block をすぐ書き、ユーザーが記事の形になっていくのを見られるようにする。
5. **記事が終わるまで step 3 をループ (Loop step 3 until the article is done.)** 終わりはユーザーが決める。

## 会話の雰囲気 (Conversational feel)

これは逆転した grilling session。ideation では "what are you actually noticing?" だった。ここでは "what is this article actually arguing, and in what order does the reader need to hear it?" と問う。押し返す。弱い transition を見逃さない。段落がその場を稼いでいなければ切る。

使い続ける具体的な move:

- "What does this paragraph do for the reader that the previous one didn't?"
- "If I cut this, what breaks?"
- "Is this prose, or should it be a list? Why prose?"
- "This sentence is doing two jobs — split it or pick one."
- "The opening promised X. We've drifted to Y. Either re-thread it or change the opening."

## pile からの引き出し (Pulling from the pile)

raw material を script ではなく採石場として扱う。fragment を引き出し、周囲の段落に合わせて rework して配置する。fragment は複数段落に分割、別のものと merge、paraphrase してよい。pile の仕事は掘られること; 記事の仕事は 1 つの声で読めること。

pile に記事が必要とするものがなければ、gap を明示: "We need an example here and the pile doesn't have one — give me one now or we cut this section."

## 実際に行うフォーマット議論 (Format arguments to actually have)

beat の描画方法を選ぶとき、ユーザーと声に出して次の tradeoff を検討する (黙って決めない):

- **Prose vs. list.** Prose は argument を運ぶ; list は並列項目を運ぶ。項目が真に並列でなければ prose がよい。並列なら list の方が scan が速い。
- **Inline vs. callout.** Tips、warnings、余談は callout (`> [!TIP]`、`> [!NOTE]`) — ただし inline だと本論を本当に derail する場合のみ。そうでなければ inline のまま。
- **Table vs. repeated structure.** 同じ shape が同じ field で 3 回以上繰り返されるなら table。そうでなければ bold lead 付き prose。
- **Quote vs. paraphrase.** 元の wording がポイントなら quote。idea だけが重要なら paraphrase。
- **Code block vs. inline code.** 複数行、実行可能、または illustrative → block。単一 token または identifier → inline。

## 執筆リズム (Writing rhythm)

合意した block ごとに article file に append。書く前に毎回 file を disk から再読み込み — ユーザーがターン間に編集している可能性がある。盲目的に上書きしない。段落の書き直しを求められたら、その段落だけ in place で編集; 残りはそのまま。

## スコープ外 (Out of scope)

- pile にない新しい fragment の採掘 (pile が入力 — 不完全なら gap を名指しし、ユーザーに埋めてもらうか section を切る)。
- raw material file の編集。
- 特定 platform 向けの publishing、formatting、ユーザーが求めていない frontmatter の追加。

</supporting-info>

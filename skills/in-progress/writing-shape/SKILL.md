---
name: writing-shape
description: Writing, exploit — shape raw material into an article, paragraph by paragraph.
disable-model-invocation: true
---

<what-to-do>

ユーザーが raw material の markdown file を渡す (または渡す予定)。入力 pile として扱う — 整った fragment のリストから、構造化されていない長文、transcript まで何でもよい。フォーマットは問わない。何もする前に最初から最後まで読む。

Then run a shaping session that produces a separate article document. This is **exploit**: the exploring is done, the pile is fixed — commit to a structure and mine the pile to fill it. Do not edit the raw material file — it is read-only to this skill.

If the user did not say where to save the article, ask once and remember the path.

</what-to-do>

<supporting-info>

## ループ (The loop)

1. **Read the pile.** Read the input file in full. Form a sense of what's in it.
2. **Establish the prerequisites.** Settle with the user what the reader knows walking in — the concepts that are **grounded** from the start. Everything else must be grounded by a block before a later block can lean on it. See [Grounding](#grounding).
3. **Draft 2–3 candidate openings.** Each opening should imply a different thesis or angle for the article. Show all of them. Force the user to pick or compose a hybrid. The chosen opening defines what the rest of the article must do.
4. **Grow paragraph by paragraph.** After the opening lands, ask "given this opening, what does the reader need to hear next?" Pull material from the pile to answer. The next block may only lean on grounded concepts, and grounds new ones as it lands. Argue about the form the next block takes — a paragraph, a list, a table, a callout, a quote, a code block. Each format choice should be deliberate and defensible.
5. **Append to the article file as you go.** Don't batch. Write each agreed paragraph or block immediately so the user can see the article taking shape.
6. **Loop step 4 until the article is done.** The user decides when it's done.

## Grounding

Every **concept** has to be **grounded** before a block can lean on it: the reader either walked in knowing it or met it in an earlier block. A block that reaches for an ungrounded concept loses the reader. The unit is the concept, not the word for it — a block can lean on an idea the reader lacks even with no jargon in sight. Where a concept has a name — a **term** — grounding it means landing the idea and the term together.

A concept gets grounded one of two ways:

- **Prerequisite** — grounded before the opening. The reader brings it. Fixed at the start.
- **Introduced** — a block establishes it, and from then on it's grounded for the rest of the article.

Keep a running list of what's grounded. When you ask "what does the reader need to hear next?", an ungrounded concept the next move needs is itself the answer: ground it first — here or in an earlier block — or you can't make the move. This is the gap-naming of [Pulling from the pile](#pulling-from-the-pile) one level up: there the pile is missing material; here the article is missing a foundation.

The lever is what you make a prerequisite versus what you ground inside the article. Demand too much up front and you shut readers out; ground too much inside and the opening drowns in definitions. Settle it with the user when you establish prerequisites.

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

When choosing how to render a block, weigh these tradeoffs out loud with the user, not silently:

- **Prose vs. list.** Prose は argument を運ぶ; list は並列項目を運ぶ。項目が真に並列でなければ prose がよい。並列なら list の方が scan が速い。
- **Inline vs. callout.** Tips、warnings、余談は callout (`> [!TIP]`、`> [!NOTE]`) — ただし inline だと本論を本当に derail する場合のみ。そうでなければ inline のまま。
- **Table vs. repeated structure.** 同じ shape が同じ field で 3 回以上繰り返されるなら table。そうでなければ bold lead 付き prose。
- **Quote vs. paraphrase.** 元の wording がポイントなら quote。idea だけが重要なら paraphrase。
- **Code block vs. inline code.** 複数行、実行可能、または illustrative → block。単一 token または identifier → inline。

## 執筆リズム (Writing rhythm)

合意した block ごとに article file に append。書く前に毎回 file を disk から再読み込み — ユーザーがターン間に編集している可能性がある。盲目的に上書きしない。段落の書き直しを求められたら、その段落だけ in place で編集; 残りはそのまま。

## スコープ外 (Out of scope)

- Mining for new fragments that aren't in the pile (handle gaps as in "Pulling from the pile").
- Editing the raw material file.
- Publishing, formatting for a specific platform, or adding frontmatter the user didn't ask for.

</supporting-info>

---
name: writing-shape
description: Writing、exploit — raw material を段落ごとに article へと形作る。
disable-model-invocation: true
---

<what-to-do>

ユーザーが raw material の markdown file を渡す (または渡す予定)。入力 pile として扱う — 整った fragment のリストから、構造化されていない長文、transcript まで何でもよい。フォーマットは問わない。何もする前に最初から最後まで読む。

そして、独立した article document を生み出す shaping セッションを実行する。これは **exploit** である: exploring はすでに終わっており、pile は固定されている — structure にコミットし、pile を掘ってそれを埋める。raw material file は編集しない — この skill にとって read-only である。

ユーザーが記事の保存先を言っていなければ、一度だけ確認し、path を記憶する。

</what-to-do>

<supporting-info>

## ループ (The loop)

1. **pile を読む。** 入力 file を最初から最後まで読む。中身の感覚を掴む。
2. **前提を確立する。** 読者がすでに知って入ってくることは何か — 最初から **grounded** な concept は何か — をユーザーと決める。それ以外のすべては、後の block が寄りかかる前に、ある block によって grounded にされなければならない。[Grounding](#grounding) を参照。
3. **2–3 の候補となる opening を draft する。** 各 opening は記事にとって異なる thesis や角度を示唆すべきである。すべてを示す。ユーザーに一つを選ばせるか、hybrid を組ませる。選ばれた opening が、記事の残りが何をすべきかを規定する。
4. **段落ごとに育てる。** opening が着地したら、「この opening を踏まえて、読者は次に何を聞く必要があるか?」と問う。pile から material を引き出して答える。次の block は grounded な concept にのみ寄りかかってよく、着地する際に新しい concept を grounds する。次の block がどの形を取るか — 段落、list、table、callout、quote、code block — を議論する。各 format の選択は意図的かつ弁護可能であるべき。
5. **進めながら article file に追記する。** batch しない。合意した段落や block をすぐに書き、ユーザーが記事の形になっていく様子を見られるようにする。
6. **記事が完成するまでステップ 4 をループする。** いつ完成かはユーザーが決める。

## Grounding

すべての **concept** は、block がそれに寄りかかる前に **grounded** されていなければならない: 読者がそれを知って入ってきたか、それより前の block でそれに出会ったかのいずれかである。grounded されていない concept に手を伸ばす block は読者を失う。単位は concept であり、それを表す語ではない — jargon が一つも見当たらなくても、block は読者が持っていない idea に寄りかかることがありうる。concept に名前 — **term** — がある場合、それを grounding するとは idea と term を一緒に着地させることを意味する。

concept は次の 2 通りのいずれかで grounded になる:

- **Prerequisite** — opening より前に grounded にされる。読者がそれを持ち込む。最初に固定される。
- **Introduced** — ある block がそれを確立し、それ以降記事の残り全体にとって grounded になる。

grounded になったものの running list を保つ。「読者は次に何を聞く必要があるか?」と問うとき、次の一手が必要とする grounded でない concept こそがその答えである: まずそれを grounding する — ここで、あるいはそれより前の block で — さもなければその一手を打てない。これは一段階上の [Pulling from the pile](#pulling-from-the-pile) における gap-naming と同じである: そこでは pile に material が欠けていた; ここでは記事に foundation が欠けている。

レバーは、何を prerequisite にし、何を記事の内部で grounding するかである。前もって要求しすぎると読者を締め出す; 内部で grounding しすぎると opening が定義まみれになる。prerequisite を確立するときにこれをユーザーと決める。

## 会話の雰囲気 (Conversational feel)

これは逆転した grilling session。ideation では「実際に何に気づいているか?」だった。ここでは「この記事は実際に何を主張していて、読者はどの順番でそれを聞く必要があるか?」と問う。押し返す。弱い transition を見逃さない。段落がその場を稼いでいなければ切る。

使い続ける具体的な move:

- 「この段落は、前の段落がしなかった何を読者にもたらすか?」
- 「これを切ったら何が壊れるか?」
- 「これは prose か、それともリストにすべきか? なぜ prose なのか?」
- 「この文は2つの仕事をしている — 分けるか、どちらか一方を選べ。」
- 「opening は X を約束していた。我々は Y にドリフトしている。再度糸を通すか、opening を変えるかだ。」

## pile からの引き出し (Pulling from the pile)

raw material を script ではなく採石場として扱う。fragment を引き出し、周囲の段落に合わせて rework して配置する。fragment は複数段落に分割、別のものと merge、paraphrase してよい。pile の仕事は掘られること; 記事の仕事は 1 つの声で読めること。

pile に記事が必要とするものがなければ、gap を明示: "We need an example here and the pile doesn't have one — give me one now or we cut this section."

## 実際に行うフォーマット議論 (Format arguments to actually have)

block をどう描画するかを選ぶとき、これらの tradeoff を黙ってではなくユーザーと声に出して検討する:

- **Prose vs. list.** Prose は argument を運ぶ; list は並列項目を運ぶ。項目が真に並列でなければ prose がよい。並列なら list の方が scan が速い。
- **Inline vs. callout.** Tips、warnings、余談は callout (`> [!TIP]`、`> [!NOTE]`) — ただし inline だと本論を本当に derail する場合のみ。そうでなければ inline のまま。
- **Table vs. repeated structure.** 同じ shape が同じ field で 3 回以上繰り返されるなら table。そうでなければ bold lead 付き prose。
- **Quote vs. paraphrase.** 元の wording がポイントなら quote。idea だけが重要なら paraphrase。
- **Code block vs. inline code.** 複数行、実行可能、または illustrative → block。単一 token または identifier → inline。

## 執筆リズム (Writing rhythm)

合意した block ごとに article file に append。書く前に毎回 file を disk から再読み込み — ユーザーがターン間に編集している可能性がある。盲目的に上書きしない。段落の書き直しを求められたら、その段落だけ in place で編集; 残りはそのまま。

## スコープ外 (Out of scope)

- pile にない新しい fragment を掘ること ("Pulling from the pile" と同様に gap として扱う)。
- raw material file を編集すること。
- 公開すること、特定プラットフォーム向けの整形をすること、ユーザーが求めていない frontmatter を追加すること。

</supporting-info>

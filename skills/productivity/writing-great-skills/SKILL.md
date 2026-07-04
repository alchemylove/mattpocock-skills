---
name: writing-great-skills
description: skills を上手く書き・編集するためのリファレンス — skill を予測可能にする語彙と原則。
disable-model-invocation: true
---

skill は stochastic なシステムから determinism を絞り出すために存在する。**Predictability** — agent が毎回同じ output ではなく同じ _process_ を取ること — が根本的な美徳であり、以下のすべてのレバーはこれに資する。

**太字の用語** は [`GLOSSARY.md`](GLOSSARY.md) で定義されている。完全な意味はそちらを参照する。

## Invocation

2 つの選択肢があり、それぞれ異なるコストとトレードオフになる:

- **model-invoked** な skill は **description** を保持するため、agent が自律的に発火できる _うえに_ 他の skill からも到達できる（もちろん名前を直接タイプしてもよい）。これは **context load** を発生させる — description は毎ターン window に載り続ける。仕組み: `disable-model-invocation` を省略し、豊富な trigger 表現（"Use when the user wants…, mentions…"）を持つ model 向けの description を書く。
- **user-invoked** な skill は agent の手が届く範囲から description を取り除く: 名前をタイプするあなただけがそれを起動でき、他の skill からは起動できない。context load はゼロになるが、代わりに **cognitive load** を消費する: それが存在することを覚えておかなければならない index は _あなた自身_ である。仕組み: `disable-model-invocation: true` を設定する。`description` は人間向けのもの — 一行の要約になり、trigger の列挙は取り除かれる。

model-invocation を選ぶのは、agent 自身がその skill に到達しなければならない場合、あるいは他の skill が到達しなければならない場合だけにする。手動でしか発火しないのであれば user-invoked にして context load を払わない。

user-invoked な skill が覚えきれないほど増えてきたら、積み重なった cognitive load は **router skill** で解消する: 他の skill の名前と、それぞれをいつ使うべきかを挙げる、単一の user-invoked skill である。

## Writing the description

model-invoked な **description** は 2 つの仕事をする — その skill が何であるかを述べることと、それを trigger すべき **branch** を列挙することである。一語ごとに **context load** が増えるため、description は本文以上に厳しい pruning に値する:

- **skill の leading word を先頭に置く** — description は invocation の仕事をする場所である。
- **1 branch につき 1 trigger。** 単一の branch を言い換えただけの同義語は **duplication** である — "build features using TDD … asks for test-first development" は同じ 1 つの branch を二度書いているにすぎない。それらは畳み込み、本当に別個の branch だけを残す。
- **本文に既にある identity は削る。** description には trigger と、「他の skill が必要とするとき…」という reach 節だけを残す。

## Information hierarchy

skill は 2 種類のコンテンツ — **steps** と **reference** — から組み立てられ、これらは自由に混ざり合う: skill はすべて steps でも、すべて reference でも、その両方でもよい。核心となる意思決定は、どちらを使うか、そしてそれぞれを **information hierarchy**（agent がその材料をどれだけ即座に必要とするかで並べた梯子）のどこに置くかである:

1. **In-skill step** — `SKILL.md` 内にある順序立った行動であり、最上位の tier: agent が順番に行うことそのもの。各 step は **completion criterion**（作業が完了したことを agent に伝える条件）で終わる。それを _checkable_ にし（agent は完了と未完了を見分けられるか？）、重要な場面では _exhaustive_ にする（"produce a change list" ではなく "every modified model accounted for"）— 曖昧な criterion は **premature completion** を招く。
2. **In-skill reference** — `SKILL.md` 内にある定義・ルール・事実であり、必要に応じて参照される。しばしば正当にフラットな peer-set である（レビューのすべてのルールが一段に並ぶなど）— これは smell ではなく、適切な配置である。 _この skill はすべて reference である。_
3. **External reference** — `SKILL.md` の外に押し出され、別ファイルに置かれた reference で、**context pointer** を通じて到達し、そのポインタが発火したときだけ読み込まれる。（`GLOSSARY.md` のような、skill の一部でありながら _disclosed_ な reference の sibling ファイルから、skill システムの外側にあり任意の skill が指せる完全な **external reference** まで幅がある。）

要求の厳しい completion criterion は、徹底的な **legwork** — agent が作業の中で行う掘り下げ — を促す。skill に steps があってもなくても同じで、"every rule applied" がフラットな reference を縛るのは、"every step done" が sequence を縛るのと同じことである。

下に押し出す量が少なすぎれば上部が膨張し、多すぎれば agent が実際に必要とする材料を隠してしまう。この緊張関係こそが、意思決定のすべてである。

**Progressive disclosure** とは、梯子を下に降りる動き — `SKILL.md` の外にある、リンクされたファイルへ移すこと — であり、これによって上部の可読性が保たれる。仕組み: skill フォルダ内にリンクされた `.md` ファイルで、中身にちなんだ名前を付ける（この skill は完全な定義を `GLOSSARY.md` に disclose している）。skill によっては複数の使われ方をするものがあり、それぞれ異なる使われ方が **branch** である — 異なる実行が skill の中で異なる経路を辿る。branch は disclosure の最も明快なテストである: すべての branch が必要とするものは inline にし、一部の branch だけが到達するものはポインタの背後に押し出す。agent がいつ、どれだけ確実にその材料に到達するかを決めるのは **context pointer** の _target_ ではなく _wording_ である。

梯子がある一片が _どれだけ下に_ 位置するかを決めるのに対し、**co-location** はそこに一度置かれた後 _何がその隣に座るか_ を決める: ある概念の定義・ルール・注意点を、散らばらせず一つの見出しの下にまとめておくことで、一部を読めばその隣接部分も一緒についてくるようにする。

## When to split

**Granularity** とは skill をどれだけ細かく分割するかであり、切り分けるたびに 2 つの load のどちらかを消費する。したがって分割は、それに見合うだけの価値があるときだけ行う。2 種類の切り分け方がある:

- **By invocation** — それ単体を trigger すべき別個の **leading word** があるとき、あるいは他の skill がそれに到達しなければならないときに、**model-invoked** な skill を切り出す。常に読み込まれる新しい **description** の分だけ **context load** を払うことになるため、その独立した到達性が見合うものでなければならない。
- **By sequence** — この先に残っている steps（ある step の **post-completion steps**）が agent に目の前の step を急がせる誘惑となる（**premature completion**）ときに、一連の **steps** を分割する。それらを視界の外に置くことで、agent は目の前のタスクにより多くの **legwork** を行うようになる。

## Pruning

それぞれの意味を **single source of truth** として保つ: 権威ある場所を一つにすることで、振る舞いの変更が一箇所の編集で済むようにする。

すべての行について **relevance** を確認する: それは今もその skill の振る舞いに関わっているか？

次に、行単位だけでなく文単位で **no-ops** を狩る: 各文を単独で no-op テストにかけ、失敗したら単語を削るのではなく文全体を削除する。積極的に行う — テストに落ちた文章のほとんどは、書き直すのではなく削除すべきである。

## Leading words

**leading word** とは、model の pretraining の中に既に存在しているコンパクトな概念であり、agent が skill を実行する間それを使って考える（例: _lesson_、_fog of war_、_tracer bullets_）。テキスト全体で繰り返される（ただし必ずしもそうとは限らない — 強い leading word は一度だけの登場で済むこともある）ことで、分散した定義を積み上げ、model が既に持っている prior を呼び起こすことで、最小のトークン数で振る舞いのある領域全体を anchor する。

これは predictability に二重に貢献する。本文の中では _execution_ を anchor する: その語が現れるたびに agent は同じ振る舞いに手を伸ばす。description の中では _invocation_ を anchor する: 同じ語が prompt・doc・code に息づいているとき、agent はその共有された言語を skill に結びつけ、より確実に発火させる。

skill を leading word を使うようリファクタリングする機会を探す。3 箇所で綴られた triad（**duplication**）や、一つのアイデアを示すために一文を費やす description — そのどちらも、単一のトークンへ **collapse** されることを求めている一節である。例:

- "fast, deterministic, low-overhead" -> _tight_ — 一つの phase にわたって繰り返し述べられていた一つの性質を、一つの pretrained word（_tight_ loop）にまとめる。
- "a loop you believe in" -> _red_ — 曖昧な gate を、二値で観測可能な状態に変換する（loop はそのバグで _red_ になるか、ならないかのどちらかである）。

こうすることで二重に得をする: トークン数が減り、_かつ_ agent が思考を掛けるためのより鋭い hook が手に入る。すべての skill には leading word に置き換えられる繰り返しの言い回しが潜んでいると想定し、それらを探し出す。

## Failure modes

これらを使って、ユーザーが skill に関して抱えている可能性のある問題を診断する。

- **Premature completion** — 本当に完了する前に step を終わらせてしまうこと。注意が _完了しているという状態_ の方へ滑ってしまう。防御策は順番に: まず completion criterion を研ぎ澄ます（安価で局所的）。それがどうしても曖昧なままで、_かつ_ 実際に急いでしまう様子が観察された場合に限り、分割（sequence の切り分け）によって post-completion steps を隠す。
- **Duplication** — 同じ意味が複数の場所にあること。メンテナンスとトークンのコストがかかり、その意味の梯子上の目立ち度を本来の順位以上に膨らませてしまう。
- **Sediment** — 追加は安全に感じられ、削除はリスキーに感じられるために積もっていく古い層。pruning の規律を持たないあらゆる skill が辿るデフォルトの運命である。
- **Sprawl** — すべての行が生きていて重複がなくても、skill が単に長すぎること。可読性と保守性を損ない、トークンを無駄にする。治療法は梯子である: **reference** をポインタの背後に disclose し、**branch** または sequence によって分割し、各経路が必要なものだけを運ぶようにする。
- **No-op** — model がデフォルトで既に従っている行であり、何も言っていないのに load を払っている状態。テスト: それはデフォルトと比べて振る舞いを変えるか？ 弱い leading word（agent が既にある程度 thorough であるときの _be thorough_）は no-op である。直すべきは異なる技法ではなく、より強い語（_relentless_）である。

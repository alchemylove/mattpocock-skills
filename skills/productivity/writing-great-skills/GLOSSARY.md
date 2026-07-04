# Glossary — Building Great Skills

優れた skill を作るための domain model。skill は stochastic なシステムから determinism を絞り出すために存在する。根本的な美徳は **Predictability** であり、以下のすべての用語はそこに働きかけるレバーである。これは [`writing-great-skills`](SKILL.md) の disclosed reference である。

用語は軸ごとにグループ化されている: **Invocation**（skill がどう到達されるか）、**Information Hierarchy**（その内容がどう配置されるか）、**Steering**（agent の実行時の振る舞いがどう形作られるか）、そして **Pruning**（どう lean に保たれるか）。それぞれの **failure mode** は、それを治すレバーのそばに置かれ、_failure mode_ とタグ付けされている。

定義文中の **太字の用語** はいずれもこの glossary 内で定義されている。見出しから探すこと。

## Predictability

skill が、毎回同じ _やり方_ — 同じ output ではなく同じ process — で agent を振る舞わせる度合い（brainstorming の skill は _予測可能に_ 発散するべきである。トークンは変わっても、振る舞いは変わらない）。他のすべての用語が仕えている根本的な美徳であり、コストや保守性はそれと競合するものではなく、その症状にすぎない。

_Avoid_: consistency, reliability, robustness, output-determinism

## Invocation

skill がどう到達されるか — そして、その選択に対して支払う 2 種類の load。

### Model-Invoked

**description** フィールドを保持している skill で、agent がそれを見て自律的に発火できる — 人間も引き続きその名前をタイプできるため、model-invocation は常に user reach を _含む_。model のみの状態というものは存在しない: description は agent の発見可能性を _追加する_ だけであり、人間の到達可能性を取り除くことは決してない。その発見可能性と引き換えに、毎ターン恒久的な **context load** を支払う。他の skill から到達可能である。なぜなら agent が発見できるようにする description は、それを invocable にもするからである。中身がすべて **reference** である model-invoked な skill は、共有 reference の置き場所にもなる: 他の skill がそれを invoke できるため、複数の skill が必要とする reference を一箇所に置ける。model-invocation を選ぶのは、agent がその skill に自力で到達しなければならない場合だけにする。手動でしか発火しないのであれば、description を外して context load を払わない。

_Avoid_: ability, tool, capability

### User-Invoked

**description** が取り除かれた skill — agent からは見えず、名前をタイプする人間だけが到達できる（**model-invoked** が user _かつ_ agent であるのに対し、user _のみ_）。agent からの発見可能性を、ゼロの **context load** と引き換えにする。description がないため、人間以外は誰も到達できない: 他のどの skill もそれを発火させられない。

_Avoid_: procedure, workflow, command

### Description

skill の機械可読な trigger であり、**model-invoked** な skill が常時読み込んでおくことを強いられる唯一の **context pointer** である。それが存在すること自体が invocation の軸そのものである: 保持すれば skill は model-invoked になり（他の skill からも到達可能になり）、削除すれば skill は **user-invoked** になり、人間だけが到達できるようになる。model-invoked な skill の **context load** の発生源である。

_Avoid_: frontmatter, summary

### Context Pointer

agent の context の中に保持される参照であり、context の外にある何らかの材料を名指しし、そこへ到達するための条件を符号化している。**description** はトップレベルの context pointer である（context window → skill）。disclose されたファイルへのポインタは、一段下にある同じものである。agent が _いつ_、_どれだけ確実に_ 到達するかを決めるのは target ではなく wording である。弱い wording のポインタの背後にある must-have な target は variance のバグである: まず wording を直し、それでも直らない場合にのみ材料を inline にする。

_Avoid_: link, reference, import

### Context Load

**model-invoked** な skill が agent の context window に課すコスト — 常に読み込まれているその **description** が、トークンと attention の両方を消費する。**user-invoked** な skill が description を持たないことで免れているものであり、model-invoked な skill をさらに分割することへのブレーキでもある。

_Avoid_: token cost, context bloat

### Cognitive Load

**user-invoked** な skill が人間に課すコスト — どの skill が存在し、それぞれをいつ使うべきかを頭の中に保持しておかなければならないという負担（人間が index になる）。**model-invocation** は agent が発見可能であることによってこれを取り除き、また user-invoked な skill をさらに分割することへのブレーキでもある。最小化すべきコストではない: それは human agency の対価であり、一部の skill が user-invoked のままである理由である。人間の判断が重要な場面ではこれを費やし、そうでない場面では取り除く。

_Avoid_: human index, burden, overhead

### Router Skill

他の user-invoked な skill を指し示すことを仕事とする **user-invoked** な skill — それぞれの名前と、いつ使うべきかを挙げる — これにより人間は多くの skill ではなく一つの skill だけを覚えておけばよくなる。ヒントを示すことしかできず、それらを発火させることはできない: user-invoked な skill には **description** がないため、人間以外は誰も到達できないからである。user-invoked な skill が増えたときの **cognitive load** に対する治療法である。

_Avoid_: dispatcher, menu, registry, index, router procedure

### Granularity

skill をどれだけ細かく分割するか。より細かい分割は 2 つの load のどちらかを消費する: より多くの **model-invoked** な skill は **context load** を消費し（window に description が増え、attention を奪い合う）、より多くの **user-invoked** な skill は **cognitive load** を消費する（人間が覚えて使う対象が増える）。分割は 2 種類の切り分けに導かれる。**invocation** による切り分けでは、それを trigger する明確な **leading word** — 実際に自分の prompt の中で使う trigger word — があるところで model-invoked な skill を切り出す。**sequence** による切り分けでは、ある step の **post-completion steps** を隠す必要があるところで一連の **steps** を分割する。それを独立した context に切り離すことで、後に続くものが見えなくなるからである。逆方向には注意する: sequence を統合すると、各 step の post-completion steps がその後に続くものにさらされ、premature completion を招く。

_Avoid_: chunking, modularity

## Information Hierarchy

skill の内容がどう配置されるか、そしてそれぞれの断片が梯子のどれだけ下に位置するか。

### Information Hierarchy

agent がそれをどれだけ即座に必要とするかによって順位付けされた skill の内容 — in-file かポインタの背後か、step か reference かという 2 つの切り口から生まれる、単一の梯子である。段は次の通り:

- **Steps** — in-file、最上位
- **Reference**（in-file）— 二次的
- **Reference**（disclosed）— **context pointer** の背後

**steps** を持たない skill は下の 2 段だけを使う — しばしば正当にフラットな peer-set である（例えばレビューのすべてのルールが一段に並ぶ）。これは smell ではなく、適切な配置である。hierarchy は invocation とは独立している: skill はすべて steps でも、すべて reference でも、その両方でも、model-invoked にも user-invoked にもなり得る。skill が steps を持つ場合、disclose すべき in-file な reference はそれらを埋もれさせ、それに注意を払うかどうかをコイントスにしてしまう — これは legibility だけでなく variance のレバーでもある。梯子の最上部は legible に保ち、押し出せるものはできる限り下へ押し出す。

_Avoid_: structure, organization, layout

### Steps

agent が実行する順序立った行動 — skill がそれを持つ場合、内容の最上位 tier であり、SKILL.md にその居場所を得る部分である。すべての skill が steps を持つわけではない: skill はすべて steps（`tdd`）でも、すべて **reference**（レビュー）でも、その両方でもよく、これは invocation とは独立している。すべての step は **completion criterion** で終わる。明確であれ曖昧であれ。

_Avoid_: workflow, instructions, choreography

### Reference

agent が必要に応じて参照する材料 — 定義、事実、パラメータ、例、条件付きの指示。skill が **steps** を持つ場合はそれに対して二次的であり、持たない場合はそれが内容のすべてである。あるいは、いかなる skill の外にも存在しうる — **External Reference** を参照。**context pointer** を介して到達し、**progressive disclosure** の主要な候補である。

_Avoid_: supporting material, docs, background

### External Reference

skill システムの外に存在する **Reference** — description も steps もない、invocable でもない、ただのファイルであり、任意の skill がそれを指すことができる。それ自体が発火する必要のない共有 reference の置き場所であり、2 つの **user-invoked** な skill が使える唯一の共有の置き場所である。どちらも description を持たないため、互いを発火させることができないからである。

_Avoid_: doc, resource, knowledge base

### Progressive Disclosure

**reference** を梯子の下へ動かすこと — SKILL.md の外に出し、**context pointer** の背後に置くことで、上部の可読性を保つ。主にトークンの最適化ではなく、**information hierarchy** をどう守るかという話である。**branching** によって許可される: 一部の branch だけが必要とするものを disclose し、すべての経路が必要とするものは inline にする。must-have な材料に対してポインタの発火が不確実な場合は、その wording を研ぎ澄まし、それでも失敗する場合にのみ inline に戻す。

_Avoid_: lazy loading, chunking

### Co-location

agent が一度に必要とする材料を一箇所にまとめておくこと — ある概念の定義・ルール・注意点を、ファイル中に散らばらせず一つの見出しの下に置き、一部を読めばその隣接部分も一緒についてくるようにする。**Information Hierarchy** に対する、ファイル内での対になる存在である: hierarchy はある断片が _どれだけ下に_ 位置するかを順位付けし、co-location はそこに一度置かれた後 _何がその隣に座るか_ を決める。**reference** のまとまりの正しいフォーマットに公式はない。テストは、skill が agent 向けに書かれた documentation のように読めるかどうかであり、グループ化された材料はそう読めるが、散らばった材料はそう読めない。**Duplication** とは異なる: duplication は一つの意味を二箇所で繰り返すことであり、散らばりは一つの意味を多くの場所へ断片化することである。

_Avoid_: grouping, clustering, cohesion

### Sprawl

_Failure mode。_ 単に長すぎる skill — SKILL.md の行数が多すぎる — であり、それが stale であるか repeated であるかとは無関係である。すべてが live で unique な skill でも sprawl は起こり得る。可読性（agent が行動に移る前により多くをかき分けなければならず、attention が余剰部分に薄まる）、保守性（余分な行が増えるほど **relevant** に保つべき行も増える）、トークンのコストがかかる。治療法は **information hierarchy** である: **reference** を **context pointer** の背後へ押し出し、**branch** やシーケンスによって分割し、各経路が必要なものだけを運ぶようにする。**sediment**（古い蓄積による長さ）や **duplication**（繰り返された意味による長さ）とは異なる — sprawl はその原因が何であれ、長さそのものである。

_Avoid_: bloat, length, size, verbosity

## Steering

agent の実行時の振る舞いを **Predictability** に向けて形作るレバー群。

### Branch

skill が invoke されうる別個の方法 — skill が扱うケース — であり、異なる実行はそれを通る異なる経路を辿る。多くの steps を持つ skill は多くの branch を持ちうる。線形な skill には branch がない。

_Avoid_: path, case, fork

### Leading Word

コンパクトな概念 — _Leitwort_ とも呼ばれる — であり、既に model の pretraining の中に存在していて、agent が skill を実行する間それを使って考える。model が既に持っている prior を呼び起こすことで、できる限り少ないトークン数で振る舞いの原則を符号化する（例: _lesson_、_proximal zone of development_、_fog of war_、_tracer bullets_）。文としてではなくトークンとして繰り返されることで、skill 全体にわたって分散した定義を積み上げ、振る舞いのある領域全体を anchor する。明確に定義すれば自作の語も機能するが、作られた語は prior を呼び起こさない — pretrained な語がタダで与えてくれるものを、定義のトークンで支払うことになる。まずは既存の語に手を伸ばす。

leading word は **predictability** に二重に貢献する。本文の中では **execution** を anchor する: その概念が現れるたびに agent は同じ振る舞いに手を伸ばし、フラットな reference の中では探すべき事物のクラスに attention を集中させ、実行のたびに正しいチェックを呼び起こす。**description** の中では **invocation** を anchor する — しかも skill の中だけではない: 同じ語が prompt・doc・codebase に息づいているとき、agent はその共有された言語を skill に結びつけ、より確実に発火させる。その skill を使いたいときに実際に使う leading word で description を書く。

_Avoid_: keyword, term, motif

### Completion Criterion

一つの作業単位が完了したことを agent に伝える条件 — agent がそれと照らし合わせて判断する target である。これをただの quality ではなくレバーにしているのは 2 つの性質である。その **clarity**（agent は完了と未完了を見分けられるか？）は **premature completion** に抵抗する — 曖昧な境界（"understanding reached"）は agent に完了を宣言させ、次の step へ滑り込ませてしまう。premature completion は steps 間の失敗であるため、この軸が効くには _steps_ が必要である。その **demand**（どれだけを要求するか）は **legwork** を定める — "produce a change list" とは違い、"every modified model accounted for" は徹底した作業を強いる — そしてこの軸は step に縛られない: フラットな reference のまとまりをも縛りうる。これが、steps を持たない skill でも exhaustiveness の基準（"every rule applied"）を持ち続けられる理由である。最も強力な criterion は checkable かつ exhaustive の両方を満たす。

_Avoid_: done condition, exit condition, stopping rule

### Legwork

agent が単一の step の中で舞台裏で行う作業 — ファイルを読み、コードベースを探索し、変更を加え、ユーザーに丸投げするのではなく必要なものを自ら掘り出すこと。step の構造の下に存在する: それ自体が独立した step として書かれることはなく、wording の中に潜んでおり、skill ではなく agent によって制御される。**post-completion steps** の step をまたぐ引力に対する、step 内での対になる存在である。**leading word**（_comprehensive_、_thorough_）や、作業を exhaustive にすることを要求する **completion criterion** — フラットな reference に適用される demand の軸も含む。これが、フラットな reference からなる skill にすべての段を網羅させる原動力である — によって高められる。その demand が欠けているとき、あるいは **premature completion** が step を途中で打ち切ってしまうときに薄くなる。

_Avoid_: scope, effort, diligence, coverage

### Post-Completion Steps

現在の step の後に続く **steps**。可視であることで、agent を **premature completion** へと引っ張る — 見えれば見えるほど、その引力は強くなる。防御策は、steps の sequence を二つに分割することでそれらを隠すことである。

_Avoid_: horizon, fog of war, lookahead

### Premature Completion

_Failure mode。_ agent の attention が作業そのものではなく完了しているという状態の方へ滑ってしまうために、現在の step が本当に完了する前に終わらせてしまうこと。steps 間の失敗である: 発生するには **steps** が必要であり、steps を持たない skill が早々に切り上げるのは premature completion ではなく、満たされない demand の下での薄い **legwork** である。2 つの力の綱引きである: 可視の **post-completion steps**（前へ引っ張る力）と **completion criterion** の clarity（抵抗する力 — 鋭く checkable な基準は持ちこたえ、曖昧なものは屈する）。曖昧さが必要条件である: 鋭い境界は、後にどれだけ多くの step が見えていても引力に抵抗するため、決して急がない step には防御が要らない。急いでしまう step を守るレバーは 2 つあるが、順番に手を伸ばす: **まず境界を研ぎ澄ます** — これは局所的で安価である。criterion がどうしても曖昧なままで、_かつ_ 実際に急いでしまう様子が観察された場合にのみ、**後の steps を隠す** — そして隠すことが機能するのは本物の context の境界を越える場合だけである（user-invoked な hand-off や subagent への dispatch。inline の model-invoked な呼び出しは後の steps を context に残したままにし、何も片付けない）。thin な legwork の原因の一つではあるが、それとは異なる: legwork は、step が完全に完了まで実行されても薄くなりうる。

_Avoid_: premature closure, the rush, rushing, shortcutting

## Pruning

skill を lean に保つこと — それぞれの治療法は、それが治す failure と対になっている。

### Single Source of Truth

それぞれの意味がちょうど一つの権威ある場所に存在し、skill の振る舞いの変更が一箇所の変更で済むという望ましい状態。**Duplication** はその違反である。

_Avoid_: home, canonical location

### Duplication

_Failure mode。_ 同じ意味に複数の **single source of truth** が与えられている状態。メンテナンスのコストがかかり（一箇所を変えたら他も変えなければならない）、トークンのコストもかかり、目立ち度を膨らませる — ある意味を繰り返すことで、それを梯子の上で本来の順位以上に重み付けしてしまう。**leading word** の偶発的な裏返しであり、leading word は意味ではなくトークンを繰り返すことで意図的に attention を高める。

_Avoid_: repetition, redundancy

### Relevance

ある行が今もその skill の振る舞いに関わっているかどうか — 何を残すべきかを見極めるレンズ。行が relevance を失うのは、そもそもタスクに関わったことがない場合（単なる説明文、あるいは disclose すべき **branch**）か、あるいは stale になっていく場合（それが描写する振る舞いや世界が変化するにつれて時代遅れになっていく）のいずれかである。短い skill ほど relevant に保ちやすい。各行を確認するコストが安いからである。**No-op** とは異なる: relevance はある行がタスクに関わっているかどうかを問い、振る舞いを変えるかどうかは問わない。

_Avoid_: load-bearing, staleness, freshness

### Sediment

_Failure mode。_ 追加は安全に感じられ、削除はリスキーに感じられるために、skill の中に積もって決して片付けられない古いコンテンツの層 — stale で irrelevant な行が蓄積し、今も生きているものを見つけるにはそれらを掘り下げなければならない。pruning の規律を持たないあらゆる skill が辿るデフォルトの運命であり、**duplication** の繰り返された意味とは対照的な、**relevance** のゆっくりとした侵食である。

_Avoid_: accretion, bloat, cruft, rot

### No-Op

_Failure mode。_ model がデフォルトで既に行っているために何も変えない指示 — agent にどうせやることを伝えるために load を払っている状態。テスト: その行はデフォルトと比べて振る舞いを変えるか？ ある行は完全に **relevant** でありながら、それでも no-op でありうる。**leading word** をタダにしているのと同じ prior が、no-op を無価値にしている。

leading word は _技法_ であり、No-Op はある行に対する _判定_ である — そして両者は交差する。デフォルトに勝てないほど弱い leading word は no-op である（agent が既にある程度 thorough であるときの _be thorough_）。直すべきは、異なる技法ではなく、判定に合格するより強い語（_relentless_）である。したがって No-Op テスト — それはデフォルトと比べて振る舞いを変えるか？ — は、leading word がその繰り返しに見合っているかどうかを評価する方法でもある。これは reader-relative ではなく model-relative である: ある行が no-op かどうかで 2 人の意見が分かれるとき、それはデフォルトについて意見が分かれているのであり、議論ではなく skill を実行することで決着させる。

_Avoid_: redundant instruction, restating the obvious, belaboring

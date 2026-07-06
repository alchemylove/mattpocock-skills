---
name: wayfinder
description: 一つの agent セッションでは収まらない巨大な作業のかたまりを、issue tracker 上の調査 ticket からなる共有 map として計画し、destination への道筋がはっきりするまで一つずつ解決していく。
---

漠然としたアイデアが到着した — 一つの agent セッションには大きすぎ、fog に包まれている: ここから **destination** までの道筋がまだ見えない。Wayfinding とは、その道を見つけることであり、destination へ一直線に向かうことではない。この skill はその道筋を repo の issue tracker 上の **共有 map** としてチャート化し、route がはっきりするまでその ticket を一つずつ処理していく。

destination は取り組みごとに異なり、それに名前を付けることがチャート化の最初の行為である — それがすべての ticket の形を決める。引き渡して iterate していく spec のこともあれば、planning が始まる前に固定しておくべき決定のこともあり、data-structure migration のようにその場で行う変更のこともある。この map は domain に依存しない — engineering work、course content、形に合うものなら何でもよい。

## 名前で参照する (Refer by name)

すべての map と ticket は issue なので、**name** — そのタイトル — を持つ。人間が読むものすべて — narration、map の Decisions-so-far — において、それを裸の id、番号、slug ではなく、その name で参照する。`#42, #43, #44` の羅列は読みにくい; name は一目で読める。id と URL が消えるわけではない — name はその link を包む — が、それらは name の *内側* に乗るのであり、name の代わりにはならない。

## Map

Map は、この repo の issue tracker 上の単一の issue であり、`wayfinder:map` というラベルが付く — canonical artifact である。その ticket は map の child issue である。

Map は **index** であり、store ではない。下された決定を列挙し、その詳細を保持する ticket を指し示す; 決定はちょうど一箇所 — その ticket — にのみ存在するので、map はそれを再掲することは決してなく、要約と link のみを行う。

**map、その child ticket、blocking、frontier query が物理的にどこに存在するかは tracker 固有である。** _この_ repo がそれらをどう表現するかは `docs/agents/issue-tracker.md` (「Wayfinding operations」セクション) を参照する。そのドキュメントが存在しない場合は、ローカルの markdown tracker をデフォルトとする。

### Map の本文 (The map body)

Map 全体を低解像度で表したもので、セッションごとに一度だけ読み込む。open な ticket は **列挙しない** — それらは query で見つかる open な child issue である。

```markdown
## Destination

<what reaching the end of this map looks like — the spec, decision, or change this effort is finding its way to. One or two lines; every session orients to it before choosing a ticket.>

## Notes

<domain; skills every session should consult; standing preferences for this effort>

## Decisions so far

<!-- the index — one line per closed ticket: enough to judge relevance, then zoom the link for the detail the ticket holds -->

- [<closed ticket title>](link) — <one-line gist of the answer>

## Not yet specified

<!-- see "Fog of war": in-scope fog you can't ticket yet; graduates as the frontier advances -->

## Out of scope

<!-- see "Out of scope": work ruled beyond the destination; closed, never graduates -->
```

### Ticket

各 ticket は map の **child issue** であり、tracker の issue id がその identity である。その本文は question であり、一つの 100K token agent セッションに収まるサイズにする:

```markdown
## Question

<the decision or investigation this ticket resolves>
```

各 ticket には `wayfinder:<type>` ラベルが付く — `research`、`prototype`、`grilling`、`task` のいずれか ([Ticket Types](#ticket-types) を参照)。

セッションは、作業を始める **前** に map を進めている dev に assign することで ticket を **claim** する — こうすることで並行セッションがそれをスキップできる。その assignee 自体が claim である: open で unassigned な ticket は unclaimed である。

Blocking には tracker の **native** な dependency relationship を使う — これは tracker 自身の UI で frontier を _視覚的に_ 描画するために不可欠であり、人間は map を開かなくても何が着手可能かを見られる。native な blocking を持たない tracker のみ、本文での慣例にフォールバックする。ticket をブロックしているすべての ticket が close されたとき、その ticket は **unblocked** である; **frontier** とは open で unblocked かつ unclaimed な child のことであり、既知の領域の縁である。

答えは本文の一部ではない — 解決時に記録される ([Work through the map](#work-through-the-map) を参照)。ticket の解決中に作成されたアセットは issue から link され、貼り付けられることはない。

## Ticket の種類 (Ticket Types)

- **Research**: ドキュメント、third-party API、または knowledge base のようなローカルリソースを読むこと。markdown の summary を linked asset として作成する。現在の working directory 外の知識が必要なときに使う。
- **Prototype**: 安価で粗く具体的な artifact — outline、rough take、stub、または /prototype skill 経由の UI/logic code — を作って議論の fidelity を上げる。prototype を asset として link する。「どう見えるべきか」「どう振る舞うべきか」が鍵となる question のときに使う。
- **Grilling**: agent との会話。/grilling と /domain-modeling skill を使う。一度に一つの question を尋ねる。デフォルトのケース。
- **Task**: 議論を先に進める前に済ませなければならない、文字通りの手作業 — 決めること、prototype すること、research することは何もない。データの移動、サービスへのサインアップ、アクセスの provisioning。agent は可能な範囲でそれを自動化し、できなければ人間に正確なチェックリストを渡す。作業が終わったときに解決とみなす; 答えには何が行われたか、そして後続の ticket が依存する結果としての事実 (認証情報の場所、新しい URL、行数) を記録する。

## Fog of war

Map は _意図的に_ 不完全である: まだ見えていないものをチャート化してはならない。生きている ticket の先には **fog of war** が広がる — 来ることは分かるがまだ確定できない決定や調査についての、ぼんやりとした眺めであり、まだ open な question に依存しているために起こる。ticket を解決すると、その先の fog が晴れ、今や specify 可能になったものが新しい ticket へと昇格する — 一度に一つずつ、destination への道筋がはっきりし、ticket が残らなくなるまで。

Map の **Not yet specified** セクションは、そのぼんやりとした眺めを書き留める場所である: 疑われる question、後で見直すべき領域。これは destination に _向かう_ 未発見の frontier である — ここにあるものはすべて in scope だが、まだ ticket にできるほど鋭くないだけだ。眺めが許す限り緩くも詳細にも書いてよい; これは、この取り組みがどこに向かっているかを読む共同作業者にとっての道標も兼ねる。

**Fog か ticket か?** 判定基準は、その question を _今_ 正確に述べられるかどうかであり — 今それに答えられるかどうか _ではない_。

- **Ticket にするのは** question がすでに鋭いとき — たとえそれが blocked でまだ着手できなくても。
- **Not yet specified にするのは** まだそこまで鋭く言い表せないとき。fog を ticket サイズにあらかじめ細切れにしない: fog は ticket より粗く、一つの patch が frontier に達したときに複数の ticket に昇格することもあれば、何も生まれないこともある。

**Not yet specified** は、すでに決定されたもの (Decisions so far)、すでに生きている ticket になっているもの、そして out of scope なもの (次のセクション) を除外する。

## Out of scope

Fog は常に destination に _向かって_ のみ集まる。destination が scope を定めるので、それを超えた作業は **out of scope** である — それは fog ではなく、**Not yet specified** にも属さない。それは map 上に専用の **Out of scope** セクションを持つ: _この_ 取り組みから意識的に除外した作業である。ここに置かれるかどうかを決めるのは sharpness ではなく scope である。

Out-of-scope な作業は決して昇格しない — frontier は destination で止まる — そのため、それが戻ってくるのは destination が引き直されたときだけであり、そのときは resumption ではなく新しい取り組みとしてである。

何かを out of scope と判定することは scoping の行為であり、route 上の一歩ではない。すでに存在する ticket が destination を超えた場所にあると判明した場合 — チャート化の時点で scope を見誤っていた、または解決によって明らかになった — その ticket を **close する** (close された ticket は frontier から外れていることが明確である) とともに、**Out of scope** セクションに一行残す: gist と、なぜそれが out of scope なのかを、close した ticket への link とともに。それは実際に歩んだ route を記録する **Decisions so far** には含まれない — scope の境界は route 上の一歩ではないからである。

## 呼び出し (Invocation)

2 つのモードがある。どちらの場合も **一つのセッションで複数の ticket を解決してはならない。**

### Map をチャート化する (Chart the map)

ユーザーが漠然としたアイデアで呼び出す。

1. **destination に名前を付ける。** `/grilling` と `/domain-modeling` セッションを実行し、この map が向かっている先 — spec、決定、あるいは変更 — を突き止める。destination が scope を定めるので、これを最初に確定する。
2. **frontier を map する。** 再び grill するが、今度は **breadth-first** で行う: 一つの thread を深掘りするのではなく空間全体に fan out し、open な決定と今すぐ着手できる最初の一歩を洗い出す。
3. **Map を作成する** (ラベル `wayfinder:map`): Destination と Notes を埋め、Decisions-so-far は空のまま、fog を **Not yet specified** にスケッチする。
4. **今 specify できる ticket を作成する** map の child issue として — その後 **第二段階** で blocking edge を配線する (issue は互いを参照する前に id を必要とする)。配線によって frontier と blocked に振り分けられる; まだ specify できないものはすべて fog — **Not yet specified** セクション — に留まる。
5. 止まる — map をチャート化するのは一つのセッションの仕事であり、ticket の解決を同時に行ってはならない。

### Map を進める (Work through the map)

ユーザーが map (URL または番号) で呼び出す。ticket は **省略可能** — 指定がなければ、次の決定を選ぶのはユーザーではなくあなたである。

1. **map** を読み込む — 低解像度のビューであり、すべての ticket 本文ではない。
2. ticket を選ぶ。ユーザーが一つ指定していればそれを使う。そうでなければ frontier の先頭の ticket を順に取る。**claim する**: 作業前に自分自身に assign する。
3. それを解決する — **必要に応じてズームする**: 関連する、または close された ticket の完全な本文をオンデマンドで取得する; `## Notes` ブロックに名前のある skill を呼び出す。迷ったら `/grilling` と `/domain-modeling` を使う。
4. 解決を記録する: **resolution comment** として答えを投稿し、issue を **close** し、map の Decisions-so-far に **context pointer を追記** する。
5. 新たに浮上した ticket を追加する (create してから wire する); 答えによって specify 可能になった fog を昇格させ、昇格した各 patch を **Not yet specified** から消して、それが新しい ticket としてのみ存在するようにする。答えによって、ある ticket — この ticket か別の ticket か — が destination を超えていることが判明した場合、それを route 上で解決するのではなく **out of scope と判定する**。決定が map の他の部分を無効にする場合は、それらの ticket を更新または削除する。

ユーザーは unblocked な ticket を並行して実行することがあるので、他のセッションが同時に tracker を編集していることを想定する。

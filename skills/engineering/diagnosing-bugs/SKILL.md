---
name: diagnosing-bugs
description: 難しいバグやパフォーマンス低下のための診断ループ。ユーザーが「diagnose」「debug this」と言った、または何かが壊れている/例外を投げている/失敗している/遅いと報告したときに使う。
---

# Diagnosing Bugs

難しいバグのための discipline。phase を飛ばすのは明示的に正当化できるときだけ。

codebase を探索する際は、`CONTEXT.md`（存在すれば）を読んで関連 module の明確な mental model を得て、触れる領域の ADR を確認する。

## Phase 1 — feedback loop を構築する

**これが本質である。** それ以外はすべて機械的な作業だ。バグに対する **tight** な pass/fail signal — *この*バグで red になるもの — があれば、原因は見つかる。bisection、hypothesis-testing、instrumentation はすべてそれを消費するだけである。それが無ければ、どれだけコードを見つめても救われない。

ここに不釣り合いなほどの労力をかける。**攻撃的であれ。創造的であれ。諦めることを拒め。**

### 構築する方法 — おおよそこの順で試す

1. バグに届く seam での **failing test** — unit、integration、e2e。
2. 稼働中の dev server に対する **Curl / HTTP script**。
3. fixture input を使い、stdout を known-good な snapshot と diff する **CLI invocation**。
4. **Headless browser script**（Playwright / Puppeteer）— UI を操作し、DOM/console/network を assert する。
5. **キャプチャした trace を再生する。** 実際の network request / payload / event log をディスクに保存し、code path 単体で再生する。
6. **使い捨ての harness。** システムの最小限のサブセット（1 つの service、mocked な依存）を立ち上げ、単一の関数呼び出しでバグの code path を動かす。
7. **Property / fuzz loop。** バグが「時々おかしい出力」であるなら、1000 個のランダムな入力を実行し failure mode を探す。
8. **Bisection harness。** バグが 2 つの既知の状態（commit、dataset、version）の間に現れたなら、"状態 X で起動し、確認し、繰り返す" を自動化して `git bisect run` できるようにする。
9. **Differential loop。** 同じ入力を旧バージョンと新バージョン（あるいは 2 つの設定）に通し、出力を diff する。
10. **HITL bash script。** 最後の手段。人間がクリックしなければならないなら、`scripts/hitl-loop.template.sh` で*その人間を*駆動し、loop を構造化されたままにする。キャプチャした出力があなたにフィードバックされる。

正しい feedback loop を構築すれば、バグは 90% 直ったも同然である。

### loop を締める

loop を product として扱う。一度 loop ができたら、**締める**:

- もっと速くできるか?（setup をキャッシュする、無関係な init をスキップする、テスト範囲を狭める。）
- signal をもっと鋭くできるか?（"クラッシュしなかった" ではなく、具体的な symptom を assert する。）
- もっと deterministic にできるか?（時刻を固定する、RNG に seed を与える、filesystem を隔離する、network を凍結する。）

30 秒かかる flaky な loop は loop が無いのとほぼ変わらない。2 秒の deterministic な loop は tight — デバッグの superpower である。

### Non-deterministic なバグ

目標はきれいな repro ではなく、**より高い再現率**である。トリガーを 100 回 loop する、並列化する、stress を加える、timing window を狭める、sleep を注入する。50% の flake するバグはデバッグ可能だが、1% は不可能 — デバッグ可能になるまで率を上げ続ける。

### 本当に loop を構築できないとき

立ち止まり、そう明示的に述べる。試したことを列挙する。ユーザーに以下を求める: (a) 再現する環境へのアクセス、(b) キャプチャされた artifact（HAR ファイル、log dump、core dump、タイムスタンプ付きの画面録画）、または (c) 一時的な production instrumentation を追加する許可。loop なしに hypothesize する段階に **進んではならない**。

### 完了基準 — red になる tight な loop

Phase 1 が完了するのは、loop が **tight** かつ **red-capable** であるとき: **1 つのコマンド** — script のパス、test invocation、curl — を名指しでき、それを**すでに少なくとも一度実行しており**（invocation とその出力を貼り付ける）、それが以下を満たす:

- [ ] **Red-capable** — 実際のバグの code path を駆動し、**ユーザーの正確な symptom** を assert する。これによりこのバグで red になり、直れば green になる。「エラーなく実行される」ではダメで、_この特定のバグを捕捉できる_必要がある。
- [ ] **Deterministic** — 毎回同じ判定になる（flaky なバグの場合: 上記のとおり固定された高い再現率）。
- [ ] **Fast** — 分ではなく秒。
- [ ] **Agent-runnable** — 人手を介さず実行できる。loop 内に人間が入るのは `scripts/hitl-loop.template.sh` 経由のみ。

このコマンドが存在する前にコードを読んで理論を組み立てようとしている自分に気づいたら、**立ち止まれ — いきなり hypothesis に飛びつくことこそ、この skill が防ごうとしている失敗そのものである。** red-capable なコマンドが無ければ、Phase 2 も無い。

## Phase 2 — 再現 + 最小化

loop を実行する。red になるのを見る — バグが現れる。

確認する:

- [ ] loop が生み出す failure mode は **ユーザー** が説明したものである — たまたま近くにある別の failure ではない。バグを間違えれば、修正も間違う。
- [ ] failure は複数回の実行にわたって再現可能である（あるいは non-deterministic なバグの場合、デバッグに十分な高さの率で再現可能である）。
- [ ] 正確な symptom（エラーメッセージ、間違った出力、遅い timing）をキャプチャしてある。これにより後の phase で修正が実際にそれに対処しているか検証できる。

### 最小化する

red になったら、repro を **red のままでいられる最小のシナリオ** に縮める。入力、caller、config、data、手順を **一度に 1 つずつ** 削り、削るたびに loop を再実行する — failure に対して load-bearing なものだけを残す。

なぜそうするか: 最小化された repro は Phase 3 での hypothesis space を縮小し（疑うべき可動部分が減る）、Phase 5 でのきれいな regression test になる。

**残っているすべての要素が load-bearing** — そのどれか 1 つを取り除くと loop が green になる — であれば完了。

再現 **かつ** 最小化するまで先に進まない。

## Phase 3 — 仮説を立てる

どれか 1 つをテストする前に **3〜5 個の順位付けされた hypothesis** を生成する。単一の hypothesis 生成は最初にもっともらしいアイデアに anchor してしまう。

各 hypothesis は **falsifiable** でなければならない: それが立てる予測を明示する。

> Format: "If <X> is the cause, then <changing Y> will make the bug disappear / <changing Z> will make it worse."
> 形式:「もし X が原因なら、Y を変えるとバグは消え、Z を変えるとバグは悪化するはずだ」

予測を述べられないなら、その hypothesis は vibe に過ぎない — 捨てるか、研ぎ澄ます。

**テストする前に、順位付けしたリストをユーザーに見せる。** ユーザーはしばしば即座に順位を入れ替える domain knowledge を持っている（「#3 への変更をちょうどデプロイしたところだ」）、あるいはすでに除外済みの hypothesis を知っている。安いチェックポイントで、大きな時間の節約になる。これでブロックしない — ユーザーが AFK なら自分の順位付けのまま進める。

## Phase 4 — 計測する (Instrument)

各 probe は Phase 3 の特定の予測に対応していなければならない。**一度に 1 つの変数だけを変える。**

Tool の優先順位:

1. 環境が対応していれば **Debugger / REPL inspection**。1 つの breakpoint は 10 個の log に勝る。
2. hypothesis を区別する境界における **Targeted logs**。
3. 「全部 log して grep する」は絶対にしない。

**すべての debug log** に一意な prefix、例えば `[DEBUG-a4f2]` を付ける。最後の cleanup が単一の grep で済むようになる。tag の無い log は生き残り、tag された log は死ぬ。

**Perf branch。** performance regression の場合、log は大抵役に立たない。代わりに: baseline measurement（timing harness、`performance.now()`、profiler、query plan）を確立し、そこから bisect する。まず計測、修正はその後。

## Phase 5 — 修正 + regression test

regression test は修正の**前に**書く — ただし **correct seam** が存在する場合に限る。

correct seam とは、call site で実際に起きる**本物のバグのパターン**をテストが行使できる seam のことである。利用可能な唯一の seam が浅すぎる場合（バグが複数の caller を必要とするのに単一 caller のテストしかない、バグを引き起こした chain を再現できない unit test しかない）、そこに regression test を置くと誤った安心感を与えるだけである。

**correct seam が存在しないなら、それ自体が finding である。** それを記録する。codebase architecture がバグを封じ込めることを妨げている。次の phase のためにこれを flag する。

correct seam が存在する場合:

1. 最小化した repro を、その seam での failing test に変える。
2. それが fail するのを見る。
3. 修正を適用する。
4. それが pass するのを見る。
5. 元の（最小化していない）シナリオに対して Phase 1 の feedback loop を再実行する。

## Phase 6 — Cleanup + post-mortem

完了を宣言する前に必須:

- [ ] 元の repro がもう再現しない（Phase 1 の loop を再実行する）
- [ ] regression test が pass する（または seam が無いことが文書化されている）
- [ ] すべての `[DEBUG-...]` instrumentation が除去されている（prefix を `grep` する）
- [ ] 使い捨ての prototype が削除されている（または明確に marked された debug 用の場所に移されている）
- [ ] 正しいと判明した hypothesis が commit / PR message に記されている — 次のデバッガーが学べるように

**そして問う: このバグを何が防げただろうか?** 答えが architectural な変更（良い test seam が無い、絡み合った caller、隠れた coupling）を伴うなら、具体的な内容とともに `/improve-codebase-architecture` skill に引き継ぐ。この提案は修正が入った**後**に行う。始めた時点よりも今の方が情報を多く持っているからだ。

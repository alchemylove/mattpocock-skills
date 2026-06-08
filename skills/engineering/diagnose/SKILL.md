---
name: diagnose
description: Disciplined diagnosis loop for hard bugs and performance regressions. Reproduce → minimise → hypothesise → instrument → fix → regression-test. Use when user says "diagnose this" / "debug this", reports a bug, says something is broken/throwing/failing, or describes a performance regression.
---

# 診断 (Diagnose)

難しいバグに対する規律あるアプローチ。明示的に正当化できる場合に限り、フェーズをスキップしてよい。

コードベースを探索するときは、プロジェクトの domain glossary を使って関連モジュールのメンタルモデルを明確にし、触る領域の ADR を確認すること。

## フェーズ 1 — フィードバックループを構築 (Phase 1 — Build a feedback loop)

**これがこの skill の本質である。** それ以外はすべて機械的な作業。バグに対して高速で決定的かつ agent が実行可能な pass/fail シグナルがあれば、原因は見つかる — bisection、仮説検証、instrumentation はすべてそのシグナルを消費するだけである。シグナルがなければ、コードをいくら凝視しても救われない。

ここに不釣り合いなほどの労力をかけること。**積極的に。創造的に。諦めない。**

### 構築方法 — おおよそこの順で試す (Ways to construct one — try them in roughly this order)

1. **Failing test** — バグに届く seam で、unit、integration、e2e のいずれか。
2. **Curl / HTTP script** — 起動中の dev server に対して実行。
3. **CLI invocation** — fixture input を渡し、stdout を known-good snapshot と diff。
4. **Headless browser script** (Playwright / Puppeteer) — UI を操作し、DOM/console/network を assert。
5. **Replay a captured trace.** 実際の network request / payload / event log をディスクに保存し、コードパスを分離して replay。
6. **Throwaway harness.** システムの最小サブセット（1 サービス、mocked deps）を立ち上げ、単一の function call でバグのコードパスを実行。
7. **Property / fuzz loop.** バグが「ときどき間違った出力」の場合、1000 件の random input を実行して failure mode を探す。
8. **Bisection harness.** バグが 2 つの既知の状態（commit、dataset、version）の間に現れた場合、「state X で起動、確認、繰り返し」を自動化し、`git bisect run` できるようにする。
9. **Differential loop.** 同じ input を old-version と new-version（または 2 つの config）で実行し、出力を diff。
10. **HITL bash script.** 最終手段。人間がクリックしなければならない場合でも、`scripts/hitl-loop.template.sh` で _彼ら_ を駆動し、ループを構造化する。キャプチャした出力があなたにフィードバックされる。

適切なフィードバックループを構築すれば、バグは 90% 修正済みである。

### ループ自体を反復改善する (Iterate on the loop itself)

ループをプロダクトとして扱う。_ある_ ループができたら、次を問う:

- もっと速くできるか？（setup を cache、無関係な init を skip、test scope を狭める。）
- シグナルをより鋭くできるか？（「クラッシュしなかった」ではなく、特定の症状を assert。）
- より決定的にできるか？（time を pin、RNG を seed、filesystem を isolate、network を freeze。）

30 秒の flaky loop は、ループなしと大差ない。2 秒の決定的 loop は debugging の超能力である。

### 非決定的なバグ (Non-deterministic bugs)

目標はきれいな repro ではなく、**再現率の向上**である。trigger を 100 回 loop、parallelise、stress を加え、timing window を狭め、sleep を注入する。50% flake のバグは debug 可能である。1% は無理 — 率を上げ続け、debug 可能になるまで。

### ループを本当に構築できない場合 (When you genuinely cannot build a loop)

明示的にそう伝えて停止する。試したことを列挙する。ユーザーに次を求める: (a) 再現する環境へのアクセス、(b) キャプチャした artifact（HAR file、log dump、core dump、タイムスタンプ付き screen recording）、または (c) 一時的な production instrumentation を追加する許可。**ループなしで hypothesise に進んではならない。**

信頼できるループができるまで、フェーズ 2 に進まないこと。

## フェーズ 2 — 再現 (Phase 2 — Reproduce)

ループを実行する。バグが現れるのを観察する。

確認すること:

- [ ] ループが **ユーザー** が説明した failure mode を再現する — たまたま近くで起きる別の failure ではない。間違ったバグ = 間違った fix。
- [ ] failure が複数回の実行で再現可能である（非決定的バグの場合は、debug に十分な再現率であること）。
- [ ] 正確な症状（error message、wrong output、slow timing）をキャプチャし、後のフェーズで fix が実際にそれに対処したことを検証できること。

バグを再現するまで進まないこと。

## フェーズ 3 — 仮説 (Phase 3 — Hypothesise)

いずれかを検証する前に、**ランク付けした 3〜5 個の仮説**を生成する。単一仮説の生成は、最初に plausible なアイデアにアンカーする。

各仮説は **falsifiable** でなければならない: その仮説が予測することを述べること。

> Format: "If <X> is the cause, then <changing Y> will make the bug disappear / <changing Z> will make it worse."

予測を述べられなければ、その仮説は vibe である — 捨てるか sharpen すること。

**検証前にランク付けリストをユーザーに見せる。** 彼らは domain knowledge で即座に再ランクできることが多い（「#3 に change を deploy したばかり」）、またはすでに除外した仮説を知っている。安い checkpoint で、大きな時間節約になる。ブロックしない — ユーザーが AFK なら自分のランキングで進む。

## フェーズ 4 — 計測 (Phase 4 — Instrument)

各 probe はフェーズ 3 の特定の予測に対応しなければならない。**一度に 1 変数だけ変更する。**

ツールの優先順位:

1. **Debugger / REPL inspection** — env が対応していれば。1 つの breakpoint は 10 個の log に勝る。
2. **Targeted logs** — 仮説を区別する境界に置く。
3. 「すべて log して grep」はしない。

**すべての debug log に** 一意の prefix を付ける。例: `[DEBUG-a4f2]`。最後の cleanup は 1 回の grep で済む。tag なし log は残る。tag 付き log は消える。

**Perf branch.** performance regression では、log は通常間違い。代わりに: baseline measurement（timing harness、`performance.now()`、profiler、query plan）を確立してから bisect。まず measure、次に fix。

## フェーズ 5 — 修正 + regression test (Phase 5 — Fix + regression test)

regression test は fix の **前に** 書く — ただし **correct seam** がある場合に限る。

correct seam とは、call site で実際に起きる **real bug pattern** を test が実行する seam である。利用可能な seam が浅すぎる場合（バグに複数 caller が必要なのに single-caller test、バグを引き起こした chain を再現できない unit test）、そこでの regression test は false confidence を与える。

**correct seam が存在しない場合、それ自体が finding である。** 記録する。コードベース architecture がバグを lock down できない。次のフェーズで flag する。

correct seam がある場合:

1. minimised repro をその seam の failing test にする。
2. fail するのを確認する。
3. fix を適用する。
4. pass するのを確認する。
5. フェーズ 1 のフィードバックループを元の（minimise 前の）シナリオで再実行する。

## フェーズ 6 — クリーンアップ + post-mortem (Phase 6 — Cleanup + post-mortem)

完了宣言の前に必須:

- [ ] 元の repro が再現しなくなった（フェーズ 1 のループを再実行）
- [ ] regression test が pass（または seam の欠如が文書化されている）
- [ ] すべての `[DEBUG-...]` instrumentation を削除（prefix で `grep`）
- [ ] throwaway prototype を削除（または明確にマークした debug 場所へ移動）
- [ ] 正しかった仮説を commit / PR message に記載 — 次の debugger が学べるように

**その後問う: このバグを防げたものは何か？** 答えに architectural change（good test seam がない、tangled callers、hidden coupling）が含まれるなら、具体的内容を添えて `/improve-codebase-architecture` skill に hand off する。推奨は fix の **後** に行う — 開始時より多くの情報がある。

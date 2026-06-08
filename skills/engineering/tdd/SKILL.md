---
name: tdd
description: Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development.
---

# テスト駆動開発 (Test-Driven Development)

## 哲学 (Philosophy)

**Core principle**: test は implementation details ではなく public interfaces 経由で behaviour を検証すべきである。コードは完全に変わってもよい; test は変わるべきではない。

**Good tests** は integration-style である: public API 経由で real code path を実行する。_何を_ するかを記述し、_どう_ するかではない。良い test は specification のように読める — "user can checkout with valid cart" は存在する capability を正確に伝える。これらの test は refactor を生き延びる。内部構造を気にしないからである。

**Bad tests** は implementation に coupled している。internal collaborator を mock し、private method を test し、interface ではなく external means（例: database を直接 query）で検証する。警告サイン: refactor しても behaviour は変わっていないのに test が壊れる。internal function の rename で test が fail するなら、それらは behaviour ではなく implementation を test していた。

例は [tests.md](tests.md)、mocking guideline は [mocking.md](mocking.md)。

## アンチパターン: 水平スライス (Anti-Pattern: Horizontal Slices)

**すべての test を先に書き、次にすべての implementation を書いてはならない。** これは "horizontal slicing" である — RED を "すべての test を書く"、GREEN を "すべての code を書く" と扱う。

これは **crap tests** を生む:

- bulk で書いた test は _想像した_ behaviour を test し、_実際の_ behaviour ではない
- _形_（data structures、function signatures）を test し、user-facing behaviour ではない
- test は real change に鈍感になる — behaviour が壊れても pass、behaviour が問題なくても fail
- headlights の先を走り、implementation を理解する前に test structure に commit する

**Correct approach**: tracer bullet による vertical slice。1 test → 1 implementation → 繰り返し。各 test は前の cycle から学んだことに応答する。コードを書いた直後なので、どの behaviour が重要か、どう検証するか正確に分かっている。

```
WRONG (horizontal):
  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5

RIGHT (vertical):
  RED→GREEN: test1→impl1
  RED→GREEN: test2→impl2
  RED→GREEN: test3→impl3
  ...
```

## ワークフロー (Workflow)

### 1. 計画 (Planning)

コードベースを探索するときは、プロジェクトの domain glossary を使い test 名と interface 語彙がプロジェクトの言語と一致するようにし、触る領域の ADR を尊重する。

いかなる code を書く前に:

- [ ] ユーザーと必要な interface changes を確認
- [ ] ユーザーと test する behaviour（優先順位）を確認
- [ ] [deep modules](deep-modules.md) の機会を特定（small interface、deep implementation）
- [ ] [testability](interface-design.md) のための interface を設計
- [ ] test する behaviour を列挙（implementation steps ではない）
- [ ] プランのユーザー承認を得る

尋ねる:「What should the public interface look like? Which behaviors are most important to test?」

**すべては test できない。** ユーザーとどの behaviour が最も重要か正確に確認する。すべての edge case ではなく、critical path と complex logic に testing effort を集中する。

### 2. Tracer Bullet

システムについて **1 つ** を確認する test を **1 つ** 書く:

```
RED:   Write test for first behavior → test fails
GREEN: Write minimal code to pass → test passes
```

これが tracer bullet である — path が end-to-end で動くことを証明する。

### 3. インクリメンタルループ (Incremental Loop)

残りの各 behaviour について:

```
RED:   Write next test → fails
GREEN: Minimal code to pass → passes
```

Rules:

- 一度に 1 test
- 現在の test を pass するのに十分な code だけ
- 将来の test を先取りしない
- test は observable behaviour に集中

### 4. リファクタ (Refactor)

すべての test が pass したら、[refactor candidates](refactoring.md) を探す:

- [ ] duplication を抽出
- [ ] module を deepen（complexity を simple interface の背後へ）
- [ ] 自然なところで SOLID principles を適用
- [ ] 新 code が既存 code について何を明らかにするか検討
- [ ] 各 refactor step の後に test を実行

**RED の間は refactor しない。** まず GREEN に到達する。

## サイクルごとのチェックリスト (Checklist Per Cycle)

```
[ ] Test describes behavior, not implementation
[ ] Test uses public interface only
[ ] Test would survive internal refactor
[ ] Code is minimal for this test
[ ] No speculative features added
```

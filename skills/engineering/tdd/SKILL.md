---
name: tdd
description: テスト駆動開発。ユーザーが機能構築やバグ修正を test-first で行いたい、「red-green-refactor」に言及した、または integration test を求めたときに使う。
---

# Test-Driven Development

TDD は red → green の loop である。この skill は、その loop が残す価値のあるテストを生み出すための reference である: 良いテストとは何か、テストがどこに置かれるか、anti-pattern、loop のルール。すべてのセクションは毎回の cycle に適用される — loop の後ではなく、前と最中に参照する。

codebase を探索する際は、テスト名と interface の vocabulary がプロジェクトの domain language と一致するよう `CONTEXT.md`（存在すれば）を読み、触れる領域の ADR を尊重する。

## 良いテストとは何か

テストは implementation の詳細ではなく public interface を通して behavior を検証する。コードはまるごと変わりうるが、テストは変わるべきではない。良いテストは specification のように読める — "user can checkout with valid cart" は、どんな capability が存在するかを正確に伝える — そして内部構造を気にしないため refactor を生き延びる。

例は [tests.md](tests.md) を、mocking の指針は [mocking.md](mocking.md) を参照。

## Seams — テストがどこに置かれるか

**seam** とは、テストする public な境界である: 内側に手を伸ばさずに behavior を観測できる interface のこと。テストは seam に置かれ、決して internals に対して置かれない。

**事前に合意した seam でのみテストする。** どんなテストを書く前にも、テスト対象の seam を書き出し、ユーザーと確認する。確認されていない seam ではテストを書かない。すべてをテストすることはできない — 事前に seam を合意することで、テストの労力があらゆる edge case ではなく critical path と複雑な logic に落ち着く。

尋ねる: 「public interface は何で、どの seam をテストすべきか?」

## Anti-patterns

- **Implementation-coupled** — 内部の collaborator を mock する、private method をテストする、あるいは側道（interface を使わずに database に直接問い合わせる）で検証する。見分け方: behavior が変わっていないのに refactor するとテストが壊れる。
- **Tautological** — assertion がコードと同じ方法で expected value を再計算している（`expect(add(a, b)).toBe(a + b)`、同じ方法で手作りされた snapshot、自分自身と等しいと assert される定数）ため、構造上必ず pass し、コードと食い違うことが決してない。expected value は独立した source of truth — known-good な literal、worked example、spec — から来なければならない。
- **Horizontal slicing** — 先にすべてのテストを書き、その後すべての implementation を書く。まとめて書いたテストは _想像上の_ behavior を検証する: ユーザー向けの behavior ではなく物事の _shape_ をテストすることになり、テストは本物の変化に鈍感になり、implementation を理解する前にテスト構造にコミットしてしまう。代わりに **vertical slices** で作業する — 1 つのテスト → 1 つの implementation → 繰り返し。各テストは前の cycle が教えてくれたことに応じる **tracer bullet** である。

## Rules of the loop

- **green の前に red。** 先に failing test を書き、それから pass させるのに足りるだけのコードだけを書く。将来のテストを先取りしたり、speculative な機能を追加したりしない。
- **一度に 1 つの slice。** 1 サイクルにつき、1 つの seam、1 つのテスト、1 つの最小限の implementation。
- **Refactoring は loop の一部ではない。** それは red → green の implementation cycle ではなく、review の段階（`code-review` skill を参照）に属する。

---
name: request-refactor-plan
description: ユーザーへのインタビューを通じて tiny commits による詳細な refactor plan を作成し、GitHub issue として提出する。ユーザーが refactor を計画したい、refactoring RFC を作成したい、または refactor を安全な段階的ステップに分解したいときに使う。
---

この skill はユーザーが refactor request を作成したいときに呼び出される。以下の手順を進める。不要と判断した手順はスキップしてよい。

1. 解決したい問題と、考えうる解決策について、ユーザーに長く詳細な説明を求める。

2. repo を調査し、ユーザーの主張を検証し、codebase の現状を理解する。

3. 他の選択肢を検討したか確認し、他の選択肢を提示する。

4. 実装についてユーザーにインタビューする。極めて詳細かつ徹底的に。

5. 実装の正確なスコープを固める。変更するものと変更しないものを明確にする。

6. codebase でこの領域の test coverage を確認する。不十分なら、テスト計画をユーザーに確認する。

7. 実装を tiny commit の plan に分解する。Martin Fowler の "make each refactoring step as small as possible, so that you can always see the program working." を念頭に置く。

8. refactor plan を GitHub issue として作成する。issue description には次のテンプレートを使用:

<refactor-plan-template>

## Problem Statement

The problem that the developer is facing, from the developer's perspective.

## Solution

The solution to the problem, from the developer's perspective.

## Commits

A LONG, detailed implementation plan. Write the plan in plain English, breaking down the implementation into the tiniest commits possible. Each commit should leave the codebase in a working state.

## Decision Document

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- Prior art for the tests (i.e. similar types of tests in the codebase)

## Out of Scope

A description of the things that are out of scope for this refactor.

## Further Notes (optional)

Any further notes about the refactor.

</refactor-plan-template>

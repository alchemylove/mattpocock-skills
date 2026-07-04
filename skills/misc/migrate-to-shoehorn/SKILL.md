---
name: migrate-to-shoehorn
description: test ファイルを `as` type assertion から @total-typescript/shoehorn へ移行する。ユーザーが shoehorn について触れた、test 内の `as` を置き換えたい、または partial test data が必要なときに使う。
---

# Shoehorn への移行 (Migrate to Shoehorn)

## なぜ shoehorn か? (Why shoehorn?)

`shoehorn` は test で partial data を渡しつつ TypeScript を満足させられる。`as` assertion を型安全な代替に置き換える。

**test code のみ。** production code では shoehorn を使わない。

test での `as` の問題:

- 使わないよう訓練されている
- target type を手動で指定する必要がある
- 意図的に誤った data には double-as (`as unknown as Type`) が必要

## インストール (Install)

```bash
npm i @total-typescript/shoehorn
```

## 移行パターン (Migration patterns)

### 必要な property が少ない大きな object

Before:

```ts
type Request = {
  body: { id: string };
  headers: Record<string, string>;
  cookies: Record<string, string>;
  // ...20 more properties
};

it("gets user by id", () => {
  // Only care about body.id but must fake entire Request
  getUser({
    body: { id: "123" },
    headers: {},
    cookies: {},
    // ...fake all 20 properties
  });
});
```

After:

```ts
import { fromPartial } from "@total-typescript/shoehorn";

it("gets user by id", () => {
  getUser(
    fromPartial({
      body: { id: "123" },
    }),
  );
});
```

### `as Type` → `fromPartial()`

Before:

```ts
getUser({ body: { id: "123" } } as Request);
```

After:

```ts
import { fromPartial } from "@total-typescript/shoehorn";

getUser(fromPartial({ body: { id: "123" } }));
```

### `as unknown as Type` → `fromAny()`

Before:

```ts
getUser({ body: { id: 123 } } as unknown as Request); // wrong type on purpose
```

After:

```ts
import { fromAny } from "@total-typescript/shoehorn";

getUser(fromAny({ body: { id: 123 } }));
```

## それぞれを使うタイミング (When to use each)

| Function        | Use case                                           |
| --------------- | -------------------------------------------------- |
| `fromPartial()` | Pass partial data that still type-checks           |
| `fromAny()`     | Pass intentionally wrong data (keeps autocomplete) |
| `fromExact()`   | Force full object (swap with fromPartial later)    |

## ワークフロー (Workflow)

1. **要件の収集 (Gather requirements)** — ユーザーに確認:
   - どの test file の `as` assertion が問題になっているか?
   - 一部の property しか重要でない大きな object を扱っているか?
   - error testing のために意図的に誤った data を渡す必要があるか?

2. **インストールと移行 (Install and migrate)**:
   - [ ] インストール: `npm i @total-typescript/shoehorn`
   - [ ] `as` assertion がある test file を検索: `grep -r " as [A-Z]" --include="*.test.ts" --include="*.spec.ts"`
   - [ ] `as Type` を `fromPartial()` に置換
   - [ ] `as unknown as Type` を `fromAny()` に置換
   - [ ] `@total-typescript/shoehorn` から import を追加
   - [ ] type check を実行して検証

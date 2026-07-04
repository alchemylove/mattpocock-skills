# 良いテストと悪いテスト (Good and Bad Tests)

## 良いテスト (Good Tests)

**Integration-style**: 内部パーツの mock ではなく、実際の interface 経由でテストする。

```typescript
// GOOD: Tests observable behavior
test("user can checkout with valid cart", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});
```

特徴:

- users/callers が気にする behavior をテストする
- public API のみを使う
- 内部 refactor 後も生き残る
- HOW ではなく WHAT を記述する
- テストあたり 1 つの論理的 assertion

## 悪いテスト (Bad Tests)

**Implementation-detail tests**: 内部構造に結合している。

```typescript
// BAD: Tests implementation details
test("checkout calls paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

危険信号:

- internal collaborators を mock している
- private methods をテストしている
- call counts/order を assertion している
- behavior が変わらない refactor でテストが壊れる
- テスト名が WHAT ではなく HOW を記述している
- interface ではなく外部手段で検証している

```typescript
// BAD: Bypasses interface to verify
test("createUser saves to database", async () => {
  await createUser({ name: "Alice" });
  const row = await db.query("SELECT * FROM users WHERE name = ?", ["Alice"]);
  expect(row).toBeDefined();
});

// GOOD: Verifies through interface
test("createUser makes user retrievable", async () => {
  const user = await createUser({ name: "Alice" });
  const retrieved = await getUser(user.id);
  expect(retrieved.name).toBe("Alice");
});
```

**Tautological tests**: 期待値が implementation を言い換えているだけなので、テストは構造上必ず通ってしまう。

```typescript
// BAD: Expected value is recomputed the way the code computes it
test("calculateTotal sums line items", () => {
  const items = [{ price: 10 }, { price: 5 }];
  const expected = items.reduce((sum, i) => sum + i.price, 0);
  expect(calculateTotal(items)).toBe(expected);
});

// GOOD: Expected value is an independent, known literal
test("calculateTotal sums line items", () => {
  expect(calculateTotal([{ price: 10 }, { price: 5 }])).toBe(15);
});
```

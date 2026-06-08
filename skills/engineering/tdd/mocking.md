# モックを使うタイミング (When to Mock)

**system boundaries** でのみモックする:

- External APIs（payment、email など）
- Databases（場合による — test DB を優先）
- Time/randomness
- File system（場合による）

モックしない:

- 自分の classes/modules
- Internal collaborators
- 自分が制御できるもの

## モック可能な設計 (Designing for Mockability)

system boundaries では、モックしやすい interface を設計する:

**1. dependency injection を使う**

外部依存を内部で生成せず、引数で渡す:

```typescript
// Easy to mock
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}

// Hard to mock
function processPayment(order) {
  const client = new StripeClient(process.env.STRIPE_KEY);
  return client.charge(order.total);
}
```

**2. 汎用 fetcher より SDK スタイルの interface を優先**

条件分岐を持つ 1 つの汎用関数ではなく、各外部操作ごとに専用関数を作る:

```typescript
// GOOD: Each function is independently mockable
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch('/orders', { method: 'POST', body: data }),
};

// BAD: Mocking requires conditional logic inside the mock
const api = {
  fetch: (endpoint, options) => fetch(endpoint, options),
};
```

SDK アプローチの利点:

- 各 mock が 1 つの特定 shape を返す
- test setup に条件分岐が不要
- テストがどの endpoint を使うか把握しやすい
- endpoint ごとの type safety

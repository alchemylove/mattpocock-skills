# テスト容易性のための interface 設計 (Interface Design for Testability)

良い interface はテストを自然にする:

1. **依存を受け取り、内部で作らない**

   ```typescript
   // Testable
   function processOrder(order, paymentGateway) {}

   // Hard to test
   function processOrder(order) {
     const gateway = new StripeGateway();
   }
   ```

2. **結果を返し、side effects を生まない**

   ```typescript
   // Testable
   function calculateDiscount(cart): Discount {}

   // Hard to test
   function applyDiscount(cart): void {
     cart.total -= discount;
   }
   ```

3. **Small surface area**
   - methods が少ない = 必要なテストが少ない
   - params が少ない = test setup が単純

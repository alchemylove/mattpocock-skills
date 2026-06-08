# リファクタ候補 (Refactor Candidates)

TDD サイクルの後、次を確認する:

- **Duplication** → function/class を抽出
- **Long methods** → private helper に分割（public interface のテストは維持）
- **Shallow modules** → 結合するか深める
- **Feature envy** → データがある場所へロジックを移動
- **Primitive obsession** → value object を導入
- **Existing code** — 新しいコードが問題として露呈させた既存コード

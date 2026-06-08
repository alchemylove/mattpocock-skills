---
name: setup-pre-commit
description: Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing.
---

# Pre-Commit Hook のセットアップ (Setup Pre-Commit Hooks)

## セットアップ内容 (What This Sets Up)

- **Husky** pre-commit hook
- **lint-staged** ですべての staged file に Prettier を実行
- **Prettier** config (ない場合)
- pre-commit hook 内の **typecheck** と **test** script

## 手順 (Steps)

### 1. package manager の検出 (Detect package manager)

`package-lock.json` (npm)、`pnpm-lock.yaml` (pnpm)、`yarn.lock` (yarn)、`bun.lockb` (bun) を確認。存在するものを使用。不明な場合は npm をデフォルト。

### 2. 依存関係のインストール (Install dependencies)

devDependencies としてインストール:

```
husky lint-staged prettier
```

### 3. Husky の初期化 (Initialize Husky)

```bash
npx husky init
```

`.husky/` ディレクトリを作成し、package.json に `prepare: "husky"` を追加する。

### 4. `.husky/pre-commit` の作成 (Create `.husky/pre-commit`)

このファイルを書き込む (Husky v9+ では shebang 不要):

```
npx lint-staged
npm run typecheck
npm run test
```

**Adapt**: `npm` を検出した package manager に置き換える。repo に `typecheck` または `test` script がなければ、その行を省略しユーザーに伝える。

### 5. `.lintstagedrc` の作成 (Create `.lintstagedrc`)

```json
{
  "*": "prettier --ignore-unknown --write"
}
```

### 6. `.prettierrc` の作成 (Create `.prettierrc`) (ない場合)

Prettier config が存在しない場合のみ作成。デフォルト:

```json
{
  "useTabs": false,
  "tabWidth": 2,
  "printWidth": 80,
  "singleQuote": false,
  "trailingComma": "es5",
  "semi": true,
  "arrowParens": "always"
}
```

### 7. 検証 (Verify)

- [ ] `.husky/pre-commit` が存在し実行可能
- [ ] `.lintstagedrc` が存在する
- [ ] package.json の `prepare` script が `"husky"`
- [ ] `prettier` config が存在する
- [ ] `npx lint-staged` を実行して動作確認

### 8. commit (Commit)

変更/作成したすべての file を stage し、次のメッセージで commit: `Add pre-commit hooks (husky + lint-staged + prettier)`

新しい pre-commit hook を通過する — すべてが動作するかの smoke test になる。

## 注意事項 (Notes)

- Husky v9+ では hook file に shebang は不要
- `prettier --ignore-unknown` は Prettier が parse できない file (画像など) をスキップ
- pre-commit はまず lint-staged (高速、staged のみ)、次に full typecheck と test を実行

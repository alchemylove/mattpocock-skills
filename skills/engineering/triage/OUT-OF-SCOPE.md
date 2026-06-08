# Out-of-Scope ナレッジベース (Out-of-Scope Knowledge Base)

repo の `.out-of-scope/` ディレクトリは、却下された feature request の永続的な記録を保存する。2 つの目的がある:

1. **Institutional memory** — feature が却下された理由。issue を閉じても reasoning が失われない
2. **Deduplication** — 新しい issue が以前の却下と一致するとき、skill は再議論の代わりに以前の決定を提示できる

## ディレクトリ構造 (Directory structure)

```
.out-of-scope/
├── dark-mode.md
├── plugin-system.md
└── graphql-api.md
```

issue ごとではなく、**concept** ごとに 1 ファイル。同じことを求める複数の issue は 1 ファイルにまとめる。

## ファイル形式 (File format)

ファイルは relaxed で読みやすい文体で書く — database entry というより短い design document。paragraphs、code samples、examples で reasoning を明確にし、初めて遭遇する人にも有用にする。

```markdown
# Dark Mode

This project does not support dark mode or user-facing theming.

## Why this is out of scope

The rendering pipeline assumes a single color palette defined in
`ThemeConfig`. Supporting multiple themes would require:

- A theme context provider wrapping the entire component tree
- Per-component theme-aware style resolution
- A persistence layer for user theme preferences

This is a significant architectural change that doesn't align with the
project's focus on content authoring. Theming is a concern for downstream
consumers who embed or redistribute the output.

```ts
// The current ThemeConfig interface is not designed for runtime switching:
interface ThemeConfig {
  colors: ColorPalette; // single palette, resolved at build time
  fonts: FontStack;
}
```

## Prior requests

- #42 — "Add dark mode support"
- #87 — "Night theme for accessibility"
- #134 — "Dark theme option"
```

### ファイルの命名 (Naming the file)

concept の短く説明的な kebab-case 名を使う: `dark-mode.md`、`plugin-system.md`、`graphql-api.md`。ディレクトリを眺めただけで何が却下されたか分かる名前にする。

### reason の書き方 (Writing the reason)

reason は substantive であること — 「欲しくない」ではなく why。良い reason は次を参照する:

- Project scope や philosophy（「このプロジェクトは X に焦点。theming は downstream の関心事」）
- Technical constraints（「これをサポートするには Y が必要で、Z architecture と矛盾する」）
- Strategic decisions（「subtle な理由で B ではなく A を選んだ」）

reason は durable であること。一時的な状況（「今は忙しすぎる」）は避ける — それは本当の却下ではなく deferral。

## `.out-of-scope/` を確認するタイミング (When to check `.out-of-scope/`)

triage 中（Step 1: Gather context）に `.out-of-scope/` の全ファイルを読む。新しい issue を評価するとき:

- リクエストが既存の out-of-scope concept と一致するか確認
- 一致は keyword ではなく concept similarity で — 「night theme」は `dark-mode.md` に一致
- 一致があれば maintainer に提示: 「これは `.out-of-scope/dark-mode.md` と似ている — 以前 [reason] で却下した。まだ同じ考えか?」

maintainer は次のいずれか:

- **Confirm** — 新しい issue を既存ファイルの "Prior requests" に追加し、close
- **Reconsider** — out-of-scope ファイルを削除または更新し、issue は通常 triage を続行
- **Disagree** — issues は関連するが別物、通常 triage を続行

## `.out-of-scope/` に書くタイミング (When to write to `.out-of-scope/`)

**enhancement**（bug ではない）が `wontfix` で却下されたときだけ。フロー:

1. Maintainer が feature request を out of scope と判断
2. 一致する `.out-of-scope/` ファイルが既にあるか確認
3. あれば: 新しい issue を "Prior requests" に追加
4. なければ: concept 名、decision、reason、最初の prior request で新規ファイル作成
5. issue に決定を説明し、`.out-of-scope/` ファイルに言及するコメントを投稿
6. `wontfix` label で issue を close

## out-of-scope ファイルの更新・削除 (Updating or removing out-of-scope files)

maintainer が以前却下した concept について考えを変えた場合:

- `.out-of-scope/` ファイルを削除
- skill は古い issues を reopen する必要はない — それらは historical records
- reconsideration を引き起こした新しい issue は通常 triage を続行

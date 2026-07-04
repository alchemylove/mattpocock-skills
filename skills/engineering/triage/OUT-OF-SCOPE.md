# Out-of-Scope Knowledge Base

repo 内の `.out-of-scope/` ディレクトリは、却下された feature request の永続的な記録を保存する。これは 2 つの目的を果たす:

1. **Institutional memory** — なぜ feature が却下されたか。issue が close されても理由が失われないように。
2. **Deduplication** — 以前の却下に一致する新しい issue が来たとき、skill は再び論争する代わりに以前の決定を表に出せる。

## Directory structure

```
.out-of-scope/
├── dark-mode.md
├── plugin-system.md
└── graphql-api.md
```

issue ごとではなく、**concept** ごとに 1 ファイル。同じことを求める複数の issue は 1 つのファイルの下にまとめられる。

## File format

ファイルは、database の entry というより短い design document のような、肩の力の抜けた読みやすいスタイルで書くべきである。段落、code sample、例を使い、初めて出会う人にとって理由が明確で役立つものにする。

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

### ファイルに名前を付ける

concept に対して短く説明的な kebab-case の名前を使う: `dark-mode.md`、`plugin-system.md`、`graphql-api.md`。ディレクトリを見る人がファイルを開かなくても何が却下されたか分かるくらい、認識しやすい名前にする。

### 理由を書く

理由は実質的であるべきだ — "we don't want this" ではなく、なぜかを書く。良い理由は以下を参照する:

- プロジェクトの scope や哲学（"This project focuses on X; theming is a downstream concern"）
- 技術的な制約（"Supporting this would require Y, which conflicts with our Z architecture"）
- 戦略的な決定（"We chose to use A instead of B because..."）

理由は durable であるべきだ。一時的な事情（"we're too busy right now"）への言及は避ける — それらは本物の却下ではなく、先送りに過ぎない。

## `.out-of-scope/` を確認するタイミング

triage 中（手順 1: context を集める）に、`.out-of-scope/` 内のすべてのファイルを読む。新しい issue を評価する際:

- request が既存の out-of-scope な concept に一致するか確認する
- マッチングは keyword ではなく concept の類似性で行う — "night theme" は `dark-mode.md` に一致する
- 一致するものがあれば、それを maintainer に表に出す: "これは `.out-of-scope/dark-mode.md` に似ています — 以前 [理由] で却下しました。今でも同じ考えですか?"

maintainer は以下を選べる:

- **Confirm** — 新しい issue が既存ファイルの "Prior requests" リストに追加され、close される
- **Reconsider** — out-of-scope ファイルが削除または更新され、issue は通常の triage を進む
- **Disagree** — issue は関連しているが別物であり、通常の triage を進める

## `.out-of-scope/` に書くタイミング

**enhancement**（bug ではない）が `wontfix` として *rejected* されたときのみ。これは issue と全く同様に enhancement な PR にも適用される — 却下された PR はここに記録され、同じ request が新しいコードとして戻ってこないようにする。

**すでに実装済み**であることを理由に何かが `wontfix` として close された場合はここに**書かない**。それは build された機能であり、却下されたものではない。記録すると、誤った却下で dedup チェックを汚染してしまう。代わりに、closing comment はその機能がすでにどこにあるかを指し示す。

flow:

1. maintainer が feature request を対象外と決定する
2. 一致する `.out-of-scope/` ファイルがすでに存在するか確認する
3. あれば: 新しい issue を "Prior requests" リストに追記する
4. 無ければ: concept 名、決定、理由、最初の prior request を持つ新しいファイルを作成する
5. issue に決定を説明し `.out-of-scope/` ファイルに言及する comment を投稿する
6. `wontfix` label を付けて issue を close する

## out-of-scope ファイルの更新・削除

maintainer が以前に却下した concept について考えを変えた場合:

- `.out-of-scope/` ファイルを削除する
- skill は古い issue を再度開く必要はない — それらは historical record である
- reconsideration を引き起こした新しい issue は通常の triage を進む

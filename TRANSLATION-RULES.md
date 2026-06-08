# 翻訳ルール (Translation Rules)

`SKILL.md` やドキュメントを日本語化するときのルール。元規則: `everything-claude-code/TRANSLATION-RULES.md`（2026-06-07 確定）。

## スコープ (Scope)

| 対象 | 件数 |
|------|------|
| ルート・バケット `README.md` | 7 |
| `SKILL.md` | 28 |
| サポート `.md` | 20 |
| `docs/adr/*.md` | 1 |
| `.out-of-scope/*.md` | 3 |
| **合計** | **59** |

## 基本方針

- 説明文・ガイドライン・手順は **日本語** に翻訳する
- キーワード、ファイルパス、他ファイルへのリンク、URL は **原文のまま** 残す

## 翻訳しないもの

| 種別 | 例 |
|------|-----|
| キーワード・技術用語 | `feat`, `fix`, `docs`, `camelCase`, `Conventional Commits` |
| ファイルパス・リンク | `skills/*/SKILL.md`, `CONTEXT.md`, `docs/adr/` |
| URL | `https://github.com/...`, `https://skills.sh/...` |
| YAML の識別子 | `name: tdd`, `description: ...` |
| メタラベル（斜体・太字） | `*Commit message example*`, `**Example commit sequence**:` |
| コード内のパス・識別子 | `import { Button } from '../components/Button'` |

## 見出し（`#` で始まる H1〜H6）

**形式:** `日本語訳 (Original English)`

```markdown
## 概要 (Overview)
## クイックスタート (Quickstart)
### エンジニアリング (Engineering)
```

- 括弧内には **元の英語見出し全文** を入れる

## Frontmatter

- `name` と `description` は識別子・メタデータのため **原文のまま**（翻訳しない）

## チェックリスト

翻訳完了時に確認:

- [ ] すべての `#` 見出しが `日本語 (English)` 形式か
- [ ] frontmatter の `name` と `description` が原文のままか
- [ ] ファイルパス・リンク・URL が改変されていないか

## 進捗確認

```powershell
# 英語のみの見出しが残っていないか検出（簡易チェック）
rg "^## [A-Za-z]" . --glob "*.md" --glob "!TRANSLATION-RULES.md"
```

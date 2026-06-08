---
name: obsidian-vault
description: Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to find, create, or organize notes in Obsidian.
---

# Obsidian Vault (Obsidian Vault)

## Vault の場所 (Vault location)

`/mnt/d/Obsidian Vault/AI Research/`

root レベルはほぼフラット。

## 命名規則 (Naming conventions)

- **Index notes**: 関連トピックを集約 (例: `Ralph Wiggum Index.md`、`Skills Index.md`、`RAG Index.md`)
- すべての note 名は **Title case**
- 整理用の folder は使わない — link と index note を使う

## リンク (Linking)

- Obsidian `[[wikilinks]]` 構文を使用: `[[Note Title]]`
- note の末尾に依存/関連 note への link
- index note は `[[wikilinks]]` のリストのみ

## ワークフロー (Workflows)

### note の検索 (Search for notes)

```bash
# Search by filename
find "/mnt/d/Obsidian Vault/AI Research/" -name "*.md" | grep -i "keyword"

# Search by content
grep -rl "keyword" "/mnt/d/Obsidian Vault/AI Research/" --include="*.md"
```

または Grep/Glob tool を vault path に直接使う。

### 新しい note の作成 (Create a new note)

1. filename に **Title Case** を使用
2. vault のルールに従い、学習の単位として content を書く
3. 末尾に関連 note への `[[wikilinks]]` を追加
4. 番号付きシーケンスの一部なら、階層的な番号付けスキームを使用

### 関連 note の検索 (Find related notes)

vault 全体で `[[Note Title]]` を検索して backlink を見つける:

```bash
grep -rl "\\[\\[Note Title\\]\\]" "/mnt/d/Obsidian Vault/AI Research/"
```

### index note の検索 (Find index notes)

```bash
find "/mnt/d/Obsidian Vault/AI Research/" -name "*Index*"
```

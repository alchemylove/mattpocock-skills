---
name: git-guardrails-claude-code
description: Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code.
---

# Git Guardrails のセットアップ (Setup Git Guardrails)

Claude が実行する前に危険な git コマンドを intercept して block する PreToolUse hook をセットアップする。

## block されるもの (What Gets Blocked)

- `git push` (すべての variant、`--force` を含む)
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

block された場合、Claude にはこれらのコマンドにアクセスする権限がない旨のメッセージが表示される。

## 手順 (Steps)

### 1. スコープの確認 (Ask scope)

ユーザーに確認: **この project のみ** (`.claude/settings.json`) か、**すべての project** (`~/.claude/settings.json`) か?

### 2. hook script のコピー (Copy the hook script)

同梱の script は: [scripts/block-dangerous-git.sh](scripts/block-dangerous-git.sh)

スコープに応じてターゲットの場所へコピー:

- **Project**: `.claude/hooks/block-dangerous-git.sh`
- **Global**: `~/.claude/hooks/block-dangerous-git.sh`

`chmod +x` で実行可能にする。

### 3. settings に hook を追加 (Add hook to settings)

適切な settings ファイルに追加:

**Project** (`.claude/settings.json`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

**Global** (`~/.claude/settings.json`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

settings ファイルが既に存在する場合、既存の `hooks.PreToolUse` 配列に hook を merge する — 他の settings を上書きしない。

### 4. カスタマイズの確認 (Ask about customization)

block リストに pattern を追加/削除したいかユーザーに確認。コピーした script をそれに応じて編集する。

### 5. 検証 (Verify)

簡単なテストを実行:

```bash
echo '{"tool_input":{"command":"git push origin main"}}' | <path-to-script>
```

exit code 2 で終了し、stderr に BLOCKED メッセージが出力されること。

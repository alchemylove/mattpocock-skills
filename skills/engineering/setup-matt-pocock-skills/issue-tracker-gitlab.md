# Issue tracker: GitLab (Issue tracker: GitLab)

この repo の issues と PRD は GitLab issues として存在する。すべての操作に [`glab`](https://gitlab.com/gitlab-org/cli) CLI を使う。

## 慣習 (Conventions)

- **Create an issue**: `glab issue create --title "..." --description "..."`。複数行 description は heredoc を使う。エディタを開くには `--description -` を渡す。
- **Read an issue**: `glab issue view <number> --comments`。machine-readable 出力には `-F json` を使う。
- **List issues**: 適切な `--label` フィルタ付きで `glab issue list -F json`
- **Comment on an issue**: `glab issue note <number> --message "..."`。GitLab では comments を "notes" と呼ぶ。
- **Apply / remove labels**: `glab issue update <number> --label "..."` / `--unlabel "..."`。複数 labels はカンマ区切りまたは flag 繰り返し。
- **Close**: `glab issue close <number>`。`glab issue close` は closing comment を受け付けないので、先に `glab issue note <number> --message "..."` で説明を投稿してから close。
- **Merge requests**: GitLab では PR を "merge requests" と呼ぶ。`glab mr create`、`glab mr view`、`glab mr note` など — `gh pr ...` と同じ形で `pr` の代わりに `mr`、`comment`/`--body` の代わりに `note`/`--message`。

`git remote -v` から repo を推論 — clone 内で実行すれば `glab` は自動で行う。

## skill が "publish to the issue tracker" と言うとき

GitLab issue を作成する。

## skill が "fetch the relevant ticket" と言うとき

`glab issue view <number> --comments` を実行する。

# Issue tracker: GitHub (Issue tracker: GitHub)

この repo の issues と PRD は GitHub issues として存在する。すべての操作に `gh` CLI を使う。

## 慣習 (Conventions)

- **Create an issue**: `gh issue create --title "..." --body "..."`。複数行 body は heredoc を使う。
- **Read an issue**: `gh issue view <number> --comments`。`jq` で comments をフィルタし、labels も取得。
- **List issues**: 適切な `--label` と `--state` フィルタ付きで `gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`
- **Comment on an issue**: `gh issue comment <number> --body "..."`
- **Apply / remove labels**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> --comment "..."`

`git remote -v` から repo を推論 — clone 内で実行すれば `gh` は自動で行う。

## skill が "publish to the issue tracker" と言うとき

GitHub issue を作成する。

## skill が "fetch the relevant ticket" と言うとき

`gh issue view <number> --comments` を実行する。

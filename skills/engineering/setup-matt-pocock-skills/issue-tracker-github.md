# Issue tracker: GitHub

この repo の issue と PRD は GitHub issue として存在する。すべての操作に `gh` CLI を使う。

## Conventions

- **issue を作成する**: `gh issue create --title "..." --body "..."`。複数行の body には heredoc を使う。
- **issue を読む**: `gh issue view <number> --comments`、comment を `jq` でフィルタし、label も取得する。
- **issue を一覧する**: `gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'` に適切な `--label` と `--state` のフィルタを付ける。
- **issue に comment する**: `gh issue comment <number> --body "..."`
- **label を適用 / 除去する**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> --comment "..."`

`git remote -v` から repo を推測する — clone の中で実行すれば `gh` が自動でこれを行う。

## Triage surface としての pull request

**PRs as a request surface: no。** _(この repo が external な PR を feature request として扱うなら `yes` に設定する。`/triage` はこの flag を読む。)_

`yes` に設定すると、PR は issue と同じ label・state を通り、`gh pr` の対応するコマンドを使う:

- **PR を読む**: diff には `gh pr view <number> --comments` と `gh pr diff <number>`。
- **triage 対象の external な PR を一覧する**: `gh pr list --state open --json number,title,body,labels,author,authorAssociation,comments` を実行し、`authorAssociation` が `CONTRIBUTOR`、`FIRST_TIME_CONTRIBUTOR`、`NONE` のものだけを残す（`OWNER`/`MEMBER`/`COLLABORATOR` は除外）。
- **Comment / label / close**: `gh pr comment`、`gh pr edit --add-label`/`--remove-label`、`gh pr close`。

GitHub は issue と PR で番号空間を共有しているため、単なる `#42` はどちらの可能性もある — `gh pr view 42` で解決し、ダメなら `gh issue view 42` にフォールバックする。

## skill が "publish to the issue tracker" と言うとき

GitHub issue を作成する。

## skill が "fetch the relevant ticket" と言うとき

`gh issue view <number> --comments` を実行する。

## Wayfinding operations

`/wayfinder` が使用する。**map** はチケットとなる **child** issue を持つ単一の issue である。

- **Map**: `wayfinder:map` label が付いた単一の issue で、Notes / Decisions-so-far / Fog の本文を保持する。`gh issue create --label wayfinder:map`。
- **Child ticket**: map に GitHub sub-issue としてリンクされた issue（sub-issues endpoint に対する `gh api`）。sub-issues が有効でない場合は、map の本文内の task list に child を追加し、child の本文冒頭に `Part of #<map>` を記載する。Labels: `wayfinder:<type>`（`research`/`prototype`/`grilling`/`task`）。claim されると、そのチケットは担当する開発者に assign される。
- **Blocking**: GitHub の **native issue dependencies** — canonical で UI 上に見える表現。`gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>` で edge を追加する。`<blocker-db-id>` は blocker の数値の **database id**（`gh api repos/<owner>/<repo>/issues/<n> --jq .id`。`#number` や `node_id` では*ない*）。GitHub は `issue_dependencies_summary.blocked_by`（open な blocker のみ — live な gate）を報告する。dependencies が利用できない場合は、child の本文冒頭の `Blocked by: #<n>, #<n>` 行にフォールバックする。すべての blocker が close されたときチケットは unblocked になる。
- **Frontier query**: map の open な child を一覧し（`gh issue list --state open` を map の sub-issues / task list に絞る）、open な blocker がある（`issue_dependencies_summary.blocked_by > 0`、または `Blocked by` 行に open な issue がある）か assignee があるものを除外する。map の順序で最初のものが勝つ。
- **Claim**: `gh issue edit <n> --add-assignee @me` — セッションの最初の書き込み。
- **Resolve**: `gh issue comment <n> --body "<answer>"`、次に `gh issue close <n>`、それから map の Decisions-so-far に context pointer（gist + link）を追記する。

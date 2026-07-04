# Issue tracker: GitLab

この repo の issue と PRD は GitLab issue として存在する。すべての操作に [`glab`](https://gitlab.com/gitlab-org/cli) CLI を使う。

## Conventions

- **issue を作成する**: `glab issue create --title "..." --description "..."`。複数行の description には heredoc を使う。エディタを開くには `--description -` を渡す。
- **issue を読む**: `glab issue view <number> --comments`。機械可読な出力には `-F json` を使う。
- **issue を一覧する**: `glab issue list -F json` に適切な `--label` フィルタを付ける。
- **issue に comment する**: `glab issue note <number> --message "..."`。GitLab は comment を "notes" と呼ぶ。
- **label を適用 / 除去する**: `glab issue update <number> --label "..."` / `--unlabel "..."`。複数の label はカンマ区切り、または flag を繰り返すことで指定できる。
- **Close**: `glab issue close <number>`。`glab issue close` は closing comment を受け付けないため、先に `glab issue note <number> --message "..."` で説明を投稿してから close する。
- **Merge requests**: GitLab は PR を "merge request" と呼ぶ。`glab mr create`、`glab mr view`、`glab mr note` などを使う — `gh pr ...` と同じ形で、`pr` の代わりに `mr`、`comment`/`--body` の代わりに `note`/`--message` を使う。

`git remote -v` から repo を推測する — clone の中で実行すれば `glab` が自動でこれを行う。

## Triage surface としての merge request

**MRs as a request surface: no。** _(この repo が external な merge request を feature request として扱うなら `yes` に設定する。`/triage` はこの flag を読む。)_

`yes` に設定すると、MR は issue と同じ label・state を通り、`glab mr` の対応するコマンドを使う:

- **MR を読む**: diff には `glab mr view <number> --comments` と `glab mr diff <number>`。
- **triage 対象の external な MR を一覧する**: `glab mr list -F json` を実行し、author が project の member/owner でない MR だけを残す（maintainer の作業中のものではなく、contributor の MR）。
- **Comment / label / close**: `glab mr note`、`glab mr update --label`/`--unlabel`、`glab mr close`。

GitHub と異なり、GitLab は issue と MR の番号を別々に振るため、maintainer がどちらの surface を意味しているか分かれば `#42` は一意である。

## skill が "publish to the issue tracker" と言うとき

GitLab issue を作成する。

## skill が "fetch the relevant ticket" と言うとき

`glab issue view <number> --comments` を実行する。

## Wayfinding operations

`/wayfinder` が使用する。**map** はチケットとなる **child** issue を持つ単一の issue である。

- **Map**: `wayfinder:map` label が付いた単一の issue で、Notes / Decisions-so-far / Fog の本文を保持する。`glab issue create --label wayfinder:map`。（native epic のある GitLab tier では、epic が代わりに map を保持してもよい。label 付き issue はどこでも動作する。）
- **Child ticket**: description 冒頭に `Part of #<map>` を、label に `wayfinder:<type>`（`research`/`prototype`/`grilling`/`task`）を持つ issue。claim されると、そのチケットは担当する開発者に assign される。
- **Blocking**: GitLab の **native blocking link** — canonical で UI 上に見える表現。`/blocked_by #<n>` quick action を note として投稿して追加する（`glab issue note <child> --message "/blocked_by #<blocker>"`）。native blocking link は Premium/Ultimate の機能である。free tier（または利用できない場合）では description 冒頭の `Blocked by: #<n>, #<n>` 行にフォールバックする。すべての blocker が close されたときチケットは unblocked になる。
- **Frontier query**: map の child に絞った `glab issue list -F json` を実行し、open な blocker（open な issue への native な `blocked_by` link、`glab api projects/:id/issues/:iid/links`）や `Blocked by` 行の open な issue、あるいは assignee があるものを除外する。map の順序で最初のものが勝つ。
- **Claim**: `glab issue update <n> --assignee @me` — セッションの最初の書き込み。
- **Resolve**: `glab issue note <n> --message "<answer>"`、次に `glab issue close <n>`、それから map の Decisions-so-far に context pointer（gist + link）を追記する。

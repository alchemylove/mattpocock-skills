# Issue tracker: Local Markdown (Issue tracker: Local Markdown)

この repo の issues と PRD は `.scratch/` 内の markdown ファイルとして存在する。

## 慣習 (Conventions)

- feature ごとに 1 ディレクトリ: `.scratch/<feature-slug>/`
- PRD は `.scratch/<feature-slug>/PRD.md`
- implementation issues は `.scratch/<feature-slug>/issues/<NN>-<slug>.md`、`01` から採番
- triage state は各 issue ファイル先頭付近の `Status:` 行に記録（role 文字列は `triage-labels.md` 参照）
- comments と会話履歴はファイル末尾の `## Comments` 見出しの下に追記

## skill が "publish to the issue tracker" と言うとき

`.scratch/<feature-slug>/` 配下に新規ファイルを作成（必要ならディレクトリも作成）。

## skill が "fetch the relevant ticket" と言うとき

参照された path のファイルを読む。ユーザーは通常 path または issue number を直接渡す。

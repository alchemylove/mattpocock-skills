# Issue tracker: Local Markdown

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

参照されたパスのファイルを読む。ユーザーは通常、パスまたは issue 番号を直接渡す。

## Wayfinding 操作 (Wayfinding operations)

`/wayfinder` が使用する。**map** は ticket ごとに1つの **child** ファイルを持つファイルである。

- **Map**: `.scratch/<effort>/map.md` — Notes / Decisions-so-far / Fog の本体。
- **Child ticket**: `.scratch/<effort>/issues/NN-<slug>.md`、`01` から採番し、本文に質問を記載する。`Type:` 行に ticket の種類（`research`/`prototype`/`grilling`/`task`）を、`Status:` 行に `claimed`/`resolved` を記録する。
- **Blocking**: 先頭付近の `Blocked by: NN, NN` 行。列挙されたすべてのファイルが `resolved` になるとブロック解除される。
- **Frontier**: `.scratch/<effort>/issues/` を走査し、open・unblocked・unclaimed なファイルを探す。番号の早いものが優先される。
- **Claim**: 作業を始める前に `Status: claimed` を設定して保存する。
- **Resolve**: `## Answer` 見出しの下に回答を追記し、`Status: resolved` を設定してから、map の `map.md` 内 Decisions-so-far に context pointer（gist + link）を追記する。

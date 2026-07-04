`skills/` 配下の bucket フォルダに skills が整理されています:

- `engineering/` — 日々のコード作業
- `productivity/` — 日々の非コード系ワークフローツール
- `misc/` — 残してあるが滅多に使われない。promoted 対象外
- `personal/` — 自分自身のセットアップに紐づく。promoted 対象外
- `in-progress/` — まだ出荷準備ができていない下書き
- `deprecated/` — もう使われていない

`engineering/` または `productivity/`（**promoted** バケット）内のすべての skill は、トップレベルの `README.md` に参照を持ち、`.claude-plugin/plugin.json` にエントリを持たなければならない。`misc/`、`personal/`、`in-progress/`、`deprecated/` 内の skill は、どちらにも登場してはならない。

トップレベルの `README.md` の各 skill entry は、skill 名をその `SKILL.md` に link しなければなりません。

各 bucket フォルダには、そのバケット内のすべての skill を一行説明とともに列挙する `README.md` があり、skill 名はその `SKILL.md` にリンクされる。promoted バケットの `README.md` とトップレベルの `README.md` は、エントリを **User-invoked** と **Model-invoked** にグループ分けする。非 promoted バケットの `README.md`（`misc/`、`personal/`）はフラットなリストを使う。

`engineering/` と `productivity/` 内の skill には、`docs/<bucket>/<skill-name>.md` に人間向けの docs page もある（docs ツリーは `skills/` 配下のこの2つの bucket フォルダを反映している）。公開 URL はバケットに関わらず `https://aihero.dev/skills-<skill-name>` であり — docs のパスはリポジトリ内の整理のためだけのものだ。`engineering/` や `productivity/` 内の skill を追加・リネーム・挙動変更したときは、[.agents/writing-docs.md](./.agents/writing-docs.md) に従って docs page を作成または再同期すること。非 promoted バケット（`misc/`、`personal/`、`in-progress/`、`deprecated/`）内の skill には docs page は**存在しない**。

すべての `SKILL.md` は、user-invoked（`disable-model-invocation: true`、人間のみが到達可能）か model-invoked（モデルまたはユーザーが到達可能）のいずれかである。詳細は [.agents/invocation.md](./.agents/invocation.md) を参照。

[`ask-matt`](./skills/engineering/ask-matt/SKILL.md) は、ユーザーが到達可能なすべての skill と、それらの関係をマッピングする router である。docs page を再同期させるのと同じトリガーがこれにも適用される: ユーザーが到達可能な skill を追加・リネーム・削除したり、フローへの組み込み方を変更したりするたびに、`ask-matt` の `SKILL.md` を読み直し、マップが正確であり続けるよう更新すること — 一度も言及されない新しい skill や、いまだにルーティングされている古い skill があれば、それは嘘をつく router だ。

すべての skill をローカルの harness skill ディレクトリ（`~/.claude/skills`、`~/.agents/skills`）へ(再)リンクするには、`scripts/link-skills.sh` を実行する。各エントリはこのリポジトリへのシンボリックリンクなので、`git pull` すればインストール済みの skill は最新のまま保たれる。skill の追加・削除・リネーム後はこのスクリプトを再実行すること。

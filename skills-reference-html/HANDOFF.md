# 引き継ぎ: mattpocock-skills 全skill翻訳 + skill一覧表 作業

## 元の依頼
1. `https://skills.sh/mattpocock/skills` の全 skill を update してほしい（upstream 同期 → 日本語へ翻訳し直し）
2. このプロジェクトで使える全 skill（mattpocock リポジトリ + ビルトイン公式 + 有効プラグイン）の一覧表を作成してほしい

## リポジトリ / ブランチ
- `C:\Users\alfas\Documents\git1\mattpocock-skills`、ブランチ `translate/ja`
- 作業前のスナップショット: ブランチ `backup/translate-ja-pre-sync`（削除しないこと）
- 作業前にステージされていた内容（旧・部分翻訳のロールバック分 + 未追跡 `.claude/`）は `git stash list` の `stash@{0}` に退避済み。まだ pop していない。必要なければそのままでよいが、勝手に drop しないこと。

## これまでの作業（すべて `translate/ja` にコミット済み、push はしていない）

1. `847837a` — upstream `mattpocock/skills` の `272f99b`（main）を `-X theirs` でマージし、英語ベースラインを確立。`decision-mapping` → `wayfinder` へのリネーム等の upstream 側構造変更を反映。
2. `ab70b14` → `a13b411` → `a182fc6` → `99d0f36` → `dfabb40` — `docs/skills-overview.ja.md`（新規）を作成・改良。全 skill（mattpocock 38件 + ビルトイン公式 16件 + プラグイン 5件 = 59件）を1つの表にまとめた。列: `skill | 起動 | 概要 | 日本語訳 | 種別 | 英語訳`。「起動」は `U`/`M`/`U?`/`M?` の短縮コード（`?`=推定）。「種別」は `mattpocock（バケット名）` / `built-in` / `plugin（プラグイン名）`。途中で見つけた bug（`claude-api` 行の日本語訳セル内に未エスケープの `|` があり表が崩れていた）も修正済み。
3. `845a73e`・`f5e1030`・`6078644`・`c09f5fb` — 全 skill（`skills/engineering`・`skills/productivity`・`skills/misc`・`skills/personal`・`skills/in-progress`・`skills/deprecated` の SKILL.md と補助ファイル、`docs/engineering`・`docs/productivity` の docs page、トップレベル `README.md`・`CLAUDE.md`・`.agents/*`）を日本語へ翻訳し直した。翻訳ルールは repo メモリ `feedback_translation_rules.md`（技術用語は英語のまま、引用文・BEFORE/AFTER は英日併記 等）に準拠。

**→ 依頼1（全skill翻訳）と依頼2（一覧表作成）はどちらも完了しコミット済み。**

## 現在取り組んでいたこと: 一覧表の HTML 版（Artifact）

`docs/skills-overview.ja.md` の表をユーザーが見やすいように、レスポンシブな HTML Artifact として別途生成していた（**この HTML はリポジトリにはコミットしていない**、生成スクリプトのみこのフォルダに保存）。

### 経緯（ユーザーからの修正依頼の流れ）
1. 最初は3つに分かれた表（mattpocockリポジトリ / ビルトイン / プラグイン）だった
2. 「skill,起動,概要日本語訳,種別,英語訳の順にしてください。種別はmatt-pocockなのかbuiltinなのか」→ 1つの表に統合、列順変更
3. 「概要と日本語訳は分けてください。英語訳は原文のまま」→ 概要/日本語訳を別列に分割、英語訳を省略せず原文全文に復元（この過程で `claude-api` 行の pipe エスケープ漏れバグを発見・修正）
4. 「モデル起動 (推定) など縦長になっています。ユーザー起動→U、モデル起動→M、推定→?、にして表はレスポンシブにしてください」→ `docs/skills-overview.ja.md` 側の起動列を `U`/`M`/`U?`/`M?` に短縮（これはリポジトリにコミット済み）。表示用に HTML Artifact を新規生成（`artifact-design` skill を読み込んで設計）。
5. 「よこscrollバーはやめてください」→ 常時カード表示レイアウトに変更して再公開
6. 「カードにしろとは言ってません。前回の型式で横スクロールバーを廃止し、レスポンシブにしてください」→ **テーブル形式に戻し**、`table-layout: fixed` + `<colgroup>` で各列を%指定（`min-width` を撤廃）、720px 以下でのみカードへフォールバックする形に修正して再公開
7. → **ここでユーザーから「不具合がいくつか出てます」と報告があったが、具体的な内容は次のセッションで説明するとのこと。**

### 現在の Artifact 公開URL
https://claude.ai/code/artifact/020e3f72-1574-409c-8568-7097c651c01a
（同じ URL に `force` なしで再公開を繰り返している。次のセッションでもこの URL に対して `Artifact` ツールで再デプロイできる）

### 生成パイプライン（このフォルダ内、3ステップ）
1. **`parse_table.py`** — `docs/skills-overview.ja.md` の Markdown 表をパースして `rows.json` を生成。**エスケープされた `\|` を正しく扱う**（一度このハンドリング漏れで `claude-api` 行が壊れたことがある）。
2. **`build_html.py`** — `rows.json` を読み、各セルの Markdown（`[label](url)` リンク、`` `code` ``、既存の `<br>`）を HTML に変換しつつ `records.json` を生成。カテゴリ（`種別`）を `mattpocock`/`built-in`/`plugin` + サブカテゴリ（バケット名等）にパース。
3. **`render_html.py`** — `records.json` から最終的な `skills-overview.html` を生成。CSS トークン（ライト/ダークテーマ両対応）、検索ボックス + 種別フィルタボタンの JS、`<table>` ベースのレイアウト（720px 以下でカードにフォールバック）を含む。

**再生成する場合は3つとも順番に実行する**（`python3 parse_table.py && python3 build_html.py && python3 render_html.py`）。ただし各スクリプト内のパスは元のセッションの scratchpad パス（`C:/Users/alfas/AppData/Local/Temp/claude/.../scratchpad/`）を指しているものが混在しているため、**新セッションで実行する前にパスをこのフォルダ（`skills-reference-html/`）基準に書き換える必要がある**。

### 既知の設計判断（引き継ぎ用メモ）
- ビルトイン/プラグイン skill の「起動」は frontmatter を直接確認できないため `U?`/`M?`（推定）表記。判定根拠は `docs/skills-overview.ja.md` 冒頭に明記。
- `resolving-merge-conflicts` skill は `skills/engineering/` に存在するが `README.md`/`plugin.json` に未登録（upstream 側の登録漏れの可能性、今回のリポジトリ構成ルール違反）。表に ※1 として注記済み。修正はしていない（upstream 側の問題のため）。
- HTML Artifact 自体はリポジトリに未コミット。ユーザーが望めば `docs/` 配下等に保存することも検討可（前回の応答で保留とした）。

## 次のセッションでまずやること
1. ユーザーから HTML Artifact の具体的な不具合（スクリーンショット等）を聞く
2. このフォルダ（`skills-reference-html/`）のスクリプトとファイルを確認し、パスを新セッションの scratchpad または任意の作業ディレクトリに合わせて調整
3. 不具合を修正し、`render_html.py` を再実行して `Artifact` ツールで同じ URL に再公開

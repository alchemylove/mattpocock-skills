`skills/` 配下の bucket フォルダに skills が整理されています:

- `engineering/` — 日々の code 作業
- `productivity/` — 日々の non-code workflow ツール
- `misc/` — 残しておくがあまり使わない
- `personal/` — 自分の setup に紐づくもので、promote しない
- `in-progress/` — まだ ship 準備ができていない draft
- `deprecated/` — もう使わない

`engineering/`、`productivity/`、`misc/` の各 skill は、トップレベルの `README.md` への参照と `.claude-plugin/plugin.json` への entry が必須です。`personal/`、`in-progress/`、`deprecated/` の skill は、どちらにも載せてはいけません。

トップレベルの `README.md` の各 skill entry は、skill 名をその `SKILL.md` に link しなければなりません。

各 bucket フォルダには `README.md` があり、その bucket 内の全 skill を one-line description 付きで一覧し、skill 名はその `SKILL.md` に link します。

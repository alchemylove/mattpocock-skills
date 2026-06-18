`skills/` 配下の bucket フォルダに skills が整理されています:

- `engineering/` — 日々の code 作業
- `productivity/` — 日々の non-code workflow ツール
- `misc/` — 残しておくがあまり使わない
- `personal/` — 自分の setup に紐づくもので、promote しない
- `in-progress/` — まだ ship 準備ができていない draft
- `deprecated/` — もう使わない

`engineering/`、`productivity/`、`misc/` の各 skill は、トップレベルの `README.md` への参照と `.claude-plugin/plugin.json` への entry が必須です。`personal/`、`in-progress/`、`deprecated/` の skill は、どちらにも載せてはいけません。

トップレベルの `README.md` の各 skill entry は、skill 名をその `SKILL.md` に link しなければなりません。

Each bucket folder has a `README.md` that lists every skill in the bucket with a one-line description, with the skill name linked to its `SKILL.md`. Bucket `README.md`s and the top-level `README.md` group entries into **User-invoked** and **Model-invoked**.

Every `SKILL.md` is either user-invoked (`disable-model-invocation: true`, reachable only by the human) or model-invoked (model- or user-reachable). For the full definitions, description conventions, and why a user-invoked skill can invoke model-invoked skills but never another user-invoked one, see [docs/invocation.md](./docs/invocation.md).

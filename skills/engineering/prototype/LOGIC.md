# ロジックプロトタイプ (Logic Prototype)

ユーザーが手動で state model を操作できる小さな対話型 terminal app。**business logic、state transitions、data shape** に関する問い — 紙の上では妥当に見えても、実際のケースを通すと違和感が出る種類 — に使う。

## この形が適切なとき (When this is the right shape)

- 「この state machine は X のあと Y という edge case を扱えるか分からない」
- 「この data model は実際に…というケースを表現できるか」
- 「書く前に API がどうあるべきか感触を掴みたい」
- ユーザーが **ボタンを押して state の変化を見たい** あらゆる場面

問いが「これはどう見えるべきか」なら — 別ブランチ。[UI.md](UI.md) を使う。

## プロセス (Process)

### 1. 問いを明文化する

コードを書く前に、どの state model でどんな問いを prototype するか書き留める。prototype の README かファイル先頭のコメントに 1 段落。間違った問いに答える logic prototype は純粋な無駄 — 問いを明示し、ユーザーが今見ているか AFK で後から戻るかにかかわらず後で検証できるようにする。

### 2. 言語を選ぶ

host project が使うものを使う。明らかな runtime がない repo（docs repo など）なら質問する。

prototype のためだけに新しい package manager や runtime を追加しない — プロジェクトの既存 tooling 慣習に合わせる。

### 3. ロジックを portable module に隔離する

問いに答える部分 — 実際の logic — を、後で本番 codebase に持ち込める小さく pure な interface の背後に置く。周りの TUI は捨て物。logic module は捨てない。

適切な形は問い次第:

- **Pure reducer** — `(state, action) => state`。actions が離散イベントで state が単一値のときに適する。
- **State machine** — 明示的な states と transitions。「今どの actions が合法か」自体が問いの一部のときに適する。
- **Plain data type に対する小さな pure functions の集合**。暗黙の current state がない — 変換だけのときに適する。
- **Class や明確な method surface を持つ module** — logic が継続的な internal state を本当に所有するとき。

TUI に配線しやすい形ではなく、問いに最も合う形を選ぶ。pure に保つ: I/O なし、terminal code なし、control flow に `console.log` なし。TUI が import して呼び出す。逆方向の流れはない。

これが prototype を寿命を超えて有用にする。問いに答えたら、検証済みの reducer / machine / function set を本番 module に持ち込める — TUI shell は削除する。

### 4. state を露出する最小の TUI を構築する

**軽量 TUI** として構築 — 毎 tick で画面をクリア（`console.clear()` / `print("\033[2J\033[H")` / 同等）し、フレーム全体を再描画。ユーザーは常に 1 つの安定した view を見る。scrollback が延々と増えない。

各フレームは次の 2 部構成、この順序:

1. **Current state** — pretty-print し diff-friendly（1 field 1 行、または formatted JSON）。field 名や section header に **bold**、timestamps、IDs、derived values など重要度の低い context に **dim**。Native ANSI escape code で十分 — `\x1b[1m` bold、`\x1b[2m` dim、`\x1b[0m` reset。プロジェクトに styling library がなければ追加不要。
2. **Keyboard shortcuts** — 下部に列挙: `[a] add user  [d] delete user  [t] tick clock  [q] quit`。key を bold、description を dim、またはその逆 — 読みやすい方。

振る舞い:

1. **Initialise state** — 単一の in-memory object/struct。起動時に最初のフレームを描画。
2. **1 keystroke（または 1 行）ずつ読み**、handler に dispatch して state を変更。
3. 各 action の後にフレーム全体を **再描画** — append せず replace。
4. **quit までループ。**

フレーム全体は 1 画面に収まること。

### 5. 1 コマンドで実行可能にする

既存の task runner（`package.json` scripts、`Makefile`、`justfile`、`pyproject.toml`）に script を追加。ユーザーは `pnpm run <prototype-name>` などを実行するだけ — path を覚える必要なし。

host project に task runner がなければ、prototype の README 先頭にコマンドを書く。

### 6. 引き渡す

run コマンドを渡す。ユーザーが自分で操作する。面白い瞬間は「待って、それはあり得ないはず」や「え、X は違うはずだった」 — それが _idea_ のバグであり、これが目的。新しい actions が欲しければ追加する。prototype は進化する。

### 7. 答えを記録する

prototype が役目を終えたら、問いへの答えだけが残す価値のあるもの。ユーザーがいれば何を学んだか聞く。いなければ prototype の隣に `NOTES.md` を置き、prototype 削除前に答えを記入できるようにする（セッションを見ていれば自分で記入してもよい）。

## アンチパターン (Anti-patterns)

- **テストを追加しない。** テストが必要な prototype はもはや prototype ではない。
- **本番 database に接続しない。** 問いが persistence そのものでなければ in-memory store を使う。
- **一般化しない。** 「後で X をサポートしたくなったら」は不要。prototype は 1 つの問いに答える。
- **logic と TUI を混ぜない。** reducer / state machine が `console.log`、prompts、terminal escape codes を参照するなら portable ではない。pure module の上に薄い TUI shell を保つ。
- **TUI shell を production に出荷しない。** shell は terminal から手動操作するために最適化されている。背後の logic module が残す価値のある部分。

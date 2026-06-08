# UI プロトタイプ (UI Prototype)

単一 route 上に **根本的に異なる UI バリエーションを複数** 生成し、floating bottom bar から切り替え可能にする。ユーザーはブラウザで variant を行き来し、1 つを選ぶ（または各 variant から要素を盗む）と、残りは捨てる。

見た目ではなく logic/state に関する問いなら — 別ブランチ。[LOGIC.md](LOGIC.md) を使う。

## この形が適切なとき (When this is the right shape)

- 「このページはどう見えるべきか?」
- 「コミット前にこの dashboard の選択肢をいくつか見たい」
- 「settings screen の別レイアウトを試したい」
- 頭の中で 3 つの曖昧な mockup を 1 日悩むことになりそうなとき

## 2 つの sub-shape — sub-shape A を強く優先

UI prototype は **アプリの残りと接している** と判断しやすい — 本物の header、sidebar、data、density。単独の throwaway route は真空で、variant は孤立するとどれも良く見える。host できる既存 page があるなら sub-shape A をデフォルトに。prototype に本当に近い home がないときだけ sub-shape B。

### Sub-shape A — 既存 page への調整（優先）

route は既に存在する。variant は **同じ route 上** に描画され、`?variant=` URL search param で切り替わる。既存の data fetching、params、auth は維持 — 描画だけ差し替え。これがデフォルト。特定の理由がない限りこれを選ぶ。

まだ page がないが *自然に既存 page の中に収まる* prototype（dashboard の新セクション、settings screen の新カード、既存 flow の新ステップ）も sub-shape A。host page 内に variant をマウントする。

### Sub-shape B — 新規 page（最後の手段）

prototype 対象に既存 page が本当にないときだけ — 例: 完全に新しい top-level surface、どこにも埋め込めない flow。

プロジェクトの既存 routing 慣習に従った **throwaway route** を作る — 新しい top-level 構造は発明しない。path や filename に `prototype` を含め、明らかに prototype である名前にする。同じ `?variant=` パターン。

sub-shape B にコミットする前に sanity-check: 本当に埋め込める既存 page がないか? 空の route は、データのある page なら露呈する design 問題を隠す。

両 sub-shape で floating bottom bar は同一。

## プロセス (Process)

### 1. 問いを明文化し N を決める

デフォルトは **3 variants**。5 を超えると根本的に異なるのではなくノイズになる — そこで cap。

prototype の場所かファイル先頭コメントに 1 行で計画を書く:

> "Three variants of the settings page, switchable via `?variant=`, on the existing `/settings` route."

ユーザーが反論に来るかどうかに関わらず有効。

### 2. 根本的に異なる variant を生成する

各 variant を起草。各 variant を次に照らす:

- page の目的とアクセスできる data
- プロジェクトの component library / styling system（TailwindCSS、shadcn、MUI、plain CSS など）
- 明確な exported component 名、例: `VariantA`、`VariantB`、`VariantC`

variant は **構造的に異なる** こと — layout、information hierarchy、primary affordance が違う。色だけ違う 3 つの card grid は UI prototype ではなく wallpaper。2 つが似すぎたら、明示的に「card grid を使うな」ガイダンスで 1 つ作り直す。

### 3. 配線する

route 上に単一の switcher component を作る:

```tsx
// pseudo-code — adapt to the project's framework
const variant = searchParams.get('variant') ?? 'A';
return (
  <>
    {variant === 'A' && <VariantA {...data} />}
    {variant === 'B' && <VariantB {...data} />}
    {variant === 'C' && <VariantC {...data} />}
    <PrototypeSwitcher variants={['A','B','C']} current={variant} />
  </>
);
```

sub-shape A（既存 page）: switcher の上に既存の data fetching をすべて維持。variant ごとに描画される subtree だけ変える。

sub-shape B（新規 page）: `/prototype/<name>` 配下の throwaway route が同じ switcher をマウント。

### 4. floating switcher を構築する

画面下部中央の小さな fixed-position bar、3 要素:

- **Left arrow** — 前の variant に循環（wrap around）
- **Variant label** — 現在の variant key と、variant が name を export していればそれも。例: `B — Sidebar layout`
- **Right arrow** — 次に循環（wrap around）

振る舞い:

- arrow クリックで URL search param を更新（framework の router を使う — Next なら `router.replace`、React Router なら `navigate` など）し、variant を共有可能で reload 安定に
- Keyboard: `←` と `→` でも循環。`<input>`、`<textarea>`、`[contenteditable]` にフォーカスがあるときは arrow key を横取りしない
- page と視覚的に区別（例: high-contrast pill、subtle shadow）— 評価対象の design の一部ではないことが明らか
- production build では非表示 — `process.env.NODE_ENV !== 'production'` または同等の check で gate し、prototype の stray merge で bar がユーザーに出ないようにする

switcher は単一の shared component に置き、両 sub-shape で再利用。プロジェクトの shared UI の場所に配置。

### 5. 引き渡す

URL（と `?variant=` keys）を提示。ユーザーは都合のよいときに行き来する。面白いフィードバックは通常 **「B の header と C の sidebar が欲しい」** — それが本当に欲しい design。

### 6. 答えを記録しクリーンアップ

勝った variant が決まったら、どれでなぜかを記録（commit message、ADR、issue、または AFK でユーザーがまだ応答していなければ prototype 横の `NOTES.md`）。その後:

- **Sub-shape A** — 負け variant と switcher を削除。winner を既存 page に統合。
- **Sub-shape B** — 勝ち variant を本物の route に昇格。throwaway route と switcher を削除。

variant components や switcher を放置しない。すぐ腐り、次の読者を混乱させる。

## アンチパターン (Anti-patterns)

- **色や copy だけ違う variant。** それは tweak であり prototype ではない。本物の variant は構造について意見が分かれる。
- **variant 間でコードを共有しすぎる。** 共有 `<Header>` はよい。共有 `<Layout>` は目的を台無しにする。各 variant は layout を捨てて自由であるべき。
- **variant を本物の mutation に接続する。** read-only prototype で十分。mutation が必要なら stub を指す — 問いは「どう見えるべきか」であり「backend は動くか」ではない。
- **prototype をそのまま production に昇格する。** variant code は prototype 制約（テストなし、最小 error handling）で書かれた。統合するときはきちんと書き直す。

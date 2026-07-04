# In Progress

まだ開発中の skill。出荷準備はできていない — 荒い部分、breaking changes、放棄された実験を想定すること。安定したバケットに昇格するまでは plugin と top-level README から除外される。

- **[wayfinder](./wayfinder/SKILL.md)** — fog に包まれた問題の中に route をチャート化する — 漠然としたアイデアを調査 ticket の map に変え、goal への道筋がはっきりするまで一つずつ解決していく。ユーザー起動 (User-invoked)。
- **[loop-me](./loop-me/SKILL.md)** — 現在の directory を状態を持つ workspace として使い、複数セッションにわたって自分自身を grill し、実装可能な workflow spec に仕上げる。ユーザー起動 (User-invoked)。
- **[wizard](./wizard/SKILL.md)** — 人間を手作業の手順 (setup、一回限りの migration、状態遷移) に沿って案内する対話的な bash wizard を生成する — URL を開き、値を捕捉し、`.env` と GitHub Actions secrets を書き込む。ユーザー起動 (User-invoked)。
- **[writing-beats](./writing-beats/SKILL.md)** — choose-your-own-adventure スタイルで、記事を beat の journey として形作る。starting beat を選び、その beat だけを書き、次へと pivot する — 記事が自然な終わりに達するまで。
- **[writing-fragments](./writing-fragments/SKILL.md)** — heterogeneous な writing の断片である fragment をあなたから掘り出す grilling セッションで、それらを将来の記事の raw material として単一の document に追記する。
- **[writing-shape](./writing-shape/SKILL.md)** — raw material の markdown file を受け取り、各ステップで format の選択を議論しながら段落ごとに記事へと形作る。
- **[claude-handoff](./claude-handoff/SKILL.md)** — 現在の会話を、handoff summary を種にした新しいバックグラウンド agent (`claude --bg` 経由) にすぐに引き渡す。ユーザー起動 (User-invoked)。

# 生産性 (Productivity)

コードに限らない、汎用的なワークフローツール。

## ユーザー起動 (User-invoked)

あなたがタイプした場合にのみ到達可能（`disable-model-invocation: true`）。

- **[grill-me](./grill-me/SKILL.md)** — 計画や設計を洗練するための容赦ないインタビュー。
- **[handoff](./handoff/SKILL.md)** — 現在の会話を、別のエージェントが引き継げるよう handoff document に圧縮する。
- **[teach](./teach/SKILL.md)** — このワークスペース内で、ユーザーに新しい skill や概念を教える。
- **[writing-great-skills](./writing-great-skills/SKILL.md)** — skills を上手く書き・編集するためのリファレンス — skill を予測可能にする語彙と原則。

## モデル起動 (Model-invoked)

モデルとユーザーの両方から到達可能（モデルが自動的に使えるよう豊富なトリガーフレーズを持つ）。

- **[grilling](./grilling/SKILL.md)** — 決定木のあらゆる分岐が解消されるまで、計画や設計についてユーザーを容赦なくインタビューする。`grill-me` と `grill-with-docs` の背後にある再利用可能なループ。

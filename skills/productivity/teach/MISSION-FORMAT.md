# MISSION.md Format

`MISSION.md` は workspace のルートに置かれる。ユーザーがこのトピックを学ぶ _理由_ を記録する。次に何を教えるか、どの resource を提示するか、どんな演習を設計するか — あらゆる教える上での意思決定は、このドキュメントに遡れるべきである。

## テンプレート (Template)

```md
# Mission: {Topic}

## Why
{1-3 sentences. The concrete real-world goal the user is chasing. What changes in their life or work when they have this skill? Avoid abstract framings like "to understand X" — push for the underlying outcome.}

## Success looks like
- {A specific, observable thing the user will be able to do}
- {Another specific thing}
- {…}

## Constraints
- {Time, budget, prior commitments, learning preferences, anything that bounds the approach}

## Out of scope
- {Adjacent topics the user explicitly does not want to chase right now — protects the zone of proximal development}
```

## ルール (Rules)

- **1 ワークスペースにつき 1 つの mission。** ユーザーが無関係な 2 つのことを学びたい場合は、それは 2 つの workspace になる。
- **抽象より具体。** "Run a half marathon by October"（10 月までにハーフマラソンを走る）は "get fitter"（もっと健康になる）に勝る。"Ship a Rust CLI to my team"（チームに Rust の CLI をリリースする）は "learn Rust"（Rust を学ぶ）に勝る。
- **曖昧さには押し返す。** ユーザーが理由をうまく言葉にできない場合は、何かを書く前にインタビューする。悪い mission は mission がないより悪い。
- **現実が変わったら見直す。** mission は変わるものである。ユーザーの目標が変わったら、このファイルを更新する — 古びた mission が今後のセッションを操縦したままにしない。
- **短く保つ。** `MISSION.md` が 1 画面を超えるようなら、それはもう compass であることをやめ、plan になってしまっている。

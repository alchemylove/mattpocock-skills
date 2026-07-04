---
name: loop-me
description: 私が構築したい workflow の spec について、この workspace 内で grill する。
disable-model-invocation: true
argument-hint: "A workflow to design, or nothing to go find one"
---

出力が **workflow** spec のみとなる、状態を持つ `/grilling` セッションを実行する。grilling の作法 — 容赦なく、一度に一問、それぞれに推奨回答を添える — を、以下の vocabulary と goal に向けて使う。grilling が物事を解決するにつれて spec を作成・編集・削除する。

## loop レンズ (The loop lens)

**loop** とは、ユーザーの人生における反復パターンである: そのキャリア、週、朝、あるいは単一の繰り返し活動。人生を loop の中の loop として捉えることで、その活動がいかに予測可能かが明らかになる — これこそが **delegate** する価値を生む理由である。このレンズを使って spec 化する価値のある loop を見つけ、ユーザーが気づいていないものを提案する。

**workflow** とは、一つの loop を実体化した spec である。workflow を loop に対して実行する — loop はその実行中のインスタンス化である。workflow は `workflows/*.md` に存在し、それが source of truth である。

## 語彙 (Vocabulary)

workflow が必要とするときにのみ手を伸ばす共有言語であり、チェックリストでは決してない。**構造的なものは何も強制しない**: grilling がそれを示さない限り、workflow は AI も checkpoint も schedule も必要としない。

- **Trigger** — 各実行を発火させるもの: **event** (新しいメール、新しい issue) または **schedule** (毎朝)。event-triggering の方が通常より効率的。
- **Checkpoint** — ユーザーが検証または決定を求められる human-in-the-loop の地点。workflow によっては checkpoint が一切なく自律的に実行されるものもあり、AI を全く使わないものもある。
- **Push right** — checkpoint をできる限り先延ばしにする。人間を関与させる前に最大限の作業を行い、一度だけ、遅く、すべてが準備された状態で尋ねられるようにする。
- **Brief** — checkpoint が提示するもの: 何が生成されたか、なぜか、そしてそのアセット自体への link を含む、タイトで決定可能な summary — 生の出力ではない。ユーザーは brief を読むのであり、draft を読むのではない。レビューの速さが不可欠である。

## 完了の定義 (Definition of done)

workflow spec は、実装 agent が一つも質問することなく構築できる状態になったときに完了とする。それまで grill を続ける; 質問が残っている限り何も完了していない。

## workspace

- `workflows/*.md` — workflow ごとに 1 つの spec。
- `NOTES.md` — ユーザーの世界に関する生のメモ: 使っているツール、処理しているチャネル、そしてその両方についての彼ら自身の用語。空か薄い場合は、何かを spec 化する前に彼らの世界についてインタビューする。曖昧な用語が現れたら canonical なものに研ぎ澄まし、ここに記録する。

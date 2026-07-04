クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=resolving-merge-conflicts
```

```bash
npx skills update resolving-merge-conflicts
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/resolving-merge-conflicts)

## 何をするか (What it does)

`resolving-merge-conflicts` は進行中の git merge や rebase の衝突を hunk ごとに処理し、その操作を完了させます — 解決し、確認し、コミットまで終えます。

これは**テキストではなく意図**によって解決します。hunk に触れる前に、それぞれの側を**primary source**（コミットメッセージ、PR、元の issue）まで遡り、なぜその変更がなされたのかを理解したうえで、両者の意図が両立する場合はそれを保持します。衝突を覆い隠すために新しい振る舞いを発明することは決してなく、`--abort` に頼ることも決してありません — merge は必ず完了させます。

## いつ使うか (When to reach for it)

`/resolving-merge-conflicts` と入力するか、タスクに合致すればエージェントが自動的に使います。

merge や rebase の途中で、git が自力で解決できない衝突で止まっているときに使ってください。これは目の前にある衝突のためのものであり、merge を計画するためのものでも、その後に壊れた振る舞いをデバッグするためのものでもありません。merge は完了したが、何かが理由の分からない形で失敗し始めた場合は、代わりに [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) を使ってください。

## 意図で解決する

衝突におけるよくある罠は、それをテキストの問題として扱うことです — マーカーを消すために「ours」か「theirs」かを選ぶだけ、というやり方です。この skill はそれを**意図**の問題として扱います。hunk の両側は、誰かが何かを望んだからこそ存在します。解決は可能な限り両方の望みを尊重しなければならず、それが本当に両立しない場合は、merge の掲げる目標に合う方を選び、そのトレードオフを声に出して書き留めます。

だからこそ primary source が重要なのです。読んでいない意図を保持することはできません。作業は diff の中からではなく、履歴 — コミット、PR、チケット — から始まります。

## うまく機能しているかの目安 (It's working if)

- 解決された各 hunk が両側の振る舞いを保持している、あるいは保持できなかった場合はそのトレードオフを明示している。
- どちらのブランチにもなかった新しい振る舞いが現れていない。
- プロジェクト自身のチェック — 型チェック、テスト、フォーマット — が見つかり、コミット前に green で通っている。
- merge や rebase が中断されることなく、最後まで完了したコミットに至っている。

## 全体の中での位置づけ (Where it fits)

いつでも使える standalone です — merge や rebase が行き詰まった瞬間に呼び出し、クリーンでコミット済みのツリーを返してくれます。自然な隣人は [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) です。merge 自体はきれいに解決したのにその後誤動作するなら、それは衝突の問題ではなく診断の問題だからです。どの skill が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が導いてくれます。

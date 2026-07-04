---
name: resolving-merge-conflicts
description: "進行中の git merge/rebase の競合を解消する必要があるときに使う。"
---

1. merge/rebase の**現在の状態を見る**。git history と競合しているファイルを確認する。

2. 各競合について**一次情報源を見つける**。それぞれの変更がなぜ行われたのか、元の意図は何だったのかを深く理解する。commit message を読み、PR を確認し、元の issue/チケットを確認する。

3. **各 hunk を解消する。** 可能な限り両方の意図を保持する。両立しない場合は merge の掲げる目標に合致する方を選び、trade-off を書き留める。新しい振る舞いを**発明しない**。常に解消し、`--abort` は決してしない。

4. プロジェクトの**自動チェック**を見つけて実行する — 通常は typecheck、次にテスト、次に format の順。merge が壊したものを修正する。

5. **merge/rebase を完了する。** すべてを stage して commit する。rebase の場合は、すべての commit が rebase されるまで rebase process を続ける。

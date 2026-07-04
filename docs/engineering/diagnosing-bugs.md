クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=diagnosing-bugs
```

```bash
npx skills update diagnosing-bugs
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)

## 何をするか (What it does)

`diagnosing-bugs` は、手強いバグやパフォーマンスの退行のために規律ある診断ループを実行します — repro を作り、それを最小化し、仮説に優先順位を付け、計装を行い、最後に regression テストとともに修正します。

**tight feedback loop**（このバグに対してすでに red になる、実行可能な1つのコマンド）を得るまでは仮説を立てることを拒否します。そのコマンドが存在する前にコードを読んで理論を組み立てることこそ、この skill が防ごうとしているまさにその失敗です。red にできるループがなければ、診断もありません。

## いつ使うか (When to reach for it)

`/diagnosing-bugs` と入力するか、タスクに合致すればエージェントが自動的に使います — 「diagnose」「debug this」という言葉に反応するほか、何かが壊れている、例外を投げている、失敗している、遅い、と報告したときにも発火します。

手強いもの — 一目見ただけでは解決しないバグ、断続的に発生する flake、既知の良好な2状態の間に紛れ込んだ退行 — に対して使ってください。欠陥を追うのではなく設計上の疑問を手早く確認したいだけなら、代わりに使い捨てのコードで [prototype](https://aihero.dev/skills-prototype) を使ってください。

## Tight loop こそが skill そのもの

signal さえ手に入れば、それ以外のこと — bisection、仮説検証、計装 — はすべて機械的な作業になります。そのためこの skill は、Phase 1 に不釣り合いなほどの労力を注ぎます。実際のバグのコードパスを駆動し、ユーザーが報告した正確な症状をアサートする pass/fail コマンドを組み立て、それが速く、決定的で、エージェントが実行可能になるまで **tightening（引き締める）** のです。30秒かかる flaky なループは、ないのとほとんど変わりません。2秒で決定的に動くループはデバッグの超能力です。

そのループを組み立てるための手段のはしごを与えます — failing test、curl スクリプト、CLI diff、ヘッドレスブラウザ、リプレイされたトレース、使い捨てのハーネス、fuzz ループ、`git bisect run`、differential run — そして最後の手段としてのみ、人間が介在する bash スクリプトです。非決定的なバグに対しては、目標はクリーンな repro ではなく、**より高い再現率**です — トリガーをループさせ、並列化し、flake がデバッグ可能になるまでストレスを加えます。

## うまく機能しているかの目安 (It's working if)

- 理論化する*前に* repro コマンドを組み立てて実行し、その呼び出しと red の出力を貼り付ける。
- ループがアサートするのは実際に報告された症状であり、近くにある別の失敗ではない。
- 仮説は、テストされる前にあなたに提示される、優先順位付けされ反証可能なリストとして届く。
- デバッグ用の計装にはタグ（`[DEBUG-...]`）が付けられ、完了を宣言する前に grep で取り除かれる。

## 全体の中での位置づけ (Where it fits)

`diagnosing-bugs` はいつでも使える standalone です — 何かが壊れた瞬間に飛び込み、修正と regression テストが揃ったら抜け出します。真の発見が「バグを封じ込める良い seam がない — 問題はバグではなくコードそのものだ」ということである場合、その post-mortem は [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) へと引き継がれます。どの skill が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が導いてくれます。

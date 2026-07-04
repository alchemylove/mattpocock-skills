# hard dependency に限り明示する `/setup-matt-pocock-skills` の pointer

Engineering skills は、`/setup-matt-pocock-skills` によって種付けされるリポジトリごとの設定（issue tracker、triage ラベルの語彙、domain doc のレイアウト）に依存している。skill の中には、その設定なしでは意味のある形で機能できないものがある — 特定の issue tracker に公開したり、特定のラベル文字列を適用したりする必要があるからだ。一方、出力を研ぎ澄ますためだけに使う（語彙、ADR の把握）skill もあり、それらは設定がなくても degrade しつつ動作する。

そこでこれらを **hard-dependency** と **soft-dependency** の skill に分けている:

- **Hard dependency**（`to-issues`、`to-prd`、`triage`） — 明示的な一文を含める: _「… があなたに提供されているはずだ — もしなければ `/setup-matt-pocock-skills` を実行せよ」_。このマッピングがなければ、出力は曖昧になるどころか誤りになる。
- **Soft dependency**（`diagnose`、`tdd`、`improve-codebase-architecture`） — 「プロジェクトの domain glossary」や「触れている領域の ADR」を、あいまいな散文の中で参照するにとどめる。ドキュメントが存在しなくても skill は機能する。ただ出力の鋭さが落ちるだけだ。

この分割により、soft-dependency の skill はトークンを軽く保て、setup pointer が load-bearing でない場所にまで cargo-cult 的に持ち込まれるのを避けられる。

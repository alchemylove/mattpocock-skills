# hard dependencies にのみ明示的 `/setup-matt-pocock-skills` pointer (Explicit `/setup-matt-pocock-skills` pointer only for hard dependencies)

Engineering skills は `/setup-matt-pocock-skills` が seed する per-repo config（issue tracker、triage label vocabulary、domain doc layout）に依存します。一部の skills はその config なしでは意味fully 機能できません — 特定の issue tracker へ publish したり、特定の label string を apply する必要があります。他は output を sharpen する（vocabulary、ADR awareness）用途のみで、なければ gracefully に degrade します。

これらを **hard-dependency** と **soft-dependency** skills に分けます:

- **Hard dependency**（`to-issues`、`to-prd`、`triage`）— 明示的 one-liner を含める: _"… should have been provided to you — run `/setup-matt-pocock-skills` if not."_ mapping がなければ output は fuzzy ではなく wrong になる。
- **Soft dependency**（`diagnose`、`tdd`、`improve-codebase-architecture`、`zoom-out`）— "the project's domain glossary" と "ADRs in the area you're touching" を vague prose のみで参照。docs がなけても skill は動く；output は just less sharp。

この split により soft-dependency skills は token-light のまま、load-bearing でない場所への setup pointer の cargo-culting を避けます。

# Matt Pocock Skills コレクション (Matt Pocock Skills)

Claude Code が load する agent skills（slash commands と behaviors）のコレクション。skills は bucket に整理され、`/setup-matt-pocock-skills` が emit する per-repo configuration によって consume されます。

## 言語 (Language)

**Issue tracker**:
repo の issues を host するツール — GitHub Issues、Linear、local `.scratch/` markdown convention、または類似のもの。`to-issues`、`to-prd`、`triage`、`qa` などの skills は、ここから read し、ここへ write します。
_Avoid_: backlog manager, backlog backend, issue host

**Issue**:
**Issue tracker** 内の単一 tracked unit of work — bug、task、PRD、または `to-issues` が produce する slice。
_Avoid_: ticket（外部 system が ticket と呼ぶ場合の quote のみ）

**Triage role**:
triage 中に **Issue** に適用される canonical state-machine label（例: `needs-triage`、`ready-for-afk`）。各 role は `docs/agents/triage-labels.md` 経由で **Issue tracker** 内の実 label string に map されます。

## 関係 (Relationships)

- 1 つの **Issue tracker** は多数の **Issues** を保持する
- 1 つの **Issue** は、常に 1 つの **Triage role** を持つ

## 曖昧さのフラグ (Flagged ambiguities)

- 以前 "backlog" は issues を host する *tool* と、その中の *body of work* の両方を指していた — 解決: tool は **Issue tracker**；"backlog" は domain term としては使わない。
- "backlog backend" / "backlog manager" — 解決: **Issue tracker** に統合。

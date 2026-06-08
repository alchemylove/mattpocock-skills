# issue tracker integrations は mainstream ツールに限定 (Issue tracker integrations are limited to mainstream tools)

`setup-matt-pocock-skills` は **mainstream** issue trackers のみ first-class support を提供します。niche、new、または single-vendor experimental trackers の support 追加要求は out of scope です。

## out of scope である理由 (Why this is out of scope)

各 issue-tracker backend は CLI shape（commands、flags、output parsing）を skills に hard-code します。新 backend ごとに permanent maintenance surface が増える — tool の CLI が evolve しても動き続け、`/to-prd`、`/to-issues`、`/triage` などで test し続ける必要があります。その cost は、meaningful fraction の users が実際に持っている trackers に対してのみ worth paying です。

"Mainstream" は numeric bar ではなく judgment call です:

- GitHub、GitLab、Backlog.md は mainstream と見なす類の tool — broadly known、widely used、experimental phase を well past。
- GitHub stars が数百の brand-new agent-focused tool は、design がどれほど interesting でも mainstream ではない。

Stars、age、download counts は call を下す際の useful signals だが、どれも rule ではない。rule は: typical engineer がこの tool を recognise し、team のために plausibly 選んだか？

non-mainstream trackers 向け escape hatch は既にある:

- lightweight in-repo tracking 向け `local markdown`。
- 自分で wire up したい users 向け `other/custom`。

どちらも core skills が specific tool を知る必要はない。

## 過去の要求 (Prior requests)

- #99 — "Add dex as an issue tracker backend"（要求時点で dex は ~3 ヶ月、~300 stars）

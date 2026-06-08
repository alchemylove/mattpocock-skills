# `setup-matt-pocock-skills` の Verify/Check Mode

この project は `setup-matt-pocock-skills` 向け dedicated verify/check mode（または separate verify skill）を add しません。

## out of scope である理由 (Why this is out of scope)

`docs/agents/*.md` artifacts が seed-template schema と still match するか check する second skill — または `--verify` flag — は、existing setup skill が conversation で既に handle する work を duplicate します。

intended workflow: **`/setup-matt-pocock-skills` を run し、current setup を verify するよう指示する。** skill は prompt-driven なので maintainer は verification pass に scope できる（"don't rewrite anything, just check my existing files against the current seed templates and report drift"）— separate code path 不要。flag や sibling skill を add すると、natural-language entry point で既に expressible な feature の surface area が split される。

configuration management を single skill に keep することで、seed templates が evolve した際に 2 skills が互いに drift する maintenance cost も避けられる。

## 過去の要求 (Prior requests)

- #106 — Feature request: verify/check mode for setup-matt-pocock-skills

---
name: claude-handoff
description: 現在の会話を、作業をすぐに引き継ぐ新しいバックグラウンド agent に引き渡す。
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

現在の会話の handoff summary を書き、新しい agent が作業を引き継げるようにする。保存する代わりに、その summary を prompt としてバックグラウンド agent を起動する: `claude --bg --name "<descriptive name>" "<handoff summary>"`。これは現在の working directory で開始し、即座に返る。ユーザーは `claude agents` でこれを管理する。

常に `-n`/`--name` に説明的な名前を渡す (例: `--name "Fix login bug"`) — job list、session picker、terminal title に表示される display name になる。

summary には "suggested skills" セクションを含め、agent が呼び出すべき skill を提案する。

他のアーティファクト (PRD、plan、ADR、issue、commit、diff) に既に記録されている内容は重複させない。パスまたは URL で参照する。

API keys、パスワード、個人を特定できる情報などの機密情報は redact する — この summary は agent の prompt になる。

ユーザーが引数を渡した場合、次のセッションが何に焦点を当てるかの説明として扱い、summary をそれに合わせて調整する。

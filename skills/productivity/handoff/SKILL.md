---
name: handoff
description: 現在の会話を、別のエージェントが引き継げるよう handoff document に圧縮する。
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

現在の会話を要約した handoff ドキュメントを書き、新しい agent が作業を引き継げるようにする。ユーザーの OS の一時ディレクトリに保存する — 現在の workspace ではない。

ドキュメントには "suggested skills" セクションを含め、agent が呼び出すべき skill を提案する。

他のアーティファクト (PRD、plan、ADR、issue、commit、diff) に既に記録されている内容は重複させない。パスまたは URL で参照する。

API keys、パスワード、個人を特定できる情報などの機密情報は redact する。

ユーザーが引数を渡した場合、次のセッションの焦点として扱い、ドキュメントをそれに合わせて調整する。

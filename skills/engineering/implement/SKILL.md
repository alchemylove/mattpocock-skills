---
name: implement
description: "PRD または一連の issue に基づいて、一区切りの作業を実装する。"
disable-model-invocation: true
---

PRD または issues でユーザーが説明した作業を実装する。

事前に合意した seam で、可能な限り /tdd を使う。

typechecking をこまめに、単体のテストファイルもこまめに実行し、最後に一度 full test suite を実行する。

完了したら /code-review を使って作業をレビューする。

作業を現在の branch に commit する。

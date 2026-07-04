---
name: research
description: 信頼度の高い一次情報源に基づいて疑問を調査し、結果をリポジトリ内の Markdown ファイルとして記録する。ユーザーがトピックの調査、ドキュメントや API の事実確認、または調べものをバックグラウンドの agent に任せたいときに使う。
---

**background agent** を立ち上げて research を行わせ、それが読んでいる間も作業を続ける。

その仕事:

1. **primary sources** — 公式ドキュメント、ソースコード、spec、first-party API — に基づいて疑問を調査する。それらの二次的な書き起こしではない。すべての主張を、それを owns する source まで遡って辿る。
2. 各主張の source を引用しながら、findings を単一の Markdown ファイルに書く。
3. repo がすでにそうしたメモを保管している場所に保存する。既存の convention に合わせ、無ければ適切な場所に置いてどこに置いたか伝える。

# モデル起動 (Model-invoked) と ユーザー起動 (User-invoked)

このリポジトリ内のすべての `SKILL.md` は skill である。それらを分ける唯一の軸が **invocation**（誰が到達できるか）である:

- **User-invoked** — **人間がその名前をタイプした場合にのみ**到達可能。frontmatter に `disable-model-invocation: true` を設定する。`description` は**人間向け**: スラッシュコマンドを眺める人が読む一行サマリー。トリガーの列挙（"Use when the user says…" のような）は取り除く。
- **Model-invoked** — **モデルまたはユーザー**が到達可能。デフォルトはこちらで、`disable-model-invocation` を省略する。`description` は**モデル向け**で、auto-invocation が発火するように豊富なトリガー表現（"Use when the user wants…, mentions…, asks for…" のような）を維持する。ある skill を model-invoked のままにすべきかどうかのテストは: _モデルがこれを自律的に有用に呼び出せるか?_ である（再利用可能性は skill を切り出す理由であって、そのテストではない）。

user-invoked skill には description がないため、人間以外は到達できない — 他のどの skill もそれを発火できない。したがって user-invoked skill は model-invoked skill を呼び出せるが、別の user-invoked skill には決して到達できない。

bucket の `README.md` 群とトップレベルの `README.md` は、エントリを **User-invoked** と **Model-invoked** にグループ分けする。

## それらの間の依存関係 (Dependencies between them)

依存関係は、深い `../other-skill/FILE.md` 形式の相互参照ではなく、**`/skill` 形式の散文的な呼び出し**（"Run the `/grilling` skill" のような）として表現される。共有される reference doc は、それを所有する skill の内部に置かれる。他の skill は、フォルダをまたいでリンクするのではなく、その skill を呼び出すことでその内容にアクセスする。

## 受動的な domain work と能動的な domain work (Passive vs active domain work)

語彙のために `CONTEXT.md` を単に_読む_ことは一行の散文的なポインタに過ぎず、`domain-modeling` skill ではない。能動的な構築・研ぎ澄ましの規律（用語を検証する、エッジケースのシナリオを作る、ADR を書く、`CONTEXT.md` をその場で更新する）だけが `domain-modeling` である。

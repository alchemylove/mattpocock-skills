---
name: prototype
description: 設計上の疑問に答えるための使い捨てプロトタイプを作る。ユーザーが state model やロジックが正しく感じられるか確認したい、または UI がどう見えるべきか探りたいときに使う。
---

# プロトタイプ (Prototype)

prototype は **質問に答える throwaway code** である。質問が形を決める。

## ブランチの選択 (Pick a branch)

答える質問を特定する — ユーザーの prompt、周辺コード、またはユーザーがいる場合は尋ねる:

- **"Does this logic / state model feel right?"** → [LOGIC.md](LOGIC.md)。紙では reasoning しにくい case を state machine が通る tiny interactive terminal app を構築する。
- **"What should this look like?"** → [UI.md](UI.md)。1 つの route 上に radically different な UI variation を複数生成し、URL search param と floating bottom bar で切り替え可能にする。

2 つの branch は非常に異なる artifact を生む — ここを間違えると prototype 全体が無駄になる。質問が genuinely ambiguous でユーザーに届かない場合、周辺コードに better match する branch を default とし（backend module → logic; page または component → UI）、prototype の先頭で assumption を述べる。

## 両方に適用されるルール (Rules that apply to both)

1. **初日から throwaway とし、明確にマークする。** prototype code は実際に使われる場所の近く（prototype 対象の module または page の隣）に置き context を明確にする — ただし casual reader が production ではなく prototype と分かる名前にする。throwaway UI route はプロジェクトの既存 routing convention に従う; 新しい top-level structure を invent しない。
2. **実行は 1 コマンド。** プロジェクトの既存 task runner が対応するもの — `pnpm <name>`、`python <path>`、`bun <path>` など。ユーザーが考えずに起動できること。
3. **デフォルトで persistence なし。** state は memory にある。persistence は prototype が _検証している_ ものであり、prototype が依存すべきものではない。質問が明示的に database を含む場合、scratch DB または "PROTOTYPE — wipe me" と明記した local file を使う。
4. **polish は skip。** test なし、prototype を _runnable_ にする以上の error handling なし、abstraction なし。目的は素早く学び、削除すること。
5. **state を surface する。** 各 action の後（logic）または各 variant 切り替え時（UI）に、関連する state 全体を print または render し、何が変わったかユーザーが見えるようにする。
6. **完了時は削除または吸収。** prototype が質問に答えたら、削除するか validated decision を real code に fold する — repo に腐らせて置かない。

## 完了時 (When done)

prototype から keep する価値があるのは _answer_ だけである。どこか durable な場所（commit message、ADR、issue、または prototype 横の `NOTES.md`）に、答えた質問とともに capture する。ユーザーがいれば capture は短い会話; いなければ placeholder を残し、削除前に verdict を埋められるようにする（ユーザーまたは次の pass の自分）。

---
name: wizard
description: 人間を手作業の手順 — third-party setup、一回限りの migration、A→B の状態遷移 — に沿って案内する対話的な bash wizard を生成する。URL を開き、値を捕捉し、各ステップを確認し、.env ファイルと GitHub Actions secrets を書き込む。
disable-model-invocation: true
---

# Wizard

**wizard** とは、手作業で行うには面倒で、毎回 AI に再説明するのも面倒な手作業の手順を、人間にステップバイステップで案内する bash script である。各 URL を開き、何をクリックし何をコピーすべきかを正確に伝え、値を捕捉し、それらをあるべき場所 (`.env`、GitHub secrets) に書き込み、各段階で確認を取り、残りどれくらいかを示す。third-party サービスを設定したり、一回限りの migration を実行したり、project をある状態から別の状態へ移したりするのに使える。

心地よい UX はすでに [template.sh](template.sh) によって解決されている — 残り時間付きの progress、confirmation gate、クロスプラットフォームな URL open (WSL を含む)、hidden な secret entry、冪等な `.env` upsert、`gh secret`/`gh variable` への書き込み、そして closing summary。**あなたの仕事は、手順のスコープを決め、その stage を書くことだけ**。`STAGES` マーカーより上の library はすべての wizard で同一である; その一貫性こそが要点であり、決して手で編集しない。

wizard はデフォルトでは ephemeral である — 一回の実行のために作られ、scratch か `scripts/` パスに保存され、job が終わったら削除される。ユーザーが repo に置いておくべき再現可能な setup path を望む場合にのみ commit する。

## 手順 (Process)

### 1. 手順のスコープを決める (Scope the procedure)

人間が取らなければならないすべての手作業ステップと、その過程で捕捉されるすべての値を洗い出す。まず repo を読む — いきなり質問しない:

- setup の場合: `.env`、`.env.example`、`.env.*`、`README`、`docker-compose*`、framework config、`.github/workflows/*` (`secrets.*` / `vars.*` への参照はすべて、wizard が生成しなければならない値である)。
- migration や transition の場合: 現在の状態、目標の状態、そしてその間の不可逆な action。

その後、順序付けられた stage のリストと各 stage が生成する値をユーザーに示し、確認する — 彼らは追加、削除、並べ替えができる。

**完了の条件:** すべての stage が順序通りに名付けられており、捕捉される各値について (a) 人間がどこでそれを得るか、(b) それがどこに書き込まれるか (`.env`、GitHub secret、その両方、あるいはどこにも書かれない — 純粋な action のみの stage もある)、(c) それが secret (hidden entry) か public かが分かっていること。

### 2. 各 stage の journey を map する (Map each stage's journey)

各 stage について、人間が辿る正確な path を書く: どの URL を開くか、そこで何をするか、値がどこに表示されるか、それがどの変数を埋めるか — 例えば「Dashboard → Developers → API keys → Reveal test key → copy」。現在の UI や正確な command を実際には知らない場合は、その旨を明示してユーザーに尋ねるか docs を確認する — 存在しないかもしれないステップを決して捏造しない。

**完了の条件:** すべての stage が、見知らぬ人でも従える具体的な instruction まで辿れること。

### 3. wizard を書く (Author the wizard)

`template.sh` を目的の path にコピーする。example stage を、依存順に並んだステップごとの `stage` に置き換える。library の helper — `stage`、`say`/`step`、`open_url`、`ask`/`ask_secret`、`write_env`、`set_secret`/`set_var`、`pause`/`confirm` — を使い、`TOTAL_STAGES` と `TOTAL_MINUTES` に正直な見積もりを設定する (これが残り時間表示を駆動する)。

template が定める基準を守る: 値を尋ねる前に URL を開く、secret なものには `ask_secret` を使う、永続化するすべての値に `write_env` を使う、CI が実際に必要とする値だけに `set_secret` を使う、そして不可逆な action の前には `confirm` する。各 `stage` は画面をクリアするので現在のステップだけが見える — 人間が必要とするものがスクロールで消えないよう、一つの stage は一つの集中したタスクに留める。マーカーより上の library には触れない。

### 4. 検証して引き渡す (Verify and hand off)

- `bash -n <script>`; 利用可能なら `shellcheck` を実行する。
- `chmod +x <script>`。
- 自分でエンドツーエンドに実行しない — browser を開き、人間の入力でブロックする。代わりに静的にトレースする: ステップ 1 のすべての値が捕捉され、ステップ 1 で述べた場所に収まっていること、そしてすべての `set_secret` の名前が CI 内の `secrets.*` 参照と正確に一致していること。
- ユーザーにそれをどう実行するか伝える。それが再現可能な setup path であれば、commit して README から link し、次の人が AI に尋ねる代わりにその script を実行できるようにする。

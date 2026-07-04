クイックスタート (Quickstart):

```bash
npx skills add mattpocock/skills --skill=setup-matt-pocock-skills
```

```bash
npx skills update setup-matt-pocock-skills
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/setup-matt-pocock-skills)

## 何をするか (What it does)

`setup-matt-pocock-skills` は、あるリポジトリに対して、そこでエンジニアリング skill 群がどう振る舞うべきかを教えます — issue はどこにあるか、triage ラベルは何と呼ばれているか、ドメイン docs はどこにあるか — そしてそれらの答えを、他の skill が読み込む**設定**として記録します。

これは設定を書き込むのであって、振る舞いをハードコードするのではありません。エンジニアリング chain は `docs/agents/` 配下に3つのファイルが存在することを前提としています。この skill は、あなたの実際のリポジトリ（`git remote`、既存のラベル、既存の `CONTEXT.md`）から発見し、推測するのではなくあなたと確認しながら、それらを一度きり生成するブートストラップです。プロンプト駆動です — 探索し、見つけたものを提示し、確認し、それから書き込みます。決定的なひな形生成ではありません。

## いつ使うか (When to reach for it)

これは `/setup-matt-pocock-skills` と入力して呼び出します — エージェントが自発的にこれを使うことはありません。

**リポジトリごとに一度、他のどのエンジニアリング skill を初めて使う前にも**使ってください。[triage](https://aihero.dev/skills-triage)、[to-prd](https://aihero.dev/skills-to-prd)、[to-issues](https://aihero.dev/skills-to-issues) が issue の置き場所を推測し始めたり、存在しないラベルを適用し始めたりしたら、ここでまだセットアップされていないということです。issue tracker を切り替えたり、最初からやり直したりする場合にのみ再実行してください — 日々の微調整は `docs/agents/*.md` を直接編集するだけで済みます。

## 3つの決定事項

一度に1つずつ、平易な言葉での説明を添えて（用語をすでに知っている前提を置きません）3つの選択を案内します。

- **Issue tracker** — 作業がどこで追跡されるか。`triage`/`to-prd`/`to-issues` が `gh` を呼ぶか、`glab` を呼ぶか、`.scratch/` 配下に markdown を書くか、あるいはあなたが説明する workflow に従うかを決めます。GitHub、GitLab、ローカル markdown、その他。
- **Triage labels** — 5つの正典的な役割（`needs-triage`、`needs-info`、`ready-for-agent`、`ready-for-human`、`wontfix`）の背後にある文字列を、あなたが実際に設定したラベルにマッピングし、`triage` が重複を作るのではなく本物のラベルを適用できるようにします。
- **Domain docs** — リポジトリが単一の `CONTEXT.md` を持つのか、マルチコンテキストのマップを持つのかを決め、ドメイン言語を読む skill が正しい場所を見るようにします。

出力は3つのファイル — `docs/agents/issue-tracker.md`、`docs/agents/triage-labels.md`、`docs/agents/domain.md` — に加えて、リポジトリがすでに使っている `CLAUDE.md` / `AGENTS.md` のどちらかに、それらを指す `## Agent skills` ブロックです。これらのファイルは、ツールキットの残りが依って立つ共有基盤です。

## うまく機能しているかの目安 (It's working if)

- `docs/agents/` 配下に3つのファイルが置かれ、あなたの `CLAUDE.md` や `AGENTS.md` に `## Agent skills` セクションが現れる。
- 提案された tracker があなたの実際の `git remote` と一致し、ラベルがリポジトリにすでに存在する文字列と一致する。
- その後、`triage` と `to-issues` が尋ねたり推測したりすることなく、正しい場所で正しいラベルを使って動作する。

## 全体の中での位置づけ (Where it fits)

`setup-matt-pocock-skills` は**一度きりのセットアップ**です — 繰り返すステップではなく、エンジニアリング skill 群全体が依って立つ土台です。隣人は、ここで書かれたものを読む skill です — ここで設定されたラベル語彙を適用する [triage](https://aihero.dev/skills-triage)、そしてここで設定された issue tracker に公開する [to-prd](https://aihero.dev/skills-to-prd) / [to-issues](https://aihero.dev/skills-to-issues) です。最初にこれを実行してください。下流のすべてがそれを前提としています。どの skill や flow が合うか迷ったときは、[ask-matt](https://aihero.dev/skills-ask-matt) が導いてくれます。

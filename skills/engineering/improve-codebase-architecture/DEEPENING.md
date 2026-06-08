# 深化 (Deepening)

依存関係を踏まえ、shallow modules のクラスタを安全に深める方法。[LANGUAGE.md](LANGUAGE.md) の語彙 — **module**、**interface**、**seam**、**adapter** — を前提とする。

## 依存関係のカテゴリ (Dependency categories)

深化候補を評価するとき、依存関係を分類する。カテゴリは deepened module が seam をまたいでどうテストされるかを決める。

### 1. In-process

Pure computation、in-memory state、I/O なし。常に deepenable — modules をマージし、新しい interface 経由で直接テスト。adapter 不要。

### 2. Local-substitutable

ローカル test stand-in がある依存関係（Postgres 用 PGLite、in-memory filesystem）。stand-in が存在すれば deepenable。deepened module は test suite で stand-in を動かしてテスト。seam は internal。module の external interface に port は不要。

### 3. Remote but owned (Ports & Adapters)

network boundary をまたぐ自分の services（microservices、internal APIs）。seam に **port**（interface）を定義。deep module が logic を所有。transport は **adapter** として注入。tests は in-memory adapter。production は HTTP/gRPC/queue adapter。

推奨の形: *"seam に port を定義し、production 用 HTTP adapter と testing 用 in-memory adapter を実装し、network をまたいで deploy されていても logic は 1 つの deep module に置く。"*

### 4. True external (Mock)

制御できない third-party services（Stripe、Twilio など）。deepened module は外部依存を injected port として受け取る。tests は mock adapter を提供。

## シーム規律 (Seam discipline)

- **One adapter means a hypothetical seam. Two adapters means a real one.** 少なくとも 2 つの adapter が正当化される（通常 production + test）まで port を導入しない。single-adapter seam は indirection に過ぎない。
- **Internal seams vs external seams.** deep module は internal seams（implementation 内 private、自分の tests が使う）と external seam（interface にある）の両方を持ち得る。tests が使うからといって internal seams を interface 経由で露出しない。

## テスト戦略: 重ねず置き換える (Testing strategy: replace, don't layer)

- shallow modules の古い unit tests は、deepened module の interface での tests が存在すれば無駄 — 削除する。
- deepened module の interface で新しい tests を書く。**interface is the test surface**。
- tests は interface 経由の observable outcomes を assertion する。internal state ではない。
- tests は internal refactor 後も生き残るべき — behavior を記述し implementation ではない。implementation が変わったときに test も変わる必要があるなら、interface を越えてテストしている。

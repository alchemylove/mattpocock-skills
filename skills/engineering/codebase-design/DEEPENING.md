# Deepening

依存関係を踏まえて、shallow な module の cluster を安全に deepen する方法。[SKILL.md](SKILL.md) の vocabulary — **module**、**interface**、**seam**、**adapter** — を前提とする。

## Dependency categories

deepening の候補を評価するとき、その依存関係を分類する。この category が、深められた module がその seam を越えてどうテストされるかを決める。

### 1. In-process

純粋な計算、in-memory な state、I/O 無し。常に deepen 可能 — module をマージし、新しい interface を通して直接テストする。adapter は不要。

### 2. Local-substitutable

ローカルなテスト用代替物がある依存関係（Postgres に対する PGLite、in-memory filesystem）。代替物が存在すれば deepen 可能。深められた module は test suite の中で代替物を動かしてテストされる。seam は内部にあり、module の external interface に port は無い。

### 3. Remote but owned（Ports & Adapters）

network 境界を越えた自分自身の services（microservices、internal API）。seam に **port**（interface）を定義する。deep module が logic を所有し、transport は **adapter** として注入される。テストは in-memory な adapter を使う。production は HTTP/gRPC/queue な adapter を使う。

推奨の形: *"seam に port を定義し、production 用の HTTP adapter とテスト用の in-memory adapter を実装することで、network をまたいでデプロイされていても logic は 1 つの deep module に収まる。"*

### 4. True external（Mock）

自分が制御できないサードパーティの services（Stripe、Twilio など）。深められた module は external な依存を注入された port として受け取り、テストは mock adapter を提供する。

## Seam discipline

- **Adapter が 1 つなら hypothetical な seam。Adapter が 2 つなら本物の seam。** 少なくとも 2 つの adapter が正当化される（典型的には production + test）のでなければ、port を導入しない。単一 adapter の seam は単なる間接化に過ぎない。
- **Internal seam と external seam。** deep module は、その interface における external seam に加えて、internal seam（その implementation に private で、自身のテストが使う）を持つこともある。テストがそれを使うからといって、internal seam を interface 経由で公開しない。

## Testing strategy: replace, don't layer

- shallow な module に対する古い unit test は、深められた module の interface でのテストが存在するようになった時点で無駄になる — 削除する。
- 深められた module の interface で新しいテストを書く。**interface がテストの表面である。**
- テストは internal state ではなく、interface を通した観測可能な結果を assert する。
- テストは internal な refactor を生き延びるべきである — behaviour を記述するのであり、implementation を記述するのではない。implementation が変わったときにテストも変えなければならないなら、それは interface を超えてテストしている。

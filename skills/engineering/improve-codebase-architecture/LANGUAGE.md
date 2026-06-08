# 用語 (Language)

この skill が行うすべての提案で共有する語彙。これらの用語を正確に使う — "component"、"service"、"API"、"boundary" で置き換えない。一貫した language こそが目的のすべて。

## 用語 (Terms)

**Module**
interface と implementation を持つあらゆるもの。意図的に scale-agnostic — function、class、package、tier をまたぐ slice に等しく適用される。
_Avoid_: unit, component, service.

**Interface**
caller が module を正しく使うために知る必要があるすべて。type signature を含むが、invariants、ordering constraints、error modes、required configuration、performance characteristics も含む。
_Avoid_: API, signature (too narrow — those refer only to the type-level surface).

**Implementation**
module の内側 — その code body。**Adapter** とは区別: 小さな adapter に大きな implementation（Postgres repo）があり得るし、大きな adapter に小さな implementation（in-memory fake）があり得る。seam が話題なら "adapter"、それ以外は "implementation"。

**Depth**
interface における leverage — caller（または test）が学ぶべき interface の単位あたりに exercise できる behavior の量。多くの behavior が小さな interface の背後にある module は **deep**。interface が implementation とほぼ同じくらい複雑な module は **shallow**。

**Seam** _(from Michael Feathers)_
その場所を編集せずに behavior を変えられる場所。module の interface が存在する *location*。seam をどこに置くかは、背後に何を置くかとは別の design decision。
_Avoid_: boundary (overloaded with DDD's bounded context).

**Adapter**
seam で interface を満たす concrete なもの。*role*（どの slot を埋めるか）を記述し、*substance*（中身）ではない。

**Leverage**
depth から caller が得るもの。学ぶべき interface の単位あたりにより多くの capability。1 つの implementation が N call sites と M tests に還元される。

**Locality**
depth から maintainer が得るもの。change、bugs、knowledge、verification が callers に散らばるのではなく 1 か所に集中。1 回直せば、どこでも直る。

## 原則 (Principles)

- **Depth は implementation ではなく interface の性質。** deep module は内部で小さく mockable で swappable な parts から構成され得る — それらは interface の一部ではない。module は **internal seams**（implementation 内 private、自分の tests が使う）と **external seam**（interface にある）の両方を持ち得る。
- **The deletion test.** module を削除すると想像する。complexity が消えるなら、module は何も隠していなかった（pass-through だった）。complexity が N callers に再出現するなら、module は存在価値があった。
- **The interface is the test surface.** callers と tests は同じ seam を越える。interface を *越えて* テストしたいなら、module の形がおそらく間違っている。
- **One adapter means a hypothetical seam. Two adapters means a real one.** 実際に何かが seam をまたいで変わるのでなければ seam を導入しない。

## 関係 (Relationships)

- **Module** は正確に 1 つの **Interface** を持つ（callers と tests に提示する surface）。
- **Depth** は **Module** の性質で、**Interface** に対して測定される。
- **Seam** は **Module** の **Interface** が存在する場所。
- **Adapter** は **Seam** にあり **Interface** を満たす。
- **Depth** は caller に **Leverage** を、maintainer に **Locality** を生む。

## 却下した枠組み (Rejected framings)

- **Depth as ratio of implementation-lines to interface-lines**（Ousterhout）: implementation を水増しする。depth-as-leverage を使う。
- **"Interface" as the TypeScript `interface` keyword or a class's public methods**: 狭すぎる — ここでの interface は caller が知るべきすべての事実を含む。
- **"Boundary"**: DDD の bounded context と overloaded。**seam** または **interface** と言う。

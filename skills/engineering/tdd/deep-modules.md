# Deep Modules

"A Philosophy of Software Design" より:

**Deep module** = 小さな interface + 多くの implementation

```
┌─────────────────────┐
│   Small Interface   │  ← Few methods, simple params
├─────────────────────┤
│                     │
│                     │
│  Deep Implementation│  ← Complex logic hidden
│                     │
│                     │
└─────────────────────┘
```

**Shallow module** = 大きな interface + 少ない implementation（避ける）

```
┌─────────────────────────────────┐
│       Large Interface           │  ← Many methods, complex params
├─────────────────────────────────┤
│  Thin Implementation            │  ← Just passes through
└─────────────────────────────────┘
```

interface を設計するとき、次を問う:

- methods の数を減らせるか?
- parameters を単純化できるか?
- 内部にもっと complexity を隠せるか?

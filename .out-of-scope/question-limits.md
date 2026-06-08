# grilling 中の question 数に hard limits (Hard limits on the number of questions during grilling)

`/grill-me` skill（および他 skills 内の grilling sessions）は question の maximum 数を enforce しない。configurable cap や hard ceiling 追加の要求は out of scope です。

## out of scope である理由 (Why this is out of scope)

Grilling は intentionally open-ended です。point は decision tree の各 branch が resolve するまで dig し続けること — ある plan は 3 questions、ある plan は 50 必要。fixed cap は hard problems で useful exploration を cut off するか、easy ones で arbitrary に feel します。

session が長すぎると feel する場合、right escape hatch は既にある:

- user はいつでも session を stop し、plan の current state を accept できる。
- user は model に wrap up、summarise、move on を指示できる — natural-language steering が intended control surface であり、numeric limit ではない。

hard cap を add すると 2 つの異なる failure modes が conflate される: plan が genuinely under-specified なため questions が多い model（working as intended）vs. redundant または low-value questions を ask する model（prompt-quality issue であり quantity issue ではない）。後者の fix は skill prompt に属し、counter ではない。

## 過去の要求 (Prior requests)

- #44 — "Codex just asked me 200 questions"

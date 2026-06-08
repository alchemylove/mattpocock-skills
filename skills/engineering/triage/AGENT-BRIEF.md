# Agent Brief の書き方 (Writing Agent Briefs)

agent brief は、issue が `ready-for-agent` に移ったときに GitHub issue に投稿する構造化コメント。AFK agent が作業する際の authoritative specification である。元の issue body と discussion は context — agent brief が contract。

## 原則 (Principles)

### 精度より耐久性 (Durability over precision)

issue は `ready-for-agent` に数日〜数週間置かれることがある。その間 codebase は変わる。ファイルが rename、移動、refactor されても brief が有用なままになるよう書く。

- **Do** interfaces、types、behavioral contracts を記述する
- **Do** agent が探す・変更すべき具体的な types、function signatures、config shapes を名指しする
- **Don't** file paths を参照する — すぐ古くなる
- **Don't** line numbers を参照する
- **Don't** 現在の implementation 構造が同じままであると仮定する

### 手順ではなく振る舞い (Behavioral, not procedural)

システムが **what** すべきかを記述し、**how** を実装する方法は書かない。agent は codebase を新鮮に探索し、自分で implementation 判断をする。

- **Good:** "`SkillConfig` type は optional な `schedule` field（type `CronExpression`）を受け付けるべき"
- **Bad:** "`src/types/skill.ts` を開き、42 行目に schedule field を追加"
- **Good:** "ユーザーが引数なしで `/triage` を実行したとき、注意が必要な issues の summary が見えるべき"
- **Bad:** "main handler function に switch statement を追加"

### 完全な acceptance criteria

agent は完了条件を知る必要がある。すべての agent brief に具体的でテスト可能な acceptance criteria を含める。各 criterion は独立して検証可能であること。

- **Good:** "`gh issue list --label needs-triage` を実行すると、初期分類を経た issues が返る"
- **Bad:** "Triage が正しく動くべき"

### 明示的な scope 境界

out of scope を明記する。agent が gold-plating したり、隣接 feature について勝手に仮定するのを防ぐ。

## テンプレート (Template)

```markdown
## Agent Brief

**Category:** bug / enhancement
**Summary:** one-line description of what needs to happen

**Current behavior:**
Describe what happens now. For bugs, this is the broken behavior.
For enhancements, this is the status quo the feature builds on.

**Desired behavior:**
Describe what should happen after the agent's work is complete.
Be specific about edge cases and error conditions.

**Key interfaces:**
- `TypeName` — what needs to change and why
- `functionName()` return type — what it currently returns vs what it should return
- Config shape — any new configuration options needed

**Acceptance criteria:**
- [ ] Specific, testable criterion 1
- [ ] Specific, testable criterion 2
- [ ] Specific, testable criterion 3

**Out of scope:**
- Thing that should NOT be changed or addressed in this issue
- Adjacent feature that might seem related but is separate
```

## 例 (Examples)

### 良い agent brief（bug）

```markdown
## Agent Brief

**Category:** bug
**Summary:** Skill description truncation drops mid-word, producing broken output

**Current behavior:**
When a skill description exceeds 1024 characters, it is truncated at exactly
1024 characters regardless of word boundaries. This produces descriptions
that end mid-word (e.g. "Use when the user wants to confi").

**Desired behavior:**
Truncation should break at the last word boundary before 1024 characters
and append "..." to indicate truncation.

**Key interfaces:**
- The `SkillMetadata` type's `description` field — no type change needed,
  but the validation/processing logic that populates it needs to respect
  word boundaries
- Any function that reads SKILL.md frontmatter and extracts the description

**Acceptance criteria:**
- [ ] Descriptions under 1024 chars are unchanged
- [ ] Descriptions over 1024 chars are truncated at the last word boundary
      before 1024 chars
- [ ] Truncated descriptions end with "..."
- [ ] The total length including "..." does not exceed 1024 chars

**Out of scope:**
- Changing the 1024 char limit itself
- Multi-line description support
```

### 良い agent brief（enhancement）

```markdown
## Agent Brief

**Category:** enhancement
**Summary:** Add `.out-of-scope/` directory support for tracking rejected feature requests

**Current behavior:**
When a feature request is rejected, the issue is closed with a `wontfix` label
and a comment. There is no persistent record of the decision or reasoning.
Future similar requests require the maintainer to recall or search for the
prior discussion.

**Desired behavior:**
Rejected feature requests should be documented in `.out-of-scope/<concept>.md`
files that capture the decision, reasoning, and links to all issues that
requested the feature. When triaging new issues, these files should be
checked for matches.

**Key interfaces:**
- Markdown file format in `.out-of-scope/` — each file should have a
  `# Concept Name` heading, a `**Decision:**` line, a `**Reason:**` line,
  and a `**Prior requests:**` list with issue links
- The triage workflow should read all `.out-of-scope/*.md` files early
  and match incoming issues against them by concept similarity

**Acceptance criteria:**
- [ ] Closing a feature as wontfix creates/updates a file in `.out-of-scope/`
- [ ] The file includes the decision, reasoning, and link to the closed issue
- [ ] If a matching `.out-of-scope/` file already exists, the new issue is
      appended to its "Prior requests" list rather than creating a duplicate
- [ ] During triage, existing `.out-of-scope/` files are checked and surfaced
      when a new issue matches a prior rejection

**Out of scope:**
- Automated matching (human confirms the match)
- Reopening previously rejected features
- Bug reports (only enhancement rejections go to `.out-of-scope/`)
```

### 悪い agent brief

```markdown
## Agent Brief

**Summary:** Fix the triage bug

**What to do:**
The triage thing is broken. Look at the main file and fix it.
The function around line 150 has the issue.

**Files to change:**
- src/triage/handler.ts (line 150)
- src/types.ts (line 42)
```

これが悪い理由:

- category がない
- 曖昧な記述（"the triage thing is broken"）
- すぐ古くなる file paths と line numbers を参照している
- acceptance criteria がない
- scope 境界がない
- current vs desired behavior の記述がない

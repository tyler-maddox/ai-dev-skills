# claude-dev-skills

Claude Code skills and specialist agents for a repeatable design → development pipeline.

Two orchestrator skills drive the pipeline. Each walks you through numbered stages, spawning specialist agents from `agents/roster.md` and invoking the supporting skills.

## Install

Skills and agents live in separate directories under `~/.claude/`:

```bash
git clone https://github.com/tyler-maddox/claude-dev-skills.git
cd claude-dev-skills

mkdir -p ~/.claude/skills ~/.claude/agents
cp -R dev-workflow design-workflow grill-me tdd improve-codebase-architecture ~/.claude/skills/
cp agents/*.md ~/.claude/agents/
```

The orchestrators read agent files from `~/.claude/agents/` by absolute path, so both halves must be installed.

## The pipeline

```
/design-workflow                          /dev-workflow
────────────────                          ─────────────
1. /grill-me                              1. /grill-me
2. Parker  → requirements issue           2. Paul  → PRD issue
3. Uma     → IA, flows, interaction       3. Ian   → vertical-slice issues
4. Vera    → visual direction             4. Dana  → review gate
5. Walt    → HTML wireframes (optional)   5. feature branch
6. Devin   → design review gate           6. /tdd  → implement each slice
7. handoff prompt ───────────────────────▶7. /improve-codebase-architecture
```

`/design-workflow` ends by writing a self-contained handoff prompt onto its spec issue, which `/dev-workflow` picks up as its starting context. Design is optional — start at `/dev-workflow` for backend or non-UI work.

## Skills

| Skill | Purpose |
| --- | --- |
| `/dev-workflow` | Orchestrates grill → PRD → issues → review gate → branch → TDD → architecture audit. |
| `/design-workflow` | Orchestrates grill → requirements → UX → visual → wireframes → review gate → dev handoff. |
| `/grill-me` | Interviews you until every branch of the decision tree is resolved. Emits a structured handoff block. |
| `/tdd` | Red-green-refactor loop. Tests describe behavior through public interfaces. |
| `/improve-codebase-architecture` | Audits for shallow modules and coupling; produces a refactor RFC issue. |

## Agents

Read `agents/roster.md` for the full schema, tags, and summaries.

- **Design team** — Parker (requirements), Uma (UX/IA), Vera (visual), Walt (wireframes), Devin (design critic).
- **Dev workflow team** — Paul (PRD), Ian (issue breakdown), Dana (dev critic).
- **Dev team** — Tara (tech lead), Jake (JS/TS), Rex (React), Juan (Java/JSP), Ada (accessibility), Quinn (QA).

## Requirements

- Claude Code
- `gh` CLI, authenticated — the workflows create and comment on GitHub issues
- A git repository with a GitHub remote

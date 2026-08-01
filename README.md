# ai-dev-skills

Agent skills and specialist personas for a repeatable design → development pipeline.

Two orchestrator skills drive the pipeline. Each walks you through numbered stages, spawning specialist agents from `agents/roster.md` and invoking the supporting skills.

Works with **Claude Code** and **OpenAI Codex CLI** — see [Using this with Codex](#using-this-with-codex).

## Install (Claude Code)

Skills and agents live in separate directories under `~/.claude/`:

```bash
git clone https://github.com/tyler-maddox/ai-dev-skills.git
cd ai-dev-skills

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

## Using this with Codex

Codex CLI has its own skill and subagent systems. The skill format is the same `SKILL.md` + `name`/`description` frontmatter, so the five skills port unchanged — only the install directory differs. Agents need converting, since Codex defines subagents as TOML rather than markdown.

| | Claude Code | Codex CLI |
| --- | --- | --- |
| Skills | `~/.claude/skills/<name>/SKILL.md` | `~/.agents/skills/<name>/SKILL.md` |
| Agents | `~/.claude/agents/<name>.md` | `~/.codex/agents/<name>.toml` |
| Invocation | `/skill-name` | `/skill-name` |
| Delegation | `Agent` tool | subagent spawn; `/agent` to inspect threads |

Codex also reads project-scoped skills from `.agents/skills/` and project-scoped agents from `.codex/agents/`, if you'd rather scope the pipeline to one repo.

### Install (Codex)

```bash
git clone https://github.com/tyler-maddox/ai-dev-skills.git
cd ai-dev-skills

# Skills — same files, Codex's skills directory
mkdir -p ~/.agents/skills
cp -R dev-workflow design-workflow grill-me tdd improve-codebase-architecture ~/.agents/skills/

# Agents — convert markdown to Codex subagent TOML
python3 scripts/agents-to-codex-toml.py          # writes to ~/.codex/agents/

# Repoint the orchestrators at the Codex agent directory and file extension
sed -i '' \
  -e 's|~/.claude/agents/<name-role>.md|~/.codex/agents/<name-role>.toml|g' \
  -e 's|~/.claude/agents|~/.codex/agents|g' \
  ~/.agents/skills/dev-workflow/SKILL.md \
  ~/.agents/skills/design-workflow/SKILL.md
```

On Linux, use `sed -i` without the `''`. Both `-e` expressions are needed and the order matters: specialist files become `.toml`, while `roster.md` stays markdown.

`agents-to-codex-toml.py` maps each agent's markdown body to `developer_instructions` and its frontmatter to `name` and `description`, then copies `roster.md` through unchanged — the orchestrators read the roster to pick specialists by role and tag, so it needs to sit alongside the TOML files.

### Behavioral differences

- **Delegation is requested, not guaranteed.** In Claude Code the orchestrator calls the `Agent` tool directly. In Codex the SKILL.md text asks for delegation and Codex decides how to honor it. If it inlines a stage instead of spawning a worker, the output is the same — the review gates (Dana, Devin) still run, just in the main thread. Say "spawn a subagent for this stage" if you want the split enforced.
- **The `Agent` tool is named explicitly** in both orchestrators' "How to Spawn Specialists" section. Codex treats that as a description of intent rather than a tool call. Harmless, but you can reword it to "spawn a subagent" if the literal name causes confusion.
- **Review-gate retry loops** (Dana's bounded 2 retries, Devin's until-approved loop) are plain instructions, not harness features — they behave the same on both.

### Running only one side

The skills and agents are independent halves. To use the Codex-native subagents without the orchestrator skills, invoke them by name (`pr_explorer`-style) after conversion. To use the skills without subagents, install the skills only — each orchestrator degrades to a single-threaded stage walkthrough.

## Requirements

- Claude Code, or Codex CLI
- `gh` CLI, authenticated — the workflows create and comment on GitHub issues
- A git repository with a GitHub remote
- Python 3.11+ if you're running the Codex agent converter

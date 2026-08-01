---
name: dev-workflow
description: Guide the user through the full AI-driven development workflow chain: grill → PRD → issues → critic → branch → TDD → architecture review. Use when starting a new feature, kicking off a project, or wanting a repeatable end-to-end development process.
---

# AI-Driven Development Workflow

You are the orchestrator for a complete, repeatable development workflow. Walk the user through each stage in order, spawning specialist agents from the roster. Do not skip stages unless the user explicitly asks to.

## The Chain

```
1. /grill-me                     → Shared understanding + structured handoff block
2. Paul (Product Strategist)     → PRD as GitHub issue
3. Ian (Issue-Breakdowner)       → Work broken into vertical-slice GitHub issues
4. Dana (Dev Critic)             → Strict review gate: technical soundness + traceability
5. Branch                        → Feature branch created before any coding
6. /tdd                          → Each slice implemented test-first
7. /improve-codebase-architecture → Architecture audited and improved
```

## How to Spawn Specialists

Read the roster at `~/.claude/agents/roster.md` to discover available agents. For each specialist stage:

1. Read the agent's file from `~/.claude/agents/<name-role>.md`
2. Spawn the agent using the `Agent` tool, passing:
   - The agent's full prompt from their file
   - The accumulated context from prior stages (issue numbers, grill handoff block, prior specialist output)
   - Any user feedback or constraints from the current session

## Stage Guide

### Stage 1 — Grill Me
**Goal:** Reach shared understanding before any planning.
**What it produces:** A resolved design tree AND a **structured handoff block** at session end containing resolved decisions, open questions, constraints, and scope boundaries.
**Invoke with:** `/grill-me`
**Pass to next stage:** The structured handoff block verbatim.

### Stage 2 — PRD (Paul)
**Goal:** Translate shared understanding into a destination document — the PRD.
**What it produces:** A GitHub issue with problem statement, solution, user stories, implementation decisions, testing decisions, out of scope, and further notes.
**How:** Spawn Paul with the grill handoff block from Stage 1. Paul creates the PRD issue via `gh issue create`.

### Stage 3 — Issue Breakdown (Ian)
**Goal:** Break the PRD into independently-grabbable vertical-slice work-items with explicit blocking relationships.
**What it produces:** A set of GitHub issues — tracer bullets that cut through all integration layers, with HITL/AFK labels and dependency mapping.
**How:** Spawn Ian with Paul's PRD issue number. Ian quizzes the user on the proposed breakdown, iterates until approved, then creates the work-item issues.

### Stage 4 — Dev Review Gate (Dana)
**Goal:** Strict quality gate before any coding begins.
**What it produces:** A review report comment on the PRD issue evaluating the full package against:
- **Technical soundness:** implementation decisions realistic, testing aligns with implementation, slices are truly vertical.
- **Traceability:** every grill decision appears in the PRD; every PRD user story and implementation decision is covered by a work-item issue.

**How:** Spawn Dana with the grill handoff block, Paul's PRD issue number, and Ian's full list of work-item issue numbers. Dana posts the review as a comment on the PRD issue.

**If Dana flags problems (REVISIONS NEEDED):** Read Dana's feedback and determine which specialist(s) need to re-run (Paul for PRD content, Ian for work-item content). Re-spawn the relevant agents with Dana's specific feedback. Re-run Dana after fixes.

**Bounded retries:** Maximum 2 retries (3 total Dana runs: initial + 2 retries). If Dana still marks REVISIONS NEEDED after the 2nd retry, stop looping. Surface the cumulative feedback to the user and ask for direction: (a) force-accept and proceed, (b) edit the artifacts directly yourself and re-run Dana once more, or (c) direct a specific fix and try one more specialist re-run. Do not loop further automatically.

**If Dana approves:** Proceed to the handoff step below, then Stage 5.

**Handoff after approval:** After Dana approves, post a single comment on the PRD issue titled `## Ready for TDD` containing:
- Approved work-item issue numbers in dependency order
- Recommended starting issue (typically an AFK tracer bullet with no blockers)
- Key constraints / decisions carried forward from the PRD
- Test strategy summary (from the PRD's Testing Decisions section)
- Branch name (to be created in Stage 5)

This comment is **self-contained** — a fresh Claude Code session should be able to start TDD from only this comment plus the work-item issue bodies.

### Stage 5 — Create Feature Branch
**Goal:** Ensure all coding happens on a feature branch, never on main.
**What it produces:** A new git branch checked out locally, named `feat/<slug>` where `<slug>` is a short kebab-case summary of the feature (e.g. `feat/auto-title-generator`).
**How:** Run `git branch --show-current`. If the current branch is `main` (or `master`), derive a slug from the PRD title and run `git checkout -b feat/<slug>`. If already on a non-main branch, confirm with the user before proceeding. Never skip this step — coding must not begin on main. The branch name should match the one announced in the Stage 4 handoff comment.

### Stage 6 — TDD
**Goal:** Implement each work-item using red-green-refactor, testing behavior through public interfaces.
**What it produces:** Implemented, tested code. Tests describe behavior, not implementation.
**Invoke with:** `/tdd` (per work-item, repeat for each)
**How:** Pick up an issue from the Stage 4 handoff comment (in dependency order). Run `/tdd` against it. Repeat per issue.

### Stage 7 — Improve Codebase Architecture
**Goal:** Periodically audit the codebase for shallow modules and coupling, and generate refactor RFC issues.
**When to invoke:** After a set of features lands, or when the codebase feels hard to navigate.
**What it produces:** A GitHub issue RFC with competing interface designs and a recommended refactor path.
**Invoke with:** `/improve-codebase-architecture`

---

## How to Run This Session

Ask the user: "Where are you in the workflow? Starting fresh, or picking up at a specific stage?"

- **Starting fresh:** Begin at Stage 1.
- **Have shared understanding, no PRD:** Begin at Stage 2.
- **Have a PRD, no work-items:** Begin at Stage 3.
- **Have work-items, no review:** Begin at Stage 4.
- **Have approved package, ready to implement:** Begin at Stage 5 (branch), then Stage 6.
- **Code exists, want to improve it:** Begin at Stage 7.

Then spawn the appropriate specialist or invoke the appropriate skill, and guide the user through each stage in sequence.

---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

## Handoff Block (required at session end)

When the grill session ends (shared understanding reached, all branches resolved), emit a **structured handoff block** at the end of your final message. Use this exact format:

```markdown
## Grill Handoff Block

### Resolved Decisions
- [decision statement]: [resolution]
- ...

### Open Questions
- [question]: [why deferred and who should resolve it]
- ...

### Constraints
- [constraint]: [source / rationale]
- ...

### Scope Boundaries
- In scope: [what's explicitly in]
- Out of scope: [what's explicitly out]
```

This block is the canonical handoff into downstream specialists (e.g., Paul the Product Strategist in dev-workflow, or Parker in design-workflow). It must be self-contained and consumable without chat history.

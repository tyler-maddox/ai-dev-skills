# Agent Roster

Specialist agents available for orchestrators and direct invocation. Orchestrators read this roster to select agents by role and tags.

## Schema

Each agent file lives in `~/.claude/agents/` and follows this format:
- **name**: Agent's name (first letter matches role)
- **role**: Job title
- **file**: Filename in this directory
- **tags**: Domain keywords for discovery
- **summary**: One-line capability description

---

## Design Team

- **Parker** | Product Strategist | `parker-product-strategist.md` | `product, requirements, jtbd, strategy, research` | Frames problems, defines requirements, competitive analysis, jobs-to-be-done
- **Uma** | UX Architect | `uma-ux-architect.md` | `ux, ia, flows, navigation, interaction, accessibility` | Information architecture, user flows, interaction patterns
- **Vera** | Visual Designer | `vera-visual-designer.md` | `visual, color, typography, spacing, hierarchy, brand, design-system` | Color, typography, spacing, visual hierarchy, design system alignment
- **Walt** | Wireframe Artist | `walt-wireframe-artist.md` | `wireframe, layout, responsive, prototype, html` | HTML wireframe prototypes, layout composition, responsive patterns
- **Devin** | Design Critic | `devin-design-critic.md` | `review, heuristics, usability, consistency, qa` | Heuristic evaluation, usability review, requirements traceability

## Dev Workflow Team

- **Paul** | Product Strategist (Dev Workflow) | `paul-product-strategist.md` | `product, prd, requirements, modules, tdd-prep` | Drafts the PRD — problem framing, user stories, implementation decisions, testing decisions
- **Ian** | Issue-Breakdowner | `ian-issue-breakdowner.md` | `issues, vertical-slices, tracer-bullets, dependencies, hitl-afk, planning` | Breaks a PRD into independently-grabbable vertical-slice GitHub issues with explicit blocking relationships
- **Dana** | Dev Critic | `dana-dev-critic.md` | `review, technical-soundness, traceability, qa, dev-workflow-gate` | Quality gate — technical soundness + PRD-to-issue traceability review


## Dev Team

- **Tara** | Tech Lead | `tara-tech-lead.md` | `triage, delegation, planning, architecture, coordination` | Reads issues, selects specialists, defines approach, coordinates implementation
- **Jake** | JavaScript/TypeScript Specialist | `jake-js-ts-specialist.md` | `javascript, typescript, node, tooling, bundlers` | JS/TS patterns, Node, tooling, runtime behavior
- **Rex** | React Specialist | `rex-react-specialist.md` | `react, components, hooks, state, rendering, frontend` | Components, hooks, state management, React ecosystem
- **Juan** | Java/JSP Specialist | `juan-java-jsp-specialist.md` | `java, jsp, servlets, legacy, spring` | Java, JSP, servlets, legacy modernization
- **Ada** | Accessibility Specialist | `ada-accessibility-specialist.md` | `accessibility, wcag, aria, screen-reader, keyboard` | WCAG compliance, ARIA, screen readers, keyboard nav, a11y auditing
- **Quinn** | QA Specialist | `quinn-qa-specialist.md` | `qa, testing, edge-cases, integration, regression, acceptance` | Test strategy, edge cases, integration testing, acceptance criteria validation

---
name: prd-writer
description: Draft a product requirements document (PRD) from a rough idea, feature request, or notes. Use when the user asks for a PRD, spec, requirements doc, or wants to turn an idea into something engineering and design can build from.
---

# PRD Writer

Turn a rough product idea into a clear, reviewable PRD. A good PRD explains **why** before **what**, and leaves **how** to engineering and design.

## When to use
- "Write a PRD for…", "spec out this feature", "turn these notes into requirements"
- The user has an idea, customer feedback, or a ticket and needs a doc others can review

## Inputs
Gather these first. If a few are missing, ask in one short batch. If the user wants a fast draft, make reasonable assumptions and list them under **Open questions**.
- The problem or opportunity, and who has it
- Evidence (data, quotes, tickets, revenue at stake)
- Target users or segments
- Constraints: deadline, platforms, dependencies, budget
- Known scope boundaries

## Steps
1. **Restate the problem** in one or two sentences without naming a solution. If the user only gave a solution, ask (or infer) what problem it solves.
2. **Define success** with 1–3 measurable goals, each with a metric, baseline (if known), and target.
3. **Write non-goals.** List what this release won't do. This prevents scope creep more than anything else.
4. **Describe users and scenarios.** Name the primary persona and 2–4 key scenarios in plain language.
5. **List requirements** as a numbered table with priority (P0 = launch blocker, P1 = should have, P2 = nice to have). Each requirement states an observable behavior, not an implementation.
6. **Cover the edges:** empty states, errors, permissions, limits, accessibility, localization, data/privacy.
7. **Note risks and dependencies,** each with a mitigation or owner.
8. **Close with open questions**, each with a suggested owner.

## Output format
```
# <Feature name> — PRD
Status: Draft · Owner: <name> · Last updated: <date>

## Problem
## Goals & success metrics   (table: Goal | Metric | Baseline | Target)
## Non-goals
## Users & scenarios
## Requirements              (table: # | Requirement | Priority | Notes)
## Edge cases & constraints
## Risks & dependencies
## Release plan              (phases or milestones, if known)
## Open questions            (question — owner)
## Appendix                  (evidence, research links)
```
Keep it to what's needed. A small feature can be one page. Don't pad sections; write "N/A" or drop them.

## Quality checklist
- [ ] The problem is stated without naming the solution
- [ ] Every goal has a metric someone could actually measure
- [ ] Non-goals exist and are specific
- [ ] Requirements describe behavior, not implementation, and each has a priority
- [ ] Each P0 is truly a launch blocker
- [ ] Assumptions you made are listed as open questions, not hidden as facts

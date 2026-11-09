---
name: confluence-to-project-plan
description: Turn a long Confluence page or spec (PRD, design doc, one-pager, roughly 3–10 pages) into a phased project plan with milestones, owners, dependencies, and risks, plus a ready-to-import set of Jira epics, stories, and tasks. Use when the user shares or links a Confluence page and wants a plan, a work breakdown, or Jira tickets from it.
---

# Confluence Page → Project Plan + Jira Tasks

Read a long product or technical document and turn it into (1) a project plan people can commit to and (2) a Jira backlog that implements it, where every ticket traces back to the source.

## When to use
- "Turn this Confluence page into a project plan", "break this spec into Jira tickets", "create epics and stories from this doc"
- The user pastes, attaches, or links a multi-page document

## Inputs
- **The document.** If a Confluence or Atlassian connector is available, fetch the page with it. Otherwise ask the user to paste the content or export it (PDF or Word). Never guess at content you couldn't read.
- Team and capacity (people, roles, sprint length). If unknown, assume 2-week sprints and say so.
- Target date or fixed deadline, if any
- Jira project key and existing epics, if any

## Steps

### 1. Read and extract
Read the whole document before planning. Build an extraction table with a section reference for each item:
- Goals and success metrics
- Scope (in and out)
- Functional requirements and user flows
- Non-functional requirements (performance, security, compliance, accessibility)
- Dependencies (teams, systems, vendors) and stated dates
- Decisions already made vs. open questions

Flag contradictions, gaps, and vague requirements (no owner, no acceptance criteria, "TBD") under **Issues found in the doc**. Don't silently resolve them.

### 2. Structure the work
- Group requirements into **workstreams**, typically by area: backend, frontend, data, infra, design, QA, launch/GTM.
- Each workstream (or major capability) becomes a Jira **epic**.
- Break each epic into **stories** (user-facing value) and **tasks** (enabling work). Aim for items that fit in one sprint; split anything bigger.
- Add the work documents usually forget: design review, tracking/analytics, QA and test plan, docs, feature flag and rollout, monitoring and alerting, support enablement, and cleanup.

### 3. Sequence and plan
- Map dependencies between tickets, and find the critical path.
- Group into **phases** with exit criteria, for example: Discovery/Design → Build (MVP) → Hardening/QA → Beta → GA.
- Set **milestones** with target dates. Only use real dates if the doc or user gives a start date and capacity; otherwise use relative weeks (W1–W2) and say so.
- Assign owners by role (e.g. "Backend lead") unless names are given.
- Write a **risk register**: risk, likelihood, impact, mitigation, owner.

### 4. Write the Jira tickets
Write each ticket to the **jira-ticket-writer** standard if that skill is available: verb-first summary, context, action items, testable acceptance criteria, measurables, out of scope. Every ticket also gets:
- **Source:** the doc section it came from (e.g. "§3.2 Bulk edit")
- **Epic link**, **estimate** (S/M/L or points), and **depends on**, if any

### 5. Check coverage
Make a traceability table mapping every requirement in the doc to at least one ticket. Any requirement with no ticket is either a gap to fix or explicitly out of scope. Any ticket with no source is extra work: label it as such (e.g. QA, rollout).

## Output format
Deliver two parts. For a long plan, offer to create a document or spreadsheet artifact. If a Jira connector is available, offer to create the tickets directly, and only create them after the user confirms.

**Part 1: Project plan**
```
# <Project> — Project plan
Source: <doc title/link> · Prepared: <date> · Assumptions: <sprint length, team, start date>

## Summary (goal, scope, target date, top 3 risks)
## Success metrics (from doc)
## Phases & milestones   (table: Phase | Exit criteria | Target | Owner)
## Workstreams & epics   (table: Epic | Scope | Owner | # tickets | Est.)
## Timeline              (by sprint or week; critical path marked)
## Dependencies          (internal/external, with dates needed)
## Risk register         (Risk | Likelihood | Impact | Mitigation | Owner)
## Issues found in the doc (contradictions, gaps, open questions → owner)
## Requirement coverage  (Doc section | Requirement | Ticket(s))
```

**Part 2: Jira backlog**
- The full tickets, grouped by epic, in Jira-friendly markdown
- A CSV for Jira's importer:
  `Issue Type,Summary,Description,Epic Name,Epic Link,Priority,Story Points,Labels,Depends On,Source Section`
  Epics get an `Epic Name`. Child issues use `Epic Link` matching that name. Put multi-line descriptions in quotes.

## Quality checklist
- [ ] The whole document was read; nothing was planned from a skim
- [ ] Every requirement maps to a ticket or is marked out of scope
- [ ] Every ticket cites its source section, or is labeled as extra work
- [ ] No ticket is bigger than one sprint
- [ ] Rollout, QA, analytics, and monitoring work is included
- [ ] Dates are real only if backed by a start date and capacity; otherwise they're relative
- [ ] Doc gaps and contradictions are surfaced, not silently resolved
- [ ] Tickets are created in Jira only after the user confirms

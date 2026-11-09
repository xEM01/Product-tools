---
name: stakeholder-update
description: Write a concise weekly, biweekly, or monthly status update for executives, cross-functional partners, or the team, covering progress, metrics, risks, and asks. Use when the user wants a status report, project update, exec summary, or update email/Slack post.
---

# Stakeholder Update

Write an update a busy reader can absorb in under a minute, with the most important thing first.

## When to use
- "Write my weekly update", "status report for leadership", "summarize where the project is"
- The user shares notes, tickets, metrics, or a messy brain-dump about a project

## Inputs
- What happened since the last update (notes, shipped items, ticket list)
- Key metrics and how they moved, if any
- Risks, blockers, and decisions needed
- Audience (execs, cross-functional, team) and channel (email, Slack, doc)
- The previous update, if available, for continuity

## Steps
1. **Pick the headline.** One sentence: overall status and the single most important thing. Lead with it.
2. **Set status honestly.** Use On track / At risk / Off track. If the project is at risk, say so and why. Don't bury it.
3. **Report outcomes, not activity.** Write "Checkout v2 shipped to 20%; conversion +1.2pt", not "worked on checkout".
4. **Surface risks with a plan.** Each risk gets impact, likelihood, and a mitigation or owner.
5. **Make asks explicit.** Name the person, the decision or help needed, and the date.
6. **Tailor depth to the audience.** Execs get status, metrics, risks, and asks. The team gets more detail and next steps.
7. **Cut.** Remove anything the reader wouldn't miss.

## Output format
```
**<Project> update — <date>** · Status: 🟢 On track / 🟡 At risk / 🔴 Off track

**TL;DR:** <one or two sentences>

**Progress**
- <outcome> (<metric or link>)

**Metrics**   (only if they moved or matter: metric — value — change)

**Risks & blockers**
- <risk> — impact — mitigation/owner

**Asks**
- @<person>: <decision/help> by <date>

**Next up**
- …
```
For Slack, keep it to the TL;DR plus bullets. For email, add a clear subject line: `[<Project>] <status> — <headline>`.

## Quality checklist
- [ ] The headline and status are in the first two lines
- [ ] Bullets describe outcomes, not activity
- [ ] Status matches the content (no 🟢 alongside a major unmitigated risk)
- [ ] Every ask has an owner and a date
- [ ] Readable in under 60 seconds

---
name: jira-ticket-writer
description: Write clean, ready-to-work Jira tickets (story, task, bug, spike) with a clear summary, context, concrete action items, testable acceptance criteria, and measurable success criteria. Use when the user wants to create, rewrite, or clean up a Jira ticket or turn a request, bug report, or Slack thread into one.
---

# Jira Ticket Writer

Produce tickets an engineer can pick up without a meeting: what to do, why, how to know it's done, and how to know it worked.

## When to use
- "Write a Jira ticket for…", "clean up this ticket", "turn this thread into a ticket"
- The user shares a request, bug report, idea, or messy existing ticket

## Inputs
Ask only for what's missing and blocks a usable ticket. Otherwise draft with assumptions marked `[ASSUMPTION]`.
- What needs to happen and why
- Issue type: Story, Task, Bug, or Spike (infer if unstated)
- Project key, epic, component, labels, assignee, sprint (optional; leave as placeholders if unknown)
- For bugs: steps to reproduce, expected vs. actual, environment, frequency, severity

## Writing rules
- **Summary:** under ~80 characters, starts with a verb, names the thing and the outcome. "Add CSV export to Invoices list", not "Export" or "Customers want CSV".
- **One ticket, one outcome.** If it needs "and" to describe two deliverables, split it and say so.
- **Action items are concrete steps,** each starting with a verb, each checkable as done. Not "look into X".
- **Acceptance criteria are testable.** Use Given/When/Then for behavior, or a checklist for tasks. Avoid untestable words: "fast", "intuitive", "robust", "properly", "etc."
- **Measurables give numbers:** a metric, threshold, and how it's checked ("p95 load < 800 ms on staging with 10k rows, measured in Datadog").
- **Separate scope from out-of-scope.** List what this ticket explicitly won't do.
- **Don't prescribe implementation** unless it's a hard constraint. Then say why.
- **Link, don't paste.** Reference designs, docs, and threads by link.

## Steps
1. Identify the issue type and the single outcome.
2. Write the summary.
3. Write 2–4 sentences of context: the problem, who's affected, and why now.
4. List action items as a checklist.
5. Write acceptance criteria (3–7 is typical; more suggests splitting).
6. Add measurables: the definition of done (quality bar) and, where relevant, a success metric after release.
7. Add out of scope, dependencies, and open questions.
8. Suggest a priority and a rough size (S/M/L or story points) with a one-line reason.
9. Run the quality checklist and fix anything that fails.

## Output format
Use Jira-friendly markdown. Fill in fields you know and leave clear placeholders for the rest.

```
**Summary:** <Verb + object + outcome>
**Type:** Story | Task | Bug | Spike   **Priority:** <P1–P4> (<reason>)   **Estimate:** <S/M/L or points>
**Epic:** <key or TBD>   **Labels:** …   **Components:** …

### Context
<Problem, who it affects, why now. Link to source.>

### Action items
- [ ] <Verb + concrete step>
- [ ] …

### Acceptance criteria
- [ ] Given <state>, when <action>, then <observable result>
- [ ] …

### Measurables
- **Definition of done:** <quality bar: tests, perf threshold, docs, feature flag, etc.>
- **Success metric:** <metric> moves from <baseline> to <target> within <time window> (measured in <tool>)

### Out of scope
- …

### Dependencies / links
- …

### Open questions
- <question> (owner: <name>)
```

### Bug variant
Replace Action items with:
```
### Steps to reproduce
1. …
**Expected:** …   **Actual:** …
**Environment:** <app version, browser/OS, account type>   **Frequency:** <always / x of y attempts>
**Severity / impact:** <users affected, workaround?>
```
Acceptance criteria then include "the bug no longer reproduces using the steps above" and a regression test.

### Spike variant
A spike is time-boxed research. Include the question to answer, the time box (e.g. 2 days), and the deliverable (a decision doc, prototype, or recommendation). The measurable is that the question is answered, not that a feature works.

## Bulk output
When asked for several tickets, also offer a CSV for Jira's importer with the columns:
`Summary,Issue Type,Description,Priority,Labels,Epic Link,Story Points`

## Quality checklist
- [ ] The summary starts with a verb and fits on one line
- [ ] The ticket has one outcome; anything that needs splitting is flagged
- [ ] Every action item is a concrete, checkable step
- [ ] Every acceptance criterion is testable, with no vague adjectives
- [ ] At least one measurable has a number and a way to measure it
- [ ] Out of scope is stated
- [ ] Assumptions are marked, not presented as facts

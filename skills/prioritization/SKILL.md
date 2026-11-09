---
name: prioritization
description: Prioritize a backlog, feature list, or set of initiatives using RICE, ICE, MoSCoW, Kano, or value-vs-effort, and produce a ranked list with rationale. Use when the user asks what to build next, how to rank items, or wants a scored backlog.
---

# Prioritization

Rank a set of candidate items with a transparent framework so the result can be debated on inputs rather than opinions.

## When to use
- "Prioritize this backlog", "what should we build next?", "RICE score these"
- The user has a list of features, bugs, bets, or requests competing for limited capacity

## Inputs
- The list of items (required)
- The goal or strategy the ranking serves (e.g. "grow activation this quarter")
- Any known data: reach, revenue, effort estimates, deadlines, commitments
- Preferred framework, if any

## Choosing a framework
| Situation | Use |
|---|---|
| Comparable features with some data | **RICE**: (Reach × Impact × Confidence) ÷ Effort |
| Fast pass, little data | **ICE**: Impact × Confidence × Ease (1–10 each) |
| Fixed-scope release, must cut | **MoSCoW**: Must / Should / Could / Won't |
| Customer-satisfaction lens | **Kano**: Basic / Performance / Delighter |
| Quick visual for stakeholders | **Value vs. effort** 2×2 |

If the user didn't specify, pick one, say why in one line, and proceed.

## Steps
1. **Anchor on the goal.** Score impact against the stated goal, not general goodness.
2. **Set scales explicitly.** For RICE use Reach = users or events per quarter; Impact = 3 / 2 / 1 / 0.5 / 0.25; Confidence = 100% / 80% / 50%; Effort = person-weeks.
3. **Score each item.** Mark every estimated value with `~` and every value from real data with its source.
4. **Rank and sanity-check.** Compare the ranking to intuition. If something feels wrong, find the input driving it and say so rather than fudging scores.
5. **Apply overrides separately.** List commitments, compliance deadlines, or dependencies that force an item up or down, outside the score.
6. **Recommend a cut line** based on available capacity, if known.

## Output format
```
## Prioritized backlog: <goal>
Framework: RICE (because …)

| Rank | Item | Reach | Impact | Confidence | Effort | Score | Notes |

### Overrides
### Recommendation (cut line, what to do first, what to defer)
### Assumptions to validate (estimates with the most influence on the ranking)
```
Calculate scores with code or careful arithmetic and show the formula, so results can be reproduced.

## Quality checklist
- [ ] The goal being optimized is stated
- [ ] Scales are defined, and estimates are marked as estimates
- [ ] Scores are arithmetically correct
- [ ] Overrides are separate from scores, not hidden in them
- [ ] The most influential uncertain inputs are named

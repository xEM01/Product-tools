---
name: experiment-design
description: Design an A/B test or product experiment plan with a hypothesis, variants, primary and guardrail metrics, sample size, duration, and decision rules. Use when the user wants to test a change, plan an experiment, or check whether a test is worth running.
---

# Experiment Design

Produce an experiment plan that gives a trustworthy, pre-committed decision before any data comes in.

## When to use
- "Help me A/B test…", "design an experiment for…", "how long should this test run?"
- The user has a proposed change and wants evidence before rolling it out

## Inputs
- The change being tested and why
- The target population and where the change appears
- The baseline value of the primary metric (e.g. 4.2% conversion)
- Eligible traffic per day or week
- The minimum effect worth detecting (MDE), or the business threshold for "worth it"

## Steps
1. **Write the hypothesis:** "We believe <change> for <users> will <move metric> because <reason>. We'll know when <primary metric> changes by ≥ <MDE>."
2. **Define the variants.** Control plus one treatment by default. Add more arms only with enough traffic to support them.
3. **Choose metrics.**
   - One **primary** metric that decides the outcome
   - **Secondary** metrics that explain why
   - **Guardrails** that must not get worse (e.g. latency, refunds, unsubscribes)
4. **Set the randomization unit** (user, account, session) and explain the choice. Watch for network effects and contamination.
5. **Calculate sample size and duration.** Use α = 0.05 (two-sided) and power = 0.8 unless told otherwise. For a conversion metric use the standard two-proportion formula. Compute it in code rather than estimating. Run for whole weeks, at least one full business cycle.
6. **Pre-commit decision rules:** ship / iterate / kill, based on the primary metric and guardrails. Say what happens if the result is flat.
7. **List threats to validity:** novelty effects, sample ratio mismatch, peeking, seasonality, and overlapping experiments.
8. **If it can't reach power** in a reasonable time, say so and suggest alternatives: a larger MDE, a more sensitive metric, a staged rollout, or qualitative testing.

## Output format
```
# Experiment plan: <name>
Hypothesis: …
Variants: Control — … | Treatment — …
Unit & allocation: <unit>, 50/50, <population>

| Metric type | Metric | Baseline | MDE / threshold |
| Primary | … |
| Guardrail | … |

Sample size: <n per arm> (α=0.05, power=0.8) → Duration: <weeks> at <traffic>/day
Decision rules: Ship if … · Iterate if … · Kill if …
Risks & validity checks: …
Owner / start date / readout date: …
```

## Quality checklist
- [ ] Exactly one primary metric
- [ ] Sample size was computed, with assumptions shown
- [ ] Duration covers whole weeks
- [ ] Decision rules are written before launch, including the flat-result case
- [ ] Guardrails are defined
- [ ] The plan says whether the test is feasible at the given traffic

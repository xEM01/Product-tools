---
name: user-research-synthesis
description: Synthesize user interview notes, transcripts, survey responses, or support tickets into themes, pain points, supporting quotes, and opportunities. Use when the user shares research data and wants insights, a findings summary, or an affinity map.
---

# User Research Synthesis

Turn raw qualitative data into findings a team can act on, with every claim traceable to evidence.

## When to use
- "Synthesize these interviews", "what are the themes?", "summarize this feedback"
- The user pastes or attaches transcripts, notes, survey open-ends, or ticket exports

## Inputs
- The raw data (required)
- The research question or goal. If missing, infer it and state the inference.
- Participant metadata if available (segment, role, plan, tenure)

## Steps
1. **Inventory the data.** Count sources and participants. Give each a short ID (P1, P2…) and note segment where known.
2. **Extract observations.** Pull atomic observations, each tagged with participant ID: what they did, said, felt, or worked around. Keep exact quotes separate from paraphrase.
3. **Cluster into themes.** Group observations bottom-up. Name each theme as an insight sentence ("Admins don't trust bulk edits because there's no undo"), not a topic label ("Bulk edit").
4. **Size each theme.** Record how many participants mention it and in which segments. Qualitative data shows patterns, not percentages, so say "5 of 8 participants", not "62%".
5. **Separate signal from noise.** Flag one-off comments, leading-question artifacts, and contradictions between participants.
6. **Derive opportunities.** For each strong theme, write a "How might we…" and its likely impact. Do not jump to specific solutions unless asked.
7. **Note gaps.** State what the data can't answer and who wasn't represented.

## Output format
```
# Research synthesis: <topic>
Sources: <n> interviews / <n> tickets · Segments: … · Date range: …

## Top findings (3–5 sentences, most important first)

## Themes
### 1. <Insight sentence>
- Prevalence: 5 of 8 participants (mostly <segment>)
- Evidence: "<quote>" (P3); "<quote>" (P7)
- Implication: …

## Opportunities   (How might we… | Themes addressed | Est. impact)
## Contradictions & outliers
## Gaps & next research questions
```

## Quality checklist
- [ ] Every theme cites at least two participants, or is marked as a single-source signal
- [ ] Quotes are verbatim and attributed to a participant ID
- [ ] Theme names are insights, not topics
- [ ] No invented data, percentages, or quotes
- [ ] Gaps in who was studied are stated

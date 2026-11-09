# Product Tools

A public collection of agent skills for Product Managers: PRDs, roadmaps, prioritization, user research synthesis, stakeholder updates, and more.

## Structure

```
skills/
  <skill-name>/
    SKILL.md        # required: frontmatter + instructions
    references/     # optional: longer docs loaded on demand
    scripts/        # optional: helper scripts
    assets/         # optional: templates, examples
  _template/        # copy this to start a new skill
docs/               # contributing and authoring guides
```

## Using a skill

Copy a folder from `skills/` into your agent's skills directory (for Claude: upload the folder as a skill, or place it in `.claude/skills/`).

## Skills

| Skill | Description |
|-------|-------------|
| [prd-writer](skills/prd-writer/SKILL.md) | Draft a PRD from a rough idea or notes |
| [user-research-synthesis](skills/user-research-synthesis/SKILL.md) | Turn interviews and feedback into themes, quotes and opportunities |
| [prioritization](skills/prioritization/SKILL.md) | Rank a backlog with RICE, ICE, MoSCoW, Kano or value vs. effort |
| [stakeholder-update](skills/stakeholder-update/SKILL.md) | Write a concise status update with progress, risks and asks |
| [experiment-design](skills/experiment-design/SKILL.md) | Plan an A/B test with hypothesis, metrics, sample size and decision rules |
| [jira-ticket-writer](skills/jira-ticket-writer/SKILL.md) | Write clean Jira tickets with action items, testable acceptance criteria and measurables |
| [confluence-to-project-plan](skills/confluence-to-project-plan/SKILL.md) | Turn a long Confluence page into a phased project plan and an importable Jira backlog |

## Contributing

This repo is public, but only the owner has write access. Suggestions are welcome via issues; pull requests from forks may be reviewed at the owner's discretion. See [docs/authoring-skills.md](docs/authoring-skills.md).

## License

MIT

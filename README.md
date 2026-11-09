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
| _none yet_ | Copy `skills/_template` to add the first one |

## Contributing

This repo is public, but only the owner has write access. Suggestions are welcome via issues; pull requests from forks may be reviewed at the owner's discretion. See [docs/authoring-skills.md](docs/authoring-skills.md).

## License

MIT

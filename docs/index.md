# Skill Graphs

![PyPI - Version](https://img.shields.io/pypi/v/skill-graphs)

**Skill Graphs** is a curated Python package of distilled, documentation-sourced skill
graphs for the agent-utilities ecosystem. Each graph transforms authoritative technical
documentation — language references, framework guides, database manuals, and
infrastructure blueprints — into structured agent knowledge that Pydantic AI agents can
load on demand.

## What this package provides

- **A broad catalog of domain skill graphs** spanning programming languages, Python and
  JavaScript frameworks, databases, homelab platforms, trading systems, and career
  references.
- **Opt-in activation** so agents load only the domains they need. Every graph is
  disabled by default and enabled through a dedicated environment flag.
- **A repeatable build workflow** that converts crawled documentation into a new skill
  graph with a single command.

## Where to go next

- The [Overview](overview.md) describes the ecosystem role, enterprise-readiness
  inheritance, and the standardized package architecture.
- The project [README](https://github.com/Knuckles-Team/skill-graphs) lists the full
  catalog of available skill graphs and their enable flags.

## Installation

```bash
pip install skill-graphs
```

## Loading skill graphs

```python
from skill_graphs.skill_graph_utilities import get_skill_graphs_path
from agent_utilities.agent_utilities import SkillsToolset

# Load enabled skill graphs
skills_directories = get_skill_graphs_path()
skills = SkillsToolset(directories=skills_directories)
```

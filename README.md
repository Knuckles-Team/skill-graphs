# Skill Graphs - Indexed Agent Knowledge

![PyPI - Version](https://img.shields.io/pypi/v/skill-graphs)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')

*Version: 0.1.1*

## Overview

Skill Graphs is a dedicated repository for structured, documentation-based skills. It is designed to host "knowledge graphs" transformed from technical documentation, APIs, and web crawls, specifically for use with Pydantic AI Agents.

## Disabling Skill Graphs

You can disable specific skill-graphs by setting their corresponding environment variables to `False`. By default, all skill-graphs included in this package are enabled if the package is loaded.

| Skill Directory | Description | Disable Flag |
|:----------------|:------------|:-------------|
| `example-docs`  | Example documentation skill | `EXAMPLE_DOCS_ENABLE=False` |

## Installation

```bash
pip install skill-graphs
```

## Usage

Skill graphs are typically loaded using the `get_skill_graphs_path()` utility from `skill_graphs.skill_graph_utilities`.

```python
from skill_graphs.skill_graph_utilities import get_skill_graphs_path
from agent_utilities.agent_utilities import SkillsToolset

# Load enabled skill graphs
skills_directories = get_skill_graphs_path()
skills = SkillsToolset(directories=skills_directories)
```

## Building New Skill Graphs

Use the `skill-graph-builder` from the `universal-skills` package to generate new graphs:

```bash
python scripts/generate_skill.py https://ai.pydantic.dev pydantic-ai
```

By default, the builder will now target this repository if it is present in your workspace.

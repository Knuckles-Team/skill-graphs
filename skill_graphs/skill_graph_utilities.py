#!/usr/bin/python
# coding: utf-8

import os
from pathlib import Path
from importlib.resources import files, as_file
from typing import Optional

try:
    from openai import AsyncOpenAI
    from pydantic_ai.providers.openai import OpenAIProvider
except ImportError:
    AsyncOpenAI = None  # type: ignore[assignment, misc]
    OpenAIProvider = None  # type: ignore[assignment, misc]

try:
    from groq import AsyncGroq
    from pydantic_ai.providers.groq import GroqProvider
except ImportError:
    AsyncGroq = None
    GroqProvider = None  # type: ignore[assignment, misc]

try:
    from mistralai import Mistral
    from pydantic_ai.providers.mistral import MistralProvider
except ImportError:
    Mistral = None
    MistralProvider = None  # type: ignore[assignment, misc]

try:
    from pydantic_ai.models.anthropic import AnthropicModel
    from anthropic import AsyncAnthropic
    from pydantic_ai.providers.anthropic import AnthropicProvider
except ImportError:
    AnthropicModel = None  # type: ignore[assignment, misc]
    AsyncAnthropic = None
    AnthropicProvider = None  # type: ignore[assignment, misc]



def get_skill_graph_package_name() -> str:
    """
    Returns the package name of skill_graphs.
    """
    return "skill_graphs"


def to_boolean(val) -> bool:
    if isinstance(val, bool):
        return val
    return str(val).lower() in ("true", "1", "t", "y", "yes")


# Default enablement state for specific skill-graphs.
SKILL_DEFAULTS: dict[str, bool] = {
    # Documentation graphs are False by default globally, but can be overridden here if needed.
    #
}


def get_skill_graphs_path(
    name: Optional[str] = None,
    default_enabled: bool = False,
) -> list[str]:
    """
    Returns a list of absolute paths pointing to the individual enabled skill-graphs
    within the repository package.

    Args:
        name: Optional single graph name (e.g. 'django-docs')
    """
    package_name = get_skill_graph_package_name()
    base_dir = files(package_name)

    try:
        with as_file(base_dir) as path:
            abs_root_path = Path(path)
    except Exception:
        return []

    if not abs_root_path.exists():
        return []

    skills_root = abs_root_path / "skills"
    if not skills_root.is_dir():
        return []

    def enabled(graph_dir: Path) -> bool:
        item_name = graph_dir.name
        item_default = SKILL_DEFAULTS.get(item_name, default_enabled)
        env_var_name = f"{item_name.upper().replace('-', '_')}_ENABLE"
        return to_boolean(os.environ.get(env_var_name, item_default))

    graph_dirs = sorted(
        p for p in skills_root.iterdir() if p.is_dir() and (p / "SKILL.md").exists()
    )
    if name:
        graph_dirs = [p for p in graph_dirs if p.name == name]
    return [str(p.resolve()) for p in graph_dirs if enabled(p)]

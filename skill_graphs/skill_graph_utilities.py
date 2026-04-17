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
    AsyncOpenAI = None
    OpenAIProvider = None

try:
    from groq import AsyncGroq
    from pydantic_ai.providers.groq import GroqProvider
except ImportError:
    AsyncGroq = None
    GroqProvider = None

try:
    from mistralai import Mistral
    from pydantic_ai.providers.mistral import MistralProvider
except ImportError:
    Mistral = None
    MistralProvider = None

try:
    from pydantic_ai.models.anthropic import AnthropicModel
    from anthropic import AsyncAnthropic
    from pydantic_ai.providers.anthropic import AnthropicProvider
except ImportError:
    AnthropicModel = None
    AsyncAnthropic = None
    AnthropicProvider = None

__version__ = "0.1.39"


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
SKILL_DEFAULTS = {
    # Documentation graphs are False by default globally, but can be overridden here if needed.
}


def get_skill_graphs_path(
    category: Optional[str] = None,
    name: Optional[str] = None,
    default_enabled: bool = False,
) -> list[str]:
    """
    Returns a list of absolute paths pointing to the individual enabled skill-graphs
    within the repository package.

    Args:
        category: Optional category folder name (e.g. 'python')
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

    enabled_paths = []

    # Helper to check if a directory is a valid graph (contains any files/subdirs and is not a category)
    # For graphs, we usually look for a directory that isn't __pycache__ or a known category
    categories = [
        "python",
        "javascript",
        "database",
        "infra",
        "ai",
        "homelab",
        "languages",
        "php",
        "systems",
    ]

    def is_graph_dir(p: Path) -> bool:
        if not p.is_dir() or p.name in categories or p.name == "__pycache__":
            return False
        # If it contains SKILL.md or matches the naming pattern '-docs'
        return (p / "SKILL.md").exists() or p.name.endswith("-docs")

    # If a specific name is requested, search recursively
    if name:
        for p in abs_root_path.rglob(name):
            if is_graph_dir(p):
                item_default = SKILL_DEFAULTS.get(name, default_enabled)
                env_var_name = f"{name.upper().replace('-', '_')}_ENABLE"
                if to_boolean(os.environ.get(env_var_name, item_default)):
                    enabled_paths.append(str(p.resolve()))
                return enabled_paths
        return []

    # If a category is requested
    if category:
        cat_dir = abs_root_path / category
        if cat_dir.is_dir():
            for graph_dir in cat_dir.iterdir():
                if is_graph_dir(graph_dir):
                    item_name = graph_dir.name
                    item_default = SKILL_DEFAULTS.get(item_name, default_enabled)
                    env_var_name = f"{item_name.upper().replace('-', '_')}_ENABLE"
                    if to_boolean(os.environ.get(env_var_name, item_default)):
                        enabled_paths.append(str(graph_dir.resolve()))
        return enabled_paths

    # Get All
    for p in abs_root_path.rglob("*"):
        if is_graph_dir(p):
            item_name = p.name
            item_default = SKILL_DEFAULTS.get(item_name, default_enabled)
            env_var_name = f"{item_name.upper().replace('-', '_')}_ENABLE"
            if to_boolean(os.environ.get(env_var_name, item_default)):
                enabled_paths.append(str(p.resolve()))

    return enabled_paths

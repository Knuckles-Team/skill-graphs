#!/usr/bin/python
# coding: utf-8

import os
from importlib.resources import files, as_file

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

__version__ = "0.1.28"


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


def _get_enabled_paths(sub_dir: str, default_enabled: bool = True) -> list[str]:
    """
    Helper to return absolute paths of items in a sub-directory that are enabled via env vars.
    Checks inside the package directory.
    """
    try:
        base_dir = files(get_skill_graph_package_name()) / sub_dir
        with as_file(base_dir) as path:
            abs_path = str(path)
    except Exception:
        return []

    enabled_paths = []
    if os.path.exists(abs_path):
        for item in os.listdir(abs_path):
            item_path = os.path.join(abs_path, item)
            if os.path.isdir(item_path):
                # Check for specific override in SKILL_DEFAULTS
                item_default = SKILL_DEFAULTS.get(item, default_enabled)

                env_var_name = f"{item.upper().replace('-', '_')}_ENABLE"
                is_enabled = to_boolean(os.environ.get(env_var_name, item_default))
                if is_enabled:
                    enabled_paths.append(item_path)
    return enabled_paths


def get_skill_graphs_path() -> list[str]:
    """
    Returns a list of absolute paths pointing to the individual enabled skill-graphs
    within the repository package.
    """
    return _get_enabled_paths("skill_graphs", default_enabled=False)

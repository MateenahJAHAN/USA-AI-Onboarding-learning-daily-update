from __future__ import annotations

from typing import Dict

from src.mcp.tools import get_tool_specs


def build_tool_registry() -> Dict[str, dict]:
    return {tool["name"]: tool for tool in get_tool_specs()}

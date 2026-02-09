"""
MCP Tool Registry
==================
Defines tools that agents can invoke through the Model Context Protocol.

Each tool is a simple callable registered by name.  The registry provides
discovery (listing available tools) and invocation by name.
"""

from typing import Any, Callable, Dict, Optional

from src.utils import get_logger

logger = get_logger(__name__)


class ToolRegistry:
    """Registry of named tools available to MCP-compliant agents."""

    def __init__(self):
        self._tools: Dict[str, dict] = {}

    # ── registration ───────────────────────────────────────────────────────

    def register(
        self,
        name: str,
        fn: Callable[..., Any],
        description: str = "",
    ) -> None:
        """Register a callable as a named tool."""
        self._tools[name] = {
            "name": name,
            "description": description,
            "fn": fn,
        }
        logger.info("Registered tool: %s", name)

    # ── discovery ──────────────────────────────────────────────────────────

    def list_tools(self) -> list:
        """Return metadata for all registered tools."""
        return [
            {"name": t["name"], "description": t["description"]}
            for t in self._tools.values()
        ]

    # ── invocation ─────────────────────────────────────────────────────────

    def invoke(self, name: str, **kwargs) -> Any:
        """Invoke a registered tool by name."""
        tool = self._tools.get(name)
        if tool is None:
            raise KeyError(f"Tool '{name}' is not registered")
        logger.info("Invoking tool: %s", name)
        return tool["fn"](**kwargs)


# ── module-level singleton ─────────────────────────────────────────────────

registry = ToolRegistry()

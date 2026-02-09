"""
MCP Context Manager
====================
Manages the context window for multi-step agent interactions following
the Model Context Protocol (MCP) pattern.

Responsibilities:
  - Maintain a rolling conversation history
  - Track token budgets (approximate)
  - Prune older context when the window limit is approached
"""

from typing import List, Optional

from src.utils import get_logger

logger = get_logger(__name__)

# Rough character-to-token ratio (English text)
_CHARS_PER_TOKEN = 4


class ContextManager:
    """Manages conversational context for MCP-compliant agent sessions."""

    def __init__(self, max_tokens: int = 8_000):
        self.max_tokens = max_tokens
        self._messages: List[dict] = []

    # ── public API ─────────────────────────────────────────────────────────

    def add_message(self, role: str, content: str) -> None:
        """Append a message and auto-prune if the budget is exceeded."""
        self._messages.append({"role": role, "content": content})
        self._prune()

    def get_messages(self) -> List[dict]:
        """Return the current context window as a list of messages."""
        return list(self._messages)

    def reset(self) -> None:
        """Clear the context window entirely."""
        self._messages.clear()
        logger.info("Context window reset")

    @property
    def estimated_tokens(self) -> int:
        """Return a rough token count for the current context."""
        total_chars = sum(len(m["content"]) for m in self._messages)
        return total_chars // _CHARS_PER_TOKEN

    # ── internal ───────────────────────────────────────────────────────────

    def _prune(self) -> None:
        """Remove oldest non-system messages until within budget."""
        while self.estimated_tokens > self.max_tokens and len(self._messages) > 1:
            removed = self._messages.pop(0)
            logger.debug("Pruned message (role=%s)", removed["role"])

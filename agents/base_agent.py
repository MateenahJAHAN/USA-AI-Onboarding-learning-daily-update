"""
Abstract base class for all LLM agents.

Subclasses must implement ``invoke()`` at minimum.  The base class provides
shared helpers for building message payloads and calling the OpenAI API.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

import openai

from src.config import config
from src.utils import get_logger

logger = get_logger(__name__)


class BaseAgent(ABC):
    """Base agent that wraps the OpenAI Chat Completions API."""

    def __init__(
        self,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        system_prompt: str = "You are a helpful AI assistant.",
    ):
        self.model = model or config.OPENAI_MODEL
        self.temperature = temperature if temperature is not None else config.OPENAI_TEMPERATURE
        self.system_prompt = system_prompt

        # Configure the OpenAI client
        openai.api_key = config.OPENAI_API_KEY

    # ── helpers ────────────────────────────────────────────────────────────

    def _build_messages(
        self,
        user_message: str,
        history: Optional[List[dict]] = None,
    ) -> List[dict]:
        """Construct the messages list for a Chat Completion call."""
        messages = [{"role": "system", "content": self.system_prompt}]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": user_message})
        return messages

    def _call_llm(self, messages: List[dict]) -> str:
        """Send messages to the OpenAI API and return the assistant reply."""
        logger.info("Calling %s (temp=%.2f) …", self.model, self.temperature)
        response = openai.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=config.OPENAI_MAX_TOKENS,
        )
        return response.choices[0].message.content.strip()

    # ── public interface ───────────────────────────────────────────────────

    @abstractmethod
    def invoke(self, prompt: str) -> str:
        """Run the agent on a single user prompt and return the result."""
        ...

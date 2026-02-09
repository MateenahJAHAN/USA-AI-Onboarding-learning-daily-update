"""
OpenAI API wrapper — thin helper around Chat Completion.

Consolidates patterns from the Day 8 / Day 10 / Day 12 scripts into a
single, reusable function with proper error handling.
"""

from __future__ import annotations

import json
import logging
from typing import Optional

import requests

logger = logging.getLogger(__name__)

_CHAT_COMPLETIONS_URL = "https://api.openai.com/v1/chat/completions"


def call_chat_completion(
    api_key: str,
    user_message: str,
    system_message: Optional[str] = None,
    model: str = "gpt-4",
    temperature: float = 0.2,
    max_tokens: int = 2048,
) -> str:
    """
    Call the OpenAI Chat Completion API and return the assistant's reply.

    Parameters
    ----------
    api_key : str
        OpenAI API key.
    user_message : str
        The user-role message content.
    system_message : str, optional
        The system-role message content.
    model : str
        Model identifier (e.g. ``"gpt-4"``, ``"gpt-3.5-turbo"``).
    temperature : float
        Sampling temperature.
    max_tokens : int
        Maximum tokens in the response.

    Returns
    -------
    str
        The text content of the assistant's reply.

    Raises
    ------
    RuntimeError
        If the API returns a non-200 status code.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": user_message})

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    response = requests.post(
        _CHAT_COMPLETIONS_URL,
        headers=headers,
        data=json.dumps(payload),
        timeout=60,
    )

    if response.status_code != 200:
        logger.error("OpenAI API error %s: %s", response.status_code, response.text)
        raise RuntimeError(
            f"OpenAI API returned {response.status_code}: {response.text}"
        )

    result = response.json()
    return result["choices"][0]["message"]["content"]

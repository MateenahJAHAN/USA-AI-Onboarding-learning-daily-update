"""
GitHub API helper — issue lifecycle (GET, POST, PATCH, CLOSE).

Consolidated from the Day 10 scripts into a single reusable client.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, Optional

import requests

logger = logging.getLogger(__name__)

_BASE_URL = "https://api.github.com"


class GitHubClient:
    """Lightweight GitHub API client scoped to a single repository."""

    def __init__(self, token: str, owner: str, repo: str):
        self.token = token
        self.owner = owner
        self.repo = repo
        self._headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        }

    # ------------------------------------------------------------------
    # Issue operations
    # ------------------------------------------------------------------

    def get_issue(self, issue_number: int) -> Dict[str, Any]:
        """Fetch a single issue by number."""
        url = f"{_BASE_URL}/repos/{self.owner}/{self.repo}/issues/{issue_number}"
        resp = requests.get(url, headers=self._headers, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def create_issue(
        self, title: str, body: str = "", labels: Optional[list] = None
    ) -> Dict[str, Any]:
        """Create a new issue."""
        url = f"{_BASE_URL}/repos/{self.owner}/{self.repo}/issues"
        payload: Dict[str, Any] = {"title": title, "body": body}
        if labels:
            payload["labels"] = labels
        resp = requests.post(url, headers=self._headers, json=payload, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def update_issue(
        self, issue_number: int, **fields: Any
    ) -> Dict[str, Any]:
        """Update (PATCH) an existing issue. Pass any updatable fields as kwargs."""
        url = f"{_BASE_URL}/repos/{self.owner}/{self.repo}/issues/{issue_number}"
        resp = requests.patch(url, headers=self._headers, json=fields, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def close_issue(self, issue_number: int) -> Dict[str, Any]:
        """Close an issue by setting its state to 'closed'."""
        return self.update_issue(issue_number, state="closed")

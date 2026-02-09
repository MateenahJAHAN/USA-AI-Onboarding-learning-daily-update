"""
DocumentParserAgent
====================
Pre-processes raw documents (plain text or PDF) before they are handed off
to downstream extraction agents.

Currently supports:
  - Plain-text normalisation (whitespace, encoding)
  - Placeholder for PDF-to-text conversion (OCR)

Future:
  - Tesseract OCR integration
  - AWS Textract support
"""

import re
from typing import Optional

from src.utils import get_logger

logger = get_logger(__name__)


class DocumentParserAgent:
    """Lightweight document pre-processing agent."""

    # ── public API ─────────────────────────────────────────────────────────

    def parse(self, raw_input: str, source_type: str = "text") -> str:
        """
        Clean and normalise a raw document.

        Parameters
        ----------
        raw_input : str
            The raw document content (text or future: base64-encoded PDF).
        source_type : str
            One of ``"text"`` or ``"pdf"`` (pdf support is a placeholder).

        Returns
        -------
        str
            Cleaned, normalised plain text ready for extraction.
        """
        if source_type == "pdf":
            text = self._pdf_to_text(raw_input)
        else:
            text = raw_input

        text = self._normalise(text)
        logger.info("Parsed document — %d characters", len(text))
        return text

    # ── internal helpers ───────────────────────────────────────────────────

    @staticmethod
    def _normalise(text: str) -> str:
        """Collapse excess whitespace and strip control characters."""
        text = re.sub(r"\r\n?", "\n", text)          # normalise line endings
        text = re.sub(r"[ \t]+", " ", text)           # collapse horizontal space
        text = re.sub(r"\n{3,}", "\n\n", text)        # collapse blank lines
        return text.strip()

    @staticmethod
    def _pdf_to_text(raw_input: str) -> str:
        """
        Placeholder for PDF ingestion.

        In a production system this would decode a base64 payload, run OCR
        (Tesseract / Textract), and return plain text.
        """
        logger.warning("PDF parsing is not yet implemented — returning raw input")
        return raw_input

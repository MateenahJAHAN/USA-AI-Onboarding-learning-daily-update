from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


def load_pdf_text(path: str) -> str:
    file_path = Path(path)
    if file_path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported.")

    reader = PdfReader(str(file_path))
    pages_text = []
    for page in reader.pages:
        pages_text.append(page.extract_text() or "")

    return "\n".join(pages_text).strip()


from pathlib import Path

import fitz
from docx import Document

from app.utils.text_utils import clean_text


class FileParserService:
    def parse(self, path: str) -> str:
        p = Path(path)
        suffix = p.suffix.lower()

        if suffix == ".pdf":
            return self._pdf(p)

        if suffix == ".docx":
            return self._docx(p)

        if suffix == ".txt":
            text = p.read_text(
                encoding="utf-8",
                errors="ignore"
            )
            return clean_text(text)

        raise ValueError(
            "Unsupported file type. Upload PDF, DOCX, or TXT."
        )

    def _pdf(self, p: Path) -> str:
        lines = []

        with fitz.open(p) as doc:
            for page in doc:
                lines.append(page.get_text())

        return clean_text("\n".join(lines))

    def _docx(self, p: Path) -> str:
        doc = Document(p)
        lines = [paragraph.text for paragraph in doc.paragraphs]

        return clean_text("\n".join(lines))

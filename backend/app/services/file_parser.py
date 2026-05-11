from pathlib import Path
import fitz
from docx import Document
from app.utils.text_utils import clean_text
class FileParserService:
    def parse(self, path: str) -> str:
        p=Path(path); s=p.suffix.lower()
        if s=='.pdf': return self._pdf(p)
        if s=='.docx': return self._docx(p)
        if s=='.txt': return clean_text(p.read_text(encoding='utf-8', errors='ignore'))
        raise ValueError('Unsupported file type. Upload PDF, DOCX, or TXT.')
    def _pdf(self,p):
        out=[]
        with fitz.open(p) as doc:
            for page in doc: out.append(page.get_text())
        return clean_text('
'.join(out))
    def _docx(self,p):
        doc=Document(p); return clean_text('
'.join(x.text for x in doc.paragraphs))

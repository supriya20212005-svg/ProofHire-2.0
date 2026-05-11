import re
def clean_text(text: str) -> str:
    if not text: return ""
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
def normalize(text: str) -> str: return clean_text(text).lower()
def extract_bullets(text: str) -> list[str]:
    bullets=[]
    for line in text.splitlines():
        line=line.strip()
        if line.startswith(("•","-","*")): bullets.append(line.lstrip("•-* ").strip())
    if not bullets:
        bullets=[c.strip() for c in re.split(r"(?<=[.!?])\s+", clean_text(text)) if len(c.strip())>35]
    return bullets[:20]
def extract_sections(text: str) -> dict:
    names=["skills","projects","experience","education","certifications","achievements"]
    sections={n:"" for n in names}; current=None
    for raw in text.splitlines():
        key=raw.strip().lower().replace(":","")
        if key in names: current=key; continue
        if current: sections[current]+=raw+"\n"
    return sections

import re
from app.utils.text_utils import clean_text, extract_bullets, extract_sections, normalize
SKILLS=["Java","Python","C++","C#","JavaScript","TypeScript","SQL","Spring Boot","FastAPI","React","REST APIs","Microservices","MySQL","PostgreSQL","Redis","Kafka","Docker","Kubernetes","AWS","Azure","Linux","CI/CD","GitHub Actions","JUnit","Pytest","Unit Testing","Integration Testing","System Design","Distributed Systems","Concurrency","Fault Tolerance","Rate Limiting","Distributed Locking","Leader Election","DLQ","RAG","LLM","Embeddings","pgvector","Semantic Search","OpenTelemetry","Grafana","Machine Learning","Artificial Intelligence","OOP","DBMS","Operating Systems","Computer Networks"]
class ExtractionService:
    def extract_skills(self,text):
        low=normalize(text); found=[]
        for skill in SKILLS:
            pattern=r"\b"+re.escape(skill.lower()).replace('\\ ',r"\s+")+r"\b"
            if re.search(pattern,low): found.append(skill)
        return sorted(set(found), key=str.lower)
    def extract_keywords(self,text,limit=40):
        words=re.findall(r"[a-zA-Z][a-zA-Z+#./-]{2,}", normalize(text))
        stop={"and","the","for","with","this","that","from","into","role","work","team","will","have","using","build","built","are","job","you","our","your","their","candidate","experience"}
        freq={}
        for w0 in words:
            if w0 not in stop: freq[w0]=freq.get(w0,0)+1
        return [w for w,_ in sorted(freq.items(), key=lambda x:x[1], reverse=True)[:limit]]
    def extract_projects(self,text):
        sections=extract_sections(text); ptext=sections.get('projects') or text
        chunks=re.split(r"\n(?=[A-Z][A-Za-z0-9 .&/-]{3,80})", ptext)
        projects=[]
        for ch in chunks:
            c=clean_text(ch)
            if len(c)<60: continue
            lines=[l.strip() for l in c.splitlines() if l.strip()]
            projects.append({'name':lines[0][:90], 'text':c, 'skills':self.extract_skills(c), 'bullets':extract_bullets(c)})
        if not projects: projects.append({'name':'Resume Projects','text':ptext,'skills':self.extract_skills(ptext),'bullets':extract_bullets(ptext)})
        return projects[:8]
    def parse_resume(self,text):
        sections=extract_sections(text)
        return {'skills':self.extract_skills(text),'keywords':self.extract_keywords(text),'projects':self.extract_projects(text),'sections':sections,'bullets':extract_bullets(text),'summary':clean_text(text)[:800]}
    def parse_job_description(self,text,role=''):
        return {'role_type':role,'required_skills':self.extract_skills(text),'keywords':self.extract_keywords(text),'responsibilities':extract_bullets(text),'summary':clean_text(text)[:900]}

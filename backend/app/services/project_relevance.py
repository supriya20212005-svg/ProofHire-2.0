from app.services.embedding import EmbeddingService
class ProjectRelevanceService:
    def __init__(self): self.embedding=EmbeddingService()
    def score_projects(self,projects,job):
        jd=' '.join(job.get('required_skills',[])+job.get('keywords',[]))+' '+job.get('summary',''); req={s.lower() for s in job.get('required_skills',[])}; res=[]
        for p in projects:
            pskills={s.lower() for s in p.get('skills',[])}; overlap=len(req&pskills)/len(req) if req else 0; sem=max(0,self.embedding.cosine(p.get('text',''),jd)); score=round(min(100,overlap*65+sem*35+10),2)
            matched=sorted(req&pskills); missing=sorted(req-pskills)
            reason = f"Strong role alignment due to evidence for {', '.join(matched[:5])}." if score>=80 else f"Moderate alignment; strong in {', '.join(matched[:4])}, but missing {', '.join(missing[:3])}." if score>=60 else f"Weak alignment; needs clearer evidence for {', '.join(missing[:4])}."
            res.append({'project':p.get('name','Project'),'score':score,'matched_requirements':matched,'missing_requirements':missing[:8],'reason':reason})
        return sorted(res,key=lambda x:x['score'], reverse=True)

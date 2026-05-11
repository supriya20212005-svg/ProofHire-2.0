from app.services.embedding import EmbeddingService
class EvidenceGraphService:
    def __init__(self): self.embedding=EmbeddingService()
    def build(self,resume_data):
        graph=[]
        for skill in resume_data.get('skills',[]):
            evidence=[]
            for p in resume_data.get('projects',[]):
                text=p.get('text','')
                if skill.lower() in text.lower(): evidence.append({'project':p.get('name','Project'),'evidence_text':self._line(skill,p),'confidence_score':0.92})
                else:
                    sim=self.embedding.cosine(skill,text)
                    if sim>0.18: evidence.append({'project':p.get('name','Project'),'evidence_text':self._line(skill,p),'confidence_score':round(min(0.70,sim+0.35),2)})
            if evidence:
                best=max(evidence,key=lambda x:x['confidence_score']); strength='HIGH' if best['confidence_score']>=0.8 else 'MEDIUM'
                graph.append({'skill':skill,'claim_strength':strength,'confidence_score':best['confidence_score'],'evidence':evidence[:3]})
            else: graph.append({'skill':skill,'claim_strength':'LOW','confidence_score':0.18,'evidence':[]})
        return graph
    def _line(self,skill,p):
        for b in p.get('bullets',[]):
            if skill.lower() in b.lower(): return b
        return (p.get('bullets') or [p.get('text','')[:180]])[0]

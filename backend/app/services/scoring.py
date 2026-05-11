class ScoringEngine:
    def keyword_score(self,a,b):
        A={x.lower() for x in a}; B={x.lower() for x in b}
        if not B: return 0.0,[],[]
        return round(len(A&B)/len(B)*100,2), sorted(A&B), sorted(B-A)
    def skill_score(self,a,b): return self.keyword_score(a,b)
    def project_evidence_score(self,g): return round(sum(x.get('confidence_score',0) for x in g)/len(g)*100,2) if g else 0.0
    def claim_support_score(self,g):
        if not g: return 0.0
        high=sum(1 for x in g if x.get('claim_strength')=='HIGH'); med=sum(1 for x in g if x.get('claim_strength')=='MEDIUM')
        return round((high+0.6*med)/len(g)*100,2)
    def interview_readiness_score(self,unsupported_count,projects):
        avg=sum(p['score'] for p in projects)/len(projects) if projects else 0
        return round(max(0,avg-min(35,unsupported_count*4)),2)
    def resume_quality_score(self,resume):
        score=50
        if len(resume.get('skills',[]))>=8: score+=15
        if len(resume.get('projects',[]))>=2: score+=15
        if len(resume.get('bullets',[]))>=5: score+=10
        if resume.get('sections',{}).get('education'): score+=10
        return min(score,100)
    def overall(self,skill,keyword,project,claim,semantic,interview,quality): return round(0.25*skill+0.10*keyword+0.20*project+0.15*claim+0.15*semantic+0.10*interview+0.05*quality,2)

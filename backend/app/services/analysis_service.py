from app.services.evidence_graph import EvidenceGraphService
from app.services.claim_verifier import ClaimVerifierService
from app.services.project_relevance import ProjectRelevanceService
from app.services.scoring import ScoringEngine
from app.services.embedding import EmbeddingService
from app.services.interview_risk import InterviewRiskService
from app.services.bullet_improver import BulletImproverService
from app.services.rag_feedback import RAGFeedbackService
class AnalysisService:
    def __init__(self):
        self.evidence=EvidenceGraphService(); self.claim=ClaimVerifierService(); self.project=ProjectRelevanceService(); self.score=ScoringEngine(); self.embed=EmbeddingService(); self.interview=InterviewRiskService(); self.bullet=BulletImproverService(); self.feedback=RAGFeedbackService()
    def analyze(self,resume_text,resume,job_text,job):
        graph=self.evidence.build(resume); unsupported=self.claim.detect_unsupported_claims(graph); projects=self.project.score_projects(resume.get('projects',[]),job)
        skill,_,miss_s=self.score.skill_score(resume.get('skills',[]),job.get('required_skills',[])); keyword,_,miss_k=self.score.keyword_score(resume.get('keywords',[]),job.get('keywords',[]))
        pe=self.score.project_evidence_score(graph); cs=self.score.claim_support_score(graph); sem=round(max(0,self.embed.cosine(resume_text,job_text))*100,2); ir=self.score.interview_readiness_score(len(unsupported),projects); q=self.score.resume_quality_score(resume); missing=sorted(set(miss_s+miss_k)); overall=self.score.overall(skill,keyword,pe,cs,sem,ir,q)
        return {'overall_readiness_score':overall,'skill_match_score':skill,'keyword_match_score':keyword,'project_evidence_score':pe,'claim_support_score':cs,'semantic_similarity_score':sem,'interview_readiness_score':ir,'resume_quality_score':q,'skill_evidence_graph':graph,'unsupported_claims':unsupported,'missing_keywords':missing,'project_relevance':projects,'interview_risks':self.interview.generate(graph,unsupported,job.get('required_skills',[])),'improved_bullets':self.bullet.improve(resume,missing),'feedback':self.feedback.generate(overall,unsupported,projects,missing),'audit_events':[{'event':'RESUME_PARSED'},{'event':'JOB_DESCRIPTION_PARSED'},{'event':'SKILL_EVIDENCE_GRAPH_GENERATED'},{'event':'UNSUPPORTED_CLAIMS_DETECTED','count':len(unsupported)},{'event':'ANALYSIS_COMPLETED','overall_score':overall}]}

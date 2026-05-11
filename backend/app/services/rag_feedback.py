class RAGFeedbackService:
    def generate(self,overall,unsupported,projects,missing):
        verdict='Strong match' if overall>=80 else 'Moderate match' if overall>=60 else 'Needs improvement'
        top=projects[0]['project'] if projects else 'No project detected'
        u=', '.join(c['skill'] for c in unsupported[:5]) or 'No major unsupported claims'
        m=', '.join(missing[:8]) or 'No major missing keywords'
        return f'{verdict}. Top aligned project: {top}. Unsupported claims: {u}. Missing keywords: {m}. Recommendation: backend bullets should mention APIs, database schema, testing, deployment, scalability, and failure handling. Every listed skill should have project evidence if likely to be asked in interviews.'

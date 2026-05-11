class InterviewRiskService:
    def generate(self,graph,unsupported,job_skills):
        risks=[]; job={s.lower() for s in job_skills}
        for c in unsupported[:5]:
            s=c['skill']; risks.append({'topic':s,'risk_level':'HIGH','reason':c['reason'],'questions':[f'Where exactly did you use {s} in your project?',f'What implementation challenges did you face with {s}?',f'Can you explain the architecture involving {s}?',f'What would happen if {s} failed in production?']})
        for item in graph:
            if item['claim_strength']=='HIGH' and item['skill'].lower() in job:
                s=item['skill']; risks.append({'topic':s,'risk_level':'MEDIUM','reason':f'{s} is strongly evidenced and likely to be discussed in interviews.','questions':[f'Why did you choose {s} for this project?',f'How does {s} improve reliability or scalability?',f'What trade-offs did you consider while using {s}?',f'How would you debug issues related to {s}?']})
        return risks[:10]

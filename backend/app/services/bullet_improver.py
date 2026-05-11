class BulletImproverService:
    def improve(self,resume,missing):
        hint=', '.join(missing[:4]) if missing else 'testing, deployment, reliability'; out=[]
        for b in resume.get('bullets',[])[:6]:
            c=b.strip().rstrip('.')
            out.append({'original':c,'improved':f'{c}; strengthened the implementation with {hint}, API validation, persistence design, and measurable reliability checks.'})
        if not out: out.append({'original':'Built backend application.','improved':f'Built a backend application with REST APIs, database schema design, {hint}, Docker deployment, and integration testing.'})
        return out

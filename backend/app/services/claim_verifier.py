class ClaimVerifierService:
    def detect_unsupported_claims(self,graph):
        out=[]
        for item in graph:
            if item['claim_strength']=='LOW':
                s=item['skill']; out.append({'skill':s,'reason':f'{s} is listed in skills but no strong project evidence was found.','risk_level':'HIGH','suggestion':f'Add concrete project evidence for {s} or remove the claim before applying.'})
        return out[:10]

import hashlib, numpy as np
class EmbeddingService:
    def embed(self,text,dimensions=384):
        v=np.zeros(dimensions,dtype=float)
        for tok in text.lower().split():
            d=hashlib.sha256(tok.encode()).digest(); idx=int.from_bytes(d[:4],'little')%dimensions; sign=1 if d[4]%2==0 else -1; v[idx]+=sign
        n=np.linalg.norm(v)
        if n: v=v/n
        return v.tolist()
    def cosine(self,left,right):
        a=np.array(self.embed(left)); b=np.array(self.embed(right)); den=np.linalg.norm(a)*np.linalg.norm(b)
        return 0.0 if den==0 else float(np.dot(a,b)/den)

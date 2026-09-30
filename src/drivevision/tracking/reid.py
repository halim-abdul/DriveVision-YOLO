import numpy as np

def cosine_distance(a,b):
    a=np.asarray(a,float); b=np.asarray(b,float)
    denom=np.linalg.norm(a)*np.linalg.norm(b)+1e-12
    return 1.0-float(a@b/denom)

class AppearanceEncoder:
    """Pluggable ReID encoder interface for future learned embeddings."""
    def encode(self,crops):
        raise NotImplementedError

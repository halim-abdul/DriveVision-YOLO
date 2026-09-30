def mota(fp,fn,id_switches,gt):
    return 1.0-(fp+fn+id_switches)/max(gt,1)

def id_precision(idtp,idfp):return idtp/max(idtp+idfp,1)
def id_recall(idtp,idfn):return idtp/max(idtp+idfn,1)
def idf1(idtp,idfp,idfn):
    p=id_precision(idtp,idfp);r=id_recall(idtp,idfn)
    return 2*p*r/max(p+r,1e-12)

def binary_iou(pred,target):
    p=pred.astype(bool);t=target.astype(bool)
    inter=(p&t).sum();union=(p|t).sum()
    return float(inter/max(union,1))

def dice(pred,target):
    p=pred.astype(bool);t=target.astype(bool)
    return float(2*(p&t).sum()/max(p.sum()+t.sum(),1))

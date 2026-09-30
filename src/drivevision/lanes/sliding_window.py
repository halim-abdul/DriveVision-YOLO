import numpy as np

def lane_pixels(binary,nwindows=9,margin=80,minpix=40):
    histogram=np.sum(binary[binary.shape[0]//2:,:],axis=0)
    mid=histogram.shape[0]//2
    left=int(np.argmax(histogram[:mid]));right=int(np.argmax(histogram[mid:])+mid)
    ys,xs=binary.nonzero();h=binary.shape[0];win=h//nwindows
    li=[];ri=[]
    for w in range(nwindows):
        y0=h-(w+1)*win;y1=h-w*win
        l=np.where((ys>=y0)&(ys<y1)&(xs>=left-margin)&(xs<left+margin))[0]
        r=np.where((ys>=y0)&(ys<y1)&(xs>=right-margin)&(xs<right+margin))[0]
        li.append(l);ri.append(r)
        if len(l)>minpix:left=int(np.mean(xs[l]))
        if len(r)>minpix:right=int(np.mean(xs[r]))
    return xs[np.concatenate(li)],ys[np.concatenate(li)],xs[np.concatenate(ri)],ys[np.concatenate(ri)]

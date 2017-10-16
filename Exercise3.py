import numpy as np
sx=[[0,1],[1,0]]
sy=[[0,-1j],[1j,0]]
sz=[[1,0],[0,-1]]
h=np.zeros((1024,1024))
l=[[1,0],[0,1]]
for i in range(9):
    px=np.kron(sx,sx)
    py=np.kron(sy,sy)
    pz=np.kron(sz,sz)
    for j in range(i):
         px=np.kron(l,px)
         py=np.kron(l,py)
         pz=np.kron(l,pz)
    for m in range(8-i):
        px=np.kron(px,l)
        py=np.kron(py,l)
        pz=np.kron(pz,l)
    h=np.add(h,px)
    h=np.add(h,py)
    h=np.add(h,pz)
px=sx
py=sy
pz=sz
for i in range(8):
    px=np.kron(px,l)
    py=np.kron(py,l)
    pz=np.kron(pz,l)
px=np.kron(px,sx)
py=np.kron(py,sy)
pz=np.kron(pz,sz)
h=np.add(h,px)                       
h=np.add(h,py)                       
h=np.add(h,pz)                       
h=0.25*h
print(np.linalg.eig(h))                      

import numpy as np
sx=[[0,1],[1,0]]
sy=[[0,-1j],[1j,0]]
sz=[[1,0],[0,-1]]
I=[[1,0],[0,1]]
sx=0.5*np.array(sx)
sy=0.5*np.array(sy)
sz=0.5*np.array(sz)
h=np.zeros((1024,1024),dtype=np.complex64)
for k in range(0,9):
    Ibsx=np.array([1])
    Ibsy=np.array([1])
    Ibsz=np.array([1])
    for l in range(0,k):
        Ibsx=np.kron(Ibsx,I)
        Ibsy=np.kron(Ibsy,I)
        Ibsz=np.kron(Ibsz,I)    
    s1=np.array(Ibsx)
    s2=np.array(Ibsy)
    s3=np.array(Ibsz)
    for l in range(0,2):
        s1=np.kron(s1,sx)
        s2=np.kron(s2,sy)
        s3=np.kron(s3,sz)
    for l in range(0,8-k):
        s1=np.kron(s1,I)
        s2=np.kron(s2,I)
        s3=np.kron(s3,I)
    h=np.add(h,s1)
    h=np.add(h,s2)
    h=np.add(h,s3)
Ibsx=np.kron(sx,I)
Ibsy=np.kron(sy,I)
Ibsz=np.kron(sz,I)   
for l in range(0,7):
        Ibsx=np.kron(Ibsx,I)
        Ibsy=np.kron(Ibsy,I)
        Ibsz=np.kron(Ibsz,I)
Ibsx=np.kron(Ibsx,sx)
Ibsy=np.kron(Ibsy,sy)
Ibsz=np.kron(Ibsz,sz)
h=np.add(h,Ibsx)
h=np.add(h,Ibsy)
h=np.add(h,Ibsz)
h1=np.linalg.eig(h)
k1=np.zeros((1024,1024))
pz=[[1,0],[0,-1]]
for l in range(9):
    pz=np.kron(pz,I)
pz2=np.transpose(pz)   #swap rows & c columns    
for t in range(1024):    
    pz=np.dot(pz2[t],pz)
for l in range(0,500,5):
    Beta=l/100
    ZB=np.trace(np.exp(-Beta*h))  
    for t in range(1024):
        en=h1[0][t]
        so=np.dot(pz,np.exp(-Beta*en))
        k1=np.add(k1,so/ZB)      
print(k1)                     

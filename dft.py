import numpy as np
import cmath as c
import matplotlib.pyplot as plt
#j=c.sqrt(-1)
N=input("number of dft ponts")
k=np.arange(0,N)
n1=np.arange(0,N)
x1=input("enter values")#ex:a=[1,2,3]
z=len(x1)
if z<N:
	q=N-z
	x1=np.append(x1,np.zeros(q))
y=[]
M=[]
P=[]
for i in k:
	sum=0;
	for j in n1:
		sum+=x1[j]*np.exp(-1*2*np.pi*1j*i*j/np.float(N))
	y.append(sum)
	M.append(np.abs(sum))
	P.append(np.angle(sum))
#print y
plt.subplot(311)
plt.stem(k,x1)
plt.subplot(312)
plt.stem(k,M)
plt.subplot(313)
plt.stem(k,P)
plt.show()

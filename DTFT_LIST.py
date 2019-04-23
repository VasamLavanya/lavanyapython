import numpy as np
import cmath as c
import matplotlib.pyplot as plt
w=np.linspace(-1*np.pi,np.pi,1000)
j=c.sqrt(-1)
#t=np.arange(-400,400,1)
#fs=100
#x=np.sin(2*np.pi*40.0/fs*t)
x=input('enter values')#a=[1,2,3]
z=len(x)
y=[]
M=[]
P=[]
for r in range(1000):
	W=w[r]
	X=0
	for n in range(z):
		X+=x[n]*np.exp(-j*W*n)
	y.append(X)
	M.append(abs(X))
	P.append(np.angle(X))
	#P.append(X)
plt.subplot(311)
plt.plot(w,y)
plt.subplot(312)
plt.plot(w,M)
plt.subplot(313)
plt.plot(w,P)
plt.show()
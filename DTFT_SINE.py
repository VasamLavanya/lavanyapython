import numpy as np
import cmath as c
import matplotlib.pyplot as plt
w=np.linspace(-1*np.pi,np.pi,500)
j=c.sqrt(-1)
t=np.arange(-200,200,1)
fs=100
x=np.sin(2*np.pi*20.0/fs*t)
#x=input('enter values')#a=[1,2,3]
X=[]
for i in w:
	sum=0;p=0;
	for j in t:
		sum=sum+x[j]*np.exp(-1*1j*i*j)
		#p=p+1;
	X.append(sum)
X_mag=np.abs(X)
X_phase=np.angle(X)
plt.subplot(311)
plt.plot(t,x)
plt.subplot(312)
plt.plot(w,X_mag)
plt.subplot(313)
plt.plot(w,X_phase)
plt.show()
import numpy as np
from matplotlib import pyplot as plt
def convolute(x,h):
	z=len(x)+len(h)-1
	w=len(x)
	r=len(h)
	u=[]
	for n in range(z):
		q=0
		for k in range(w):
			if n-k<r and n-k>=0:
				q +=x[k]*(h[n-k])
		u.append(q)
	return u
def time_rev(x):
	l=len(x)
	g=[]
	s=l-1
	for i in range(l):
		p=x[s-i]
		g.append(p)
	return g
n=np.arange(0,500)
x=np.sin(2*np.pi*20.0/400.0*n)
N1=np.random.rand(x.shape[0])
X_N=x+N1
h=[1.0/3.0,1.0/3.0,1.0/3.0]
y1=convolute(h,X_N)
y2=convolute(X_N,time_rev(x))
y3=convolute(X_N,time_rev(X_N))
plt.subplot(611)
plt.plot(x)
plt.subplot(612)
plt.plot(N1)
plt.subplot(613)
plt.plot(X_N)
plt.subplot(614)
plt.plot(y1)
plt.subplot(615)
plt.plot(y2)
plt.subplot(616)
plt.plot(y3)
plt.show()




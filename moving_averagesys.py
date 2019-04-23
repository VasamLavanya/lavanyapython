import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
p=input("enter the order of the moving average system")
Fs=4000
f1=10
f2=400
y=np.zeros(200)
t=np.linspace(0,400,200)
u=np.sin(2*np.pi*f1*t/Fs)
v=np.sin(2*np.pi*f2*t/Fs)
x=u+v
sum=0
for i in range(0,200,1):
	for k in range(0,p-1,1):
		sum=sum+x[i-k]
	print sum
	y[i]=float((sum)/(p))
	sum=0
print y
plt.subplot(411)
plt.plot(t,u)
plt.subplot(412)
plt.plot(t,v)
plt.subplot(413)
plt.plot(t,x)
plt.subplot(414)
plt.plot(t,y)
plt.show()



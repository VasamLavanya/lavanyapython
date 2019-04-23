import matplotlib.pyplot as plt
import numpy as np
fs=8000
f1=500
f2=600
n=100
a1=5

p1=60
p2=30

x=np.arange(n)
y1=np.sin((2*np.pi*f1*x/fs)+p1)
plt.subplot(511)
plt.plot(x,(a1*y1))
y2=np.sin((2*np.pi*f1*x/fs)+p2)
plt.subplot(512)
plt.plot(x,(a1*y2))
y3=np.sin((2*np.pi*f2*x/fs)+p1)
plt.subplot(513)
plt.plot(x,a1*y3)
y4=np.sin((2*np.pi*f2*x/fs)+p2)
plt.subplot(514)
plt.plot(x,a1*y4)
z=a1*(y1+y2+y3+y4)
plt.subplot(515)
plt.plot(x,z)

plt.show() 

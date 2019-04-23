import matplotlib.pyplot as plt
import numpy as np
fs=8000
f1=100

n=100
a1=5

p1=60
p2=30
x=np.arange(n)
y1=np.sin((2*np.pi*f1*x/fs)+p1)
plt.subplot(311)
plt.plot(x,a1*y1)
y2=np.sin((2*np.pi*f1*x/fs)+p2)
plt.subplot(312)
plt.plot(x,a1*y2)
z=(a1*y1)+(a1*y2)
plt.subplot(313)
plt.plot(x,z)
plt.xlabel('x')
plt.ylabel('y')
plt.show() 

import matplotlib.pyplot as plt
import numpy as np
fs=8000
f1=600

n=100
a1=5
a2=10
p=60
x=np.arange(n)
y1=np.sin((2*np.pi*f1*x/fs)+p)
plt.subplot(311)
plt.plot(x,a1*y1)
y2=np.sin((2*np.pi*f1*x/fs)+p)
plt.subplot(312)
plt.plot(x,a2*y2)
z=(a1*y1)+(a2*y2)
plt.subplot(313)
plt.plot(x,z)
plt.show() 

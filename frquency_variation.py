import matplotlib.pyplot as plt
import numpy as np
fs=8000
f1=600
f2=500
n=200
x=np.arange(n)
y1=np.sin(2*np.pi*f1*x/fs)
plt.subplot(311)
plt.plot(x,y1)
y2=np.sin(2*np.pi*f2*x/fs)
plt.subplot(312)
plt.plot(x,y2)
z=y1+y2
plt.subplot(313)
plt.plot(x,z)
plt.show() 

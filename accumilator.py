import numpy as np
from matplotlib import pyplot as plt
n=input('number of inputs:')
y=0
k=[]
a=[]
for j in range(0,n):
	x=input('enter value')
	k.append(x)
	y+=x
	a.append(y)
print(y)
print k
print a
plt.stem(k,a)
plt.show()

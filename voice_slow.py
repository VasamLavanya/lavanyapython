import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs1,data=wav.read('kav.wav')
print(fs1,len(data),data)
wav.write('hello2.wav',0.5*fs1,data)
plt.plot(data)
plt.show()
#print(fs2,len(data),data)
#plt.subplot(211)
#plt.plot(data)
#t=np.arange(0,len(data)/fs,1.0/fs)
#plt.subplot(212)
#plt.plot(t,data)
#plt.show()
#wav.write('nav1-slow.wav',0.5*fs2,data)
#data1=np.array(data1,dtype='unit8')
#t1=np.arange(0,len(data)/np.float(fs2),1.0/fs1)
#print(fs,len(data),t1)

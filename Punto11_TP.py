import numpy as np
import scipy.signal 
import librosa as lb
import matplotlib.pyplot as plt
###############################################################################
def pdsexp(F0, R, Ar, phi_r, fs, t):
    x = []
    xt = []
    n = np.arange(0,t,1/fs); 
    for r in range(0,R): 
        x.append(Ar[r]*np.exp(1j*2*np.pi*r*F0*n + phi_r[r]))
    xt = [sum(i) for i in zip(*x)]        
    return n,np.real(xt),np.imag(xt);
###############################################################################
fs = 44100 
t = 2 
F0 = 440 
R = 5
Ar = [1, 1/2, 1/3, 1/4, 1/5] 
phi_r = [0, 0, 0, 0, 0] 
###############################################################################   
n,x,xI = pdsexp (F0, R, Ar, phi_r, fs, t)

h, fsRI = lb.load("resp_imp.wav",sr=None)

y1 = scipy.convolve(x,h)

y2 = scipy.signal.fftconvolve(x,h, mode = 'full')
n = np.arange(1,len(y1),1)
plt.subplot(2,1,1)
plt.plot(n[100:400],y1[100:400])
plt.subplot(2,1,2)
plt.plot(n[100:400],y2[100:400])
plt.show()

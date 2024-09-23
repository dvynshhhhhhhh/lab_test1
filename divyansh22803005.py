import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
pollution_data=np.random.normal(10,60,1440)
ran_noise=np.random.random(1440)
totalnoises=pollution_data + ran_noise
fs=200
cut_off=0.5
d,e2= signal.butter(4,cut_off,fs=fs,btype='lowpass')
smooth=signal.filtfilt(d,e,totalnoises)
def avrg(smooth):
    avg=[np.average(i) for i in range (0,len(smooth),60)]
    print('PM2.5 LEVELS EACH HOUR:',avg)
    
avrg(smooth)

plt.subplot(1,2,1)
plt.plot(pollution_data,ran_noise)
plt.plot(pollution_data,smooth)

plt.xlabel('data')
plt.ylabel('POLLUTION_COUNT')

plt.show()

import os
import sys
import librosa as lr
import matplotlib.pyplot as plt

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except:
    pass

audioData, samplingRate = lr.load("../Dataset/Actor_01/03-01-01-01-01-01-01.wav")

n0 = 10
n1 = 50
lr.display.waveshow(audioData[n0:n1], sr = samplingRate)
plt.grid()
plt.title("Example Waveform")
plt.savefig("../Images/Zero_Crossing.png")

plt.close()

n0 = 30000
n1 = 50000
lr.display.waveshow(audioData[n0:n1], sr = samplingRate)
plt.grid()
plt.title("Example Waveform")
plt.savefig("../Images/Spectral_Contrast.png")
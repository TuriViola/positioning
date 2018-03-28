from scipy import signal
from get_acoudata import get_acoudata
import matplotlib.pyplot as plt
import numpy as np
import argparse
parser = argparse.ArgumentParser(description='spectrogram_plot')
parser.add_argument('--filename', dest='filename', type=str, nargs='+', required=True, help='filename (e.g.  raw_data_filename1  raw_data_filename2 ...) ')
parser.add_argument('--nfft', dest='nfft', type=int, nargs=1, required=False, help='Length of the FFT used, if a zero padded FFT is desired. If None, the FFT length is nperseg.')
parser.add_argument('--nperseg', dest='nperseg', type=int, nargs=1, required=False, help='Length of each segment.')
parser.add_argument('--noverlap', dest='noverlap', type=int, nargs=1, required=False, help='Number of points to overlap between segments.') 
args = parser.parse_args()
data_spect=[]


filename = args.filename
nfft=args.nfft[0]
noverlap=args.noverlap[0]
nperseg=args.nperseg[0]



for i in range (0, len(filename)):
       	time,data=get_acoudata(filename[i])
	data_spect.extend(data)
fs = 195312.4

f, t, Sxx = signal.spectrogram(np.asarray(data_spect),nfft=nfft, nperseg=nperseg, noverlap=noverlap, fs=fs)
plt.pcolormesh(t, f, 10*np.log10(Sxx))
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

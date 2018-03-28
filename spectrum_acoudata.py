from scipy import signal
from get_acoudata import get_acoudata
import matplotlib.pyplot as plt
import numpy as np
import argparse
parser = argparse.ArgumentParser(description='spectrum_plot')
parser.add_argument('--filename', dest='filename', type=str, nargs='+', required=True, help='filename (e.g.  raw_data_filename1  raw_data_filename2 ...)')
parser.add_argument('--nfft', dest='nfft', type=int, nargs=1, required=False, help='Length of the FFT used, if a zero padded FFT is desired. If None, the FFT length is nperseg.')
parser.add_argument('--nperseg', dest='nperseg', type=int, nargs=1, required=False, help='Length of each segment.')
parser.add_argument('--noverlap', dest='noverlap', type=int, nargs=1, required=False, help='Number of points to overlap between segments.') 
args = parser.parse_args()
filename = args.filename
nfft=args.nfft[0]
noverlap=args.noverlap[0]
data_spect=[]
nperseg=args.nperseg[0]

title_font = {'fontname':'Bitstream Vera Sans', 'size':'14', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'Bitstream Vera Sans', 'size':'24'}
plot_font =  {'fontname':'Bitstream Vera Sans', 'size':'16'}

for i in range (0, len(filename)):
       	time,data=get_acoudata(filename[i])
	data_spect.extend(data)
fs = 195312.4
f,Pxx = signal.welch(np.asarray(data_spect),nfft=nfft, nperseg=nperseg, noverlap=noverlap, fs=fs)
f, t, Sxx = signal.spectrogram(np.asarray(data_spect),nfft=nfft, nperseg=nperseg, noverlap=noverlap, fs=fs)

plt.plot(f, 10*np.log10(Pxx), 'b', label='mean')
plt.plot(f, 10*np.log10(np.percentile(Sxx,10,axis=1)), 'r', label='10th percentile')
plt.plot(f, 10*np.log10(np.percentile(Sxx,50,axis=1)), 'k',label='50th percentile')
plt.plot(f, 10*np.log10(np.percentile(Sxx,90,axis=1)), 'g',label='90th percentile')

plt.xlabel('Frequency [s]',**axis_font)
plt.ylabel('PSD',**axis_font)
plt.rc('xtick', labelsize=16) 
plt.rc('ytick', labelsize=16)
plt.grid()
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()

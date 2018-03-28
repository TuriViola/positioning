from get_acoudata import get_acoudata
import matplotlib.pyplot as plt
import numpy as np
import argparse
parser = argparse.ArgumentParser(description='waveform_plot')
parser.add_argument('--filename', dest='filename', type=str, nargs='+', required=True, help='filename (e.g.  raw_data_filename1  raw_data_filename2 ...)')
args = parser.parse_args()
filename = args.filename
title_font = {'fontname':'Bitstream Vera Sans', 'size':'14', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'Bitstream Vera Sans', 'size':'24'}
plot_font =  {'fontname':'Bitstream Vera Sans', 'size':'16'}
data_plot=[]
for i in range (0, len(filename)):
       	time,data=get_acoudata(filename[i])
	data_plot.extend(data)
fs = 195312.4
plt.plot(np.arange(0,len(data_plot),1)/fs, data_plot, 'b')
plt.xlabel('Time [s]',**axis_font)
plt.ylabel('Amplitude',**axis_font)
plt.rc('xtick', labelsize=16) 
plt.rc('ytick', labelsize=16)
plt.grid()
plt.show()

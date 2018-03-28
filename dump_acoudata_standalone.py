import argparse
import numpy as np
import os
from os import listdir
def get_acoudata(filename):
	
	seconds=[]
	samples=[]
	ticks=[]
	data0=[]
	time=[]
	fid=open(filename)
	for i in range (0,int(os.path.getsize(filename)/(12+123260*4)+1)):
		seconds=np.fromfile(fid, np.uint32, count=1)
		ticks= np.fromfile(fid, np.uint32, count=1)
		samples=np.fromfile(fid, np.uint32, count=1) 
		data0.extend((np.fromfile(fid, np.float32, count=123260)))
		time.extend(list(seconds+ticks*16*10**(-9)))
	fid.close()
	return time,data0  
parser = argparse.ArgumentParser(description='dump_acoudata')
parser.add_argument('--filename', dest='filename', type=str, nargs='+', required=True, help='filename (e.g.  raw_data_filename1  raw_data_filename2 ...)')
args = parser.parse_args()
filename = args.filename
for i in range (0, len(filename)):
       	time,data=get_acoudata(filename[i])
print(time,data)




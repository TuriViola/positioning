import numpy as np
import os
from os import listdir
import matplotlib.pyplot as plt

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
   

		  
		

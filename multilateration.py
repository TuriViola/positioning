import os
import sys
import io
from collections import defaultdict
import numpy as np
from get_toas import get_toas
import argparse
import math
import scipy
import scipy.optimize

def multilateration(detid, du, floor, run):
	beacon=[0,1,2,3,4,5,6,7,8]
	toa={}
	for b in beacon:
		try:
			toa[b]=np.array(get_toas(detid, du, floor, run, run, b, threshold=0))
			toe[b]=np.array(get_toes(run,run,b))
			beacon_pos[b]=np.array(get_beaconpos(run,run,b))
		except:
			pass
			
	
	tof = {}
	for b in toa:
		tof[b] = []
		for t in range (1,int((maxtime-mintime)/rr)): 
			tmp=list(filter(lambda toe: (toe[b]-t)<rr & (toe[b]-t)>0), number_list))
			if len(tmp) != 0:
				toe_f[b][t] = tmp
				tof[b][t]=(min(toa[b]-toe_f[b][t]))

	position = []
	for t in range (1,int((maxtime-mintime)/rr)		
		f = lambda x: [sqrt((beacon_pos[b][0]-x[0])**2+(beacon_pos[b][1])-x[1])**2+(beacon_pos[b][2]-x[2])**2)-tof[1][t]*c for b in toa]

		[pos_x, pos_y, pos_z] = scipy.optimize.fsolve(f, [0, 0, 0])

		time_pos=mintime+(t-1)*rr
		n_emitter=len(tof)	
		position.append([[pos_x, pos_y, pos_z, time_pos,time_pos,n_emitter]])
				 
	return position

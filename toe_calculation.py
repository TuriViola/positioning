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
import km3pipe as kp

def toe_calculation(detid,emitterid,run,rr):
	pos_hydro={1:[4743507.3,257115.8,-2437]}
	beacon_pos=[4743789.8,257049.3,-2433]
	toas_base={}
	toe={}
	table_selected={}
	toe_f=[]
	tmp={}
	toe_temp={}
	c=1540
	db = kp.db.DBManager()
        table=db.run_table(detid)
        ind,=np.where((table["RUN"]==run))
        mintime= table['UNIXJOBSTART'][ind] 
        maxtime= table['UNIXJOBEND'][ind] 
        sds = kp.db.StreamDS()
	duid = [db.doms.via_dom_id(x).du for x in db.doms.ids("D_ORCA002")]
	du=set(duid)
	du_involved=set()
	try:
		for i in du:
			macaddress = db.doms.via_omkey((i+1,0), detid).dom_id
			toas_base[i] = get_toas(detid=detid,du=i+1, floor=0, minrun=run, maxrun=run, emitterid=emitterid,threshold=100000)
			toe[i]=(toas_base[i]-math.sqrt((beacon_pos[0]-pos_hydro[i][0])**2+(beacon_pos[1]-pos_hydro[i][1])**2+(beacon_pos[2]-pos_hydro[i][2])**2)/c)
		for t in np.arange(mintime/1000, maxtime/1000,rr):
			for i in du:
				tmp=filter(lambda x: ((x-t)<rr and (x-t)>0),toe[i])	
				if len(tmp)>0:
					toe_temp[i]=tmp[0]
			if  len(toe_temp)>0:
				du_involved.add(i)	
				n_du=len(toe_temp)		
				toe_mean=map(lambda x: scipy.mean(toe_temp[x]), toe_temp)
				toe_std= map(lambda x: scipy.std(toe_temp[x]), toe_temp)		
				if (toe_f==[]):
					toe_f.append({"toe": toe_mean[0], "n_du": n_du, "dus": list(du_involved),"toe_std":toe_std[0]})
				if (toe_f[-1]["toe"]!=toe_mean[0]):
			 		toe_f.append({"toe": toe_mean[0], "n_du": n_du, "dus": list(du_involved),"toe_std":toe_std[0]})
	
	except Exception:
		pass
	
			
	return toe_f

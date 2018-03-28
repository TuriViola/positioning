import km3pipe as kp
import numpy as np
import argparse
from threshold_calculation import threshold_calculation

parser = argparse.ArgumentParser(description='Quality factor thrshold calculation for all detector acoustic sensors')
parser.add_argument('--detid', dest='det_id', type=str, nargs=1, required=True,
                    help='The detector ID (e.g. D_ARCA003)')
parser.add_argument('--emitterid', dest='emitterid', type=int, nargs='+', required=True,
                    help='Beacon ID (e.g. 0 ...7)')
parser.add_argument('--run', dest='run', type=int, nargs=1, required=True,
                    help='First run')



args = parser.parse_args()
detid = args.det_id[0]
emitterid=args.emitterid
run=args.run[0]



db = kp.db.DBManager()
th=[]

for b in emitterid:
	
	duid = [db.doms.via_dom_id(x).du for x in db.doms.ids(detid)]
	du=set(duid)
	for i in du:
		for k in range(0,19):
			try:
				threshold= threshold_calculation(detid, i+1, k, run, run,b)
				th.append({"detid": detid, "du": i+1, "floor": k, "beaconid":b, "QF_thershold":threshold, "run":run})
			
			except Exception:
				pass
			
print(th)

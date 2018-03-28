import km3pipe as kp
import numpy as np
db = kp.db.DBManager()
beacon_period=2.0
def threshold_calculation(detid, du, floor, minrun, maxrun,emitterid):
	
	sds = kp.db.StreamDS()

	macaddress = db.doms.via_omkey((du,floor), detid).dom_id
	
		
	toas_all = sds.toashort(detid=detid, minrun=minrun, maxrun=maxrun, domid=macaddress, emitterid=emitterid)
	threshold=np.percentile(toas_all["QUALITYFACTOR"], (1-0.670/beacon_period)*100)
	return threshold

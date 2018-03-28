import km3pipe as kp
import numpy as np

def get_toas(detid, du, floor, minrun, maxrun, emitterid, threshold=0):
	db = kp.db.DBManager()

	sds = kp.db.StreamDS()

	macaddress = db.doms.via_omkey((du,floor), detid).dom_id

	toas_all = sds.toashort(detid=detid, minrun=minrun, maxrun=maxrun, domid=macaddress, emitterid=emitterid)
	ind,=np.where((toas_all["QUALITYFACTOR"]>=threshold))
	selected = toas_all.loc[ind, :]
	toas = selected["UNIXTIMEBASE"] + selected["TOA_S"]
	return toas

       
		

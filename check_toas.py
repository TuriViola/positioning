import os
import sys
import io
from collections import defaultdict
import numpy as np

from get_toas import get_toas
import matplotlib.pyplot as plt

import argparse

parser = argparse.ArgumentParser(description='TToA analyzer')
parser.add_argument('--detid', dest='det_id', type=str, nargs=1, required=True,
                    help='The detector ID (e.g. D_ARCA003)')
parser.add_argument('--duid', dest='du_id', type=int, nargs=1, required=True,
                    help='Detector Unit ID (e.g. 1 ... 115)')
parser.add_argument('--floor', dest='floor_number', type=int, nargs=1, required=True,
                    help='Floor number (e.g. Base=0, Floor=1...18)')
parser.add_argument('--emitterid', dest='emitterid', type=int, nargs=1, required=True,
                    help='Beacon ID (e.g. 0 ...7)')
parser.add_argument('--minrun', dest='minrun', type=int, nargs=1, required=True,
                    help='First run')
parser.add_argument('--maxrun', dest='maxrun', type=int, nargs=1, required=True,
                    help='Last run')
parser.add_argument('--dump-toas', dest='dump_toas', type=str, nargs=1,
                    help='This option writes ToAs list to file')
parser.add_argument('--dump-toas-mod', dest='dump_toas_mod', type=str, nargs=1,
                    help='This option writes ToAs modulo beacon repetition rate to file')


args = parser.parse_args()

detid = args.det_id[0]
du = args.du_id[0]
floor = args.floor_number[0]
emitterid=args.emitterid[0]
minrun=args.minrun[0]
maxrun=args.maxrun[0]

title_font = {'fontname':'Bitstream Vera Sans', 'size':'14', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'Bitstream Vera Sans', 'size':'10'}
plot_font =  {'fontname':'Bitstream Vera Sans', 'size':'6'}
beacon_rr=11.8010006
th=np.loadtxt('threshold_toa_orcadu2_beacon0.txt', skiprows=0, dtype=float)
threshold=th[floor]

toas = get_toas(detid, du, floor, minrun, maxrun, emitterid, threshold)

if len(toas) != 0:
	toasmod = np.mod(toas, beacon_rr)

	plt.plot(toas - min(toas), toasmod, 'b.')
	plt.xlabel('Time [s]',**axis_font)
	plt.ylabel('ToA modulo Repetion Rate [s]',**axis_font)
	plt.title('DU%d-Floor%d' % (du, floor),**title_font) 
	plt.rc('xtick', labelsize=6) 
	plt.rc('ytick', labelsize=6)
	plt.axis([0, max(toas)-min(toas), 0.0, beacon_rr])
	plt.grid()
	plt.subplots_adjust( hspace=0.5 )
	plt.show()
try:
	with open(args.dump_toas[0], 'w') as f:
		for t in toas:
			f.write("%lf\n" % t)
except IOError as err:
	print err

try:
	with open(args.dump_toas_mod[0], 'w') as f:
		for t in toasmod:
			f.write("%lf\n" % t)
except IOError as err:
	print err


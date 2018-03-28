from get_acoudata import get_acoudata
import argparse
parser = argparse.ArgumentParser(description='dump_acoudata')
parser.add_argument('--filename', dest='filename', type=str, nargs='+', required=True, help='filename (e.g.  raw_data_filename1  raw_data_filename2 ...)')
args = parser.parse_args()
filename = args.filename
for i in range (0, len(filename)):
       	time,data=get_acoudata(filename[i])
print(time,data)


import pandas as pd
import argparse
from os import listdir
from os.path import isfile, join
import glob
import os

#need to install xlrd==1.2.0
def main():
	parser = argparse.ArgumentParser(description='Upload files to splunk')
	parser.add_argument('source_path', type=str, help='The path of the directory to upload')
	args = parser.parse_args()

	files = glob.glob('temp/*')
	for f in files:
	    os.remove(f)

	onlyfiles = [(f, join(args.source_path, f)) for f in listdir(args.source_path) if isfile(join(args.source_path, f))]
	for file in onlyfiles:
		print("file is: " + file[0])
		print("full path is: " + file[1])
		read_file = pd.read_excel(file[1])
		read_file.to_csv("../data/fwd/vol_out/" + file[0] + ".csv", index = None, header=True)

		#send_to_splunk()
		
main()
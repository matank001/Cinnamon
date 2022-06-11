import pandas as pd
import argparse
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
from os import listdir
from os.path import isfile, join
import glob
import os

#need to install xlrd==1.2.0
def main():
	parser = argparse.ArgumentParser(description='Upload files to splunk')
	parser.add_argument('source_path', type=str, help='The path of the directory to upload')
	parser.add_argument('remote_addr', type=str, help='address of the splunk vm')
	parser.add_argument('root_username', type=str, default='root', help='username of the splunk vm')
	parser.add_argument('root_password', type=str, help='password of the splunk vm')
	args = parser.parse_args()

	ssh = SSHClient()
	ssh.set_missing_host_key_policy(AutoAddPolicy())
	ssh.connect(args.remote_addr, username=args.root_username , password=args.root_password)

	scp = SCPClient(ssh.get_transport())

	files = glob.glob('/vol/temp/*')
	for f in files:
		os.remove(f)

	onlyfiles = [(f, join(args.source_path, f)) for f in listdir(args.source_path) if isfile(join(args.source_path, f))]
	for file in onlyfiles:
		print("file is: " + file[0])
		print("full path is: " + file[1])
		read_file = pd.read_excel(file[1])
		new_path = "/vol/temp/" + file[0] + ".csv"
		read_file.to_csv(new_path, index = None, header=True)
		scp.put(new_path, recursive=True, remote_path='/home/user/Documents/Cinnamon/splunk/data/fwd/vol_out')
		
main()

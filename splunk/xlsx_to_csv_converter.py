import pandas as pd
import argparse

#need to install xlrd==1.2.0

parser = argparse.ArgumentParser(description='convert xlsx file to csv file')
parser.add_argument('source_path', type=str, help='the path of the source xlsx file')
parser.add_argument('destination_path',type=str, help='the path of the dest csv file')
args = parser.parse_args()

read_file = pd.read_excel (args.source_path)
read_file.to_csv (args.destination_path, index = None, header=True)
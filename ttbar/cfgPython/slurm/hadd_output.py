import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')


args = parser.parse_args()
directory = args.directory

heppy_output = 'heppy_output/'


listdir = os.listdir(directory)

for l in listdir:
    cmd = 'heppy_hadd.py '+directory+l
    os.system(cmd)

for l in listdir:
    cmd = 'mv '+directory+l+'/'+l+' '+heppy_output
    os.system(cmd)
    


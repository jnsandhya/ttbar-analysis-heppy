import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')


args = parser.parse_args()
directory = args.directory


listdir = os.listdir(directory)

for l in listdir:
    cmd = 'heppy_hadd.py '+directory+l
    os.system(cmd)

print 'Done'

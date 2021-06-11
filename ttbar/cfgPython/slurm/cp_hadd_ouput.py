import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')
parser.add_argument('output', help='display your output directory')


args = parser.parse_args()
directory = args.directory
output    = args.output

os.system('mkdir '+output)


if directory[-1] != '/':
    directory += '/'
if output[-1] != '/':
    output += '/'


listdir = os.listdir(directory)

for l in listdir:   
    print l
    if len(os.listdir(directory+l+'/'+l+'/NtupleProducer')) != 0:
        cmd = 'cp -r '+directory+l+'/'+l+'/ '+output
        os.system(cmd)

print 'Done'


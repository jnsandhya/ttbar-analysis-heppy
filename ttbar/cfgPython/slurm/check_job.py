#scontrol show job $1 

import os
import subprocess

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')
#parser.add_argument('sample', help='display your sample')

args = parser.parse_args()
directory = args.directory
#sample = args.sample

jobs = os.listdir(directory)

'''
for i in range(100):

    direc = directory+'/MC_'+sample+'_Chunk'+str(i)
    cmd = 'tail '+direc+'/slurm*.out -n 1'
    output = subprocess.check_output(cmd, shell=True)
    print direc+' -> '+output


'''
for j in jobs:
    if j.find('Chunk') == -1 :
        continue
    cmd = 'tail '+directory+'/'+j+'/slurm*.out -n 1'
    output = subprocess.check_output(cmd, shell=True)
    print j+' -> '+output

#tail slurm-91578.out -n 1


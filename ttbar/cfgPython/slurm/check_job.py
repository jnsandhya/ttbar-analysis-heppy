#scontrol show job $1 

import os
import subprocess

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')
#parser.add_argument('sample', help='display your sample')
parser.add_argument('log', help='log')

args = parser.parse_args()
directory = args.directory
#sample = args.sample
log = args.log

jobs = os.listdir(directory)

'''
for i in range(100):

    direc = directory+'/MC_'+sample+'_Chunk'+str(i)
    cmd = 'tail '+direc+'/slurm*.out -n 1'
    output = subprocess.check_output(cmd, shell=True)
    print direc+' -> '+output


'''

n_fai = 0
n_suc = 0 
n_tot = 0
failed_submission = []


for j in jobs:
    if j.find('Chunk') == -1 :
        continue

    n_tot += 1
    if log == 'log':
        cmd = 'tail '+directory+'/'+j+'/log.txt -n 10'
    else:
        cmd = 'tail '+directory+'/'+j+'/local.output -n 10'
    try:
        output = subprocess.check_output(cmd, shell=True)
    except:
        print ' ### Failed submission '+j+' ###'
        continue
        #failed_submission.append(directory+'/'+j)

    if output == '':
        #print j+' ### Empty log'
        n_fai += 1
        failed_submission.append(directory+'/'+j)
    else:
        print j+' -> '+output
        n_suc += 1


print ''
print 'failed job :'+str(n_fai)+'/'+str(n_tot)
print 'succed job :'+str(n_suc)+'/'+str(n_tot)
print ''


print ' ------------ '
start_harvest = None
while start_harvest not in ['y','n']:
    start_harvest = raw_input('Resubmit jobs ? [y/n]')
if start_harvest == 'y':
    print 'Resubmit !.'
    for sub in failed_submission:
        #print ' -> '+sub
        cmd = 'cd '+sub+' && sbatch ./batchScript.sh'
        os.system(cmd)
else:
    quit()


#tail slurm-91578.out -n 1


#scontrol show job $1 

import os
import subprocess
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')
#parser.add_argument('sample', help='display your sample')


######################################################
## init
######################################################

args = parser.parse_args()
directory = args.directory
#sample = args.sample

if directory[-1] != '/':
    directory += '/'


jobs = os.listdir(directory)

n_fai = 0
n_suc = 0 
n_run = 0
n_tot = 0
failed_submission = []


######################################################
## Functions
######################################################


def get_slurm_file(target):
    slurm = []
    for l in os.listdir(target):
        if l.find('slurm-') != -1:
            slurm.append(l)
    slurm.sort()
    return slurm[-1]

def print_job(name, n, n_tot):
    print name+' job : '+str(math.floor(float(n)/n_tot*100))+'% --> '+str(n)+'/'+str(n_tot) 

######################################################
## Test jobs
######################################################

for j in jobs:
    if j.find('Chunk') == -1 :
        continue

    n_tot += 1
    target_dir = directory+'/'+j
    slurm_file = get_slurm_file(target_dir)

    cmd1 = 'tail -n 10 '+target_dir+'/log.txt'
    cmd2 = 'tail -n 1  '+target_dir+'/'+slurm_file

    try:
        output1 = subprocess.check_output(cmd1, shell=True)
        output2 = subprocess.check_output(cmd2, shell=True)
    except:
        print ' ### Failed submission '+j+' ###'
        continue

    if output2.find('sending the job directory back') != -1 :
        if output1 == '':
            print j+' ### Failed job'
            n_fai += 1
            failed_submission.append(target_dir)
        else:
            print j+' -> '+output1
            n_suc += 1
    else:
        n_run += 1

print '\n ******************************************* '
print_job(' failed', n_fai, n_tot)
print_job(' succed', n_suc, n_tot)
print_job('running', n_run, n_tot)
print '******************************************* \n'


######################################################
## Resubmit
######################################################


print ' ------------ \n'
start_harvest = None
while start_harvest not in ['y','n']:
    start_harvest = raw_input('Resubmit jobs ? [y/n]')
if start_harvest == 'y':
    print 'Resubmit !.'
    for sub in failed_submission:
        #print ' -> '+sub
        cmd = 'cd '+sub+' && rm -rf */ && rm slurm-* && sbatch ./batchScript.sh'
        os.system(cmd)
else:
    quit()


#tail slurm-91578.out -n 1


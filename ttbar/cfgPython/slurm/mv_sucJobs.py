#scontrol show job $1 

import os
import subprocess
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')
parser.add_argument('target', help='mv successful jobs back to the main directory')


######################################################
## init
######################################################

args = parser.parse_args()
directory = args.directory
target = args.target

if directory[-1] != '/':
    directory += '/'


jobs = os.listdir(directory)

n_fai = 0
n_suc = 0 
n_run = 0
n_not = 0
n_notlog = 0
n_tot = 0
failed_submission = []
failed_jobs = []
failed_log = []
failed_ids ={}
failed_subids ={}
succ_ids ={}

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
    slurm_file = ''
    
    try:
        slurm_file = get_slurm_file(target_dir)

    except :
        failed_submission.append(target_dir)
        failed_subids[target_dir] = slurm_file
        n_not += 1
        #print j, slurm_file+' ### Failed Submission, no slurm file'
        #print ' ### Failed submission '+j+' ###'
        continue


    cmd1 = 'tail -n 10 '+target_dir+'/log.txt'
    cmd2 = 'tail -n 1  '+target_dir+'/'+slurm_file

    try:
        output1 = subprocess.check_output(cmd1, shell=True)
        output2 = subprocess.check_output(cmd2, shell=True)

        if output2.find('sending the job directory back') != -1 :
            if output1 == '':
                #print j, slurm_file+' ### Failed job'
                n_fai += 1
                failed_jobs.append(target_dir)
                failed_ids[target_dir] = slurm_file

            else:
                #print j+' -> '+output1
                succ_ids[target_dir] = slurm_file
                n_suc += 1
        elif output2.find('running')!= -1 :
            #print j, slurm_file+' ### Running job'
            n_run += 1
        else:
            #print j+' ### Failed job back'
            #print j, slurm_file+' ### Failed job'
            n_fai += 1
            failed_jobs.append(target_dir)
            failed_ids[target_dir] = slurm_file
            
    except :
        failed_log.append(target_dir)
        output2 = subprocess.check_output(cmd2, shell=True)
        if output2.find('running')!= -1 :
            #print j, slurm_file+' ###Running, no log file'
            n_run+=1
        else:
            n_fai += 1
            failed_jobs.append(target_dir)
            failed_ids[target_dir] = slurm_file

        n_notlog += 1
        continue

os.system('mkdir -p '+target)
print 'Printing '+str(len(succ_ids))+' succesful jobs !.'
for keys,values in succ_ids.items():
    print ' -> '+keys+'/'+values
    cmd = 'mv '+keys+' '+target
    os.system(cmd)



print '\n ******************************************* '
print_job(' failed', n_fai, n_tot)
print_job(' succed', n_suc, n_tot)
print_job('running', n_run, n_tot)
print_job('not sub', n_not, n_tot)
#print_job('not log', n_notlog, n_tot)
print '******************************************* \n'


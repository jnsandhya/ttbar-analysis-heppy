#scontrol show job $1 

import os
import subprocess
import math
import argparse


def IntersecOfSets(arr1, arr2, arr3):
    # Converting the arrays into sets
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)
      
    # Calculates intersection of 
    # sets on s1 and s2
    set1 = s1.intersection(s2)         #[80, 20, 100]
      
    # Calculates intersection of sets
    # on set1 and s3
    result_set = set1.intersection(s3)
      
    # Converts resulting set to list
    final_list = list(result_set)
    #print final_list
    return final_list

parser = argparse.ArgumentParser()
parser.add_argument('directory1', help='display your Nominal directory')
parser.add_argument('directory2', help='display your JEC_up directory')
parser.add_argument('directory3', help='display your JEC_down directory')
#parser.add_argument('sample', help='display your sample')


######################################################
## init
######################################################
if __name__ == '__main__' :
    args = parser.parse_args()
    directory1 = args.directory1
    directory2 = args.directory2
    directory3 = args.directory3
    #sample = args.sample
    
    if directory1[-1] != '/':
        directory1 += '/'
        
    if directory2[-1] != '/':
        directory2 += '/'

    if directory3[-1] != '/':
        directory3 += '/'
                

    jobs1 = os.listdir(directory1)
    jobs2 = os.listdir(directory2)
    jobs3 = os.listdir(directory3)

    common_dir = IntersecOfSets(jobs1,jobs2,jobs3)
    print common_dir 

    print ' ------------ \n'
    start_harvest = None
    while start_harvest not in ['y','n']:
        start_harvest = raw_input(' -> Do you want to move common jobs in new directories ? [y/n]')
        if start_harvest == 'y':
            new_dir = raw_input('  name of new directory :')
            print 'Move !.'
            new_dir1 = new_dir+'_Nominal'
            new_dir2 = new_dir+'_Total_up'
            new_dir3 = new_dir+'_Total_down'
            os.system('mkdir -p '+new_dir1)
            os.system('mkdir -p '+new_dir2)
            os.system('mkdir -p '+new_dir3)
            #time.sleep(2)
            for l in common_dir:
                #if l.find('Chunk') == -1:
                cmd = 'cp -r '+directory1+l+'/ '+new_dir1
                os.system(cmd)
                cmd = 'cp -r '+directory2+l+'/ '+new_dir2
                os.system(cmd)
                cmd = 'cp -r '+directory3+l+'/ '+new_dir3
                os.system(cmd)
        else:
            quit()
    #print intersection

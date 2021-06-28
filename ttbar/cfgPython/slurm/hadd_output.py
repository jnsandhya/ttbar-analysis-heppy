import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')

######################################################
## init
######################################################

args = parser.parse_args()
directory = args.directory


if directory[-1] != '/':
    directory += '/'


listdir = os.listdir(directory)

print listdir
start_hadd = None
while start_hadd not in ['y','n', 'pass']:
    start_hadd = raw_input(' -> Confirm it\'s good directory directory (or pass to move)? [y/n/pass]')
if start_hadd == 'n':
    quit()
elif start_hadd == 'pass':
    pass
else:
    cmd = 'heppy_hadd.py '+directory
    os.system(cmd)

print 'Done'

print ' ------------ \n'
start_harvest = None
while start_harvest not in ['y','n']:
    start_harvest = raw_input(' -> Do you want to move hadd in new directory ? [y/n]')
if start_harvest == 'y':
    new_dir = raw_input('  name of new directory :')
    print 'Move !.'
    os.system('mkdir '+new_dir)
    
    for l in listdir:
        if l.find('Chunk') == -1:
            cmd = 'cp -r '+directory+l+'/ '+new_dir
            os.system(cmd)
else:
    quit()

import os
import argparse
import shutil


parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')

args = parser.parse_args()
directory = args.directory

listdir = os.listdir(directory)

removed_dir = []
for l in listdir:
    if l.find('MC_') == -1:
        removed_dir.append(l)
for l in removed_dir:
    listdir.remove(l)


if directory[-1] != '/':
    directory += '/'

to_remove = []

for l in listdir:

    if l[-1] != '/':
        l += '/'    
    direct = directory+l

    try:
    
        listing1 = os.listdir(direct+'/MCWeighter/')        
        listing2 = os.listdir(direct+'/NtupleProducer/')        
        if len(listing1) == 0 or  len(listing2) == 0:
            to_remove.append(direct)    

    except:

        to_remove.append(direct)    



print to_remove



print ' ------------ \n'
start_harvest = None
while start_harvest not in ['y','n']:
    start_harvest = raw_input('Remove failed jobs ? [y/n]')
if start_harvest == 'y':

    for l in to_remove:
        shutil.rmtree(l)
else:
    quit()


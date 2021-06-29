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


for l in listdir:

    if l[-1] != '/':
        l += '/'    
    direct = directory+l
    
    listing = os.listdir(direct+'/MCWeighter/')        
    
    if len(listing) == 0:
        print listing
        shutil.rmtree(direct)

    #print direct
    #cmd = '\n\
    #directories=$(ls '+direct+' | grep _Chunk | sort)\n\
    #for directory in ${directories}\n\
    #do\n\
    #    #echo "${directory}"\n\
    #    if find '+direct+'${directory}/MCWeighter/ -mindepth 1 -maxdepth 1 | read; then\n\
    #        echo "Not Empty"\n\
    #    else\n\
    #        rm -rf '+direct+'${directory} \n\
    #        echo "Empty" \n\
    #    fi\n\
    #done'

    #print cmd
    #os.system(cmd)


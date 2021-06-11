import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')
parser.add_argument('output', help='display your output directory')


args = parser.parse_args()
directory = args.directory
output    = args.output

cmd = '\n\
directories=$(ls '+directory+' | grep _Chunk | sort)\n\
output_dir='+output+'\n\
for directory in ${directories}\n\
do\n\
    echo "${directory}"\n\
    sample=${directory%_Chunk*}\n\
    mkdir -p ${output_dir}/${sample} && mv '+directory+'/${directory} ${output_dir}/${sample}/${directory} || "FAILURE"\n\
done\n\
'

#print cmd
os.system(cmd)
os.system("rm -rf "+directory)

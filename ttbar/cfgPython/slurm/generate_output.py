import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='display your directory')


args = parser.parse_args()
directory = args.directory

slurm_output = 'slurm_output/' 

mc_ttbar = [
    'MC_dibosons_WW',             
    'MC_singletop_ST_t_top',        
    'MC_ttx_TTZ2',
    'MC_dibosons_WZ',             
    'MC_singletop_ST_tW_antitop',   
    'MC_ttx_TTZ3',
    'MC_dibosons_ZZ',             
    'MC_singletop_ST_tW_antitop2',  
    'MC_wjets_WJets',
    'MC_signal_dilep',            
    'MC_singletop_ST_tW_top',       
    'MC_wjets_WJets2', 
    'MC_signal_hadronic',         
    'MC_singletop_ST_tW_top2',       
    'MC_zjets_DY_1050',
    'MC_signal_semilep',          
    'MC_ttx_TTW',                   
    'MC_zjets_DY_50',
    'MC_singletop_ST_s',          
    'MC_ttx_TTW2',                  
    'MC_zjets_DY_502',
    'MC_singletop_ST_s2',         
    'MC_ttx_TTW3',
    'MC_singletop_ST_t_antitop',  
    'MC_ttx_TTZ'
]

for l in mc_ttbar:
    os.system('mkdir -p '+slurm_output+l)



jobs = os.listdir(directory)

for j in jobs:
    for l in mc_ttbar:
        if j.find(l+'_') != -1 :
            cmd ='cp -r '+directory+j+' '+slurm_output+l+'/'
            os.system(cmd)
            #print cmd
    print j

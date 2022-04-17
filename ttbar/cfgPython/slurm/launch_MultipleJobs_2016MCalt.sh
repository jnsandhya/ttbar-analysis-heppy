#!/bin/sh

mkdir $CMSSW_BASE/src/CMGTools/ttbar/cfgPython/emu/$1
#rm -rf $1_Nominal
#sed -e 's/*TESTCORR//g' < ../emu/emu_test_cfg.py > ../emu/$1/emu_nominal_cfg.py 
cp ../emu/emu_prod_2016MCalt_cfg.py ../emu/$1/emu_nominal_cfg.py 
bash launch.sh ../emu/$1/emu_nominal_cfg.py $1_Nominal

# Absolute Absolute_2016 BBEC1 BBEC1_2016 FlavorQCD RelativeBal RelativeSample_2016 Total

#for corr in Total
#do
#    rm -rf ../emu/$1/emu_${corr}_up_cfg.py $1_${corr}_up 
#    sed -e 's/TESTCORR/x.corr_'"${corr}"'_JEC_up/g' < ../emu/emu_test_cfg.py > ../emu/$1/emu_${corr}_up_cfg.py
#    bash launch.sh ../emu/$1/emu_${corr}_up_cfg.py $1_${corr}_up
#    rm -rf ../emu/$1/emu_${corr}_down_cfg.py $1_${corr}_down
#    sed -e 's/TESTCORR/x.corr_'"${corr}"'_JEC_down/g' < ../emu/emu_test_cfg.py > ../emu/$1/emu_${corr}_down_cfg.py
#    bash launch.sh ../emu/$1/emu_${corr}_down_cfg.py $1_${corr}_down
#done
#heppy_batch.py $1 -o $2 -b "sbatch ./batchScript.sh"

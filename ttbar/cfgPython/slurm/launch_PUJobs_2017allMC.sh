#!/bin/sh

#mkdir $CMSSW_BASE/src/CMGTools/ttbar/cfgPython/emu/pu_2017allMC_Lyon
#cp ../weight/pu_2017allMC_Lyon_cfg.py ../emu/pu_2017allMC_Lyon/pu_cfg.py 
bash launch.sh ../weight/pu_2017allMC_Lyon_cfg.py PU_2017allMC_Lyon
bash launch.sh ../weight/pu_2017allMC_AAA_cfg.py PU_2017allMC_AAA

#mkdir $CMSSW_BASE/src/CMGTools/ttbar/cfgPython/emu/pu_2017allMC_AAA
#cp ../weight/pu_2017allMC_AAA_cfg.py ../emu/pu_2017allMC_AAA/pu_cfg.py 
#bash launch.sh ../emu/pu_2017allMC_AAA/pu_cfg.py PU_2017allMC_AAA




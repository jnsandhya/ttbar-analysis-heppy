# ttbar time analysis  (CERN/Lyon)

## Installation recipe

If you work in Lyon, do the following to set up your global CMS environment:
```
source /cvmfs/cms.cern.ch/cmsset_default.sh
```

Then follow this recipe to install the analysis software: 

```
cmsrel CMSSW_10_4_0
cd CMSSW_10_4_0/src
cmsenv
git cms-init --upstream-only

# first make a fork from git@github.com:Arc-Pintade/cmg-cmssw.git to get cmg-cmssw.

# get HEPPY structure
git remote add lucas git@github.com:lucastorterotot/cmg-cmssw.git -f -t htt_10_4_0_v1

# configure the sparse checkout, and get the base heppy packages (cp need to be on lyouicms machine cause of the presence of afs directory)
cp /afs/cern.ch/user/g/gpetrucc/public/sparse-checkout_104X_heppy .git/info/sparse-checkout 
git checkout -t lucas/htt_10_4_0_v1

# get my CMGTools subsystem from the cmgtools-lite repository
git clone -o aure git@github.com:Arc-Pintade/cmgtools-lite.git -b ttbar_9_4_11_cand1_v1 CMGTools

# get the recoil correction interface
git clone https://github.com/CMS-HTT/RecoilCorrections.git  HTT-utilities/RecoilCorrections 

# compile : Warning you need to compile on CentOS6 (lyouicms machine)
scram b -j 20

# Last installation
cd CMGTools/ttbar
python scripts/install.py
```


## In practice

The idea of this code is, at the end, to create a ROOT flat tree containing all wanted observable of selected events.

In practice, hearts of the code are the config files in `CMGTools/TTbarTime/cfgPython/YOUR_CHANNEL/`
In these files, you can make selection on you events, get observable from AOD, MINIAOD, NanoAOD,... or create new ones.
Config file call all modules needed for your analysis (call Analyzers) present in `CMGTools/TTbarTime/python/heppy/` or `CMGTools/TTbarTime/python/proto/`.

## Start with heppy

The first thing to do is to run init.sh script to source everything needed and init voms

```
cd CMGTools/ttbar/
source ./init.sh 
```

## Running our analysis in heppy

Let's try the code with small interactive test: 

```
cd CMGTools/ttbar/cfgPython/emu/
heppy Test emu_cfg.py -o test=True -o year=2017 -N 1000 -f
```
This command will launch heppy in test mode (On a small part of MiniAOD), for 2017, and shut the run at 1000 events. 
All results including rootfiles will be store in the `Trash` directory.



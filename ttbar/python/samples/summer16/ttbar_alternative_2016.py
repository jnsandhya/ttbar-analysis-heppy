import os 
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

json = os.path.expandvars('$CMSSW_BASE/src/CMGTools/ttbar/data/2016/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt')
lumi = 35921.875594646

############################################################################
# MC
############################################################################


alt_MC_hdampUp = creator.makeMCComponent("alt_MC_hdampUp","/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);

alt_MC_hdampUp_pmx = creator.makeMCComponent("alt_MC_hdampUp_pmx","/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);



alt_MC_hdampDown_pmx = creator.makeMCComponent("alt_MC_hdampDown_pmx","/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);

alt_MC_hdampDown = creator.makeMCComponent("alt_MC_hdampDown","/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);



alt_MC_CP5Up_pmx = creator.makeMCComponent("alt_MC_CP5Up_pmx","/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_CP5Up = creator.makeMCComponent("alt_MC_CP5Up","/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_CP5Down_pmx = creator.makeMCComponent("alt_MC_CP5Down_pmx","/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_CP5Down = creator.makeMCComponent("alt_MC_CP5Down","/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);


##############


alt_MC_erdOn = creator.makeMCComponent("alt_MC_erdOn","/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);

alt_MC_erdOn_ext = creator.makeMCComponent("alt_MC_erdOn_ext","/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_QCDbased = creator.makeMCComponent("alt_MC_QCDbased","/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);



alt_MC_GluonMove = creator.makeMCComponent("alt_MC_GluonMove","/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_mtop169p5 = creator.makeMCComponent("alt_MC_mtop169p5","/TTTo2L2Nu_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MC_mtop175p5 = creator.makeMCComponent("alt_MC_mtop175p5","/TTTo2L2Nu_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);




alt_ttbar = [
    alt_MC_hdampUp,
    alt_MC_hdampUp_pmx,
    alt_MC_hdampDown_pmx,
    alt_MC_hdampDown,
    alt_MC_CP5Up_pmx,
    alt_MC_CP5Up,
    alt_MC_CP5Down_pmx,
    alt_MC_CP5Down,
    alt_MC_erdOn,
    alt_MC_erdOn_ext,
    alt_MC_QCDbased,
    alt_MC_GluonMove,
    alt_MC_mtop169p5,
    alt_MC_mtop175p5
]





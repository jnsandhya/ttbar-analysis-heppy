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

alt_MC_erdOn = creator.makeMCComponent("alt_MC_erdOn","/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_erdOn_ext = creator.makeMCComponent("alt_MC_erdOn_ext","/TTTo2L2Nu_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);

alt_MC_QCDbased = creator.makeMCComponent("alt_MC_QCDbased","/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);

alt_MC_GluonMove = creator.makeMCComponent("alt_MC_GluonMove","/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);

alt_MC_mtop169p5 = creator.makeMCComponent("alt_MC_mtop169p5","/TTTo2L2Nu_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);

alt_MC_mtop175p5 = creator.makeMCComponent("alt_MC_mtop175p5","/TTTo2L2Nu_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 89.05);


alt_MCsemilep_hdampDown = creator.makeMCComponent("alt_MCsemilep_hdampDown","/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_hdampUp = creator.makeMCComponent("alt_MCsemilep_hdampUp","/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 366.9);

alt_MCsemilep_CP5Down = creator.makeMCComponent("alt_MCsemilep_CP5Down","/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_CP5Up = creator.makeMCComponent("alt_MCsemilep_CP5Up","/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 366.9);

alt_MCsemilep_erdOn = creator.makeMCComponent("alt_MCsemilep_erdOn","/TTToSemiLeptonic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_QCDbased = creator.makeMCComponent("alt_MCsemilep_QCDbased","/TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_GluonMove = creator.makeMCComponent("alt_MCsemilep_GluonMove","/TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 366.9);

alt_MCsemilep_mtop169p5 = creator.makeMCComponent("alt_MCsemilep_mtop169p5","/TTToSemiLeptonic_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_mtop175p5 = creator.makeMCComponent("alt_MCsemilep_mtop175p5","/TTToSemiLeptonic_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 366.9);


alt_MChad_hdampDown = creator.makeMCComponent("alt_MChad_hdampDown","/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_hdampUp = creator.makeMCComponent("alt_MChad_hdampUp","/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 377.96);

alt_MChad_CP5Down = creator.makeMCComponent("alt_MChad_CP5Down","/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_CP5Up = creator.makeMCComponent("alt_MChad_CP5Up","/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 377.96);

alt_MChad_erdOn = creator.makeMCComponent("alt_MChad_erdOn","/TTToHadronic_TuneCP5_PSweights_erdON_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_QCDbased = creator.makeMCComponent("alt_MChad_QCDbased","/TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_GluonMove = creator.makeMCComponent("alt_MChad_GluonMove","/TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 377.96);

alt_MChad_mtop169p5 = creator.makeMCComponent("alt_MChad_mtop169p5","/TTToHadronic_TuneCP5_PSweights_mtop1695_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_mtop175p5 = creator.makeMCComponent("alt_MChad_mtop175p5","/TTToHadronic_TuneCP5_PSweights_mtop1755_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_backup_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM","CMS",".*root", 377.96);



alt_MC_hdampUp.splitFactor = 10
alt_MC_hdampUp_pmx.splitFactor = 5
alt_MC_hdampDown_pmx.splitFactor = 10
alt_MC_hdampDown.splitFactor = 5
alt_MC_CP5Up_pmx.splitFactor = 10
alt_MC_CP5Up.splitFactor = 5
alt_MC_CP5Down_pmx.splitFactor = 10
alt_MC_CP5Down.splitFactor = 5 
alt_MC_erdOn.splitFactor = 10
alt_MC_erdOn_ext.splitFactor = 5
alt_MC_QCDbased.splitFactor = 15
alt_MC_GluonMove.splitFactor = 15
alt_MC_mtop169p5.splitFactor = 15
alt_MC_mtop175p5.splitFactor = 12
alt_MCsemilep_hdampDown.splitFactor = 30
alt_MCsemilep_hdampUp.splitFactor = 30
alt_MCsemilep_CP5Down.splitFactor = 30
alt_MCsemilep_CP5Up.splitFactor = 30
alt_MCsemilep_erdOn.splitFactor = 29
alt_MCsemilep_QCDbased.splitFactor = 30
alt_MCsemilep_GluonMove.splitFactor = 27
alt_MCsemilep_mtop169p5.splitFactor = 27
alt_MCsemilep_mtop175p5.splitFactor = 22 
alt_MChad_hdampDown.splitFactor = 29
alt_MChad_hdampUp.splitFactor = 29
alt_MChad_CP5Down.splitFactor = 28
alt_MChad_CP5Up.splitFactor = 28
alt_MChad_erdOn.splitFactor = 28
alt_MChad_QCDbased.splitFactor = 28
alt_MChad_GluonMove.splitFactor = 29
alt_MChad_mtop169p5.splitFactor = 10
alt_MChad_mtop175p5.splitFactor = 10




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
    alt_MC_mtop175p5,
    alt_MCsemilep_hdampDown, 
    alt_MCsemilep_hdampUp,
    alt_MCsemilep_CP5Down,
    alt_MCsemilep_CP5Up,
    alt_MCsemilep_erdOn,
    alt_MCsemilep_QCDbased,
    alt_MCsemilep_GluonMove,
    alt_MCsemilep_mtop169p5,
    alt_MCsemilep_mtop175p5, 
    alt_MChad_hdampDown, 
    alt_MChad_hdampUp, 
    alt_MChad_CP5Down, 
    alt_MChad_CP5Up, 
    alt_MChad_erdOn, 
    alt_MChad_QCDbased, 
    alt_MChad_GluonMove, 
    alt_MChad_mtop169p5, 
    alt_MChad_mtop175p5
]





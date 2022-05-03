import os 
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

json = os.path.expandvars('$CMSSW_BASE/src/CMGTools/ttbar/data/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt')
lumi = 41529.

############################################################################
# MC
############################################################################


alt_MC_hdampUp = creator.makeMCComponent("alt_MC_hdampUp","/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_hdampUp.splitFactor = 10

alt_MC_hdampUp_pmx = creator.makeMCComponent("alt_MC_hdampUp_pmx","/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_hdampUp_pmx.splitFactor = 4

alt_MC_hdampDown_pmx = creator.makeMCComponent("alt_MC_hdampDown_pmx","/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_hdampDown_pmx.splitFactor = 6

alt_MC_hdampDown = creator.makeMCComponent("alt_MC_hdampDown","/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_hdampDown.splitFactor = 10

alt_MC_CP5Up_pmx = creator.makeMCComponent("alt_MC_CP5Up_pmx","/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_CP5Up_pmx.splitFactor = 6 

alt_MC_CP5Up = creator.makeMCComponent("alt_MC_CP5Up","/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_CP5Up.splitFactor = 10

alt_MC_CP5Down_pmx = creator.makeMCComponent("alt_MC_CP5Down_pmx","/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_CP5Down_pmx.splitFactor = 6

alt_MC_CP5Down = creator.makeMCComponent("alt_MC_CP5Down","/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_CP5Down.splitFactor = 10


alt_MC_erdOn = creator.makeMCComponent("alt_MC_erdOn","/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_erdOn.splitFactor = 6

alt_MC_QCDbased = creator.makeMCComponent("alt_MC_QCDbased","/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_QCDbased.splitFactor = 6

alt_MC_QCDbased_ext = creator.makeMCComponent("alt_MC_QCDbased_ext","/TTTo2L2Nu_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_QCDbased_ext.splitFactor = 10

alt_MC_GluonMove = creator.makeMCComponent("alt_MC_GluonMove","/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_GluonMove.splitFactor = 6

alt_MC_GluonMove_ext = creator.makeMCComponent("alt_MC_GluonMove","/TTTo2L2Nu_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_GluonMove_ext.splitFactor = 10

alt_MC_mtop169p5_pmx = creator.makeMCComponent("alt_MC_mtop169p5_pmx","/TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_mtop169p5_pmx.splitFactor = 5 

alt_MC_mtop169p5 = creator.makeMCComponent("alt_MC_mtop169p5","/TTTo2L2Nu_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_mtop169p5.splitFactor = 10

alt_MC_mtop175p5_pmx = creator.makeMCComponent("alt_MC_mtop175p5_pmx","/TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_mtop175p5_pmx.splitFactor = 5 

alt_MC_mtop175p5 = creator.makeMCComponent("alt_MC_mtop175p5","/TTTo2L2Nu_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 89.05);
alt_MC_mtop175p5.splitFactor = 10

##############


alt_MCsemilep_hdampDown = creator.makeMCComponent("alt_MCsemilep_hdampDown","/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_hdampDown.splitFactor = 27

alt_MCsemilep_hdampUp = creator.makeMCComponent("alt_MCsemilep_hdampUp","/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_hdampUp.splitFactor = 24 

alt_MCsemilep_CP5Down = creator.makeMCComponent("alt_MCsemilep_CP5Down","/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_CP5Down.splitFactor = 28

alt_MCsemilep_CP5Up = creator.makeMCComponent("alt_MCsemilep_CP5Up","/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_CP5Up.splitFactor = 21

alt_MCsemilep_erdOn = creator.makeMCComponent("alt_MCsemilep_erdOn","/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_erdOn.splitFactor = 10

alt_MCsemilep_QCDbased = creator.makeMCComponent("alt_MCsemilep_QCDbased","/TTToSemiLeptonic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_QCDbased.splitFactor = 28

alt_MCsemilep_GluonMove = creator.makeMCComponent("alt_MCsemilep_GluonMove","/TTToSemiLeptonic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_GluonMove.splitFactor = 28

alt_MCsemilep_mtop169p5_pmx = creator.makeMCComponent("alt_MCsemilep_mtop169p5_pmx","/TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_mtop169p5_pmx.splitFactor = 19

alt_MCsemilep_mtop169p5 = creator.makeMCComponent("alt_MCsemilep_mtop169p5","/TTToSemiLeptonic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_mtop169p5.splitFactor = 10

alt_MCsemilep_mtop175p5_pmx = creator.makeMCComponent("alt_MCsemilep_mtop175p5_pmx","/TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_mtop175p5_pmx.splitFactor = 19

alt_MCsemilep_mtop175p5 = creator.makeMCComponent("alt_MCsemilep_mtop175p5","/TTToSemiLeptonic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM","CMS",".*root", 366.9);
alt_MCsemilep_mtop175p5.splitFactor = 10

##############

alt_MChad_hdampDown = creator.makeMCComponent("alt_MChad_hdampDown","/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_hdampDown.splitFactor = 28

alt_MChad_hdampUp = creator.makeMCComponent("alt_MChad_hdampUp","/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_hdampUp.splitFactor = 28 

alt_MChad_CP5Down = creator.makeMCComponent("alt_MChad_CP5Down","/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_CP5Down.splitFactor = 28 

alt_MChad_CP5Up = creator.makeMCComponent("alt_MChad_CP5Up","/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_CP5Up.splitFactor = 28

alt_MChad_erdOn = creator.makeMCComponent("alt_MChad_erdOn","/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_erdOn.splitFactor = 27

alt_MChad_QCDbased = creator.makeMCComponent("alt_MChad_QCDbased","/TTToHadronic_TuneCP5CR1_QCDbased_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_QCDbased.splitFactor = 28

alt_MChad_GluonMove = creator.makeMCComponent("alt_MChad_GluonMove","/TTToHadronic_TuneCP5CR2_GluonMove_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_GluonMove.splitFactor = 28

alt_MChad_mtop169p5 = creator.makeMCComponent("alt_MChad_mtop169p5","/TTToHadronic_mtop169p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_mtop169p5.splitFactor = 19

alt_MChad_mtop175p5_pmx = creator.makeMCComponent("alt_MChad_mtop175p5_pmx","/TTToHadronic_mtop175p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root", 377.96);
alt_MChad_mtop175p5_pmx.splitFactor = 20


##############

alt_MC_ST_s_mtop169p5 = creator.makeMCComponent("alt_MC_ST_s_top_mtop169p5","/ST_s-channel_4f_leptonDecays_mtop1695_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 10.32);
alt_MC_ST_s_mtop169p5.splitFactor = 5

alt_MC_ST_s_mtop175p5 = creator.makeMCComponent("alt_MC_ST_s_mtop175p5", "/ST_s-channel_4f_leptonDecays_mtop1755_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 10.32);
alt_MC_ST_s_mtop175p5.splitFactor = 5

alt_MC_ST_t_top_mtop169p5 = creator.makeMCComponent("alt_MC_ST_t_top_mtop169p5", "/ST_t-channel_top_4f_InclusiveDecays_mtop1695_TuneCP5_PSweights_13TeV-powheg-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS", ".*root",136.02);
alt_MC_ST_t_top_mtop169p5.splitFactor = 10

alt_MC_ST_t_top_mtop175p5 = creator.makeMCComponent("alt_MC_ST_t_top_mtop175p5", "/ST_t-channel_top_4f_InclusiveDecays_mtop1755_TuneCP5_PSweights_13TeV-powheg-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS", ".*root",136.02);
alt_MC_ST_t_top_mtop175p5.splitFactor = 10

alt_MC_ST_t_antitop_mtop169p5 = creator.makeMCComponent("alt_MC_ST_t_antitop_mtop169p5", "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1695_TuneCP5_PSweights_13TeV-powheg-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS", ".*root",80.95);
alt_MC_ST_t_antitop_mtop169p5.splitFactor = 10

alt_MC_ST_t_antitop_mtop173p5 = creator.makeMCComponent("alt_MC_ST_t_antitop_mtop173p5", "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1735_TuneCP5_PSweights_13TeV-powheg-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS", ".*root",80.95);
alt_MC_ST_t_antitop_mtop173p5.splitFactor = 10
#Careful, no 175.5 for this one

alt_MC_tW_top_mtop169p5 = creator.makeMCComponent("alt_MC_tW_top_mtop169p5","/ST_tW_top_5f_inclusiveDecays_mtop1695_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS", ".*root",35.5);
alt_MC_tW_top_mtop169p5.splitFactor = 4

alt_MC_tW_top_mtop175p5 = creator.makeMCComponent("alt_MC_tW_top_mtop175p5","/ST_tW_top_5f_inclusiveDecays_mtop1755_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS", ".*root",35.5);
alt_MC_tW_top_mtop175p5.splitFactor = 4

alt_MC_tW_antitop_mtop169p5 = creator.makeMCComponent("alt_MC_tW_antitop_mtop169p5", "/ST_tW_antitop_5f_inclusiveDecays_mtop1695_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS", ".*root",35.5);
alt_MC_tW_antitop_mtop169p5.splitFactor = 4

alt_MC_tW_antitop_mtop175p5 = creator.makeMCComponent("alt_MC_tW_antitop_mtop175p5", "/ST_tW_antitop_5f_inclusiveDecays_mtop1755_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM","CMS", ".*root",35.5);
alt_MC_tW_antitop_mtop175p5.splitFactor = 4




alt_ttbar_test = [
    alt_MChad_mtop175p5_pmx
]

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
    alt_MC_QCDbased,
    alt_MC_QCDbased_ext,
    alt_MC_GluonMove,
    alt_MC_GluonMove_ext,
    alt_MC_mtop169p5_pmx,
    alt_MC_mtop169p5,
    alt_MC_mtop175p5_pmx,
    alt_MC_mtop175p5,
    alt_MCsemilep_hdampDown, 
    alt_MCsemilep_hdampUp,
    alt_MCsemilep_CP5Down,
    alt_MCsemilep_CP5Up,
    alt_MCsemilep_erdOn,
    alt_MCsemilep_QCDbased,
    alt_MCsemilep_GluonMove,
    alt_MCsemilep_mtop169p5_pmx,
    alt_MCsemilep_mtop169p5,
    alt_MCsemilep_mtop175p5_pmx,
    alt_MCsemilep_mtop175p5, 
    alt_MChad_hdampDown, 
    alt_MChad_hdampUp, 
    alt_MChad_CP5Down, 
    alt_MChad_CP5Up, 
    alt_MChad_erdOn, 
    alt_MChad_QCDbased, 
    alt_MChad_GluonMove, 
    alt_MChad_mtop169p5, 
    alt_MChad_mtop175p5_pmx
]

alt_singletop = [
    alt_MC_ST_s_mtop169p5,
    alt_MC_ST_s_mtop175p5,
    alt_MC_ST_t_top_mtop169p5,
    alt_MC_ST_t_top_mtop175p5, 
    alt_MC_ST_t_antitop_mtop169p5, 
    alt_MC_ST_t_antitop_mtop173p5, 
    alt_MC_tW_top_mtop169p5, 
    alt_MC_tW_top_mtop175p5, 
    alt_MC_tW_antitop_mtop169p5, 
    alt_MC_tW_antitop_mtop175p5 
]

alt_ttbar = alt_ttbar + alt_singletop


import os
import ROOT

import PhysicsTools.HeppyCore.framework.config     as cfg
from   PhysicsTools.HeppyCore.framework.config     import printComps
from   PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
from   PhysicsTools.HeppyCore.framework.looper     import Looper
from   PhysicsTools.HeppyCore.framework.event      import Event
from   CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
Event.print_patterns = ['*taus*', 
                        '*muons*', 
                        '*electrons*', 
                        'veto_*', 
                        '*dileptons_*', 
                        '*jets*']

#import pdb; pdb.set_trace()

#ComponentCreator.useAAA = True
ComponentCreator.useLyonAAA = True

import logging
logging.shutdown()
#reload(logging)
logging.basicConfig(level=logging.WARNING)

############################################################################
# Options
############################################################################

# Get all heppy options; set via "-o production" or "-o production=True"

# production = True run on batch, production = False run locally
test       = getHeppyOption('test', False)
syncntuple = getHeppyOption('syncntuple', True)
data       = getHeppyOption('data', True)
alternate  = getHeppyOption('alternate', False)
year       = getHeppyOption('year', '2016' )
tes_string = getHeppyOption('tes_string', '') # '_tesup' '_tesdown'
reapplyJEC = getHeppyOption('reapplyJEC', True)
btagger    = getHeppyOption('btagger', 'DeepCSV')

############################################################################
# Components
############################################################################
if year == '2016':
    #from CMGTools.ttbar.samples.summer16.ttbar2016 import mc_signal_dilep as mc_ttbar
    from CMGTools.ttbar.samples.summer16.ttbar2016 import mc_ttbar
    #from CMGTools.ttbar.samples.summer16.ttbar2016 import mc_ttbar_test
    from CMGTools.ttbar.samples.summer16.ttbar_alternative_2016   import alt_ttbar
    from CMGTools.ttbar.samples.summer16.ttbar2016 import data_elecmuon
    from CMGTools.ttbar.samples.summer16.trigger   import data_triggers
    from CMGTools.ttbar.samples.summer16.trigger   import mc_triggers
if year == '2017':
    from CMGTools.ttbar.samples.fall17.ttbar2017   import mc_ttbar
    from CMGTools.ttbar.samples.fall17.ttbar_alternative_2017   import alt_ttbar
    from CMGTools.ttbar.samples.fall17.ttbar2017   import data_elecmuon
    #from CMGTools.ttbar.samples.fall17.ttbar2017   import data_singles ##
    #from CMGTools.ttbar.samples.fall17.ttbar2017   import data_muon_electron ##
    from CMGTools.ttbar.samples.fall17.trigger     import data_triggers
    from CMGTools.ttbar.samples.fall17.trigger     import mc_triggers

#data_files = data_singles
data_files = data_elecmuon

events_to_pick = []

# JEC Tag stored as GT
#https://twiki.cern.ch/twiki/bin/view/CMS/JECDataMC
if year == '2016':
    gt_mc   = 'Summer16_07Aug2017_V11_MC'
    gt_data = 'Summer16_07Aug2017{}_V11_DATA'
if year == '2017':    
    gt_mc   = 'Fall17_17Nov2017_V32_MC'
    gt_data = 'Fall17_17Nov2017{}_V32_DATA'



# PileUp
if year == '2016':    
    puFileData     = '$CMSSW_BASE/src/CMGTools/ttbar/data/2016/MyDataPileupHistogram.root'
    puFileDataUp   = '$CMSSW_BASE/src/CMGTools/ttbar/data/2016/MyDataPileupHistogram_up.root'
    puFileDataDown = '$CMSSW_BASE/src/CMGTools/ttbar/data/2016/MyDataPileupHistogram_down.root'
    puFileMC       = '$CMSSW_BASE/src/CMGTools/ttbar/data/2016/pileup.root'
    puFileMCalt    = '$CMSSW_BASE/src/CMGTools/ttbar/data/2016/pileup_alternative.root'
    
if year == '2017':
    puFileData     = '$CMSSW_BASE/src/CMGTools/ttbar/data/2017/pudistributions_data_2017.root'
    puFileDataUp   = '$CMSSW_BASE/src/CMGTools/ttbar/data/2017/pudistributions_data_2017_up.root'
    puFileDataDown = '$CMSSW_BASE/src/CMGTools/ttbar/data/2017/pudistributions_data_2017_down.root'
    puFileMC       = '$CMSSW_BASE/src/CMGTools/ttbar/data/2017/pudistributions_mc_2017.root'
    puFileMCalt    = '$CMSSW_BASE/src/CMGTools/ttbar/data/2017/pudistributions_mc_alt_2017.root'

#print data_triggers 
for sample in data_files:
    #print sample
    #sample.name[sample.name.find('2017')+4] are era A,B,C,D,E and F
    #print sample.name, sample.name.find(year), sample.name.find(year)+4, sample.name[sample.name.find(year)+4], data_triggers[sample.name[sample.name.find(year)+4]]
    sample.triggers = data_triggers[sample.name[sample.name.find(year)+4]]
    era = sample.name[sample.name.find(year)+4]
    if year == '2017':
        if 'V32' in gt_data and era in ['D','E']:
            era = 'DE'
    elif year == '2016':
        if 'V11' in gt_data and era in ['B','C','D']:
            era = 'BCD'
        if 'V11' in gt_data and era in ['E','F']:
            era = 'EF'
        if 'V11' in gt_data and era in ['G','H']:
            era = 'GH'
    sample.dataGT = gt_data.format(era)

if not data:
    if not alternate:
        selectedComponents = mc_ttbar
    else:
        selectedComponents = alt_ttbar
elif data:
    selectedComponents = data_files

for sample in selectedComponents:
    #sample.splitFactor = 50
    if not data:
        sample.puFileData  = puFileData
        sample.triggers    = mc_triggers
        sample.puFileMC    = puFileMC

        if alternate:
            #sample.splitFactor = 40
            sample.puFileMC = puFileMCalt

        #if year=='2016' and 'signal' in sample.name:
            #sample.splitFactor = 80
            #print sample.name, sample.splitFactor

        #if 'wjets' in sample.name:
            #sample.splitFactor = 100
            #print sample.name, sample.splitFactor
        print sample.name, sample.splitFactor 
      
############################################################################
# Test
############################################################################
if year == '2016':    
    import CMGTools.ttbar.samples.summer16.ttbar2016 as backgrounds_forindex
    #import CMGTools.ttbar.samples.summer16.ttbar_alternative_2016 as backgrounds_forindex    
if year == '2017':
    import CMGTools.ttbar.samples.fall17.ttbar2017 as backgrounds_forindex    
    #import CMGTools.ttbar.samples.fall17.ttbar_alternative_2017 as backgrounds_forindex    

from CMGTools.ttbar.samples.component_index import ComponentIndex
bindex = ComponentIndex(backgrounds_forindex)


if test:
    cache = True
    if not data:
	comp = bindex.glob('background_MC_WW')[0]
	#comp = bindex.glob('background_MC_WJets')[0]
	#comp = bindex.glob('background_MC_DY')[0]
        #comp = bindex.glob('background_MC_DY_50')[0]
        #comp = bindex.glob('background_MC_TTZ')[0]
        #comp = bindex.glob('background_MC_TTW')[0]
	#comp = bindex.glob('background_MC_ST_s')[0]
	#comp = bindex.glob('background_MC_ST_t_top')[0]
	#comp = bindex.glob('background_MC_tW_top')[0]
        #comp = bindex.glob('MC_signal_dilep')[0]
               #MC_signal_dilep
               #alt_MC_hdampUp
               #MC_signal_dilep
               #MC_signal_hadronic
	       #MC_zjets_DY_1050
	       #MC_zjets_DY_502
    else:
        #comp = selectedComponents[0]
        #comp = bindex.glob('MuonEG_Run2017B_31Mar2018')[0]
        comp = bindex.glob('MuonEG_Run2017B_31Mar2018')[0]
                # SingleElectron_Run2017E_31Mar2018
    selectedComponents   = [comp]
    comp.files           = [comp.files[5]]
    comp.splitFactor     = 1
    comp.fineSplitFactor = 1
    #selectedComponents   = mc_resubmit

############################################################################
# Analyzers 
############################################################################
from PhysicsTools.Heppy.analyzers.core.JSONAnalyzer      import JSONAnalyzer
from PhysicsTools.Heppy.analyzers.core.SkimAnalyzerCount import SkimAnalyzerCount
from PhysicsTools.Heppy.analyzers.objects.VertexAnalyzer import VertexAnalyzer
from CMGTools.ttbar.analyzers.TriggerAnalyzer            import TriggerAnalyzer
from CMGTools.ttbar.analyzers.Debugger                   import Debugger
from CMGTools.ttbar.analyzers.EventFilter                import EventFilter
from CMGTools.ttbar.analyzers.Selector                   import Selector

json = cfg.Analyzer(JSONAnalyzer,
                    name='JSONAnalyzer',)

skim = cfg.Analyzer(SkimAnalyzerCount,
                    name='SkimAnalyzerCount')

trigger = cfg.Analyzer(TriggerAnalyzer,
                       name='TriggerAnalyzer',
                       addTriggerObjects=False,
                       requireTrigger=True,
                       usePrescaled=True)

vertex = cfg.Analyzer(VertexAnalyzer,
                      name='VertexAnalyzer',
                      fixedWeight=1,
                      keepFailingEvents=False,
                      verbose=False)


debugger = cfg.Analyzer(Debugger,
                        name = 'Debugger',
                        condition = lambda x: True)


############################################################################
# Time
############################################################################
from CMGTools.ttbar.analyzers.TimeAnalyzer import TimeAnalyzer

time = cfg.Analyzer(TimeAnalyzer,
                    name = 'TimeAnalyzer',
                    year = year,
                    data = data)


############################################################################
# Muon 
############################################################################
# setting up an alias for our isolation, now use iso_htt everywhere
from PhysicsTools.Heppy.physicsobjects.Muon     import Muon
from CMGTools.ttbar.analyzers.MuonSF            import MuonSF
from CMGTools.ttbar.analyzers.MuonSystematic    import MuonSystematic
from CMGTools.ttbar.analyzers.MuonAnalyzer      import MuonAnalyzer


Muon.iso_htt = lambda x: x.relIso(0.4, 
                                  'dbeta', 
                                  dbeta_factor = 0.5, 
                                  all_charged = False)

muons = cfg.Analyzer(MuonAnalyzer,
                     name = 'MuonAnalyzer',
                     output = 'muons',
                     muons = 'slimmedMuons',)

def select_muon_function(muon): #boolean use to select good muons
    return muon.pt() > 20 and \
           abs(muon.eta()) < 2.4 and\
           muon.tightId() and\
           muon.iso_htt() < 0.15 
    # https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2

def exclude_muon_function(muon):
    return muon.pt() > 10 and \
           abs(muon.eta()) < 2.4 and\
           muon.looseId() and\
           muon.iso_htt() < 0.25 and\
           not(select_muon_function(muon))

select_muon = cfg.Analyzer(Selector,
                           'select_muon',
                           output = 'select_muon',
                           src = 'muons',
                           filter_func = select_muon_function)

exclude_muon = cfg.Analyzer(Selector,
                           'exclude_muon',
                           output = 'exclude_muon',
                           src = 'muons',
                           filter_func = exclude_muon_function)

reweight_muon = cfg.Analyzer(MuonSF, 
                             'reweight_muon', 
                             muons = 'select_muon', 
                             year = year)

one_muon = cfg.Analyzer(EventFilter, 
                        'one_muon',
                        src = 'select_muon',
                        filter_func = lambda x : len(x)>0)
                        
exclude_loose_muon = cfg.Analyzer(EventFilter,
                                 'exlude_loose_muon',
                                 src='exclude_muon',
                                 filter_func = lambda x : len(x)==0)

systematic_muon = cfg.Analyzer(MuonSystematic, 
                             'systematic_muon', 
                             muons = 'select_muon', 
                             year = year)



############################################################################
# Electron 
############################################################################
# setting up an alias for our isolation, now use iso_htt everywhere
from PhysicsTools.Heppy.physicsobjects.Electron         import Electron
from PhysicsTools.Heppy.physicsutils.EffectiveAreas     import areas
from CMGTools.ttbar.analyzers.ElectronSF                import ElectronSF
from CMGTools.ttbar.analyzers.ElectronAnalyzer          import ElectronAnalyzer
from CMGTools.ttbar.analyzers.ElectronSystematic        import ElectronSystematic

Electron.EffectiveArea03 = areas['Fall17']['electron']

Electron.iso_htt = lambda x: x.relIso(0.3,
                                      "EA", #effective area
                                      all_charged=False)

electrons = cfg.Analyzer(ElectronAnalyzer,
                         output = 'electrons',
                         electrons = 'slimmedElectrons',) #name in MiniAOD


def is_out_gap_ECAL(electron):
    return abs(electron.superCluster().eta()) >= 1.5660 or\
           abs(electron.superCluster().eta()) <= 1.4442

def select_electron_function(electron): #function use in the next Analyzer
    return electron.pt() > 20 and\
           abs(electron.eta()) < 2.4 and\
           is_out_gap_ECAL(electron) and\
           electron.id_passes("cutBasedElectronID-Fall17-94X-V2","tight") 
           
def exclude_electron_function(electron): #function use in the next Analyzer
    return electron.pt() > 10 and\
           abs(electron.eta()) < 2.4 and\
           is_out_gap_ECAL(electron) and\
           electron.id_passes("cutBasedElectronID-Fall17-94X-V2","veto") and\
           not(select_electron_function(electron))

#electron.id_passes("cutBasedElectronID-Fall17-94X-V2","tight") 
#electron.id_passes("cutBasedElectronID-Fall17-94X-V2","veto") and\

select_electron = cfg.Analyzer(Selector,
                               'select_electron',
                               output = 'select_electron',
                               src = 'electrons',
                               filter_func = select_electron_function)

exclude_electron = cfg.Analyzer(Selector,
                              'exclude_electron',
                              output = 'exclude_electron',
                              src = 'electrons',
                              filter_func = exclude_electron_function)
                         
reweight_electron = cfg.Analyzer(ElectronSF, 
                                 'reweight_electron', 
                                 electrons = 'select_electron', 
                                 year = year)
                               
one_electron = cfg.Analyzer(EventFilter, 
                            'one_electron',
                            src = 'select_electron',
                            filter_func = lambda x : len(x)>0)

exclude_loose_electron = cfg.Analyzer(EventFilter,
                                     'exclude_loose_electron',
                                     src='exclude_electron',
                                     filter_func = lambda x : len(x)==0)

systematic_electron = cfg.Analyzer(ElectronSystematic, 
                                    'systematic_electron', 
                                    electrons = 'select_electron', 
                                    year = year)



############################################################################
# Dilepton 
############################################################################
from CMGTools.ttbar.analyzers.DiLeptonAnalyzer  import DiLeptonAnalyzer
from CMGTools.ttbar.analyzers.DilepTriggerSF    import DilepTriggerSF
from CMGTools.ttbar.analyzers.DilepTriggerSyst  import DilepTriggerSyst
from CMGTools.ttbar.analyzers.Sorter            import Sorter

dilepton = cfg.Analyzer(DiLeptonAnalyzer,
                        output = 'dileptons',
                        l1 = 'select_muon',
                        l2 = 'select_electron',
                        dr_min = 0.5) #unspecified


def select_dilepton_function(dilep): #function use in the next Analyzer
    return dilep.mass() > 20 and \
           (dilep.leg1().charge() + dilep.leg2().charge()) == 0 and\
           ((dilep.leg1().pt()>25 and dilep.leg2().pt()>20) == True or\
           (dilep.leg1().pt()>20 and dilep.leg2().pt()>25) == True)

select_dilepton = cfg.Analyzer(Selector,
                         'select_dilepton',
                         output = 'select_dilepton',
                         src = 'dileptons',
                         filter_func = select_dilepton_function)

reweight_dilepton_trig = cfg.Analyzer(DilepTriggerSF, 
                                      'reweight_dilepton', 
                                      dilepton = 'select_dilepton', 
                                      year =year)

only_one_dilepton = cfg.Analyzer(EventFilter, 
                            name = 'OneDilepton',
                            src = 'select_dilepton',
                            filter_func = lambda x : len(x)==1)

systematic_dilepton = cfg.Analyzer(DilepTriggerSyst, 
                                      'systematic_dilepton', 
                                      dilepton = 'select_dilepton', 
                                      year =year)


#completely useless with 1 dilepton but in case of ..
dilepton_sorted = cfg.Analyzer(
    Sorter,
    output = 'dileptons_sorted',
    src = 'dileptons',
    metric = lambda x : x.pt(),
    reverse = False
    )


############################################################################
# Jets 
############################################################################
from CMGTools.ttbar.analyzers.JetAnalyzer import JetAnalyzer
from CMGTools.ttbar.analyzers.JetCleaner  import JetCleaner

def select_good_jets_FixEE2017(jet): #function use in the next Analyzer
    return jet.correctedJet("Uncorrected").pt() > 50. or\
           abs(jet.eta()) < 2.65 or\
           abs(jet.eta()) > 3.139

if year == '2016':
    jets = cfg.Analyzer(JetAnalyzer, 
                        output = 'jets',
                        jets = 'slimmedJets',
                        do_jec = True,
                        gt_mc = gt_mc,
                        year = year)
                        
else:
    
    jets = cfg.Analyzer(JetAnalyzer, 
                        output = 'jets',
                        jets = 'slimmedJets',
                        do_jec = True,
                        gt_mc = gt_mc,
                        year = year,
                        selection = select_good_jets_FixEE2017)


from CMGTools.ttbar.analyzers.Calibrator import Calibrator

#up_down = ['up','down']
#
#if not data:
#    JES = [
#        #'CMS_scale_j_eta0to5_13Tev',
#        #'CMS_scale_j_eta0to3_13TeV',
#        #'CMS_scale_j_eta3to5_13TeV',
#        'CMS_scale_j_RelativeBal_13TeV'
#        #'CMS_scale_j_RelativeSample_13TeV'
#        ]
#    for source in JES:
#        jet_calibrator = cfg.Analyzer(
#            Calibrator,
#            src = 'jets',
#            calibrator_factor_func = lambda x: getattr(x,"corr_{}_JEC_{}".format(source,'up'), 1./x.rawFactor()) * x.rawFactor()
#            #calibrator_factor_func = lambda x: getattr(x,"corr_{}_JEC_{}".format(source,'down'), 1./x.rawFactor()) * x.rawFactor()
#            )
       
# From https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVRun2017


jet_sorter = cfg.Analyzer(
    Sorter,
    output = 'jets_sorted',
    src = 'jets',
    metric = lambda jet: (jet.pt()),
    reverse = True
    )




if year == '2016':
    def select_jets_IDpt(jet): #function use in the next Analyzer
        return  jet.pt()>20 and\
                abs(jet.eta())<2.4 and\
                jet.jetID("POG_PFID_TightLepVeto2016")
else : 
    def select_jets_IDpt(jet): #function use in the next Analyzer
        return  jet.pt()>20 and\
                abs(jet.eta())<2.4 and\
                jet.jetID("POG_PFID_TightLepVeto")

jets_20_unclean = cfg.Analyzer(Selector,
                               'jets_20_unclean',
                               output = 'jets_20_unclean',
                               src = 'jets_sorted',
                               filter_func = select_jets_IDpt)

jet_20_electron_clean = cfg.Analyzer(JetCleaner,
                      output = 'jets_20_electron_clean',
                      leptons = 'select_electron',
                      jets = 'jets_20_unclean',
                      drmin = 0.4)
                      
jet_20_clean = cfg.Analyzer(JetCleaner,
                      output = 'jets_20_clean',
                      leptons = 'select_muon',
                      jets = 'jets_20_electron_clean',
                      drmin = 0.4)

jets_30 = cfg.Analyzer(Selector,
                       'jets_30',
                       output = 'jets_30',
                       src = 'jets_20_clean',
                       filter_func = lambda x : x.pt()>30)
                       
two_jets = cfg.Analyzer(EventFilter, 
                        name = 'TwoJets',
                        src = 'jets_30',
                        filter_func = lambda x : len(x)>1)




############################################################################
# b-Jets 
############################################################################
from CMGTools.ttbar.analyzers.BJetAnalyzer    import BJetAnalyzer


btaganalyzer = cfg.Analyzer(BJetAnalyzer, 
                       'btagger', 
                       jets = 'jets_30', 
                       year = year, 
                       tagger = btagger)

one_bjets = cfg.Analyzer(EventFilter, 
                         name = 'OneBJets',
                         src = 'bjets_30',
                         filter_func = lambda x : len(x)>0)

#always put after btaganalyzer
bjets_30 = cfg.Analyzer(Selector, 
                        'bjets_30',
                        output = 'bjets_30', 
                        src = 'jets_30',
                        filter_func = lambda x: x.is_btagged)


############################################################################
# Generator stuff 
############################################################################
#from PhysicsTools.Heppy.analyzers.gen.LHEWeightAnalyzer import LHEWeightAnalyzer
from CMGTools.ttbar.analyzers.PileUpAnalyzer            import PileUpAnalyzer
from CMGTools.ttbar.analyzers.GenAnalyzer               import GenAnalyzer
from CMGTools.ttbar.analyzers.GenMatcherAnalyzer        import GenMatcherAnalyzer
from CMGTools.ttbar.analyzers.MCWeighter                import MCWeighter
from CMGTools.ttbar.analyzers.NJetsAnalyzer             import NJetsAnalyzer
from CMGTools.ttbar.analyzers.METAnalyzer               import METAnalyzer
from CMGTools.ttbar.analyzers.LHEWeightAnalyzer 	import LHEWeightAnalyzer

#"genmatcher = cfg.Analyzer(
#    GenMatcherAnalyzer, 
#    'genmatcher',
#    jetCol='slimmedJets',
#    genPtCut=8.,
#    genmatching = True,
#    filter_func = select_dilepton
#)

gen_particles = cfg.Analyzer(GenAnalyzer,
                             name='GenAnalyzer',
                             jetCol='slimmedJets',
                             genmatching=True,
                             genPtCut=8.,
                             workspace_path='$CMSSW_BASE/src/CMGTools/ttbar/data/gen_scalefactors_v2.root'
                             )

#pfmetana = cfg.Analyzer(METAnalyzer,
#                        name='PFMetana',
#                        recoil_correction_file='HTT-utilities/RecoilCorrections/data/Type1_PFMET_2017.root',
#                        met = 'pfmet',
#                        apply_recoil_correction= True,#Recommendation states loose pfjetID for jet multiplicity but this WP is not supported anymore?
#                        runFixEE2017= True)

#lheweight = cfg.Analyzer(LHEWeightAnalyzer,
#                         name="LHEWeightAnalyzer",
#                         useLumiInfo=False)

pileup = cfg.Analyzer(PileUpAnalyzer,
                      name='PileUpAnalyzer',
                      true=True,
                      autoPU=False,
                      puFileDataUp   = puFileDataUp,
                      puFileDataDown = puFileDataDown)

lheanalyzer = cfg.Analyzer(LHEWeightAnalyzer,
			   name='LHEWeightAnalyzer',
			   useLumiInfo=False)

mcweighter = cfg.Analyzer(MCWeighter,
                          name='MCWeighter')

njets_ana = cfg.Analyzer(NJetsAnalyzer,
                         name='NJetsAnalyzer',
                         fillTree=True,
                         verbose=False)



############################################################################
# Ntuples 
############################################################################
from CMGTools.ttbar.ntuple.NtupleProducer import NtupleProducer
if year == '2016':
    from CMGTools.ttbar.ntuple.NtupleCreator import common2016 as event_content_test
if year == '2017':
    from CMGTools.ttbar.ntuple.NtupleCreator import common2017 as event_content_test

ntuple = cfg.Analyzer(NtupleProducer,
                      name = 'NtupleProducer',
                      outputfile = 'events.root',
                      treename = 'events',
                      event_content = event_content_test)
                      
from CMGTools.ttbar.analyzers.PrefiringAnalyzer import PrefiringAnalyzer
if year == '2016':
    prefiringana = cfg.Analyzer(PrefiringAnalyzer, 
                                name='PrefiringAnalyzer',
                                L1Maps = '$CMSSW_BASE/src/CMGTools/RootTools/data/L1PrefiringMaps_new.root',
                                photons = 'slimmedPhotons',
                                jets = 'slimmedJets',
                                DataEra = '2016BtoH',
                                UseJetEMPt = False ,
                                PrefiringRateSystematicUncty =  0.2 , 
                                jetMaxMuonFraction=0.5,
                                SkipWarnings= True,

                            )
if year == '2017':
    prefiringana = cfg.Analyzer(PrefiringAnalyzer, 
                                name='PrefiringAnalyzer',
                                L1Maps = '$CMSSW_BASE/src/CMGTools/RootTools/data/L1PrefiringMaps_new.root',
                                photons = 'slimmedPhotons',
                                jets = 'slimmedJets',
                                DataEra = '2017BtoF',
                                UseJetEMPt = False ,
                                PrefiringRateSystematicUncty =  0.2 , 
                                jetMaxMuonFraction=0.5,
                                SkipWarnings= True,
                            )


sequence = cfg.Sequence([
    mcweighter,
    lheanalyzer,
# Analyzers
    json,
    vertex,
    gen_particles,
    trigger,
    #trigger_match,
    #lheweight,
    pileup,
    
# Time
    time,
# Muon
    muons,
    select_muon,
    exclude_muon,
    reweight_muon,
    one_muon,
    exclude_loose_muon,
    systematic_muon,
# Electron
    electrons,
    select_electron,
    exclude_electron,
    reweight_electron,
    one_electron,
    exclude_loose_electron,
    systematic_electron,
# Dilepton
    dilepton,
    select_dilepton,
    reweight_dilepton_trig,
    systematic_dilepton,
    only_one_dilepton,
    dilepton_sorted,
# Jets
    jets,
    jet_sorter,
    #jet_calibrator, 
    jets_20_unclean,
    jet_20_electron_clean,
    jet_20_clean,
    jets_30,
    two_jets,
# b-jets
    btaganalyzer,
    bjets_30,
    one_bjets,
# Rescaling
    #met_filters,
    njets_ana,
#Met
    # Ntple
    prefiringana,
    #debugger,
    ntuple
])


############################################################################
from PhysicsTools.Heppy.analyzers.core.EventSelector import EventSelector

if events_to_pick:
    from CMGTools.ttbar.ntuple.ntuple_base_cff import eventSelector
    eventSelector.toSelect = events_to_pick
    sequence.insert(0, eventSelector)

# the following is declared in case this cfg is used in input to the
# heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config(components=selectedComponents,
                    sequence=sequence,
                    services=[],
                    events_class=Events)

printComps(config.components, True)







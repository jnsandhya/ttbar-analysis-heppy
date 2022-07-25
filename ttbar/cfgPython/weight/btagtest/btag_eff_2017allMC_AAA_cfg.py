import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
from PhysicsTools.HeppyCore.framework.config import printComps
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

test = getHeppyOption('test', False)
year = getHeppyOption('year', '2017' )
btagger = getHeppyOption('btagger', 'DeepCSV' )


#ComponentCreator.useLyonAAA = True
ComponentCreator.useAAA = True


################################################################################
# Analyzers 
################################################################################
from PhysicsTools.Heppy.analyzers.core.JSONAnalyzer import JSONAnalyzer
from PhysicsTools.Heppy.analyzers.core.SkimAnalyzerCount import SkimAnalyzerCount
from PhysicsTools.Heppy.analyzers.objects.VertexAnalyzer import VertexAnalyzer

json = cfg.Analyzer(JSONAnalyzer,
                    name='JSONAnalyzer',)

vertex = cfg.Analyzer(VertexAnalyzer,
                      name='VertexAnalyzer',
                      fixedWeight=1,
                      keepFailingEvents=True,
                      verbose=False)


################################################################################
# Components
################################################################################
if (year == '2016'):
    from CMGTools.ttbar.samples.summer16.ttbar2016 import mc_ttbar
elif(year == '2017'):
    from CMGTools.ttbar.samples.fall17.ttbar2017  import mc_ttbar_AAA as mc_ttbar

events_to_pick = []
selectedComponents = mc_ttbar

################################################################################

############################################################################
# Test
############################################################################
if(year == '2016'):    
    import CMGTools.ttbar.samples.summer16.ttbar2016 as backgrounds_forindex
elif(year == '2017'):
    import CMGTools.ttbar.samples.fall17.ttbar2017 as backgrounds_forindex    


from CMGTools.ttbar.samples.component_index import ComponentIndex
bindex = ComponentIndex(backgrounds_forindex)

if test:
    cache = True
    comp = bindex.glob('MC_signal_dilep')[0]
                        #MC_a_dilep
                        #'MC_y_DY_50'
    selectedComponents = [comp]
    comp.files = [comp.files[0]]
    comp.splitFactor = 1
    comp.fineSplitFactor = 1


############################################################################
# Muon 
############################################################################
# setting up an alias for our isolation, now use iso_htt everywhere
from PhysicsTools.Heppy.physicsobjects.Muon     import Muon
from CMGTools.ttbar.analyzers.MuonAnalyzer      import MuonAnalyzer
from CMGTools.ttbar.analyzers.EventFilter       import EventFilter
from CMGTools.ttbar.analyzers.Selector          import Selector

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

select_muon = cfg.Analyzer(Selector,
                           'select_muon',
                           output = 'select_muon',
                           src = 'muons',
                           filter_func = select_muon_function)

one_muon = cfg.Analyzer(EventFilter, 
                        'one_muon',
                        src = 'select_muon',
                        filter_func = lambda x : len(x)==1)

################################################################################
# Electron 
############################################################################
# setting up an alias for our isolation, now use iso_htt everywhere
from PhysicsTools.Heppy.physicsobjects.Electron          import Electron
from PhysicsTools.Heppy.physicsutils.EffectiveAreas      import areas
from CMGTools.ttbar.analyzers.ElectronSF                import ElectronSF
from CMGTools.ttbar.analyzers.ElectronAnalyzer          import ElectronAnalyzer

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
           
select_electron = cfg.Analyzer(Selector,
                               'select_electron',
                               output = 'select_electron',
                               src = 'electrons',
                               filter_func = select_electron_function)

one_electron = cfg.Analyzer(EventFilter, 
                            'one_electron',
                            src = 'select_electron',
                            filter_func = lambda x : len(x)==1)

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

only_one_dilepton = cfg.Analyzer(EventFilter, 
                            name = 'OneDilepton',
                            src = 'select_dilepton',
                            filter_func = lambda x : len(x)==1)


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
from CMGTools.ttbar.analyzers.BJetEfficiencyCreator import BJetEfficiencyCreator
from CMGTools.ttbar.analyzers.Sorter            import Sorter

if year == '2016':
    gt_mc = 'Summer16_07Aug2017_V11_MC'
    JERFileMC      = '/gridgroup/cms/sjain/CMSSW_10_4_0/src/CMGTools/ttbar/data/2016/jer/Summer16_25nsV1b_MC_PtResolution_AK4PFchs.txt'
else:
    JERFileMC       = "/gridgroup/cms/sjain/CMSSW_10_4_0/src/CMGTools/ttbar/data/2017/jer/Fall17_V3b_MC_PtResolution_AK4PFchs.txt"
    gt_mc = 'Fall17_17Nov2017_V32_MC'


def select_good_jets_FixEE2017(jet): #function use in the next Analyzer
    return jet.correctedJet("Uncorrected").pt() > 50. or\
           abs(jet.eta()) < 2.65 or\
           abs(jet.eta()) > 3.139
          
if year == '2016':
    jets = cfg.Analyzer(JetAnalyzer, 
                        output = 'jets',
                        jets = 'slimmedJets',
                        genJetCol = 'slimmedGenJets',
                        rho = ('fixedGridRhoFastjetAll','',''),
                        jer = JERFileMC,
                        smearJets = True,
                        shiftJER = 0,
                        addJERShifts = 1,
                        do_mc_match=True,
                        do_jec = True,
                        gt_mc = gt_mc,
                        year = year)
                        
else:
    jets = cfg.Analyzer(JetAnalyzer, 
                        output = 'jets',
                        jets = 'slimmedJets',
                        genJetCol = 'slimmedGenJets',
                        rho = ('fixedGridRhoFastjetAll','',''),
                        jer = JERFileMC,
                        smearJets = True,
                        shiftJER = 0,
                        addJERShifts = 1,
                        do_mc_match=True,
                        do_jec = True,
                        gt_mc = gt_mc,
                        year = year,
                        selection = select_good_jets_FixEE2017)

# From https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVRun2017

jet_sorter = cfg.Analyzer(
    Sorter,
    output = 'jets_sorted',
    src = 'jets',
    metric = lambda jet: (jet.pt()),
    reverse = True
    )

def select_jets_pteta(jet): #function use in the next Analyzer
        return  jet.pt()>20 and\
                abs(jet.eta())<2.4

jets_20_unclean = cfg.Analyzer(Selector,
                               'jets_20_unclean',
                               output = 'jets_20_unclean',
                               src = 'jets',
                               filter_func = select_jets_pteta)

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

two_jets = cfg.Analyzer(EventFilter, 
                        name = 'TwoJets',
                        src = 'jets_20_clean',
#                        src = 'jets_30',
                        filter_func = lambda x : len(x)>1)
jets_30 = cfg.Analyzer(Selector,
                       'jets_30',
                       output = 'jets_30',
                       src = 'jets_20_clean',
                       filter_func = lambda x : x.pt()>30)


btag = cfg.Analyzer(BJetEfficiencyCreator,
                    name='BJetEfficiencyCreator',
                    jets = 'jets_30', 
                    year = year, 
                    tagger = btagger)


sequence = cfg.Sequence([
# Analyzers
    json,
    vertex,
    muons, 
    select_muon,
    one_muon,
    electrons, 
    select_electron,
    one_electron,
    dilepton,
    select_dilepton,
    only_one_dilepton,
    dilepton_sorted,
    jets,
    jets_20_unclean,
    jet_20_electron_clean,
    jet_20_clean,
    two_jets,
    jets_30,
    btag
])


# the following is declared in case this cfg is used in input to the
# heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config(components=selectedComponents,
                    sequence=sequence,
                    services=[],
                    events_class=Events)

printComps(config.components, True)

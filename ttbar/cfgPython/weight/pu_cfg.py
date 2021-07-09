import PhysicsTools.HeppyCore.framework.config     as cfg
from   PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
from   PhysicsTools.HeppyCore.framework.config     import printComps
from   CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

test       = getHeppyOption('test', False)
alternate  = getHeppyOption('alternate', True)
year       = getHeppyOption('year', '2016' )


ComponentCreator.useAAA = True
#ComponentCreator.useLyonAAA = True


################################################################################
# Components
################################################################################

if (year == '2016'):
    from CMGTools.ttbar.samples.summer16.ttbar2016              import mc_ttbar
    from CMGTools.ttbar.samples.summer16.ttbar_alternative_2016 import alt_ttbar
elif(year == '2017'):
    from CMGTools.ttbar.samples.fall17.ttbar2017              import mc_ttbar
    from CMGTools.ttbar.samples.fall17.ttbar_alternative_2017 import alt_ttbar


events_to_pick = []

if not alternate:
    selectedComponents = mc_ttbar
else:
    selectedComponents = alt_ttbar

################################################################################
# Test
################################################################################
if(year == '2016'):    
    if not alternate:
        import CMGTools.TTbarTime.proto.samples.summer16.ttbar2016 as backgrounds_forindex
    else:
        import CMGTools.ttbar.samples.summer16.ttbar_alternative_2016 as backgrounds_forindex
elif(year == '2017'):
    if not alternate:
        import CMGTools.ttbar.samples.fall17.ttbar2017 as backgrounds_forindex    
    else:
        import CMGTools.ttbar.samples.fall17.ttbar_alternative_2017 as backgrounds_forindex    

from CMGTools.ttbar.samples.component_index import ComponentIndex
bindex = ComponentIndex(backgrounds_forindex)

if test:
    cache = True
    comp = bindex.glob('alt_MC_hdampUp')[0]
    #'signal_MC_dilep'
    #'alt_MC_hdampUp'
    selectedComponents = [comp]
    comp.files = [comp.files[0]]
    comp.splitFactor = 1
    comp.fineSplitFactor = 1

################################################################################
# Core
################################################################################

from CMGTools.ttbar.analyzers.PileUpPrecalculator import PileUpPrecalculator

pu = cfg.Analyzer(PileUpPrecalculator,
                    name='PileUpPrecalculator')


from CMGTools.ttbar.ntuple.NtupleProducer import NtupleProducer
from CMGTools.ttbar.ntuple.NtupleCreator  import pileup

ntuple = cfg.Analyzer(NtupleProducer,
                      name = 'NtupleProducer',
                      outputfile = 'events.root',
                      treename = 'events',
                      event_content = pileup)


sequence = cfg.Sequence([
    pu,
    ntuple
])


# the following is declared in case this cfg is used in input to the
# heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config(components=selectedComponents,
                    sequence=sequence,
                    services=[],
                    events_class=Events)

printComps(config.components, True)


#import os
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
#from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
#from PhysicsTools.HeppyCore.statistics.average import Average
#import PhysicsTools.HeppyCore.framework.config as cfg

#import FWCore.ParameterSet.Config as cms
#process_cms = cms.Process('LumiPerEvent')

class TimeAnalyzer( Analyzer ):
                                                         
    def process(self, event):
    
#        lumi_file = '$CMSSW_BASE/src/CMGTools/TTbarTime/data/2017/LumiData_2017.csv'
        
        
#        process_cms.LumiInfo = cms.EDProducer('LumiProducerFromBrilcalc',
#                                          lumiFile = cms.string(lumi_file),
#                                          throwIfNotFound = cms.bool(False),
#                                          doBunchByBunch = cms.bool(False))

#        process_cms.test = cms.EDAnalyzer('LumiPerEvent',
#                                      inputTag = cms.untracked.InputTag("LumiInfo", "brilcalc"))
    
#        process_cms.p = cms.Path(process_cms.LumiInfo*process_cms.test)    
    
    
        self.readCollections(event.input)      
       
        time = event.input.eventAuxiliary().time()
        unix_time = time.unixTime()
#        unix_time = time.timeLow()
#        import pdb; pdb.set_trace()       
        
        
        setattr(event, 'unixTime', unix_time)

        if event.unixTime is None:
            raise ValueError('time cannot be None!')
        


from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from CMGTools.ttbar.analyzers.BTagSF import BTagSF

class BJetAnalyzer(Analyzer):
        
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(BJetAnalyzer, self).__init__(cfg_ana, cfg_comp, looperName)
        self.btagSF = BTagSF(0, wp='loose', year = self.cfg_ana.year, tagger = self.cfg_ana.tagger)

    def process(self, event):
        '''Adds the is_btagged attribute to the jets of the
        given jets collection.
        '''
        #https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
        #https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation2016Legacy


        sfb_weight = 1.
        sfb_weightup = 1.
        sfb_weightdown = 1.
        sfc_weight = 1.
        sfc_weightup = 1.
        sfc_weightdown = 1.
        sfl_weight = 1.
        sfl_weightup = 1.
        sfl_weightdown = 1.
        
        jets = getattr(event, self.cfg_ana.jets)
        for jet in jets:
            if self.cfg_ana.year == '2016': 
                if self.cfg_ana.tagger == 'DeepCSV' :
                    csv     = jet.btag("pfDeepCSVJetTags:probb") + jet.btag("pfDeepCSVJetTags:probbb")
                    csv_cut = 0.2217
                if self.cfg_ana.tagger == 'DeepJet' :
                    csv     = jet.btag("pfDeepFlavourJetTags:probb") +  jet.btag("pfDeepFlavourJetTags:probbb") +  jet.btag("pfDeepFlavourJetTags:problepb")
                    csv_cut = 0.0614
                if self.cfg_ana.tagger == 'CSVv2' :
                    csv     = jet.btag("pfCombinedInclusiveSecondaryVertexV2BJetTags")
                    csv_cut = 0.5803 #assumption to keep it same as 2017, no SFs are actually provided for CSVv2 in 2016.
            else: 
                if self.cfg_ana.tagger == 'DeepCSV' :
                    csv     = jet.btag("pfDeepCSVJetTags:probb") + jet.btag("pfDeepCSVJetTags:probbb")
                    csv_cut = 0.1522
                if self.cfg_ana.tagger == 'DeepJet' :
                    csv     = jet.btag("pfDeepFlavourJetTags:probb") +  jet.btag("pfDeepFlavourJetTags:probbb") +  jet.btag("pfDeepFlavourJetTags:problepb")
                    csv_cut = 0.0521 #not sure if this will work on 2017 as the twiki says one needs to run recipe to obtain this on MiniAOD.
                if self.cfg_ana.tagger == 'CSVv2' :
                    csv     = jet.btag("pfCombinedInclusiveSecondaryVertexV2BJetTags")
                    csv_cut = 0.5803 
          
            jet.is_btagged = self.btagSF.isBTagged(jet, pt=jet.pt(),
                                                   eta =jet.eta(),
                                                   csv = csv,
                                                   jetflavor=abs(jet.hadronFlavour()),
                                                   is_data=not self.cfg_comp.isMC,
                                                   csv_cut=csv_cut)
 
            sf_weight *= jet.btagWeight
            if(jet.btagWeight > 0 and abs(jet.hadronFlavour()) in [4, 5]):
                sfb_weightup *= jet.btagWeightUp
                sfb_weightdown *= jet.btagWeightDown
                sfl_weightup *= jet.btagWeight
                sfl_weightdown *= jet.btagWeight
            else:    
                sfb_weightup *= jet.btagWeight
                sfb_weightdown *= jet.btagWeight
                sfl_weightup *= jet.btagWeightUp
                sfl_weightdown *= jet.btagWeightDown

            
        setattr(event, 'sfWeight', sf_weight)
        setattr(event, 'sfbWeightUp', sfb_weightup)
        setattr(event, 'sfbWeightDown', sfb_weightdown)
        setattr(event, 'sflWeightUp', sfl_weightup)
        setattr(event, 'sflWeightDown', sfl_weightdown)

        event.eventWeight *= event.sfWeight
            
                                                   

# CSVv2 "pfCombinedInclusiveSecondaryVertexV2BJetTags"  loose : 0.5803 
# DeepCSV "pfDeepCSVJetTags:probb + pfDeepCSVJetTags:probbb" loose : 0.1522 


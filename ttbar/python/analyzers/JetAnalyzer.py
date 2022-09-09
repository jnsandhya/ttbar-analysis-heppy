from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.Jet import Jet
from PhysicsTools.HeppyCore.utils.deltar import deltaR2, deltaPhi, matchObjectCollection, matchObjectCollection2, bestMatch,matchObjectCollection3

from CMGTools.ttbar.utils.JesEnergyScaleSources import fulljesunc_sources_2016
from CMGTools.ttbar.utils.JesEnergyScaleSources import fulljesunc_sources_2017
from CMGTools.ttbar.utils.JesEnergyScaleSources import redjesunc_sources_2016
from CMGTools.ttbar.utils.JesEnergyScaleSources import redjesunc_sources_2017
import os 
import ROOT
import math

def shiftJERfactor(JERShift, aeta, year):
#def shiftJERfactor(JERShift, aeta):
    # Summer16_25nsV1 (80X, 2016, BCDEFGH, 07Aug ReReco) DATA/MC SFs
    if year == '2016' :
        factor = 1.1595 + JERShift * 0.0645
        if   aeta > 3.139: factor = 1.1922 + JERShift * 0.1488
        elif aeta > 2.964: factor = 1.1869 + JERShift * 0.1243
        elif aeta > 2.853: factor = 1.7788 + JERShift * 0.2008
        elif aeta > 2.5:   factor = 1.3418 + JERShift * 0.2091
        elif aeta > 2.322: factor = 1.2963 + JERShift * 0.2371
        elif aeta > 2.043: factor = 1.1512 + JERShift * 0.1140
        elif aeta > 1.930: factor = 1.1426 + JERShift * 0.1214
        elif aeta > 1.740: factor = 1.1000 + JERShift * 0.1079
        elif aeta > 1.305: factor = 1.1278 + JERShift * 0.0986
        elif aeta > 1.131: factor = 1.1609 + JERShift * 0.1025
        elif aeta > 0.783: factor = 1.1464 + JERShift * 0.0632
        elif aeta > 0.522: factor = 1.1948 + JERShift * 0.0652
        return factor
    if year == '2017' :
        factor = 1.1432 + JERShift * 0.0222
        if   aeta > 3.139: factor = 1.1542 + JERShift * 0.1524
        elif aeta > 2.964: factor = 1.2696 + JERShift * 0.1089
        elif aeta > 2.853: factor = 2.2923 + JERShift * 0.3743
        elif aeta > 2.5:   factor = 1.9909 + JERShift * 0.5684
        elif aeta > 2.322: factor = 1.4085 + JERShift * 0.2020
        elif aeta > 2.043: factor = 1.2604 + JERShift * 0.1501
        elif aeta > 1.930: factor = 1.2393 + JERShift * 0.1909
        elif aeta > 1.740: factor = 1.1600 + JERShift * 0.0976
        elif aeta > 1.305: factor = 1.1307 + JERShift * 0.1470
        elif aeta > 1.131: factor = 1.1137 + JERShift * 0.1397
        elif aeta > 0.783: factor = 1.0989 + JERShift * 0.0456
        elif aeta > 0.522: factor = 1.1815 + JERShift * 0.0484
        return factor


def is_between(a, x, b):
    return min(a, b) < x < max(a, b)

def getResolution(jer, pt, eta, rho ) : 
    lines = []
    count = 0
    with open(jer, 'r') as f:
        lines = list(f)
        #print(str(count)+' '+str(lines))
        count += 1
    
    count = 0
    resolution = 0. 
    for line in lines:
        linespl = line.split(" ")
        cllines = [x for x in linespl if x]
        if(count):
            for i,n in enumerate(cllines):
                cllines[i] = n.strip()
                cllines[i] = float(cllines[i])
            #print cllines
            if(is_between(cllines[0],eta,cllines[1]) and is_between(cllines[2],rho,cllines[3])): 
                #print(eta)
                #print('line '+ str(count) + ': '+ line)
                # and is_between(float(cllines[2]),rho,float(cllines[3]))):
                #    print(str(count)+ ' '+'eta'+ ' '+cllines[0]+' '+cllines[1])
                #    print(str(count)+ ' '+'rho'+ ' '+cllines[2]+' '+cllines[3])
                #print(str(count)+ ' '+'pt' + ' '+cllines[5]+' '+cllines[6]+ ' '+ pt)

               # print("resolution:", math.sqrt(cllines[7]*abs(cllines[7])/(pt*pt)+cllines[8]*cllines[8]*pow(pt,cllines[10])+cllines[9]*cllines[9]))
                resolution = math.sqrt(cllines[7]*abs(cllines[7])/(pt*pt)+cllines[8]*cllines[8]*pow(pt,cllines[10])+cllines[9]*cllines[9])
        count +=1
    return resolution    


class JetAnalyzer(Analyzer):

    def beginLoop(self, setup):
        super(JetAnalyzer, self).beginLoop(setup)
        if self.cfg_ana.do_jec: 
            global_tag = self.cfg_ana.gt_mc 
            if not self.cfg_comp.isMC:
                global_tag = self.cfg_comp.dataGT

            do_residual = not self.cfg_comp.isMC
            self.matchJetsWithThreshold = getattr(self.cfg_ana, 'matchJetsWithThreshold', False)
            
            from CMGTools.ttbar.analyzers.JetReCalibrator import JetReCalibrator
            if self.cfg_ana.year == '2016' :
                if self.cfg_comp.isMC:
                    if self.cfg_ana.redsetJEC:
                        jesunc_sources = redjesunc_sources_2016
                    else:
                        jesunc_sources = fulljesunc_sources_2016

                    self.jet_calibrator = JetReCalibrator(
                        global_tag, 'AK4PFchs', do_residual, self.cfg_ana.redsetJEC,
                        jecPath=os.path.expandvars(
                            "${CMSSW_BASE}/src/CMGTools/RootTools/data/jec"
                            ),
                        #upToLevel=3,
                        #calculateSeparateCorrections=True,
                        calculateType1METCorrection=True,
                        groupForUncertaintySources = jesunc_sources
                        )
                else:
                    self.jet_calibrator = JetReCalibrator(
                        global_tag, 'AK4PFchs', do_residual, self.cfg_ana.redsetJEC,
                        jecPath=os.path.expandvars(
                            "${CMSSW_BASE}/src/CMGTools/RootTools/data/jec"
                            ),
                        #upToLevel=3,
                        #calculateSeparateCorrections=True,
                        calculateType1METCorrection=True,
                        )
            else:
                if self.cfg_comp.isMC:
                    if self.cfg_ana.redsetJEC:
                        jesunc_sources = redjesunc_sources_2017
                    else:
                        jesunc_sources = fulljesunc_sources_2017

                    self.jet_calibrator = JetReCalibrator(
                        global_tag, 'AK4PFchs', do_residual, self.cfg_ana.redsetJEC,
                        jecPath=os.path.expandvars(
                            "${CMSSW_BASE}/src/CMGTools/RootTools/data/jec"
                        ),
                        #upToLevel=3,
                        #calculateSeparateCorrections=True,
                        calculateType1METCorrection=True,
                        groupForUncertaintySources = jesunc_sources
                        )
                else:
                    self.jet_calibrator = JetReCalibrator(
                        global_tag, 'AK4PFchs', do_residual, self.cfg_ana.redsetJEC,
                        jecPath=os.path.expandvars(
                            "${CMSSW_BASE}/src/CMGTools/RootTools/data/jec"
                        ),
                        #upToLevel=3,
                        #calculateSeparateCorrections=True,
                        calculateType1METCorrection=True
                        )

        self.counters.addCounter('JetAnalyzer')
        count = self.counters.counter('JetAnalyzer')
        count.register('all events')
        count.register('at least 2 good jets')
        count.register('at least 2 clean jets')
 
    def declareHandles(self):
        super(JetAnalyzer, self).declareHandles()

        self.handles['jets'] = AutoHandle(
            self.cfg_ana.jets,
            'std::vector<pat::Jet>'
        )
        self.handles['genJet'] = AutoHandle( 
            self.cfg_ana.genJetCol, 
            'std::vector<reco::GenJet>'
        )
        self.handles['rho'] = AutoHandle( 
            self.cfg_ana.rho, 
            'double' 
        )

        self.shiftJER = self.cfg_ana.shiftJER if hasattr(self.cfg_ana, 'shiftJER') else 0
        self.addJERShifts = self.cfg_ana.addJERShifts if hasattr(self.cfg_ana, 'addJERShifts') else 0
        self.jer = self.cfg_ana.jer 
        #self.params_resolution = ROOT.PyJetParametersWrapper()

    def process(self, event):
        self.readCollections(event.input)
        jets = self.handles['jets'].product()
        output_jets = []
        if self.cfg_ana.year == '2016' :
            for jet in jets:
                hjet = Jet(jet)
		if hjet.jetID("POG_PFID_TightLepVeto2016")==True:
                    output_jets.append(hjet)
        else:    
            for jet in jets:
                hjet = Jet(jet)
                if not hasattr(self.cfg_ana,'selection'):
                    continue
                elif self.cfg_ana.selection(hjet):
		    if hjet.jetID("POG_PFID_TightLepVeto")==True:
                        output_jets.append(hjet)

        if self.cfg_ana.do_jec:
            event.metShift = [0., 0.]
            event.type1METCorr = [0.,0.,0.]
            try:
                self.jet_calibrator.correctAll(output_jets, event.rho, delta=0.,
                                           addCorr=True, addShifts=True, 
                                           metShift=event.metShift,
                                           type1METCorr=event.type1METCorr)
            except:
                pass
            
        if self.cfg_comp.isMC:
            rho  = float(self.handles['rho'].product()[0])
            self.genJets = [ x for x in self.handles['genJet'].product() ]
            if self.cfg_ana.do_mc_match:
                for igj, gj in enumerate(self.genJets):
                    gj.index = igj
                #self.matchJets(event, allJets)
                if self.matchJetsWithThreshold and not getattr(self.cfg_ana, 'smearJets', False):
                    for j in output_jets: 
                        jet.res = getResolution(self.jer,jet.pt(), jet.eta(), rho)
                    self.matchJets(event, [ j for j in output_jets if abs(igj.pt - j.pt()) < 3*j.pt()*j.res ]) # To match only jets above chosen threshold
                else:
                    self.matchJets(event, output_jets)
            if getattr(self.cfg_ana, 'smearJets', False):
                self.smearJets(event, output_jets, self.cfg_ana.year, rho)
                           
        output_jets.sort(key = lambda j : j.pt(), reverse = True)

        setattr(event, self.cfg_ana.output, output_jets)
        
        
    def matchJets(self, event, jets):
        
        match = matchObjectCollection2(jets,
                                       self.genJets,
                                       deltaRMax = 0.2)
        for jet in jets:
            jet.mcJet = match[jet]

   
    def smearJets(self, event, jets, year, rho):
         # https://twiki.cern.ch/twiki/bin/viewauth/CMS/TWikiTopRefSyst#Jet_energy_resolution
         for jet in jets:
            gen = jet.mcJet 
            if gen != None:
               genpt, jetpt, aeta = gen.pt(), jet.pt(), abs(jet.eta())
               # from https://twiki.cern.ch/twiki/bin/view/CMS/JetResolution
               factor = shiftJERfactor(self.shiftJER, aeta, year)
               dPt = jetpt-genpt
               ptscale = max(0.0, 1 + (factor-1.)*dPt/jetpt)             
               if ptscale != 0:
                  jet.setP4(jet.p4()*ptscale)
                  # leave the uncorrected unchanged for sync
                  jet.setRawFactor(jet.rawFactor()/ptscale)
               if (self.shiftJER==0) and (self.addJERShifts):
                   setattr(jet, "corrJER", ptscale)
                   factorJERUp = shiftJERfactor(1, aeta, year)
                   ptscaleJERUp = max(0.0, 1 + (factorJERUp-1.)*dPt/jetpt)
                   setattr(jet, "corrJERUp", ptscaleJERUp)
                   factorJERDown= shiftJERfactor(-1, aeta, year)
                   ptscaleJERDown = max(0.0, 1 + (factorJERDown-1.)*dPt/jetpt)
                   setattr(jet, "corrJERDown", ptscaleJERDown)
                   #print "jet with pt %.2f, eta %.2f has ptscale %.2f, %.2f up corr, %.2f down corr" % (jet.pt(), jet.eta(), ptscale, ptscaleJERUp, ptscaleJERDown)
            else:
		aeta = abs(jet.eta())
                #print "jet with pt %.2f, eta %.2f is unmatched" % (jet.pt(), jet.eta())
                factor = shiftJERfactor(self.shiftJER, aeta, year)
                if factor > 1. : 
                    #print "jet with pt %.2f, eta %.2f is unmatched and SF > 1." % (jet.pt(), jet.eta())
                    res = getResolution(self.jer,jet.pt(), jet.eta(), rho)  
                    rnd = ROOT.TRandom3(12345)
                    rand = rnd.Gaus(0, res)  
                    ptscale = max(0.0, (1 + rand*math.sqrt(factor**2-1.)))
                    if ptscale != 0:
                        jet.setP4(jet.p4()*ptscale)
                        jet.setRawFactor(jet.rawFactor()/ptscale)
                    if (self.shiftJER==0) and (self.addJERShifts):
                        setattr(jet, "corrJER", ptscale)
                        factorJERUp = shiftJERfactor(1, aeta, year)
                        ptscaleJERUp = 1.
                        if factorJERUp**2 > 1:  
                            ptscaleJERUp = max(0.0, (1 + rand*math.sqrt(factorJERUp**2-1.)))
                         
                        setattr(jet, "corrJERUp", ptscaleJERUp)
                        factorJERDown= shiftJERfactor(-1, aeta, year)
                        ptscaleJERDown = 1.
                        if factorJERDown**2 > 1:  
                            ptscaleJERDown = max(0.0, (1 + rand*math.sqrt(factorJERDown**2-1.)))
                        setattr(jet, "corrJERDown", ptscaleJERDown)
                        #print "unmatched jet with pt %.2f, eta %.2f has ptscale %.2f, %.2f up corr, %.2f down corr" % (jet.pt(), jet.eta(), ptscale, ptscaleJERUp, ptscaleJERDown)
                else : print("Impossible to smear this jet")
        
        

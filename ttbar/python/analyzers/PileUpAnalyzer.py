import os
from PhysicsTools.Heppy.analyzers.core.VertexHistograms import VertexHistograms
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.statistics.average import Average
from PhysicsTools.Heppy.physicsutils.PileUpSummaryInfo import PileUpSummaryInfo
import PhysicsTools.HeppyCore.framework.config as cfg

from ROOT import TFile, TH1F, gPad

class PileUpAnalyzer( Analyzer ):
    '''Computes pile-up weights for MC from the pile up histograms for MC and data.
    These histograms should be set on the components as
    puFileData, puFileMC attributes, as is done here:

    http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/CMG/CMGTools/H2TauTau/Colin/test_tauMu_2012_cfg.py?view=markup

    THESE HISTOGRAMS MUST BE CONSISTENT, SEE
    https://twiki.cern.ch/twiki/bin/view/CMS/CMGToolsPileUpReweighting#Generating_pile_up_distributions

    If the component is not MC, or if the puFileData and puFileMC are not
    set for the component, the reweighting is not done.

    The analyzer sets event.vertexWeight.
    This weight is multiplied to the global event weight, event.eventWeight.
    When using this analyzer, make sure that the VertexAnalyzer is disabled,
    as you would be reweighting the MC PU distribution twice!

    Additionally, this analyzer writes in the output an histogram containing the unweighting MC
    pile-up distribution, to be used in input of the weighting for a later pass.

    Example of use:

    puAna = cfg.Analyzer(
      "PileUpAnalyzer",
      # build unweighted pu distribution using number of pile up interactions if False
      # otherwise, use fill the distribution using number of true interactions
      true = True
      )
    '''

    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(PileUpAnalyzer, self).__init__(cfg_ana, cfg_comp, looperName)
        self.datafile = TFile( self.cfg_comp.puFileData )
        self.datafile_up   = TFile(self.cfg_ana.puFileDataUp)
        self.datafile_down = TFile(self.cfg_ana.puFileDataDown)
        
        self.datahist = self.datafile.Get('pileup')
        self.datahist_up = self.datafile_up.Get('pileup')
        self.datahist_down = self.datafile_down.Get('pileup')

                
        self.datafiles_pu_time      = []
        self.datafiles_pu_time_up   = []
        self.datafiles_pu_time_down = []
        self.datahists_pu_time      = []
        self.datahists_pu_time_up   = []
        self.datahists_pu_time_down = []

        self.fname_inc = 'src/CMGTools/ttbar/data/'+str(self.cfg_ana.year)+'/pu_timebins/MyDataPileupHistogram_'+str(self.cfg_ana.year)+'_inc.root'
        self.fname_inc_up = 'src/CMGTools/ttbar/data/'+str(self.cfg_ana.year)+'/pu_timebins/MyDataPileupHistogram_'+str(self.cfg_ana.year)+'_inc_up.root'
        self.fname_inc_down = 'src/CMGTools/ttbar/data/'+str(self.cfg_ana.year)+'/pu_timebins/MyDataPileupHistogram_'+str(self.cfg_ana.year)+'_inc_down.root'
        
        self.fname_inc = TFile('/'.join([os.environ["CMSSW_BASE"],self.fname_inc]))
        self.fname_inc_up = TFile('/'.join([os.environ["CMSSW_BASE"],self.fname_inc_up]))
        self.fname_inc_down = TFile('/'.join([os.environ["CMSSW_BASE"],self.fname_inc_down]))
        
        self.datahists_pu_time_inc      = self.fname_inc.Get('pileup')
        self.datahists_pu_time_inc_up   = self.fname_inc_up.Get('pileup')
        self.datahists_pu_time_inc_down = self.fname_inc_down.Get('pileup')


        self.fname_new = 'src/CMGTools/ttbar/data/'+str(self.cfg_ana.year)+'/pu_timebins/MyDataPileupHistogram_'+str(self.cfg_ana.year)+'.root'
        self.fname_new_up = 'src/CMGTools/ttbar/data/'+str(self.cfg_ana.year)+'/pu_timebins/MyDataPileupHistogram_'+str(self.cfg_ana.year)+'_up.root'
        self.fname_new_down = 'src/CMGTools/ttbar/data/'+str(self.cfg_ana.year)+'/pu_timebins/MyDataPileupHistogram_'+str(self.cfg_ana.year)+'_down.root'
        
        self.fname_new = TFile('/'.join([os.environ["CMSSW_BASE"],self.fname_new]))
        self.fname_new_up = TFile('/'.join([os.environ["CMSSW_BASE"],self.fname_new_up]))
        self.fname_new_down = TFile('/'.join([os.environ["CMSSW_BASE"],self.fname_new_down]))
        
        self.datahist_new      = self.fname_inc.Get('pileup')
        self.datahist_new_up   = self.fname_inc_up.Get('pileup')
        self.datahist_new_down = self.fname_inc_down.Get('pileup')
        
        for i in range(24):
            fname      = 'src/CMGTools/ttbar/data/'+str(self.cfg_ana.year)+'/pu_timebins/MyDataPileupHistogram_'+str(self.cfg_ana.year)+'_'+str(i)+'.root'
            fname_up   = 'src/CMGTools/ttbar/data/'+str(self.cfg_ana.year)+'/pu_timebins/MyDataPileupHistogram_'+str(self.cfg_ana.year)+'_'+str(i)+'_up.root'
            fname_down = 'src/CMGTools/ttbar/data/'+str(self.cfg_ana.year)+'/pu_timebins/MyDataPileupHistogram_'+str(self.cfg_ana.year)+'_'+str(i)+'_down.root'
            fname = TFile('/'.join([os.environ["CMSSW_BASE"],fname]))
            fname_up = TFile('/'.join([os.environ["CMSSW_BASE"],fname_up]))
            fname_down = TFile('/'.join([os.environ["CMSSW_BASE"],fname_down]))
            self.datafiles_pu_time.append(fname)
            self.datafiles_pu_time_up.append(fname_up)
            self.datafiles_pu_time_down.append(fname_down)
            
            self.datahists_pu_time.append(self.datafiles_pu_time[i].Get('pileup'))
            self.datahists_pu_time_up.append(self.datafiles_pu_time_up[i].Get('pileup'))
            self.datahists_pu_time_down.append(self.datafiles_pu_time_down[i].Get('pileup'))

        self.doHists=True
        self.currentFile = None

        if (hasattr(self.cfg_ana,'makeHists')) and (not self.cfg_ana.makeHists):
            self.doHists=False

        self.allVertices = self.cfg_ana.allVertices if (hasattr(self.cfg_ana,'allVertices')) else "_AUTO_"

        self.autoPU = getattr(self.cfg_ana, 'autoPU', False)

        if self.cfg_comp.isMC and self.doHists:
            self.rawmcpileup = VertexHistograms('/'.join([self.dirName,
                                                          'rawMCPU.root']))
        self.enable = True
        ## if component is embed return (has no trigger obj)
        if self.cfg_comp.isEmbed :
          self.cfg_comp.puFileMC   = None
          self.cfg_comp.puFileData = None

        self.setupInputs()


    def setupInputs(self, event=None):
        if self.cfg_comp.isMC or self.cfg_comp.isEmbed:
            if not hasattr(self.cfg_comp,"puFileMC") or (self.cfg_comp.puFileMC is None and self.cfg_comp.puFileData is None):
                self.enable = False
            else:
                assert( os.path.isfile(os.path.expandvars(self.cfg_comp.puFileData)) )
                #self.datafile = TFile( self.cfg_comp.puFileData )
                #self.datahist = self.datafile.Get('pileup')
                #self.datahist_up = self.datafile_up.Get('pileup')
                #self.datahist_down = self.datafile_down.Get('pileup')
                self.datahist.Scale( 1 / self.datahist.Integral() )
                self.datahist_up.Scale( 1 / self.datahist_up.Integral() )
                self.datahist_down.Scale( 1 / self.datahist_down.Integral() )

                self.datahist_new.Scale( 1 / self.datahist_new.Integral() )
                self.datahist_new_up.Scale( 1 / self.datahist_new_up.Integral() )
                self.datahist_new_down.Scale( 1 / self.datahist_new_down.Integral() )
                
                self.datahists_pu_time_inc.Scale(1/self.datahists_pu_time_inc.Integral() )
                self.datahists_pu_time_inc_up.Scale(1/self.datahists_pu_time_inc_up.Integral() )
                self.datahists_pu_time_inc_down.Scale(1/self.datahists_pu_time_inc_down.Integral() )
                
                for i in range(24):
                    self.datahists_pu_time[i].Scale(1/self.datahists_pu_time[i].Integral() )
                    self.datahists_pu_time_up[i].Scale(1/self.datahists_pu_time_up[i].Integral() )
                    self.datahists_pu_time_down[i].Scale(1/self.datahists_pu_time_down[i].Integral() )
                        

                if not self.autoPU:
                    assert( os.path.isfile(os.path.expandvars(self.cfg_comp.puFileMC)) )

                    self.mcfile = TFile( self.cfg_comp.puFileMC )
                    self.mchist = self.mcfile.Get('pileup')
                    if self.mchist == None: # and not is None!!
                        # trying the file structure of Artur. 
                        # the distribution for each dataset is stored in the root file with a key like: 
                        # #SUSYGluGluToHToTauTau_M-3200_TuneCP5_13TeV-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM
                        key = self.cfg_comp.dataset.replace("/","#")
                        self.mchist = self.mcfile.Get(key)
                        if self.mchist == None: 
                            raise ValueError('no pile up distribution for dataset {} in file {}'.format(
                                    self.cfg_comp.dataset,
                                    self.mcfile.GetName()
                                    ))
                    self.mchist.Scale( 1 / self.mchist.Integral(0, self.mchist.GetNbinsX() + 1) )
                    if self.mchist.GetNbinsX() != self.datahist.GetNbinsX():
                        raise ValueError('data and mc histograms must have the same number of bins')
                    if self.mchist.GetXaxis().GetXmin() != self.datahist.GetXaxis().GetXmin():
                        raise ValueError('data and mc histograms must have the same xmin')
                    if self.mchist.GetXaxis().GetXmax() != self.datahist.GetXaxis().GetXmax():
                        raise ValueError('data and mc histograms must have the same xmax')


    def setupEventInputs(self, event=None):
        if self.cfg_comp.isMC or self.cfg_comp.isEmbed:
            if not hasattr(self.cfg_comp,"puFileMC") or (self.cfg_comp.puFileMC is None and self.cfg_comp.puFileData is None):
                self.enable = False
            else:
                self.datafile.cd()
                self.mchist = self.datahist.Clone('pileup_MC')
                self.mchist.Reset()
                self.currentFile = event.input.events.object().getTFile().GetName()
                event.input.events.object().getTFile().Get("Events").Draw("slimmedAddPileupInfo.getTrueNumInteractions()>>pileup_MC", "slimmedAddPileupInfo.getBunchCrossing()==0")
                self.mchist = gPad.GetPrimitive("pileup_MC").Clone() # It's the only method that I get to work
                self.mchist.Scale( 1 / self.mchist.Integral(0, self.mchist.GetNbinsX() + 1) )


    def declareHandles(self):
        super(PileUpAnalyzer, self).declareHandles()
        self.mchandles['pusi'] =  AutoHandle(
            'slimmedAddPileupInfo',
            'std::vector<PileupSummaryInfo>',
            fallbackLabel="addPileupInfo"
            )

        if self.allVertices == '_AUTO_':
            self.handles['vertices'] =  AutoHandle( "offlineSlimmedPrimaryVertices", 'std::vector<reco::Vertex>', fallbackLabel="offlinePrimaryVertices" )
        else:
            self.handles['vertices'] =  AutoHandle( self.allVertices, 'std::vector<reco::Vertex>' )

    def beginLoop(self, setup):
        super(PileUpAnalyzer,self).beginLoop(setup)
        self.averages.add('puWeight', Average('puWeight') )


    def process(self, event):
        self.readCollections( event.input )
        if self.autoPU and self.currentFile != event.input.events.object().getTFile().GetName():
            self.setupEventInputs(event)

        ## if component is embed return (has no trigger obj)
        if self.cfg_comp.isEmbed :
          return True

        event.puWeight = 1
        event.puWeightUp = 1
        event.puWeightDown = 1

        event.puWeightNew = 1
        event.puWeightNewUp = 1
        event.puWeightNewDown = 1

        event.puWeightInc = 1
        event.puWeightIncUp = 1
        event.puWeightIncDown = 1


        event.puWeightTime = []
        event.puWeightTimeUp = []
        event.puWeightTimeDown = []
        for i in range(24):
            event.puWeightTime.append(1)
            event.puWeightTimeUp.append(1)
            event.puWeightTimeDown.append(1)
            
        event.nPU = None
        event.pileUpVertex_z = []
        event.pileUpVertex_ptHat = []
        if self.cfg_comp.isMC:
            event.pileUpInfo = map( PileUpSummaryInfo,
                                    self.mchandles['pusi'].product() )
            for puInfo in event.pileUpInfo:
                if puInfo.getBunchCrossing()==0:
                    # import pdb; pdb.set_trace()
                    if self.cfg_ana.true is False:
                        event.nPU = puInfo.nPU()
                    else:
                        event.nPU = puInfo.nTrueInteractions()

                    if self.doHists:
                        self.rawmcpileup.hist.Fill( event.nPU )

                    ##get z position of on-time pile-up sorted by pt-hat
                    ptHat_zPositions = zip(puInfo.getPU_pT_hats(),puInfo.getPU_zpositions())
                    ptHat_zPositions.sort(reverse=True)
                    for ptHat_zPosition in ptHat_zPositions:
                        event.pileUpVertex_z.append(ptHat_zPosition[1])
                        event.pileUpVertex_ptHat.append(ptHat_zPosition[0])

            if event.nPU is None:
                raise ValueError('nPU cannot be None! means that no pu info has been found for bunch crossing 0.')
        elif self.cfg_comp.isEmbed:
            vertices = self.handles['vertices'].product()
            event.nPU = len(vertices)
        else:
            return True

        if self.enable:
            bin = self.datahist.FindBin(event.nPU)
            if bin<1 or bin>self.datahist.GetNbinsX():
                event.puWeight = 0
                event.puWeightUp = 0
                event.puWeightDown = 0
            else:
                data      = self.datahist.GetBinContent(bin)
                mc        = self.mchist.GetBinContent(bin)

                data_up   = self.datahist_up.GetBinContent(bin)
                data_down = self.datahist_down.GetBinContent(bin)
                #Protect 0 division!!!!
                if mc !=0.0:
                    event.puWeight     = data/mc
                    event.puWeightUp   = data_up/mc
                    event.puWeightDown = data_down/mc
                else:
                    event.puWeight = 1
                    event.puWeightUp = 1
                    event.puWeightDown = 1

            bin = self.datahist_new.FindBin(event.nPU)
            if bin<1 or bin>self.datahist_new.GetNbinsX():
                event.puWeightNew = 0
                event.puWeightNewUp = 0
                event.puWeightNewDown = 0
            else:
                data      = self.datahist_new.GetBinContent(bin)
                mc        = self.mchist.GetBinContent(bin)

                data_up   = self.datahist_new_up.GetBinContent(bin)
                data_down = self.datahist_new_down.GetBinContent(bin)
                #Protect 0 division!!!!
                if mc !=0.0:
                    event.puWeightNew     = data/mc
                    event.puWeightNewUp   = data_up/mc
                    event.puWeightNewDown = data_down/mc
                else:
                    event.puWeightNew = 1
                    event.puWeightNewUp = 1
                    event.puWeightNewDown = 1

            bin = self.datahists_pu_time_inc.FindBin(event.nPU)
            if bin<1 or bin>self.datahists_pu_time_inc.GetNbinsX():
                event.puWeightInc = 0
                event.puWeightIncUp = 0
                event.puWeightIncDown = 0
            else:
                data      = self.datahists_pu_time_inc.GetBinContent(bin)
                mc        = self.mchist.GetBinContent(bin)

                data_up   = self.datahists_pu_time_inc_up.GetBinContent(bin)
                data_down = self.datahists_pu_time_inc_down.GetBinContent(bin)
                #Protect 0 division!!!!
                if mc !=0.0:
                    event.puWeightInc     = data/mc
                    event.puWeightIncUp   = data_up/mc
                    event.puWeightIncDown = data_down/mc
                else:
                    event.puWeightInc = 1
                    event.puWeightIncUp = 1
                    event.puWeightIncDown = 1
        
            for i in range(24):
                bin = self.datahists_pu_time[i].FindBin(event.nPU)
                if bin<1 or bin>self.datahists_pu_time[i].GetNbinsX():
                    event.puWeightTime[i] = 0
                    event.puWeightTimeUp[i] = 0
                    event.puWeightTimeDown[i] = 0
                else:
                    data      = self.datahists_pu_time[i].GetBinContent(bin)
                    mc        = self.mchist.GetBinContent(bin)

                    data_up   = self.datahists_pu_time_up[i].GetBinContent(bin)
                    data_down = self.datahists_pu_time_down[i].GetBinContent(bin)
                    #Protect 0 division!!!!
                    if mc !=0.0:
                        event.puWeightTime[i]     = data/mc
                        event.puWeightTimeUp[i]   = data_up/mc
                        event.puWeightTimeDown[i] = data_down/mc
                    else:
                        event.puWeightTime[i] = 1
                        event.puWeightTimeUp[i] = 1
                        event.puWeightTimeDown[i] = 1

        #print "event PU weight orig, up, down : ", event.puWeight, event.puWeightUp, event.puWeightDown
        #print "event PU weight inc, up, down : ", event.puWeightInc, event.puWeightIncUp, event.puWeightIncDown
        #for i in range(24):
        #    print "PU weight time bin ", event.puWeightTime[i], event.puWeightTimeUp[i], event.puWeightTimeDown[i]

        #import pdb; pdb.set_trace()
        event.eventWeight *= event.puWeight
        self.averages['puWeight'].add( event.puWeight)
        return True

    def write(self, setup):
        super(PileUpAnalyzer, self).write(setup)
        if self.cfg_comp.isMC and self.doHists:
            self.rawmcpileup.write()


setattr(PileUpAnalyzer,"defaultConfig", cfg.Analyzer(
    class_object = PileUpAnalyzer,
    true = True,  # use number of true interactions for reweighting
    makeHists=False
)
)

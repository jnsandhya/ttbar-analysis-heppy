from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
import PhysicsTools.HeppyCore.framework.config as cfg
from DataFormats.FWLite import Handle, Runs
from ROOT.gen import WeightsInfo
from CMGTools.RootTools.statistics.TreeNumpy import TreeNumpy
from ROOT import TFile, TH1F

class LHEWeightAnalyzer( Analyzer ):
    """Read the WeightsInfo objects of the LHE branch and store them
       in event.LHE_weights list.
       If the WeightsInfo.id is a string, replace it with an integer.
       So far the only allowed string format is "mg_reweight_X",
       which gets stored as str(10000+int(X))
       If w.id is an unknown string or anything but a string or int,
       a RuntimeError is raised.
    """
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(LHEWeightAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)
        self.index = []

    def declareHandles(self):
        super(LHEWeightAnalyzer, self).declareHandles()

        self.mchandles['LHEweights'] = AutoHandle('externalLHEProducer',
                                                  'LHEEventProduct',
                                                  mayFail=True,
                                                  fallbackLabel='source',
                                                  lazy=False )

        self.mchandles['GenInfos'] = AutoHandle('generator',
                                                'GenEventInfoProduct',
                                                 mayFail=True,
                                                 fallbackLabel='source',
                                                 lazy=False )

        #self.mchandles['GenHeader'] = AutoHandle('generator',
        #                                         'GenLumiInfoHeader',
        #                                         mayFail=True,
        #                                         fallbackLabel='source',
        #                                         lazy=False )

    def beginLoop(self, setup):
        super(LHEWeightAnalyzer,self).beginLoop(setup)

        self.scale = TH1F('scale', 'scale', 10, 0, 10)
        self.pdf = TH1F('pdf', 'pdf', 103, 0, 103)
        #self.alpha_s = TH1F('alpha_s', 'alpha_s', 2, 0, 2)
        self.ps = TH1F('ps', 'ps', 100, 0, 100)

        if self.cfg_comp.isData:
            return True

        self.run = Runs(self.cfg_comp.files[0])

	#genLumiHandle = AutoHandle('generator',
        #                           'GenLumiInfoHeader',
        #                           mayFail=True,
        #                           fallbackLabel='source',
        #                           lazy=False )


        #genLumiHandle = Handle("GenLumiInfoHeader")
	#self.run.getByLabel('generator', '', 'SIM', genLumiHandle)

	#iterator_psnames = genLumiHandle.product().weightNames()
	#for it in range(len(iterator_psnames)):
	#    print it

	if (self.cfg_comp.name.find('WW')!=-1 or self.cfg_comp.name.find('WZ')!=-1 or self.cfg_comp.name.find('ZZ')!=-1):
	    return True

        runsHandle = Handle('LHERunInfoProduct')
        self.run.getByLabel('externalLHEProducer', runsHandle)

        iterator = runsHandle.product().headers_begin()

	hasNNLO31pdf = False

        # scan iterator so that it includes weight information
        for it in range(100):
            flag = False
            for itt in iterator.base().lines():
                #print itt
                if (itt.find('weight') != -1 and itt.find('id') != -1): 
		    flag = True
		    if (itt.find('306001')!=-1):
		        hasNNLO31pdf = True
            if flag: 
                break
            else: iterator.next()
        else:
            print 'Could not find any weight information !!'

	if (hasNNLO31pdf==True):
	    print 'Contains NNPDF3.1 nnlo variation'
	else:
	    print 'Does not contain NNPDF3.1 nnlo variation'

        self.index = []
        self.pdfindex = []
        #self.alphaindex = []

        idx = 0

        for a in iterator.base().lines(): 
            if (a.find('weight')==-1 or a.find('id')==-1): continue
            #print a

            # For Higgs signal
            #if (a.find('muR')!=-1 and a.find('muF')!=-1 and a.find('muR=2 muF=0.5')==-1 and a.find('muR=0.5 muF=2')==-1):
            # For LO Z->tautau
            #if(a.find('mur')!=-1 and a.find('muf')!=-1 and a.find('mur=2 muf=0.5')==-1 and a.find('mur=0.5 muf=2')==-1):
	    # TTbar signal
	    if ((a.find('renscfact')!=-1 and a.find('facscfact')!=-1 and a.find('renscfact=2d0 facscfact=0.5d0')==-1 and a.find('renscfact=0.5d0 facscfact=2d0')==-1) or (a.find('muR')!=-1 and a.find('muF')!=-1 and a.find('muR=0.50000E+00 muF=0.20000E+01')==-1 and a.find('muR=0.20000E+01 muF=0.50000E+00')==-1) or (a.find('mur')!=-1 and a.find('muf')!=-1 and a.find('mur=2 muf=0.5')==-1 and a.find('mur=0.5 muf=2')==-1)):

                self.index.append(idx)
		#idx += 1
		#continue

# For Higgs signal 
#            if a.find('PDF')!=-1:
#                flag = False
#                for weight_id in range(260000, 260101):
#                    if a.find(str(weight_id))!=-1: flag = True
#
#                if flag:
#                    self.pdfindex.append(idx)
#                
#            if a.find('PDF')!=-1 and a.find('265000')!=-1 or a.find('266000')!=-1: 
#                self.alphaindex.append(idx)


# For TTbar signal
            if (a.find('weight')!=-1 and a.find('id')!=-1):
                flag = False
                #for weight_id in range(2000, 2103):
		if (hasNNLO31pdf==True):
		    for weight_id in range(306001, 306103):
                        #if a.find('id=\"' + str(weight_id) + '\"')!=-1: flag = True
		        if (a.find(str(weight_id))!=-1 and a.find('renscfact')==-1 and a.find('muR')==-1 and a.find('mur')==-1): flag = True
		else:
		    for weight_id in range(292201, 292303):
		        if (a.find(str(weight_id))!=-1 and a.find('renscfact')==-1 and a.find('muR')==-1 and a.find('mur')==-1): flag = True
                if flag:
                    self.pdfindex.append(idx)
                
#            if a.find('pdf')!=-1 and a.find('292301')!=-1 or a.find('292302')!=-1: 

	    #if (a.find('weight')!=-1 and a.find('id')!=-1):
            idx += 1

        #self.alphaindex.append(0)
        #self.alphaindex.append(1)
	
	#In 306000 pdf set, alpha_s variation is the two last replicas?



        print 'scale variation index: ', self.index, 'len', len(self.index)
        print 'pdf variation index: ', self.pdfindex, 'len', len(self.pdfindex)
        #print 'alpha variation index: ', self.alphaindex, 'len', len(self.alphaindex)





    def process(self, event):
        self.readCollections( event.input )

#        import pdb; pdb.set_trace()
        # if not MC, nothing to do
        if not self.cfg_comp.isMC:
            return True

	event.ps_variation = []

	#print 'A'

        if self.mchandles['GenInfos'].isValid():
            for cnt,w in enumerate(self.mchandles['GenInfos'].product().weights()):
		#print cnt, w
		if cnt==0:
		   ps_weight_nominal = w
                event.ps_variation.append(w/ps_weight_nominal)
		#print('ps_weight_nominal='+str(ps_weight_nominal))
		#print('event.ps_variation[-1]='+str(event.ps_variation[-1]))
                #self.ps.Fill(cnt, event.ps_variation[-1])

            setattr(event, 'psWeight', event.ps_variation)

	#print 'B'

        #print 'ps variation: ', event.ps_variation, 'len', len(event.ps_variation)


        if (self.cfg_comp.name.find('WW')!=-1 or self.cfg_comp.name.find('WZ')!=-1 or self.cfg_comp.name.find('ZZ')!=-1):
            return True

        # Add LHE weight info

        event.LHE_originalWeight = 1.0

        if self.mchandles['LHEweights'].isValid()==False: 
            print 'LHE information not available !'
            return True

        event.LHE_originalWeight = self.mchandles['LHEweights'].product().originalXWGTUP()
        event.scale_variation = []
        event.pdf_variation = []
        #event.alpha_variation = []

        for ii, windex in enumerate(self.index):

            #print('self.index ii='+str(ii)+' windex='+str(windex))
            LHE_weight = self.mchandles['LHEweights'].product().weights()[windex].wgt
            event.scale_variation.append(LHE_weight/event.LHE_originalWeight)
	    setattr(event, 'qcdScaleWeight', event.scale_variation)

            #self.scale.Fill(ii, LHE_weight/event.LHE_originalWeight)

        for ii, windex in enumerate(self.pdfindex):

	    #print('self.pdfindex ii='+str(ii)+' windex='+str(windex))
            LHE_weight = self.mchandles['LHEweights'].product().weights()[windex].wgt
            event.pdf_variation.append(LHE_weight/event.LHE_originalWeight)
            setattr(event, 'pdfasWeight', event.pdf_variation)

            #self.pdf.Fill(ii, LHE_weight/event.LHE_originalWeight)

        #for ii, windex in enumerate(self.alphaindex):

         #   LHE_weight = self.mchandles['LHEweights'].product().weights()[windex].wgt
         #   event.alpha_variation.append(LHE_weight/event.LHE_originalWeight)

         #   self.alpha_s.Fill(ii, LHE_weight/event.LHE_originalWeight)

        return True


    def write(self, setup):
#        import pdb; pdb.set_trace()
        super(LHEWeightAnalyzer, self).write(setup)

	#print 'Writing output of LHEWeightAnalyzer'

        if not self.cfg_comp.isMC:
            return True
        if (self.cfg_comp.name.find('WW')!=-1 or self.cfg_comp.name.find('WZ')!=-1 or self.cfg_comp.name.find('ZZ')!=-1):
            return True

        #self.rootfile = TFile('/'.join([self.dirName,
        #                                'weight.root']), 'recreate')

        #self.alpha_s.Write()
        #self.pdf.Write()
        #self.scale.Write()
	#self.ps.Write()
        #self.rootfile.Write()
        #self.rootfile.Close()


setattr(LHEWeightAnalyzer,"defaultConfig",
    cfg.Analyzer(LHEWeightAnalyzer,
    )
)

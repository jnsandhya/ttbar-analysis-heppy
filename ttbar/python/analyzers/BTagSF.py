import os
import ROOT
import numpy as np

from ROOT import TRandom3, TFile
ROOT.gSystem.Load('libCondToolsBTau')

#todo: move this to separate BTagSF analyzer that could be configured? 
class BTagSF(object):
    '''Translate heppy run 1 BTagSF class to python, and update to 2012.
    '''
    def __init__ (self, seed, wp='loose', year= '2017',tagger = 'DeepCSV', measurement='central') :
        self.randm = TRandom3(seed)
        if year == '2016' :
            if tagger == 'DeepCSV':
                rootfname = '/'.join([os.environ["CMSSW_BASE"],
                                      'src/CMGTools/ttbar/data/2016/btag/btag_efficiency_DeepCSV.root'])
                calib_bc   = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2016/btag/DeepCSV_2016LegacySF_V1_YearCorrelation-V1.csv"))
                calib_incl = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2016/btag/DeepCSV_2016LegacySF_V1.csv"))
            if tagger == 'DeepJet':
                rootfname = '/'.join([os.environ["CMSSW_BASE"],
                              'src/CMGTools/ttbar/data/2016/btag/btag_efficiency_CSVv2.root'])
                calib_bc   = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2016/btag/DeepCSV_2016LegacySF_V1_YearCorrelation-V1.csv"))
                calib_incl = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2016/btag/DeepCSV_2016LegacySF_V1.csv"))
                #calib = ROOT.BTagCalibration("CSVv2", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2016/btag/DeepJet_2016LegacySF_V1.csv"))
            if tagger == 'CSVv2':
                rootfname = '/'.join([os.environ["CMSSW_BASE"],
                              'src/CMGTools/ttbar/data/2016/btag/btag_efficiency_CSVv2.root'])
                calib_bc   = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2016/btag/DeepCSV_2016LegacySF_V1_YearCorrelation-V1.csv"))
                calib_incl = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2016/btag/DeepCSV_2016LegacySF_V1.csv"))
                #calib = ROOT.BTagCalibration("CSVv2", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2016/btag/CSVv2_94XSF_V2_B_F.csv"))

        else:
            if tagger == 'DeepCSV':
                rootfname = '/'.join([os.environ["CMSSW_BASE"],
                                      'src/CMGTools/ttbar/data/2017/btag/btag_efficiency_DeepCSV_2017.root'])
                calib_bc   = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2017/btag/DeepCSV_94XSF_V4_B_F_YearCorrelation-V1.csv"))
                calib_incl = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2017/btag/DeepCSV_94XSF_V5_B_F.csv"))
            if tagger == 'DeepJet':
                rootfname = '/'.join([os.environ["CMSSW_BASE"],
                                      'src/CMGTools/ttbar/data/2017/btag/btag_efficiency_DeepCSV.root'])
                calib_bc   = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2017/btag/DeepCSV_94XSF_V4_B_F_YearCorrelation-V1.csv"))
                calib_incl = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2017/btag/DeepCSV_94XSF_V5_B_F.csv"))
            if tagger == 'CSVv2':
                rootfname = '/'.join([os.environ["CMSSW_BASE"],
                                      'src/CMGTools/ttbar/data/2017/btag/btag_efficiency_DeepCSV.root'])
                #calib = ROOT.BTagCalibration("CSVv2", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2017/btag/CSVv2_94XSF_V2_B_F.csv"))
                calib_bc   = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2017/btag/DeepCSV_94XSF_V4_B_F_YearCorrelation-V1.csv"))
                calib_incl = ROOT.BTagCalibration("DeepCSV", os.path.expandvars("$CMSSW_BASE/src/CMGTools/ttbar/data/2017/btag/DeepCSV_94XSF_V5_B_F.csv"))

        self.mc_eff_file = TFile(rootfname)

        # MC b-tag efficiencies as measured in HTT by Adinda
        self.btag_eff_b = self.mc_eff_file.Get('btag_b')
        self.btag_eff_c = self.mc_eff_file.Get('btag_c')
        self.btag_eff_oth = self.mc_eff_file.Get('btag_oth')

        op_dict = {
            'loose':0,
            'medium':1,
            'tight':2
        }
        print 'Booking b/c reader'

        v_sys = getattr(ROOT, 'vector<string>')()
        v_sys.push_back('up')
        v_sys.push_back('down')
        v_sys.push_back('up_correlated')
        v_sys.push_back('down_correlated')
        v_sys.push_back('up_uncorrelated')
        v_sys.push_back('down_uncorrelated')

        self.reader_bc = ROOT.BTagCalibrationReader(op_dict[wp], measurement, v_sys)
        self.reader_bc.load(calib_bc, 0, 'mujets')
        self.reader_bc.load(calib_bc, 1, 'mujets')
        print 'Booking light reader'
        self.reader_light = ROOT.BTagCalibrationReader(op_dict[wp], measurement, v_sys)
        self.reader_light.load(calib_incl, 2, 'incl')

    @staticmethod
    def getBTVJetFlav(flav):
        if abs(flav) == 5:
            return 0
        elif abs(flav) == 4:
            return 1
        return 2

    def getMCBTagEff(self, pt, eta, flavor):
        hist = self.btag_eff_oth
        if flavor == 5:
            hist = self.btag_eff_b
        elif flavor == 4:
            hist = self.btag_eff_c

        binx = hist.GetXaxis().FindFixBin(pt)
        biny = hist.GetYaxis().FindFixBin(abs(eta))
        eff = hist.GetBinContent(binx, biny)
        return eff

    def getPOGSFB(self, pt, eta, flavor, measurement='central'):
        if flavor in [4,5]:
            return self.reader_bc.eval_auto_bounds(measurement, self.getBTVJetFlav(flavor), eta, pt)
        
        return self.reader_light.eval_auto_bounds(measurement, self.getBTVJetFlav(flavor), eta, pt)

    def isBTagged(self, jet, pt, eta, csv, jetflavor, is_data, csv_cut=0.5803 ): #CSVv2 loose default
        jetflavor = abs(jetflavor)
        setattr(jet, 'btagWeight', 1.)
        SFb = self.getPOGSFB(pt, abs(eta), jetflavor)
        SFb_up = self.getPOGSFB(pt, abs(eta), jetflavor,'up')
        SFb_down = self.getPOGSFB(pt, abs(eta), jetflavor,'down')

        SFb_up_corr = self.getPOGSFB(pt, abs(eta), jetflavor,'up_correlated')
        SFb_down_corr = self.getPOGSFB(pt, abs(eta), jetflavor,'down_correlated')

        SFb_up_uncorr = self.getPOGSFB(pt, abs(eta), jetflavor,'up_uncorrelated')
        SFb_down_uncorr = self.getPOGSFB(pt, abs(eta), jetflavor,'down_uncorrelated')
        #print SFb, SFb_up, SFb_down
        eff_b = self.getMCBTagEff(pt, abs(eta), jetflavor)
        
        if csv > csv_cut:
            if(eff_b != 0):
                jet.btagWeight = (SFb*eff_b)/eff_b
                jet.btagWeightUp = (SFb_up*eff_b)/eff_b
                jet.btagWeightDown = (SFb_down*eff_b)/eff_b

                jet.btagWeightUp_correlated = (SFb_up_corr*eff_b)/eff_b
                jet.btagWeightDown_correlated = (SFb_down_corr*eff_b)/eff_b
                jet.btagWeightUp_uncorrelated = (SFb_up_uncorr*eff_b)/eff_b
                jet.btagWeightDown_uncorrelated = (SFb_down_uncorr*eff_b)/eff_b
            else:
                jet.btagWeight = 1
                jet.btagWeightUp = 1
                jet.btagWeightDown = 1
                jet.btagWeightUp_correlated = 1
                jet.btagWeightDown_correlated = 1
                jet.btagWeightUp_uncorrelated = 1
                jet.btagWeightDown_uncorrelated = 1
            return True
        else:
            if(eff_b != 1):
                jet.btagWeight = (1 - SFb*eff_b)/(1 - eff_b)
                jet.btagWeightUp = (1 - SFb_up*eff_b)/(1 - eff_b)
                jet.btagWeightDown = (1 - SFb_down*eff_b)/(1 - eff_b)
                jet.btagWeightUp_correlated = (1 - SFb_up_corr*eff_b)/(1 - eff_b)
                jet.btagWeightDown_correlated = (1 - SFb_down_corr*eff_b)/(1 - eff_b)
                jet.btagWeightUp_uncorrelated = (1 - SFb_up_uncorr*eff_b)/(1 - eff_b)
                jet.btagWeightDown_uncorrelated = (1 - SFb_down_uncorr*eff_b)/(1 - eff_b)

            else:
                jet.btagWeight = 1
                jet.btagWeightUp = 1
                jet.btagWeightDown = 1
                jet.btagWeightUp_correlated = 1
                jet.btagWeightDown_correlated = 1
                jet.btagWeightUp_uncorrelated = 1
                jet.btagWeightDown_uncorrelated = 1
            return False


if __name__ == '__main__':

    btag = BTagSF(12345)
    #print 'created BTagSF instance'
    #print btag.isBTagged(25., 2.3, 0.9, 5, False)
    #print btag.isBTagged(104.3933, -0.885529, 0.9720, 5, False)


import os
import ROOT
from ROOT import TFile, TH2F

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer


class MuonSystematic(Analyzer):

    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(MuonSystematic, self).__init__(cfg_ana, cfg_comp, looperName)
        self.lumi_BCDEF = 19695.422958521
        self.lumi_GH    = 16226.452636126
        self.year       = self.cfg_ana.year

        if self.year == '2016':
            rootfname_id_1 = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/ttbar/data/2016/muonSF/SystUnc/RunBCDEF_SF_ID.root'])
            rootfname_iso_1 = '/'.join([os.environ["CMSSW_BASE"],
                              'src/CMGTools/ttbar/data/2016/muonSF/SystUnc/RunBCDEF_SF_ISO.root'])
            rootfname_id_2 = '/'.join([os.environ["CMSSW_BASE"],
                           'src/CMGTools/ttbar/data/2016/muonSF/SystUnc/RunGH_SF_ID.root'])                       
            rootfname_iso_2 = '/'.join([os.environ["CMSSW_BASE"],
                              'src/CMGTools/ttbar/data/2016/muonSF/SystUnc/RunGH_SF_ISO.root'])
                

            self.mc_syst_id_file1 = TFile(rootfname_id_1)
            self.mc_syst_id_hist1 = self.mc_syst_id_file1.Get('NUM_TightID_DEN_genTracks_eta_pt_syst')
            self.mc_stat_id_hist1  = self.mc_syst_id_file1.Get('NUM_TightID_DEN_genTracks_eta_pt_stat')
            self.mc_syst_iso_file1 = TFile(rootfname_iso_1)
            self.mc_syst_iso_hist1 = self.mc_syst_iso_file1.Get('NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_syst')
            self.mc_stat_iso_hist1 = self.mc_syst_iso_file1.Get('NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_stat')
            self.mc_syst_id_file2 = TFile(rootfname_id_2)
            self.mc_syst_id_hist2 = self.mc_syst_id_file2.Get('NUM_TightID_DEN_genTracks_eta_pt_syst') 
            self.mc_stat_id_hist2  = self.mc_syst_id_file2.Get('NUM_TightID_DEN_genTracks_eta_pt_stat')
            self.mc_syst_iso_file2 = TFile(rootfname_iso_2)
            self.mc_syst_iso_hist2 = self.mc_syst_iso_file2.Get('NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_syst') 
            self.mc_stat_iso_hist2 = self.mc_syst_iso_file2.Get('NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_stat') 


        elif self.year == '2017':
            rootfname_id_1 = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/ttbar/data/2017/muonSF/RunBCDEF_SF_ID_syst.root'])                       
            rootfname_iso_1 = '/'.join([os.environ["CMSSW_BASE"],
                              'src/CMGTools/ttbar/data/2017/muonSF/RunBCDEF_SF_ISO_syst.root'])
            self.mc_syst_id_file1 = TFile(rootfname_id_1)
            self.mc_syst_id_hist1 = self.mc_syst_id_file1.Get('NUM_TightID_DEN_genTracks_pt_abseta_syst')                              
            self.mc_stat_id_hist1 = self.mc_syst_id_file1.Get('NUM_TightID_DEN_genTracks_pt_abseta_stat')
            self.mc_syst_iso_file1 = TFile(rootfname_iso_1)
            self.mc_syst_iso_hist1 = self.mc_syst_iso_file1.Get('NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta_syst')      
            self.mc_stat_iso_hist1 = self.mc_syst_iso_file1.Get('NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta_stat')      
        
    def process(self, event):

        syst_id_weight = 0.    
        syst_iso_weight = 0.
        stat_id_weight = 0.    
        stat_iso_weight = 0.

        if self.year == '2016':
            syst_id_weight1  = 0.    
            syst_iso_weight1 = 0.
            syst_id_weight2  = 0.    
            syst_iso_weight2 = 0.
            stat_id_weight1  = 0.    
            stat_iso_weight1 = 0.
            stat_id_weight2  = 0.    
            stat_iso_weight2 = 0.
            common_factor = 1. 

        muons = getattr(event, self.cfg_ana.muons)    

        for muon in muons:
            if(muon.pt() < 120):
                if self.year == '2016':
                    common_factor    = self.mc_syst_id_hist1.GetBinContent(self.mc_syst_id_hist1.FindBin(muon.eta(), muon.pt()))*self.lumi_BCDEF + self.mc_syst_id_hist2.GetBinContent(self.mc_syst_id_hist2.FindBin(muon.eta(), muon.pt()))*self.lumi_GH
                    syst_id_weight1  = self.mc_syst_id_hist1.GetBinError(self.mc_syst_id_hist1.FindBin(muon.eta(), muon.pt()))*self.lumi_BCDEF/common_factor
                    syst_id_weight2  = self.mc_syst_id_hist2.GetBinError(self.mc_syst_id_hist2.FindBin(muon.eta(), muon.pt()))*self.lumi_GH/common_factor

                    syst_id_weight  += syst_id_weight1**2 + syst_id_weight2**2

                    syst_iso_weight1 = self.mc_syst_iso_hist1.GetBinError(self.mc_syst_iso_hist1.FindBin(muon.eta(), muon.pt()))*self.lumi_BCDEF/common_factor
                    syst_iso_weight2 = self.mc_syst_iso_hist2.GetBinError(self.mc_syst_iso_hist2.FindBin(muon.eta(), muon.pt()))*self.lumi_GH/common_factor

                    syst_iso_weight += syst_iso_weight1**2 + syst_iso_weight2**2


                    common_factor    = self.mc_stat_id_hist1.GetBinContent(self.mc_stat_id_hist1.FindBin(muon.eta(), muon.pt()))*self.lumi_BCDEF + self.mc_stat_id_hist2.GetBinContent(self.mc_stat_id_hist2.FindBin(muon.eta(), muon.pt()))*self.lumi_GH
                    stat_id_weight1  = self.mc_stat_id_hist1.GetBinError(self.mc_stat_id_hist1.FindBin(muon.eta(), muon.pt()))*self.lumi_BCDEF/common_factor
                    stat_id_weight2  = self.mc_stat_id_hist2.GetBinError(self.mc_stat_id_hist2.FindBin(muon.eta(), muon.pt()))*self.lumi_GH/common_factor
                    
                    stat_id_weight  += stat_id_weight1**2 + stat_id_weight2**2
                    
                    stat_iso_weight1 = self.mc_stat_iso_hist1.GetBinError(self.mc_stat_iso_hist1.FindBin(muon.eta(), muon.pt()))*self.lumi_BCDEF/common_factor
                    stat_iso_weight2 = self.mc_stat_iso_hist2.GetBinError(self.mc_stat_iso_hist2.FindBin(muon.eta(), muon.pt()))*self.lumi_GH/common_factor
                    
                    stat_iso_weight += stat_iso_weight1**2 + stat_iso_weight2**2
      
                elif self.year == '2017': 
                    syst_id_weight  += (self.mc_syst_id_hist1.GetBinError(self.mc_syst_id_hist1.FindBin(muon.pt(),abs(muon.eta())))/self.mc_syst_id_hist1.GetBinContent(self.mc_syst_id_hist1.FindBin(muon.pt(),abs(muon.eta()))))**2 
                    syst_iso_weight += (self.mc_syst_iso_hist1.GetBinError(self.mc_syst_iso_hist1.FindBin(muon.pt(),abs(muon.eta())))/self.mc_syst_iso_hist1.GetBinContent(self.mc_syst_iso_hist1.FindBin(muon.pt(),abs(muon.eta()))))**2

                    stat_id_weight  += (self.mc_stat_id_hist1.GetBinError(self.mc_stat_id_hist1.FindBin(muon.pt(),abs(muon.eta())))/self.mc_syst_id_hist1.GetBinContent(self.mc_stat_id_hist1.FindBin(muon.pt(),abs(muon.eta()))))**2 
                    stat_iso_weight += (self.mc_stat_iso_hist1.GetBinError(self.mc_stat_iso_hist1.FindBin(muon.pt(),abs(muon.eta())))/self.mc_stat_iso_hist1.GetBinContent(self.mc_stat_iso_hist1.FindBin(muon.pt(),abs(muon.eta()))))**2

               
        
        syst_id_weight  = syst_id_weight**0.5
        syst_iso_weight = syst_iso_weight**0.5
        stat_id_weight  = stat_id_weight**0.5
        stat_iso_weight = stat_iso_weight**0.5

    
        setattr(event, 'systMuonIdWeight', syst_id_weight)
        setattr(event, 'systMuonIsoWeight', syst_iso_weight)
        setattr(event, 'statMuonIdWeight', stat_id_weight)
        setattr(event, 'statMuonIsoWeight', stat_iso_weight)
        
       
#scale factor = (L(BCDEF)*sf(BCDEF) + L(GH)*sf(GH))/(L(BCDEF)+L(GH)) 
        
        

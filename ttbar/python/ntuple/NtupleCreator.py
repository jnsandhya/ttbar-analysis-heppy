from tools import *
from CMGTools.ttbar.utils.JesEnergyScaleSources import *
import math

#if year == '2016':
#        redjesunc_sources = redjesunc_sources_2016
#else:
#        redjesunc_sources = redjesunc_sources_2017


default = Variable.default

weight_pdfas_variation = []

event = Block(
    'event', lambda x: x,
    run = v(lambda x: x.run, int),
    lumi = v(lambda x: x.lumi, int),
    event = v(lambda x: x.eventId, int, 'l'),
    n_up = v(lambda x: getattr(x, 'NUP', default), int),
    n_pu = v(lambda x: getattr(x, 'nPU', default) if getattr(x, 'nPU', default) is not None else default, int),# to handle data and embedded samples
    n_pv = v(lambda x: len(x.vertices), int),
    rho = v(lambda x: x.rho),
    is_data = v(lambda x: x.input.eventAuxiliary().isRealData(), int),
    unix_time = v(lambda x: x.unixTime),
    #inst_lumi_delivred = v(lambda x: x.instLumiDelivred),
    #inst_lumi_recorded = v(lambda x: x.instLumiRecorded)
    )
   
#items1 = {}
#items2 = {}
#for iJet, key in enumerate(jesunc_sources.keys()) :
 # branch_name = "corr_%s_JEC_up" %(key)
  #branch_name2 = "corr_%s_JEC_down" %(key)
  #test_nominal = v(lambda x: 1 if (len(x)>1 and (x[0].pt()>30. and x[1].pt()>30.) ) else 0, int),
  #items1[branch_name] = v(lambda x: 1 if (len(x)>1 and (x[0].pt()*getattr(x[0],  branch_name, 0.) > 30. and x[1].pt()*getattr(x[1],  branch_name, 0.) > 30. )) else 0, int)
  #items1[branch_name2] = v(lambda x: 1 if (len(x)>1 and (x[0].pt()*getattr(x[0],  branch_name2, 0.) > 30. and x[1].pt()*getattr(x[1],  branch_name2, 0.) > 30. )) else 0, int)
  #items1[branch_name2] = v(lambda x: getattr(x[0], "corr_"+key+"_JEC_down", 0.) if len(x)>0 else 0)
  #items1[branch_name3] = v(lambda x: getattr(x[1], "corr_"+key+"_JEC_up", 0.) if len(x)>1 else 0)
  #items1[branch_name4] = v(lambda x: getattr(x[1], "corr_"+key+"_JEC_down", 0.) if len(x)>1 else 0)
  #print(branch_name)

jets30 = Block(
    'jets_30', lambda x: x.jets_30,
    n_jets = v(lambda x: len(x), int),
    j1_pt = v(lambda x: x[0].pt() if len(x)>0 else default),
    j1_eta = v(lambda x: x[0].eta() if len(x)>0 else default),
    j1_phi = v(lambda x: x[0].phi() if len(x)>0 else default),
    j1_m = v(lambda x: x[0].mass() if len(x)>0 else default),
    # j1_bcsv = v(lambda x: x.bcsv()),
    j1_pumva = v(lambda x: x[0].puMva('pileupJetId:fullDiscriminant') if len(x)>0 else default),
#    j1_puid = v(lambda x: x[0].pileUpJetId_htt() if len(x)>0 else default),
    j1_flavour_parton = v(lambda x: x[0].partonFlavour() if len(x)>0 else default),
    j1_flavour_hadron = v(lambda x: x[0].hadronFlavour() if len(x)>0 else default),
    j1_rawf = v(lambda x: x[0].rawFactor() if len(x)>0 else default),
    j2_pt = v(lambda x: x[1].pt() if len(x)>1 else default),
    j2_eta = v(lambda x: x[1].eta() if len(x)>1 else default),
    j2_phi = v(lambda x: x[1].phi() if len(x)>1 else default),
    j2_m = v(lambda x: x[1].mass() if len(x)>1 else default),
    j2_pumva = v(lambda x: x[1].puMva('pileupJetId:fullDiscriminant') if len(x)>1 else default ),
#    j2_puid = v(lambda x: x[1].pileUpJetId_htt() if len(x)>1 else default ),
    j2_flavour_parton = v(lambda x: x[1].partonFlavour() if len(x)>1 else default),
    j2_flavour_hadron = v(lambda x: x[1].hadronFlavour() if len(x)>1 else default),
    j2_rawf = v(lambda x: x[1].rawFactor() if len(x)>1 else default),
    dijet_m = v(lambda x: (x[0].p4()+x[1].p4()).M() if len(x)>1 else default),
    #corr_nominal = v(lambda x: 1 if (len(x)>1 and (x[0].pt()>30. and x[1].pt()>30.) ) else 0, int),
    #corr_nominal = v(lambda x: True if (len(x)>1 and (x[0].pt>30. and x[1].pt>30.) ) else False), 
    #j2_corr_nominal = v(lambda x: getattr(x[1], "corr_nominal",1.) if len(x)>1 else 1), 
    #j1_corr_CMS_scale_j_eta0to5_13Tev_JEC_up =  v(lambda x: getattr(x[0], "corr_CMS_scale_j_eta0to5_13Tev_JEC_up", 0.) if len(x)>0 else 0),
   # **items1
)

#jets2_30 = Block(
#    'jets_30', lambda x: x.jets_30,
 
#    **items2
#)

#jets1unc_30 = Block(
#  'jets_30', lambda x: x.jets_30,
#    **items1)
#
#jets2unc_30 = Block(
#    'jets_30', lambda x: x.jets_30,
#    **items2
#)


#unc_jet =  Block(
#    'jets_30', lambda x: x.jets_30,
#    **items1)
#    #**items2)

#metvars = Block(
#    'metvars', lambda x: x.pfmet,
#    met = v(lambda x: x.pt()),
#    metphi = v(lambda x: x.phi()),
#)

weights = Block(
    'weights', lambda x: x, 
    weight = v(lambda x : x.eventWeight),
    weight_top = v(lambda x : getattr(x, 'topWeight', 1.)),
    weight_generator = v(lambda x : getattr(x, 'generatorWeight', 1.)),
    weight_pu = v(lambda x : getattr(x, 'puWeight', 1.)),
    weight_pu_up = v(lambda x : getattr(x, 'puWeightUp',1.)),
    weight_pu_down = v(lambda x : getattr(x, 'puWeightDown',1.)),
    weight_punew = v(lambda x : getattr(x, 'puWeightNew', 1.)),
    weight_punew_up = v(lambda x : getattr(x, 'puWeightNewUp',1.)),
    weight_punew_down = v(lambda x : getattr(x, 'puWeightNewDown',1.)),
    weight_puinc = v(lambda x : getattr(x, 'puWeightInc', 1.)),
    weight_puinc_up = v(lambda x : getattr(x, 'puWeightIncUp',1.)),
    weight_puinc_down = v(lambda x : getattr(x, 'puWeightIncDown',1.)),
    weight_putime0 = v(lambda x : getattr(x, 'puWeightTime')[0] if hasattr(x, 'puWeightTime') else default),
    weight_putime0_up = v(lambda x : getattr(x, 'puWeightTimeUp')[0] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime0_down = v(lambda x : getattr(x, 'puWeightTimeDown')[0] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime1 = v(lambda x : getattr(x, 'puWeightTime')[1] if hasattr(x, 'puWeightTime') else default),
    weight_putime1_up = v(lambda x : getattr(x, 'puWeightTimeUp')[1] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime1_down = v(lambda x : getattr(x, 'puWeightTimeDown')[1] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime2 = v(lambda x : getattr(x, 'puWeightTime')[2] if hasattr(x, 'puWeightTime') else default),
    weight_putime2_up = v(lambda x : getattr(x, 'puWeightTimeUp')[2] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime2_down = v(lambda x : getattr(x, 'puWeightTimeDown')[2] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime3 = v(lambda x : getattr(x, 'puWeightTime')[3] if hasattr(x, 'puWeightTime') else default),
    weight_putime3_up = v(lambda x : getattr(x, 'puWeightTimeUp')[3] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime3_down = v(lambda x : getattr(x, 'puWeightTimeDown')[3] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime4 = v(lambda x : getattr(x, 'puWeightTime')[4] if hasattr(x, 'puWeightTime') else default),
    weight_putime4_up = v(lambda x : getattr(x, 'puWeightTimeUp')[4] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime4_down = v(lambda x : getattr(x, 'puWeightTimeDown')[4] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime5 = v(lambda x : getattr(x, 'puWeightTime')[5] if hasattr(x, 'puWeightTime') else default),
    weight_putime5_up = v(lambda x : getattr(x, 'puWeightTimeUp')[5] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime5_down = v(lambda x : getattr(x, 'puWeightTimeDown')[5] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime6 = v(lambda x : getattr(x, 'puWeightTime')[6] if hasattr(x, 'puWeightTime') else default),
    weight_putime6_up = v(lambda x : getattr(x, 'puWeightTimeUp')[6] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime6_down = v(lambda x : getattr(x, 'puWeightTimeDown')[6] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime7 = v(lambda x : getattr(x, 'puWeightTime')[7] if hasattr(x, 'puWeightTime') else default),
    weight_putime7_up = v(lambda x : getattr(x, 'puWeightTimeUp')[7] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime7_down = v(lambda x : getattr(x, 'puWeightTimeDown')[7] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime8 = v(lambda x : getattr(x, 'puWeightTime')[8] if hasattr(x, 'puWeightTime') else default),
    weight_putime8_up = v(lambda x : getattr(x, 'puWeightTimeUp')[8] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime8_down = v(lambda x : getattr(x, 'puWeightTimeDown')[8] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime9 = v(lambda x : getattr(x, 'puWeightTime')[9] if hasattr(x, 'puWeightTime') else default),
    weight_putime9_up = v(lambda x : getattr(x, 'puWeightTimeUp')[9] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime9_down = v(lambda x : getattr(x, 'puWeightTimeDown')[9] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime10 = v(lambda x : getattr(x, 'puWeightTime')[10] if hasattr(x, 'puWeightTime') else default),
    weight_putime10_up = v(lambda x : getattr(x, 'puWeightTimeUp')[10] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime10_down = v(lambda x : getattr(x, 'puWeightTimeDown')[10] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime11 = v(lambda x : getattr(x, 'puWeightTime')[11] if hasattr(x, 'puWeightTime') else default),
    weight_putime11_up = v(lambda x : getattr(x, 'puWeightTimeUp')[11] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime11_down = v(lambda x : getattr(x, 'puWeightTimeDown')[11] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime12 = v(lambda x : getattr(x, 'puWeightTime')[12] if hasattr(x, 'puWeightTime') else default),
    weight_putime12_up = v(lambda x : getattr(x, 'puWeightTimeUp')[12] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime12_down = v(lambda x : getattr(x, 'puWeightTimeDown')[12] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime13 = v(lambda x : getattr(x, 'puWeightTime')[13] if hasattr(x, 'puWeightTime') else default),
    weight_putime13_up = v(lambda x : getattr(x, 'puWeightTimeUp')[13] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime13_down = v(lambda x : getattr(x, 'puWeightTimeDown')[13] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime14 = v(lambda x : getattr(x, 'puWeightTime')[14] if hasattr(x, 'puWeightTime') else default),
    weight_putime14_up = v(lambda x : getattr(x, 'puWeightTimeUp')[14] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime14_down = v(lambda x : getattr(x, 'puWeightTimeDown')[14] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime15 = v(lambda x : getattr(x, 'puWeightTime')[15] if hasattr(x, 'puWeightTime') else default),
    weight_putime15_up = v(lambda x : getattr(x, 'puWeightTimeUp')[15] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime15_down = v(lambda x : getattr(x, 'puWeightTimeDown')[15] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime16 = v(lambda x : getattr(x, 'puWeightTime')[16] if hasattr(x, 'puWeightTime') else default),
    weight_putime16_up = v(lambda x : getattr(x, 'puWeightTimeUp')[16] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime16_down = v(lambda x : getattr(x, 'puWeightTimeDown')[16] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime17 = v(lambda x : getattr(x, 'puWeightTime')[17] if hasattr(x, 'puWeightTime') else default),
    weight_putime17_up = v(lambda x : getattr(x, 'puWeightTimeUp')[17] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime17_down = v(lambda x : getattr(x, 'puWeightTimeDown')[17] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime18 = v(lambda x : getattr(x, 'puWeightTime')[18] if hasattr(x, 'puWeightTime') else default),
    weight_putime18_up = v(lambda x : getattr(x, 'puWeightTimeUp')[18] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime18_down = v(lambda x : getattr(x, 'puWeightTimeDown')[18] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime19 = v(lambda x : getattr(x, 'puWeightTime')[19] if hasattr(x, 'puWeightTime') else default),
    weight_putime19_up = v(lambda x : getattr(x, 'puWeightTimeUp')[19] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime19_down = v(lambda x : getattr(x, 'puWeightTimeDown')[19] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime20 = v(lambda x : getattr(x, 'puWeightTime')[20] if hasattr(x, 'puWeightTime') else default),
    weight_putime20_up = v(lambda x : getattr(x, 'puWeightTimeUp')[20] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime20_down = v(lambda x : getattr(x, 'puWeightTimeDown')[20] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime21 = v(lambda x : getattr(x, 'puWeightTime')[21] if hasattr(x, 'puWeightTime') else default),
    weight_putime21_up = v(lambda x : getattr(x, 'puWeightTimeUp')[21] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime21_down = v(lambda x : getattr(x, 'puWeightTimeDown')[21] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime22 = v(lambda x : getattr(x, 'puWeightTime')[22] if hasattr(x, 'puWeightTime') else default),
    weight_putime22_up = v(lambda x : getattr(x, 'puWeightTimeUp')[22] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime22_down = v(lambda x : getattr(x, 'puWeightTimeDown')[22] if hasattr(x, 'puWeightTimeDown') else default),
    weight_putime23 = v(lambda x : getattr(x, 'puWeightTime')[23] if hasattr(x, 'puWeightTime') else default),
    weight_putime23_up = v(lambda x : getattr(x, 'puWeightTimeUp')[23] if hasattr(x, 'puWeightTimeUp') else default),
    weight_putime23_down = v(lambda x : getattr(x, 'puWeightTimeDown')[23] if hasattr(x, 'puWeightTimeDown') else default),
    weight_sfb = v(lambda x : getattr(x, 'sfWeight', 1.)),
    weight_sfb_up = v(lambda x : getattr(x, 'sfbWeightUp', 1.)),
    weight_sfb_down = v(lambda x : getattr(x, 'sfbWeightDown', 1.)),
    weight_sfb_up_correlated = v(lambda x : getattr(x, 'sfbWeightUp_correlated', 1.)),
    weight_sfb_down_correlated = v(lambda x : getattr(x, 'sfbWeightDown_correlated', 1.)),
    weight_sfb_up_uncorrelated = v(lambda x : getattr(x, 'sfbWeightUp_uncorrelated', 1.)),
    weight_sfb_down_uncorrelated = v(lambda x : getattr(x, 'sfbWeightDown_uncorrelated', 1.)),
    #weight_sfc = v(lambda x : getattr(x, 'sfcWeight', 1.)),
    #weight_sfc_up = v(lambda x : getattr(x, 'sfcWeightUp', 1.)),
    #weight_sfc_down = v(lambda x : getattr(x, 'sfcWeightDown', 1.)),
    #weight_sfl = v(lambda x : getattr(x, 'sflWeight', 1.)),
    weight_sfl_up = v(lambda x : getattr(x, 'sflWeightUp', 1.)),
    weight_sfl_down = v(lambda x : getattr(x, 'sflWeightDown', 1.)),
    weight_sfl_up_correlated = v(lambda x : getattr(x, 'sflWeightUp_correlated', 1.)),
    weight_sfl_down_correlated = v(lambda x : getattr(x, 'sflWeightDown_correlated', 1.)),
    weight_sfl_up_uncorrelated = v(lambda x : getattr(x, 'sflWeightUp_uncorrelated', 1.)),
    weight_sfl_down_uncorrelated = v(lambda x : getattr(x, 'sflWeightDown_uncorrelated', 1.)),

    weight_sfe_id = v(lambda x : getattr(x, 'sfeIdWeight', 1.)),
    weight_sfe_reco = v(lambda x : getattr(x, 'sfeRecoWeight', 1.)),
    weight_sfm_id = v(lambda x : getattr(x, 'sfmIdWeight', 1.)),
    weight_sfm_iso = v(lambda x : getattr(x, 'sfmIsoWeight', 1.)),
#    weight_sf_ee_trig = v(lambda x : getattr(x, 'sfEETrigWeight', 1.)),
    weight_sf_em_trig = v(lambda x : getattr(x, 'sfEMTrigWeight', 1.)),
#    weight_sf_mm_trig = v(lambda x : getattr(x, 'sfMTrigWeight', 1.)),
    weight_prefiring = v(lambda x : getattr(x, 'prefiringWeight', 1.)),
    weight_prefiring_up = v(lambda x : getattr(x, 'prefiringWeightUp', 1.)),
    weight_prefiring_down = v(lambda x : getattr(x, 'prefiringWeightDown', 1.)),

    weight_qcdscale_variation0 = v(lambda x : getattr(x, 'qcdScaleWeight')[1] if hasattr(x, 'qcdScaleWeight') else default),
    weight_qcdscale_variation1 = v(lambda x : getattr(x, 'qcdScaleWeight')[2] if hasattr(x, 'qcdScaleWeight') else default),
    weight_qcdscale_variation2 = v(lambda x : getattr(x, 'qcdScaleWeight')[3] if hasattr(x, 'qcdScaleWeight') else default),
    weight_qcdscale_variation3 = v(lambda x : getattr(x, 'qcdScaleWeight')[4] if hasattr(x, 'qcdScaleWeight') else default),
    weight_qcdscale_variation4 = v(lambda x : getattr(x, 'qcdScaleWeight')[5] if hasattr(x, 'qcdScaleWeight') else default),
    weight_qcdscale_variation5 = v(lambda x : getattr(x, 'qcdScaleWeight')[6] if hasattr(x, 'qcdScaleWeight') else default),

    #v(lambda x : x.qcdScaleWeight[2]
    #and len(x.qcdScaleWeight)>=7) else default
    #weight_pdfas_variation =  v(lambda x : x.pdfasWeight if len(x.pdfasWeight)>0 else default), 
    weight_pdfas_variation =  v(lambda x : getattr(x, 'pdfasWeight') if hasattr(x, 'pdfasWeight') else default),

    #weight_pdfas_variation0 = v(lambda x : x.pdfasWeight[1] if len(x.pdfasWeight)>=100 else default),

    weight_ps_variation0 = v(lambda x : getattr(x, 'psWeight')[2] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=2) else default),
    weight_ps_variation1 = v(lambda x : getattr(x, 'psWeight')[3] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=3) else default),
    weight_ps_variation2 = v(lambda x : getattr(x, 'psWeight')[4] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=4) else default),
    weight_ps_variation3 = v(lambda x : getattr(x, 'psWeight')[5] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=5) else default),
    weight_ps_variation4 = v(lambda x : getattr(x, 'psWeight')[6] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=6) else default),
    weight_ps_variation5 = v(lambda x : getattr(x, 'psWeight')[7] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=7) else default),
    weight_ps_variation6 = v(lambda x : getattr(x, 'psWeight')[8] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=8) else default),
    weight_ps_variation7 = v(lambda x : getattr(x, 'psWeight')[9] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=9) else default),
    weight_ps_variation8 = v(lambda x : getattr(x, 'psWeight')[10] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=10) else default),
    weight_ps_variation9 = v(lambda x : getattr(x, 'psWeight')[11] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=11) else default),
    weight_ps_variation10 = v(lambda x : getattr(x, 'psWeight')[12] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=12) else default),
    weight_ps_variation11 = v(lambda x : getattr(x, 'psWeight')[13] if (hasattr(x, 'psWeight') and len(getattr(x, 'psWeight'))>=13) else default),



) 

syst = Block(
    'systematics', lambda x: x,
#    weight_syst = v(lambda x : x.eventSystWeight),
    syst_muon_id = v(lambda x : getattr(x, 'systMuonIdWeight', 0.)),
    syst_muon_iso = v(lambda x : getattr(x, 'systMuonIsoWeight',0.)),
    stat_muon_id = v(lambda x : getattr(x, 'statMuonIdWeight', 0.)),
    stat_muon_iso = v(lambda x : getattr(x, 'statMuonIsoWeight',0.)),
    syst_elec_id = v(lambda x : getattr(x, 'systElecIdWeight',0.)),
    syst_elec_reco = v(lambda x : getattr(x, 'systElecRecoWeight',0.)),

#    syst_ee_trig = v(lambda x : getattr(x, 'systEETrigWeight', 0.)),
    syst_em_trig = v(lambda x : getattr(x, 'systEMTrigWeight', 0.)),
#    syst_mm_trig = v(lambda x : getattr(x, 'systMTrigWeight', 0.)),
)  

#triggers_fired = Block()

triggers2017 = Block(
    'triggers2017', lambda x: getattr(x, 'trigger_infos', []),
    # electron
    trg_electron_ele32doubleEG_fired       = v(lambda x : any('Ele32_WPTight_Gsf_L1DoubleEG_v' in trg.name for trg in x if trg.fired)),
    trg_electron_ele35_fired               = v(lambda x : any('Ele35_WPTight_Gsf_v' in trg.name for trg in x if trg.fired)),
    trg_electron_ele38_fired               = v(lambda x : any('Ele38_WPTight_Gsf_v' in trg.name for trg in x if trg.fired)), 
    # double electron
    trg_double_electron_ele23ele12DZ_fired = v(lambda x : any('Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v' in trg.name for trg in x if trg.fired)), 
    trg_double_electron_ele23ele12_fired   = v(lambda x : any('Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v' in trg.name for trg in x if trg.fired)),    
    # muon 
    trg_muon_mu24eta21_fired               = v(lambda x : any('IsoMu24_eta2p1_v' in trg.name for trg in x if trg.fired)), 
    trg_muon_mu27_fired                    = v(lambda x : any('IsoMu27_v' in trg.name for trg in x if trg.fired)),    
    # double muon
    trg_double_muon_mu17_fired             = v(lambda x : any('Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v' in trg.name for trg in x if trg.fired)),
    trg_double_muon_mu17m3_fired           = v(lambda x : any('Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v' in trg.name for trg in x if trg.fired)),
    trg_double_muon_mu17m8_fired           = v(lambda x : any('Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v' in trg.name for trg in x if trg.fired)), 
    # electron - muon
    trg_muon_electron_mu23ele12_fired      = v(lambda x : any('Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v' in trg.name for trg in x if trg.fired)),
    trg_muon_electron_mu8ele23DZ_fired     = v(lambda x : any('Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v' in trg.name for trg in x if trg.fired)),
    trg_muon_electron_mu12ele23DZ_fired    = v(lambda x : any('Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v' in trg.name for trg in x if trg.fired)),
    trg_muon_electron_mu23ele12DZ_fired    = v(lambda x : any('Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v' in trg.name for trg in x if trg.fired))
)


triggers2016 = Block(
    'triggers2016', lambda x: getattr(x, 'trigger_infos', []),
    # electron
    trg_electron_ele27_fired            = v(lambda x : any('HLT_Ele27_WPTight_Gsf_v' in trg.name for trg in x if trg.fired)),
    trg_electron_ele25eta21_fired       = v(lambda x : any('HLT_Ele25_eta2p1_WPTight_Gsf_v' in trg.name for trg in x if trg.fired)),
    trg_electron_ele32eta21_fired       = v(lambda x : any('HLT_Ele32_eta2p1_WPTight_Gsf_v' in trg.name for trg in x if trg.fired)),

    # double electron
    trg_double_electron_ele23ele12DZ_fired = v(lambda x : any('HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v' in trg.name for trg in x if trg.fired)), 
    trg_double_electron_ele24ele22eta21_fired   = v(lambda x : any('HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v' in trg.name for trg in x if trg.fired)),    
    # muon 
    trg_muon_mu22eta21_fired               = v(lambda x : any('HLT_IsoMu22_eta2p1_v' in trg.name for trg in x if trg.fired)), 
    trg_muon_mutk22eta21_fired             = v(lambda x : any('HLT_IsoTkMu22_eta2p1_v' in trg.name for trg in x if trg.fired)), 
    trg_muon_mu24_fired                    = v(lambda x : any('HLT_IsoMu24_v' in trg.name for trg in x if trg.fired)),    
    trg_muon_mutk24_fired                  = v(lambda x : any('HLT_IsoTkMu24_v' in trg.name for trg in x if trg.fired)),    
    # double muon
    trg_double_muon_mu17_fired             = v(lambda x : any('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v' in trg.name for trg in x if trg.fired)),
    trg_double_muon_mutk17_fired           = v(lambda x : any('HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v' in trg.name for trg in x if trg.fired)),
    # electron - muon
    trg_muon_electron_mu23ele12_fired      = v(lambda x : any('Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v' in trg.name for trg in x if trg.fired)),
    trg_muon_electron_mu23ele12DZ_fired    = v(lambda x : any('Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v' in trg.name for trg in x if trg.fired)),
    trg_muon_electron_mu12ele23_fired      = v(lambda x : any('Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v' in trg.name for trg in x if trg.fired)),
    trg_muon_electron_mu12ele23DZ_fired    = v(lambda x : any('Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v' in trg.name for trg in x if trg.fired)),
    trg_muon_electron_mu8ele23_fired       = v(lambda x : any('Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v' in trg.name for trg in x if trg.fired)),
    trg_muon_electron_mu8ele23DZ_fired     = v(lambda x : any('Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v' in trg.name for trg in x if trg.fired))


)

bjets = Block(
    'bjets_30', lambda x: x.bjets_30,
    n_bjets = v(lambda x: len(x), int),
    #n_bjets_len = v(lambda x: bool(len(x))),
    #b_corr_2 = v(lambda x: True for jet in x if jet.is_btagged)
    #has_b = v(lambda x: bool(sum([jet.is_btagged for jet in x])))
)

up_down = ['up','down']

#bjets_30_corr = []
#for source in redjesunc_sources_2016:
#    for unc in up_down:
#        bjets_corr_name = 'bjets_30_' + source + '_' + unc
#        bjets_30_corr.append(bjets = Block(
#					'bjets_30', lambda x: x.bjets_30,
#    					n_bjets = v(lambda x: len(x), int),




jets_30_corr = []
jets_30_corr_2016 = []
jets_30_corr_2017 = []
#for source in redjesunc_sources_2016:
#    for unc in up_down:
#	jets_corr_name = 'jets_30_' + source + '_' + unc
#	jets_30_corr.append(  Block(
#			 jets_corr_name, lambda x:  getattr(x, jets_corr_name),
#			 n_jets_corr = v(lambda x: len(x), int))
#			)
jets_30_corr.append(  Block(
                        'jets_30_Total_up', lambda x:  getattr(x, 'jets_30_Total_up', []),
                        n_jets_Total_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_Total_down', lambda x:  getattr(x, 'jets_30_Total_down', []),
                        n_jets_Total_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_Absolute_up', lambda x:  getattr(x, 'jets_30_Absolute_up', []),
                        n_jets_Absolute_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_Absolute_down', lambda x:  getattr(x, 'jets_30_Absolute_down', []),
                        n_jets_Absolute_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_AbsoluteMPFBias_up', lambda x:  getattr(x, 'jets_30_AbsoluteMPFBias_up', []),
                        n_jets_AbsoluteMPFBias_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_AbsoluteMPFBias_down', lambda x:  getattr(x, 'jets_30_AbsoluteMPFBias_down', []),
                        n_jets_AbsoluteMPFBias_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_AbsoluteScale_up', lambda x:  getattr(x, 'jets_30_AbsoluteScale_up', []),
                        n_jets_AbsoluteScale_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_AbsoluteScale_down', lambda x:  getattr(x, 'jets_30_AbsoluteScale_down', []),
                        n_jets_AbsoluteScale_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_AbsoluteStat_2016_up', lambda x:  getattr(x, 'jets_30_AbsoluteStat_2016_up', []),
                        n_jets_AbsoluteStat_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_AbsoluteStat_2016_down', lambda x:  getattr(x, 'jets_30_AbsoluteStat_2016_down', []),
                        n_jets_AbsoluteStat_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_AbsoluteStat_2017_up', lambda x:  getattr(x, 'jets_30_AbsoluteStat_2017_up', []),
                        n_jets_AbsoluteStat_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_AbsoluteStat_2017_down', lambda x:  getattr(x, 'jets_30_AbsoluteStat_2017_down', []),
                        n_jets_AbsoluteStat_2017_down = v(lambda x: len(x), int))
                       )

jets_30_corr_2016.append(  Block(
			'jets_30_Absolute_2016_up', lambda x:  getattr(x, 'jets_30_Absolute_2016_up', []),
                        n_jets_Absolute_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_Absolute_2016_down', lambda x:  getattr(x, 'jets_30_Absolute_2016_down', []),
                        n_jets_Absolute_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_Absolute_2017_up', lambda x:  getattr(x, 'jets_30_Absolute_2017_up', []),
                        n_jets_Absolute_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_Absolute_2017_down', lambda x:  getattr(x, 'jets_30_Absolute_2017_down', []),
                        n_jets_Absolute_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_FlavorQCD_up', lambda x:  getattr(x, 'jets_30_FlavorQCD_up', []),
                        n_jets_FlavorQCD_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_FlavorQCD_down', lambda x:  getattr(x, 'jets_30_FlavorQCD_down', []),
                        n_jets_FlavorQCD_down = v(lambda x: len(x), int))
                       )

jets_30_corr.append(  Block(
                        'jets_30_FlavorPureGluon_up', lambda x:  getattr(x, 'jets_30_FlavorPureGluon_up', []),
                        n_jets_FlavorPureGluon_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_FlavorPureGluon_down', lambda x:  getattr(x, 'jets_30_FlavorPureGluon_down', []),
                        n_jets_FlavorPureGluon_down = v(lambda x: len(x), int))
                       )

jets_30_corr.append(  Block(
                        'jets_30_FlavorPureQuark_up', lambda x:  getattr(x, 'jets_30_FlavorPureQuark_up', []),
                        n_jets_FlavorPureQuark_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_FlavorPureQuark_down', lambda x:  getattr(x, 'jets_30_FlavorPureQuark_down', []),
                        n_jets_FlavorPureQuark_down = v(lambda x: len(x), int))
                       )

jets_30_corr.append(  Block(
                        'jets_30_FlavorPureCharm_up', lambda x:  getattr(x, 'jets_30_FlavorPureCharm_up', []),
                        n_jets_FlavorPureCharm_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_FlavorPureCharm_down', lambda x:  getattr(x, 'jets_30_FlavorPureCharm_down', []),
                        n_jets_FlavorPureCharm_down = v(lambda x: len(x), int))
                       )

jets_30_corr.append(  Block(
                        'jets_30_FlavorPureBottom_up', lambda x:  getattr(x, 'jets_30_FlavorPureBottom_up', []),
                        n_jets_FlavorPureBottom_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_FlavorPureBottom_down', lambda x:  getattr(x, 'jets_30_FlavorPureBottom_down', []),
                        n_jets_FlavorPureBottom_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_Fragmentation_up', lambda x:  getattr(x, 'jets_30_Fragmentation_up', []),
                        n_jets_Fragmentation_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_Fragmentation_down', lambda x:  getattr(x, 'jets_30_Fragmentation_down', []),
                        n_jets_Fragmentation_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpDataMC_up', lambda x:  getattr(x, 'jets_30_PileUpDataMC_up', []),
                        n_jets_PileUpDataMC_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpDataMC_down', lambda x:  getattr(x, 'jets_30_PileUpDataMC_down', []),
                        n_jets_PileUpDataMC_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpPtBB_up', lambda x:  getattr(x, 'jets_30_PileUpPtBB_up', []),
                        n_jets_PileUpPtBB_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpPtBB_down', lambda x:  getattr(x, 'jets_30_PileUpPtBB_down', []),
                        n_jets_PileUpPtBB_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpPtEC1_up', lambda x:  getattr(x, 'jets_30_PileUpPtEC1_up', []),
                        n_jets_PileUpPtEC1_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpPtEC1_down', lambda x:  getattr(x, 'jets_30_PileUpPtEC1_down', []),
                        n_jets_PileUpPtEC1_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpPtEC2_up', lambda x:  getattr(x, 'jets_30_PileUpPtEC2_up', []),
                        n_jets_PileUpPtEC2_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpPtEC2_down', lambda x:  getattr(x, 'jets_30_PileUpPtEC2_down', []),
                        n_jets_PileUpPtEC2_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpPtHF_up', lambda x:  getattr(x, 'jets_30_PileUpPtHF_up', []),
                        n_jets_PileUpPtHF_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpPtHF_down', lambda x:  getattr(x, 'jets_30_PileUpPtHF_down', []),
                        n_jets_PileUpPtHF_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpPtRef_up', lambda x:  getattr(x, 'jets_30_PileUpPtRef_up', []),
                        n_jets_PileUpPtRef_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_PileUpPtRef_down', lambda x:  getattr(x, 'jets_30_PileUpPtRef_down', []),
                        n_jets_PileUpPtRef_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_RelativeFSR_up', lambda x:  getattr(x, 'jets_30_RelativeFSR_up', []),
                        n_jets_RelativeFSR_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_RelativeFSR_down', lambda x:  getattr(x, 'jets_30_RelativeFSR_down', []),
                        n_jets_RelativeFSR_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeJEREC1_2016_up', lambda x:  getattr(x, 'jets_30_RelativeJEREC1_2016_up', []),
                        n_jets_RelativeJEREC1_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeJEREC1_2016_down', lambda x:  getattr(x, 'jets_30_RelativeJEREC1_2016_down', []),
                        n_jets_RelativeJEREC1_2016_down = v(lambda x: len(x), int))
                       )

jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeJEREC1_2017_up', lambda x:  getattr(x, 'jets_30_RelativeJEREC1_2017_up', []),
                        n_jets_RelativeJEREC1_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeJEREC1_2017_down', lambda x:  getattr(x, 'jets_30_RelativeJEREC1_2017_down', []),
                        n_jets_RelativeJEREC1_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeJEREC2_2016_up', lambda x:  getattr(x, 'jets_30_RelativeJEREC2_2016_up', []),
                        n_jets_RelativeJEREC2_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeJEREC2_2016_down', lambda x:  getattr(x, 'jets_30_RelativeJEREC2_2016_down', []),
                        n_jets_RelativeJEREC2_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeJEREC2_2017_up', lambda x:  getattr(x, 'jets_30_RelativeJEREC2_2017_up', []),
                        n_jets_RelativeJEREC2_2017_up = v(lambda x: len(x), int))
                       )

jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeJEREC2_2017_down', lambda x:  getattr(x, 'jets_30_RelativeJEREC2_2017_down', []),
                        n_jets_RelativeJEREC2_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_RelativeJERHF_up', lambda x:  getattr(x, 'jets_30_RelativeJERHF_up', []),
                        n_jets_RelativeJERHF_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_RelativeJERHF_down', lambda x:  getattr(x, 'jets_30_RelativeJERHF_down', []),
                        n_jets_RelativeJERHF_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_RelativePtBB_up', lambda x:  getattr(x, 'jets_30_RelativePtBB_up', []),
                        n_jets_RelativePtBB_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_RelativePtBB_down', lambda x:  getattr(x, 'jets_30_RelativePtBB_down', []),
                        n_jets_RelativePtBB_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativePtEC1_2016_up', lambda x:  getattr(x, 'jets_30_RelativePtEC1_2016_up', []),
                        n_jets_RelativePtEC1_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativePtEC1_2016_down', lambda x:  getattr(x, 'jets_30_RelativePtEC1_2016_down', []),
                        n_jets_RelativePtEC1_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativePtEC1_2017_up', lambda x:  getattr(x, 'jets_30_RelativePtEC1_2017_up', []),
                        n_jets_RelativePtEC1_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativePtEC1_2017_down', lambda x:  getattr(x, 'jets_30_RelativePtEC1_2017_down', []),
                        n_jets_RelativePtEC1_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativePtEC2_2016_up', lambda x:  getattr(x, 'jets_30_RelativePtEC2_2016_up', []),
                        n_jets_RelativePtEC2_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativePtEC2_2016_down', lambda x:  getattr(x, 'jets_30_RelativePtEC2_2016_down', []),
                        n_jets_RelativePtEC2_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativePtEC2_2017_up', lambda x:  getattr(x, 'jets_30_RelativePtEC2_2017_up', []),
                        n_jets_RelativePtEC2_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativePtEC2_2017_down', lambda x:  getattr(x, 'jets_30_RelativePtEC2_2017_down', []),
                        n_jets_RelativePtEC2_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_RelativePtHF_up', lambda x:  getattr(x, 'jets_30_RelativePtHF_up', []),
                        n_jets_RelativePtHF_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_RelativePtHF_down', lambda x:  getattr(x, 'jets_30_RelativePtHF_down', []),
                        n_jets_RelativePtHF_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeStatEC_2016_up', lambda x:  getattr(x, 'jets_30_RelativeStatEC_2016_up', []),
                        n_jets_RelativeStatEC_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeStatEC_2016_down', lambda x:  getattr(x, 'jets_30_RelativeStatEC_2016_down', []),
                        n_jets_RelativeStatEC_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeStatEC_2017_up', lambda x:  getattr(x, 'jets_30_RelativeStatEC_2017_up', []),
                        n_jets_RelativeStatEC_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeStatEC_2017_down', lambda x:  getattr(x, 'jets_30_RelativeStatEC_2017_down', []),
                        n_jets_RelativeStatEC_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeStatFSR_2016_up', lambda x:  getattr(x, 'jets_30_RelativeStatFSR_2016_up', []),
                        n_jets_RelativeStatFSR_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeStatFSR_2016_down', lambda x:  getattr(x, 'jets_30_RelativeStatFSR_2016_down', []),
                        n_jets_RelativeStatFSR_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeStatFSR_2017_up', lambda x:  getattr(x, 'jets_30_RelativeStatFSR_2017_up', []),
                        n_jets_RelativeStatFSR_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeStatFSR_2017_down', lambda x:  getattr(x, 'jets_30_RelativeStatFSR_2017_down', []),
                        n_jets_RelativeStatFSR_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeStatHF_2016_up', lambda x:  getattr(x, 'jets_30_RelativeStatHF_2016_up', []),
                        n_jets_RelativeStatHF_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeStatHF_2016_down', lambda x:  getattr(x, 'jets_30_RelativeStatHF_2016_down', []),
                        n_jets_RelativeStatHF_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeStatHF_2017_up', lambda x:  getattr(x, 'jets_30_RelativeStatHF_2017_up', []),
                        n_jets_RelativeStatHF_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeStatHF_2017_down', lambda x:  getattr(x, 'jets_30_RelativeStatHF_2017_down', []),
                        n_jets_RelativeStatHF_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_SinglePionECAL_up', lambda x:  getattr(x, 'jets_30_SinglePionECAL_up', []),
                        n_jets_SinglePionECAL_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_SinglePionECAL_down', lambda x:  getattr(x, 'jets_30_SinglePionECAL_down', []),
                        n_jets_SinglePionECAL_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_SinglePionHCAL_up', lambda x:  getattr(x, 'jets_30_SinglePionHCAL_up', []),
                        n_jets_SinglePionHCAL_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_SinglePionHCAL_down', lambda x:  getattr(x, 'jets_30_SinglePionHCAL_down', []),
                        n_jets_SinglePionHCAL_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_TimePtEta_2016_up', lambda x:  getattr(x, 'jets_30_TimePtEta_2016_up', []),
                        n_jets_TimePtEta_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_TimePtEta_2016_down', lambda x:  getattr(x, 'jets_30_TimePtEta_2016_down', []),
                        n_jets_TimePtEta_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_TimePtEta_2017_up', lambda x:  getattr(x, 'jets_30_TimePtEta_2017_up', []),
                        n_jets_TimePtEta_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_TimePtEta_2017_down', lambda x:  getattr(x, 'jets_30_TimePtEta_2017_down', []),
                        n_jets_TimePtEta_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_BBEC1_up', lambda x:  getattr(x, 'jets_30_BBEC1_up', []),
                        n_jets_BBEC1_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_BBEC1_down', lambda x:  getattr(x, 'jets_30_BBEC1_down', []),
                        n_jets_BBEC1_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_BBEC1_2016_up', lambda x:  getattr(x, 'jets_30_BBEC1_2016_up', []),
                        n_jets_BBEC1_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_BBEC1_2016_down', lambda x:  getattr(x, 'jets_30_BBEC1_2016_down', []),
                        n_jets_BBEC1_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_BBEC1_2017_up', lambda x:  getattr(x, 'jets_30_BBEC1_2017_up', []),
                        n_jets_BBEC1_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_BBEC1_2017_down', lambda x:  getattr(x, 'jets_30_BBEC1_2017_down', []),
                        n_jets_BBEC1_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_EC2_up', lambda x:  getattr(x, 'jets_30_EC2_up', []),
                        n_jets_EC2_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_EC2_down', lambda x:  getattr(x, 'jets_30_EC2_down', []),
                        n_jets_EC2_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_EC2_2016_up', lambda x:  getattr(x, 'jets_30_EC2_2016_up', []),
                        n_jets_EC2_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_EC2_2016_down', lambda x:  getattr(x, 'jets_30_EC2_2016_down', []),
                        n_jets_EC2_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_EC2_2017_up', lambda x:  getattr(x, 'jets_30_EC2_2017_up', []),
                        n_jets_EC2_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_EC2_2017_down', lambda x:  getattr(x, 'jets_30_EC2_2017_down', []),
                        n_jets_EC2_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_HF_up', lambda x:  getattr(x, 'jets_30_HF_up', []),
                        n_jets_HF_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_HF_down', lambda x:  getattr(x, 'jets_30_HF_down', []),
                        n_jets_HF_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_HF_2016_up', lambda x:  getattr(x, 'jets_30_HF_2016_up', []),
                        n_jets_HF_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_HF_2016_down', lambda x:  getattr(x, 'jets_30_HF_2016_down', []),
                        n_jets_HF_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_HF_2017_up', lambda x:  getattr(x, 'jets_30_HF_2017_up', []),
                        n_jets_HF_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_HF_2017_down', lambda x:  getattr(x, 'jets_30_HF_2017_down', []),
                        n_jets_HF_2017_down = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_RelativeBal_up', lambda x:  getattr(x, 'jets_30_RelativeBal_up', []),
                        n_jets_RelativeBal_up = v(lambda x: len(x), int))
                       )
jets_30_corr.append(  Block(
                        'jets_30_RelativeBal_down', lambda x:  getattr(x, 'jets_30_RelativeBal_down', []),
                        n_jets_RelativeBal_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeSample_2016_up', lambda x:  getattr(x, 'jets_30_RelativeSample_2016_up', []),
                        n_jets_RelativeSample_2016_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2016.append(  Block(
                        'jets_30_RelativeSample_2016_down', lambda x:  getattr(x, 'jets_30_RelativeSample_2016_down', []),
                        n_jets_RelativeSample_2016_down = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeSample_2017_up', lambda x:  getattr(x, 'jets_30_RelativeSample_2017_up', []),
                        n_jets_RelativeSample_2017_up = v(lambda x: len(x), int))
                       )
jets_30_corr_2017.append(  Block(
                        'jets_30_RelativeSample_2017_down', lambda x:  getattr(x, 'jets_30_RelativeSample_2017_down', []),
                        n_jets_RelativeSample_2017_down = v(lambda x: len(x), int))
                       )



bjets_30_corr = []
bjets_30_corr_2016 = []
bjets_30_corr_2017 = []
bjets_30_corr.append(  Block(
                        'bjets_30_Total_up', lambda x:  getattr(x, 'bjets_30_Total_up', []),
                        n_bjets_Total_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_Total_down', lambda x:  getattr(x, 'bjets_30_Total_down', []),
                        n_bjets_Total_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_Absolute_up', lambda x:  getattr(x, 'bjets_30_Absolute_up', []),
                        n_bjets_Absolute_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_Absolute_down', lambda x:  getattr(x, 'bjets_30_Absolute_down', []),
                        n_bjets_Absolute_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_AbsoluteMPFBias_up', lambda x:  getattr(x, 'bjets_30_AbsoluteMPFBias_up', []),
                        n_bjets_AbsoluteMPFBias_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_AbsoluteMPFBias_down', lambda x:  getattr(x, 'bjets_30_AbsoluteMPFBias_down', []),
                        n_bjets_AbsoluteMPFBias_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_AbsoluteScale_up', lambda x:  getattr(x, 'bjets_30_AbsoluteScale_up', []),
                        n_bjets_AbsoluteScale_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_AbsoluteScale_down', lambda x:  getattr(x, 'bjets_30_AbsoluteScale_down', []),
                        n_bjets_AbsoluteScale_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_AbsoluteStat_2016_up', lambda x:  getattr(x, 'bjets_30_AbsoluteStat_2016_up', []),
                        n_bjets_AbsoluteStat_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_AbsoluteStat_2016_down', lambda x:  getattr(x, 'bjets_30_AbsoluteStat_2016_down', []),
                        n_bjets_AbsoluteStat_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_AbsoluteStat_2017_up', lambda x:  getattr(x, 'bjets_30_AbsoluteStat_2017_up', []),
                        n_bjets_AbsoluteStat_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_AbsoluteStat_2017_down', lambda x:  getattr(x, 'bjets_30_AbsoluteStat_2017_down', []),
                        n_bjets_AbsoluteStat_2017_down = v(lambda x: len(x), int))
                       )

bjets_30_corr_2016.append(  Block(
			'bjets_30_Absolute_2016_up', lambda x:  getattr(x, 'bjets_30_Absolute_2016_up', []),
                        n_bjets_Absolute_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_Absolute_2016_down', lambda x:  getattr(x, 'bjets_30_Absolute_2016_down', []),
                        n_bjets_Absolute_2016_down = v(lambda x: len(x)))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_Absolute_2017_up', lambda x:  getattr(x, 'bjets_30_Absolute_2017_up', []),
                        n_bjets_Absolute_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_Absolute_2017_down', lambda x:  getattr(x, 'bjets_30_Absolute_2017_down', []),
                        n_bjets_Absolute_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_FlavorQCD_up', lambda x:  getattr(x, 'bjets_30_FlavorQCD_up', []),
                        n_bjets_FlavorQCD_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_FlavorQCD_down', lambda x:  getattr(x, 'bjets_30_FlavorQCD_down', []),
                        n_bjets_FlavorQCD_down = v(lambda x: len(x), int))
                       )

bjets_30_corr.append(  Block(
                        'bjets_30_FlavorPureGluon_up', lambda x:  getattr(x, 'bjets_30_FlavorPureGluon_up', []),
                        n_bjets_FlavorPureGluon_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_FlavorPureGluon_down', lambda x:  getattr(x, 'bjets_30_FlavorPureGluon_down', []),
                        n_bjets_FlavorPureGluon_down = v(lambda x: len(x), int))
                       )

bjets_30_corr.append(  Block(
                        'bjets_30_FlavorPureQuark_up', lambda x:  getattr(x, 'bjets_30_FlavorPureQuark_up', []),
                        n_bjets_FlavorPureQuark_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_FlavorPureQuark_down', lambda x:  getattr(x, 'bjets_30_FlavorPureQuark_down', []),
                        n_bjets_FlavorPureQuark_down = v(lambda x: len(x), int))
                       )

bjets_30_corr.append(  Block(
                        'bjets_30_FlavorPureCharm_up', lambda x:  getattr(x, 'bjets_30_FlavorPureCharm_up', []),
                        n_bjets_FlavorPureCharm_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_FlavorPureCharm_down', lambda x:  getattr(x, 'bjets_30_FlavorPureCharm_down', []),
                        n_bjets_FlavorPureCharm_down = v(lambda x: len(x), int))
                       )

bjets_30_corr.append(  Block(
                        'bjets_30_FlavorPureBottom_up', lambda x:  getattr(x, 'bjets_30_FlavorPureBottom_up', []),
                        n_bjets_FlavorPureBottom_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_FlavorPureBottom_down', lambda x:  getattr(x, 'bjets_30_FlavorPureBottom_down', []),
                        n_bjets_FlavorPureBottom_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_Fragmentation_up', lambda x:  getattr(x, 'bjets_30_Fragmentation_up', []),
                        n_bjets_Fragmentation_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_Fragmentation_down', lambda x:  getattr(x, 'bjets_30_Fragmentation_down', []),
                        n_bjets_Fragmentation_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpDataMC_up', lambda x:  getattr(x, 'bjets_30_PileUpDataMC_up', []),
                        n_bjets_PileUpDataMC_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpDataMC_down', lambda x:  getattr(x, 'bjets_30_PileUpDataMC_down', []),
                        n_bjets_PileUpDataMC_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpPtBB_up', lambda x:  getattr(x, 'bjets_30_PileUpPtBB_up', []),
                        n_bjets_PileUpPtBB_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpPtBB_down', lambda x:  getattr(x, 'bjets_30_PileUpPtBB_down', []),
                        n_bjets_PileUpPtBB_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpPtEC1_up', lambda x:  getattr(x, 'bjets_30_PileUpPtEC1_up', []),
                        n_bjets_PileUpPtEC1_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpPtEC1_down', lambda x:  getattr(x, 'bjets_30_PileUpPtEC1_down', []),
                        n_bjets_PileUpPtEC1_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpPtEC2_up', lambda x:  getattr(x, 'bjets_30_PileUpPtEC2_up', []),
                        n_bjets_PileUpPtEC2_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpPtEC2_down', lambda x:  getattr(x, 'bjets_30_PileUpPtEC2_down', []),
                        n_bjets_PileUpPtEC2_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpPtHF_up', lambda x:  getattr(x, 'bjets_30_PileUpPtHF_up', []),
                        n_bjets_PileUpPtHF_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpPtHF_down', lambda x:  getattr(x, 'bjets_30_PileUpPtHF_down', []),
                        n_bjets_PileUpPtHF_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpPtRef_up', lambda x:  getattr(x, 'bjets_30_PileUpPtRef_up', []),
                        n_bjets_PileUpPtRef_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_PileUpPtRef_down', lambda x:  getattr(x, 'bjets_30_PileUpPtRef_down', []),
                        n_bjets_PileUpPtRef_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_RelativeFSR_up', lambda x:  getattr(x, 'bjets_30_RelativeFSR_up', []),
                        n_bjets_RelativeFSR_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_RelativeFSR_down', lambda x:  getattr(x, 'bjets_30_RelativeFSR_down', []),
                        n_bjets_RelativeFSR_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeJEREC1_2016_up', lambda x:  getattr(x, 'bjets_30_RelativeJEREC1_2016_up', []),
                        n_bjets_RelativeJEREC1_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeJEREC1_2016_down', lambda x:  getattr(x, 'bjets_30_RelativeJEREC1_2016_down', []),
                        n_bjets_RelativeJEREC1_2016_down = v(lambda x: len(x), int))
                       )

bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeJEREC1_2017_up', lambda x:  getattr(x, 'bjets_30_RelativeJEREC1_2017_up', []),
                        n_bjets_RelativeJEREC1_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeJEREC1_2017_down', lambda x:  getattr(x, 'bjets_30_RelativeJEREC1_2017_down', []),
                        n_bjets_RelativeJEREC1_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeJEREC2_2016_up', lambda x:  getattr(x, 'bjets_30_RelativeJEREC2_2016_up', []),
                        n_bjets_RelativeJEREC2_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeJEREC2_2016_down', lambda x:  getattr(x, 'bjets_30_RelativeJEREC2_2016_down', []),
                        n_bjets_RelativeJEREC2_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeJEREC2_2017_up', lambda x:  getattr(x, 'bjets_30_RelativeJEREC2_2017_up', []),
                        n_bjets_RelativeJEREC2_2017_up = v(lambda x: len(x), int))
                       )

bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeJEREC2_2017_down', lambda x:  getattr(x, 'bjets_30_RelativeJEREC2_2017_down', []),
                        n_bjets_RelativeJEREC2_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_RelativeJERHF_up', lambda x:  getattr(x, 'bjets_30_RelativeJERHF_up', []),
                        n_bjets_RelativeJERHF_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_RelativeJERHF_down', lambda x:  getattr(x, 'bjets_30_RelativeJERHF_down', []),
                        n_bjets_RelativeJERHF_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_RelativePtBB_up', lambda x:  getattr(x, 'bjets_30_RelativePtBB_up', []),
                        n_bjets_RelativePtBB_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_RelativePtBB_down', lambda x:  getattr(x, 'bjets_30_RelativePtBB_down', []),
                        n_bjets_RelativePtBB_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativePtEC1_2016_up', lambda x:  getattr(x, 'bjets_30_RelativePtEC1_2016_up', []),
                        n_bjets_RelativePtEC1_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativePtEC1_2016_down', lambda x:  getattr(x, 'bjets_30_RelativePtEC1_2016_down', []),
                        n_bjets_RelativePtEC1_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativePtEC1_2017_up', lambda x:  getattr(x, 'bjets_30_RelativePtEC1_2017_up', []),
                        n_bjets_RelativePtEC1_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativePtEC1_2017_down', lambda x:  getattr(x, 'bjets_30_RelativePtEC1_2017_down', []),
                        n_bjets_RelativePtEC1_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativePtEC2_2016_up', lambda x:  getattr(x, 'bjets_30_RelativePtEC2_2016_up', []),
                        n_bjets_RelativePtEC2_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativePtEC2_2016_down', lambda x:  getattr(x, 'bjets_30_RelativePtEC2_2016_down', []),
                        n_bjets_RelativePtEC2_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativePtEC2_2017_up', lambda x:  getattr(x, 'bjets_30_RelativePtEC2_2017_up', []),
                        n_bjets_RelativePtEC2_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativePtEC2_2017_down', lambda x:  getattr(x, 'bjets_30_RelativePtEC2_2017_down', []),
                        n_bjets_RelativePtEC2_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_RelativePtHF_up', lambda x:  getattr(x, 'bjets_30_RelativePtHF_up', []),
                        n_bjets_RelativePtHF_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_RelativePtHF_down', lambda x:  getattr(x, 'bjets_30_RelativePtHF_down', []),
                        n_bjets_RelativePtHF_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeStatEC_2016_up', lambda x:  getattr(x, 'bjets_30_RelativeStatEC_2016_up', []),
                        n_bjets_RelativeStatEC_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeStatEC_2016_down', lambda x:  getattr(x, 'bjets_30_RelativeStatEC_2016_down', []),
                        n_bjets_RelativeStatEC_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeStatEC_2017_up', lambda x:  getattr(x, 'bjets_30_RelativeStatEC_2017_up', []),
                        n_bjets_RelativeStatEC_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeStatEC_2017_down', lambda x:  getattr(x, 'bjets_30_RelativeStatEC_2017_down', []),
                        n_bjets_RelativeStatEC_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeStatFSR_2016_up', lambda x:  getattr(x, 'bjets_30_RelativeStatFSR_2016_up', []),
                        n_bjets_RelativeStatFSR_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeStatFSR_2016_down', lambda x:  getattr(x, 'bjets_30_RelativeStatFSR_2016_down', []),
                        n_bjets_RelativeStatFSR_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeStatFSR_2017_up', lambda x:  getattr(x, 'bjets_30_RelativeStatFSR_2017_up', []),
                        n_bjets_RelativeStatFSR_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeStatFSR_2017_down', lambda x:  getattr(x, 'bjets_30_RelativeStatFSR_2017_down', []),
                        n_bjets_RelativeStatFSR_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeStatHF_2016_up', lambda x:  getattr(x, 'bjets_30_RelativeStatHF_2016_up', []),
                        n_bjets_RelativeStatHF_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeStatHF_2016_down', lambda x:  getattr(x, 'bjets_30_RelativeStatHF_2016_down', []),
                        n_bjets_RelativeStatHF_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeStatHF_2017_up', lambda x:  getattr(x, 'bjets_30_RelativeStatHF_2017_up', []),
                        n_bjets_RelativeStatHF_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeStatHF_2017_down', lambda x:  getattr(x, 'bjets_30_RelativeStatHF_2017_down', []),
                        n_bjets_RelativeStatHF_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_SinglePionECAL_up', lambda x:  getattr(x, 'bjets_30_SinglePionECAL_up', []),
                        n_bjets_SinglePionECAL_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_SinglePionECAL_down', lambda x:  getattr(x, 'bjets_30_SinglePionECAL_down', []),
                        n_bjets_SinglePionECAL_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_SinglePionHCAL_up', lambda x:  getattr(x, 'bjets_30_SinglePionHCAL_up', []),
                        n_bjets_SinglePionHCAL_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_SinglePionHCAL_down', lambda x:  getattr(x, 'bjets_30_SinglePionHCAL_down', []),
                        n_bjets_SinglePionHCAL_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_TimePtEta_2016_up', lambda x:  getattr(x, 'bjets_30_TimePtEta_2016_up', []),
                        n_bjets_TimePtEta_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_TimePtEta_2016_down', lambda x:  getattr(x, 'bjets_30_TimePtEta_2016_down', []),
                        n_bjets_TimePtEta_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_TimePtEta_2017_up', lambda x:  getattr(x, 'bjets_30_TimePtEta_2017_up', []),
                        n_bjets_TimePtEta_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_TimePtEta_2017_down', lambda x:  getattr(x, 'bjets_30_TimePtEta_2017_down', []),
                        n_bjets_TimePtEta_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_BBEC1_up', lambda x:  getattr(x, 'bjets_30_BBEC1_up', []),
                        n_bjets_BBEC1_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_BBEC1_down', lambda x:  getattr(x, 'bjets_30_BBEC1_down', []),
                        n_bjets_BBEC1_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_BBEC1_2016_up', lambda x:  getattr(x, 'bjets_30_BBEC1_2016_up', []),
                        n_bjets_BBEC1_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_BBEC1_2016_down', lambda x:  getattr(x, 'bjets_30_BBEC1_2016_down', []),
                        n_bjets_BBEC1_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_BBEC1_2017_up', lambda x:  getattr(x, 'bjets_30_BBEC1_2017_up', []),
                        n_bjets_BBEC1_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_BBEC1_2017_down', lambda x:  getattr(x, 'bjets_30_BBEC1_2017_down', []),
                        n_bjets_BBEC1_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_EC2_up', lambda x:  getattr(x, 'bjets_30_EC2_up', []),
                        n_bjets_EC2_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_EC2_down', lambda x:  getattr(x, 'bjets_30_EC2_down', []),
                        n_bjets_EC2_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_EC2_2016_up', lambda x:  getattr(x, 'bjets_30_EC2_2016_up', []),
                        n_bjets_EC2_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_EC2_2016_down', lambda x:  getattr(x, 'bjets_30_EC2_2016_down', []),
                        n_bjets_EC2_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_EC2_2017_up', lambda x:  getattr(x, 'bjets_30_EC2_2017_up', []),
                        n_bjets_EC2_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_EC2_2017_down', lambda x:  getattr(x, 'bjets_30_EC2_2017_down', []),
                        n_bjets_EC2_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_HF_up', lambda x:  getattr(x, 'bjets_30_HF_up', []),
                        n_bjets_HF_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_HF_down', lambda x:  getattr(x, 'bjets_30_HF_down', []),
                        n_bjets_HF_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_HF_2016_up', lambda x:  getattr(x, 'bjets_30_HF_2016_up', []),
                        n_bjets_HF_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_HF_2016_down', lambda x:  getattr(x, 'bjets_30_HF_2016_down', []),
                        n_bjets_HF_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_HF_2017_up', lambda x:  getattr(x, 'bjets_30_HF_2017_up', []),
                        n_bjets_HF_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_HF_2017_down', lambda x:  getattr(x, 'bjets_30_HF_2017_down', []),
                        n_bjets_HF_2017_down = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_RelativeBal_up', lambda x:  getattr(x, 'bjets_30_RelativeBal_up', []),
                        n_bjets_RelativeBal_up = v(lambda x: len(x), int))
                       )
bjets_30_corr.append(  Block(
                        'bjets_30_RelativeBal_down', lambda x:  getattr(x, 'bjets_30_RelativeBal_down', []),
                        n_bjets_RelativeBal_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeSample_2016_up', lambda x:  getattr(x, 'bjets_30_RelativeSample_2016_up', []),
                        n_bjets_RelativeSample_2016_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2016.append(  Block(
                        'bjets_30_RelativeSample_2016_down', lambda x:  getattr(x, 'bjets_30_RelativeSample_2016_down', []),
                        n_bjets_RelativeSample_2016_down = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeSample_2017_up', lambda x:  getattr(x, 'bjets_30_RelativeSample_2017_up', []),
                        n_bjets_RelativeSample_2017_up = v(lambda x: len(x), int))
                       )
bjets_30_corr_2017.append(  Block(
                        'bjets_30_RelativeSample_2017_down', lambda x:  getattr(x, 'bjets_30_RelativeSample_2017_down', []),
                        n_bjets_RelativeSample_2017_down = v(lambda x: len(x), int))
                       )






#for i in range(len(jets_30_corr)):
#    jets_30_corr_i = jets_30_corr[i]
#    for vname, variable in jets_30_corr_i.iteritems():
        #i = 0
#        for source in redjesunc_sources_2016:
#            for unc in up_down:
#                corr_name = source + '_' + unc
                #newname = vname.replace('jets_30','jets_30_'+corr_name,1)
	        #newname = newname.replace('n_jets','n_jets_'+corr_name,1)
	        #newname = vname.replace('n_jets','n_jets_'+corr_name,1)
	        #newname = newname.replace('dijet_m','dijet_m_'+corr_name,1)
	        #newname = vname.replace('j1','j1_'+corr_name,1)
	        #newname = newname.replace('j1','j1_'+corr_name,1)
    	        #newname = newname.replace('j2','j2_'+corr_name,1)
                #newname = newname.replace('n_jets','n_jets_'+corr_name,1)
                #newname = newname.replace('dijet_m','dijet_m_'+corr_name,1)
	        #jets_30_corr_i = jets_30_corr[i]
	        #jets_30_corr_i[newname] = variable
	        #i = i + 1


for vname, variable in jets30.iteritems():
    #if vname.startswith('j1_corr'):
    #  continue
    #if vname.startswith('j2_corr'):
    #  continue
    if not vname.startswith('j'):
      continue
    newname = vname.replace('j1','b1',1)
    newname = newname.replace('j2','b2',1)
    #newname = newname.replace('dijet_m','dibjet_m',1)
    bjets[newname] = variable


electron = Block(
    'electron', lambda x: x.select_electron[0],
    pt_elec    = v(lambda x: x.pt()),
    eta_elec   = v(lambda x: x.eta()),
    phi_elec   = v(lambda x: x.phi()),
    m_elec     = v(lambda x: x.mass()),
    q_elec     = v(lambda x: x.charge()),
    iso_elec   = v(lambda x: x.iso_htt()),
)

muon = Block(
    'muon', lambda x: x.select_muon[0],
    pt_muon    = v(lambda x: x.pt()),
    eta_muon   = v(lambda x: x.eta()),
    phi_muon   = v(lambda x: x.phi()),
    m_muon     = v(lambda x: x.mass()),
    q_muon     = v(lambda x: x.charge()),
    iso_muon   = v(lambda x: x.iso_htt()),
)

dilepton = Block(
    'dilepton', lambda x: x.dileptons_sorted[0],
    m_dilep = v(lambda x: x.mass()),
    pt_emu = v(lambda x: x.pt()),
    pt_lead = v(lambda x: x.pt_lead()),
    pt_sublead = v(lambda x: x.pt_sublead()),
    eta_l1 = v(lambda x: x._l1.eta()),
    eta_l2 = v(lambda x: x._l2.eta())
)


sequence_eventcontent = [event, weights, syst, jets30, bjets]

sequence_jetcorr = []
for i in range(len(jets_30_corr)):
	sequence_jetcorr.append(jets_30_corr[i])
        sequence_jetcorr.append(bjets_30_corr[i])

sequence_jetcorr_2016 = []
for i in range(len(jets_30_corr_2016)):
	sequence_jetcorr_2016.append(jets_30_corr_2016[i])
        sequence_jetcorr_2016.append(bjets_30_corr_2016[i])

sequence_jetcorr_2017 = []
for i in range(len(jets_30_corr_2017)):
        sequence_jetcorr_2017.append(jets_30_corr_2017[i])
        sequence_jetcorr_2017.append(bjets_30_corr_2017[i])


#for jets_30_corr_i in jets_30_corr:
#       sequence_eventcontent.append(jets_30_corr_i)
#for bjets_30_corr_i in bjets_30_corr:
#       sequence_eventcontent.append(bjets_30_corr_i)


#sequence_eventcontent_2016 = sequence_eventcontent
#sequence_eventcontent_2017 = sequence_eventcontent

#for i in range(len(jets_30_corr_2016)):
#        sequence_eventcontent_2016.append(jets_30_corr_2016[i])
#        sequence_eventcontent_2016.append(bjets_30_corr_2016[i])
#for i in range(len(jets_30_corr_2017)):
#        sequence_eventcontent_2017.append(jets_30_corr_2017[i])
#        sequence_eventcontent_2017.append(bjets_30_corr_2017[i])

#sequence_jetcorr_2016 = []
#sequence_jetcorr_2017 = []



sequence_leptons = [electron, muon, dilepton]

sequence_eventcontent_2016 = sequence_eventcontent + sequence_jetcorr + sequence_jetcorr_2016 + sequence_leptons + [triggers2016]
sequence_eventcontent_2017 = sequence_eventcontent + sequence_jetcorr + sequence_jetcorr_2017 + sequence_leptons + [triggers2017]


#sequence_eventcontent_2016.append(electron)
#sequence_eventcontent_2016.append(muon)
#sequence_eventcontent_2016.append(dilepton)
#sequence_eventcontent_2016.append(triggers2016)

#sequence_eventcontent_2017.append(electron)
#sequence_eventcontent_2017.append(muon)
#sequence_eventcontent_2017.append(dilepton)
#sequence_eventcontent_2017.append(triggers2017)

common2016 = EventContent(
    #[event, weights, syst, jets30,  bjets, electron, muon, dilepton, metvars, triggers2016]
    #[event, weights, syst, jets30,  bjets, electron, muon, dilepton, triggers2016]
    sequence_eventcontent_2016
)

common2017 = EventContent(
    #[event, weights, syst, jets30,  bjets, electron, muon, dilepton, metvars, triggers2017]
    #[event, weights, syst, jets30,  bjets, electron, muon, dilepton, triggers2017]
    sequence_eventcontent_2017
)

################################################################################
#Weight Generator
################################################################################

nPU = Block(
    'pu', lambda x: x,
    pu = v(lambda x: x.nPU)
)

pileup = EventContent(
    [nPU]
)


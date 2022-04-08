from tools import *
from CMGTools.ttbar.utils.JesEnergyScaleSources import jesunc_sources
import math

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
    weight_pu = v(lambda x : getattr(x, 'puWeight', 1.)),
    weight_generator = v(lambda x : getattr(x, 'generatorWeight', 1.)),
    weight_pu_up = v(lambda x : getattr(x, 'puWeightUp',1.)),
    weight_pu_down = v(lambda x : getattr(x, 'puWeightDown',1.)),
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

for vname, variable in jets30.iteritems():
    if vname.startswith('j1_corr'):
      continue
    if vname.startswith('j2_corr'):
      continue
    if not vname.startswith('j'):
      continue
    newname = vname.replace('j1','b1',1)
    newname = newname.replace('j2','b2',1)
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
    pt_lead = v(lambda x: x.pt_lead()),
    pt_sublead = v(lambda x: x.pt_sublead()),
    eta_l1 = v(lambda x: x._l1.eta()),
    eta_l2 = v(lambda x: x._l2.eta())
)


common2016 = EventContent(
    #[event, weights, syst, jets30,  bjets, electron, muon, dilepton, metvars, triggers2016]
    [event, weights, syst, jets30,  bjets, electron, muon, dilepton, triggers2016]
)

common2017 = EventContent(
    #[event, weights, syst, jets30,  bjets, electron, muon, dilepton, metvars, triggers2017]
    [event, weights, syst, jets30,  bjets, electron, muon, dilepton, triggers2017]
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


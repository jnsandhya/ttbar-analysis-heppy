import sys,os
from optparse import OptionParser
from ROOT import TFile, TH1D, TTree

from   PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

usage = "usage: python pu_hist_gen.py [options] \n example: python pu_hist_gen.py -l CRABtest -y year"
parser = OptionParser(usage=usage)
parser.add_option("-y","--year", dest='year', default="2016", help="year on which u want to run the PU")
parser.add_option("-l","--dirc", dest='dirc', default="test", help=" dir that has output PU")
options,args = parser.parse_args()

print options

is_alternative_sample = True


if options.year == '2016':
    from CMGTools.ttbar.samples.summer16.ttbar2016            import mc_ttbar
    if is_alternative_sample:
        from CMGTools.ttbar.samples.summer16.ttbar_alternative_2016 import alt_ttbar as mc_ttbar
else: 
    from CMGTools.ttbar.samples.fall17.ttbar2017              import mc_ttbar
    if is_alternative_sample:
        from CMGTools.ttbar.samples.fall17.ttbar_alternative_2017 import alt_ttbar_more as mc_ttbar

if is_alternative_sample:
    name_alt = '_alternative'
else:
    name_alt = ''

dir_input  = "./input_files/pu/"+options.year+"/"+options.dirc+"/"
dir_output = "./output_files/pu/"+options.year+"/"
if not os.path.exists(dir_output):
    os.mkdir(dir_output)

test_dict = {}

for i in mc_ttbar:
    test_dict.setdefault(str(i.name), [])
    test_dict[str(i.name)].append('#'.join(i.dataset.split("/")))

pu_hist = []


for key,value in test_dict.items():
    infile = TFile(dir_input+key+"/NtupleProducer/tree.root")
    test_dict[key].append(infile)
    intree = infile.Get('events')
    test_dict[key].append(intree)
    pu_hist.append(TH1D(str(test_dict[key][0]),"",200,0.,200.))
    test_dict[key].append(intree.Project(str(test_dict[key][0]), "pu"))


#print test_dict

rootfile = TFile(dir_output+"pileup"+name_alt+".root", "RECREATE")
for i in range(len(pu_hist)):
    pu_hist[i].Write()

rootfile.Close()









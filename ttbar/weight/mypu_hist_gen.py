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
    from CMGTools.ttbar.samples.summer16.ttbar_alternative_2016 import alt_ttbar
else: 
    from CMGTools.ttbar.samples.fall17.ttbar2017              import mc_ttbar
    from CMGTools.ttbar.samples.fall17.ttbar_alternative_2017 import alt_ttbar


samples=[]
dir_input  = "./input_files/pu/"+options.year+"/"+options.dirc+"/"
#if options.get_files:
#    if not os.path.exists(dir_input):
#        '''
#        create the input file path
#         '''
#        print "here am I creating input directory" 
#        os.makedirs(dir_input)
#    samples=os.listdir("../../scripts/"+options.prod_label)
#    os.chdir(dir_input)
#    for i in samples:
#        os.system("cp -r ../../../../scripts/"+options.prod_label+"/"+i+" . ") 
#    os.chdir("../../")

dir_output = "./output_files/pu/"+options.year+"/"
if not os.path.exists(dir_output):
    os.mkdir(dir_output)

name_list = []
test_dict = {}
if is_alternative_sample:
    name_alt = '_alternative'
    mc_ttbar = alt_ttbar 
for i in mc_ttbar:
    #print '#'.join(i.dataset.split("/"))
    name_list.append('#'.join(i.dataset.split("/")))
    test_dict[str(i.name)]= '#'.join(i.dataset.split("/"))


pu_tree = {}
pu_hist = []


for key,value in test_dict.items():
    #print key
    #print type(key)
    pu_file =  TFile(dir_input+key+"/NtupleProducer/tree.root")
    pu_tree[key] = pu_file.Get('events')

rootfile = TFile(dir_output+"pileup.root", "RECREATE")
if is_alternative_sample:
    rootfile = TFile(dir_output+"pileup"+name_alt+".root", "RECREATE")

i=0
for key,value in test_dict.items():
    print "sample:", key
    pu_hist.append(TH1D(str(value),"",200,0.,200.))
    pu_tree[key].Project(str(value), "pu")
    print "pu hist:", value
    print "\n" 
    #print i, len(pu_tree.items())
    pu_hist[i].Write()
    i=i+1



rootfile.Close()






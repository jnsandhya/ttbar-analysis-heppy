import sys,os
from optparse import OptionParser
from ROOT import TFile, TH1D, TTree

from   PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption


parser.add_option("-i","--input",dest='input')
parser.add_option("-a","--add",dest='more')
parser.add_option("-o","--output",dest='output')

options,args = parser.parse_args()

#print options

fInput = TFile(options.input,'READ')
fInput.ls()
fMore = TFile(options.more,'READ')
fMore.ls()

fOutput = TFile(options.output,'RECREATE')
fOutput.cd()

for l in fInput.GetListOfKeys():
    h = fInput.Get(l.GetName())
    h.Write()
for l in fMore.GetListOfKeys():
    h = fMore.Get(l.GetName())
    h.Write()



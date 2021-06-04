import os
import csv

'''
import time
import datetime
import re

def convert(s):
    try:
        date = re.split('/| |:',s)
        date[2] = '20'+date[2]
        return [int(i) for i in date]
    except:
        return 0


def unixtime(l):
    try:
        date = convert(l)
        utc = datetime.datetime(date[2],date[0],date[1],date[3],date[4],date[5])
        return int(time.mktime(utc.timetuple()))
    except:
        return 0
'''
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer


class TimeAnalyzer( Analyzer ):
        
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(TimeAnalyzer, self).__init__(cfg_ana, cfg_comp, looperName)
        self.data       = self.cfg_ana.data
        self.year       = self.cfg_ana.year
        '''
        self.lumi_info = []

        if self.data == True:
            if self.year == '2016' :
                rootfname = '/'.join([os.environ["CMSSW_BASE"], 'src/CMGTools/ttbar/data/LumiData_2016.csv'])
            elif self.year == '2017' :
                rootfname = '/'.join([os.environ["CMSSW_BASE"], 'src/CMGTools/ttbar/data/LumiData_2017.csv'])

            with open(rootfname) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:
                    if len(row) == 9:
                        self.lumi_info.append(row)
                                      
        '''
   
    def process(self, event):
    
        self.readCollections(event.input)      
       
        time = event.input.eventAuxiliary().time()
        unix_time = time.unixTime()
        #inst_lumi_recorded = -99
        #inst_lumi_delivred = -99
        '''
        if self.data == True:
            for info in self.lumi_info:
                if unix_time == unixtime(info[2]):
                    inst_lumi_delivred = float(info[5])
                    inst_lumi_recorded = float(info[6])
                    break
        '''
        
        setattr(event, 'unixTime', unix_time)
        #setattr(event, 'instLumiDelivred', inst_lumi_delivred)        
        #setattr(event, 'instLumiRecorded', inst_lumi_recorded)

        if event.unixTime is None:
            raise ValueError('time cannot be None!')
        


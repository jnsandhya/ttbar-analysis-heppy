from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle

class MCWeighter(Analyzer):

    def declareHandles(self):
        super(MCWeighter, self).declareHandles()
        #self.mchandles['GenInfo'] = AutoHandle( ('generator','',''), 'GenEventInfoProduct' )
        self.mchandles['GenInfo'] = AutoHandle('generator',
                                                'GenEventInfoProduct',
                                                 mayFail=True,
                                                 fallbackLabel='source',
                                                 lazy=False )

    def beginLoop(self, setup):
        super(MCWeighter,self).beginLoop(setup)
        self.counters.addCounter('SkimReport')
        self.count = self.counters.counter('SkimReport')
        self.count.register('All Events')
        if self.cfg_comp.isMC: 
            self.count.register('Sum Weights')

    def process(self, event):
        self.count.inc('All Events')
        if self.cfg_comp.isMC: 
            self.readCollections(event.input)
	    if self.mchandles['GenInfo'].isValid():
                event.generatorWeight = self.mchandles['GenInfo'].product().weight()
	    else:
		event.generatorWeight = 0.
            self.count.inc('Sum Weights', event.generatorWeight)


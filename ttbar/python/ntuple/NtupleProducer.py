from PhysicsTools.Heppy.analyzers.core.TreeAnalyzerNumpy import TreeAnalyzerNumpy


class NtupleProducer(TreeAnalyzerNumpy):
        
    def declareVariables(self, event):
        for block in self.cfg_ana.event_content: 
            for varname, var in block.iteritems():
		if varname.find('weight_pdfas_variation')!=-1:
		    #for i in range(len(var.function(block.data_source(event)))):
		    for i in range(0, 102):
			#print(varname+'_'+str(i))
		        self.tree.var(varname+'_'+str(i), float, -99., varname+'_'+str(i), "default")
		else:
                    self.tree.var(varname, var.vtype, var.default, varname, var.storageType)

    def process(self, event):
        if hasattr(self.cfg_ana, 'skim_func') and not self.cfg_ana.skim_func(event):
            return False
	for block in self.cfg_ana.event_content: 
            data = block.data_source(event)
            for varname, var in block.iteritems():
                if (varname.find('weight_pdfas_variation')!=-1):
		    if (self.cfg_comp.isData or self.cfg_comp.name.find('WW')!=-1 or self.cfg_comp.name.find('WZ')!=-1 or self.cfg_comp.name.find('ZZ')!=-1 or self.cfg_comp.name.find('ST_t_')!=-1):
		        continue
		    for i in range(0, 102):
			try:
		            self.tree.fill(varname+'_'+str(i), var.function(data)[i])
                    	except OverflowError:
                            print 'value', var.function(data)[i], "didn't fit in var", varname
                            continue
                        except TypeError:
                            message = 'Variable {} took the type: {} \n instead of the intended type: {}'.format(
                                    varname,
                                    str(type(var.function(data)[i])),
                                    str(var)
                            )
                            raise TypeError(message)
		    #continue
                else:
		    try:
                        self.tree.fill(varname, var.function(data))
                    except OverflowError:
                        print 'value', var.function(data), "didn't fit in var", varname
                        continue
                    except TypeError:
                        message = 'Variable {} took the type: {} \n instead of the intended type: {}'.format(
			        varname,
			        str(type(var.function(data))),
			        str(var)
		        )
                        raise TypeError(message)
        self.tree.tree.Fill()

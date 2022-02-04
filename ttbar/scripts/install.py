import os

#architecture = 'slc6_amd64_gcc700'
architecture = 'slc7_amd64_gcc820'

print ''
print ' > Copy of Jet.py object with loose ID'
new_jet = './scripts/files_install/Jet.py'
old_jet = '../../PhysicsTools/Heppy/python/physicsobjects/Jet.py'
new_calib = './scripts/files_install/JetReCalibrator.py' 
old_calib = '../../PhysicsTools/Heppy/python/physicsutils/JetReCalibrator.py'
os.system('cp '+new_calib+' '+old_calib)
os.system('cp '+new_jet+' '+old_jet)



print ''
print ' > Copy of batch scripts'
new_manager = './scripts/files_install/batchmanager.py'
old_manager = '../../PhysicsTools/HeppyCore/python/utils/batchmanager.py'
new_batch = './scripts/files_install/heppy_batch.py'
old_batch = '../../../bin/'+architecture+'/heppy_batch.py'
old_hadd  = '../../../bin/'+architecture+'/heppy_hadd.py'
new_hadd  = './scripts/files_install/heppy_hadd.py'


os.system('cp '+new_manager+' '+old_manager)
os.system('cp '+new_batch+' '+old_batch)
os.system('cp '+new_hadd+' '+old_hadd)

print ''

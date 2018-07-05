import numpy as np
import numpy
import os

folder = '/home3/srallaba/projects/siri_expts/merlin/egs/voice_conversion/s2/chinese/feats/VC_scripts/postprocessed_mgc/'
os.chdir(folder)
files = sorted(os.listdir('.'))
for file in files:

 if file.endswith('.sp_ascii'):

   predicted = numpy.loadtxt(file)
   original = numpy.loadtxt('/home3/srallaba/projects/siri_expts/merlin/egs/voice_conversion/s2/chinese/feats/VC_scripts/sp/' + file)
   matrix = np.ones((513, 513))
   N = np.dot(predicted, matrix)

   M=np.dot(original, matrix)
   energy = (predicted/M) * (N)
   np.savetxt('/home3/srallaba/projects/siri_expts/merlin/egs/voice_conversion/s2/chinese/feats/VC_scripts/postprocessed_mgc/' + file, energy)

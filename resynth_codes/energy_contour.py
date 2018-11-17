import numpy as np
import numpy
import os

folder = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/warped_feats/slt_bdl/reconstruction/postprocessed_mgc/'
os.chdir(folder)
files = sorted(os.listdir('.'))
for file in files:

 if file.endswith('.sp_ascii'):

   predicted = numpy.loadtxt(file)
   original = numpy.loadtxt('/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/cmu_us_slt_arctic/feats/' + file.split('.')[0]+'.sp_ascii')
   matrix = np.ones((513, 513))
   N = np.dot(predicted, matrix)

   M=np.dot(original, matrix)
   energy = (predicted/M) * (N)
   np.savetxt('/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/warped_feats/slt_bdl/reconstruction/postprocessed_mgc/' + file, energy)

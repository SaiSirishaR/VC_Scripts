import math
import numpy as np
import os


folder ='/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/warped_feats/slt_bdl/reconstruction/valid_f0/'
source_log_f0 = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/warped_feats/slt_bdl/reconstruction/log_valid_f0/'
os.chdir(folder)
files = sorted(os.listdir('.'))
for file in files:

 if file.endswith('.f0_ascii'):
  g = open(source_log_f0 + file,'w')
  f = open(file)

  for line in f:
   line = line.split('\n')[0]
   if int(float(line)) > 0:
#    print(np.log(int(float(line))))
    g.write(str(np.log(int(float(line))))+'\n')
   else:
    g.write(str(line)+'\n')
  g.close()

import numpy as np
import numpy
import math
import os 




source_folder='/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/warped_feats/slt_bdl/reconstruction/log_valid_f0/'
new_folder = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/warped_feats/slt_bdl/reconstruction/modified_log_f0/'
k = 0
os.chdir(source_folder)
files = sorted(os.listdir('.'))
for file in files:


 f_src = open(file)

 src = []
 for line in f_src:
   line = line.split('\n')[0].strip(' ')
   src.append(line)

 src_file = open('/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/warped_feats/slt_bdl/reconstruction/src_f0.txt')

 source = []

 for line in src_file:
    line = line.split('\n')[0].strip(' ')
    source.append(line)

 f_tgt = open('/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/warped_feats/slt_bdl/reconstruction/tgt_f0.txt')

 tgt = []

 for line in f_tgt:
    line = line.split('\n')[0].strip(' ')
    tgt.append(line)

 source = np.array(source).astype(np.float)
 tgt = np.array(tgt).astype(np.float)
 src = np.array(src).astype(np.float)

 mu_src = numpy.mean(source)
# print("mean of src is", mu_src)
 mu_tgt = numpy.mean(tgt)

 sig_src = numpy.std(source)
 sig_tgt = numpy.std(tgt)

 g = open(new_folder + file,'w')
 for i in range(0,len(src)):
   
   d = sig_tgt / float(sig_src)
   dif = (src[i]) - mu_src
    
   new_f0 = d * dif + mu_tgt
 #  print("i is..", i, "new_fo is", new_f0)
   g.write(str(new_f0) + '\n')
 g.close()


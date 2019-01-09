
#!/usr/bin/python

import os, sys
import numpy as np

# Locations
data_dir = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/VC_reconstruction/predicted/'

g = open('files','w')

files = sorted(os.listdir(data_dir))

for file in files:
   
    fname = file.split('.')[0]
    #fname = fname.split('awb_')[-1]
#    print(fname)
    print("writing", fname)
    g.write(str(fname)+'\n')
g.close()





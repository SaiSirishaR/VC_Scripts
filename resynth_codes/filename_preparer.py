#!/usr/bin/python

import os, sys
import numpy as np

# Locations
data_dir = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/warped_feats/slt_bdl/reconstruction/final_f0/'

g = open('files','w')

files = sorted(os.listdir(data_dir))

for file in files:
   
    fname = file.split('.')[0]
    print("writing", fname)
    g.write(str(fname)+'\n')
g.close()






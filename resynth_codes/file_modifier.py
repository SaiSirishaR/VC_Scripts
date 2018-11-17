import os, numpy
import numpy as np

data_dir = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/cmu_us_slt_arctic/feats/mgc/'
os.chdir(data_dir)
files = sorted(os.listdir(data_dir))

for file in files:
 feats = np.loadtxt(file)
 np.savetxt(data_dir+file, feats)

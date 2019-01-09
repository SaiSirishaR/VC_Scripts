import os, numpy
import numpy as np

data_dir = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/lf0_converted/'
os.chdir(data_dir)
files = sorted(os.listdir(data_dir))

for file in files:
 feats = np.loadtxt(file)
 np.savetxt(data_dir+file, feats)


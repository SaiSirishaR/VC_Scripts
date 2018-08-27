#!/usr/bin/python

import os, sys
import numpy 
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

aligned_folder = '/home/siri/Documents/Projects/VC_expts/Data/slt_bdl/output_full/'

src_files=[]
tgt_files = []

def align(src,tgt):

   f = numpy.loadtxt( '/home/siri/Documents/Projects/VC_expts/Data/slt_bdl/slt/Train/' + src)
   print("processing", src,"from source files")
   g = numpy.loadtxt( '/home/siri/Documents/Projects/VC_expts/Data/slt_bdl/bdl/Train/'+tgt)
  
   h = open(aligned_folder  + tgt.split('.')[0] + '_aligned' + '.coeffs','w')
   distance, path = fastdtw(f,g, dist=euclidean)
   print("writing aligned files for ", tgt)

   for i in range(0,len(path)):
    for kp in range(0,len(g[path[i][1]])):
    
     h.write(str((g[path[i][1]][kp]))+' ')
    h.write('\n')
   h.close()

    
def main():

# Load the source files

  source_folder=  '/home/siri/Documents/Projects/VC_expts/Data/slt_bdl/slt/Train/'
  
  os.chdir(source_folder)
  files = sorted(os.listdir('.'))
  for file in files:
    src_files.append(file)
 
# Load the target files

  target_folder = '/home/siri/Documents/Projects/VC_expts/Data/slt_bdl/bdl/Train/'


  os.chdir(target_folder)
  gfiles = sorted(os.listdir('.'))
  for gfile in gfiles:
    tgt_files.append(gfile)
  

  for i in range(0,len(src_files)):
   print("file is", i)
   align(src_files[i], tgt_files[i])


if __name__ == '__main__':
     main()

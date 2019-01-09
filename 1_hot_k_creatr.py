#!/usr/bin/python

import numpy, os
import numpy as np


source_folder=  '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_NAACL/valid_input/'
target_folder='/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_NAACL/1_hot_vectors_valid/'
os.chdir(source_folder)
files = sorted(os.listdir('.'))
for file in files:
 #if file.startswith('awb'):
  print("processing file...", file)
  g = open(target_folder + file.split('.')[0]+'.txt', 'w')
  f = open(file)

  for line in f:
   #line = line.split('\n')[0].split(' ')
#   print("line is:", line)#print(int(float(line[0])))
   for i in range(0,6):
     if i==5:
       g.write(str('1')+ ' ')

     else:
       g.write(str('0')+' ')
   g.write('\n')
  g.close()


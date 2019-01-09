import math 
import os


source_folder='/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/VC_reconstruction/predicted/'
new_folder = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/VC_reconstruction/postprocessed_mgc/'
os.chdir(source_folder)
files = sorted(os.listdir('.'))

for file in files:
 if file.startswith('SM4'):
  src = []
  f_src = open('/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/deltas_full/mgc/'+file.split('.')[0] + '.mgc')
  for line in f_src:
   line = line.split('\n')[0]
   src.append(line)

  f_array =[]
  f0 = open('/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/lf0/SM4_converted/f0/' +file.split('.')[0] + '.f0')
  for line in f0:
   line = line.split('\n')[0]
   f_array.append(line)


  p_array = []
  pred = open(file)
  for line in pred:
    line = line.split('\n')[0]
    p_array.append(line)


  g = open(new_folder + file.split('.')[0] + '.mgc', 'w')

  for i in range(0,len(f_array)):
#    if (f_array[i]) == -1e+10:
   if not int(float(f_array[i]))> 0:
#      print("s",f_array[i])
      g.write(str(src[i]) + '\n')
   else:
      g.write(str(p_array[i])+'\n')

  g.close()

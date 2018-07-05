import math 
import os


source_folder='/home3/srallaba/projects/siri_expts/merlin/egs/voice_conversion/s2/chinese/feats/VC_scripts/test_modified/'
new_folder = '/home3/srallaba/projects/siri_expts/merlin/egs/voice_conversion/s2/chinese/feats/VC_scripts/postprocessed_mgc/'
os.chdir(source_folder)
files = sorted(os.listdir('.'))
for file in files:
 #if file.endswith('.mgc_ascii'):
  print("file is..", file)
  src = []
  f_src = open('/home3/srallaba/projects/siri_expts/merlin/egs/voice_conversion/s2/chinese/feats/female/mgc/'+file.split('.')[0] + '.mgc_ascii')
  for line in f_src:
   line = line.split('\n')[0]
   src.append(line)

  f_array =[]
  f0 = open('/home3/srallaba/projects/siri_expts/merlin/egs/voice_conversion/s2/chinese/feats/female/f0/' + file.split('.')[0] + '.f0_ascii')
  for line in f0:
   line = line.split('\n')[0]
   f_array.append(line)


  p_array = []
  pred = open(file)
  for line in pred:
    line = line.split('\n')[0]
    p_array.append(line)


  g = open(new_folder + file.split('.')[0] + '.mgc_ascii', 'w')

  for i in range(0,len(f_array)):
#    if (f_array[i]) == -1e+10:
   if not int(float(f_array[i]))> 0:
#      print("s",f_array[i])
      g.write(str(src[i]) + '\n')
   else:
      g.write(str(p_array[i])+'\n')

  g.close()

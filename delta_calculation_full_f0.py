import numpy
import os, sys
import numpy as np





def delta(input, file):
  g = open('/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/deltas/lf0/'+file,'w')

  for i in range(0,len(input)):
   deltas=[]
   deltas = str(str((input[i])/2) )
   g.write(str(deltas))
   g.write('\n')   
  g.close()




def doubledelta(input, file):
  g = open('/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/doubledeltas/lf0/'+file,'w')

  for i in range(0,len(input)):
   doubledeltas=[]
   doubledeltas = str(str((input[i])/2) )
   g.write(str(doubledeltas))
   g.write('\n')
  g.close()



def main():

 # delta calculation

 data_dir = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/lf0_converted/'
 os.chdir(data_dir)
 files = sorted(os.listdir(data_dir))

 for file in files:
  if file.endswith('.lf0'):
   print("processing...", file, "for deltas")
   fname = file.split('.')[0]

   input = numpy.loadtxt(file)
   deltas= delta(input, file)
 print("calculated deltas")

 data_dir = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/deltas/lf0/'
 os.chdir(data_dir)
 files = sorted(os.listdir(data_dir))

 for file in files:
  if file.endswith('.lf0'):
   print("processing...", file, "for doubledeltas")
   fname = file.split('.')[0]

   input = numpy.loadtxt(file)
   doubledeltas= doubledelta(input, file)
 print("calculated deouble deltas")

if __name__ =='__main__':
 main()


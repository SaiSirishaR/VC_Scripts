import numpy
import os, sys
import numpy as np





def delta(input, file):
  g = open('/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/deltas/mgc/'+file,'w')

  for i in range(0,len(input)):
   deltas=[]
   for j in range(0,len(input[i])):
 
    if j==0:
     deltas.append((input[i][j+1])/2)
 
    elif j==59:#59 4
     deltas.append(-input[0][58]/2)#58 3

    else:
     deltas.append((input[i][j+1]-input[i][j-1])/2)

   for ii in range(0,len(deltas)):
    g.write(str(deltas[ii]) + ' ')
   g.write('\n')
  g.close()

def doubledelta(input, file):
  g = open('/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/doubledeltas/mgc/'+file,'w')

  for i in range(0,len(input)):
   doubledeltas=[]
   for j in range(0,len(input[i])):

    if j==0:
     doubledeltas.append((input[i][j+1])/2)

    elif j==59:#59 4
     doubledeltas.append(-input[0][58]/2)#58 3

    else:
     doubledeltas.append((input[i][j+1]-input[i][j-1])/2)

   for ii in range(0,len(doubledeltas)):
    g.write(str(doubledeltas[ii]) + ' ')
   g.write('\n')
  g.close()




def main():

 # delta calculation

 data_dir = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/mgc_converted/'
 os.chdir(data_dir)
 files = sorted(os.listdir(data_dir))

 for file in files:
  if file.endswith('.mgc'):
   print("processing...", file, "for deltas")
   fname = file.split('.')[0]

   input = numpy.loadtxt(file)
   deltas= delta(input, file)


# double delta

 delta_dir = '/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/deltas/mgc/'
 os.chdir(delta_dir)
 files = sorted(os.listdir(delta_dir))

 for file in files:
  if file.endswith('.mgc'):
   print("processing...", file, "for double deltas")
   fname = file.split('.')[0]

   input = numpy.loadtxt('/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/deltas/mgc/'+ file)
   doubledeltas= doubledelta(input, file)


if __name__ =='__main__':
 main()


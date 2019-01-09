#!/bin/bash
folder1="/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/valid_input/"
folder2="/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/lf0_converted"
folder3="/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/VC_reconstruction/src_log_f0"
#mkdir $new_folder
cd $folder1
for file in *;
do
          echo $file
          fbname=$(basename "$file" .lab)          
          cp -r  $folder2/$fbname.lf0 $folder3/$fbname.lf0
 
done


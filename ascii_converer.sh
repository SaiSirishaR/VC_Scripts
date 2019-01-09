#!/bin/bash

folder="/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/lf0/SM4/"
new_folder="/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/lf0/SM4_converted"

mkdir $new_folder
cd $folder
for file in *;
do
          echo $file 
          #$SPTKDIR/bin/x2x +fa711 $file > $new_folder/$file
          $SPTKDIR/bin/x2x +fa1 $file > $new_folder/$file
done


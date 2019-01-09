#!/bin/bash
folder1="/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/deltas_full/lf0"
folder2="/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/deltas_full/mgc"
folder3="/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/deltas_full/bap"
folder4="/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/expt_2jan_2019/jan6_expts/ss_dnn/data/deltas_full/feats"
#mkdir $new_folder
cd $folder1
for file in *;
do
          echo $file
          fbname=$(basename "$file" .lf0)          
          paste $folder1/$file $folder2/$fbname.mgc $folder3/$fbname.bap  > $folder4/$fbname.coeffs
done


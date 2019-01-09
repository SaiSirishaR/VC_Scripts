#!/bin/bash
folder="/home/siri/Documents/Projects/NUS_projects/vc_arctic_data/Project_independent_vc/intermediate_network/VC_reconstruction/predicted/" #change
#new_folder="/home/siri/Documents/Projects/NUS_projects/TTS-Male-BC2010text/wav_modified/"

mkdir $new_folder
cd $folder
for file in *;
do
          echo $file
          fbname=$(basename "$file" .mgc_ascii.mgc_ascii) #chnage
          mv $file $fbname.mgc_ascii   #chnage
done


Steps for the current framework

Average voice generation:

1)use run.sh to extract the features
modify the run.sh accordingly for feature extraction and signal reconstruction

command for feature extrcation ---> sh do_world wav_to_ccoeffs files
comment the second line in run.sh while doing the feature extraction

do_world --> main code
wav_to_ccoeffs --> argument for feature extraction
files --> a txt file with list of files for which feature extraction is being done

Change the path in do_world to indicate wav folder directory and the features directory

2) Training and testing with auto_encoder.py
Modify the file paths

3) Signal reconstruction

i) f0 tranfromation using f0_modifier_full.py
ii) postprocessing on MGCs in the silence regions --> post_processing_full.py
iii) Energy preservation --> energy_contour.py
iv) uncomment the second line in run.sh and modify the paths for f0,mgc,ap(after transformed), comment the 1st line in run.sh and run it

Parallel conversion:

1) Repeat the feature extraction steps but change the wav folder to the avearge voice(previously synthesized speech)
2) train_dnn.py (chnage the accordingly to test on parallel and cross-lingual data)
Modify the file paths

3) reconstruction


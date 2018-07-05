#!/usr/bin/python

import os, sys
import numpy as np
import soundfile as sf
import pyworld as pw

wav_file = sys.argv[1]
f0_file = sys.argv[2]
sp_file = sys.argv[3]
ap_file = sys.argv[4]

x, fs = sf.read(wav_file)
f0, sp, ap = pw.wav2world(x, fs) 
np.savetxt(f0_file, f0)
np.savetxt(sp_file, sp)    
np.savetxt(ap_file, ap)    

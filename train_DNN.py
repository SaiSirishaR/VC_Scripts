#!/usr/bin/python

import numpy as np
import numpy
import keras
from keras.layers import Input, Dense, Activation, BatchNormalization
from keras.constraints import maxnorm
from keras.layers.core import Dropout
from keras.optimizers import SGD
from keras.models import Model, Sequential
import numpy as np
from keras.models import load_model
import os,sys
from sklearn import preprocessing
import pickle, logging
from keras.callbacks import *


inp_dim=60
out_dim = 60
encoding_dim = 512


test_dir = # path to te prediction folder

if not os.path.exists(test_dir):
   os.makedirs(test_dir)
#   os.makedirs(resynth_dir)

input_files = [filename for filename in sorted(os.listdir('/home3/srallaba/projects/siri_expts/input_full/'))]
output_files = [filename for filename in sorted(os.listdir('/home3/srallaba/projects/siri_expts/output_full/'))]
valid_input_files = [filename for filename in sorted(os.listdir('/home3/srallaba/projects/siri_expts/valid_input/'))]
valid_output_files = [filename for filename in sorted(os.listdir('/home3/srallaba/projects/siri_expts/valid_output/'))]



train_input = []
train_output = []
valid_input = []
valid_output = []
valid_files = []

g = open('valid_files','w')

# Load validation data

for i, (valid_input_file, valid_output_file) in enumerate(zip(valid_input_files, valid_output_files)):

      A = np.loadtxt('/home3/srallaba/projects/siri_expts/valid_input/' + valid_input_file)
      i_l = len(A)
      B = np.loadtxt('/home3/srallaba/projects/siri_expts/valid_output/' + valid_output_file) 
      o_l = len(B)
      if i_l == o_l:
         g.write(valid_input_file.split('.')[0] + '\n')
         valid_input.append(A)
         valid_output.append(B)
         valid_files.append(valid_input_file)
g.close()

# Load the training data

for i, (input_file, output_file) in enumerate(zip(input_files, output_files)):
      A = np.loadtxt('/home3/srallaba/projects/siri_expts/input_full/' + input_file) 
      i_l = len(A) 
      B = np.loadtxt('/home3/srallaba/projects/siri_expts/output_full/' + output_file) 
      o_l = len(B)
      
      if i_l == o_l:
         for (a,b) in zip(A,B):
            train_input.append(a)
            train_output.append(b)      
      else:
         print("Discarding ", input_file)    


train_input = np.array(train_input)
train_output = np.array(train_output)
#logfile_name=exp_dir + '/log/log'
logfile_name='log'

class LoggingCallback(Callback):
    """Callback that logs message at end of epoch.
    """
    def __init__(self, print_fcn="print"):
        Callback.__init__(self)
        self.print_fcn = print_fcn

    def on_epoch_end(self, epoch, logs={}):
        pass
        # If  first epoch, remove the log file
        if epoch == 0:
            g = open(logfile_name,'w')
            g.close()

        # Log the progress
        msg = "{Epoch: %i} %s" % (epoch, ", ".join("%s: %f" % (k, v) for k, v in logs.items()))
        self.print_fcn(msg)
        with open(logfile_name,'a') as g:
            g.write(msg + '\n')
        #test_model(self.model,input_scaler,output_scaler, epoch)
        
        #Save the model every 5 epochs
        #if epoch % 3 == 1 and save_model:
        #     print self.model
        #     self.model.save(exp_name + '/models/mvp.h5')


def valid_model():
   # Test each file
   for (inp, out, fname) in zip(valid_input, valid_output, valid_files):
       inp = input_scaler.transform(inp)
       pred = model.predict(inp)
       pred = output_scaler.inverse_transform(pred)
       np.savetxt(test_dir + '/' + fname, pred)
#       np.savetxt(resynth_dir + '/' + fname, out)  


input_scaler = preprocessing.StandardScaler().fit(train_input)
output_scaler = preprocessing.StandardScaler().fit(train_output)
train_input = input_scaler.transform(train_input)
train_output = output_scaler.transform(train_output)

def train_model():

   global model
   # Create the model	
   model = Sequential()

   # INPUT LAYER
   model.add(Dropout(0.0, input_shape=(inp_dim,)))
   model.add(Dense(inp_dim,activation='selu'))

   # HIDDEN 1
   model.add(Dense(encoding_dim,  activation='selu'))
   #model.add(Dropout(0.2))

   # HIDDEN 2
   model.add(Dense(encoding_dim,  activation='selu'))
   #model.add(Dropout(0.2))

   # HIDDEN 3
   model.add(Dense(encoding_dim,  activation='selu'))


   # HIDDEN 4
   model.add(Dense(encoding_dim,  activation='selu'))


   model.add(Dense(out_dim,  activation='selu'))

   # Compile the model
   sgd = SGD(lr=0.1, momentum=0.2, decay=1e-6, nesterov=False)
   model.compile(optimizer=sgd, loss='mse')
   model.summary()
   model.fit(train_input,train_output,epochs=30, batch_size=32, shuffle=True,callbacks=[LoggingCallback(logging.info)])

print("input shape is ------------------------------------------------------------------------------>",numpy.shape(train_input))
train_model()
valid_model()

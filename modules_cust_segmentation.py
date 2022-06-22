# -*- coding: utf-8 -*-
"""modules_cust_segmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TEW4IZa5v06KHrUgZL8VPDtzhxcsnpLf
"""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from tensorflow.keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,BatchNormalization

class CramersV():

    def cramers_corrected_stat(confusion_matrix):
      """ calculate Cramers V statistic for categorial-categorial association.
        uses correction from Bergsma and Wicher, 
        Journal of the Korean Statistical Society 42 (2013): 323-328
      """
      chi2 = ss.chi2_contingency(confusion_matrix)[0]
      n = confusion_matrix.sum()
      phi2 = chi2/n
      r,k = confusion_matrix.shape
      phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))    
      rcorr = r - ((r-1)**2)/(n-1)
      kcorr = k - ((k-1)**2)/(n-1)

      return np.sqrt(phi2corr / min( (kcorr-1), (rcorr-1)))

class ModelCreation():
    def __init__(self):
        pass
    
    def simple_lstm_layer(self,nb_features,nb_classes,
                          num_node=128,drop_rate=0.3,output_node=1):      
        
      model = Sequential()
      model.add(Input(shape=nb_features))
      model.add(Dense(num_node,activation='relu',name='Hidden_Layer1'))
      model.add(BatchNormalization())
      model.add(Dropout(drop_rate))
      model.add(Dense(num_node,activation='relu',name='Hidden_Layer2'))
      model.add(BatchNormalization())
      model.add(Dropout(drop_rate))
      model.add(Dense(nb_classes,activation='softmax',name='Output_Layer'))
      model.summary()

      return model

class model_evaluation():
    def __init__(self):
        pass

    def plot_graph(self,hist):

      plt.figure()
      plt.plot(hist.history['acc'])
      plt.plot(hist.history['val_acc'])
      plt.legend(['Training ACC','Validation ACC'])
      plt.title('Metrics')
      plt.show()
    
      plt.figure()
      plt.plot(hist.history['loss'])
      plt.plot(hist.history['val_loss'])
      plt.legend(['Training Loss','Validation Loss'])
      plt.title('Loss')
      plt.show()
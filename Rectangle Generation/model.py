# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:38:45 2019

@author: vinayver
"""

from random import random
from matplotlib import pyplot
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM,Dense




# generate a rectangle with random width and height
def random_rectangle():
    rec = list()
    width,height = random(),random()
    rec.append([0.0,0.0])
    rec.append([width,0.0])
    rec.append([width,height])
    rec.append([0.0,height])
    return rec

rec = random_rectangle()
print(rec)

# plot a rectangle
def plot_rectangle(rec):
    #close the rectangle path
    rec.append(rec[0])
    #define the path
    codes =  [Path.MOVETO,Path.LINETO,Path.LINETO,
              Path.LINETO,Path.CLOSEPOLY]
    path = Path(rec,codes)
    axis = pyplot.gca()
    patch = PathPatch(path)
    axis.add_patch(patch)
    axis.set_xlim(-0.1,1.1)
    axis.set_ylim(-0.1,1.1)
    pyplot.show()


plot_rectangle(rec)  
    
def generate_sequences():
    rec = random_rectangle()
    X,y = list(),list()
    for i in range(1,len(rec)):
        X.append(rec[i-1])
        y.append(rec[i])
        
    X = np.array(X)
    y = np.array(y)
    X =  X.reshape(X.shape[0],1,2)
    return X,y

X,y = generate_sequences()

for i in range(X.shape[0]):
    print(X[i], '=>' , y[i])
        


model =Sequential()
model.add(LSTM(units=10,input_shape=(1,2),return_sequences=True))
model.add(LSTM(20))
model.add(Dense(units=2,activation='linear'))
model.compile(loss='mae',optimizer='adam')
model.summary()




samples = [100,500,1000,1500,10000,20000,30000]

# fit model
for sample in samples:
    for i in range(sample):
        X, y = generate_sequences()
        model.fit(X, y, epochs=1, verbose=2, shuffle=False)
      
    filename = 'model-{}-samples.h5'.format(sample)
    model.save(filename)
    BL = np.array([[0.0,0.0]])
    BR = model.predict(BL.reshape(BL.shape[0],1,2))
    TR = model.predict(BR.reshape(BL.shape[0],1,2))
    TL = model.predict(TR.reshape(BL.shape[0],1,2))
    
    rec = np.array([BL[0],BR[0],TR[0],TL[0],BL[0]])
    
    codes =  [Path.MOVETO,Path.LINETO,Path.LINETO,
                  Path.LINETO,Path.CLOSEPOLY]
    
    path = Path(rec,codes)
    axis = pyplot.gca()
    patch = PathPatch(path)
    axis.add_patch(patch)
    axis.set_xlim(-0.1,1.1)
    axis.set_ylim(-0.1,1.1)
    pyplot.show()
    
    

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 02:05:36 2018

@author: KoI
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

# read mnist data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("x_train.shape={}, y_train.shape={}".format(x_train.shape, y_train.shape))
print("x_test.shape={}, y_test.shape={}".format(x_test.shape, y_test.shape))

# normalize input data, 0 < data < 1
def normalize_input(input_train):
    return input_train.reshape(input_train.shape[0], 28, 28, 1).astype('float64') / 255

# one-hot encoding, 0 0 0 0 1 0 0 0 0 0 (?)
def normalize_output(output):
    return np_utils.to_categorical(output)

x_train = normalize_input(x_train)
x_test = normalize_input(x_test)
y_train = normalize_output(y_train)
y_test = normalize_output(y_test)

# build CNN model
model = Sequential()
# add layer 1
model.add(
        Conv2D(filters = 16, # the number of output filters
               kernel_size = (5, 5), # the width and height of the 2D convolution window
               padding = 'same', # not changing data shape
               input_shape = (28, 28, 1),
               activation = 'relu'
               )
        )
# add pool 1
model.add(
        MaxPooling2D(
                pool_size = (2, 2)
                )
        )     
# add layer 2
model.add(
        Conv2D(filters = 36,
               kernel_size = (5, 5),
               padding = 'same',
               input_shape = (28, 28, 1),
               activation = 'relu'
               )
        )
# add pool 2        
model.add(
        MaxPooling2D(
                pool_size = (2, 2)
                )
        )
#add dropout layer
model.add(Dropout(rate = 0.25))
model.add(Flatten())
# add hidden layer 1
model.add(
    Dense(
        units = 128,
        activation = 'relu',
        kernel_initializer = 'normal',
        bias_initializer = 'normal'
    )
)
# add hidden layer 2
model.add(
    Dense(
        units = 10,
        activation = 'softmax',
        kernel_initializer = 'normal',
        bias_initializer = 'normal'
    )
)
print(model.summary(), '\n')

# definite training method
model.compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['accuracy']
)

# start training
train_history = model.fit(
        x = x_train,
        y = y_train, 
        validation_split = 0.2,  
        epochs = 1, 
        batch_size = 300, 
        verbose = 1
        )

# show train history
def show_train_history(train_history, train, validation):  
    plt.plot(train_history.history[train])  
    plt.plot(train_history.history[validation])  
    plt.title('Train History')  
    plt.ylabel(train)  
    plt.xlabel('Epoch')  
    plt.legend(['train', 'validation'], loc='upper left')  
    plt.show()

show_train_history(train_history, 'acc', 'val_acc')
show_train_history(train_history, 'loss', 'val_loss')

# accuracy
print("Evaluating:")
scores = model.evaluate(x_test, y_test)  
print("Accuracy of testing data = {:2.1f}%".format(scores[1]*100.0))  

# predicting
prediction = model.predict_classes(x_test)

# confusing matrix
#print(pd.crosstab(y_test, prediction, colnames=['predict'], rownames=['label']), '\n')


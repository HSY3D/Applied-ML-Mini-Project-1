# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:26:38 2015

@author: hannansyed
"""
import numpy as np 
from numpy import genfromtxt

data_size = 39644
training_set_size = 30000

def main():
    raw_data = getData('OnlineNewsPopularity/OnlineNewsPopularity.csv')
    linearRegression(raw_data)
    gradientDescent(raw_data)
  
def linearRegression(raw_data):
    global training_set_size
    #Remove the first row and first two columns    
    raw_data = raw_data[1:,]
    raw_data = np.delete(raw_data, np.s_[0:2], 1)
    #Get the X values and Y Values
    X = getXValues(raw_data)
    Y = getYValues(raw_data)
    #Training Set & TestSet
    XTrainingSet = X[0:training_set_size, :]
    YTrainingSet = Y[0:training_set_size, :]
    XTestSet = X[training_set_size:, :]
    YTestSet = Y[training_set_size:, :]
    #Add 1s to XTest and XTraining
    XTrainingSet = addOnes(XTrainingSet, training_set_size)
    XTestSet = addOnes(XTestSet, data_size-training_set_size)
    
    #Caclulate weights
    weights = getWeights2(XTrainingSet, YTrainingSet, training_set_size)  
    #Calculate Error
    error = getError(XTestSet, YTestSet, weights, data_size-training_set_size)
    print error    

def gradientDescent(raw_data):
    global data_size
    global training_set_size
    #Remove the first row and first two columns    
    raw_data = raw_data[1:,]
    raw_data = np.delete(raw_data, np.s_[0:2], 1)
    #Get the X values and Y Values
    X = getXValues(raw_data)
    Y = getYValues(raw_data)
    #Training Set & TestSet
    XTrainingSet = X[0:training_set_size, :]
    YTrainingSet = Y[0:training_set_size, :]
    XTestSet = X[training_set_size:, :]
    YTestSet = Y[training_set_size:, :]
    a = 0.05
    w_k = np.ones((58,), dtype=np.int)
    w_k1 = w_k - a*gradientStep(XTrainingSet,YTrainingSet,w_k)    
    while (getError(XTrainingSet, YTrainingSet, abs(w_k1-w_k), training_set_size) < 252034158.7):
        w_k = w_k1        
        w_k1 = w_k - a*gradientStep(XTrainingSet,YTrainingSet,w_k) 
    print w_k1
    
############## HELPER FUNCTIONS ##############
def gradientStep(X,Y,w):
    XtX_w = np.dot(np.dot(X.T, X), w)
    Xt_Y = np.dot(X.T,Y)
    return 2*(XtX_w-Xt_Y)
    
    
def addOnes(X, setSize):
    #New column of 1s
    ones = np.ones((setSize,), dtype=np.int)
    #Append column to X
    X = np.column_stack((X, ones)) 
    return X
    
def getError(XTest, YTest, w, setSize):
    #Transpose X and multiply X^tX
    Ypredict = np.dot(XTest,w)
    #Caclulate Error
    return np.mean((YTest - Ypredict)**2)
    
def getWeights2(X, Y, setSize):
    #Transpose X and multiply X^tX
    Xt = np.transpose(X)
    Xt_X = np.dot(Xt,X)
    Xt_Y = np.dot(Xt,Y)
    return np.linalg.lstsq(Xt_X, Xt_Y)[0]
    
def getWeights(X, Y, setSize):
    #New column of 1s
    ones = np.ones((setSize,), dtype=np.int)
    #Append column to X
    X = np.column_stack((X, ones)) 
    #X = np.concatenate((X,ones), axis = 1)
    #Transpose X and multiply X^tX
    Xt = np.transpose(X)
    Xt_X = np.dot(Xt,X)
    #Take (X^tX)^-1
    Xt_X_inverse = np.linalg.inv(Xt_X)
    #Multiply X^tY
    Xt_Y = np.dot(Xt,Y)
    #Get weights
    return np.dot(Xt_X_inverse,Xt_Y)    

def getYValues(data):
    #Save the Y values
    return data.take([-1], axis = 1) 
 
def getXValues(data):
    #Remove the y-column 
    return np.delete(data, -1, 1)  
  
def getData(url):
    #Get the data from the CVS file into an array    
    return genfromtxt(url, delimiter=',')
    
main()
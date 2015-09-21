# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:26:38 2015

@author: hannansyed
"""
import numpy as np 
from numpy import genfromtxt

data_size = 39644
training_set_size = 20000

def main():
    raw_data = getData('OnlineNewsPopularity/OnlineNewsPopularity.csv')
    linearRegression(raw_data)
  
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
    #Caclulate weights
    weights = getWeights(XTrainingSet, YTrainingSet, training_set_size)    
    #print weights    
    #Calculate Error
    print getError(XTestSet, YTestSet, weights, data_size-training_set_size)
    #print YPredict
    

    
############## HELPER FUNCTIONS ##############
def getError(X, YTest, w, setSize):
    #New columns of 1s
    ones = np.ones((setSize,), dtype = np.int)
    #Append columns to X
    X = np.column_stack((X, ones))
    #Transpose X and multiply X^tX
    Ypredict = np.dot(X,w)
    #Caclulate Error
    return np.mean((YTest - Ypredict)**2)
    
    
def getWeights(X, Y, setSize):
    #New column of 1s
    ones = np.ones((setSize,), dtype=np.int)
    #Append column to X
    X = np.column_stack((X, ones))   
    #Transpose X and multiply X^tX
    Xt = X.T
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
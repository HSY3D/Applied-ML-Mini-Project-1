import numpy as np 
from numpy import genfromtxt



def getYValues(data):
    #Remove the descriptor row
    data = data[1:,]    
    
    #Save the Y values
    y_data = data.take([-1], axis = 1)
    
    return y_data
    
def getXValues(data):
    #Clean the non-predictive columns, and remove the descriptor row
    data = data[1:,]
    data = np.delete(data, np.s_[0:2], 1)
    
    #Clean the y-column 
    data = np.delete(data, -1, 1)
    
    return data
    
def getWeights(X, Y):
    #New column of 1s
    ones = np.ones((39644,), dtype=np.int)
    
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
    w = np.dot(Xt_X_inverse,Xt_Y)
    
    return w
    
def getError(X, w):
    #New columns of 1s
    ones = np.ones((39644,), dtype = np.int)
    
    #Append columns to X
    X = np.column_stack((X, ones))
    
    #Transpose X and multiply X^tX
    Ypredict = np.dot(X,w)
    Ytest = X
    
    Err = np.mean((Ypredict - Ytest)**2)
    
    print Err
    
    
def main():
    #Get the data from the CVS file into an array    
    data = genfromtxt('OnlineNewsPopularity/OnlineNewsPopularity.csv', delimiter=',')
    y_Values = getYValues(data)
    x_Values = getXValues(data)
    weights = getWeights(x_Values,y_Values)
    getError(x_Values, weights)
    
    #print x_Values.shape
    #print y_Values
    
    
    
main()
    


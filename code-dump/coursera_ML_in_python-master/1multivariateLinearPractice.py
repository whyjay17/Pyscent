# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 18:20:14 2017

@author: YJ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.getcwd() + '\ex1data2.txt'
data = pd.read_csv(path, header=None, names=['Size','Bedrooms','Price'])
data.head()

def featureScaling(data):
    data = (data - data.mean()) / data.std()
    return data

data = featureScaling(data)

# modify implementation of linear regression to handle more than 1 dependent variable

def costFunction(X, y, theta):
    m = len(X)
    #J = (1/2*m) * (np.sum( (hypo(X,theta) - y) ** 2))
    J = np.sum((X.dot(theta)-y)**2)/2/m
    return J
    
def gradientDescent(X, y, theta, alpha, iters):
    m = len(X)
    costHistory = [0] * iters
    
    for i in range(iters):
        # 1) calculate hypothesis[97x1] 
        hypothesis = X.dot(theta) # or X * theta.T    
        
        # 2) calculate loss[97x1] (element-wise subtration)
        loss = hypothesis - y
        
        # 3) calculate gradient[2x1] = X'[2x97] * loss[97x1]
        gradient = X.T.dot(loss) / m
        
        # 4) update parameter theta[2x1] after element-wise subtraction multiplied by a scalar
        theta = theta - alpha * gradient
        
        # 5) find cost by using costFunction
        cost = costFunction(X, y, theta)
        costHistory[i] = cost
    
    return theta, costHistory

alpha = 0.02
iters = 1500
data.insert(0, 'Ones', 1)
cols = data.shape[1]  
X2 = data.iloc[:,0:cols-1]  
y2 = data.iloc[:,cols-1:cols]

X = np.array(X2)
y = np.array(y2).flatten()
theta = np.array([0, 0, 0])

newTheta, c = gradientDescent(X, y, theta, alpha, iters)

print("cost : ", c[iters-1])

fig, ax = plt.subplots(figsize=(12,8))  
ax.plot(np.arange(iters), c, 'r')  
ax.set_xlabel('Iterations')  
ax.set_ylabel('Cost')  
ax.set_title('Error vs. Training Epoch')  

bestFitX = np.linspace(0, 25, 20)
bestFity = [t[1] + t[0] * xx for xx in bestFitX]
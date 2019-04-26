# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 17:07:16 2017

@author: YJ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn import linear_model

path = os.getcwd() + '\ex1data2.txt'
data2 = pd.read_csv(path, header=None, names=['Size','Bedrooms','Price'])
data2.head()

# feature normalization

data2 = (data2 - data2.mean()) / data2.std()
data2.head()

# no change needed since they use matrix operations

def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))


def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    params = int(theta.ravel().shape[1]) #flattens
    cost = np.zeros(iters)

    for i in range(iters):
        err = (X * theta.T) - y
        
        for j in range(params):
            term = np.multiply(err, X[:,j])
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))
        
        theta = temp
        cost[i] = computeCost(X, y, theta)
    
    return theta, cost

data2.insert(0, 'Ones', 1)

cols = data2.shape[1]
X2 = data2.iloc[:, 0:cols-1]
y2 = data2.iloc[:, cols-1:cols]

X2 = np.matrix(X2.values)
y2 = np.matrix(y2.values)

theta2 = np.matrix(np.array([0,0,0]))
alpha = 0.01
iters = 1000

g2, cost2 = gradientDescent(X2, y2, theta2, alpha, iters)

print(computeCost(X2, y2, g2))

fig, ax = plt.subplots(figsize=(12,8))  
ax.plot(np.arange(iters), cost2, 'r')  
ax.set_xlabel('Iterations')  
ax.set_ylabel('Cost')  
ax.set_title('Error vs. Training Epoch')  

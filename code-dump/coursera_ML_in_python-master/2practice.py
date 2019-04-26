# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 16:48:19 2017

@author: YJ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('ex1data1.txt', names = ['population', 'profit'])

print(data.head())

X_df = pd.DataFrame(data.population)
y_df = pd.DataFrame(data.profit)

m = len(y_df)

def hypo(X, theta):
    #h(x) = B.Tx = B0 + B1x
    return X.dot(theta)

def costFunction(X, y, theta):
    m = len(X)
    #J = (1/2*m) * (np.sum( (hypo(X,theta) - y) ** 2))
    J = np.sum((X.dot(theta)-y)**2)/2/m
    return J
    
def gradientDescent(X, y, theta, alpha, iters):
    
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

#plt.figure(figsize=(10,8))
#plt.plot(X_df, y_df, 'kx')
#plt.xlabel("Population")
#plt.ylabel("Profit")

# relationship: y = B0 + B1x , B0 = intercept
# in multivariable y = XB in vector form

# make best fit line : we need parameters B that allows our predicted
# value to be as close to the actual value as possible
# we want distance between our h(x) and y to be minimized

# cost function: sum of squared distanes
# hypothesis that we are trying to find is given by linear model:
    # h(x) = B^T x = B0 + B1x1
    # we adjust B to minimize J(B)

# perform batch grad descent where each iteration performs the update
# Bj := Bj - a(1/m) sum((h(x)-y)xi)

alpha = 0.01
iters = 1500

X_df['intercept'] = 1

X = np.array(X_df)
y = np.array(y_df).flatten()
theta = np.array([0, 0])

(t, c) = gradientDescent(X, y, theta, alpha, iters)

print("t:", t)

# since we added the intercept afterwards, second col is B0

def prediction(x, t):
    return t[1] + t[0] * x

# plot best-fit line

bestFitX = np.linspace(0, 25, 20)
bestFity = [t[1] + t[0] * xx for xx in bestFitX]

plt.figure(figsize=(10,6))
plt.plot(X_df.population, y_df, '.')
plt.plot(bestFitX, bestFity, '-')
plt.axis([0, 25, -5, 25])
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.title('Profit vs. Population with Linear Regression Line')

fig, ax = plt.subplots(figsize=(12,8))  
ax.plot(np.arange(iters), c, 'r')  
ax.set_xlabel('Iterations')  
ax.set_ylabel('Cost')  
ax.set_title('Error vs. Training Epoch')  
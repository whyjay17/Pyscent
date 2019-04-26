# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 16:31:00 2017

@author: YJ
"""

#Logistic Regression ML - Week2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt  
import os

path = os.getcwd() + '\ex2data1.txt'
data = pd.read_csv(path, header = None, names = ['Exam 1', 'Exam 2', 'Admitted'])
data.head()

# visualize

pos = data[data['Admitted'].isin([1])]
neg = data[data['Admitted'].isin([0])]

fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(pos['Exam 1'], pos['Exam 2'], s=50, c='b', marker='o', label='Admitted')  
ax.scatter(neg['Exam 1'], neg['Exam 2'], s=50, c='r', marker='x', label='Not Admitted')  
ax.legend()  
ax.set_xlabel('Exam 1 Score')  
ax.set_ylabel('Exam 2 Score')  

def sigmoid(z):
    return 1 / ( 1 + np.exp(-z))

nums = np.arange(-10, 10, step = 1)

fig, ax = plt.subplots(figsize=(12,8))

ax.plot(nums, sigmoid(nums), 'r')

def cost(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X) # turn into np matrix
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1-y), np.log(1 - sigmoid(X * theta.T)))
    return np.sum(first - second) / (len(X))

data.insert(0, 'Ones', 1)

cols = data.shape[1]
X = data.iloc[:, 0:cols-1]
y = data.iloc[:, cols-1:cols]
X = np.array(X.values)
y = np.array(y.values)

theta = np.zeros(3)

print(cost(theta, X, y))

def gradient(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    
    params = int(theta.ravel().shape[1])
    grad = np.zeros(params)
    
    err = sigmoid(X * theta.T) - y
    
    for i in range(params):
        term = np.multiply(err, X[:, i])
        grad[i] = np.sum(term) / len(X)
        
    return grad

result = opt.fmin_tnc(func=cost, x0=theta, fprime=gradient, args=(X, y))  
print(cost(result[0], X, y))

def predict(theta, X):
    probability = sigmoid(X * theta.T)
    return [1 if x >= 0.5 else 0 for x in probability]

theta_min = np.matrix(result[0])
predictions = predict(theta_min, X)

correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y)]
accuracy = (sum(map(int, correct)) % len(correct))  
print('accuracy = {0}%'.format(accuracy))
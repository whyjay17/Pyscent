import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.getcwd() + '\ex1data1.txt'
data = pd.read_csv(path, header = None, names = ['Population', 'Profit'])
data.head()

data.plot(kind='scatter', x ='Population', y ='Profit', figsize=(8,4))

def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))

#def gradientDescent(X, y, theta, alpha, iters):
#    temp = np.matrix(np.zeros(theta.shape))
#    params = int(theta.ravel().shape[1]) #flattens
#    cost = np.zeros(iters)
#
#    for i in range(iters):
#        err = (X * theta.T) - y
#        
#        for j in range(params):
#            term = np.multiply(err, X[:,j])
#            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))
#        
#        theta = temp
#        cost[i] = computeCost(X, y, theta)
#    
#    return theta, cost

def gradientDescent(X, y, theta, alpha, iters):
    XT = X.T
    m = len(X)
    for i in range(0, iters):
        hypo = np.dot(XT, theta)
        loss = hypo - y
        cost = np.sum(loss ** 2) / (2 * m)
        gradient = np.dot(X, loss) / m
        
        theta -= alpha * gradient
        
    return theta, cost
# append ones to the first column

data.insert(0, 'Ones', 1)

# separate data into X and y

cols = data.shape[1]
X = data.iloc[:, 0:cols - 1]
y = data.iloc[:, cols-1:cols]

#convert data frames to np matrices

X = np.matrix(X.values)
y = np.matrix(y.values)

theta = np.matrix(np.array([0,0]))

alpha = 0.01
iters = 1000

# perform gradient descent to fit the model
g, cost = gradientDescent(X, y, theta, alpha, iters)

# Visualize solution

x = np.linspace(data.Population.min(), data.Population.max(), 300)
f = g[0, 0] + (g[0, 1] * x)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, f, 'r', label = 'Prediction')
ax.scatter(data.Population, data.Profit, label = 'Training Data')
ax.legend(loc = 2)

ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs Population Size')

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(np.arange(iters), cost, 'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs Training Epoch')

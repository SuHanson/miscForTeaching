#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Making the imports
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Preprocessing Input data
data = pd.read_csv('data2.txt', header = None)
X = data.iloc[:, 0]
Y = data.iloc[:, 1]

# In[5]:


# Building the model
m = 0
c = 0

L = 0.0001  # The learning Rate
epochs = 10  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X

# Performing Gradient Descent 
fig, ax = plt.subplots()
ax.scatter(X, Y)

for i in range(epochs): 
    Y_pred = m*X + c  # The current predicted value of Y
    D_m = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c
    ax.clear()
    ax.scatter(X,Y) 
    ax.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
    plt.pause(0.05)
    # input("please press keyboard for next iteraion!")

print (m, c)
#plt.show()
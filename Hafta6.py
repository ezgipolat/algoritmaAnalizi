#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


class Perceptron(object):


# In[3]:


def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
       self.threshold = threshold
       self.learning_rate = learning_rate
       self.weights = np.zeros(no_of_inputs + 1)


# In[4]:


def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
          activation = 1
        else:
          activation = 0            
        return activation


# In[5]:


def train(self, training_inputs, labels):    # O(s,k,n)
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)


# In[6]:


training_inputs = []


# In[7]:


training_inputs.append(np.array([1, 1]))
training_inputs.append(np.array([1, 0]))
training_inputs.append(np.array([0, 1]))
training_inputs.append(np.array([0, 0]))


# In[8]:


labels = np.array([0, 1, 1, 0]) #xor
perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)
inputs = np.array([1, 1])
perceptron.predict(inputs) 
#=> 1 
inputs = np.array([1, 1])
perceptron.predict(inputs) 


# In[ ]:





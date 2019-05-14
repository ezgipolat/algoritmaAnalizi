#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import print_function, division
from future.utils import iteritems
from builtins import range, input


# In[2]:


def get_data(limit=None):
    print("Reading in and transforming data...")
    df = pd.read_csv('train.csv')
    data = df.values
    np.random.shuffle(data)
    X = data[:, 1:] / 255.0 # data is from 0..255
    Y = data[:, 0]
    if limit is not None:
        X, Y = X[:limit], Y[:limit]
    return X, Y


# In[3]:


import numpy as np
from datetime import datetime
from scipy.stats import norm
from scipy.stats import multivariate_normal as mvn


# In[4]:


class NaiveBayes(object):
    def fit(self, X, Y, smoothing=1e-2):
        self.gaussians = dict()
        self.priors = dict()
        labels = set(Y)
        for c in labels:
            current_x = X[Y == c] 
            self.gaussians[c] = {
                'mean': current_x.mean(axis=0), 
                'var': current_x.var(axis=0) + smoothing,
            }
            self.priors[c] = float(len(Y[Y == c])) / len(Y)


# In[5]:


def score(self, X, Y):
        P = self.predict(X)
        return np.mean(P == Y)


# In[6]:


def predict(self, X): #O(p) p class sayısı 0.1.2...9
       N, D = X.shape
       K = len(self.gaussians)
       P = np.zeros((N, K))
       for c, g in iteritems(self.gaussians):
           mean, var = g['mean'], g['var']
           P[:,c] = mvn.logpdf(X, mean=mean, cov=var) + np.log(self.priors[c])
       return np.argmax(P, axis=1)


# In[7]:


if __name__ == '__main__':
    X, Y = get_data(10000)
    Ntrain = len(Y) // 2
    Xtrain, Ytrain = X[:Ntrain], Y[:Ntrain]
    Xtest, Ytest = X[Ntrain:], Y[Ntrain:]

    model = NaiveBayes()
    t0 = datetime.now()
    model.fit(Xtrain, Ytrain)
    print("Training time:", (datetime.now() - t0))

    t0 = datetime.now()
    print("Train accuracy:", model.score(Xtrain, Ytrain))
    print("Time to compute train accuracy:", (datetime.now() - t0), "Train size:", len(Ytrain))

    t0 = datetime.now()
    print("Test accuracy:", model.score(Xtest, Ytest))
    print("Time to compute test accuracy:", (datetime.now() - t0), "Test size:", len(Ytest))


# In[ ]:





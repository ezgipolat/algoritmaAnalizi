#!/usr/bin/env python
# coding: utf-8

# In[3]:


import ctypes


# In[2]:


class DynamicArray:
    def getsize(self):
        import sys
        return sys.getsizeof(self._A)


# In[4]:


def ToString(self):
        for i in self._A:
            print(i, " ")


# In[5]:


def getLength(self):
        return len(self._A)


# In[8]:


def __init__(self):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)


# In[9]:


def __len__(self):
        return self._n


# In[10]:


def __getitem__(self,k):
        if not 0 <= k <self._n:
            raise IndexError('invalid index')
        return self._A[k]


# In[11]:


def append(self,obj):
        if self._n == self._capacity: 
            self._resize(2*self._capacity)
        self._A[self._n]=obj
        self._n+=1


# In[12]:


def _resize(self, c): # nonpublic utitity
        print("su an worst-case durumunda , liste dolu, başka yerden n*2 lik yer alınıp taşıma yapılacak")
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A=B # use the bigger array
        self._capacity = c


# In[13]:


def _make_array(self, c): # nonpublic utitity
    return(c*ctypes.py_object)()


# In[14]:


c=DynamicArray()
for i in range(33):
    c.append(" add an item"+str(i))
    print(str(i)+" eklendi , dizi boyutu : "+str(c.getLength())) 


# In[ ]:





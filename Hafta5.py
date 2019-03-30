#!/usr/bin/env python
# coding: utf-8

# In[1]:


def minparabul(para,paralist):
    kacfarkli=0
    while(para):
        for i in range(len(paralist)-1,-1,-1):
            if(paralist[i]<=para):
                para=para-paralist[i]
                print("1 Tane",paralist[i])
                kacfarkli=kacfarkli+1
                break
    return kacfarkli


# In[2]:


print("toplam para sayısı:",minparabul(293,[1,5,10,25,50]))


# In[3]:


def recMC(coinValueList,change):
    minCoins=change
    if(change in coinValueList): #bozuk para listesinde var ise 1
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC(coinValueList,change-i)
            if(numCoins<minCoins):
                minCoins=numCoins
    return minCoins


# In[4]:


recMC([1,5,10,25,50],43)


# In[5]:


def rec_fb(n,result): #fibonacci optimizasyon
    if n<2:
        return n
    elif(result[n]!=0): #elde ettiğim değerleri hafızadan direk al eüer yoksa else girip hesap yap
        return result[n]
    else:
        result[n]=rec_fb(n-1,result)+rec_fb(n-2,result)
        return result[n]


# In[6]:


for i in range(13,50):
    print(rec_fb(i,[0]*(i+1)),end=" ")


# In[7]:


def recMC2(coinValueList,change,knownResults):
    minCoins=change
    if(change in coinValueList): #bozuk para listesinde var ise 1
        knownResults[change]=1
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC2(coinValueList,change-i,knownResults)
            if(numCoins<minCoins):
                minCoins=numCoins
                knownResults[change]=minCoins
    return minCoins


# In[8]:


for i in range(8,20):
    print(i," ",recMC2([1,5,10,25,50],i,[0]*(i+1)))


# In[ ]:





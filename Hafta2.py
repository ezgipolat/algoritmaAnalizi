#!/usr/bin/env python
# coding: utf-8

# In[1]:


sayac=0
def power_1(m,n):
    t=1
    global sayac
    for i in range(n):
        sayac=sayac+1
        t=t*m
    return (t,sayac)


# In[2]:


def call_report(x,y):
    global sayac
    sayac=0
    r=power_1(x,y)
    print("Recursive olmayan : ",x," üzeri ", y," değeri : ",r[0],"çağrım sayısı: ",r[1])


# In[3]:


def power_2(x,n):
    global sayac
    sayac=sayac+1
    if(n==0):
        return 1
    if(n==1):
        return x
    if(n%2==0):
        return power_2(x*x,int(n/2))
    else:
        return power_2(x*x,int(n/2))*x


# In[4]:


def call_report_recursive(x,y):
    global sayac
    sayac=0
    r=power_2(x,y)
    print(x," üzeri", y," değeri",r ," çağrım sayısı : ",sayac)
    


# In[5]:


call_report(2,8)
call_report_recursive(2,8)
call_report_recursive(2,16)
call_report_recursive(2,32)
call_report_recursive(2,8)


# In[ ]:





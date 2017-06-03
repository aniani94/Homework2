
# coding: utf-8

# In[1]:

collection1 = input("Input some numbers separated by a comma: ")
def my_average(collection1):
    return float(sum(collection1))/(len(collection1))
print(collection1)
print float(sum(collection1))/(len(collection1))


# In[10]:

collection1 = input("Input some numbers separated by a comma: ")
collection2= input("Argument_2: ")
def my_average(collection1):
    return float(sum(collection1[-(collection2):]))/float(int(collection2))
print (collection1)
print float(sum(collection1[-(collection2):]))/float(int(collection2))


# In[11]:

import random


# In[13]:

random.randint(1,100)
x= random.randint(1,100)
def well(x):
    print x
    if 50<x<100:
        return "Win"
    elif 1<=x<=50:
        return "Loss"
    else:
        return "Draw"


# In[14]:

print well(x)


# In[15]:

import pandas_datareader.data as web


# In[16]:

data = web.DataReader(["IBM","AAPL","MSFT"],"google")


# In[17]:

our_list=["IBM","AAPL","MSFT"]
for i in our_list:
    data=web.DataReader(i,"google")
    print  data.head(7)


# In[34]:

import pandas_datareader.data as web
import matplotlib.pyplot as plt
our_list=["IBM","AAPL","MSFT"]
for i in our_list:
    data=plt.plot(web.DataReader(i, 'google')["Open"])
    print(plt.show())


# In[ ]:




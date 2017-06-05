
# coding: utf-8

# In[1]:

set1 = input("Input some numbers separated by a comma: ")
def my_average(set1):
    return float(sum(set1))/(len(set1))
print(set1)
print float(sum(set1))/(len(set1))


# In[2]:

set1 = input("Input some numbers separated by a comma: ")
set2= input("Argument_2: ")
def my_average(set1):
    return float(sum(set1[-(set2):]))/float(int(set2))
print (set1)
print float(sum(set1[-(set2):]))/float(int(set2))


# In[3]:

import random


# In[4]:

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


# In[5]:

print well(x)


# In[7]:

import pandas_datareader.data as web


# In[8]:

data = web.DataReader(["IBM","AAPL","MSFT"],"google")
our_list=["IBM","AAPL","MSFT"]
for i in our_list:
    data=web.DataReader(i,"google")
    print  data.head(7)


# In[9]:

import pandas_datareader.data as web
import matplotlib.pyplot as plt
our_list=["IBM","AAPL","MSFT"]
for i in our_list:
    data=plt.plot(web.DataReader(i, 'google')["Open"])
    print(plt.show())


# In[ ]:




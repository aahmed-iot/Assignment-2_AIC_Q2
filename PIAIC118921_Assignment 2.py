#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Question:1


# In[2]:


### Convert a 1D array to a 2D array with 2 rows?


# In[4]:


import numpy as np


# In[47]:


Arr1 = np.array([0,1,2,3,4,5,6,7,8,9])


# In[49]:


Arr2 = np.reshape(Arr1, (-1, 5))


# In[50]:


Arr2


# In[14]:


## Question:2


# In[15]:


###  How to stack two arrays vertically?


# In[51]:


Arrx = np.array([3, 5, 7])


# In[52]:


Arry = np.array([5, 7, 9])


# In[53]:


np.vstack((Arrx,Arry))


# In[27]:


## Question:2


# In[28]:


###  How to stack two arrays horizontally?


# In[54]:


np.hstack((Arrx,Arry))


# In[30]:


## Question:4


# In[31]:


### How to convert an array of arrays into a flat 1d array?


# In[56]:


arr = np.array([[1, 2], [3, 4]])


# In[46]:


arr.reshape(-1)


# In[55]:


## Question:5


# In[57]:


### How to Convert higher dimension into one dimension?


# In[60]:


Arr5 = np.random.randn(4,5)


# In[63]:


Arr5.flatten()


# In[64]:


## Question:6


# In[65]:


### Convert one dimension to higher dimension?


# In[72]:


arr_1d = np.arange(6)


# In[78]:


arr_2d = arr_1d.reshape((3, 2))


# In[79]:


arr_2d


# In[81]:


## Question:7


# In[82]:


## Create 5x5 an array and find the square of an array?


# In[85]:


x7 = np.random.random((5,5))


# In[87]:


x7_out = x7*2


# In[88]:


x7_out 


# In[89]:


## Question:8


# In[90]:


### Create 5x6 an array and find the mean?


# In[91]:


x8 = np.random.random((5,6))


# In[96]:


np.mean(x8)


# In[97]:


## Question:9


# In[98]:


### Find the standard deviation of the previous array in Q8?


# In[99]:


np.std(x8)


# In[100]:


## Question:10


# In[101]:


### Find the median of the previous array in Q8?


# In[102]:


np.median(x8)


# In[103]:


## Question:11


# In[104]:


### Find the transpose of the previous array in Q8?


# In[105]:


np.transpose(x8)


# In[106]:


## Question:12


# In[107]:


### Create a 4x4 an array and find the sum of diagonal elements?


# In[108]:


x12 = np.random.random((4,4))


# In[118]:


x123 = np.diagonal(x12)


# In[119]:


np.sum(x123)


# In[120]:


## Question:13


# In[121]:


### Find the determinant of the previous array in Q12?


# In[122]:


np.linalg.det(x12)


# In[123]:


## Question:14


# In[124]:


### Find the 5th and 95th percentile of an array?


# In[125]:


np.percentile(x12, 0.05)


# In[126]:


np.percentile(x12, 0.95)


# In[127]:


## Question:15


# In[128]:


### How to find if a given array has any null values?


# In[133]:


array15 = np.array([])


# In[135]:


empty = array15.size == 0


# In[136]:


empty


# In[ ]:





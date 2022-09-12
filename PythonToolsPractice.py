#!/usr/bin/env python
# coding: utf-8

# # Tools
# 

# In[1]:


name = input("what is your name? ")
print("welcome, " + name)


# In[3]:


import numpy as np

x = np.array([[1,2,3], [4,5,6]])
print("x:\n{}".format(x))


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y = np.sin(x)

plt.plot(x, y, marker="x")


# In[8]:


import pandas as pd
from IPython.display import display

data = {'Name': ["John", "Ana", "Peter", "Linda"],
       'Loction:': ["New York", "Paris", "Berlin", "London"],
       'Age' : [24, 13, 53, 33]}

data_pandas = pd.DataFrame(data)
display(data_pandas)

#Select all rows that have an age column greater than 30
display(data_pandas[data_pandas.Age > 30])


# In[ ]:





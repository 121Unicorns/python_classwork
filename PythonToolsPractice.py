#!/usr/bin/env python
# coding: utf-8

# # Toolsa

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


# In[26]:


import pandas as pd
from IPython.display import display

data = {'Name': ["John", "Ana", "Peter", "Linda"],
       'Loction:': ["New York", "Paris", "Berlin", "London"],
       'Age' : [24, 13, 53, 33]}

data_pandas = pd.DataFrame(data)
display(data_pandas)


# In[27]:


#Select all rows that have an age column greater than 30
display(data_pandas[data_pandas.Age > 30])


# In[23]:


from sklearn.datasets import load_iris
iris_dataset = load_iris()


# In[24]:


print("Keys of iris_dataset: \n\n{}".format(iris_dataset.keys()))


# In[25]:


print(iris_dataset['DESCR'][:193] + "\n...")


# In[29]:


print("Target names: {}".format(iris_dataset['target_names']))


# In[30]:


print("Feature names: {}".format(iris_dataset['feature_names']))


# In[31]:


print("Type of data {}".format(type(iris_dataset['data'])))


# In[32]:


print("Shape of data: {}".format(iris_dataset['data'].shape))


# In[33]:


print("First five rows of data: \n{}".format(iris_dataset['data'][:5]))


# In[35]:


print("Type of target: {}".format(type(iris_dataset['target'])))


# In[36]:


print("Shape of target: {}".format(iris_dataset['target'].shape))


# In[37]:


print("Target:\n{}".format(iris_dataset['target']))

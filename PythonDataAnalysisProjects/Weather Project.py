#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[10]:


data = pd.read_csv(r"C:\Users\Lenovo-Yoga\Downloads\1. Weather Data.csv")


# In[11]:


data


# In[12]:


data.head()


# In[14]:


data.shape


# In[15]:


data.index


# In[16]:


data.columns


# In[17]:


data.dtypes


# In[18]:


data['Weather'].unique()


# In[19]:


data.nunique()


# In[20]:


data['Weather'].nunique()


# In[21]:


data.count()


# In[23]:


data['Weather'].value_counts()


# In[24]:


data.info()


# data.dtypes

# In[25]:


data.head(2)


# In[26]:


data.nunique()


# In[27]:


data['Wind Speed_km/h'].nunique()


# In[28]:


data['Wind Speed_km/h'].unique()


#  Q) 2. Find the number of times when the 'weather is exactly clear'.
# 

# In[29]:


data.Weather.value_counts()


# In[32]:


#filtering
data[data.Weather == 'Clear']


# In[33]:


#groupby()
data.groupby('Weather').get_group('Clear')


# # Find the number of times whereby the windspeed was exactly 4km/h
# 

# In[36]:


#data.head()
data.groupby('Wind Speed_km/h').get_group(4)


# # Find out The Null Values in the dataset

# In[38]:


data.isnull().sum()


# In[40]:


data.notnull().sum()


# # Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[41]:


data.rename(columns = {'Weather' : 'Weather Condition'})


# # What is the mean 'Visibility'?

# In[42]:


data.head(2)


# In[43]:


data.Visibility_km.mean()


# # What is the standard deviation of 'Pressure' in the dataset

# In[44]:


data.head()


# In[45]:


data.Press_kPa.std()


# # What is the Variance of 'Relative Humidity' in this data?

# In[46]:


data.head()


# In[47]:


data['Rel Hum_%'].var()


# # Find all instances when 'Snow' was recorded

# In[49]:


#value_counts()
#data.head()
data['Weather'].value_counts()


# In[51]:


#filtering
data[data['Weather']== 'Snow']


# In[53]:


#str.contains
data[data['Weather'].str.contains('Snow')].head(50)


# In[54]:


data[data['Weather'].str.contains('Snow')].tail(50)


# # Find all instances when 'Wind speed is above 24' and 'Visibility is 25'

# In[59]:


#data.head(2)
data[(data['Wind Speed_km/h'] > 24)&(data['Visibility_km']== 25)]


# # What is the mean value of each column against each weather condition

# In[60]:


data.head(2)


# In[61]:


data.groupby('Weather').mean()


# # what is the min and max value of each column against 'weather'

# In[62]:


data.groupby('Weather').min()


# In[63]:


data.groupby('Weather').max()


# # Show all the records where the weather is fog

# In[64]:


data[data['Weather'] == 'Fog']


# # Find all the instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[65]:


data[(data['Weather'] == 'Clear') | (data['Visibility_km']>40)]


# In[66]:


data[(data['Weather'] == 'Clear') | (data['Visibility_km']>40)].head(50)


# In[67]:


data[(data['Weather'] == 'Clear') | (data['Visibility_km']>40)].tail(50)


# # Find all instances when:
# # A. Weather is Clear and Relative Humidity is greater than 50
# or
# # B.Visibility is above 40

# In[68]:


data.head()


# In[69]:


data[(data['Weather'] == 'Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km'] > 40)]


# In[ ]:





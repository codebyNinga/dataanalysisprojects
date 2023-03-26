#!/usr/bin/env python
# coding: utf-8

# # SALES ANALYSIS
# 
# 
# 
# ## import necessary libraries

# In[55]:


import pandas as pd

import os


# #### Task 1: Merging 12 months of sales data into a single file

# In[56]:


df = pd.read_csv(r"C:\Users\Lenovo-Yoga\Downloads\Pandas-Data-Science-Tasks-master\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\Sales_April_2019.csv")

files = [file for file in os.listdir(r"C:\Users\Lenovo-Yoga\Downloads\Pandas-Data-Science-Tasks-master\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data")]

all_months_data =pd.DataFrame()

for file in files:
    df = pd.read_csv(r"C:\Users\Lenovo-Yoga\Downloads\Pandas-Data-Science-Tasks-master\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data/"+file)
    all_months_data =pd.concat([all_months_data, df])
    
all_months_data.to_csv("all_sales.csv", index=False)   


# ### Read in Updated Dataframe

# In[57]:


all_sales = pd.read_csv(r"C:\Users\Lenovo-Yoga\Downloads\Pandas-Data-Science-Tasks-master\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\all_sales.csv")
all_sales.head()


# ## Cleaning up the Data
# 
# 
# #### Removing NAN Rows

# In[58]:


nan_df = all_sales[all_sales.isna().any(axis=1)]
nan_df.head()

all_sales = all_sales.dropna(how='all')
all_sales.head()


# ### Error: invalid literal for int() with base 10: 'Or'
# 
# #### Find 'Or' and Delete It
# 
# 

# In[59]:


all_sales = all_sales[all_sales['Order Date'].str[0:2] != 'Or']
all_sales.head()


# ### Converting Data in columns to the correct Format/Data Type

# In[60]:


all_sales['Price Each'] = pd.to_numeric(all_sales['Price Each'])
all_sales['Quantity Ordered'] = pd.to_numeric(all_sales['Quantity Ordered'])

all_sales.head()



# ## Adding additional columns to the data
# 
# ### Task 2: Adding the Month Column

# In[61]:


all_sales['Month'] = all_sales['Order Date'].str[0:2]
all_sales.head()


# #### Converting the month from string to Integer

# In[62]:


all_sales['Month'] = all_sales['Order Date'].str[0:2]
all_sales['Month'] = all_sales['Month'].astype('int32')
all_sales.head()


# ##### Task 3: Adding a Sales Column (Quantity Ordered * Price Each)

# In[63]:


all_sales['Sales'] = all_sales['Quantity Ordered'] * all_sales['Price Each']
all_sales.head()


# ### Task 4: Add a City Column
# 
# 
# -Use the .apply() method
# 

# In[88]:


def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]


all_sales['City'] =all_sales['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})")


all_sales.head() 


# In[ ]:





# #### QUESTION 1: What was the best month for sales? How much was earned that month?

# In[75]:


all_sales.groupby('Month').sum()


# #### What was the best month for sales? How much was earned that month? (AS CHART)

# In[69]:


results = all_sales.groupby('Month').sum()


# In[71]:


import matplotlib.pyplot as plt

months = range(1,13)

plt.bar(months, results['Sales'])
plt.show()


# In[73]:


import matplotlib.pyplot as plt

months = range(1,13)

plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month Number')
plt.show()


# #### Question 2: What city had the highest number of sales

# In[74]:


all_sales.head()


# In[89]:


results = all_sales.groupby('City').sum()
results


# In[90]:


import matplotlib.pyplot as plt

cities = [city for city, df in all_sales.groupby('City')]

plt.bar(cities, results['Sales'])
plt.xticks(cities, rotation = 'vertical', size =8)
plt.ylabel('Sales in USD ($)')
plt.xlabel('City Name')
plt.show()


# ### Question 3: What time should we display advertisements to maximize likelihood of customers buying product?

# In[91]:


all_sales['Order Date'] = pd.to_datetime(all_sales['Order Date'])


# In[96]:


all_sales['Hour'] = all_sales['Order Date'].dt.hour

all_sales['Minute'] = all_sales['Order Date'].dt.minute

all_sales.head()


# In[100]:


hours = [hour for hour, df in all_sales.groupby('Hour')]

plt.plot(hours, all_sales.groupby(['Hour']).count())

all_sales.groupby(['Hour']).count()


# In[105]:


hours = [hour for hour, df in all_sales.groupby('Hour')]

plt.plot(hours, all_sales.groupby(['Hour']).count())
plt.xticks(hours)
plt.xlabel('Hours(24)')
plt.ylabel('Number Of Orders')
plt.grid()
plt.show()


# #### Question 4: What products are most often sold together?

# In[106]:


all_sales.head()


# In[107]:


df = all_sales[all_sales['Order ID'].duplicated(keep=False)]
df.head(20)


# In[110]:


df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df.head()

df = df[['Order ID', 'Grouped']].drop_duplicates()
df.head()


# In[114]:


from itertools import combinations
from collections import Counter


count = Counter()

for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 3)))
    
for key, value in count.most_common(10):
    print(key, value)

                        


# ### Question 5: What product sold the most? Why do you think it sold the most?

# In[124]:


product_group = all_sales.groupby('Product')
quantity_ordered = product_group.sum()


# In[130]:


product_group = all_sales.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

products = [product for product, df in product_group]

plt.bar(products, quantity_ordered)
plt.ylabel('Quantity Ordered')
plt.xlabel('Product')
plt.xticks(products, rotation = 'vertical', size=8)
plt.show()
 


# In[131]:


prices = all_sales.groupby('Product').mean()['Price Each']
print(prices)


# ### adding an overlay to a bar graph

# In[134]:


prices = all_sales.groupby('Product').mean()['Price Each']

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products, quantity_ordered, color='g')
ax2.plot(products, prices, 'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price($)', color='b')
ax1.set_xticklabels(products, rotation='vertical', size=8)

plt.show()



# In[132]:


all_sales.head()


# In[ ]:





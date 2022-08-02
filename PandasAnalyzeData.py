#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import os


# In[ ]:


## Merging 12 months of sales data into a single file


# In[13]:


df = pd.read_csv("C:/Users/tiffc/OneDrive/Documents/Python/Jupyter/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/Sales_April_2019.csv")



files = [file for file in os.listdir("C:/Users/tiffc/OneDrive/Documents/Python/Jupyter/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data")]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("C:/Users/tiffc/OneDrive/Documents/Python/Jupyter/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/" + file)
    all_months_data = pd.concat([all_months_data, df])
    
all_months_data.to_csv("C:/Users/tiffc/OneDrive/Documents/Python/Jupyter/all_months_data.csv", index = False)


# In[15]:


#Read in updated dataframe 
all_data = pd.read_csv("C:/Users/tiffc/OneDrive/Documents/Python/Jupyter/all_months_data.csv")
all_data.head()


# In[21]:


# Cleaning data
# Dropping rows of NaN

nan_df = all_data[all_data.isna().any(axis = 1)]
nan_df.head(50)

all_data = all_data.dropna(how ='all')
all_data.head()


# In[26]:


#Fixing error, dropping all months that resemble 'Or'

all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']


# In[29]:


# Chaning Quantity Ordered and Price Each columns to correct type

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])


# In[27]:


# What was the best month for sales? How much was earned that month?
# Lets first add a column that lets us know what month it is.

all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')
all_data.head()


# In[33]:


# Adding a sales column

all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head()


# In[37]:


# What was the best month for sales? How much was earned that month?

results = all_data.groupby('Month').sum()


# In[39]:


import matplotlib.pyplot as plt

#plotting this data into a bar chart

months = range(1,13)
plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD')
plt.xlabel('Months')
plt.show()


# In[49]:


#What US City had the highest number of sales?

#Create a city column

def get_city(address):
    return address.split(',')[1]
def get_state(address):
    return address.split(',')[2].split(' ')[1]

all_data['City2']= all_data[ 'Purchase Address'].apply(lambda x: get_city(x) + ' ' + get_state(x))
all_data.head(50)


# In[50]:


# Grouping by city 

results = all_data.groupby('City2').sum()
results


# In[75]:


#What products are most often sold together?

#Looking for all duplicate order ids
df = all_data[all_data['Order ID'].duplicated(keep = False)]

#adding grouped column that shows all products ordered together
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

#dropping duplicates
df = df[['Order ID', 'Grouped']].drop_duplicates()

df.head()


# In[78]:


#counting the amount of times certain groups of products are bought

from itertools import combinations
from collections import Counter

count = Counter()
for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))
    
count.most_common(10)


# In[87]:


#What product sold the most? 
import matplotlib.pyplot as plt

product_group = all_data.groupby('Product')

quantity_ordered = product_group.sum()['Quantity Ordered']

products = [product for product, df in product_group]
plt.ylabel('Quantity Ordered')
plt.xlabel('Product')
plt.bar(products, quantity_ordered)
plt.xticks(products, rotation = 'vertical', size = 8)
plt.show()


# In[92]:


# showing the price vs the amount of products bought

prices = all_data.groupby('Product').mean()['Price Each']

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products, quantity_ordered, color = 'g')
ax2.plot(products, prices, 'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color = 'g')
ax2.set_ylabel('Price ($)', color = 'b')
ax1.set_xticklabels(products, rotation = 'vertical', size = 8)

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Use this cell to begin your analyses, and add as many cells as you would like!
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/lego_sets.csv')
theme = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/lego-analysis/master/datasets/parent_themes.csv')


# In[2]:


df.head()


# In[6]:


theme.head(10)


# In[9]:


#What percentage of all licensed sets ever released were Star Wars themed?

#Merging both data sets
all_data = df.merge(theme, left_on= 'parent_theme', right_on = 'name')

#dropping duplicate columns
all_data = all_data.drop(columns = 'name_y')
all_data.head()


# In[27]:


#Filtering to all licensed legos
licensed = all_data[all_data['is_licensed'] ==True]
licensed = licensed.dropna(subset = ['set_num']) 
licensed.head()


# In[11]:


#Which percentage is Star Wars

star_wars = licensed[licensed['parent_theme']== 'Star Wars']
star_wars.head(50)


# In[13]:


#Shows number of star wars themed legos
num_star = star_wars.shape[0]


# In[29]:


#Dividing number of star war legos by number of licensed 
perc_star = star_wars.shape[0] / licensed.shape[0]
print(perc_star)


# In[26]:


#Cleaning data - shows number of rows that the set_num column shows as Null.
all_data[all_data['set_num'].isnull()].shape


# In[42]:


#Which year was star wars not the most popular licensed theme? 

#Sorting data by year and adding a count column 
licensed_sorted = licensed.sort_values('year')
licensed_sorted['count'] = 1

summed_df = licensed_sorted.groupby(['year', 'parent_theme']).sum().reset_index()

max_df = summed_df.sort_values('count', ascending=False).drop_duplicates(['year'])
max_df.sort_values('year', inplace=True)
max_df


# In[ ]:





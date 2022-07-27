#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd

df = pd.read_csv('C:/Users/tiffc/OneDrive/Documents/Python/Jupyter/pokemon_data.csv')


# In[23]:


# Read Headers / Column Names (print)
df.columns


# In[24]:


# Read Columns
df[['Name', 'Type 1']][0:5]


# In[25]:


# Read Each Row
df.iloc[1:4]


# In[32]:


for index, row in df.iterrows():
   print(index, row['Name'])
    


# In[27]:


df.loc[df['Type 1'] == "Fire"] 


# In[28]:


#Read a specific location (R,C)
df.iloc[2,1]


# In[33]:


#gives a summary of stats for the data
df.describe()


# In[36]:


#Sorting values
df.sort_values(['Type 1','Name'], ascending=[1,0])
#Type 1 here sorts A -Z and Name sorts Z to A


# In[40]:


#Making changes to data

# Lets make a total rank

# Adding total column
df['Total'] = df['HP'] + df['Attack'] +df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
 
df.head(5)


# #### Drop a column
# # df= df.drop(columns = ['Total'])
# df.head(5)

# In[46]:


#Easier way to add a column
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#axis = 1 is adding horizontally and axis = 0 is adding vertically 
# using 10 to include the 9th column.
df.head(5)


# In[48]:


#Changing location of added column
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
df.head(5)


# In[53]:


# Saving CSV to computer 
df.to_csv('C:/Users/tiffc/OneDrive/Documents/Python/Jupyter/modified.csv', index = False)
#index = False will get rid of your index. 
df.to_excel('C:/Users/tiffc/OneDrive/Documents/Python/Jupyter/modified1.xlsx', index = False)


# In[61]:


#Filtering Data
#inside pandas use & instead of and. If you wanted or use | 

df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]

#new_df.to_cvs('filtered.csv')
# above will create a new excel 

#reseting the indec
new_df = new_df.reset_index()

new_df


# In[63]:


#Filtering all the data that contains 'Mega'
# the ~ means NOT IN
df.loc[~df['Name'].str.contains('Mega')]


# In[68]:


import re

#filtering by fire and grass
#flags=re.I means ignoring case (upper and lower case)
df.loc[df['Type 1'].str.contains('FIre|GraSs', flags=re.I, regex=True)]


# In[71]:


#Filtering by Names that start with Pi and can have 0 or more any other characters in it
# ^ in the code below means starting with "pi"
# [a,z] says any letters can come after the i
# * means 0 to inf letters can come after pi -- broadnening the search.

df.loc[df['Name'].str.contains('^pi[a,z]*', flags=re.I, regex=True)]


# In[73]:


#Changing the name of something

df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
df


# In[75]:


# using condition to set the parameter of another
df.loc[df['Type 1'] == 'Flamer', 'Legendary'] = True
df


# In[76]:


#Chaning more columns
#df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE'


# In[79]:


#Group by for aggregate statistics 
# sum, mean, and count

df.groupby(['Type 1']).mean().sort_values('HP', ascending = False)


# In[80]:


#Adding a count column

df['count'] = 1
df.groupby(['Type 1']).count()['count']


# In[84]:


#Working with large amounts of data
#means 5 rows being passed in at a time.
#if you were working with a huge data set if might be 100000 instead of 5

for df in pd.read_csv('modified.csv', chunksize = 5):
    print(df)


# In[ ]:





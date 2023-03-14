#!/usr/bin/env python
# coding: utf-8

# # Import Necessary Libraries and Dataset

# In[1]:


import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\HP\Downloads\Weather Data.csv')


# # General Operations on Dataset

# In[2]:


# head() returns the top records from the dataset.

df.head(5)


# In[3]:


# tail() returns the last records from the dataset.

df.tail(5)


# In[4]:


# Check if any null values present in the Dataset.

df.isnull().sum()


# In[5]:


# basic statistical method

df.describe()


# In[6]:


# to check the overall datatypes of the columns

df.info()


# # EDA on Weather Dataset

# ### 1. Find all the Unique 'Wind Speed' values in the Dataset

# In[7]:


# unique() will give all the Unique Values present in the Column

df['Wind Speed_km/h'].unique()


# In[8]:


# nunique() returns the lenght of the unique Values present in the Column

df['Wind Speed_km/h'].nunique()


# ### 2. Find the number of times when the Weather is exactly 'Clear'

# In[9]:


# By filtering the data we can get our desired Output

df.head(2)          # Displaying the df for reference.


# In[10]:


# In order to get the correct output we have to just put the above condition again in df['']

df[df['Weather'] == 'Clear']


# In[11]:


# By using value_counts() we can also get the required count.

df['Weather'].value_counts().to_dict()    # to_dict() to get the Output in Dictionary Format.


# ### 3. Find the Number of Times when the 'Wind Speed' was exactly 4 km/h.

# In[12]:


# To solve this same approach as previous

df[df['Wind Speed_km/h'] == 4]


# ### 4. Find any null values present in the DataFrame.

# In[13]:


df.isnull().sum()        # Displays Column wise Sum of Null Values


# ### 5. Rename the Weather Column to 'Weather Condition'

# In[14]:


# by using rename() we can change the name if the column in dataframe.

df.rename(columns = {'Weather' : 'Weather Condition'})  


# In[15]:


# Here although we are alble to see the change in Column Name but it was temporary
# To apply the change to main DF we need to use 'inplace'
   
df.head(5)


# In[16]:


df.rename(columns = {'Weather' : 'Weather Condition'}, inplace=True)  


# In[17]:


df.head(5)


# ### 6. What is the Mean Visibilty ? round it up to 2 decimal points.

# In[18]:


print("Mean Visibility :",round(df.Visibility_km.mean(),2))


# ### 7. What is Standard Deviation of Pressure ? 

# In[19]:


print("Standard Deviation of Pressure :",df.Press_kPa.std())


# ### 8. What is the Variance of Relative Humidity ?

# In[20]:


print("Variance of Relative Humidity :",round(df['Rel Hum_%'].var(),2))


# ### 9. Find all instances where Snow was recorded.  (Weather Contains Snow in it)

# In[21]:


# using str.contains() method will return all the instances of the Weather Condition contains "snow" in it.

df[df['Weather Condition'].str.contains('Snow')]


# #### What if there are lot of Case sensitve Weather Conditions as well ?

# In[22]:


# we can tackle this while temporary converting Weather Condition to lower case for better match !

df[df['Weather Condition'].str.lower().str.contains('snow')]


# In[23]:


# cross checking 

df[df['Weather Condition'].str.lower().str.contains('SNOW'.lower())]


# ### 10. Find all instances where 'Wind Speed' is above 24 and 'Visibility' = 25

# In[24]:


# We need to filter the Data with 'AND' Operator including both conditions

df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] == 25)]


# ### 11. What is the Mean value of each column against each 'Weather Condition' ?

# In[25]:


# grouping by the Weather Condition to get desired output !

df.groupby('Weather Condition').mean().head()


# ### 12. What is the Min and Max Value of each column against 'Weather Condition' ? 

# In[26]:


# min (limiting to first 10 entries)

df.groupby('Weather Condition').min().head(10)


# In[27]:


# max (limiting to first 10 entries)

df.groupby('Weather Condition').max().head(10)


# # End

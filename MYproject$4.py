#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
df=pd.read_csv('Music_and_Mental_Health_-_Survey.csv')
import matplotlib.pyplot as plt


# In[40]:


df.head()


# In[41]:


df.shape


# In[42]:


df.describe()


# In[43]:


df.columns


# In[44]:


df.isnull().sum()


# In[45]:


df.info()


# In[46]:


hours_per_day_mean = df['Hours per day'].mean()
print("Mean hours per day:", hours_per_day_mean)


# In[47]:


plt.figure(figsize=(6,4))
sns.barplot(data = df,x = 'Hours per day',y = 'Age')
plt.show()
plt.close()


# In[48]:


genre_colum = [col for col in df.columns if 'Frequency' in col]
corr = df[genre_colum + ['Anxiety', 'Depression', 'Insomnia', 'OCD']].corr()
corr


# In[32]:


# relationships between music genre preferences and mental health symptoms.


# In[76]:


df = df.dropna()


# In[80]:


df.duplicated().sum()


# In[81]:


missing_values_count = df["BPM"].isna().sum()

missing_values_count


# In[ ]:





# In[82]:


mean = df["BPM"].mean()
std_dev = df["BPM"].std()
# identify outliers
outliers = df[(df["BPM"] < mean - 2*std_dev) | (df["BPM"] > mean + 2*std_dev)]
outliers.head()
     
# create boxplot
sns.boxplot(x=df["BPM"])


# In[83]:


cleaned_data=pd.read_csv('Music_and_Mental_Health_-_Survey.csv')


# In[84]:


df.to_csv('Music_and_Mental_Health_-_Survey.csv',index=False)


# In[85]:


df = df[~df.index.isin(outliers.index)]


# In[86]:


# create boxplots
sns.boxplot(x=df["BPM"])


# In[87]:


cleaned_data.head()


# In[75]:


cleaned_data.info()


# In[88]:


df.isnull().sum()


# In[ ]:





# In[ ]:





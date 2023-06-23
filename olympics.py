import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# In[63]:


df = pd.read_csv("C:/Users/ashvi/internship23/notebooks/summer.csv")


# In[64]:
print("\n")
print("Printing preview of the dataframe.\n")
print(df.head())
print("\n\n")

# In[65]:


summer_num = df['City'].nunique()


# In[66]:


print("The number of cities in which the summer olympics has been held so far is", summer_num)
print("\n\n")

# In[67]:


df_gold = df[df['Medal'] == 'Gold']


# In[68]:


most_gold_medals = df_gold['Sport'].value_counts().head(5)


# In[69]:


print("The top 5 sports with most gold medals is\n",most_gold_medals)
print("\n\n")


# In[70]:


most_medals = df['Sport'].value_counts().head(5)


# In[71]:


print("The top 5 sports with the most medals is\n", most_medals)
print("\n\n")


# In[72]:


most_medals_player = df['Athlete'].value_counts().head(5)


# In[73]:


print("The top 5 players with the most medals won is\n", most_medals_player)
print("\n\n")

# In[74]:


most_gold_medals_player = df_gold['Athlete'].value_counts().head(5)


# In[75]:


print("The top 5 players with the most gold medals won is\n", most_gold_medals_player)
print("\n\n")

# In[98]:


india_gold = df[(df['Country'] == 'IND')  & (df['Medal'] == 'Gold')]
india_gold_first = india_gold['Year'].min()
print("The year in which India first won the Gold medal is", india_gold_first)
print("\n\n")

# In[110]:


popular_event = df.groupby('Event')['Athlete'].nunique().sort_values(ascending=False).head(5)
print("The top 5 events that is the most popular in terms of number of players is\n", popular_event)
print("\n\n")

# In[115]:


df_female_gold = df_gold = df[(df['Medal'] == 'Gold') & (df['Gender'] == 'Women')]
most_female_gold = df_female_gold.groupby('Sport')['Athlete'].nunique().sort_values(ascending=False).head(5)
print("The top 5 sports that has the most female gold medalists is\n", most_female_gold)

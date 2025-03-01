

import pandas as pd
import os


# In[2]:


pd.read_excel(r'/Users/terezasaskova/Desktop/python/Data_squirrels.xltx')


# In[3]:


pd.read_csv(r'/Users/terezasaskova/Desktop/python/cleaned_park_data_final.csv')


# In[4]:


squirrel_data = pd.read_excel(r'/Users/terezasaskova/Desktop/python/Data_squirrels.xltx')


# In[5]:


park_data = pd.read_csv(r'/Users/terezasaskova/Desktop/python/cleaned_park_data_final.csv')



# In[6]:


squirrel_data = squirrel_data.dropna(subset=['Area Name','Area ID','Park Name','Highlights in Fur Color','Location','Interactions with Humans','Activities'])


# In[7]:


park_data = park_data.dropna(subset=['Park Conditions','Litter','Temperature & Weather']) 


# In[8]:


merged_data = pd.merge(squirrel_data, park_data, on='Park Name') 


# In[9]:


squirrel_count_per_park = merged_data.groupby('Park Name').size().reset_index(name='squirrel_count')  


# In[10]:


print(squirrel_count_per_park) 


# In[11]:


from sqlalchemy import create_engine


# In[12]:


merged_data = pd.merge(park_data, squirrel_data, on='Park Name', how='outer')
print("\nMerged DataFrame:")
print(merged_data.head())


# In[13]:


squirrel_counts = merged_data['Park Name'].value_counts()
df = squirrel_count_per_park = merged_data.groupby('Park Name').size().reset_index(name='squirrel_count')  


df


# In[14]:


import os

directory = '/Users/terezasaskova/Desktop/Python'
filename = 'squirrel_count_per_park.xlsx'
excel_path = os.path.join(directory, filename)

squirrel_count_per_park.to_excel(excel_path, index=False)

print(f"Excel file saved to {excel_path}")


# In[15]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[16]:


plt.figure(figsize=(10, 6))
sns.barplot(x=squirrel_counts.index, y=squirrel_counts.values)
plt.title('Number of Squirrels in Each Park')
plt.xlabel('Park Name')
plt.ylabel('Number of Squirrels')
plt.xticks(rotation=65,fontsize=5)

download_path = '/Users/terezasaskova/Desktop/Python/squirrels_numbers.jpg'
plt.savefig(download_path)
plt.show()

print(f"Graph saved to {download_path}")



# In[17]:


activity_counts = squirrel_data['Activities'].value_counts()  
df2= activity_counts
   

df2


# In[18]:


squirrel_stats = squirrel_data.describe()
df3 = squirrel_stats


df3


# In[19]:


park_stats = park_data.describe()
df4 = park_stats


df4


# In[20]:


df5= color_distribution = squirrel_data['Primary Fur Color'].value_counts()  

df5


# In[21]:


df6 =squirrels_per_park = merged_data.groupby('Park Name').size().reset_index(name='squirrel_count')  
df6 = pd.DataFrame

df6


# In[22]:


pip install xlsxwriter


# In[23]:


import pandas as pd


# Create DataFrames with the relevant data
squirrel_counts = merged_data['Park Name'].value_counts()
df1 = merged_data.groupby('Park Name').size().reset_index(name='squirrel_count')

activity_counts = squirrel_data['Activities'].value_counts() 
df2 = activity_counts.reset_index().rename(columns={'index': 'Activity', 'Activities': 'Count'})

squirrel_stats = squirrel_data.describe()
df3 = squirrel_stats

park_stats = park_data.describe()
df4 = park_stats

color_distribution = squirrel_data['Primary Fur Color'].value_counts()  
df5 = color_distribution.reset_index().rename(columns={'index': 'Color', 'Primary Fur Color': 'Count'})

squirrels_per_park = merged_data.groupby('Park Name').size().reset_index(name='squirrel_count')
df6 = squirrels_per_park

download_path = '/Users/terezasaskova/Desktop/Python/multiple_dataframes.xlsx'

with pd.ExcelWriter(download_path, engine='xlsxwriter') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
    df3.to_excel(writer, sheet_name='Sheet3')
    df4.to_excel(writer, sheet_name='Sheet4')
    df5.to_excel(writer, sheet_name='Sheet5', index=False)
    df6.to_excel(writer, sheet_name='Sheet6', index=False)

print(f"DataFrames saved to {download_path}")


# In[24]:


print("\nBasic Park Statistics:")
print(park_stats)


# In[25]:


print("\nSquirrel Activity Counts:")
print(activity_counts)


# In[26]:


print("\nSquirrel Color Distribution:")
print(color_distribution)


# In[27]:


print("\nSquirrel Count Per Park:")
print(squirrels_per_park)


# In[28]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# In[29]:


squirrel_file_path = r'/Users/terezasaskova/Desktop/python/Data_squirrels.xltx'
squirrel_data = pd.read_excel(squirrel_file_path)


# In[30]:


park_file_path = r'/Users/terezasaskova/Desktop/python/cleaned_park_data_final.csv'

park_data = pd.read_csv(park_file_path)


# In[31]:


squirrel_data.rename(columns=lambda x: x.strip(), inplace=True)
park_data.rename(columns=lambda x: x.strip(), inplace=True)


# In[32]:


merged_data = pd.merge(park_data, squirrel_data, on='Park Name', how='outer')


# In[33]:


print("\nMerged DataFrame:")
print(merged_data.head())


# In[34]:


approaches_humans_column = 'Interactions with Humans'
eating_column = 'Activities'


# In[35]:


approach_humans_data = squirrel_data[squirrel_data[approaches_humans_column] == 'Approaches']
approach_humans_eating = approach_humans_data[eating_column].value_counts()

df_approach = pd.DataFrame(list(approach_humans_eating.items()), columns=['Activity', 'Frequency'])

download_path = '/Users/terezasaskova/Desktop/Python/approach_humans_eating.csv'
df_approach.to_csv(download_path, index=False)


# In[36]:


not_approach_humans_data = squirrel_data[squirrel_data[approaches_humans_column].isin(['Indifferent', 'Runs from'])]
not_approach_humans_eating = not_approach_humans_data[eating_column].value_counts()

df_not_approach = pd.DataFrame(list(not_approach_humans_eating.items()), columns=['Activity', 'Frequency'])

download_path = '/Users/terezasaskova/Desktop/Python/not_approach_humans_eating.csv'
df_not_approach.to_csv(download_path, index=False)



# In[37]:


print("\nEating frequency for squirrels that approach humans:")
print(approach_humans_eating)


# In[38]:


print("\nEating frequency for squirrels that do not approach humans:")
print(not_approach_humans_eating)



# In[39]:


approach_humans_eating_proportion = (approach_humans_data[eating_column] == 'Eating').mean()
not_approach_humans_eating_proportion = (not_approach_humans_data[eating_column] == 'Eating').mean()


# In[40]:


print(f"\nProportion of squirrels that approach humans and eat: {approach_humans_eating_proportion}")
print(f"Proportion of squirrels that do not approach humans and eat: {not_approach_humans_eating_proportion}")


# In[45]:


import matplotlib.pyplot as plt
import seaborn as sns


approach_humans_eating_proportion = (approach_humans_data[eating_column] == 'Eating').mean()
not_approach_humans_eating_proportion = (not_approach_humans_data[eating_column] == 'Eating').mean()

approach_humans_eating = {'Eating': approach_humans_eating_proportion, 'Not Eating': 1 - approach_humans_eating_proportion}
not_approach_humans_eating = {'Eating': not_approach_humans_eating_proportion, 'Not Eating': 1 - not_approach_humans_eating_proportion}

plt.figure(figsize=(12, 6))

# Plot for squirrels that approach humans
plt.subplot(1, 2, 1)
sns.barplot(x=list(approach_humans_eating.keys()), y=list(approach_humans_eating.values()))
plt.title('Eating Activities of Squirrels That Approach Humans')
plt.xlabel('Activity')
plt.ylabel('Proportion')
plt.xticks(rotation=55)

# Plot for squirrels that do not approach humans
plt.subplot(1, 2, 2)
sns.barplot(x=list(not_approach_humans_eating.keys()), y=list(not_approach_humans_eating.values()))
plt.title('Eating Activities of Squirrels That Do Not Approach Humans', fontsize=12)
plt.xlabel('Activity', fontsize=10)
plt.ylabel('Proportion', fontsize=10)
plt.xticks(rotation=65, fontsize=10)

plt.tight_layout()

# Save the plot to a file
download_path = '/Users/terezasaskova/Desktop/Python/squirrels_eating_activities2.pdf'
plt.savefig(download_path)

# Show the plot
plt.show()


# In[ ]:





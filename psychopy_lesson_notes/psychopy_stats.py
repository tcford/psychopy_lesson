
# coding: utf-8

# <img src=psychopyDocBanner2.gif align="left">

# ### Using the Pandas library to explore the data
# ###### Learning objectives:
# - Use shell commands to navigate to the data folder
# - Import Psychopy data into the Jupyter Notebook
# - Generate descriptive statistics
# - Plot some comparisons by grouping data 

# ----------------

# ---------
# 
# We will set up the notebook and load the additional software library we will need  - "Pandas".
# 
# ----------

# In[1]:

import pandas as pd


# -------
# 
# The Jupyter Notebook understands shell commands as well, we'll use this to find our data. We'll use the exclamation mark to signal that what follows is a shell command rather than Python code.
# 
# ---------

# In[2]:

# print working directory 
get_ipython().system(u'pwd')


# In[3]:

# list files in 'data/'
get_ipython().system(u'ls data/')


# --------
# 
# We can use the 'read_csv' function of Pandas to read the datafile into a pandas DataFrame. A DataFrame will look familiar to anyone who has used Excel or SPSS.
# 
# --------

# In[4]:

# read the csv
df = pd.read_csv('data/tf1_visneuro_2016_Feb_02_1234.csv')
# print the first 5 lines of the DataFrame
df.head()


# In[5]:

# drop the first row (under the header)
# the inplace option allows us to makes changes to the dataframe directly 
# rather than having to save the output to another variable
df.drop(0, inplace=True)
df.head()


# In[6]:

# drop all colums with NA's
df.dropna(axis=1, inplace=True, how='all')
df.head()


# In[7]:

# save out new dataframe as csv
df.to_csv('data/ID001.csv', index=False)

# to read back in you can use:
#df = pd.read_csv('data/ID001.csv')


# ----------
# 
# # Visualising the data
# -----------
# 
# **Now that we have cleaned the data, it might be helpful to visualise it.  
# To do this we need to import some packages. **
# 
# **Matplotlib** is a Python library that produces quality figures and graphs from data.  
# **Seaborn** is a Python library based on matplotlib, which provides additional graphical modifications for matplotlib figures and graphs.
# 
# -------------

# In[8]:

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns # seaborn 

# to see the plots in the workspace we use:
get_ipython().magic(u'matplotlib inline')

# these are seaborn commands, they are used for asthetics
sns.set_color_codes()
sns.set_style('whitegrid')


# -------------
# Create a basic plot of all the columns
# 
# -------------

# In[9]:

df.plot()


# -------------
# The plot is good, but it doesn't actually tell us much.  
# Let's used the package matplotlib.pyplot ('plt'), but first, find out what the function 'plot' in the package does.
# 
# -------------

# In[10]:

get_ipython().magic(u'pinfo plt.plot')


# -------------
# To plot a single column (e.g. reaction time), enter the name of the column (the header) as a **string** in square brackets immediately following the dataframe label as shown below. The column header is the 'index' for that column. In this example, the plot will include the legend.
# 
# -------------

# In[12]:

df['key_resp_3.rt'].plot(legend=True)


# -------------
# Seaborn (sns) has a nice distribution plot to visualise whether the responses are normally disributed.
# 
# -------------

# In[14]:

sns.distplot(df['key_resp_3.rt'])


# -------------
# It is clear from the graphs that the first answer is much longer than the rest of the answers. This is more likely due to it being the first response and therefore it isn't real data. We should filter it out so it doesn't overly affect the result.
# 
# -------------

# In[16]:

df_clean = df[df['key_resp_3.rt'] < .9]


# In[18]:

sns.distplot(df_clean['key_resp_3.rt'])


# ----------
# 
# It's still not looking particularly normal but better. Maybe less than 0.3 would be better still...  
# 
# We can plot the reaction time by the type of image by including the column name 'type_of_image' in parentheses before the index.
# 
# ---------

# In[19]:

df_clean.groupby('type_of_image')['key_resp_3.rt'].plot(legend=True)


# --------
# Creating a variable that groups reation time by the animal type gives some more functionality
# 
# ------

# In[21]:

animal_type_group = df_clean.groupby('type_of_image')['key_resp_3.rt']


# In[44]:

# then we can plot that variable
animal_type_group.plot(legend = True)


# -------
# This doesn't tell us much, but we can now print out the statistics for that variable.
# 
# ------

# In[22]:

animal_type_group.mean()


# In[23]:

print('Mean: ',animal_type_group.mean())
print('SD: ',animal_type_group.std())


# -------
# We can also visualise the reaction time by the type of image as a boxplot
# 
# ------

# In[25]:

df_clean.boxplot('key_resp_3.rt',by = 'type_of_image',)


# -------
# and save plot to the current working directory
# 
# ------

# In[26]:

plt.savefig('ID001_boxplot.png')


# In[ ]:




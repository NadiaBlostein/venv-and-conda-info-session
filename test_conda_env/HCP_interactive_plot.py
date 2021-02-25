#!/usr/bin/env python
# coding: utf-8

# <h3> About this notebook </h3>

# The purpose of this Notebook is to use the conda environment that we created in order to make an interactive plot. It is inspired by Dr. Thomas Bury's CAMBAM-CRM workshop (reference at the end of the notebook).
# 
# Quick parenthesis: Big Gabe hates Jupyter Notebooks; scroll down to the bottom of this one to find out why.

# <h3> Useful Jupyter notebook shortcuts (from Dr. Bury's workshop) </h3>
# <img src='images/jupyter.png' width='40'>
# 
# Outside of cells:
# - A : create new cell above
# - B : create new cell below
# - DD : delete cell
# - Y : make cell of <i>code</i> type
# - M : make cell of <i>text</i> type
# - enter : enter cell
# 
# Within cell:
# - **Cmd + /** : comment/uncomment a line of code
# - **Shift + enter** : run cell
# - **esc** : escape from cell

# <h3> Import required packages </h3>

# In[1]:


import numpy as np # For numerical computation
import pandas as pd # For handling dataframes
import plotly.express as px # For rapid plotting
import plotly.graph_objects as go # For finer plot details


# <h3> Import & clean the data </h3>

# In[2]:


hcp_df = pd.read_csv("HCP_data.csv")


# In[3]:


hcp_df.head()


# In[4]:


hcp_df = hcp_df.fillna(hcp_df.mean())


# In[5]:


hcp_df.columns


# <h3> Create Plot </h3>

# NB: for the plot, you can chose any variable that is part of hcp_df.columns for: x, y, color, size, animation frame and hover name!

# In[6]:


x_axis="TBV"
y_axis="Left Striatum Volume"
x_min=min(hcp_df[x_axis])
x_max=max(hcp_df[x_axis])
y_min=min(hcp_df[y_axis])
y_max=max(hcp_df[y_axis])


# In[7]:


fig = px.scatter(hcp_df, 
                 x=x_axis, 
                 y=y_axis, 
                 range_x=[x_min,x_max],
                 range_y=[y_min,y_max],
                 color='Gender',
                 size="Income",            
                 animation_frame="Age",
                 hover_name="Subject",
                 title="Left striatal volume as a function of TBV"
)
fig.write_html('left_str_by_TBV.html')


# <h3> References </h3>
# 
# To learn more about interactive plots (and if you have issues installing the correct packages), you can go through Dr. Thomas Bury's (thomas.bury@mcgill.ca) CAMBAM-CRM workshop (I have his permission to share it with the lab):
# https://drive.google.com/drive/folders/1b5SwQo_AK6e3JBiYsAl8NJjREIuf35Un
# 
# Jupyter Notebook to work through if you would like to learn more about Pandas:
# https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
# 
# Article on how to put your data into ’tidy’ form in Python is here
# https://www.jeannicholashould.com/tidy-data-in-python.html
# 
# **Finally**, here is a video on why Joel Grus (and Gabriel Devenyi) do NOT like Jupyter Notebooks: https://www.youtube.com/watch?v=7jiPeIFXb6U

# In[ ]:





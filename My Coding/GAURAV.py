#!/usr/bin/env python
# coding: utf-8

# # Explore the Gapminder Dataset with Plotly Express

# ### 1. Loading the necessary labraries

# In[1]:


import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np


# In[2]:


import plotly.express as px
from plotly.figure_factory import create_table


# ### 2. Loading the Data

# In[3]:


gapminder = px.data.gapminder()


# In[4]:


table = create_table(gapminder.head(10))


# In[5]:


py.iplot(table)


# In[6]:


type(gapminder)


# ### 3. Quick Visualizations with Custom Bar Charts

# In[7]:


data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop', height=400)
fig.show()


# In[8]:


fig = px.bar(data_canada, x='year', y='pop',
            hover_data=['lifeExp','gdpPercap'], color='lifeExp',
            labels={'pop': 'population of Canada'}, height=400)
fig.show()


# ### 4. Plot Life Expectancy vs GDP per Capita

# In[9]:


gapminder2007 = gapminder.query("year == 2007")
px.scatter(gapminder2007, x="gdpPercap", y="lifeExp")


# In[10]:


px.scatter(gapminder2007, x='gdpPercap', y='lifeExp', color='continent')


# ### 5. Customize Interactive Bubble Charts

# In[11]:


px.scatter(gapminder2007, x='gdpPercap', y='lifeExp', color='continent',
          size="pop", size_max=60, hover_name="country")


# ### 6. Create Interactive Animations and Facet Plots

# In[12]:


px.scatter(gapminder2007, x='gdpPercap', y='lifeExp', color='continent',
          size="pop", size_max=60, hover_name="country", facet_col="continent", log_x=True)


# In[13]:


fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country", facet_col="continent",
           log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])
fig.show()


# In[ ]:





# In[14]:


px.scatter(gapminder, x="gdpPercap", y="lifeExp", color='continent',
          size="pop", size_max=60, hover_name="country", animation_frame='year',
          animation_group="country", log_x=True, range_x=[100,100000],range_y=[25,90],
          labels=dict(pop="Population", gdpPercap="GDP per Capita", lifeExp="Life Expenctancy"))


# ### 7. Represent Geographic Data as Animated Maps

# In[15]:


px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country",
             animation_frame="year", color_continuous_scale=px.colors.sequential.Plasma,
             projection="natural earth")


# In[16]:


px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country",
             animation_frame="year", color_continuous_scale=px.colors.sequential.Plasma,
             projection="orthographic")


# In[17]:


fig = px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year", range_color=[20,80])
fig.show()


# In[ ]:





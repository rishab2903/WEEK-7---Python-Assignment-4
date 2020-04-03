#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
Location = "~/Downloads/learn-data-analysis-w-python-master/datasets/gradedata.csv"
df = pd.read_csv(Location)
bins=[0,80,100]
group_names=['A','B']
df['lettergrade']=pd.cut(df['grade'],bins,labels=group_names)
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





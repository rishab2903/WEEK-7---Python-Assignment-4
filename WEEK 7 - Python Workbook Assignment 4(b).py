#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
df = pd.read_csv('~/Downloads/learn-data-analysis-w-python-master/datasets/gradedata.csv')
df
import numpy as np
df['timemgmt']=np.where((df['exercise']>3)&(df['hours']>17),'busy','idle')
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





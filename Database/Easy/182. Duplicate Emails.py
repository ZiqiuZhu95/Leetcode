# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:38:39 2020

@author: Ziqiu Zhu
"""

#%%

import pandas as pd
import numpy as np

data = np.array([[1,2,3],['a@b.com', 'c@d.com', 'a@b.com']]).T

df = pd.DataFrame(data,
                  columns = ['Id', 'Email'])

df.head()

#%%

#return all duplicates
grouped = df.groupby('Email').count()
grouped[grouped['Id']> 1].index
    

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:43:58 2020

@author: Ziqiu Zhu
"""

#%% BIG COUNTRIES EASY
import pandas as pd
import numpy as np

data =  np.array([['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'],
                 ['Asia', 'Europe', 'Africa', ' Europe', 'Africa'],
                 [652230, 28748, 2381741,468, 1246700],
                 [25500100, 2831741, 37100000, 78155, 20609294],
                 [20343000, 12960000, 188681000, 3712000, 10099000]]).T

df = pd.DataFrame(data,
                  columns = ['name', 'continent', 'area', 'population', 'gdp'])

df.head()

#%%
# want to output name, population and area for Afghanistan and Algeria

df.loc[[0,2], ['name', 'population', 'area']]
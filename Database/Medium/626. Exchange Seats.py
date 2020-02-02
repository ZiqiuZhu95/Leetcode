# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:19:36 2020

@author: Ziqiu Zhu
"""

#%%
# Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.
# The column id is continuous increment.
# Mary wants to change seats for the adjacent students.

import pandas as pd
import numpy as np

data =  np.array([['Abbott', 'Doris', 'Emerson', 'Green', 'James']]).T

df = pd.DataFrame(data, 
                  columns = ['student'])

df.head()

#%%

#this means that every even-indexed student has to switch spots with the
#student after them (startnig at index 0).

for row in range(len(df.index)):
    if (row + 1) % 2 == 0:
        temp1,temp2 = df.iloc[row].copy(), df.iloc[row-1].copy()
        df.iloc[row] = temp2
        df.iloc[row-1] = temp1
        
df.head()


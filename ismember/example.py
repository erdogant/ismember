# Example
# -------

import numpy as np
from ismember import ismember
import pandas as pd

# %% Example 1

a_vec  = [1,2,3,None]
b_vec  = [4,1,2]
[I,idx] = ismember(a_vec,b_vec)
np.array(a_vec)[I]
np.array(b_vec)[idx]

# %% Example 2

a_vec   = pd.DataFrame(['aap','None','mies','aap','boom','mies',None,'mies','mies','pies',None])
b_vec   = pd.DataFrame([None,'mies','mies','pies',None])
[I,idx] = ismember(a_vec,b_vec)
a_vec.values[I]
b_vec.values[idx].flatten()

# %% Example 3

a_vec   = np.array([1,2,3,None])
b_vec   = np.array([1,2,4])
[I,idx] = ismember(a_vec,b_vec)
a_vec[I]
b_vec[idx]


# %% Example 4

a_vec   = np.array(['boom','aap','mies','aap'])
b_vec   = np.array(['aap','boom','aap'])
[I,idx] = ismember(a_vec,b_vec)
a_vec[I]
b_vec[idx]

# %% Example 5

a_vec = np.random.randint(0,10,(5,8))
b_vec = np.random.randint(0,10,(5,10))
Iloc, idx = ismember(a_vec, b_vec, 'rows')

i=0
a_vec[i,Iloc[i]]==b_vec[i,idx[i]]


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

# %%
from datetime import datetime

t1=[]
t2=[]
ns = np.random.randint(10,10000,1000)

for n in ns:
    a_vec = np.random.randint(0,100,n)
    b_vec = np.random.randint(0,100,n)
    # Run stack version
    start = datetime.now()
    out1=ismember_stack(a_vec, b_vec)
    end = datetime.now()
    t1.append(end - start)

    # Run ismember
    start = datetime.now()
    out2=ismember(a_vec, b_vec)
    end = datetime.now()
    t2.append(end - start)

#
print(np.sum(t1))
# ismember pypi
print(np.sum(t2))

# %%
def ismember_stack(a, b):
    bind = {}
    for i, elt in enumerate(b):
        if elt not in bind:
            bind[elt] = i
    return [bind.get(itm, None) for itm in a]  # None can be replaced by any other "not in b" value

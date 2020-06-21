# pytest test_ismember.py
import numpy as np
import pandas as pd
from ismember import ismember

def test_ismember():
    # Test 1
    a_vec  = [1,2,3,None]
    b_vec  = [4,1,2]
    [I,idx] = ismember(a_vec,b_vec)
    assert np.all(np.array(a_vec)[I]==np.array(b_vec)[idx])

    # Test 2    
    a_vec = pd.DataFrame(['aap','None','mies','aap','boom','mies',None,'mies','mies','pies',None])
    b_vec = pd.DataFrame([None,'mies','mies','pies',None])
    [I,idx] = ismember(a_vec,b_vec)
    assert np.all(a_vec.values[I] == b_vec.values[idx].flatten())
    
    # Test 3
    a_vec   = np.array([1,2,3,None])
    b_vec   = np.array([1,2,4])
    [I,idx] = ismember(a_vec,b_vec)
    assert np.all(a_vec[I]==b_vec[idx])
    
    # Test 4
    a_vec   = np.array(['boom','aap','mies','aap'])
    b_vec   = np.array(['aap','boom','aap'])
    [I,idx] = ismember(a_vec,b_vec)
    assert np.all(a_vec[I]==b_vec[idx])

    # Test 5: matrices
    a_vec = np.random.randint(0,10,(5,8))
    b_vec = np.random.randint(0,10,(5,10))
    Iloc, idx = ismember(a_vec, b_vec, 'rows')
    
    for i in np.arange(0,a_vec.shape[0]):
        assert np.all(a_vec[i,Iloc[i]]==b_vec[i,idx[i]])

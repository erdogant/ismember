from ismember.ismember import ismember

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '0.2.1'

# module level doc-string
__doc__ = """
ismember
=====================================================================

Description
-----------
ismember returns array elements that are members of set array.

Example
-------
>>> from ismember import ismember
>>> import numpy as np
>>>
>>> a_vec = np.array([1,2,3,None])
>>> b_vec = np.array([4,1,2])
>>> Iloc,idx = ismember(a_vec,b_vec)
>>> a_vec[Iloc] == b_vec[idx]
>>>
>>> # Example with matrices
>>> a_vec = np.random.randint(0,10,(5,8))
>>> b_vec = np.random.randint(0,10,(5,10))
>>> Iloc, idx = ismember(a_vec, b_vec, 'elementwise')
>>> # Evaluate the result for the first record:
>>> i=3
>>> a_vec[i,Iloc[i]]==b_vec[i,idx[i]]
>>>
>>> # Row wise comparison
>>> a_vec = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)))
>>> b_vec = np.array(((4, 5, 6), (7, 8, 0)))
>>> Iloc, idx = ismember(a_vec, b_vec, 'rows')
>>> a_vec[Iloc]==b_vec[idx]


References
----------
https://github.com/erdogant/ismember

"""
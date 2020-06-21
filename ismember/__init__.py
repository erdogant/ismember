from ismember.ismember import ismember

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '0.1.3'

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
>>> a_vec = np.array([1,2,3,None])
>>> b_vec = np.array([4,1,2])
>>> Iloc,idx = ismember(a_vec,b_vec)
>>> a_vec[Iloc] == b_vec[idx]
>>>
>>> #Example with matrices
>>> a_vec = np.random.randint(0,10,(5,8))
>>> b_vec = np.random.randint(0,10,(5,10))
>>> Iloc, idx = ismember(a_vec, b_vec, 'rows')
>>> # Evaluate the result for the first record:
>>> i=0
>>>a_vec[i,Iloc[i]]==b_vec[i,idx[i]]


References
----------
https://github.com/erdogant/ismember

"""
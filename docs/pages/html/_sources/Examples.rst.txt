Check whether the elements of X are present in Y
###############################################################

In the following example, the ``ismember`` function checks whether the elements present in X are also present in Y and returns the logical values in the form of True (1) and False (0). The first value of X i.e. 4 is present in Y, so the first value of the resultant LX is 1. Similarly, the values at the 3rd and 4th positions are also present in the Y, so the resultant values are 1. Since the value at 2nd position i.e. 6 is not present in Y, so the resultant value is 0.


.. code:: python

	X = [4, 6, 3, 2]
	Y = [1, 2, 4, 5, 3, 8]
	LX, _ = ismember(X, Y)

	print(LX)
	# array([ True, False,  True,  True])


Determine the corresponding location of the values that are present in Y array
################################################################################

In the underneath example, the ``ismember`` function first checks whether the values present in X are also a part of Y. It subsequently returns the values in the form of True and False which can be seen in LX. After that, we have given another variable in syntax to determine the lowest index of the values of X that are present in Y. So, the first element of X i.e.4 is present in Y at only position 3, so it will return 3. The second element which is present in Y is 3 and the respective position is 5, 2 is present in the 2nd position in Y. If the values are not present in Y, then the location value will be 0.


.. code:: python

	X = [4, 6, 3, 2]
	Y = [1, 2, 4, 5, 3, 8]
	LX, LocY = ismember(X,Y)

	print(LX)
	# array([ True, False,  True,  True])

	print(LocY)
	# array([2, 4, 1], dtype=int64)


Row wise comparison (1)
##################################################

.. code:: python

	X = np.array(((1, 2, 4, 7),
			  (3, 4, 5, 9)))

	Y = np.array(((13, 4, 5, 9),
			  (0, 3, 8, 7),
			  (3, 4, 5, 9)))

	LX, LocY = ismember(X, Y, 'rows')

	print(LX)
	# array([False,  True])

	print(LocY)
	# array([2]


Row wise comparison (2)
########################

.. code:: python

	a_vec = np.array(((1, 2, 3),
			  (4, 5, 6),
			  (7, 8, 9),
			  (10, 11, 12),
			  (4, 5, 6)))

	b_vec = np.array(((4, 5, 6),
			  (7, 8, 0),
			  (10, 11, 12)))

	Lia, Locb = ismember(a_vec, b_vec, 'rows')

	print(a_vec[Lia])
	print(b_vec[Locb])

	# 
	# [[ 4  5  6]
	#  [10 11 12]
	#  [ 4  5  6]]
	# [[ 4  5  6]
	#  [10 11 12]
	#  [ 4  5  6]]



Elementwise comparison
########################

.. code:: python

	a_vec = np.random.randint(0,10,(5,8))
	b_vec = np.random.randint(0,10,(5,10))
	Iloc, idx = ismember(a_vec, b_vec, 'elementwise')

	print(a_vec)
	# [[6 8 9 0 3 3 9 4]
	#  [5 8 4 9 9 6 9 7]
	#  [4 7 0 9 0 7 7 9]
	#  [5 0 4 1 3 0 3 6]
	#  [3 5 6 2 2 8 2 6]]

	 print(b_vec)
	# [[7 5 8 9 3 1 8 1 9 3]
	#  [7 3 1 0 2 2 2 3 3 6]
	#  [8 0 1 7 2 3 3 1 7 6]
	#  [8 1 8 1 3 3 9 9 7 4]
	#  [1 5 0 5 9 8 2 2 0 6]]
	
	# The following is identical
	i=0
	a_vec[i,Iloc[i]]==b_vec[i,idx[i]]


String input
########################

.. code:: python

	a_vec   = np.array(['boom','aap','mies','aap'])
	b_vec   = np.array(['aap','boom','aap'])
	[I,idx] = ismember(a_vec,b_vec)

	print(a_vec[I])
	print(b_vec[idx])

	# ['boom' 'aap' 'aap']
	# ['boom' 'aap' 'aap']



Handling None
########################

.. code:: python

	a_vec  = [1,2,3,None]
	b_vec  = [4,1,2]
	I, idx = ismember(a_vec,b_vec)

	# Collect same elements
	print(np.array(a_vec)[I])
	print(np.array(b_vec)[idx])

	# [1 2]
	# [1 2]


Pandas Dataframes
########################

.. code:: python

	a_vec   = pd.DataFrame(['aap','None','mies','aap','boom','mies',None,'mies','mies','pies',None])
	b_vec   = pd.DataFrame([None,'mies','mies','pies',None])

	[I,idx] = ismember(a_vec,b_vec)
	
	# Check whether the results are correct
	a_vec.values[I] == b_vec.values[idx].flatten()





[1] https://www.datacamp.com/community/tutorials/pickle-python-tutorial


.. raw:: html

	<hr>
	<center>
		<script async type="text/javascript" src="//cdn.carbonads.com/carbon.js?serve=CEADP27U&placement=erdogantgithubio" id="_carbonads_js"></script>
	</center>
	<hr>

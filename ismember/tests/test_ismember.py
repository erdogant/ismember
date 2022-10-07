# pytest test_ismember.py
import numpy as np
import pandas as pd
from ismember import ismember
import unittest

class TestCLUSTIMAGE(unittest.TestCase):

	def test_ismember(self):
		# Test 1
		a_vec  = [1,2,3,None]
		b_vec  = [4,1,2]
		I, idx = ismember(a_vec,b_vec)
		assert np.all(np.array(a_vec)[I]==np.array(b_vec)[idx])

		# Test 2    
		a_vec = pd.DataFrame(['aap','None','mies','aap','boom','mies',None,'mies','mies','pies',None])
		b_vec = pd.DataFrame([None,'mies','mies','pies',None])
		I, idx = ismember(a_vec,b_vec)
		assert np.all(a_vec.values[I] == b_vec.values[idx].flatten())

		# Test 3
		a_vec   = np.array([1,2,3,None])
		b_vec   = np.array([1,2,4])
		[, idx = ismember(a_vec,b_vec)
		assert np.all(a_vec[I]==b_vec[idx])

		# Test 4
		a_vec   = np.array(['boom','aap','mies','aap'])
		b_vec   = np.array(['aap','boom','aap'])
		I, idx = ismember(a_vec,b_vec)
		assert np.all(a_vec[I]==b_vec[idx])

		# Test 5: elements matrices
		a_vec = np.random.randint(0,10,(5,8)).astype(str)
		b_vec = np.random.randint(0,10,(5,10)).astype(str)
		Iloc, idx = ismember(a_vec, b_vec, 'elementwise')
		for i in np.arange(0,a_vec.shape[0]):
			assert np.all(a_vec[i,Iloc[i]]==b_vec[i,idx[i]])

		# Test 5: elements matrices
		a_vec = np.random.randint(0,10,(5,8)).astype(str)
		b_vec = np.random.randint(0,10,(5,10)).astype(str)
		Iloc, idx = ismember(a_vec, b_vec, 'elementwise')
		for i in np.arange(0,a_vec.shape[0]):
			assert np.all(a_vec[i,Iloc[i]]==b_vec[i,idx[i]])

		# Test rows
		a_vec = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (4, 5, 6)))
		b_vec = np.array(((4, 5, 6), (7, 8, 0), (10, 11, 12)))
		Lia, Locb = ismember(a_vec, b_vec, 'rows')
		assert np.all(a_vec[Lia]==b_vec[Locb])

	def test_ismember_objects(self):

		# Test 2    
		a_vec = pd.DataFrame(['aap','None','mies','aap','boom','mies',None,'mies','mies','pies',None]).astype('O')
		b_vec = pd.DataFrame([None,'mies','mies','pies',None]).astype('O')
		I, idx = ismember(a_vec,b_vec)
		assert np.all(a_vec.values[I] == b_vec.values[idx].flatten())

		# Test 3
		a_vec   = np.array([1,2,3,None]).astype('O')
		b_vec   = np.array([1,2,4]).astype('O')
		I, idx = ismember(a_vec,b_vec)
		assert np.all(a_vec[I]==b_vec[idx])

		# Test 4
		a_vec   = np.array(['boom','aap','mies','aap']).astype('O')
		b_vec   = np.array(['aap','boom','aap']).astype('O')
		I, idx = ismember(a_vec,b_vec)
		assert np.all(a_vec[I]==b_vec[idx])

		# Test 5: elements matrices
		a_vec = np.random.randint(0,10,(5,8)).astype('O')
		b_vec = np.random.randint(0,10,(5,10)).astype('O')
		Iloc, idx = ismember(a_vec, b_vec, 'elementwise')
		for i in np.arange(0,a_vec.shape[0]):
			assert np.all(a_vec[i,Iloc[i]]==b_vec[i,idx[i]])

		# Test 5: elements matrices
		a_vec = np.random.randint(0,10,(5,8)).astype('O')
		b_vec = np.random.randint(0,10,(5,10)).astype('O')
		Iloc, idx = ismember(a_vec, b_vec, 'elementwise')
		for i in np.arange(0,a_vec.shape[0]):
			assert np.all(a_vec[i,Iloc[i]]==b_vec[i,idx[i]])

		# Test rows
		a_vec = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (4, 5, 6))).astype('O')
		b_vec = np.array(((4, 5, 6), (7, 8, 0), (10, 11, 12))).astype('O')
		Lia, Locb = ismember(a_vec, b_vec, 'rows')
		assert np.all(a_vec[Lia]==b_vec[Locb])
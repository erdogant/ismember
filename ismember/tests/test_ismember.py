# pytest test_ismember.py
import numpy as np
import pandas as pd
from ismember import ismember, is_row_in
import unittest

class TestCLUSTIMAGE(unittest.TestCase):

    def test_fillna_inplace_compatibility(self):
        """Ensure None/NaN in pandas DataFrames are replaced with 'NaN' string in-place, compatible with newer pandas that dropped inplace= from extension arrays."""
        a_vec = pd.DataFrame(['aap', None, 'mies']).astype('O')
        b_vec = pd.DataFrame([None, 'mies']).astype('O')
        
        I, idx = ismember(a_vec, b_vec)
        
        # Original DataFrames must be modified in-place: None -> 'NaN'
        assert a_vec.values[1, 0] == 'NaN', "None in a_vec should be replaced with 'NaN' in-place"
        assert b_vec.values[0, 0] == 'NaN', "None in b_vec should be replaced with 'NaN' in-place"
        
        # Results should match correctly
        assert list(a_vec.values[I]) == ['NaN', 'mies']
        assert list(b_vec.values[idx].flatten()) == ['NaN', 'mies']
        
    def test_ismember(self):
        # Test 1
        a_vec  = [1,2,3,None]
        b_vec  = [4,1,2]
        I, idx = ismember(a_vec,b_vec)
        assert list(np.array(a_vec)[I]) == [1, 2]
        assert list(np.array(b_vec)[idx]) == [1, 2]
        assert np.all(np.array(a_vec)[I]==np.array(b_vec)[idx])

        # Test 2
        a_vec = pd.DataFrame(['aap','None','mies','aap','boom','mies',None,'mies','mies','pies',None])
        b_vec = pd.DataFrame([None,'mies','mies','pies',None])
        I, idx = ismember(a_vec, b_vec)
        assert list(a_vec.values[I]) == ['mies', 'mies', 'NaN', 'mies', 'mies', 'pies', 'NaN']
        assert list(b_vec.values[idx].flatten()) == ['mies', 'mies', 'NaN', 'mies', 'mies', 'pies', 'NaN']
        assert np.all(a_vec.values[I] == b_vec.values[idx].flatten())

        # Test 3
        a_vec = np.array([1,2,3,None])
        b_vec = np.array([1,2,4])
        I, idx = ismember(a_vec, b_vec)
        assert list(a_vec[I]) == [1, 2]
        assert list(b_vec[idx]) == [1, 2]
        assert np.all(a_vec[I] == b_vec[idx])

        # Test 4
        a_vec = np.array(['boom','aap','mies','aap'])
        b_vec = np.array(['aap','boom','aap'])
        I, idx = ismember(a_vec, b_vec)
        assert list(a_vec[I]) == ['boom', 'aap', 'aap']
        assert list(b_vec[idx]) == ['boom', 'aap', 'aap']
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
        assert np.all(a_vec[Lia] == np.array([[ 4,  5,  6], [10, 11, 12], [ 4,  5,  6]]))
        assert np.all(b_vec[Locb] == np.array([[ 4,  5,  6], [10, 11, 12], [ 4,  5,  6]]))
        assert np.all(a_vec[Lia]==b_vec[Locb])

    def test_ismember_objects(self):
        # Test 2
        a_vec = pd.DataFrame(['aap','None','mies','aap','boom','mies',None,'mies','mies','pies',None]).astype('O')
        b_vec = pd.DataFrame([None,'mies','mies','pies',None]).astype('O')
        I, idx = ismember(a_vec,b_vec)
        assert list(a_vec.values[I]) == ['mies', 'mies', 'NaN', 'mies', 'mies', 'pies', 'NaN']
        assert list(b_vec.values[idx].flatten()) == ['mies', 'mies', 'NaN', 'mies', 'mies', 'pies', 'NaN']
        assert np.all(a_vec.values[I] == b_vec.values[idx].flatten())

        # Test 3
        a_vec = np.array([1,2,3,None]).astype('O')
        b_vec = np.array([1,2,4]).astype('O')
        I, idx = ismember(a_vec,b_vec)
        assert list(a_vec[I]) == [1, 2]
        assert list(b_vec[idx]) == [1, 2]
        assert np.all(a_vec[I]==b_vec[idx])

        # Test 4
        a_vec = np.array(['boom','aap','mies','aap']).astype('O')
        b_vec = np.array(['aap','boom','aap']).astype('O')
        I, idx = ismember(a_vec,b_vec)
        assert list(a_vec[I]) == ['boom', 'aap', 'aap']
        assert list(b_vec[idx]) == ['boom', 'aap', 'aap']
        assert np.all(a_vec[I] == b_vec[idx])

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

class TestIsmemberStress(unittest.TestCase):
    def test_large_array(self):
        # Large 1D arrays
        a_vec = np.random.randint(0, 100000, size=1000000)
        b_vec = np.random.randint(0, 100000, size=1000000)
        I, idx = ismember(a_vec, b_vec)
        # Just check that output shapes are correct and no crash
        assert I.shape == a_vec.shape
        assert idx.shape[0] == np.sum(I)

    def test_large_2d_elementwise(self):
        # Large 2D arrays for elementwise
        a_vec = np.random.randint(0, 1000, size=(100, 1000))
        b_vec = np.random.randint(0, 1000, size=(100, 1200))
        Iloc, idx = ismember(a_vec, b_vec, 'elementwise')
        assert len(Iloc) == a_vec.shape[0]
        assert len(idx) == a_vec.shape[0]
        for i in np.arange(0,a_vec.shape[0]):
            assert np.all(a_vec[i,Iloc[i]]==b_vec[i,idx[i]])

    def test_large_2d_rows(self):
        # Large 2D arrays for rows
        a_vec = np.random.randint(0, 1000, size=(1000, 10))
        b_vec = np.random.randint(0, 1000, size=(500, 10))
        Iloc, idx = ismember(a_vec, b_vec, 'rows')
        assert Iloc.shape[0] == a_vec.shape[0]
        assert idx.shape[0] == np.sum(Iloc)

    def test_all_elements_match(self):
        # All elements in a_vec are in b_vec
        a_vec = np.arange(1000)
        b_vec = np.arange(1000)
        I, idx = ismember(a_vec, b_vec)
        assert np.all(I)
        assert np.all(a_vec[I] == b_vec[idx])

    def test_no_elements_match(self):
        # No elements in a_vec are in b_vec
        a_vec = np.arange(1000)
        b_vec = np.arange(1000, 2000)
        I, idx = ismember(a_vec, b_vec)
        assert not np.any(I)
        assert idx.shape[0] == 0

    def test_empty_arrays(self):
        # Empty input arrays
        a_vec = np.array([])
        b_vec = np.array([])
        I, idx = ismember(a_vec, b_vec)
        assert I.shape == (0,)
        assert idx.shape == (0,)

    def test_nan_and_none(self):
        # Arrays with NaN and None
        a_vec = np.array([np.nan, None, 1, 2, 3], dtype=object)
        b_vec = np.array([None, np.nan, 2, 4], dtype=object)
        I, idx = ismember(a_vec, b_vec)
        assert list(a_vec[I]) == [np.nan, None, 2]
        assert list(b_vec[idx]) ==[np.nan, None, 2]
        # Should find None and 2, but not NaN (since NaN != NaN)
        assert I[1]          # None
        assert I[3]          # 2
        assert I[0]          # NaN
        assert not I[2]      # 1
        assert not I[4]      # 3

    def test_is_row_in_shape_and_behavior(self):
        boundaries = np.array([
            [1,2],
            [3,4],
            [6,7],
            [10,11]
        ])
        local_edges = np.array([
            [6,7],
            [3,4],
            [12,3]
        ])
        is_local_boundary = is_row_in(boundaries, local_edges)
        # Should be 1D boolean array of length 4
        assert isinstance(is_local_boundary, np.ndarray)
        assert is_local_boundary.dtype == bool
        assert is_local_boundary.shape == (4,)
        # Check correct rows are marked True
        expected = np.array([False, True, True, False])
        assert np.all(is_local_boundary == expected)

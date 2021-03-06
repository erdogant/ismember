# ismember

[![Python](https://img.shields.io/pypi/pyversions/ismember)](https://img.shields.io/pypi/pyversions/ismember)
[![PyPI Version](https://img.shields.io/pypi/v/ismember)](https://pypi.org/project/ismember/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/ismember/blob/master/LICENSE)
[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)
[![Downloads](https://pepy.tech/badge/ismember)](https://pepy.tech/project/ismember)


* Python package ismember returns array elements that are members of set array

## Contents
- [Installation](#-installation)
- [Contribute](#-contribute)
- [License](#-copyright)

## Installation
* Install ismember from PyPI (recommended). ismember is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* It is distributed under the MIT license.


```bash
pip install ismember
```

* Alternatively, install ismember from the GitHub source:
```bash
git clone https://github.com/erdogant/ismember.git
cd ismember
python setup.py install
```  

### Import ismember package
```python
from ismember import ismember
```

### Example:
```python
import numpy as np
from ismember import ismember

# Example with lists
a_vec  = [1,2,3,None]
b_vec  = [4,1,2]
[I,idx] = ismember(a_vec,b_vec)
np.array(a_vec)[I]
np.array(b_vec)[idx]

# Example with DataFrames
a_vec   = pd.DataFrame(['aap','None','mies','aap','boom','mies',None,'mies','mies','pies',None])
b_vec   = pd.DataFrame([None,'mies','mies','pies',None])
[I,idx] = ismember(a_vec,b_vec)
a_vec.values[I]
b_vec.values[idx]

a_vec   = np.array([1,2,3,None])
b_vec   = np.array([1,2,4])
[I,idx] = ismember(a_vec,b_vec)
a_vec[I]
b_vec[idx]

# Example with Numpy array
a_vec   = np.array(['boom','aap','mies','aap'])
b_vec   = np.array(['aap','boom','aap'])
[I,idx] = ismember(a_vec,b_vec)
a_vec[I]
b_vec[idx]

# Example with matrices
# Create two random matrices
a_vec = np.random.randint(0,10,(5,8))
b_vec = np.random.randint(0,10,(5,10))
# Row-wise comparison
Iloc, idx = ismember(a_vec, b_vec, 'rows')
# Print results for the first row:
i=0
a_vec[i,Iloc[i]]==b_vec[i,idx[i]]

```

### References
* https://in.mathworks.com/help/matlab/ref/ismember.html
   
### Maintainer
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
* Contributions are welcome.
* If you wish to buy me a <a href="https://erdogant.github.io/donate/?currency=USD&amount=5">Coffee</a> for this work, it is very appreciated :)

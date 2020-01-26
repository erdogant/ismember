# ismember

[![Python](https://img.shields.io/pypi/pyversions/ismember)](https://img.shields.io/pypi/pyversions/ismember)
[![PyPI Version](https://img.shields.io/pypi/v/ismember)](https://pypi.org/project/ismember/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/ismember/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/ismember/week)](https://pepy.tech/project/ismember/week)
[![Donate](https://img.shields.io/badge/donate-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)

* Python package ismember returns array elements that are members of set array

## Contents
- [Installation](#-installation)
- [Requirements](#-Requirements)
- [Quick Start](#-quick-start)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

## Installation
* Install ismember from PyPI (recommended). ismember is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* It is distributed under the MIT license.

## Requirements
pip install numpy
```
## Quick Start
```

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
import ismember as ismember
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

```

### References
* https://in.mathworks.com/help/matlab/ref/ismember.html
   
### Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)

### Contribute
* Contributions are welcome.

### Licence
See [LICENSE](LICENSE) for details.

### Donation
* This package is created and maintained in my free time. If this package is usefull, you can show your <a href="https://erdogant.github.io/donate/?currency=USD&amount=5">gratitude</a> :) Thanks!

# ismember

[![Python](https://img.shields.io/pypi/pyversions/ismember)](https://img.shields.io/pypi/pyversions/ismember)
[![PyPI Version](https://img.shields.io/pypi/v/ismember)](https://pypi.org/project/ismember/)
![GitHub Repo stars](https://img.shields.io/github/stars/erdogant/ismember)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/ismember/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/ismember)](https://pepy.tech/project/ismember)
[![Downloads](https://pepy.tech/badge/ismember/month)](https://pepy.tech/project/ismember/)
[![Sphinx](https://img.shields.io/badge/Sphinx-Docs-Green)](https://erdogant.github.io/ismember/)
<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->

``ismember`` is a Python library that checks whether the elements in X is present in Y. 


# 
**⭐️ Star this repo if you like it ⭐️**
# 


### [Documentation pages](https://erdogant.github.io/ismember/)

On the [documentation pages](https://erdogant.github.io/ismember/) you can find more information about ``ismember`` with examples. 

# 

##### Install ismember from PyPI
```bash
pip install ismember     # normal install
pip install -U ismember  # update if needed
```


### Import ismember package
```python
from ismember import ismember
```
<hr>

#### Quick example

Use the documentation pages for more detailed usage. Some of the most used functionalities are linked below.

```python

from ismember import ismember

# Example with lists
I, idx = ismember([1,2,3,None], [4,1,2])
I, idx = ismember(["1","2","3"], ["4","1","2"])
```


#

#### [Example: Check whether the elements of X are present in Y](https://erdogant.github.io/ismember/pages/html/Examples.html#)

#

#### [Example: Determine the corresponding location of the values that are present in Y array](https://erdogant.github.io/ismember/pages/html/Examples.html#determine-the-corresponding-location-of-the-values-that-are-present-in-y-array)

#

#### [Example: Row wise comparison](https://erdogant.github.io/ismember/pages/html/Examples.html#row-wise-comparison-1)

#

#### [Example: Elementwise comparison](https://erdogant.github.io/ismember/pages/html/Examples.html#elementwise-comparison)

<hr> 

### References
* https://in.mathworks.com/help/matlab/ref/ismember.html

### Maintainer
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
* Contributions are welcome.
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)

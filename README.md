## Lazy function application over text files

#### Usage
```python

from lazyfile.utils import *
from nltk import word_tokenize

with LazyFile('text.txt') as handle:
    generator = handle.apply(word_tokenize)
    # do something

```

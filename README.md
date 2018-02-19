## Lazy function application over text files

#### Usage
```python

from utils import *
from nltk import word_tokenize

if __name__ == '__main__':
    with Lazyfile('text.txt') as handle:
        generator = handle.apply(word_tokenize)
        # do something with tokenized data

```

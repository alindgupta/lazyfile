## Lazy function application over text files
[![Build Status](https://travis-ci.org/alindgupta/lazyfile.svg?branch=master)](https://travis-ci.org/alindgupta/lazyfile)

#### Usage
```python

from utils import *
from nltk import word_tokenize

if __name__ == '__main__':
    with Lazyfile('text.txt') as handle:
        generator = handle.apply(word_tokenize)
        # do something with tokenized data

```

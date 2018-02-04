"""
utils.py
~~~~~~~~
Lazy function application over text.
"""

import os
from functools import partial


# Note: This function should not be used directly.
# _fst_arg_last is a helper function for `LazyFile.map_function`
def _fst_arg_last(func):
    """ Returns a new function whose final parameter
    is the first parameter of the function arglist
    eg. fst_arg_last will do the following manipulation
    on a function named tokenize

    For example,
    ```python
    tokenize(string, separator=' ', language='english')
    ```
    is transformed into
    ```python
    tokenize(separator=' ', language='english', string)
    ```

    Parameters
    ----------
    func: callable(A,B,C,..)
      A function/callable.

    Returns
    -------
    A callable(B,C,..,A)

    """
    def inner(*args, **kwargs):
        args = args[1:] + (args[0],)
        return func(*args, **kwargs)
    return inner


class LazyFile:
    """ Lazily read a text file and apply a function to each line

    Usage requires the use of a context-manager so files can be closed
    appropriately.

    """
    def __init__(self, filename: str, buf=-1, enc='utf-8'):
        if not os.path.isfile(filename):
            raise IOError(f'Could not find {filename}')
        self.context_managed = False
        self._file = filename           # filename
        self._fhandle = None            # file handle
        self.lines = None               # line iterator
        self.buf = buf
        self.enc = enc

    # context manager - enter clause
    def __enter__(self):
        self._fhandle = open(self._file, 'r', self.buf, self.enc)
        self.lines = (line for line in self._fhandle)
        self.context_managed = True
        return self

    # context manager - exit clause
    def __exit__(self, exec_type, exec_value, traceback):
        if exec_type is not None:
            print(exec_type, exec_value, traceback)
        if self._fhandle:
            self._fhandle.close()
        else:
            raise Exception('Improperly closed file!')

    @property
    def file(self):
        return self._file

    def apply(self, func, *args, **kwargs):
        """ Apply function to lines from file

        Parameters
        ----------
        func: Callable[[str], Any]
          A function that operates on strings.

        Optional args and kwargs for func.

        Returns
        -------
        A generator.

        """
        if not self.context_managed:
            raise Exception('Object must be initialized with context manager')
        try:
            yield from (func(line, *args, **kwargs) for line in self.lines)
        except Exception:
            raise

    def map_function(self, func, *args, **kwargs):
        """ Another (lazier) version of apply using Python's `map` function

        Parameters
        ----------
        func: Callable[[str], Any]
          A function that operates on strings.

        Optional args and kwargs for func.

        Returns
        -------
        A generator.

        """
        if not self.context_managed:
            raise Exception('Object must be initialized with context manager')
        try:
            yield from map(
                func if not args else partial(
                    _fst_arg_last(func),
                    *args,
                    **kwargs),
                self.lines)
        except Exception:
            raise

""" """

import os
from functools import partial
from typing import Callable, Any, Generator


def fst_arg_last(func: Callable) -> Callable:
    """ 
    Returns a new function whose final parameter
    is the first parameter of the function arglist
    eg. fst_arg_last will do the following manipulation
    on a function named tokenize
    
    tokenize(string, separator=' ', language='english')
    -> tokenize(separator=' ', language='english' string)
    
    :param func: callable(A,B,C,..)
    :return: callable(B,C,..,A)
    
    """
    def inner(*args, **kwargs):
        args = args[1:] + (args[0],)
        return func(*args, **kwargs)
    return inner


class LazyFileReader:
    """
    
    Lazily read a text file and apply a function to each line
    
    Usage: requires the use of a context-manager so files can be closed
    appropriately
    
    """

    def __init__(self, filename: str, buf=-1, enc='utf-8'):

        if not os.path.isfile(filename):
            raise IOError('Could not find', filename)

        self.context_managed = False
        self._file = filename           # filename
        self._fhandle = None            # file handle
        self.lines = None               # line iterator
        self.buf = buf
        self.enc = enc

    def __enter__(self):
        self._fhandle = open(self._file, 'r', self.buf, self.enc)
        self.lines = (line for line in self._fhandle)
        self.context_managed = True
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        if exec_type is not None:
            print(exec_type, exec_value, traceback)
        if self._fhandle:
            self._fhandle.close()
        else:
            raise Exception('Improperly closed fhandle!')

    def apply(self, func, *args, **kwargs) -> Generator:
        """
        Apply function to lines from file
        
        :param func: Function that operates on string
        :param args: Optional arguments to func
        :param kwargs: Optional keyword arguments to func
        :return: Generator
        """
        if not self.context_managed:
            raise Exception('Object must be initialized with context manager')
        try:
            yield from (func(line, *args, **kwargs) for line in self.lines)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e)

    def mapfunc(self, func: Callable[[str], Any], *args, **kwargs) -> Generator:
        """
        Lazier version of apply using Python's map function

         :param func: Function that operates on string
         Use partialfunc to generate a partial function easily
         :return: Generator
         """
        if not self.context_managed:
            raise Exception('Object must be initialized with context manager')
        try:
            yield from map(func if not args else partial(fst_arg_last(func), *args, **kwargs),
                           self.lines)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e)

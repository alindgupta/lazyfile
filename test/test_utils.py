import lazyfile
from lazyfile import utils
import os

filename = os.path.join(os.path.dirname(__file__), 'text.txt')

def test_initialization():
    # no argument
    try:
        a = utils.Lazyfile()
        assert False
    except TypeError:
        assert True
    
    # no such file
    try:
        a = utils.Lazyfile('')
        assert False
    except OSError:
        assert True

    # no context manager
    try:
        a = utils.Lazyfile(filename)
        a.map_function(len)
        a.apply(len)
        assert False
    except:
        assert True

    # correct use
    with utils.Lazyfile(filename) as txt:
        print(txt.map_function(len))
    assert True
        

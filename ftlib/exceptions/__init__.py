from ._Exceptions import *


def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")
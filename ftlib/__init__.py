from ._Ftlib import Ftlib


from .projects import _Projects
from .cursus import _Cursus
from ._Constants import *
from .journal import _Journal
from .users import _Users
__all__ = ["Ftlib"]

def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")


def __dir__():
    return __all__
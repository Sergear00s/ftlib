from ._Cursus import Cursus

__all__ = ["Cursus"]

def __dir__():
    return __all__
def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")
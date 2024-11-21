from ._Projects import Projects

__all__ = ["Projects"]

def __dir__():
    return __all__
def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")
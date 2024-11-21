from ._Cursus import Cursus



def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")
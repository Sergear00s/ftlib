from ._Projects import Projects



def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")
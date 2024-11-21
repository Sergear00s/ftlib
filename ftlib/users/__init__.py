from ._Users import User

def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")
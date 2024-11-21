from ._Users import User
__all__ = ["Users", "User"]

def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")
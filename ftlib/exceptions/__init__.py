from ._Exceptions import *

__all__ = ["UserIdNotFound", "RateLimit", "Error_auth", "Error_response"]

def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")
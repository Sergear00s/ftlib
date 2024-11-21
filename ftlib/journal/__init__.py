from ._Journal import Journal

__all__ = ["Journal"]
def __dir__():
    return __all__
def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")
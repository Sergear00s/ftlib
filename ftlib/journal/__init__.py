from ._Journal import Journal

__all__ = ["Journal"]

def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")
from ._Journal import Journal


def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")
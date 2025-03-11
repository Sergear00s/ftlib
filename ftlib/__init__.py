from ._Ftlib import Ftlib
from .projects._Projects import Projects
from .cursus._Cursus import Cursus
from ._Constants import *
from .journal._Journal import Journal
from .users._Users import Users
from .api._Api import Api
from .wallet._Transaction import Transaction
from .campus._Campus import Campus
from .exam._Exam import Exam
from .candidatures._Candidatures import Candidatures
from .achivement._Achivement import Achivement
from .title import Title
from .quest import Quest
from .scale_teams import Scale_teams

__all__ = ("Ftlib")

def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")


def __dir__():
    return __all__
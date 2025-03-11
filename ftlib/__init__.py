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
from .evaluations import Evaluations
from .credentials._Credentials import Credentials


def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")



class ftlib:
    def __init__(self, creds : Credentials):
        self.Projects = Projects(creds)
        self.Cursus = Cursus(creds)
        self.Journal = Journal(creds)
        self.Users = Users(creds)
        self.Transaction = Transaction(creds)
        self.Campus = Campus(creds)
        self.Exam = Exam(creds)
        self.Candidatures = Candidatures(creds)
        self.Achivement = Achivement(creds)
        self.Title = Title(creds)
        self.Quest = Quest(creds)
        self.Scale_teams = Scale_teams(creds)
        self.Evaluations = Evaluations(creds)
        self.Credentials = creds
        self.Api = Api(creds)

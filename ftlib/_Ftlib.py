

import requests
import time
from .users._Users import Users
from .cursus._Cursus import Cursus
from .exceptions._Exceptions import Error_response, Error_auth, RateLimit
from .projects._Projects import Projects
from .journal._Journal import Journal
from .wallet._Transaction import Transaction
from .campus._Campus import Campus
from .exam._Exam import Exam
from .candidatures import Candidatures
from .achivement import Achivement
from .quest import Quest
from .api import Api

from ._Constants import CAMPUS_ISTANBUL




__all__ = ("Ftlib")
def __getattr__(name):
    raise AttributeError(f"{name} can't be imported")

def tokenizer(func):
    def wrapper(self, *args, **kwargs):
        self.tokener()
        return func(self, *args, **kwargs)
    return wrapper


class Ftlib():
    def __init__(self, intra_uid : str, intra_secret: str, scopes : str = "public projects forum profile elearning tig", campus_id : int = CAMPUS_ISTANBUL) -> None:
        """
            intra_uid: UID of APP
            intra_secret: Secret key of APP
            scopes: scopes
            campus_id: campus id
        """
        ##public
        self.Users = Users(self)
        self.Journal = Journal(self)
        self.Cursus = Cursus(self)
        self.Projects = Projects(self)
        self.Api = Api(self) 
        self.Transaction = Transaction(self)
        self.Candidatures = Candidatures(self)
        self.Campus = Campus(self)
        self.Quest = Quest(self)
        self.Exam = Exam(self)
        self.Achivement = Achivement(self)
        ##end public
        self.campus_id = campus_id
        self.secret = intra_secret
        self.__uid = intra_uid
        self.endpoint = "https://api.intra.42.fr"
        self.token = None
        self.header = None
        # if self.token is not None:
        #     self.header = {
        #         "Authorization": f"Bearer {self._grep_token()}"
        #     }
        self.scopes = scopes
        
    def tokener(self):
        if (self.token_check() is False):
            self.update_token()
            if (self.token_check() is False):
                raise ConnectionRefusedError("Token error")

    def _grep_token(self):
        if self.token:
            return self.token["access_token"]
        return None
    
    def update_token(self) -> dict:
        data = {"client_id": self.__uid, "client_secret":self.secret, "grant_type": "client_credentials", "scope":self.scopes}
        auth = self.endpoint + "/oauth/token"
        resp_json = {}
        resp = requests.post(auth, data=data)
        if (resp.status_code == 200):
            resp_json = resp.json()
        else:
           raise Exception(f"No token {resp}")
        self.token = resp_json
        self.update_header()
        return resp_json        

    def token_check(self) -> bool:
        if self.token is None:
            return False
        self.header = {
                "Authorization": f"Bearer {self.token['access_token']}"
        }
        resp = requests.get(self.endpoint + "/oauth/token/info", headers=self.header)
        if (resp.status_code == 200):
            return True
        return False

    def update_header(self):
         self.header = {
                "Authorization": f"Bearer {self.token['access_token']}"
        }


    def eval_resp(self, response):
        codes = [500, 400, 429, 401, 403, 404, 422]
        if (response.status_code == codes[0]):
            raise Error_response(f'{response, response.json()}')
        if (response.status_code == codes[1]):
            raise Error_auth(f'{response, response.json()}')
        if (response.status_code == codes[2]):
            raise RateLimit("RateLimit")
        if (response.status_code == codes[3]):
            raise Error_auth(f'{response, response.json()}')
        if (response.status_code in codes):
            raise Exception(f'{response, response.json()}')

        
        
    def format_page_resp(self, data : dict) -> dict:
        keyss = data.keys()
        for i in keyss:
            val = data[i].json()
            data[i] = val
        return data

    def extract(self, data : dict) -> list:
        keys = data.keys()
        rtn = []
        for i in keys:
            data_in = data[i]
            for x in data_in:
                rtn.append(x)
        return rtn
    
    def __str__(self) -> str:
        return self.token


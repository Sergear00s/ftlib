import requests
import time
from .Users import Users
from .journal import *
from .Exceptions import Error_response, Error_auth, RateLimit

def tokenizer(func):
    def wrapper(self, *args, **kwargs):
        self.tokener()
        return func(self, *args, **kwargs)
    return wrapper

class Ftlib():
    def __init__(self, intra_uid : str, intra_secret: str, scopes : str = "", campus_id : int = 49 ) -> None:

        ##public
        self.Users = Users(self)
        self.Journal = Journal(self)
        self.campus_id = campus_id
        ##end public
        self.secret = intra_secret
        self.__uid = intra_uid
        self.endpoint = "https://api.intra.42.fr"
        self.token = None
        self.header = None
        if self.token is not None:
            self.header = {
                "Authorization": f"Bearer {self._grep_token()}"
            }
        self.scopes = scopes

    def tokener(self):
        if (self.token_check() is False):
            self.update_token()

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
        codes = [500, 400, 429,401, 403, 404, 422]
        if (response.status_code == codes[0]):
            raise Error_response(f'{response, response.json()}')
        if (response.status_code == codes[1]):
            raise Error_auth(f'{response, response.json()}')
        if (response.status_code == codes[2]):
            raise RateLimit("RateLimit")
        
        
    @tokenizer
    def s_request(self, endpoint : str, headers=None, params=None, data=None, max_page : int = 250 ) -> list:
        items = []
        done = False
        params["page[size]"] = 100
        i = 1
        while i <= max_page + 1:
            if (done == True):
                break
            params["page[number]"] = i
            resp = requests.get(endpoint, headers=headers, params=params, data=data)
            try:
                self.eval_resp(resp)
            except RateLimit as e:
                time.sleep(1)
            except Exception as e:
                raise
            current = resp.json()
            items.append(current)
            size = int(int(resp.headers.get("X-Total")) // 100)
            if ((size) < i ):
                done = True
            i += 1
        return items


    def __str__(self) -> str:
        return self.token
        
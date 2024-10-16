import requests
import time
import threading
from .Users import Users
from .journal import *
from .Exceptions import Error_response, Error_auth

def tokenizer(func):
    def wrapper(self, *args, **kwargs):
        self.tokener()
        return func(self, *args, **kwargs)
    return wrapper

class ft_api():
    def __init__(self, intra_uid : str, intra_secret: str, scopes="", campus_id=49) -> None:

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

    def __th(self, args:list, rtn, func):
        resp = func(args[0], headers=args[1], params=args[2], data=args[3])
        rtn[args[4]] = resp

    @tokenizer
    def page_request(self, endpoint : str, headers=None, params=None, data=None, max_page : int = 100 ) -> list:
        items = []
        done = False
        params["page[size]"] = 100
        i = 0
        while i <= max_page + 1:
            time.sleep(1)
            if done:
                break
            ths = [0, 0, 0, 0, 0, 0, 0, 0]
            values = {}
            for x in range(8):
                values[x] = None
                params["page[number]"] = i
                ths[x] = threading.Thread(target=self.__th, args=[[endpoint, headers, params, data, x], values, requests.get])
                ths[x].start()
                i = i + 1
            for x in range(8):
                ths[x].join()
            for x in range(8):
                if (values[x] is not None and values[x].status_code == 200):
                    value = values[x].json()
                    if (value.__len__() <= 0):
                        done = True
                    items.append(value)
        return items
    

    def eval_resp(self, response):
        codes = [500, 400, 401, 403, 404, 422]
        if (response.status_code == codes[0]):
            raise Error_response(f'{response, response.json()}')
        if (response.status_code == codes[1]):
            raise Error_auth(f'{response, response.json()}')

    @tokenizer
    def s_request(self, endpoint : str, headers=None, params=None, data=None, max_page : int = 100 ) -> list:
        items = []
        done = False
        params["page[size]"] = 100
        i = 0
        cnt = 0
        while i <= max_page + 1:
            if (done == True):
                break
            if (i % 8 == 0):
                time.sleep(0.2)
            params["page[number]"] = i
            resp = requests.get(endpoint, headers=headers, params=params, data=data)
            try:
                self.eval_resp(resp)
            except Exception as e:
                if type(e) == Error_response:
                    cnt += 1
                    if (cnt > 15):
                        raise e
                    continue
                if (type(e) == Error_auth):
                    raise e 
            current = resp.json()
            for x in current:
                items.append(x)
            if current.__len__() <= 0:
                done == True
            i += 1
        return items

    def __str__(self) -> str:
        return str({"Conf": self.__config})
        
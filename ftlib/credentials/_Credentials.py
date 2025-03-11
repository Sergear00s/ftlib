import requests

class Credentials:
    def __init__(self, intra_uid : str, intra_secret: str, scopes : str = "public projects forum profile elearning tig") -> None:
        
        self.secret = intra_secret
        self.__uid = intra_uid
        self.endpoint = "https://api.intra.42.fr"
        self.token = None
        self.header = None
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
    
    def __str__(self) -> str:
        return self.token
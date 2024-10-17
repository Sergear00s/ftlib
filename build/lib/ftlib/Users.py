import requests
from .Exceptions import UserIdNotFound

class User:
    def __init__(self, data : dict, api) -> None:
        self.data = data
        self.__api = api
    def add_correction(self, reason: str,amount : int = 1):
        self.__api.tokener()
        resp : list = requests.post(f"{self.__api.endpoint}/v2/users/{self.login}/correction_points/add", headers=self.__api.header, data={"amount":amount, "reason":reason})
    def del_correction(self, reason:str, amount : int = 1):
        self.__api.tokener()
        resp : list = requests.delete(f"{self.__api.endpoint}/v2/users/{self.login}/correction_points/remove", headers=self.__api.header, data={"amount":amount, "reason":reason})

    def __getattr__(self, name):
        """['id', 'email', 'login', 'first_name', 'last_name', 'usual_full_name', 'usual_first_name', 'url', 'phone', 'displayname', 'kind', 'image', 'staff?', 'correction_point', 'pool_month', 'pool_year', 'location', 'wallet', 'anonymize_date', 'data_erasure_date', 'created_at', 'updated_at', 'alumnized_at', 'alumni?', 'active?']"""
        if name in self.data:
            return self.data[name]
        raise AttributeError(f"'User' object has no attribute '{name}'")
    def __str__(self) -> str:
        return str(self.data)


class Users:
    def __init__(self, api) -> None:
        self.__api = api

    def get_user_by_login(self, login : str) -> User:
        """
            login: user login,
            return value: user id
        """
        if (self.__api.token_check() is False):
            self.__api.update_token()
        params = {"filter[login]": login, "filter[primary_campus_id]": self.__api.campus_id}
        resp : list = self.__api.s_request(requests.get, f"{self.__api.endpoint}/v2/users", params=params, headers=self.__api.header)
        #resp = requests.get(f"{self.__api.endpoint}/v2/users", params=params, headers=self.__api.header)
        #self.__api.eval_resp(resp)
        try:
            jsn = resp.pop(0)
        except IndexError as e:
            raise UserIdNotFound
        except Exception as e:
            raise
        if (jsn and len(jsn)>0):
            return User(jsn[0], self.__api)
        raise UserIdNotFound
    
    
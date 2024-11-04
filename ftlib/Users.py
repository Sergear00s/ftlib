import requests
from .Exceptions import UserIdNotFound

class User:
    def __init__(self, data : dict, api) -> None:
        self.data = data
        self.cursus_data = None
        self.__api = api
    
    def add_correction(self, reason: str,amount : int = 1):
        self.__api.tokener()
        resp : list = requests.post(f"{self.__api.endpoint}/v2/users/{self.login}/correction_points/add", headers=self.__api.header, data={"amount":amount, "reason":reason})
    
    def del_correction(self, reason:str, amount : int = 1):
        self.__api.tokener()
        resp : list = requests.delete(f"{self.__api.endpoint}/v2/users/{self.login}/correction_points/remove", headers=self.__api.header, data={"amount":amount, "reason":reason})

    def show_freezes(self):
        self.__api.tokener()
        resp: list = requests.get()

    def __getattr__(self, name):
        """['id', 'email', 'login', 'first_name', 'last_name', 'usual_full_name', 'usual_first_name', 'url', 'phone', 'displayname', 'kind', 'image', 'staff?', 'correction_point', 'pool_month', 'pool_year', 'location', 'wallet', 'anonymize_date', 'data_erasure_date', 'created_at', 'updated_at', 'alumnized_at', 'alumni?', 'active?']"""
        if name in self.data:
            return self.data[name]
        if self.cursus_data and  name in self.cursus_data:
            return self.cursus_data[name]
        raise AttributeError(f"'User' object has no attribute '{name}'")
    
    def __str__(self) -> str:
        try:
            login = self.data
            return str(login)
        except:
            return ""
    def __repr__(self) -> str:
        return str(self.data)


class Users:
    def __init__(self, api) -> None:
        self.__api = api

    def get_user_by_login(self, login : str) -> User:
        """
            login: user login,
            return value: User()
        """
        params = {"filter[login]": login, "filter[primary_campus_id]": self.__api.campus_id}
        resp : list = self.__api.s_request(requests.get, f"{self.__api.endpoint}/v2/users", params=params, headers=self.__api.header)
        try:
            jsn = resp.pop(0)
        except IndexError as e:
            raise UserIdNotFound
        except Exception as e:
            raise e
        if (jsn):
            return User(jsn, self.__api)
        raise UserIdNotFound
    
    def get_users_by_logins(self, login_list : list) -> list:
        """
            login_list: list of logins
        """
        rtn = []
        params = {}
        params["filter[primary_campus_id]"] = self.__api.campus_id
        that_users = ""
        for i in login_list:
            that_users += "," + str(i)
        params["filter[login]"] = that_users
        resp : list = self.__api.s_request(requests.get, f"{self.__api.endpoint}/v2/campus/{self.__api.campus_id}/users", params=params, headers=self.__api.header)
        users = resp
        return users
    
    def get_campus_users(self):
        to = "/v2/cursus/:cursus_id/cursus_users"
        param = {
            "filter[campus_id]":self.__api.campus_id
        }
        resp : list = self.__api.s_request(requests.get, f"{self.__api.endpoint}/v2/campus/{self.__api.campus_id}/users", headers=self.__api.header)
        users = []
        for i in resp:
            users.append(User(i, self.__api))
        users_ = ""
        for i in users:
            users_ += "," + i.login
        param["filter[user_id]"] = users_
        resp_cursus : list = self.__api.s_request(requests.get, f"{self.__api.endpoint}/v2/cursus/{21}/cursus_users", headers=self.__api.header, params=param)
        for i in resp_cursus:
            ids = i["id"]
            for x in users:
                if (x.id == ids):
                    x.cursus_data = i
        return users